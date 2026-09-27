# Quarterly Refresh Protocol: TEMPLATE

> Brief, Part 4: document **exactly what gets re-run each quarter** (new filings, new transcripts, re-scored specificity/sentiment) so the index is genuinely maintainable, not a one-off.
> **Status:** TEMPLATE. Fill this in once the pipeline exists. It should be usable by someone who wasn't on the team (e.g., the client's research assistant).

## Trigger and timing
<!-- When does a refresh run? e.g., N weeks after quarter-end, once 10-Qs are filed. -->

## Pre-flight checklist
- [ ] Firm universe still valid (mergers, delistings, new firms)?
- [ ] Credentials / User-Agent configured (`.env`)?
- [ ] Taxonomy and rubric versions unchanged? (If changed, see "Re-scoring history" below.)

## Steps
1. **Collect new documents:** <!-- which forms/sources, which command/notebook -->
2. **Extract AI-relevant text:** <!-- -->
3. **Classify into taxonomy:** <!-- -->
4. **Score metrics:** <!-- -->
5. **Human spot-check / IRR sample:** <!-- how many items, who -->
6. **Normalize and compute the index:** <!-- -->
7. **Update the dashboard data:** <!-- -->
8. **Log the refresh:** <!-- date, quarter added, anomalies → where? -->

## Re-scoring history
<!-- If the taxonomy/metrics change, do we re-score all back quarters? Document the rule. -->

## Estimated effort
<!-- Person-hours and cost (e.g., LLM API) per refresh. -->

## Refresh log
| Date | Quarter added | Run by | Notes |
|---|---|---|---|
