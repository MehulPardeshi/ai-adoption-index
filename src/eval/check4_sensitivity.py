"""Evaluation check #4: do the scores make sense? (sensitivity + benchmark)

(a) Sensitivity: rescore FY2025 (the most complete year: Q1-Q3 10-Qs + the 10-K) under
    alternative rules and see whether the company ranking moves.
      baseline   D2/D1/P = 3/1/0.5, ENT counts once (team rule, frozen Oct 27)
      no_ent     ENT = 0 (the rule before Oct 25)
      w2         D2 = 2 instead of 3
      strict     only specific uses count (D2 only; Julie's "strict measure" question)
    Rank agreement with the baseline: Spearman's rho (ties averaged).
(b) Benchmark: FY2023 10-Ks, the latest year in the Dong et al. AI Intensity data
    (data/processed/sec/shu_run/dong_baseline_6firms.csv). Dong counts AI words, so we
    expect it to follow our talk volume (AI passages) more than our use score.

Labels: the AI-assisted v0 draft labels by default; rerun with the human consensus set
once adjudication is done (--labels).
Run from the repo root:  python3 -m src.eval.check4_sensitivity
"""
import argparse
import csv
from pathlib import Path

from src.index.score_companies import score
from src.nlp.taxonomy_v0 import EVIDENCE_WEIGHT, LABELS, read

DONG = Path("data/processed/sec/shu_run/dong_baseline_6firms.csv")
VARIANTS = ["baseline", "no_ent", "w2", "strict"]


def ranks(values: dict) -> dict:
    order = sorted(values, key=lambda k: -values[k])
    out, i = {}, 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        for k in order[i:j + 1]:
            out[k] = (i + j) / 2 + 1
        i = j + 1
    return out


def spearman(x: dict, y: dict) -> float:
    keys = sorted(set(x) & set(y))
    rx, ry = ranks({k: x[k] for k in keys}), ranks({k: y[k] for k in keys})
    mx, my = sum(rx.values()) / len(keys), sum(ry.values()) / len(keys)
    cov = sum((rx[k] - mx) * (ry[k] - my) for k in keys)
    vx = sum((rx[k] - mx) ** 2 for k in keys) ** 0.5
    vy = sum((ry[k] - my) ** 2 for k in keys) ** 0.5
    return cov / (vx * vy) if vx and vy else float("nan")


def use_scores(rows, year, variant, forms=None):
    rows = [dict(r) for r in rows if r["period"][:4] == year and (forms is None or r["form"] in forms)]
    if variant == "strict":  # only specific uses count
        for r in rows:
            if r["evidence_v0"] in ("D1", "P"):
                r["evidence_v0"] = "N"
    saved = dict(EVIDENCE_WEIGHT)
    if variant == "w2":
        EVIDENCE_WEIGHT["D2"] = 2.0  # the scorer reads this dict
    try:
        scored = score(rows, ent_counts=variant != "no_ent")
    finally:
        EVIDENCE_WEIGHT.update(saved)
    return {s["ticker"]: s for s in scored}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--labels", default=str(LABELS), help="labels CSV (default: the v0 draft labels)")
    args = ap.parse_args()
    rows = read(args.labels)

    print("CHECK #4a: sensitivity of the FY2025 AI Use Score (draft labels)\n")
    table = {v: {t: s["ai_use_score"] for t, s in use_scores(rows, "2025", v).items()} for v in VARIANTS}
    tickers = sorted(table["baseline"], key=lambda t: -table["baseline"][t])
    print(f"{'company':<8}" + "".join(f"{v:>10}" for v in VARIANTS))
    for t in tickers:
        print(f"{t:<8}" + "".join(f"{table[v].get(t, 0):>10}" for v in VARIANTS))
    no_citi = {v: {t: x for t, x in table[v].items() if t != "C"} for v in VARIANTS}
    for label, t in (("all 7 firms", table), ("6 PoC firms (no Citi)", no_citi)):
        rhos = {v: spearman(t["baseline"], t[v]) for v in VARIANTS if v != "baseline"}
        print(f"Spearman rho vs. baseline, {label:<22}" + "   ".join(
            f"{v} {r:.2f}" if r == r else f"{v} n/a (all scores 0)" for v, r in rhos.items()))

    print("\nCHECK #4b: benchmark vs. Dong et al. AI Intensity, FY2023 10-Ks (6 PoC firms)\n")
    dong = {r["ticker"]: float(r["AI Intensity (All)"]) for r in csv.DictReader(DONG.open(encoding="utf-8"))
            if r["filing_date"][:4] == "2024"}  # 10-K filed early 2024 = FY2023
    ours = use_scores(rows, "2023", "baseline", forms={"10-K"})
    talk = {t: ours[t]["substantive_ai_passages"] if t in ours else 0 for t in dong}
    use = {t: ours[t]["ai_use_score"] if t in ours else 0 for t in dong}
    print(f"{'company':<8}{'Dong (All)':>12}{'our AI passages':>17}{'our use score':>15}")
    for t in sorted(dong, key=lambda t: -dong[t]):
        print(f"{t:<8}{dong[t]:>12.3f}{talk[t]:>17}{use[t]:>15}")
    print(f"\nSpearman rho: Dong vs. our talk volume {spearman(dong, talk):.2f} · "
          f"Dong vs. our use score {spearman(dong, use):.2f}  (n = 6, indicative only)")


if __name__ == "__main__":
    main()
