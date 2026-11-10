"""Sector AI Use Index: combine firm AI Use Scores into one number per fiscal year (#134).

    AI-EW  equal-weighted:  average of the firms' AI Use Scores
    AI-CW  cap-weighted:    sum(score x public float) / sum(public float)

Public float = market value of shares held by non-affiliates, from the cover page of the same
fiscal year's 10-K (dei:EntityPublicFloat, measured at the end of Q2). It comes from SEC's free
XBRL API; see data/processed/sec/public_float.csv (one row per firm and year, with the accession).

A firm-year counts when we downloaded its 10-K (filings inventory) and have its public float, so
partial years with no 10-K yet (FY2026) drop out on their own. A firm-year with a 10-K but no
substantive AI passage has no row in the scores file; it counts as a score of 0. Years the scores
file doesn't cover at all (e.g. the agent run, FY2025 only) are skipped. Citi is a benchmark and
is left out unless --tickers includes it.

Run from the repo root:
    python3 -m src.index.sector_index                         # 6 PoC firms, consensus scores
    python3 -m src.index.sector_index --scores data/processed/sec/agent_scores_v1.csv
    python3 -m src.index.sector_index --tickers JPM,BAC,COF,WFC,SCHW,PFG,C
For the ~75-firm run, point --scores at its scores file, add its floats to the float CSV and pass
--tickers all.
"""
import argparse
import csv
from collections import defaultdict
from pathlib import Path

SCORES = Path("data/processed/sec/company_scores_consensus.csv")
FLOAT = Path("data/processed/sec/public_float.csv")
INVENTORY = Path("data/processed/sec/filings_inventory.csv")
OUT = Path("data/processed/sec/sector_index.csv")
OUT_FIRMS = Path("data/processed/sec/sector_index_firms.csv")
POC = ["JPM", "BAC", "COF", "WFC", "SCHW", "PFG"]


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build(scores, floats, inventory, tickers=None):
    fl = {(r["ticker"], r["fiscal_year"]): float(r["public_float_usd"]) for r in floats}
    sc = {(r["ticker"], r["fiscal_year"]): float(r["ai_use_score"]) for r in scores}
    tenk = {(r["ticker"], r["period"][:4]) for r in inventory if r["form"].startswith("10-K")}
    years_scored = {fy for _, fy in sc}
    by_year = defaultdict(list)
    for key in sorted(tenk & set(fl)):
        t, fy = key
        if fy not in years_scored or (tickers and t not in tickers):
            continue
        by_year[fy].append((t, sc.get(key, 0.0), fl[key]))
    index, firms = [], []
    for fy in sorted(by_year):
        rows = by_year[fy]
        total = sum(f for _, _, f in rows)
        ew = sum(s for _, s, _ in rows) / len(rows)
        cw = sum(s * f for _, s, f in rows) / total
        index.append({"fiscal_year": fy, "n_firms": len(rows), "ai_ew": round(ew, 1), "ai_cw": round(cw, 1),
                      "total_public_float_usd": int(total), "firms": " ".join(sorted(t for t, _, _ in rows))})
        for t, s, f in sorted(rows, key=lambda x: -x[2]):
            firms.append({"fiscal_year": fy, "ticker": t, "ai_use_score": s, "public_float_usd": int(f),
                          "cw_weight_pct": round(100 * f / total, 1)})
    return index, firms


def write(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--scores", default=str(SCORES), help="firm scores CSV (score_companies output)")
    ap.add_argument("--floats", default=str(FLOAT), help="public float CSV")
    ap.add_argument("--inventory", default=str(INVENTORY), help="filings inventory CSV (which 10-Ks we have)")
    ap.add_argument("--tickers", default=",".join(POC), help="comma-separated tickers, or 'all'")
    ap.add_argument("--out", default=str(OUT), help="index CSV (one row per fiscal year)")
    ap.add_argument("--out-firms", default=str(OUT_FIRMS), help="per-firm weights CSV")
    a = ap.parse_args()
    tickers = None if a.tickers == "all" else set(a.tickers.split(","))
    index, firms = build(read(a.scores), read(a.floats), read(a.inventory), tickers)
    write(Path(a.out), index)
    write(Path(a.out_firms), firms)
    for r in index:
        print(r)
    print(f"-> {a.out}, {a.out_firms}")


if __name__ == "__main__":
    main()
