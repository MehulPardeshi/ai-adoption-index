"""Build the blind sample for labeling round 3: the sector pilot (Nov 10 plan, #133).

The agent was tuned and checked on bank filings. Before we trust its scores for the other firm
types, two people label 10 passages per new type on their own and we check the agent against
them with the same bar as check 3 (overclaim at most 5%).

Design:
  * Pool: the S&P 500 Financials run's labeled passages, minus the 7 proof-of-concept firms
    (already human-checked) and minus X (definitions, headings). Exact repeats dropped.
  * Four new types (firms.csv firm_type): insurer, asset_mgmt_broker, payments_consumer_finance,
    exchange_data. Banks are already checked.
  * Per type, 10 passages: up to 5 the agent calls use (D2/D1, where an overclaim would show),
    up to 1 plan (P), the rest no use (N, including labels the guardrail held); short strata
    are filled from the others. At most 2 passages per firm, so a type isn't one firm.
  * Fixed seed, so anyone can rebuild the same sample.

The sample has NO labels (raters stay blind); the agent's labels go to agent_key.csv.
Then the same tools as rounds 1 and 2:
    python3 -m src.eval.make_labeling_workbook 3              # the Excel workbook for raters
    python3 -m src.eval.workbook_to_csv labeling_<name>.xlsx <name> 3

Run from the repo root (after the agent has labeled the run):
    python3 -m src.eval.make_sector_pilot_sample
"""
import argparse
import csv
import random
from collections import defaultdict
from pathlib import Path

SEED = 20261115
PER_TYPE = 10
QUOTA = {"use": 5, "plan": 1}           # the rest is filled with "no use"
MAX_PER_FIRM = 2
NEW_TYPES = ["insurer", "asset_mgmt_broker", "payments_consumer_finance", "exchange_data"]
DIR = Path("data/processed/sec/sp500_financials")
PASSAGES = Path("data/interim/sec/sp500_financials/ai_passages.csv")
OUT = Path("docs/part3-metrics/labeling_round_3")
SAMPLE_FIELDS = ["item", "passage_id", "company", "form", "period", "section_guess", "passage", "source_url"]
KEY_FIELDS = ["item", "passage_id", "ticker", "firm_type", "stratum", "evidence_v0", "scenarios_v0", "evidence_raw",
              "confidence", "verify_status"]


def read(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def stratum(label: dict) -> str:
    if label["evidence_v0"] in ("D2", "D1"):
        return "use"
    if label["evidence_v0"] == "P":
        return "plan"
    return "no_use"


def pick(pool: list[dict], n: int, per_firm: dict, rng: random.Random) -> list[dict]:
    """Up to n passages from pool, at most MAX_PER_FIRM per firm, spread across firms."""
    rng.shuffle(pool)
    by_firm = defaultdict(list)
    for r in pool:
        by_firm[r["ticker"]].append(r)
    firms = sorted(by_firm)
    rng.shuffle(firms)
    out = []
    while len(out) < n:
        added = False
        for t in firms:  # one per firm per pass
            if len(out) >= n:
                break
            if by_firm[t] and per_firm[t] < MAX_PER_FIRM:
                out.append(by_firm[t].pop())
                per_firm[t] += 1
                added = True
        if not added:
            break
    return out


def build(firms: list[dict], passages: list[dict], labels: list[dict], seed: int = SEED):
    ftype = {f["ticker"]: f["firm_type"] for f in firms}
    poc = {f["ticker"] for f in firms if f.get("poc_firm") == "yes"}
    text = {p["passage_id"]: p for p in passages}
    seen, pool = set(), defaultdict(lambda: defaultdict(list))
    for lab in sorted(labels, key=lambda r: (r["period"], r["passage_id"])):  # earliest copy wins
        p = text.get(lab["passage_id"])
        t = lab["ticker"]
        if not p or t in poc or lab["evidence_v0"] == "X" or ftype.get(t) not in NEW_TYPES:
            continue
        key = " ".join(p["passage"].lower().split())
        if key in seen:
            continue
        seen.add(key)
        pool[ftype[t]][stratum(lab)].append({**lab, **p, "firm_type": ftype[t], "stratum": stratum(lab)})

    rng = random.Random(seed)
    chosen = []
    for t in NEW_TYPES:
        per_firm = defaultdict(int)
        got = []
        for s in ("use", "plan"):
            got += pick(list(pool[t][s]), QUOTA[s], per_firm, rng)
        got += pick(list(pool[t]["no_use"]), PER_TYPE - len(got), per_firm, rng)
        if len(got) < PER_TYPE:  # too few "no use" passages: fill from what's left
            ids = {r["passage_id"] for r in got}
            left = [r for s in ("use", "plan") for r in pool[t][s] if r["passage_id"] not in ids]
            got += pick(left, PER_TYPE - len(got), per_firm, rng)
        chosen += got
    rng.shuffle(chosen)  # raters see the types mixed
    sample, key = [], []
    for i, r in enumerate(chosen, 1):
        sample.append({"item": i, **{k: r.get(k, "") for k in SAMPLE_FIELDS if k != "item"}})
        key.append({"item": i, **{k: r.get(k, "") for k in KEY_FIELDS if k != "item"}})
    return sample, key


def write(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Build the blind sample for labeling round 3 (sector pilot).")
    ap.add_argument("--dir", default=str(DIR))
    ap.add_argument("--passages", default=str(PASSAGES))
    ap.add_argument("--out", default=str(OUT))
    a = ap.parse_args(argv)
    d = Path(a.dir)
    sample, key = build(read(d / "firms.csv"), read(Path(a.passages)), read(d / "agent_labels.csv"))
    out = Path(a.out)
    write(out / "sample_passages.csv", sample, SAMPLE_FIELDS)
    write(out / "agent_key.csv", key, KEY_FIELDS)
    counts = defaultdict(lambda: defaultdict(int))
    for k in key:
        counts[k["firm_type"]][k["stratum"]] += 1
    print(f"{len(sample)} passages -> {out / 'sample_passages.csv'} (blind), agent labels -> {out / 'agent_key.csv'}")
    for t in NEW_TYPES:
        c = counts[t]
        short = "  (fewer than 10)" if sum(c.values()) < PER_TYPE else ""
        print(f"  {t:26} use {c['use']}, plan {c['plan']}, no use {c['no_use']}{short}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
