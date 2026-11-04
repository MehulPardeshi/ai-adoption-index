"""Evaluation check 1: did the keyword search find the AI text? (recall)

Sweeps every paragraph the search did NOT flag for near-miss wording, then samples 100 for a
person to read. Needs the full filing text from src/edgar/download_sec_filings.py (not in git).

    python3 -m src.eval.make_recall_sample --data <folder with raw/sec/text>

Writes docs/part3-metrics/check1/recall_sample.csv and prints the sweep counts.
Covers the 74 filings in data/processed/sec/filings_inventory.csv.
"""
import argparse
import csv
import random
import re
from pathlib import Path

OUT = Path("docs/part3-metrics/check1/recall_sample.csv")
INVENTORY = Path("data/processed/sec/filings_inventory.csv")
SEED = 20261103
MIN_CHARS = 80  # table cells and crumbs aren't passages

# The search terms in src/edgar/download_sec_filings.py
FLAGGED = re.compile(r"artificial intelligence|machine[- ]learning|generative AI|gen ?AI|large language models?|"
                     r"\bLLMs?\b|deep learning|neural networks?|natural language processing|\bNLP\b|chat ?bots?|"
                     r"\bcopilots?\b|agentic|AI agents?|predictive (?:analytics|models?)|computer vision", re.I)
AI_WORD = re.compile(r"(?<![A-Za-z])AI(?![A-Za-z])")

# Wording the search could plausibly miss: spelling variants and product names. Reported as counts.
SWEEP = {
    "spelling variants": r"machine.learning|large.language|generative.{0,2}(?:artificial|model)|artificial.{0,3}intel|\bA\.I\.",
    "assistants and bots": r"virtual (?:assistant|agent)|digital assistant|conversational|\bbots?\b|robotic|\bRPA\b",
    "intelligent or cognitive": r"intelligen(?:t|ce) (?:automation|system|agent|assistant|tool|technolog)|cognitive (?:comput|tech)",
    "product names": r"\bErica\b|LLM Suite|ChatGPT|OpenAI|\bGPT\b|\bEno\b",
    "deepfakes": r"deep.?fakes?|synthetic (?:media|identit)",
    "robo or automated advice": r"robo.?advi|intelligent portfolio|digital advice|automated (?:online )?investment|algorithmic.based",
}
# Near-miss strata for the sample, with how many to draw from each
STRATA = [("algorithm", r"algorithm", 17), ("deepfakes", SWEEP["deepfakes"], 2), ("automation", r"\bautomat(?:ion|ed|ing)\b", 28),
          ("emerging technology", r"emerging technolog|new technolog|innovative technolog", 25),
          ("machine", r"\bmachines?\b", 8), ("model", r"\bmodels?\b", 28)]


def unflagged(data: Path, inventory: list[dict]):
    for f in inventory:
        stem = f"{f['ticker']}_{f['period']}_{f['form']}"
        paragraphs = (data / "raw/sec/text" / f"{stem}.txt").read_text(encoding="utf-8").split("\n\n")
        for i, p in enumerate(paragraphs):
            if len(p) >= MIN_CHARS and not FLAGGED.search(p) and not AI_WORD.search(p):
                yield {"paragraph_id": f"{stem}_{i:05d}", "company": f["company"], "form": f["form"],
                       "period": f["period"], "source_url": f["url"], "paragraph": p}


def _key(text: str) -> str:
    return " ".join(re.findall(r"[a-z]+", text.lower())[:25])  # filings repeat paragraphs year after year


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True, help="folder that holds raw/sec/text/")
    args = ap.parse_args()
    inventory = list(csv.DictReader(INVENTORY.open(encoding="utf-8")))
    rows = list(unflagged(Path(args.data), inventory))
    print(f"{len(inventory)} filings, {len(rows)} unflagged paragraphs of at least {MIN_CHARS} characters\n\nSweep:")
    for name, pattern in SWEEP.items():
        print(f"  {name:<26}{sum(bool(re.search(pattern, r['paragraph'], re.I)) for r in rows)}")

    rng = random.Random(SEED)
    seen, sample = set(), []
    print("\nSample:")
    for name, pattern, n in STRATA:
        pool, keys = [], set()
        for r in rows:
            k = _key(r["paragraph"])
            if k not in seen and k not in keys and re.search(pattern, r["paragraph"], re.I):
                keys.add(k)
                pool.append(r)
        picked = rng.sample(pool, min(n, len(pool)))
        seen |= {_key(r["paragraph"]) for r in picked}
        sample += [{**r, "near_miss_term": name} for r in picked]
        print(f"  {name:<26}{len(picked)} of {len(pool)} distinct")
    rng.shuffle(sample)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fields = ["item", "paragraph_id", "company", "form", "period", "near_miss_term", "paragraph", "source_url"]
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows({**r, "item": i} for i, r in enumerate(sample, 1))
    print(f"\n-> {OUT} ({len(sample)} paragraphs)")


if __name__ == "__main__":
    main()
