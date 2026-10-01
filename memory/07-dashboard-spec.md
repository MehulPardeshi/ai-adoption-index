# 07 — Dashboard (Part 5)

> **2026-10-01 kickoff clarification:** See [minutes](../meetings/2026-10-01-client.md) and the latest decisions log. Julie recommended a 4–5-bank pilot and permits a simpler team-designed measure. Final coverage, taxonomy, and metrics remain open; quarterly automation is desired only if feasible. Earlier targets below remain brief material, not confirmed client commitments. Course/rubric obligations must be checked with the instructor before reducing graded requirements.


> **Read [`09-decisions-log.md`](09-decisions-log.md) first.** Working spec: [`docs/part5-dashboard/dashboard_spec.md`](../docs/part5-dashboard/dashboard_spec.md)

## Tool: NOT YET CHOSEN
Options from the brief: **Tableau, Power BI, or Python (Streamlit / Dash / Plotly)**.
Constraint from the course: TP3 requires an **externally hosted app/website with agentic capabilities**, plus **runnable demo code**. Weigh that when choosing. Log the choice in 09.

## Required views (from the brief)
1. **Index trend line** per firm, plus the **peer-group average**, over time
2. **Category breakdown** (stacked bar or treemap) per firm per quarter
3. **Sentiment trend** over time
4. **Firm-comparison view:** radar/spider chart across categories
5. **Drill-down to cited evidence** (paraphrased and cited) for any data point, for auditability

## Required filters
- **Sector** and **firm**, so the book chapter can pull a clean **retirement-only view** without excluding that data from the cross-sector index.

## Audience
Non-technical (analysts, regulators, journalists, and the client). The team goal is a dashboard that **works end to end**, not just a mockup.
