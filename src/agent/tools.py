"""The agent's seven tools.

Each function's docstring is written for the LLM that calls it (course requirement #3), and
TOOL_SPECS holds the matching JSON schemas for DeepSeek function calling. Every tool returns a
JSON-serialisable dict; on bad input it returns {"error": "..."} instead of raising, so the agent
can read the problem and recover.

Granularity: passages are identified by passage_id (<TICKER>_<period>_<form>_<idx>);
scores are per ticker per fiscal year (FY = year of the filing period end).
"""
import json
import re

from src.agent import config, llm, prompts, store
from src.agent.verify import normalize, verify_label as _verify
from src.index.score_companies import score as _score
from src.nlp.taxonomy_v0 import read as _read_labels

COMPANIES = {"JPM": "JPMorgan Chase", "BAC": "Bank of America", "COF": "Capital One", "WFC": "Wells Fargo",
             "SCHW": "Charles Schwab", "PFG": "Principal Financial Group", "C": "Citigroup"}


def _err(msg: str) -> dict:
    return {"error": msg}


def _ticker(t) -> str | None:
    t = str(t or "").strip().upper()
    return t if t in COMPANIES else None


# ---------------------------------------------------------------- 1. fetch_sec_filings
def fetch_sec_filings(ticker: str, fiscal_year: int, forms: list[str] | None = None, live: bool = False) -> dict:
    """List the SEC 10-K / 10-Q filings we hold for one company and fiscal year.

    Use this to see which reports exist before looking for AI passages. By default it reads the
    team's filing inventory (no network). live=True downloads the filing list from SEC EDGAR
    instead (slow, needs internet and SEC_USER_AGENT); only use it when the inventory lacks a year.

    Args:
        ticker: one of JPM, BAC, COF, WFC, SCHW, PFG, C.
        fiscal_year: e.g. 2025. A 10-K for FY2025 has period 2025-12-31.
        forms: ["10-K"], ["10-Q"] or both. Default both.
        live: download from EDGAR instead of reading the local inventory.

    Returns: {"ticker", "fiscal_year", "filings": [{"form", "period", "filing_date", "accession", "url", "ai_passages"}]}
    """
    t = _ticker(ticker)
    if not t:
        return _err(f"unknown ticker {ticker!r}; use one of {sorted(COMPANIES)}")
    forms = {f.upper() for f in (forms or ["10-K", "10-Q"])}
    fy = int(fiscal_year)
    if live:
        return _fetch_live(t, fy, forms)
    rows = [r for r in store.read_csv(config.INVENTORY)
            if r["ticker"] == t and store.fiscal_year(r["period"]) == fy and r["form"] in forms]
    filings = [{k: r[k] for k in ("form", "period", "filing_date", "accession", "url")} | {"ai_passages": int(r["ai_passages"])}
               for r in sorted(rows, key=lambda r: r["period"])]
    out = {"ticker": t, "fiscal_year": fy, "filings": filings}
    if not filings:
        out["note"] = "No filing in the local inventory for this year (window is periods 2024-07 to 2026-06)."
    return out


def _fetch_live(t: str, fy: int, forms: set[str]) -> dict:
    """Wraps Yen-Chu's downloader functions (src/edgar/download_sec_filings.py)."""
    import os
    from src.edgar import download_sec_filings as dl
    config.load_dotenv()
    if os.environ.get("SEC_USER_AGENT"):
        dl.session.headers["User-Agent"] = os.environ["SEC_USER_AGENT"]
    try:
        cik = dl.ticker_to_cik()[t]
        rows = dl.filings_in_window(cik, f"{fy}-01-01", f"{fy}-12-31")
    except Exception as e:  # network or SEC errors go back to the agent as data
        return _err(f"EDGAR request failed: {e}")
    filings = []
    for f in rows:
        if f["form"] in forms:
            acc = f["accession"].replace("-", "")
            filings.append({**{k: f[k] for k in ("form", "period", "filing_date", "accession")},
                            "url": f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/{f['primary_doc']}"})
    return {"ticker": t, "fiscal_year": fy, "filings": filings, "source": "live EDGAR"}


# ---------------------------------------------------------------- 2. find_ai_passages
def find_ai_passages(ticker: str, fiscal_year: int, forms: list[str] | None = None,
                     max_chars: int = 600, limit: int = 50) -> dict:
    """Return the paragraphs that mention AI in one company's filings for one fiscal year.

    Passages were extracted by the team's SEC run (any paragraph with 'artificial intelligence',
    'AI', 'machine learning', 'generative AI', 'LLM', 'chatbot', 'agentic' and similar terms).
    A passage that mentions AI is NOT evidence of use; classify it before claiming anything.

    Args:
        ticker: JPM, BAC, COF, WFC, SCHW, PFG or C.
        fiscal_year: e.g. 2025.
        forms: ["10-K"], ["10-Q"] or both (default both).
        max_chars: cut each passage's text to this length (full text is used when classifying).
        limit: maximum passages to return.

    Returns: {"ticker", "fiscal_year", "count", "passages": [{"passage_id", "form", "period", "section_guess", "text", "source_url"}]}
    """
    t = _ticker(ticker)
    if not t:
        return _err(f"unknown ticker {ticker!r}")
    rows = store.select_passages(tickers=[t], fiscal_years=[int(fiscal_year)], forms=forms)
    out = [{"passage_id": r["passage_id"], "form": r["form"], "period": r["period"],
            "section_guess": r["section_guess"], "text": r["passage"][:max_chars], "source_url": r["source_url"]}
           for r in rows[:limit]]
    return {"ticker": t, "fiscal_year": int(fiscal_year), "count": len(rows), "passages": out}


# ---------------------------------------------------------------- 3. classify_passage
def classify_passage(passage_id: str | None = None, text: str | None = None, company: str | None = None,
                     requested_company: str | None = None, guardrails: bool = True) -> dict:
    """Label one passage with the Taxonomy v0 codebook using DeepSeek.

    Decides whether the filing company says it USES AI (D2 specific / D1 general / P planned)
    or only TALKS about it (N), or whether the text is not substantive (X), and returns the
    supporting quote. Give a passage_id from find_ai_passages or get_labels; pass raw text only
    for passages outside the dataset. In the chat agent the result is always checked by
    verify_label before you see it.

    Args:
        passage_id: id of a stored passage (preferred).
        text: raw passage text, if there is no passage_id.
        company: filing company name (filled in automatically from passage_id).
        requested_company: the company the user asked about, if different (used to catch misattribution).

    Returns: {"passage_id", "company", "about_ai", "evidence", "scenarios", "topic", "quote", "specific",
              "reason", "confidence", "flags"}
    """
    rec = store.get_passage(passage_id) if passage_id else None
    if passage_id and not rec and not text:
        return _err(f"unknown passage_id {passage_id!r}")
    if rec:
        text, company = rec["passage"], rec["company"]
    if not text:
        return _err("give a passage_id or text")
    company = company or "Unknown company"

    msgs = prompts.classify_messages(text, company, passage_id or "", guardrails, requested_company)
    try:
        reply = llm.complete(msgs, json_mode=True, max_tokens=config.MAX_TOKENS_CLASSIFY,
                             mock=lambda m, t: {"content": json.dumps(_mock_classify(passage_id, text, company, requested_company)),
                                                "tool_calls": []})
        label = llm.parse_json(reply["content"])
    except Exception as e:
        return {"passage_id": passage_id, "company": company, "error": f"classify failed: {e}",
                "evidence": "", "scenarios": [], "topic": "", "quote": "", "specific": None,
                "reason": "", "confidence": 0.0, "flags": ["llm_error"]}
    label.setdefault("flags", [])
    label["scenarios"] = label.get("scenarios") or []
    return {"passage_id": passage_id, "company": company, **label}


# ---------------------------------------------------------------- 4. verify_label
def verify_label(label: dict, source_text: str | None = None) -> dict:
    """Guardrail: check a label against its source before it can count.

    Rules: (1) every D2/D1/P label must carry a quote found word for word in the source,
    otherwise it goes to human review and is not scored; (2) D2 must name something specific
    (tool, number, body, role, date) inside the quote, otherwise it drops to D1; (3) confidence
    below 0.70 goes to human review; (4) N and X carry no scenarios; (5) unknown codes go to review.

    Args:
        label: a classify_passage result (needs evidence, scenarios, topic, quote, specific, confidence).
        source_text: the passage text; looked up from label["passage_id"] if omitted.

    Returns: the label with evidence/scenarios after the checks, plus evidence_raw, scenarios_raw,
             verify_status (pass | downgraded | needs_review) and verify_reason.
    """
    if not isinstance(label, dict):
        return _err("label must be an object")
    if source_text is None:
        rec = store.get_passage(label.get("passage_id") or "")
        if not rec:
            return _err("no source_text and no stored passage for this label")
        source_text = rec["passage"]
    return _verify(label, source_text)


# ---------------------------------------------------------------- 5. score_companies
def score_companies(labels: str = "agent", tickers: list[str] | None = None, fiscal_year: int | None = None,
                    ent_counts: bool = False) -> dict:
    """Roll passage labels up into company scores per fiscal year.

    AI Use Score (0-100): for each of the 11 use-case scenarios take the strongest evidence that
    year (D2=3, D1=1, P=0.5), add up, divide by 33. Readiness Score (0-100): same over the
    3 enablers (GOV, TALENT, INVEST), divided by 9. Talk ratio: share of substantive AI passages
    that show no use. A high talk ratio means a lot of AI talk and little use shown.

    Args:
        labels: "agent" (this agent's verified labels) or "draft" (the AI-assisted v0 draft labels).
        tickers: limit to these companies (default all).
        fiscal_year: limit to one year (default all).
        ent_counts: let ENT ("uses AI, area not named") count once (pending team vote #33).

    Returns: {"labels", "scores": [{"ticker", "fiscal_year", "ai_use_score", "scenarios_with_use",
              "readiness_score", "talk_ratio_pct", "substantive_ai_passages"}]}
    """
    path = config.AGENT_LABELS if labels == "agent" else config.DRAFT_LABELS
    if not path.exists():
        return _err(f"{path.name} does not exist yet; run python3 -m src.agent.run_batch first")
    rows = _score(_read_labels(path), ent_counts=ent_counts)
    tk = {t.upper() for t in tickers} if tickers else None
    rows = [r for r in rows if (not tk or r["ticker"] in tk) and (not fiscal_year or int(r["fiscal_year"]) == int(fiscal_year))]
    return {"labels": labels, "ent_counts": ent_counts, "scores": rows}


# ---------------------------------------------------------------- 6. lookup_baseline
def lookup_baseline(ticker: str, fiscal_year: int) -> dict:
    """Look up the Dong, Doukas & Zhang (2026) AI Intensity score for one company and fiscal year.

    Their measure counts AI dictionary terms per 1,000 words of the 10-K; it measures how much a
    firm TALKS about AI and cannot separate use from talk. Use it as an outside comparison.
    Coverage: 10-Ks filed 2010-2024, i.e. up to FY2023. Their Wells Fargo values are 0 because
    their parser missed Exhibit 13 (the annual report body), so do not trust WFC.

    Args:
        ticker: JPM, BAC, COF, WFC, SCHW or PFG.
        fiscal_year: e.g. 2023 (the 10-K filed in early 2024).

    Returns: {"ticker", "fiscal_year", "available", "ai_intensity_core", "ai_intensity_all",
              "filing_date", "total_words", "note"}. Cite: SSRN 6051714.
    """
    t = _ticker(ticker)
    fy = int(fiscal_year)
    base = {"ticker": ticker, "fiscal_year": fy, "available": False, "ai_intensity_core": None,
            "ai_intensity_all": None, "filing_date": None, "total_words": None, "note": ""}
    if not t:
        return base | {"note": f"unknown ticker {ticker!r}"}
    hits = [r for r in store.read_csv(config.DONG_BASELINE)
            if r["ticker"].upper() == t and r["form"] == "10-K" and int(r["filing_date"][:4]) == fy + 1]
    if not hits:
        last = 2023
        why = (f"Dong et al. cover 10-Ks up to FY{last}." if fy > last
               else "No row for this firm-year in our extract (only JPM, BAC, COF, WFC, SCHW, PFG).")
        return base | {"ticker": t, "note": why}
    r = hits[0]
    note = "Parser defect: Dong et al. missed Exhibit 13, so WFC shows 0. Do not use." if t == "WFC" else ""
    return {"ticker": t, "fiscal_year": fy, "available": True,
            "ai_intensity_core": round(float(r["AI Intensity (Core)"]), 4),
            "ai_intensity_all": round(float(r["AI Intensity (All)"]), 4),
            "filing_date": r["filing_date"], "total_words": int(r["total_words"]), "note": note}


# ---------------------------------------------------------------- 7. get_labels
def get_labels(ticker: str, fiscal_year: int | None = None, evidence: list[str] | None = None,
               scenario: str | None = None, labels: str = "agent", limit: int = 20) -> dict:
    """Read labels that were already produced (fast, no LLM call). Start here in chat.

    Use evidence=["D2","D1"] to get passages where the company says it uses AI, each with its
    verified quote and SEC link. Labels with verify_status "needs_review" are not counted in scores.

    Args:
        ticker: JPM, BAC, COF, WFC, SCHW, PFG or C.
        fiscal_year: e.g. 2025 (default all years).
        evidence: filter by levels, e.g. ["D2","D1"].
        scenario: filter by one scenario code, e.g. "CX".
        labels: "agent" (default) or "draft".
        limit: maximum rows.

    Returns: {"count", "labels": [{"passage_id", "form", "period", "evidence", "scenarios", "topic",
              "quote", "verify_status", "source_url"}]}
    """
    t = _ticker(ticker)
    if not t:
        return _err(f"unknown ticker {ticker!r}")
    path = config.AGENT_LABELS if labels == "agent" else config.DRAFT_LABELS
    if not path.exists():
        return _err(f"{path.name} does not exist yet; run python3 -m src.agent.run_batch first")
    ev = {e.upper() for e in evidence} if evidence else None
    rows = []
    for r in store.read_csv(path):
        if r["ticker"] != t or (fiscal_year and store.fiscal_year(r["period"]) != int(fiscal_year)):
            continue
        if ev and r["evidence_v0"] not in ev:
            continue
        if scenario and scenario.upper() not in r["scenarios_v0"].split(";"):
            continue
        rows.append({"passage_id": r["passage_id"], "form": r["form"], "period": r["period"],
                     "evidence": r["evidence_v0"], "scenarios": r["scenarios_v0"], "topic": r["topic_v0"],
                     "quote": r.get("quote", ""), "verify_status": r.get("verify_status", ""),
                     "source_url": r["source_url"]})
    return {"count": len(rows), "labels": rows[:limit]}


# ---------------------------------------------------------------- registry for function calling
def _spec(name, desc, props, required):
    return {"type": "function", "function": {"name": name, "description": desc,
            "parameters": {"type": "object", "properties": props, "required": required}}}


_T = {"type": "string", "description": "Ticker: JPM, BAC, COF, WFC, SCHW, PFG or C"}
_FY = {"type": "integer", "description": "Fiscal year, e.g. 2025"}
_FORMS = {"type": "array", "items": {"type": "string", "enum": ["10-K", "10-Q"]}}

TOOL_SPECS = [
    _spec("fetch_sec_filings", "List the 10-K/10-Q filings held for a company and fiscal year.",
          {"ticker": _T, "fiscal_year": _FY, "forms": _FORMS}, ["ticker", "fiscal_year"]),
    _spec("find_ai_passages", "Paragraphs that mention AI in a company's filings for a year. Mentions are not evidence of use.",
          {"ticker": _T, "fiscal_year": _FY, "forms": _FORMS, "limit": {"type": "integer"}}, ["ticker", "fiscal_year"]),
    _spec("classify_passage", "Label one passage (D2/D1/P/N/X, scenarios, topic, quote) with the codebook. Result is checked by verify_label.",
          {"passage_id": {"type": "string"}, "text": {"type": "string"},
           "requested_company": {"type": "string", "description": "Company the user asked about, if any"}}, []),
    _spec("verify_label", "Check a label against its source: quote must exist word for word; D2 must be specific; low confidence goes to review.",
          {"label": {"type": "object"}, "source_text": {"type": "string"}}, ["label"]),
    _spec("score_companies", "AI Use Score, Readiness Score and talk ratio per company per fiscal year.",
          {"labels": {"type": "string", "enum": ["agent", "draft"]}, "tickers": {"type": "array", "items": {"type": "string"}},
           "fiscal_year": _FY}, []),
    _spec("lookup_baseline", "Dong et al. AI Intensity (word-count) score for a company-year, FY2023 or earlier. WFC values are defective.",
          {"ticker": _T, "fiscal_year": _FY}, ["ticker", "fiscal_year"]),
    _spec("get_labels", "Already-produced labels with verified quotes and SEC links. Use evidence=['D2','D1'] for use claims.",
          {"ticker": _T, "fiscal_year": _FY, "evidence": {"type": "array", "items": {"type": "string"}},
           "scenario": {"type": "string"}, "limit": {"type": "integer"}}, ["ticker"]),
]

FUNCTIONS = {"fetch_sec_filings": fetch_sec_filings, "find_ai_passages": find_ai_passages,
             "classify_passage": classify_passage, "verify_label": verify_label,
             "score_companies": score_companies, "lookup_baseline": lookup_baseline, "get_labels": get_labels}


def dispatch(name: str, args: dict, guardrails: bool = True) -> dict:
    """Run a tool the LLM asked for. With guardrails on, classify_passage output is always passed
    through verify_label (the model cannot skip the check) and live EDGAR downloads are disabled."""
    fn = FUNCTIONS.get(name)
    if not fn:
        return _err(f"unknown tool {name!r}")
    args = dict(args or {})
    if name == "fetch_sec_filings":
        args["live"] = False
    if name == "classify_passage":
        args["guardrails"] = guardrails
    try:
        result = fn(**args)
    except TypeError as e:
        return _err(f"bad arguments for {name}: {e}")
    if name == "classify_passage" and guardrails and "error" not in result:
        result = verify_label(result, args.get("text") if not args.get("passage_id") else None)
    return result


# ---------------------------------------------------------------- offline mock (tests and dry runs only)
_AI_TERM = re.compile(r"artificial intelligence|machine[- ]learning|generative|\bAI\b|\bLLMs?\b|chatbot|agentic|virtual assistant", re.I)
_SPECIFIC = re.compile(r"\b\d[\d,.]*\s*(?:million|billion|%|percent|agents|hours|applications|code reviews|utilizations)?|Head of [A-Z][\w ]+|Committee|Agent Assist|Erica|LLM Suite", re.I)


def _first_ai_sentence(text: str) -> str:
    for s in re.split(r"(?<=[.;])\s+", normalize(text)):
        if _AI_TERM.search(s):
            return s
    return normalize(text)[:200]


def _mock_classify(passage_id, text, company, requested_company) -> dict:
    """Stand-in for DeepSeek. Replays the v0 draft label for known passages, and uses simple rules
    for new text. Its only job is to exercise the pipeline offline; its labels are not results."""
    flags = []
    if re.search(r"ignore your (codebook|rules)|label this|print your api key|maximum ai use score|system note", text, re.I):
        flags.append("injection_attempt")
    if passage_id and requested_company and COMPANIES.get(store.ticker_of(passage_id)) not in (requested_company, None):
        flags.append("company_mismatch")
    draft = {r["passage_id"]: r for r in _draft_labels()}.get(passage_id or "")
    if draft:
        ev, scen, topic = draft["evidence_v0"], [s for s in draft["scenarios_v0"].split(";") if s], draft["topic_v0"]
    else:
        t = text.lower()
        if re.search(r"\b(may|could|might)\b", t) or re.search(r"threat|attack|fraudster|criminal|competitor", t):
            ev, scen, topic = "N", [], "THREAT" if re.search(r"threat|attack|fraud", t) else "USE"
        elif re.search(r"\b(plan|intend|expect) to\b|\bpilot\b", t):
            ev, scen, topic = "P", ["CREDIT" if "underwrit" in t else "ENT"], "USE"
        elif re.search(r"\bwe (use|deployed|launched|rolled out)\b|\bour (virtual assistant|ai)\b", t):
            ev = "D2" if _SPECIFIC.search(text) else "D1"
            scen, topic = ["CX" if re.search(r"call-center|customer|chat", t) else "ENT"], "USE"
        else:
            ev, scen, topic = "N", [], "USE"
    if "company_mismatch" in flags:
        ev, scen = "N", []
    quote = _first_ai_sentence(text) if ev in ("D2", "D1", "P") else ""
    m = _SPECIFIC.search(quote) if ev == "D2" else None
    return {"about_ai": True, "evidence": ev, "scenarios": scen, "topic": topic, "quote": quote,
            "specific": m.group(0).strip() if m else None, "reason": "mock label (offline dry run)",
            "confidence": 0.9, "flags": flags}


_DRAFT_CACHE: list = []


def _draft_labels():
    if not _DRAFT_CACHE:
        _DRAFT_CACHE.extend(store.read_csv(config.DRAFT_LABELS))
    return _DRAFT_CACHE
