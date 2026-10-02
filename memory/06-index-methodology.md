# 06 — Index Construction (Part 4)

> **2026-10-01 kickoff clarification:** See [minutes](../meetings/2026-10-01-client.md) and the latest decisions log. the proof of concept covers **5–6 big U.S. financial companies** (e.g., JPMorgan; decided 2026-10-01, superseding the 4–5-bank figure in the transcript excerpts) and permits a simpler team-designed measure. Final coverage, taxonomy, and metrics remain open; quarterly automation is desired only if feasible. Earlier targets below remain brief material, not confirmed client commitments. Course/rubric obligations must be checked with the instructor before reducing graded requirements.


> **Read [`09-decisions-log.md`](09-decisions-log.md) first.** Working docs: [`docs/part4-index/methodology.md`](../docs/part4-index/methodology.md), [`docs/part4-index/refresh_protocol.md`](../docs/part4-index/refresh_protocol.md)

## Requirements from the brief
1. **Unit of analysis:** **firm-sector-quarter**, using the sector universe from Part 1.5.
2. **Normalize** each metric within the peer universe using **z-scores or min-max scaling**, so metrics on different scales can be combined.
3. **Weighting:** **start equal-weighted.** Any deviation (e.g., weighting specificity above raw mention count) must be **tested and justified**.
4. **Backfill 8–12 historical quarters per firm** for a baseline trend. Source primarily from EDGAR full-text search plus archived transcripts and press releases. Minimum graded: **8 quarters × chosen firms** (20% of the rubric). The retirement sector may warrant deeper backfill.
5. **Refresh protocol:** document exactly what gets re-run each quarter (new filings, new transcripts, re-scored specificity/sentiment) so the index is genuinely maintainable.
6. **Methodology appendix:** the most important academic artifact. **A reader must be able to reproduce the index from it.**

## Worth including (from the brief)
- A paragraph on the **functional vs. SIC/legal classification mismatch** (see 03).
- A comparison to existing indices (e.g., the Fed's textual sentiment indices, sell-side "AI mentions in earnings calls" trackers): where are we novel vs. replicative?
- **Optional bonus track:** validate against an external proxy (AI job postings, AI patents).

## Open decisions (log in 09 when made)
- z-score vs. min-max, and whether to normalize within sector or across the full universe
- How to treat firms with a missing quarter
- Calendar vs. fiscal quarters
