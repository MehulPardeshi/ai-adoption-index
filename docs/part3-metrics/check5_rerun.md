# Check 5: can someone else reproduce it?

> **Status, Nov 3:** Mehul's dry run matched. **The check still needs a teammate who didn't build the pipeline** (Logan or Snehal, per the evaluation plan); a run by its owner doesn't count as independent (#102).

## Dry run (Nov 3, Mehul with Claude; not independent)
Fresh download from SEC EDGAR plus a fresh clone of the repo:

| What | Result |
|---|---|
| Filings | All 74 official filings found, with identical paragraph counts |
| AI passages | All 277 official passage IDs reproduced, none missing |
| Labeling samples (round 1 + round 2) | 80 of 80 passages have identical text |
| Scores (`company_scores_v0.csv`) | Identical |
| Extra in the rerun | 3 Citi filings before Q3 2024 and their 5 passages, outside the official set by design (the FY2023 backfill covered the six PoC firms only) |

## For the teammate (about 20 minutes, mostly waiting; uses about 850 MB)
Use a folder **outside the repo** for `<folder>`, and follow only these steps. Note anything that's confusing or missing: that's part of the result.
```bash
git clone https://github.com/MehulPardeshi/ai-adoption-index.git
cd ai-adoption-index
python3 -m pip install -r requirements.txt
python3 src/edgar/download_sec_filings.py --data <folder> --start 2023-12-31 --end 2026-06-30
python3 -m src.index.score_companies --out <folder>/scores.csv
python3 -m src.eval.check5_compare --data <folder>
```
Post the last command's output on #102. It should end with `RESULT: MATCH`.
