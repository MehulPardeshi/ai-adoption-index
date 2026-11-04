"""Evaluation check 5: compare an independent download with the team's official files.

    python3 src/edgar/download_sec_filings.py --data <folder> --start 2023-12-31 --end 2026-06-30
    python3 -m src.index.score_companies --out <folder>/scores.csv
    python3 -m src.eval.check5_compare --data <folder>

The official set has 74 filings: Citi's three filings before Q3 2024 aren't in it, so the rerun
finds 3 extra filings and 5 extra passages. Those are reported, not counted as differences.
"""
import argparse
import csv
from pathlib import Path

LABELS = Path("data/processed/sec/passage_labels_v0.csv")
INVENTORY = Path("data/processed/sec/filings_inventory.csv")
SCORES = Path("data/processed/sec/company_scores_v0.csv")
SAMPLES = [Path(f"docs/part3-metrics/labeling_round_{n}/sample_passages.csv") for n in (1, 2)]


def rows(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True, help="the --data folder of the independent download")
    data = Path(ap.parse_args().data)
    key = lambda r: (r["ticker"], r["form"], r["period"])

    new_inv, old_inv = {key(r): r for r in rows(data / "processed/sec/filings_inventory.csv")}, {key(r): r for r in rows(INVENTORY)}
    para_diff = [k for k in old_inv if k in new_inv and old_inv[k]["paragraphs"] != new_inv[k]["paragraphs"]]
    new_pass = {r["passage_id"]: r for r in rows(data / "interim/sec/ai_passages.csv")}
    old_ids = {r["passage_id"] for r in rows(LABELS)}
    text_diff = [r["passage_id"] for p in SAMPLES for r in rows(p) if new_pass.get(r["passage_id"], {}).get("passage") != r["passage"]]
    score_file = data / "scores.csv"
    same_scores = score_file.exists() and rows(score_file) == rows(SCORES)

    print(f"Filings: {len(old_inv)} official, missing from the rerun: {sorted(set(old_inv) - set(new_inv))}")
    print(f"  extra in the rerun: {sorted(set(new_inv) - set(old_inv))}")
    print(f"  paragraph counts that differ: {para_diff}")
    print(f"AI passages: {len(old_ids)} official, missing from the rerun: {sorted(old_ids - set(new_pass))}")
    print(f"  extra in the rerun: {sorted(set(new_pass) - old_ids)}")
    print(f"Labeling-sample text that differs: {text_diff}")
    print(f"Scores identical: {same_scores}" + ("" if score_file.exists() else f" (no {score_file})"))
    ok = not (set(old_inv) - set(new_inv) or para_diff or old_ids - set(new_pass) or text_diff) and same_scores
    print("\nRESULT:", "MATCH" if ok else "DIFFERENCES: please explain each one")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
