"""Labeling round 1 scoring: human agreement (check #2) and AI vs. humans (check #3).

Inputs:
  * Human raters: every docs/part3-metrics/labeling_round_1/rater_<name>.csv
    (except the TEMPLATE). Planned raters: Logan, Yen-Chu, Snehal (Mehul runs the analysis), all labeling blind.
  * AI labels: data/processed/sec/passage_labels_v0.csv. These were drafted with
    Claude (AI-assisted, not hand-coded; see PR #49), so they are NOT a human rater.
    They are scored against the humans as an early preview of evaluation check #3.

Check #2: human vs. human, on the evidence level (D2/D1/P/N/X)
  * Cohen's kappa for every pair of human raters (chance-corrected agreement)
  * Fleiss' kappa across all human raters (same idea, for 3+ raters)
  * Quadratic-weighted kappa on the ordered levels N < P < D1 < D2 (near-misses count
    partly; items any rater marked X are left out)
  * "Use vs. no use" kappa (D1/D2 vs. everything else), the call that moves the score
  * Scenario overlap (Jaccard) on items both raters coded D1/D2

Check #3 preview: AI vs. the human majority (items where most humans agree)
  * Accuracy, Cohen's kappa, use/no-use kappa
  * Overclaim rate: the AI says "uses AI" (D1/D2) when the humans don't
  * Underclaim rate: the AI misses use the humans found

Writes disagreements.csv (human vs. human) and ai_vs_humans.csv for the team to discuss.
Run from the repo root:  python3 -m src.eval.irr
Score the agent instead of the draft labels:  python3 -m src.eval.irr --ai-labels data/processed/sec/agent_labels_v1.csv
"""
import argparse
import csv
import itertools
from collections import Counter
from pathlib import Path

ROUND = Path("docs/part3-metrics/labeling_round_1")
AI_LABELS = Path("data/processed/sec/passage_labels_v0.csv")
LEVELS = ["D2", "D1", "P", "N", "X"]
ORDER = {"N": 0, "P": 1, "D1": 2, "D2": 3}
PROVISIONAL_TARGET = 0.60      # "substantial" agreement (Landis & Koch, 1977); revisit after round 1
OVERCLAIM_TARGET = 0.05        # AI may wrongly claim use on at most 5% of passages


def cohen_kappa(a: list, b: list, weights: dict | None = None) -> float:
    """Cohen's kappa; with `weights` (category -> rank) it is quadratic-weighted."""
    n = len(a)
    if n == 0:
        return float("nan")
    cats = sorted(set(a) | set(b), key=lambda c: (weights or {}).get(c, 0))
    if weights:
        k = max(weights.values()) or 1
        w = lambda x, y: 1 - ((weights[x] - weights[y]) / k) ** 2
    else:
        w = lambda x, y: 1.0 if x == y else 0.0
    po = sum(w(x, y) for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[x] * cb[y] * w(x, y) for x in cats for y in cats) / (n * n)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def fleiss_kappa(table: list[list[str]], cats: list[str]) -> float:
    """table[i] = the labels all raters gave item i."""
    n_raters, n_items = len(table[0]), len(table)
    counts = [[row.count(c) for c in cats] for row in table]
    p_j = [sum(r[j] for r in counts) / (n_items * n_raters) for j in range(len(cats))]
    p_i = [(sum(x * x for x in r) - n_raters) / (n_raters * (n_raters - 1)) for r in counts]
    pbar, pe = sum(p_i) / n_items, sum(p * p for p in p_j)
    return 1.0 if pe == 1 else (pbar - pe) / (1 - pe)


def jaccard(x: str, y: str) -> float:
    a = {s.strip().upper() for s in x.split(";") if s.strip()}
    b = {s.strip().upper() for s in y.split(";") if s.strip()}
    return 1.0 if not a and not b else len(a & b) / len(a | b)


def use(level: str) -> str:
    return "USE" if level in ("D1", "D2") else "NO"


def load_humans() -> dict[str, dict[str, dict]]:
    humans = {}
    for path in sorted(ROUND.glob("rater_*.csv")):
        if "TEMPLATE" in path.name:
            continue
        rows = {}
        for r in csv.DictReader(path.open(encoding="utf-8")):
            if r.get("evidence", "").strip():
                r["evidence"] = r["evidence"].strip().upper()
                rows[r["passage_id"]] = r
        humans[path.stem.removeprefix("rater_")] = rows
    return humans


def load_ai(items: set[str], path: Path = AI_LABELS) -> dict[str, dict]:
    return {r["passage_id"]: {"evidence": r["evidence_v0"].strip().upper(), "scenarios": r["scenarios_v0"]}
            for r in csv.DictReader(Path(path).open(encoding="utf-8")) if r["passage_id"] in items}


def human_agreement(humans: dict, items: list[str]) -> None:
    names = list(humans)
    print(f"CHECK #2: human agreement ({len(names)} raters: {', '.join(names)}; {len(items)} items)\n")
    print(f"{'pair':<22}{'kappa':>8}{'weighted':>10}{'use/no-use':>12}{'scenario Jaccard':>18}")
    for x, y in itertools.combinations(names, 2):
        ex = [humans[x][i]["evidence"] for i in items]
        ey = [humans[y][i]["evidence"] for i in items]
        ordinal = [(a, b) for a, b in zip(ex, ey) if a != "X" and b != "X"]
        both = [i for i in items if use(humans[x][i]["evidence"]) == use(humans[y][i]["evidence"]) == "USE"]
        jac = (sum(jaccard(humans[x][i].get("scenarios", ""), humans[y][i].get("scenarios", "")) for i in both) / len(both)
               if both else float("nan"))
        print(f"{x + ' vs ' + y:<22}{cohen_kappa(ex, ey):>8.2f}"
              f"{cohen_kappa([a for a, _ in ordinal], [b for _, b in ordinal], ORDER):>10.2f}"
              f"{cohen_kappa([use(e) for e in ex], [use(e) for e in ey]):>12.2f}{jac:>18.2f}")
    if len(names) >= 3:
        fk = fleiss_kappa([[humans[n][i]["evidence"] for n in names] for i in items], LEVELS)
        print(f"\nFleiss' kappa, all {len(names)} human raters (evidence level): {fk:.2f}")
    print(f"Provisional target: kappa >= {PROVISIONAL_TARGET}. Revisit after round 1.")
    out = ROUND / "disagreements.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["passage_id"] + [f"{n}_evidence" for n in names] + [f"{n}_scenarios" for n in names])
        for i in items:
            ev = [humans[n][i]["evidence"] for n in names]
            if len(set(ev)) > 1:
                w.writerow([i] + ev + [humans[n][i].get("scenarios", "") for n in names])
    print(f"Human disagreements written to {out}\n")


def ai_vs_humans(humans: dict, ai: dict, items: list[str]) -> None:
    names = list(humans)
    majority = {}
    for i in items:
        level, votes = Counter(humans[n][i]["evidence"] for n in names).most_common(1)[0]
        if votes > len(names) / 2:
            majority[i] = level
    print(f"CHECK #3 preview: AI-assisted draft labels vs. human majority ({len(majority)} of {len(items)} items have a majority)\n")
    for n in names:
        a = [ai[i]["evidence"] for i in items]
        h = [humans[n][i]["evidence"] for i in items]
        print(f"  AI vs {n:<10} kappa {cohen_kappa(a, h):.2f}   use/no-use kappa {cohen_kappa([use(x) for x in a], [use(x) for x in h]):.2f}")
    ids = sorted(majority)
    if not ids:
        return
    a = [ai[i]["evidence"] for i in ids]
    m = [majority[i] for i in ids]
    acc = sum(x == y for x, y in zip(a, m)) / len(ids)
    over = sum(use(x) == "USE" and use(y) == "NO" for x, y in zip(a, m)) / len(ids)
    under = sum(use(x) == "NO" and use(y) == "USE" for x, y in zip(a, m)) / len(ids)
    print(f"\n  vs majority: accuracy {acc:.0%}, kappa {cohen_kappa(a, m):.2f}, "
          f"overclaim rate {over:.0%} (target <= {OVERCLAIM_TARGET:.0%}), underclaim rate {under:.0%}")
    out = ROUND / "ai_vs_humans.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["passage_id", "ai_evidence", "human_majority", "type"])
        for i, x, y in zip(ids, a, m):
            if x != y:
                kind = "overclaim" if use(x) == "USE" and use(y) == "NO" else "underclaim" if use(x) == "NO" and use(y) == "USE" else "level differs"
                w.writerow([i, x, y, kind])
    print(f"  AI-vs-human differences written to {out}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ai-labels", default=str(AI_LABELS), help="AI labels CSV (default: the AI-assisted draft labels)")
    args = ap.parse_args()
    humans = load_humans()
    if not humans:
        print("No completed rater_<name>.csv files yet in", ROUND)
        return
    items = sorted(set.intersection(*(set(r) for r in humans.values())))
    bad = [(n, i, humans[n][i]["evidence"]) for n in humans for i in items if humans[n][i]["evidence"] not in LEVELS]
    if bad:
        print("Invalid evidence codes (fix first):", bad[:10])
        return
    if len(humans) >= 2:
        human_agreement(humans, items)
    else:
        print("Only one human rater so far; check #2 needs at least two.\n")
    ai_vs_humans(humans, load_ai(set(items), args.ai_labels), items)


if __name__ == "__main__":
    main()
