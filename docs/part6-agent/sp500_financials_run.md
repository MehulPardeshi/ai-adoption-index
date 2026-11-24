# S&P 500 Financials run: AI passages, agent labels and scores (#133)

> **Generated** 2026-11-21 by `python3 -m src.index.sector_run_report`. **Status: draft.** The agent was tuned and checked on banks (check 3: 81% exact on 48 unseen passages, 0 overclaims); the other firm types are checked in [labeling round 3](../part3-metrics/labeling_round_3/) before their scores are trusted. Labels the guardrail held count as no use until a person reviews them ([review queue](../../data/processed/sec/sp500_financials/review_queue.csv)).

- **Firms:** 76 S&P 500 Financials constituents, from github.com/datasets/s-and-p-500-companies (from Wikipedia), commit 05c998c, snapshot 2026-11-05 ([firms.csv](../../data/processed/sec/sp500_financials/firms.csv)).
- **Filings:** 10-K, 10-Qs (fiscal years 2024, 2025; FY = year the fiscal year ends; a 10-Q counts in the fiscal year it belongs to). Same paragraph search as the 7-firm data (check 1).
- **Agent:** deepseek-flash@DeepSeek-V4.1-Flash-1017, prompt `classify-v1.5`, guardrails on, confidence bar 0.7.

## Coverage by firm type

| Firm type | Firms | 10-Ks (FY2024 / FY2025) | 10-Qs | AI passages (10-K / 10-Q) | Per 10-K | Public floats |
|---|---|---|---|---|---|---|
| Banks | 13 | 13 / 13 | 78 | 254 / 35 | 9.8 | 26 |
| Insurers (incl. brokers, Berkshire) | 24 | 24 / 24 | 144 | 496 / 111 | 10.3 | 48 |
| Asset managers and brokers | 18 | 18 / 18 | 106 | 436 / 117 | 12.1 | 36 |
| Payments and consumer finance | 12 | 12 / 12 | 72 | 381 / 124 | 15.9 | 24 |
| Exchanges and data | 9 | 9 / 9 | 54 | 309 / 90 | 17.2 | 18 |
| **All** | 76 | 76 / 76 | 454 | 1876 / 477 | 12.3 | 152 |

**Problems in the download (1):**

- SPGI [public float]: 2024-12-31 10-K 0000064040-25-000052: no public float tagged

**Public float, checked by hand (4)** ([public_float_corrections.csv](../../data/processed/sec/sp500_financials/public_float_corrections.csv)):

- ARES FY2025: **corrected to $32.7B** (estimate: the cover-page figure x 100, a typo in the filing). Cover page and tag both say 'approximately $326,653,262' at a $173.20 closing price, i.e. 1.9 million non-affiliate shares, while 220,902,613 Class A shares were outstanding (Feb 19, 2026) and the FY2024 float was $25.5B. x100 = $32.7B = 188.6 million shares. Estimate; confirm with Ares's own numbers if it matters.
- SPGI FY2024: **corrected to $139.6B** (10-K cover page text (EntityPublicFloat not tagged)). Cover page: market value held by non-affiliates as of June 30, 2024 'was $139.6 billion' (closing price $446.00). Rounded to $0.1B as stated.
- COF FY2025: kept as tagged. x2.6 from FY2024 is real: the cover says 'approximately $135.2 billion' on June 30, 2025 (Capital One bought Discover in 2025).
- HOOD FY2025: kept as tagged. x4.4 from FY2024 is real: the cover says 'approximately $71.3 billion' on June 30, 2025.

Fiscal years not ending in December (FY = the year it ends): BEN (09/30), FDS (08/31), JKHY (06/30), RJF (09/30), V (09/30). Their 10-Qs count in the fiscal year they belong to (with a Sep 30 year end, the quarter to Dec 31, 2024 is FY2025).

## Agent labels by firm type

Use = D2 or D1 after the guardrail. *Use with no named area* = use labels whose only area is ENT; a high share hints that our 11 areas don't fit that firm type.

| Firm type | Passages | Use | D2 | D1 | P | N | X | Held for review | Use with no named area |
|---|---|---|---|---|---|---|---|---|---|
| Banks | 289 | 56 (19%) | 14 | 42 | 2 | 202 | 29 | 16 (6%) | 28 (50%) |
| Insurers (incl. brokers, Berkshire) | 607 | 63 (10%) | 23 | 40 | 14 | 463 | 67 | 35 (6%) | 24 (38%) |
| Asset managers and brokers | 553 | 111 (20%) | 41 | 70 | 3 | 342 | 97 | 41 (7%) | 58 (52%) |
| Payments and consumer finance | 505 | 121 (24%) | 37 | 84 | 13 | 343 | 28 | 57 (11%) | 58 (48%) |
| Exchanges and data | 399 | 121 (30%) | 30 | 91 | 17 | 212 | 49 | 51 (13%) | 71 (59%) |
| **All** | 2353 | 472 (20%) | 145 | 327 | 49 | 1562 | 270 | 200 (8%) | 239 (51%) |

**Most-used areas** (D2/D1/P labels; ENT = use with no named area), and the enablers (governance, talent, investment) that feed Readiness:

- Banks: ENT 30, PROD 4, RISKM 4, OPS 3, DEV 2 · enablers: GOV 8, TALENT 6
- Insurers (incl. brokers, Berkshire): ENT 39, OPS 5, CREDIT 3, CX 3, PROD 2 · enablers: GOV 17, TALENT 11, INVEST 9
- Asset managers and brokers: ENT 62, CX 14, FRAUD 11, ADV 9, DEV 8 · enablers: GOV 23, INVEST 9, TALENT 4
- Payments and consumer finance: ENT 69, FRAUD 11, CYBER 7, RISKM 4, OPS 4 · enablers: INVEST 22, GOV 14, TALENT 1
- Exchanges and data: ENT 87, FRAUD 9, PROD 5, MKT 5, OPS 5 · enablers: TALENT 16, INVEST 11, GOV 7

## AI Use Scores by firm type

Mean (median) per fiscal year; firms with no substantive AI passage have no score row and count as 0 in the index.

| Firm type | FY2024 | FY2025 |
|---|---|---|
| Banks | 2.5 (3), n=13 | 6.5 (3), n=13 |
| Insurers (incl. brokers, Berkshire) | 3.2 (2), n=23 | 2.9 (2), n=24 |
| Asset managers and brokers | 6.3 (3), n=18 | 7.8 (3), n=18 |
| Payments and consumer finance | 9.9 (3), n=12 | 11.8 (6), n=12 |
| Exchanges and data | 9.4 (6), n=9 | 12.1 (5), n=9 |

**Highest AI Use Scores, FY2025:**

| Firm | Type | AI Use | Areas with use | Readiness | Talk ratio |
|---|---|---|---|---|---|
| Citigroup (C) | Banks | 48 | CX DEV ENT OPS PROD SURV | 33 | 62% |
| Robinhood Markets (HOOD) | Asset managers and brokers | 48 | ADV CX DEV ENT FRAUD OPS | 67 | 40% |
| Visa Inc. (V) | Payments and consumer finance | 45 | CYBER ENT FRAUD OPS PROD | 33 | 44% |
| Interactive Brokers (IBKR) | Asset managers and brokers | 36 | ADV CX MKT PROD | 11 | 67% |
| Nasdaq, Inc. (NDAQ) | Exchanges and data | 36 | ENT FRAUD MKT SURV | 50 | 52% |
| MSCI (MSCI) | Exchanges and data | 30 | ENT MKT OPS RISKM | 67 | 56% |
| Jack Henry & Associates (JKHY) | Payments and consumer finance | 24 | CX CYBER ENT FRAUD | 33 | 43% |
| Mastercard (MA) | Payments and consumer finance | 24 | CX CYBER ENT OPS | 33 | 69% |
| Assurant (AIZ) | Insurers | 21 | ENT OPS PROD | 72 | 55% |
| BNY Mellon (BNY) | Asset managers and brokers | 21 | DEV ENT PROD | 67 | 82% |
| FactSet (FDS) | Exchanges and data | 18 | CX ENT | 39 | 53% |
| Corpay (CPAY) | Payments and consumer finance | 12 | CREDIT OPS | 0 | 71% |

## Sector index preview (all firms in the list)

Computed with `sector_index.build()` (#134) on the agent's 10-K and 10-Q scores. Draft: Yen-Chu owns the index; held labels count as no use; new firm types not yet validated.

| Fiscal year | Firms | AI-EW (equal) | AI-CW (by public float) |
|---|---|---|---|
| 2024 | 76 | 5.6 | 6.3 |
| 2025 | 76 | 7.2 | 9.4 |

Yen-Chu's command for the index files:

```
python3 -m src.index.sector_index --scores data/processed/sec/sp500_financials/agent_scores.csv \
    --floats data/processed/sec/sp500_financials/public_float.csv \
    --inventory data/processed/sec/sp500_financials/filings_inventory.csv --tickers all \
    --out data/processed/sec/sp500_financials/sector_index.csv \
    --out-firms data/processed/sec/sp500_financials/sector_index_firms.csv
```

## Run facts

- Download: 606/606 filings read, 2353 AI passages, 152 public floats, 989.5 s, run 2026-11-21T02:27:29.
- Agent: 2353 passages, 59 new model calls, 2294 from the cache, 34.2 s with 6 at a time, run 2026-11-21T16:12:24; tokens in 164258 (cached 137088), out 22579, 0 cut off.
- Model cost: about **$0.02** at off-peak prices (about $0.04 at peak).
- Guardrail: {'pass': 2152, 'needs_review': 200, 'downgraded': 1}.

## Next

1. **Review the 200 held labels** (`review_queue.csv`: fill review_evidence and review_scenarios).
2. **Labeling round 3 (sector pilot):** two people label the 40 sampled passages (10 per new firm type) on their own; same bar as check 3 (overclaim at most 5%). A type that misses gets its own rules and a rerun.
3. **Index (#134):** Yen-Chu runs the command above once the pilot passes.
4. **10-Qs (#157):** this run includes the 10-Qs (team decision Nov 19: Citi's specific AI uses are only in its 10-Qs, and repeats add no points since each area counts once a year). Julie approved on Nov 23.

