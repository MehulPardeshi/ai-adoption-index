# Dashboard Spec (Part 5)

> **Status:** requirements captured from the brief. **Streamlit was selected on 2026-10-04.** The dashboard now has two intentionally separate data tracks: preliminary annual SEC disclosure scores and a fictional interface walkthrough. The final index data contract and methodology remain open. See [`memory/09-decisions-log.md`](../../memory/09-decisions-log.md).
> Background: [`memory/07-dashboard-spec.md`](../../memory/07-dashboard-spec.md). Graded: **20%** (client brief), plus the course's hosted-app and demo requirements.

## Audience
Non-technical users: the client (writing a book chapter on AI in retirement), analysts, regulators, journalists.

## Required views
| # | View | Chart type (brief) | Data needed | Notes / open questions |
|---|---|---|---|---|
| 1 | Index trend per firm + peer-group average | Line | Index by firm-sector-quarter | |
| 2 | Category breakdown per firm per quarter | Stacked bar or treemap | Category counts/shares | |
| 3 | Sentiment trend | Line | Sentiment by firm-quarter | |
| 4 | Firm comparison across categories | Radar / spider | Category scores per firm | |
| 5 | Evidence drill-down | Table / side panel | Paraphrased/cited evidence per data point | Must support auditability |

## Required filters
- **Sector** (multi-select; firms can carry multiple tags)
- **Firm**
- A **retirement-only view** is achievable via the sector filter, without removing retirement firms from the cross-sector index

## Two data tracks and guardrails
- The interface fixture includes the six proof-of-concept firms and Citigroup as a benchmark selector.
- Company names and sectors are selector labels; the two data tracks below have distinct meanings.

### Preliminary scored data
- The `SEC pilot scores` view reads annual company scores from `data/processed/sec/company_scores_v0.csv`.
- Join scores to firm selectors by ticker and verify company labels; the score unit is company × fiscal year, not quarter.
- This file is scored from SEC filing passage labels using the v0 scoring method. The underlying v0 labels are AI-assisted drafts, so present the data as **preliminary SEC disclosure scores**, not verified company-wide adoption or the final index.
- FY2026 is partial through June 30, 2026. Citi and Principal have no FY2023 score. Missing firm-years must remain unavailable, not be filled with zero.
- A score of zero means no scored use was found in the available labeled disclosures; it does not prove that the firm does not use AI.
- The score CSV does not contain evidence IDs or citations. Do not imply that this view supports passage-level audit or evidence drill-down.

### Envisioned fictional interface
- Fictional use-case records contain invented periods, titles, summaries, details, example areas, and demo stages. They are not claims about the named firms.
- Any mock totals and charts are calculated only from those fictional records.
- The example areas and stages demonstrate interface controls only; they are not an approved taxonomy, scoring rule, or classification method.
- Keep fictional records and their aggregates separate from the scored SEC data; never join, blend, or compare them as if they were measured observations.
- The evidence preview must say no real source is attached. Do not fabricate citations or imply that the intended data contract or methodology is implemented.
- Load the approved Merriweather and Inter fonts from Google Fonts with local CSS fallbacks.
  This is a typography-only network request; do not add external data connections to the dashboard.
- Preserve Streamlit's toolbar controls, make the top toolbar transparent, and use normal document
  scrolling so it moves out of view as the page scrolls.
- Use blue selected-firm chips in the comparison selector, and keep evidence-preview content
  wrapped within the expanded card at narrow and wide viewport sizes.

## Demo user journey and design rationale
1. **Review SEC pilot scores:** show the annual score table and trend separately, with preliminary-data, AI-assistance, and coverage caveats visible on the same view.
2. **Explore the envisioned firm story:** use familiar firm selectors for fictional cards and make clear that the dates, records, areas, and stages are invented.
3. **Compare envisioned firms:** compare only fictional records from the mock fixture; never frame mock differences as actual company performance or rank firms.

The goal is to demonstrate both the current preliminary scoring artifact and a possible future interface without conflating them. The fictional overview, record list, detail view, and comparison must all tell the same story from `src/dashboard/mock_data.py`. The score view reads only the annual data in `company_scores_v0.csv`.

## Prototype visual style
The dashboard uses the evolving, minimalist blue-and-purple style guide in [`src/dashboard/style.md`](../../src/dashboard/style.md). Its Streamlit implementation is centralized in [`src/dashboard/theme.py`](../../src/dashboard/theme.py), with automated checks in [`tests/test_dashboard_style.py`](../../tests/test_dashboard_style.py). Keep the guide and executable theme aligned when adjusting the design.

## Tool decision criteria (to discuss, not decided)
- Can it be **externally hosted** (course TP3 requirement)?
- Can it show **agentic capabilities** (course TP3: "an agent that plans/acts across steps")?
- Evidence drill-down support
- Team familiarity
- Cost / licensing

## Current score-view data contract
- Source: `data/processed/sec/company_scores_v0.csv`
- Key: `(ticker, fiscal_year)`; one annual row per company/year.
- Fields: `company`, `ticker`, `fiscal_year`, `ai_use_score`, `scenarios_with_use`, `readiness_score`, `talk_ratio_pct`, `substantive_ai_passages`.
- The loader validates required fields, numeric bounds, unique keys, and firm labels. Missing company-years are shown as unavailable.
- This pilot contract is not the final Part 4 index contract. It has no quarterly dimension, sector peer index, or evidence IDs. Define those only after the team finalizes the methodology.

## Wireframes
<!-- Link sketches/Figma here. -->
