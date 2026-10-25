# Dashboard Spec (Part 5)

> **Status:** requirements captured from the brief. **Streamlit was selected on 2026-10-04.** The current branch contains a synthetic-data interface prototype only; the final data contract and methodology remain open. See [`memory/09-decisions-log.md`](../../memory/09-decisions-log.md).
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

## Prototype data guardrails
- The interface fixture includes the six proof-of-concept firms and Citigroup as a benchmark selector.
- Company names and sectors are selector labels only. The use-case records attached to those names are entirely fictional and are not claims about those firms.
- Fictional use-case records contain invented periods, titles, summaries, details, example areas, and demo stages. Any totals and charts are calculated only from those fictional records.
- The example areas and stages demonstrate interface controls only; they are not an approved taxonomy, scoring rule, or classification method.
- The prototype is strictly mock-only: it does not read project data files, rules, research notes, or source evidence; call an agent, model, or API; or write research outputs.
- The evidence preview must say no real source is attached. Do not fabricate citations or imply that the intended data contract or methodology is implemented.
- Keep styling self-contained; do not add external assets or data connections to the mock dashboard.

## Prototype user journey and design rationale
1. **Choose a firm:** use the familiar proof-of-concept firm names as selectors, with a prominent warning that examples attached to names are invented.
2. **Get an overview:** summarize the selected firm's fictional records, distinct example areas, and demo-only stages. Every total must be derived from those records.
3. **Browse records:** show each invented use case by period, title, example area, and demo stage.
4. **Open a record:** show its fictional summary and detail, followed by an explicit no-real-source notice where reviewed evidence could appear in a future data-backed product.
5. **Compare firms:** select multiple firms and compare record counts, example areas, and demo stages using the same fictional records shown in the firm view. Never frame mock differences as actual company performance or rank firms.

The goal is to demonstrate a coherent user journey, not to imply research findings. The overview, record list, detail view, and firm comparison must all tell the same story from `src/dashboard/mock_data.py`.

## Prototype visual style
The dashboard uses the evolving, minimalist blue-and-purple style guide in [`src/dashboard/style.md`](../../src/dashboard/style.md). Its Streamlit implementation is centralized in [`src/dashboard/theme.py`](../../src/dashboard/theme.py), with automated checks in [`tests/test_dashboard_style.py`](../../tests/test_dashboard_style.py). Keep the guide and executable theme aligned when adjusting the design.

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
