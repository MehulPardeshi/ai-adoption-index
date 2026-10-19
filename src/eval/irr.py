"""Inter-rater reliability (IRR) for labeling round 1 (evaluation check #2).

Compares every rater file in docs/part3-metrics/labeling_round_1/rater_*.csv
(except the TEMPLATE) with each other and with the AI-assisted draft labels
(data/processed/sec/passage_labels_v0.csv, treated as rater "ai_draft"; these
were drafted with Claude, not hand-coded, so they are the AI side of check #3).

Reports, for the evidence level (D2/D1/P/N/X):
  * Cohen's kappa for every pair of raters (chance-corrected agreement)
  * Fleiss' kappa across all raters (same idea, for 3+ raters)
  * Quadratic-weighted kappa per pair on the ordered levels N < P < D1 < D2
    (near-misses count partly; items any rater marked X are left out)
  * "Use vs no use" kappa (D1/D2 vs everything else): the call that moves the score
And for scenarios (Label A): mean Jaccard overlap on items both raters coded D1/D2.

Writes a disagreements file for the team to discuss.
Run from the repo root:  python3 -m src.eval.irr
"""
import csv
import itertools
from collections import Counter
from pathlib import Path

ROUND = Path("docs/part3-metrics/labeling_round_1")
DRAFT = Path("data/processed/sec/passage_labels_v0.csv")
LEVELS = ["D2", "D1", "P", "N", "X"]
ORDER = {"N": 0, "P": 1, "D1": 2, "D2": 3}
PROVISIONAL_TARGET = 0.60  # "substantial" agreement (Landis & Koch, 1977); revisit after round 1


def cohen_kappa(a: list, b: list, weights: dict | None = None) -> float:
    """Cohen's kappa; with `weights` (category -> rank) it is quadratic-weighted."""
    cats = sorted(set(a) | set(b), key=lambda c: (weights or {}).get(c, 0))
    n = len(a)
    if n == 0:
        return float("nan")
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
    n_raters = len(table[0])
    n_items = len(table)
    counts = [[row.count(c) for c in cats] for row in table]
    p_j = [sum(r[j] for r in counts) / (n_items * n_raters) for j in range(len(cats))]
    p_i = [(sum(x * x for x in r) - n_raters) / (n_raters * (n_raters - 1)) for r in counts]
    pbar, pe = sum(p_i) / n_items, sum(p * p for p in p_j)
    return 1.0 if pe == 1 else (pbar - pe) / (1 - pe)


def jaccard(x: str, y: str) -> float:
    a = {s.strip().upper() for s in x.split(";") if s.strip()}
    b = {s.strip().upper() for s in y.split(";") if s.strip()}
    return 1.0 if not a and not b else len(a & b) / len(a | b)


def load() -> dict[str, dict[str, dict]]:
    raters: dict[str, dict[str, dict]] = {}
    for path in sorted(ROUND.glob("rater_*.csv")):
        if "TEMPLATE" in path.name:
            continue
        rows = {r["passage_id"]: r for r in csv.DictReader(path.open(encoding="utf-8")) if r.get("evidence", "").strip()}
        raters[path.stem.removeprefix("rater_")] = rows
    items = set.intersection(*(set(r) for r in raters.values())) if raters else set()
    draft = {r["passage_id"]: {"evidence": r["evidence_v0"], "scenarios": r["scenarios_v0"]}
             for r in csv.DictReader(DRAFT.open(encoding="utf-8")) if r["passage_id"] in items}
    raters = {"ai_draft": draft, **raters}
    for rows in raters.values():
        for r in rows.values():
            r["evidence"] = r["evidence"].strip().upper()
    return raters


def main() -> None:
    raters = load()
    if len(raters) < 2:
        print("Need at least one completed rater_<name>.csv in", ROUND)
        return
    items = sorted(set.intersection(*(set(r) for r in raters.values())))
    names = list(raters)
    bad = [(n, i, raters[n][i]["evidence"]) for n in names for i in items if raters[n][i]["evidence"] not in LEVELS]
    if bad:
        print("Invalid evidence codes (fix first):", bad[:10])
        return
    print(f"Items labeled by all {len(names)} raters ({', '.join(names)}): {len(items)}\n")
    use = lambda e: "USE" if e in ("D1", "D2") else "NO"
    print(f"{'pair':<22}{'kappa':>8}{'weighted':>10}{'use/no-use':>12}{'scenario Jaccard':>18}")
    for x, y in itertools.combinations(names, 2):
        ex = [raters[x][i]["evidence"] for i in items]
        ey = [raters[y][i]["evidence"] for i in items]
        k = cohen_kappa(ex, ey)
        ordinal = [(a, b) for a, b in zip(ex, ey) if a != "X" and b != "X"]
        kw = cohen_kappa([a for a, _ in ordinal], [b for _, b in ordinal], ORDER)
        ku = cohen_kappa([use(e) for e in ex], [use(e) for e in ey])
        both = [i for i in items if use(raters[x][i]["evidence"]) == use(raters[y][i]["evidence"]) == "USE"]
        jac = sum(jaccard(raters[x][i].get("scenarios", ""), raters[y][i].get("scenarios", "")) for i in both) / len(both) if both else float("nan")
        print(f"{x + ' vs ' + y:<22}{k:>8.2f}{kw:>10.2f}{ku:>12.2f}{jac:>18.2f}")
    if len(names) >= 3:
        fk = fleiss_kappa([[raters[n][i]["evidence"] for n in names] for i in items], LEVELS)
        print(f"\nFleiss' kappa, all {len(names)} raters (evidence level): {fk:.2f}")
    print(f"\nProvisional target: kappa >= {PROVISIONAL_TARGET} ('substantial'). Revisit after round 1.")
    out = ROUND / "disagreements.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["passage_id"] + [f"{n}_evidence" for n in names] + [f"{n}_scenarios" for n in names])
        for i in items:
            ev = [raters[n][i]["evidence"] for n in names]
            if len(set(ev)) > 1:
                w.writerow([i] + ev + [raters[n][i].get("scenarios", "") for n in names])
    print(f"Disagreements written to {out}")


if __name__ == "__main__":
    main()
