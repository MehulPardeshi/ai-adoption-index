# S&P 500 Financials run: AI passages, agent labels and scores (#133)

> **Generated** 2026-11-15 by `python3 -m src.index.sector_run_report`. **Status: draft.** The agent was tuned and checked on banks (check 3: 81% exact on 48 unseen passages, 0 overclaims); the other firm types are checked in [labeling round 3](../part3-metrics/labeling_round_3/) before their scores are trusted. Labels the guardrail held count as no use until a person reviews them ([review queue](../../data/processed/sec/sp500_financials/review_queue.csv)).

- **Firms:** 76 S&P 500 Financials constituents, from github.com/datasets/s-and-p-500-companies (from Wikipedia), commit 05c998c, snapshot 2026-11-05 ([firms.csv](../../data/processed/sec/sp500_financials/firms.csv)).
- **Filings:** 10-Ks with periods 2024-01-01 to 2025-12-31 (fiscal years 2024, 2025; FY = year the fiscal year ends). Same paragraph search as the 7-firm data (check 1).
- **Agent:** deepseek-flash@DeepSeek-V4.1-Flash-1017, prompt `classify-v1.5`, guardrails on, confidence bar 0.7.

## Coverage by firm type

| Firm type | Firms | 10-Ks (FY2024 / FY2025) | AI passages | Per 10-K | Public floats |
|---|---|---|---|---|---|
| Banks | 13 | 13 / 13 | 254 | 9.8 | 26 |
| Insurers (incl. brokers, Berkshire) | 24 | 24 / 24 | 496 | 10.3 | 48 |
| Asset managers and brokers | 18 | 18 / 18 | 436 | 12.1 | 36 |
| Payments and consumer finance | 12 | 12 / 12 | 381 | 15.9 | 24 |
| Exchanges and data | 9 | 9 / 9 | 309 | 17.2 | 18 |
| **All** | 76 | 76 / 76 | 1876 | 12.3 | 152 |

**Problems in the download (1):**

- SPGI [public float]: 2024-12-31 10-K 0000064040-25-000052: no public float tagged

**Public float, checked by hand (4)** ([public_float_corrections.csv](../../data/processed/sec/sp500_financials/public_float_corrections.csv)):

- ARES FY2025: **corrected to $32.7B** (estimate: the cover-page figure x 100, a typo in the filing). Cover page and tag both say 'approximately $326,653,262' at a $173.20 closing price, i.e. 1.9 million non-affiliate shares, while 220,902,613 Class A shares were outstanding (Feb 19, 2026) and the FY2024 float was $25.5B. x100 = $32.7B = 188.6 million shares. Estimate; confirm with Ares's own numbers if it matters.
- SPGI FY2024: **corrected to $139.6B** (10-K cover page text (EntityPublicFloat not tagged)). Cover page: market value held by non-affiliates as of June 30, 2024 'was $139.6 billion' (closing price $446.00). Rounded to $0.1B as stated.
- COF FY2025: kept as tagged. x2.6 from FY2024 is real: the cover says 'approximately $135.2 billion' on June 30, 2025 (Capital One bought Discover in 2025).
- HOOD FY2025: kept as tagged. x4.4 from FY2024 is real: the cover says 'approximately $71.3 billion' on June 30, 2025.

Fiscal years not ending in December (FY = the year it ends): BEN (09/30), FDS (08/31), JKHY (06/30), RJF (09/30), V (09/30).

## Agent labels by firm type

Use = D2 or D1 after the guardrail. *Use with no named area* = use labels whose only area is ENT; a high share hints that our 11 areas don't fit that firm type.

| Firm type | Passages | Use | D2 | D1 | P | N | X | Held for review | Use with no named area |
|---|---|---|---|---|---|---|---|---|---|
| Banks | 254 | 47 (19%) | 7 | 40 | 2 | 178 | 27 | 16 (6%) | 27 (57%) |
| Insurers (incl. brokers, Berkshire) | 496 | 60 (12%) | 20 | 40 | 13 | 372 | 51 | 34 (7%) | 24 (40%) |
| Asset managers and brokers | 436 | 73 (17%) | 24 | 49 | 3 | 279 | 81 | 37 (8%) | 39 (53%) |
| Payments and consumer finance | 381 | 98 (26%) | 30 | 68 | 11 | 250 | 22 | 41 (11%) | 44 (45%) |
| Exchanges and data | 309 | 96 (31%) | 24 | 72 | 5 | 174 | 34 | 42 (14%) | 54 (56%) |
| **All** | 1876 | 374 (20%) | 105 | 269 | 34 | 1253 | 215 | 170 (9%) | 188 (50%) |

**Most-used areas** (D2/D1/P labels; ENT = use with no named area), and the enablers (governance, talent, investment) that feed Readiness:

- Banks: ENT 29, RISKM 4, OPS 3, PROD 1 · enablers: GOV 6, TALENT 6
- Insurers (incl. brokers, Berkshire): ENT 39, OPS 5, CREDIT 3, CX 3, PROD 2 · enablers: GOV 17, TALENT 11, INVEST 5
- Asset managers and brokers: ENT 43, CX 8, ADV 8, FRAUD 5, DEV 3 · enablers: GOV 13, TALENT 4, INVEST 2
- Payments and consumer finance: ENT 54, FRAUD 11, CYBER 7, OPS 4, CX 4 · enablers: GOV 14, INVEST 13, TALENT 1
- Exchanges and data: ENT 60, FRAUD 6, MKT 5, OPS 5, PROD 3 · enablers: TALENT 13, INVEST 9, GOV 7

## AI Use Scores by firm type

Mean (median) per fiscal year; firms with no substantive AI passage have no score row and count as 0 in the index.

| Firm type | FY2024 | FY2025 |
|---|---|---|
| Banks | 2.5 (3), n=13 | 3.7 (3), n=13 |
| Insurers (incl. brokers, Berkshire) | 3.2 (2), n=23 | 2.9 (2), n=24 |
| Asset managers and brokers | 6.3 (3), n=18 | 7.8 (3), n=18 |
| Payments and consumer finance | 9.9 (3), n=12 | 11.8 (6), n=12 |
| Exchanges and data | 9.2 (6), n=9 | 10.9 (5), n=9 |

**Highest AI Use Scores, FY2025:**

| Firm | Type | AI Use | Areas with use | Readiness | Talk ratio |
|---|---|---|---|---|---|
| Robinhood Markets (HOOD) | Asset managers and brokers | 48 | ADV CX DEV ENT FRAUD OPS | 33 | 43% |
| Visa Inc. (V) | Payments and consumer finance | 45 | CYBER ENT FRAUD OPS PROD | 33 | 54% |
| Interactive Brokers (IBKR) | Asset managers and brokers | 36 | ADV CX MKT PROD | 11 | 50% |
| Nasdaq, Inc. (NDAQ) | Exchanges and data | 36 | ENT FRAUD MKT SURV | 50 | 54% |
| MSCI (MSCI) | Exchanges and data | 30 | ENT MKT OPS RISKM | 67 | 56% |
| Jack Henry & Associates (JKHY) | Payments and consumer finance | 24 | CX CYBER ENT FRAUD | 33 | 43% |
| Mastercard (MA) | Payments and consumer finance | 24 | CX CYBER ENT OPS | 33 | 66% |
| Assurant (AIZ) | Insurers | 21 | ENT OPS PROD | 72 | 55% |
| BNY Mellon (BNY) | Asset managers and brokers | 21 | DEV ENT PROD | 67 | 83% |
| Citigroup (C) | Banks | 12 | ENT OPS | 33 | 76% |
| Corpay (CPAY) | Payments and consumer finance | 12 | CREDIT OPS | 0 | 71% |
| FactSet (FDS) | Exchanges and data | 9 | ENT | 39 | 62% |

## Sector index preview (all firms in the list)

Computed with `sector_index.build()` (#134) on the agent's 10-K scores. Draft: Yen-Chu owns the index; held labels count as no use; new firm types not yet validated.

| Fiscal year | Firms | AI-EW (equal) | AI-CW (by public float) |
|---|---|---|---|
| 2024 | 76 | 5.6 | 6.3 |
| 2025 | 76 | 6.5 | 8.6 |

Yen-Chu's command for the index files:

```
python3 -m src.index.sector_index --scores data/processed/sec/sp500_financials/agent_scores.csv \
    --floats data/processed/sec/sp500_financials/public_float.csv \
    --inventory data/processed/sec/sp500_financials/filings_inventory.csv --tickers all \
    --out data/processed/sec/sp500_financials/sector_index.csv \
    --out-firms data/processed/sec/sp500_financials/sector_index_firms.csv
```

## Run facts

- Download: 152/152 filings read, 1876 AI passages, 151 public floats, 704.1 s, run 2026-11-15T21:38:00.
- Agent: 1876 passages in 2 passes (a rerun calls the model only for what failed; the rest comes from the cache): 1748 model calls and 1234.6 s in all; tokens in 4732229 (cached 4027904), out 665228. Replies cut off: 2 in earlier passes (retried), 0 in the last.
  - Pass 1, run 2026-11-15T21:38:24: 1746 new model calls, 130 from the cache, 1216.6 s with 6 at a time, 2 cut off.
  - Pass 2, run 2026-11-15T21:59:03: 2 new model calls, 1874 from the cache, 18.0 s with 6 at a time, 0 cut off.
- Model cost: about **$0.52** at off-peak prices (about $1.03 at peak).
- Guardrail: {'pass': 1705, 'needs_review': 170, 'downgraded': 1}.

## Next

1. **Review the 170 held labels** (`review_queue.csv`: fill review_evidence and review_scenarios).
2. **Labeling round 3 (sector pilot):** two people label the 40 sampled passages (10 per new firm type) on their own; same bar as check 3 (overclaim at most 5%). A type that misses gets its own rules and a rerun.
3. **Index (#134):** Yen-Chu runs the command above once the pilot passes.
4. **10-Q question (#157):** this run is 10-K only, as Julie prefers. On our 7 firms, FY2024–25, the 10-Qs change only Citi's FY2025 score (53 with them, 9 without); the team decides whether to add the 10-Qs.

