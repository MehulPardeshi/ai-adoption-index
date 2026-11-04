"""Score each company per fiscal year from Taxonomy v0 labels (DRAFT method).

    AI Use Score (0-100)    for each of the 11 use-case scenarios, take the
                            strongest evidence that year (D2=3, D1=1, P=0.5),
                            add them up, plus ENT once (see below), divide by 33
    Readiness Score (0-100) the same over the 3 enablers, divided by 9
    Talk ratio (%)          share of substantive AI passages (not X) with no
                            evidence of own use (N)

Run from the repo root:
    python3 -m src.index.score_companies
    python3 -m src.index.score_companies --labels data/processed/sec/agent_labels_v1.csv \
        --out data/processed/sec/agent_scores_v1.csv          # score the agent's labels
Writes data/processed/sec/company_scores_v0.csv by default.

ENT ("uses AI, area not named") adds its weight once to the AI Use Score (team decision
Oct 25, frozen Oct 27, #33); the denominator stays 33 and the score is capped at 100.
--no-ent reproduces the earlier rule (ENT = 0 points) as a sensitivity check.
"""
import argparse
import csv
from collections import defaultdict
from pathlib import Path

from src.nlp.taxonomy_v0 import ENABLERS, EVIDENCE_WEIGHT, LABELS, SCENARIOS, read

OUT = Path("data/processed/sec/company_scores_v0.csv")


def score(labels, ent_counts=True):
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
        use = sum(v for s, v in b.items() if s in SCENARIOS or (ent_counts and s == "ENT"))
        ready = sum(v for s, v in b.items() if s in ENABLERS)
        out.append({
            "company": names[key[0]], "ticker": key[0], "fiscal_year": key[1],
            "ai_use_score": min(100, round(100 * use / (3 * len(SCENARIOS)))),
            "scenarios_with_use": " ".join(sorted(s for s in b if s in SCENARIOS or (ent_counts and s == "ENT" and b[s] > 0))),
            "readiness_score": round(100 * ready / (3 * len(ENABLERS))),
            "talk_ratio_pct": round(100 * n / sub) if sub else "",
            "substantive_ai_passages": sub,
        })
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--labels", default=str(LABELS), help="labels CSV (default: the v0 draft labels)")
    ap.add_argument("--out", default=str(OUT), help="scores CSV to write")
    ap.add_argument("--no-ent", action="store_true",
                    help="sensitivity check: ENT earns 0 points (the rule before Oct 25)")
    ap.add_argument("--ent-counts", action="store_true", help=argparse.SUPPRESS)  # now the default; kept for old commands
    a = ap.parse_args()
    out_path = Path(a.out)
    rows = score(read(a.labels), ent_counts=not a.no_ent)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(r)
    print(f"-> {out_path}")


if __name__ == "__main__":
    main()
