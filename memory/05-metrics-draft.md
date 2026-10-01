# 05 — Metrics (Part 3): DRAFT STARTER BATTERY ONLY

> **2026-10-01 kickoff clarification:** See [minutes](../meetings/2026-10-01-client.md) and the latest decisions log. Julie recommended a 4–5-bank pilot and permits a simpler team-designed measure. Final coverage, taxonomy, and metrics remain open; quarterly automation is desired only if feasible. Earlier targets below remain brief material, not confirmed client commitments. Course/rubric obligations must be checked with the instructor before reducing graded requirements.


> ⚠️ **DRAFT — NOT FINAL — DO NOT SUBMIT AS-IS.**
> This is the brief's suggested starting battery. Part 3 is graded on the team **proposing, testing, and justifying** its own metrics. AI agents: **do not implement scoring logic or pick final definitions/thresholds** until the team logs them in [`09-decisions-log.md`](09-decisions-log.md).
> Working docs: [`docs/part3-metrics/metrics.md`](../docs/part3-metrics/metrics.md), [`docs/part3-metrics/inter_rater_reliability.md`](../docs/part3-metrics/inter_rater_reliability.md)

## Starter battery from the brief (DRAFT)
| Metric | What it captures | Design challenge (from the brief) |
|---|---|---|
| AI mention density | AI words/sentences as a % of document length | Normalize by length **and** document type (a 10-K ≠ a press release) |
| Category breadth | # distinct use-case categories mentioned per quarter | Risk of overcounting vague mentions |
| Specificity score | **1–5 rubric:** a named tool/model/outcome vs. "we use AI" | Hand-coded rubric + **inter-rater reliability check (REQUIRED)** |
| Sentiment/tone | Opportunity-framed vs. risk-framed vs. neutral | **Loughran-McDonald** financial dictionary preferred over generic sentiment tools |
| Forward vs. retrospective framing | Future plan vs. deployed capability | Needs tense/modal-verb tagging |
| Repetition/consistency | Does a use case recur quarter over quarter (real) or vanish (hype)? | Needs entity/topic tracking over time |
| Investment signal | Capex, headcount, or partnerships tied to AI | Cross-reference 8-Ks and press releases |

## Hard requirement
**Inter-rater reliability on the specificity score is required, not optional.** Use e.g. Cohen's kappa between team members (see the glossary in [`10-glossary.md`](10-glossary.md)). This is the "creative metrics still need validity checks" lesson.

## Open questions for the team (not answers)
- What exactly distinguishes a 2 from a 3 on specificity? (The rubric anchors must come from real examples.)
- Which document types feed which metrics?
- Does an LLM-based scorer need its own agreement check against human coders?

**Deliverable:** metrics methodology write-up = **20%** of the client rubric.
