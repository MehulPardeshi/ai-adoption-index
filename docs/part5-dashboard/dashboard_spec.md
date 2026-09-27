# Dashboard Spec (Part 5)

> **Status:** requirements captured from the brief. **The tool is not chosen yet** (Tableau / Power BI / Streamlit / Dash / Plotly). Log the choice in [`memory/09-decisions-log.md`](../../memory/09-decisions-log.md).
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

## Tool decision criteria (to discuss, not decided)
- Can it be **externally hosted** (course TP3 requirement)?
- Can it show **agentic capabilities** (course TP3: "an agent that plans/acts across steps")?
- Evidence drill-down support
- Team familiarity
- Cost / licensing

## Data contract (TBD)
<!-- Columns the dashboard expects from data/processed/, e.g., firm, cik, sector_tags, quarter, metric_*, index_value, evidence_id. Define once Part 4 is settled. -->

## Wireframes
<!-- Link sketches/Figma here. -->
