# Metrics Methodology (Part 3)

> # ⚠️ DRAFT — NOT FINAL — DO NOT SUBMIT
> The table below is the **brief's suggested starter battery**. The team must **propose, test, and justify** its own metrics (graded: **20%**). Keep, change, or drop any of these, but justify it.
> AI agents: do **not** write final definitions, thresholds, or scoring code until the team logs its decisions in [`memory/09-decisions-log.md`](../../memory/09-decisions-log.md).

Background: [`memory/05-metrics-draft.md`](../../memory/05-metrics-draft.md) · IRR: [`inter_rater_reliability.md`](inter_rater_reliability.md)

---

## Starter battery (DRAFT)
| Metric | What it captures | Design challenge |
|---|---|---|
| AI mention density | Words/sentences on AI, as % of document length | Normalize by length **and** doc type |
| Category breadth | # distinct use-case categories per quarter | Overcounting vague mentions |
| Specificity score | 1–5: named tool/model/outcome vs. "we use AI" | Hand-coded rubric + **required** inter-rater check |
| Sentiment/tone | Opportunity vs. risk vs. neutral framing | Loughran-McDonald > generic sentiment |
| Forward vs. retrospective | Future plan vs. deployed capability | Tense/modal-verb tagging |
| Repetition/consistency | Use case recurs (real) vs. disappears (hype) | Topic tracking across quarters |
| Investment signal | AI-tied capex, headcount, partnerships | Cross-reference 8-Ks and press releases |

---

## Final metric definitions (TEMPLATE, one block per metric the team keeps)

### Metric: `<name>`
- **What it measures (plain language):**
- **Why it matters for AI adoption:**
- **Unit / input:** (sentence, document, firm-quarter; which doc types)
- **Calculation:** (formula or rubric, precise enough to reproduce)
- **Scale / range:**
- **Known limitations and failure modes:** (e.g., "mentions ≠ use")
- **Validation performed:** (IRR, spot checks, sanity plots)
- **Decision log reference:** (link to the 09 entry)

## Metrics considered and dropped
<!-- Record what you tried and why you dropped it. Graders value the reasoning. -->
| Metric | Why dropped | Date |
|---|---|---|
