"""Score each company per fiscal year from Taxonomy v0 labels (DRAFT method).

    AI Use Score (0-100)    for each of the 11 use-case scenarios, take the
                            strongest evidence that year (D2=3, D1=1, P=0.5),
                            add them up, divide by 33
    Readiness Score (0-100) the same over the 3 enablers, divided by 9
    Talk ratio (%)          share of substantive AI passages (not X) with no
                            evidence of own use (N)

Run from the repo root:
    python3 -m src.index.score_companies
Writes data/processed/sec/company_scores_v0.csv
"""
import csv
from collections import defaultdict
from pathlib import Path

from src.nlp.taxonomy_v0 import ENABLERS, EVIDENCE_WEIGHT, LABELS, SCENARIOS, read

OUT = Path("data/processed/sec/company_scores_v0.csv")


def score(labels):
    best = defaultdict(dict)            # (ticker, year) -> {scenario: weight}
    talk = defaultdict(lambda: [0, 0])  # (ticker, year) -> [N count, substantive]
    names = {}
    for r in labels:
        key = (r["ticker"], r["period"][:4])  # all 7 companies use calendar fiscal years
        names[r["ticker"]] = r["company"]
        if r["evidence_v0"] != "X":
            talk[key][1] += 1
            talk[key][0] += r["evidence_v0"] == "N"
        w = EVIDENCE_WEIGHT.get(r["evidence_v0"], 0.0)
        for s in filter(None, r["scenarios_v0"].split(";")):
            best[key][s] = max(best[key].get(s, 0.0), w)

    out = []
    for key in sorted(talk):
        b, (n, sub) = best[key], talk[key]
        use = sum(v for s, v in b.items() if s in SCENARIOS)
        ready = sum(v for s, v in b.items() if s in ENABLERS)
        out.append({
            "company": names[key[0]], "ticker": key[0], "fiscal_year": key[1],
            "ai_use_score": round(100 * use / (3 * len(SCENARIOS))),
            "scenarios_with_use": " ".join(sorted(s for s in b if s in SCENARIOS)),
            "readiness_score": round(100 * ready / (3 * len(ENABLERS))),
            "talk_ratio_pct": round(100 * n / sub) if sub else "",
            "substantive_ai_passages": sub,
        })
    return out


def main():
    rows = score(read(LABELS))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(r)
    print(f"-> {OUT}")


if __name__ == "__main__":
    main()
