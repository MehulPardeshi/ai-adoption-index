# Check 5: can someone else reproduce it?

> **Status, Nov 8: passed.** Logan, who didn't build the pipeline, reran it from a fresh clone and got `RESULT: MATCH` (#102). Mehul's Nov 3 dry run matched too.

## Independent rerun (Nov 8, Logan)
| What | Result |
|---|---|
| Setup | Fresh clone at commit `4c3fd3e`, Python 3.12.4 in a clean virtual environment, on a Mac; dependency check passed |
| Fresh SEC download | 77 filings, 282 AI passages: the official 74 and 277 plus the 3 Citi filings and 5 passages expected below |
| Labeling samples | No text differences |
| Scores | Identical |
| Final line | `RESULT: MATCH` |

Logan followed the steps below with help from an AI coding assistant and hit no errors. **What this shows:** anyone can redownload the filings and rebuild the same passages and scores from the saved labels. **What it doesn't:** it doesn't rerun the AI labeling itself (that is checked against people in rounds 1 and 2).

## Dry run (Nov 3, Mehul; not independent)
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
