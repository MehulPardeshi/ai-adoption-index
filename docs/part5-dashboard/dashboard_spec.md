# Dashboard Spec (Part 5)

> **Status:** Streamlit dashboard using the current consensus-based company scores and the six-firm sector index. It supports individual-firm and aggregate views, with limitations visible in the interface. See [`memory/09-decisions-log.md`](../../memory/09-decisions-log.md). Graded: **20%** (client brief), plus the course's hosted-app and demo requirements.

## Audience

Non-technical users: the client (writing a book chapter on AI in retirement), analysts, regulators, and journalists.

## Dashboard views

| View | Data | Purpose |
|---|---|---|
| Sector overview | `data/processed/sec/sector_index.csv` | Compare equal-weighted (AI-EW) and market-cap-weighted (AI-CW) annual scores for the six core firms. |
| Company scores | `data/processed/sec/company_scores_consensus.csv` | Compare firms for a selected fiscal year, review scenario categories, and explore annual score trends. |
| About the data | Both files above | Explain label coverage, methodology boundaries, missing years, and source limitations. |

For this dashboard, “financial sector” means the selected six-company proof-of-concept sample—JPMorgan Chase, Bank of America, Capital One, Wells Fargo, Charles Schwab, and Principal Financial Group. This is not a standard market-sector index or a census of financial services; it spans banks, wealth, and retirement services. Citigroup is an individual-firm benchmark and is excluded from the sector index. The index files cover complete fiscal years only.

## Data contracts and presentation rules

### Company scores

- One row per `(ticker, fiscal_year)` from `company_scores_consensus.csv`; the fields are `company`, `ticker`, `fiscal_year`, `ai_use_score`, `scenarios_with_use`, `readiness_score`, `talk_ratio_pct`, and `substantive_ai_passages`.
- Join company labels by ticker and reject unknown tickers, label mismatches, duplicate company-years, invalid scores, or unknown scenario codes.
- **Label coverage is mixed:** human-agreed labels cover 80 of 277 passages; the remaining passages use AI-draft labels. The interface must say this wherever it presents the scores. Do not describe the full score file as human-labeled.
- These are disclosure-based scores from SEC 10-K and 10-Q passages. They are not verified measures of firm-wide AI adoption.
- FY2026 is partial through June 30, 2026. Hide it in the dashboard while retaining source rows in the CSV. Missing company-years remain unavailable, never zero.
- A score of zero means no scored use was found in the available labeled disclosures; it does not prove that the firm does not use AI.
- Show scenario codes and their human-readable names from the frozen codebook in `src/nlp/taxonomy_v0.py`.
- Provide visible, click-to-open definitions for AI Use Score, Readiness Score, and Talk Ratio (%).
- Provide visible, horizontally aligned circular `?` controls above the sector summary table for fiscal year, firm coverage, both weighting methods, and public float.
- The score data has no evidence IDs or citations. Do not imply that the dashboard supports passage-level audit or evidence drill-down.

### Sector index

- Read existing annual aggregates from `data/processed/sec/sector_index.csv`; do not recalculate weighting in the UI.
- Display both AI-EW and AI-CW series, the number of firms in each year, and the complete fiscal-year coverage.
- AI-EW is the equal-weighted mean of the six core firms' AI Use Scores. AI-CW weights those same scores by public float from SEC filings. See `src/index/sector_index.py` for calculation and missing-data rules.
- The sector index excludes Citigroup, which is retained as a benchmark in the individual company view.
- The supplied index currently has complete-year rows for FY2023–FY2025. Do not show partial years.

## Interpretation and limitations

- “AI Use Score” measures evidence in disclosures, not all of a firm's AI activity or verified deployments.
- The current source combines human-agreed and AI-draft labels; this distinction must remain clear in titles, captions, and the About view.
- Earnings-call transcripts are not included in the index. The data used in this dashboard is derived from SEC filings.
- Keep unavailable years distinct from zero and do not fabricate citations, use cases, or evidence.
- The current company set and sector index are a small proof-of-concept. The sector series should not be presented as a broad industry census.

## Visual and interaction design

- Keep sector-level context and firm-level detail as distinct views, both backed by actual score data.
- Company filters apply only to the company view; the sector overview shows the precomputed six-firm aggregates.
- Use the light-gray canvas, white table surfaces, blue/purple palette, and Merriweather/Inter font stacks in [`src/dashboard/theme.py`](../../src/dashboard/theme.py). Google Fonts is a typography-only request; do not add external data connections.
- Preserve visible, compact data disclosures, keyboard focus states, and Streamlit toolbar controls.

## Validation

- `tests/test_dashboard_scores.py` checks the consensus CSV, ticker and code validation, missing and partial years, and sector-index CSV.
- `tests/test_dashboard_app.py` checks the company and sector views, both sector weighting series, the mixed-label disclosure, and missing-year behavior.
- `tests/test_dashboard_style.py` checks the visual theme and accessibility-related style contracts.
