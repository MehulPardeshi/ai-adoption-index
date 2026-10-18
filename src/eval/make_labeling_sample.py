"""Build the blind 50-passage sample for labeling round 1 (evaluation check #2).

Design (agreed by Mehul, 2026-10-18; see docs/part3-metrics/evaluation_plan.md):
  * Pool = the 245 AI passages from the SEC test run (PR #43).
  * Drop exact repeats (same text in several filings): keep the earliest copy.
  * Drop passages Yen-Chu's draft labels mark X (definitions, headings).
  * Stratify on Yen-Chu's draft evidence level: keep every D2, D1 and P passage
    (the hard cases), then fill to 50 with a random draw of N passages.
  * Shuffle with a fixed seed, so anyone can rebuild the identical sample.

The output contains NO labels: raters must label blind.

Run from the repo root:  python3 -m src.eval.make_labeling_sample
"""
import csv
import random
from pathlib import Path

SEED = 20261018
SAMPLE_SIZE = 50
PASSAGES = Path("data/interim/sec/ai_passages.csv")
LABELS = Path("data/processed/sec/passage_labels_v0.csv")
OUT_DIR = Path("docs/part3-metrics/labeling_round_1")
KEEP_ALL = {"D2", "D1", "P"}


def _norm(text: str) -> str:
    return " ".join(text.lower().split())


def build_sample() -> list[dict]:
    passages = list(csv.DictReader(PASSAGES.open(encoding="utf-8")))
    labels = {r["passage_id"]: r["evidence_v0"] for r in csv.DictReader(LABELS.open(encoding="utf-8"))}

    passages.sort(key=lambda r: (r["period"], r["passage_id"]))  # earliest copy wins
    seen, unique = set(), []
    for row in passages:
        key = _norm(row["passage"])
        if key not in seen:
            seen.add(key)
            unique.append(row)

    unique = [r for r in unique if labels[r["passage_id"]] != "X"]
    hard = [r for r in unique if labels[r["passage_id"]] in KEEP_ALL]
    talk = [r for r in unique if labels[r["passage_id"]] == "N"]

    rng = random.Random(SEED)
    sample = hard + rng.sample(talk, SAMPLE_SIZE - len(hard))
    rng.shuffle(sample)
    return sample


def main() -> None:
    sample = build_sample()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cols = ["item", "passage_id", "company", "form", "period", "section_guess", "passage", "source_url"]
    with (OUT_DIR / "sample_passages.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for i, row in enumerate(sample, 1):
            w.writerow({**row, "item": i})
    with (OUT_DIR / "rater_TEMPLATE.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["item", "passage_id", "about_ai", "evidence", "scenarios", "note"])
        for i, row in enumerate(sample, 1):
            w.writerow([i, row["passage_id"], "", "", "", ""])
    print(f"Wrote {len(sample)} passages to {OUT_DIR}/sample_passages.csv (seed {SEED}).")


if __name__ == "__main__":
    main()
