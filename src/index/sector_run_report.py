"""Report on the S&P 500 Financials run (#133): coverage, labels and scores by firm type.

Reads the files the run writes (src/edgar/download_sector.py, then src/agent/run_batch.py with
--passages) and writes:
    docs/part6-agent/sp500_financials_run.md                  the report
    data/processed/sec/sp500_financials/review_queue.csv      labels the guardrail held for a person

The index preview uses Yen-Chu's src/index/sector_index.build() on the agent's scores, every firm
in the list (Citi is a constituent here, not a benchmark). It is a preview: the index itself is
#134, and the new firm types are not validated yet (labeling round 3, the sector pilot).

Run from the repo root:  python3 -m src.index.sector_run_report
"""
import argparse
import csv
import json
import statistics
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

from src.index import sector_index

DIR = Path("data/processed/sec/sp500_financials")
PASSAGES = Path("data/interim/sec/sp500_financials/ai_passages.csv")
OUT_MD = Path("docs/part6-agent/sp500_financials_run.md")
REVIEW_FIELDS = ["passage_id", "company", "ticker", "firm_type", "form", "period", "evidence_raw", "scenarios_raw",
                 "confidence", "verify_reason", "quote", "passage", "source_url",
                 "review_evidence", "review_scenarios", "reviewer", "review_note"]
TYPE_ORDER = ["bank", "insurer", "asset_mgmt_broker", "payments_consumer_finance", "exchange_data", "other"]
TYPE_NAME = {"bank": "Banks", "insurer": "Insurers (incl. brokers, Berkshire)",
             "asset_mgmt_broker": "Asset managers and brokers", "payments_consumer_finance": "Payments and consumer finance",
             "exchange_data": "Exchanges and data", "other": "Other"}
# DeepSeek deepseek-flash, per 1M tokens, off-peak (peak = 2x); docs/part6-agent/agent_design.md (checked Oct 23)
PRICE = {"hit": 0.003, "miss": 0.15, "out": 0.60}
USE = {"D2", "D1"}


def read(path: Path) -> list[dict]:
    if not Path(path).exists():
        return []
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def read_json(path: Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8")) if Path(path).exists() else {}


def cost(usage: dict) -> float:
    miss = usage.get("prompt_tokens", 0) - usage.get("cached_prompt_tokens", 0)
    return (usage.get("cached_prompt_tokens", 0) * PRICE["hit"] + miss * PRICE["miss"]
            + usage.get("completion_tokens", 0) * PRICE["out"]) / 1e6


def pct(k: int, n: int) -> str:
    return f"{k} ({k / n:.0%})" if n else "–"


def table(head: list[str], rows: list[list]) -> list[str]:
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return out


def build(d: Path = DIR, passages_path: Path = PASSAGES, today: str | None = None) -> tuple[str, list[dict]]:
    firms = read(d / "firms.csv")
    ftype = {f["ticker"]: f["firm_type"] for f in firms}
    inv = read(d / "filings_inventory.csv")
    info = read_json(d / "download_info.json")
    passages = read(passages_path)
    labels = read(d / "agent_labels.csv")
    scores = read(d / "agent_scores.csv")
    run = read_json(d / "agent_run_info.json")
    floats = read(d / "public_float.csv")
    years = sorted({r["fiscal_year"] for r in inv if r["form"] == "10-K"})
    types = [t for t in TYPE_ORDER if any(f["firm_type"] == t for f in firms)]
    text = {p["passage_id"]: p["passage"] for p in passages}

    md = ["# S&P 500 Financials run: AI passages, agent labels and scores (#133)", "",
          f"> **Generated** {today or date.today().isoformat()} by `python3 -m src.index.sector_run_report`. "
          "**Status: draft.** The agent was tuned and checked on banks (check 3: 81% exact on 48 unseen passages, "
          "0 overclaims); the other firm types are checked in [labeling round 3](../part3-metrics/labeling_round_3/) "
          "before their scores are trusted. Labels the guardrail held count as no use until a person reviews them "
          "([review queue](../../data/processed/sec/sp500_financials/review_queue.csv)).", ""]
    src = firms[0] if firms else {}
    md += [f"- **Firms:** {len(firms)} S&P 500 Financials constituents, from {src.get('source', '?')}, snapshot "
           f"{src.get('source_date', '?')} ([firms.csv](../../data/processed/sec/sp500_financials/firms.csv)).",
           f"- **Filings:** {', '.join(info.get('forms', ['10-K']))}s"
           + (f" with periods {' to '.join(info['window'])}" if info.get("window") else "")
           + f" (fiscal years {', '.join(years) or '?'}; FY = year the fiscal year ends). Same paragraph search as "
           "the 7-firm data (check 1).",
           f"- **Agent:** {run.get('model', '?')}, prompt `{run.get('prompt_version', '?')}`, guardrails "
           f"{'on' if run.get('guardrails', True) else 'off'}, confidence bar {run.get('min_confidence', 0.7)}.", ""]

    # coverage
    md += ["## Coverage by firm type", ""]
    rows = []
    for t in types + ["**All**"]:
        sel = (lambda tk: ftype.get(tk) == t) if t != "**All**" else (lambda tk: True)
        n_f = sum(1 for f in firms if sel(f["ticker"]))
        tk = [r for r in inv if r["form"] == "10-K" and sel(r["ticker"]) and r["status"].startswith("ok")]
        per_year = " / ".join(str(sum(1 for r in tk if r["fiscal_year"] == y)) for y in years)
        ps = [p for p in passages if sel(p["ticker"])]
        fl = sum(1 for r in floats if sel(r["ticker"]) and r["fiscal_year"] in years)
        mean = round(len(ps) / len(tk), 1) if tk else "–"
        rows.append([TYPE_NAME.get(t, t), n_f, per_year, len(ps), mean, fl])
    md += table(["Firm type", "Firms", f"10-Ks ({' / '.join('FY' + y for y in years)})", "AI passages",
                 "Per 10-K", "Public floats"], rows) + [""]
    probs = info.get("problems", [])
    if probs:
        md += [f"**Problems in the download ({len(probs)}):**", ""]
        md += [f"- {p['ticker']} [{p['where']}]: {p['problem']}" for p in probs[:60]]
        if len(probs) > 60:
            md.append(f"- … {len(probs) - 60} more in `download_info.json`")
        md.append("")
    off = info.get("fiscal_year_end_not_december") or {}
    if off:
        md += ["Fiscal years not ending in December (FY = the year it ends): "
               + ", ".join(f"{t} ({v[:2]}/{v[2:]})" for t, v in sorted(off.items())) + ".", ""]

    # labels
    held = [r for r in labels if r.get("verify_status") == "needs_review"]
    if labels:
        md += ["## Agent labels by firm type", "",
               "Use = D2 or D1 after the guardrail. *Use with no named area* = use labels whose only area is ENT; "
               "a high share hints that our 11 areas don't fit that firm type.", ""]
        rows = []
        for t in types + ["**All**"]:
            ls = [r for r in labels if t == "**All**" or ftype.get(r["ticker"]) == t]
            ev = Counter(r["evidence_v0"] for r in ls)
            use = [r for r in ls if r["evidence_v0"] in USE]
            ent_only = sum(1 for r in use if set(filter(None, r["scenarios_v0"].split(";"))) <= {"ENT"})
            h = sum(1 for r in ls if r.get("verify_status") == "needs_review")
            rows.append([TYPE_NAME.get(t, t), len(ls), pct(len(use), len(ls)), ev["D2"], ev["D1"], ev["P"], ev["N"],
                         ev["X"], pct(h, len(ls)), pct(ent_only, len(use))])
        md += table(["Firm type", "Passages", "Use", "D2", "D1", "P", "N", "X", "Held for review",
                     "Use with no named area"], rows) + [""]
        area = defaultdict(Counter)
        for r in labels:
            if r["evidence_v0"] in USE | {"P"}:
                for s in filter(None, r["scenarios_v0"].split(";")):
                    area[ftype.get(r["ticker"], "other")][s] += 1
        md += ["**Most-used areas** (D2/D1/P labels):", ""]
        md += [f"- {TYPE_NAME.get(t, t)}: " + (", ".join(f"{s} {k}" for s, k in area[t].most_common(5)) or "none")
               for t in types] + [""]

    # scores
    if scores:
        md += ["## AI Use Scores by firm type", "", "Mean (median) per fiscal year; firms with no substantive AI "
               "passage have no score row and count as 0 in the index.", ""]
        by = defaultdict(list)
        for s in scores:
            by[(ftype.get(s["ticker"], "other"), s["fiscal_year"])].append(float(s["ai_use_score"]))
        rows = []
        for t in types:
            cells = []
            for y in years:
                v = by.get((t, y), [])
                cells.append(f"{statistics.mean(v):.1f} ({statistics.median(v):.0f}), n={len(v)}" if v else "–")
            rows.append([TYPE_NAME.get(t, t)] + cells)
        md += table(["Firm type"] + [f"FY{y}" for y in years], rows) + [""]
        last = years[-1] if years else ""
        top = sorted((s for s in scores if s["fiscal_year"] == last), key=lambda s: -float(s["ai_use_score"]))[:12]
        if top:
            md += [f"**Highest AI Use Scores, FY{last}:**", ""]
            md += table(["Firm", "Type", "AI Use", "Areas with use", "Readiness", "Talk ratio"],
                        [[f"{s['company']} ({s['ticker']})", TYPE_NAME.get(ftype.get(s["ticker"]), "?").split(" (")[0],
                          s["ai_use_score"], s["scenarios_with_use"], s["readiness_score"], f"{s['talk_ratio_pct']}%"]
                         for s in top]) + [""]

        # index preview
        index, _ = sector_index.build(scores, floats, inv, tickers=None)
        if index:
            md += ["## Sector index preview (all firms in the list)", "",
                   "Computed with `sector_index.build()` (#134) on the agent's 10-K scores. Draft: Yen-Chu owns the "
                   "index; held labels count as no use; new firm types not yet validated.", ""]
            md += table(["Fiscal year", "Firms", "AI-EW (equal)", "AI-CW (by public float)"],
                        [[r["fiscal_year"], r["n_firms"], r["ai_ew"], r["ai_cw"]] for r in index]) + [""]
            md += ["Yen-Chu's command for the index files:", "",
                   "```",
                   "python3 -m src.index.sector_index --scores data/processed/sec/sp500_financials/agent_scores.csv \\",
                   "    --floats data/processed/sec/sp500_financials/public_float.csv \\",
                   "    --inventory data/processed/sec/sp500_financials/filings_inventory.csv --tickers all \\",
                   "    --out data/processed/sec/sp500_financials/sector_index.csv \\",
                   "    --out-firms data/processed/sec/sp500_financials/sector_index_firms.csv",
                   "```", ""]

    # run facts
    md += ["## Run facts", ""]
    if info:
        md.append(f"- Download: {info.get('filings_ok', '?')}/{info.get('filings', '?')} filings read, "
                  f"{info.get('ai_passages', '?')} AI passages, {info.get('public_floats', '?')} public floats, "
                  f"{info.get('wall_seconds', '?')} s, run {info.get('run_at', '?')}.")
    if run:
        u = run.get("usage", {})
        md.append(f"- Agent: {run.get('passages', '?')} passages, {u.get('calls', '?')} new model calls, "
                  f"{u.get('cache_hits', '?')} from the cache, {run.get('wall_seconds', '?')} s with "
                  f"{run.get('workers', 1)} at a time, run {run.get('run_at', '?')}; tokens in {u.get('prompt_tokens', '?')} "
                  f"(cached {u.get('cached_prompt_tokens', '?')}), out {u.get('completion_tokens', '?')}, "
                  f"{u.get('truncated', 0)} cut off.")
        md.append(f"- Model cost: about **${cost(u):.2f}** at off-peak prices (about ${2 * cost(u):.2f} at peak).")
        md.append(f"- Guardrail: {run.get('verify_status', {})}.")
    md += ["", "## Next", "",
           f"1. **Review the {len(held)} held labels** (`review_queue.csv`: fill review_evidence and review_scenarios).",
           "2. **Labeling round 3 (sector pilot):** two people label the 40 sampled passages (10 per new firm type) "
           "on their own; same bar as check 3 (overclaim at most 5%). A type that misses gets its own rules and a rerun.",
           "3. **Index (#134):** Yen-Chu runs the command above once the pilot passes.",
           "4. **10-Q question (#157):** this run is 10-K only, as Julie prefers. On our 7 firms, FY2024–25, the 10-Qs "
           "change only Citi's FY2025 score (53 with them, 9 without); the team decides whether to add the 10-Qs.", ""]

    queue = [{**r, "firm_type": ftype.get(r["ticker"], ""), "passage": text.get(r["passage_id"], ""),
              "review_evidence": "", "review_scenarios": "", "reviewer": "", "review_note": ""} for r in held]
    return "\n".join(md) + "\n", queue


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dir", default=str(DIR))
    ap.add_argument("--passages", default=str(PASSAGES))
    ap.add_argument("--out-md", default=str(OUT_MD))
    a = ap.parse_args(argv)
    md, queue = build(Path(a.dir), Path(a.passages))
    try:  # Windows console redirected to a file: never crash on a character
        import sys
        sys.stdout.reconfigure(errors="replace")
    except Exception:
        pass
    Path(a.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out_md).write_text(md, encoding="utf-8")
    with (Path(a.dir) / "review_queue.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=REVIEW_FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(queue)
    print(md)
    print(f"-> {a.out_md}\n-> {Path(a.dir) / 'review_queue.csv'} ({len(queue)} held labels)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
