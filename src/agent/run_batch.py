"""Batch mode: label passages with the agent and score the companies.

Fixed order, so a rerun gives the same files: passages -> classify_passage -> verify_label ->
agent_labels_v1.csv -> score_companies -> agent_scores_v1.csv.

Examples (from the repo root):
    python3 -m src.agent.run_batch                               # all 245 passages
    python3 -m src.agent.run_batch --tickers JPM,BAC,COF,WFC,SCHW,PFG --year 2025 --forms 10-K
    python3 -m src.agent.run_batch --ids docs/part3-metrics/labeling_round_1/sample_passages.csv
    python3 -m src.agent.run_batch --no-guardrails               # for the check 6 comparison
    AGENT_LLM_PROVIDER=mock python3 -m src.agent.run_batch --limit 20   # offline dry run
    python3 -m src.agent.run_batch --passages data/interim/sec/sp500_financials/ai_passages.csv \
        --labels-out data/processed/sec/sp500_financials/agent_labels.csv \
        --scores-out data/processed/sec/sp500_financials/agent_scores.csv \
        --run-info-out data/processed/sec/sp500_financials/agent_run_info.json --workers 6   # sector run

--workers N sends N passages to the model at a time. The output order and the labels are the
same as with one worker (each passage's answer is cached on its own); only the time changes.

Rerunning the same command (say, after a reply was cut off) calls the model only for what failed;
everything else comes from the cache. The run log keeps the earlier passes (earlier_passes) and
their totals (all_passes), so the first pass's time and tokens aren't lost. Its top-level fields
describe the last pass, the one the labels file now reflects.

Output columns: the first eleven match passage_labels_v0.csv, so src/eval/irr.py and
src/index/score_companies.py read the file unchanged (pass the new path with --ai-labels / --labels).
evidence_v0 / scenarios_v0 hold the value AFTER the guardrail; needs_review rows are N with no
scenarios so they never reach the score; the model's own call is in evidence_raw / scenarios_raw.
"""
import argparse
import json
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

from src.agent import config, llm, store, tools


def _rel(p: Path) -> str:
    try:
        return str(p.resolve().relative_to(config.ROOT))
    except ValueError:
        return str(p)
from src.index.score_companies import score as score_rows

V0_FIELDS = ["passage_id", "company", "ticker", "form", "period", "topic_v0", "evidence_v0", "scenarios_v0",
             "coder", "coder_note", "source_url"]
AGENT_FIELDS = ["quote", "specific", "confidence", "flags", "evidence_raw", "scenarios_raw",
                "verify_status", "verify_reason", "model", "prompt_version", "run_at"]
FIELDS = V0_FIELDS + AGENT_FIELDS
SCORE_FIELDS = ["company", "ticker", "fiscal_year", "ai_use_score", "scenarios_with_use", "readiness_score",
                "talk_ratio_pct", "substantive_ai_passages"]
# A run log is continued (not restarted) when all of these match the previous one.
SAME_RUN = ("model", "prompt_version", "guardrails", "passages_file", "labels_file", "passages")
PASS_KEYS = ("run_at", "wall_seconds", "workers", "usage")
SUM_KEYS = ("calls", "prompt_tokens", "cached_prompt_tokens", "completion_tokens", "reasoning_tokens", "truncated")


def add_earlier_passes(info: dict, old: dict) -> dict:
    """Return this pass's run log with the passes before it that wrote the same labels file.

    A different model, prompt, guardrail setting or passage set starts a new log. all_passes sums
    the calls, tokens and seconds of every pass (cache hits are left out: a rerun re-reads them).
    """
    same = bool(old) and all(old.get(k) == info.get(k) for k in SAME_RUN)
    earlier = list(old.get("earlier_passes") or []) + [{k: old.get(k) for k in PASS_KEYS}] if same else []
    passes = earlier + [{k: info.get(k) for k in PASS_KEYS}]
    total = {k: sum((p.get("usage") or {}).get(k, 0) for p in passes) for k in SUM_KEYS}
    total["wall_seconds"] = round(sum(p.get("wall_seconds") or 0 for p in passes), 1)
    return {**info, "earlier_passes": earlier, "all_passes": {"passes": len(passes), **total}}


def _read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def label_one(rec: dict, guardrails: bool, run_at: str) -> dict:
    raw = tools.classify_passage(passage_id=rec["passage_id"], guardrails=guardrails)
    if guardrails:
        checked = tools.verify_label(raw, rec["passage"])
    else:  # no guardrail: the model's call goes straight to the score
        checked = {**raw, "evidence_raw": raw.get("evidence", ""), "scenarios_raw": ";".join(raw.get("scenarios") or []),
                   "verify_status": "not_checked", "verify_reason": "guardrails off"}
    if raw.get("error"):
        checked.update(evidence="N", scenarios=[], verify_status="needs_review", verify_reason=raw["error"])
    return {
        "passage_id": rec["passage_id"], "company": rec["company"], "ticker": rec["ticker"],
        "form": rec["form"], "period": rec["period"],
        "topic_v0": checked.get("topic", ""), "evidence_v0": checked.get("evidence", ""),
        "scenarios_v0": ";".join(checked.get("scenarios") or []),
        "coder": f"agent: {llm.model_tag()}", "coder_note": checked.get("reason", ""),
        "source_url": rec["source_url"],
        "quote": checked.get("quote", ""), "specific": checked.get("specific") or "",
        "confidence": checked.get("confidence", ""), "flags": ";".join(checked.get("flags") or []),
        "evidence_raw": checked.get("evidence_raw", ""), "scenarios_raw": checked.get("scenarios_raw", ""),
        "verify_status": checked.get("verify_status", ""), "verify_reason": checked.get("verify_reason", ""),
        "model": llm.model_tag(), "prompt_version": config.PROMPT_VERSION, "run_at": run_at,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Label SEC AI passages with the agent and score companies.")
    ap.add_argument("--tickers", help="comma-separated, e.g. JPM,BAC (default all)")
    ap.add_argument("--year", type=int, action="append", help="fiscal year; repeat for several")
    ap.add_argument("--forms", help="10-K, 10-Q or 10-K,10-Q (default both)")
    ap.add_argument("--ids", help="CSV with a passage_id column (e.g. the labeling sample)")
    ap.add_argument("--limit", type=int, help="label only the first N passages (smoke test)")
    ap.add_argument("--no-guardrails", action="store_true", help="skip verify_label and the injection-safe prompt")
    ap.add_argument("--no-ent", action="store_true", help="sensitivity check: ENT earns 0 points (rule before Oct 25)")
    ap.add_argument("--ent-counts", action="store_true", help=argparse.SUPPRESS)  # now the default (#33, Oct 27)
    ap.add_argument("--labels-out", help="labels CSV path")
    ap.add_argument("--scores-out", help="scores CSV path")
    ap.add_argument("--run-info-out", help="write the run log (model, prompt, usage, time) here; "
                                           "default: agent_run_info.json, only for the default labels file. "
                                           "A rerun into the same labels file adds itself as a pass; "
                                           "delete the log to start a new one")
    ap.add_argument("--passages", help="passage CSV to label (default: the 7-firm data/interim/sec/ai_passages.csv)")
    ap.add_argument("--workers", type=int, default=1, help="passages sent to the model at a time (default 1)")
    a = ap.parse_args(argv)

    if a.passages:
        if not a.labels_out or not a.scores_out:
            ap.error("--passages needs --labels-out and --scores-out, so the 7-firm files aren't overwritten")
        config.PASSAGES = Path(a.passages)
    guard = not a.no_guardrails
    ids = [r["passage_id"] for r in store.read_csv(Path(a.ids))] if a.ids else None
    recs = store.select_passages(tickers=a.tickers.split(",") if a.tickers else None, fiscal_years=a.year,
                                 forms=a.forms.split(",") if a.forms else None, ids=ids)
    if a.limit:
        recs = recs[: a.limit]
    if not recs:
        print("No passages match those filters.")
        return 1

    labels_out = Path(a.labels_out) if a.labels_out else (config.AGENT_LABELS if guard else config.AGENT_LABELS_NOGUARD)
    scores_out = Path(a.scores_out) if a.scores_out else (config.AGENT_SCORES if guard else
                                                           config.AGENT_SCORES.with_name("agent_scores_v1_noguard.csv"))
    run_at = datetime.now().isoformat(timespec="seconds")
    workers = max(1, a.workers)
    print(f"Labeling {len(recs)} passages with {llm.model_tag()} (guardrails {'on' if guard else 'off'}, "
          f"{workers} at a time) ...")

    llm.reset_usage()  # the run log reports this pass only, also when main() runs twice in one process
    t0 = time.monotonic()
    step = 25 if len(recs) < 500 else 100
    with ThreadPoolExecutor(max_workers=workers) as pool:
        rows = []
        for i, row in enumerate(pool.map(lambda rec: label_one(rec, guard, run_at), recs), 1):
            rows.append(row)  # map() keeps the input order
            if i % step == 0 or i == len(recs):
                print(f"  {i}/{len(recs)}  ({round(time.monotonic() - t0)} s)", flush=True)
    wall = round(time.monotonic() - t0, 1)

    store.write_csv(labels_out, rows, FIELDS)
    scores = score_rows(rows, ent_counts=not a.no_ent)
    store.write_csv(scores_out, scores, SCORE_FIELDS)

    status = Counter(r["verify_status"] for r in rows)
    ev = Counter(r["evidence_v0"] for r in rows)
    info = {"run_at": run_at, "model": llm.model_tag(), "provider": config.PROVIDER,
            "prompt_version": config.PROMPT_VERSION, "temperature": config.TEMPERATURE,
            "guardrails": guard, "min_confidence": config.MIN_CONFIDENCE, "ent_counts": not a.no_ent,
            "passages": len(rows), "evidence": dict(ev), "verify_status": dict(status),
            "usage": dict(llm.USAGE), "wall_seconds": wall, "workers": workers,
            "passages_file": _rel(Path(config.PASSAGES)), "labels_file": _rel(labels_out),
            "scores_file": _rel(scores_out)}
    log = Path(a.run_info_out) if a.run_info_out else (config.AGENT_RUN_INFO if guard and not a.labels_out else None)
    if log:
        info = add_earlier_passes(info, _read_json(log))
        log.write_text(json.dumps(info, indent=2), encoding="utf-8")

    print(f"\nEvidence: {dict(ev)}")
    print(f"Guardrail: {dict(status)}")
    print(f"LLM calls {llm.USAGE['calls']}, cache hits {llm.USAGE['cache_hits']}, "
          f"tokens in {llm.USAGE['prompt_tokens']} (cached {llm.USAGE['cached_prompt_tokens']}), out {llm.USAGE['completion_tokens']}")
    if info.get("earlier_passes"):
        t = info["all_passes"]
        print(f"All {t['passes']} passes into this labels file: LLM calls {t['calls']}, {t['wall_seconds']} s, "
              f"tokens in {t['prompt_tokens']} (cached {t['cached_prompt_tokens']}), out {t['completion_tokens']}")
    print(f"-> {_rel(labels_out)}\n-> {_rel(scores_out)}")
    for s in scores:
        print(f"   {s['ticker']:5} FY{s['fiscal_year']}  use {s['ai_use_score']:>3}  readiness {s['readiness_score']:>3}"
              f"  talk {s['talk_ratio_pct']}%  [{s['scenarios_with_use']}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
