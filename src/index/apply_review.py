"""Apply the people's decisions on held labels, then re-score (the human-in-the-loop step, #170).

The guardrail holds a label it can't trust (confidence under 0.70, quote not found word for word):
it is scored as N until a person looks at it. Reviewers fill three columns of review_queue.csv:

    review_evidence    D2, D1, P, N or X (required for the row to count as reviewed)
    review_scenarios   area codes separated by ";" (required for D2/D1/P, empty for N/X)
    reviewer           your name
    review_note        optional: why

This script copies the reviewed rows into a new labels file (verify_status = human_reviewed) and
scores it. Rows not reviewed yet stay N, as before. The agent's own labels file is never changed.

Run from the repo root:
    python3 -m src.index.apply_review          # S&P 500 Financials files (defaults)
Then build the index from the reviewed scores (#134):
    python3 -m src.index.sector_index --scores data/processed/sec/sp500_financials/agent_scores_reviewed.csv ...
"""
import argparse
import csv
import sys
from pathlib import Path

from src.index.score_companies import score
from src.nlp.taxonomy_v0 import ALL_SCENARIOS, EVIDENCE, read

DIR = Path("data/processed/sec/sp500_financials")
USE = {"D2", "D1", "P"}


def check_row(r: dict) -> tuple[str, list[str], str]:
    """Return (evidence, scenarios, problem). problem is "" when the review is valid."""
    ev = (r.get("review_evidence") or "").strip().upper()
    scen = [s.strip().upper() for s in (r.get("review_scenarios") or "").replace(",", ";").split(";") if s.strip()]
    if ev not in EVIDENCE:
        return ev, scen, f"unknown evidence {ev!r}"
    bad = [s for s in scen if s not in ALL_SCENARIOS]
    if bad:
        return ev, scen, f"unknown area code(s) {bad}"
    if ev in USE and not scen:
        return ev, scen, f"{ev} needs at least one area code"
    if ev not in USE and scen:
        return ev, scen, f"{ev} takes no area codes"
    if not (r.get("reviewer") or "").strip():
        return ev, scen, "reviewer name missing"
    return ev, scen, ""


def apply(labels: list[dict], queue: list[dict]) -> tuple[list[dict], dict, list[str]]:
    """Return (new labels, counts, problems). Only valid, filled-in reviews change a label."""
    by_id = {r["passage_id"]: r for r in queue}
    problems, n_done = [], 0
    out = []
    for lab in labels:
        rev = by_id.get(lab["passage_id"])
        if rev is None or lab.get("verify_status") != "needs_review" or not (rev.get("review_evidence") or "").strip():
            out.append(lab)
            continue
        ev, scen, problem = check_row(rev)
        if problem:
            problems.append(f"{lab['passage_id']}: {problem}")
            out.append(lab)
            continue
        new = dict(lab)
        new.update(evidence_v0=ev, scenarios_v0=";".join(scen), verify_status="human_reviewed",
                   verify_reason=f"held ({lab.get('verify_reason', '')}); reviewed by {rev['reviewer'].strip()}",
                   coder=rev["reviewer"].strip(), coder_note=(rev.get("review_note") or "").strip())
        out.append(new)
        n_done += 1
    held = sum(1 for r in labels if r.get("verify_status") == "needs_review")
    unknown = sorted(set(by_id) - {r["passage_id"] for r in labels})
    problems += [f"{pid}: not in the labels file" for pid in unknown]
    return out, {"held": held, "reviewed": n_done, "still_held": held - n_done}, problems


def write(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--labels", default=str(DIR / "agent_labels.csv"), help="the agent's labels (read only)")
    ap.add_argument("--queue", default=str(DIR / "review_queue.csv"), help="review queue with the people's decisions")
    ap.add_argument("--labels-out", default=str(DIR / "agent_labels_reviewed.csv"))
    ap.add_argument("--scores-out", default=str(DIR / "agent_scores_reviewed.csv"))
    a = ap.parse_args(argv)
    if Path(a.labels_out).resolve() == Path(a.labels).resolve():
        print("--labels-out must differ from --labels: the agent's labels are never overwritten.")
        return 2
    labels, counts, problems = apply(read(a.labels), read(a.queue))
    for p in problems:
        print("  fix:", p)
    write(Path(a.labels_out), labels)
    write(Path(a.scores_out), score(labels))
    print(f"Held by the guardrail: {counts['held']} · reviewed: {counts['reviewed']} · "
          f"still held (scored as N): {counts['still_held']} · rows to fix: {len(problems)}")
    print(f"-> {a.labels_out}\n-> {a.scores_out}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
