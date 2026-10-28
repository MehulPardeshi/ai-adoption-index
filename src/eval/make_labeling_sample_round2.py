"""Build the blind 30-passage sample for labeling round 2 (evaluation check #2, after round 1).

Design (Mehul, 2026-10-27; see docs/part3-metrics/evaluation_plan.md, "Round 2"):
  * Pool = the 277 AI passages (passage_labels_v0.csv), minus every passage whose text the
    raters saw in round 1, minus the guardrail test passages (their expected labels are
    public in guardrail_redteam_cases.csv), minus repeats (keep the earliest copy). A repeat is a passage whose
    first 25 words match another's: filings re-use risk paragraphs year after year with small
    edits, and keeping those would let one company (Capital One) fill the sample.
  * Round 1 used every D2/D1/P passage, so a random draw would be almost all easy "just talk"
    passages and would inflate agreement. Instead, stratify on the AI-assisted draft label and
    target the rules round 1 got wrong:
      - every remaining D1 passage (real use);
      - N passages where the company talks about its OWN models/AI ("we use", "our models"):
        the D1-vs-N boundary (risk factors that admit use, hedged "may use");
      - other N passages (risks, threats, laws): tests the clarified "about AI" rule;
      - X passages (definitions, headings, non-AI keyword hits).
  * Shuffle with a fixed seed, so anyone can rebuild the identical sample.

The output contains NO labels: raters must label blind.

Run from the repo root:  python3 -m src.eval.make_labeling_sample_round2
"""
import csv
import random
import re
from pathlib import Path

SEED = 20261027
PASSAGES = Path("data/interim/sec/ai_passages.csv")
LABELS = Path("data/processed/sec/passage_labels_v0.csv")
ROUND_1 = Path("docs/part3-metrics/labeling_round_1/sample_passages.csv")
REDTEAM = Path("docs/part3-metrics/guardrail_redteam_cases.csv")
OUT_DIR = Path("docs/part3-metrics/labeling_round_2")
N_BOUNDARY, N_TALK, N_X = 12, 11, 4  # plus every remaining D1 passage (3): 30 in total
OWN_USE = re.compile(r"\b(we|our|the (firm|company|bank)|JPMorganChase|Citi|Schwab)\b[^.]{0,80}"
                     r"\b(use|uses|using|deploy\w*|leverag\w+|adopt\w*|implement\w*)\b[^.]{0,60}"
                     r"\b(AI|artificial intelligence|machine learning|generative)", re.I)


def _norm(text: str) -> str:
    return " ".join(re.sub(r"[^a-z ]", " ", text.lower()).split()[:25])


def build_sample() -> list[dict]:
    passages = list(csv.DictReader(PASSAGES.open(encoding="utf-8")))
    labels = {r["passage_id"]: r["evidence_v0"] for r in csv.DictReader(LABELS.open(encoding="utf-8"))}
    seen = {_norm(r["passage"]) for r in csv.DictReader(ROUND_1.open(encoding="utf-8"))}

    redteam = {r["passage_id"] for r in csv.DictReader(REDTEAM.open(encoding="utf-8")) if r["passage_id"]}
    seen |= {_norm(r["passage"]) for r in passages if r["passage_id"] in redteam}

    passages.sort(key=lambda r: (r["period"], r["passage_id"]))  # earliest copy wins
    unique = []
    for row in passages:
        key = _norm(row["passage"])
        if key not in seen:
            seen.add(key)
            unique.append(row)

    use = [r for r in unique if labels[r["passage_id"]] in {"D2", "D1", "P"}]
    boundary = [r for r in unique if labels[r["passage_id"]] == "N" and OWN_USE.search(r["passage"])]
    talk = [r for r in unique if labels[r["passage_id"]] == "N" and not OWN_USE.search(r["passage"])]
    other = [r for r in unique if labels[r["passage_id"]] == "X"]

    rng = random.Random(SEED)
    sample = use + rng.sample(boundary, N_BOUNDARY) + rng.sample(talk, N_TALK) + rng.sample(other, N_X)
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
