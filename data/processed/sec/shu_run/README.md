# Shu's SEC run (2026-10-17) — independent cross-check of the SEC test run

> **Oct 22 (#53):** the two runs are consolidated. `data/interim/sec/ai_passages.csv` is the single running dataset (Yen-Chu's run plus the FY2023 / early-2024 filings re-parsed with her code). This folder stays as the independent cross-check and as the home of `dong_baseline_6firms.csv`.

Second, independent pass over SEC 10-K/10-Q filings for the six PoC firms, done in parallel with Yen-Chu's test run (PR #43). Same source (EDGAR), different code path and slightly different window and keyword list, so the two runs serve as a reproducibility check for the evaluation plan (`docs/part3-metrics/evaluation_plan.md`).

| File | What it is |
|---|---|
| `filings_manifest.csv` | 66 filings: JPM, BAC, COF, WFC, SCHW, PFG; every 10-K and 10-Q filed 2024-01-01 → 2026-08-07 (3 × 10-K + 8 × 10-Q per firm). Accession, filing date, report period, primary document, EDGAR URL. |
| `filing_ai_counts.csv` | Per filing: word count, AI keyword hits (total and by keyword), hits per 1,000 words, number of extracted passages. |
| `dong_baseline_6firms.csv` | The six firms' rows (141 firm-year filings, 2010–2024) from the Dong et al. AI Intensity dataset (github.com/FengDong-Elon/ai-intensity-dataset): 8 category counts, AI Intensity (Core) and (All). **Cite:** Dong, Doukas & Zhang, "Artificial Intelligence Engagement, Firm Value, and Risk Transformation", SSRN 6051714. |
| `../../interim/sec/shu_run/ai_passages_all.json` | 274 AI-related passages with ~900 chars of context, plus 169 de-duplicated `unique_passages` with the list of filings where the same text recurs. Each has accession, document, approximate Item, position, matched keyword. Verbatim SEC text — same basis as `data/interim/sec/ai_passages.csv`; final retention per the ethics memo (#26). |
| `../../../src/edgar/fetch_filings_shu.py` | Re-downloads every primary-document part for the manifest (handles WFC's `_d2.htm` split). Raw HTML stays in `data/raw/` (gitignored). |
| (removed Oct 22) | Shu's draft categories were merged into `docs/part2-taxonomy/sec_test_run_taxonomy_v0_DRAFT.md` (mapping table in section 4, #33). |

## Differences from the SEC test run (PR #43)

| | Yen-Chu (#43) | Shu (this run) |
|---|---|---|
| Firms | 6 + Citi | 6 |
| Window | filed 2024-07-01 → 2026-06-30 (56 filings) | filed 2024-01-01 → 2026-08-07 (66 filings; adds FY2023 10-Ks and the Aug 2026 10-Qs) |
| Keywords | 17 strong + 3 weak terms | 17 terms (no weak terms; adds `generative`, `virtual assistant`, `robotic process automation`) |
| Unit | paragraph | keyword-centred window, de-duplicated across quarters |
| WFC 10-K | — | reads both `wfc-YYYYMMDD.htm` and `_d2.htm` (the annual-report body) |

Hit counts are not a replication of Dong et al.'s ~500-term dictionary; word counts also differ (we count alphabetic tokens in rendered text; their tokenizer is not published).

## Findings worth carrying into the taxonomy and the Julie meeting

1. **Dong baseline fails on WFC.** Their dataset gives WFC 0 every year; their WFC word count (~117.8k) matches the first file plus exhibits and excludes the ~110k-word `_d2.htm` body, so their parser appears to have missed it. Our pass finds 5–12 AI mentions per WFC 10-K. PFG's 0 for FY2023 is genuine (we also find 0).
2. **10-Qs carry almost no AI text** (0–2 hits each, mostly forward-looking boilerplate). Quarterly granularity will have to come from earnings calls (#34).
3. **Mentions roughly doubled or tripled FY2023 → FY2025 at every firm**, mostly new or expanded risk factors rather than new deployments. Roughly 85 % of unique passages are risk / regulation / cyber-threat language, not "we use AI for X".
