"""verify_label: the rule-based guardrail between the LLM and the score (course requirement #7).

Principle: rather miss a real use than claim one the filing does not support. A label reaches
the score only if its quote is found word for word in the source passage. The checks are plain
rules, not another LLM, so they are explainable and unit-tested.

Status values
  pass          label unchanged, counted in the score
  downgraded    label weakened by a rule (D2 -> D1, stray scenarios removed), still counted
  needs_review  not counted: evidence set to N and scenarios cleared for scoring; the model's
                original call stays in evidence_raw / scenarios_raw for a person to check
"""
import re
import unicodedata

from src.agent import config
from src.nlp.taxonomy_v0 import ALL_SCENARIOS, EVIDENCE, TOPICS

USE_LEVELS = {"D2", "D1", "P"}
# Words that never count as the "specific" item behind a D2 label
GENERIC = {"ai", "artificial intelligence", "machine learning", "generative ai", "genai", "models", "model",
           "technology", "technologies", "tools", "tool", "data", "automation", "algorithms", "analytics",
           "llm", "llms", "we", "our", "the company"}


def normalize(s: str) -> str:
    """Compare text the way a careful reader would: same words, ignoring curly quotes, dash style,
    non-breaking spaces and runs of whitespace. Case is kept."""
    s = unicodedata.normalize("NFKC", s or "")
    s = (s.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
          .replace("–", "-").replace("—", "-").replace(" ", " "))
    return re.sub(r"\s+", " ", s).strip()


def quote_in_source(quote: str, source: str) -> bool:
    """True if the quote appears in the source word for word. A quote may skip text with '...';
    then every fragment must appear, in order."""
    q, src = normalize(quote), normalize(source)
    if not q:
        return False
    frags = [f.strip(" .,;:") for f in re.split(r"\.\.\.|…", q) if f.strip(" .,;:")]
    if not frags or any(len(f) < 8 for f in frags):
        return False
    pos = 0
    for f in frags:
        i = src.find(f, pos)
        if i < 0:
            return False
        pos = i + len(f)
    return True


def _split_codes(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        value = re.split(r"[;,\s]+", value)
    return [str(v).strip().upper() for v in value if str(v).strip()]


def verify_label(label: dict, source_text: str, min_confidence: float = config.MIN_CONFIDENCE) -> dict:
    """Check one label against its source passage. Pure function: no I/O, no LLM.

    `label` needs: evidence, scenarios (list or ';' string), topic, quote, specific, confidence.
    Returns a new dict with the checked evidence/scenarios plus evidence_raw, scenarios_raw,
    verify_status and verify_reason.
    """
    ev_raw = str(label.get("evidence", "")).strip().upper()
    scen_raw = _split_codes(label.get("scenarios"))
    topic = str(label.get("topic", "")).strip().upper()
    quote = label.get("quote") or ""
    specific = label.get("specific")
    try:
        conf = float(label.get("confidence", 0))
    except (TypeError, ValueError):
        conf = 0.0
    flags = [str(f) for f in (label.get("flags") or [])]

    out = dict(label)
    out.update(evidence_raw=ev_raw, scenarios_raw=";".join(scen_raw))
    ev, scen, notes = ev_raw, list(scen_raw), []

    def review(reason):
        out.update(evidence="N", scenarios=[], topic=topic if topic in TOPICS else "",
                   verify_status="needs_review", verify_reason=reason)
        return out

    # 1. Codes must exist in the codebook
    if ev not in EVIDENCE:
        return review(f"unknown evidence level {ev_raw!r}")
    bad = [s for s in scen if s not in ALL_SCENARIOS]
    if bad:
        return review(f"unknown scenario code(s) {bad}")
    if topic and topic not in TOPICS:
        return review(f"unknown topic {topic!r}")

    # 2. Attribution: a label for the wrong company never counts
    if "company_mismatch" in flags and ev in USE_LEVELS:
        return review("model flagged a company mismatch but still claimed use")

    if ev in USE_LEVELS:
        # 3. Every use claim needs a quote that exists in the source
        if not quote_in_source(quote, source_text):
            return review("quote not found word for word in the source passage")
        # 4. Use claims need a scenario (codebook rule)
        if not scen:
            return review(f"{ev} label has no scenario")
        # 5. D2 must name something specific that sits inside the quote
        if ev == "D2":
            sp = normalize(specific or "")
            if not sp or sp.lower() in GENERIC or sp not in normalize(quote):
                ev = "D1"
                notes.append("D2 -> D1: no specific tool, number, body, role or date in the quote")
        # 6. Low confidence goes to a person
        if conf < min_confidence:
            return review(f"confidence {conf:.2f} below {min_confidence:.2f}")
    else:
        # 7. N and X carry no scenarios
        if scen:
            scen = []
            notes.append(f"{ev} cannot carry scenarios; removed")

    out.update(evidence=ev, scenarios=scen, topic=topic,
               verify_status="downgraded" if notes else "pass",
               verify_reason="; ".join(notes) if notes else "ok")
    return out
