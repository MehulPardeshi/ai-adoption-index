# Evaluation (TP3 README section, DRAFT)

> **Owner:** Mehul (Evaluation lead). **Status:** draft v0.3, Nov 22 (held-label review result), ready to paste into the final README (#166). Covers course requirement 5. One number comes later: labeling round 3 (#169), marked **[pending]**.

We judge the system on one question: **can a reader trust a score?** That breaks into six checks, each with a bar set before we ran it ([evaluation plan](../part3-metrics/evaluation_plan.md)). The bar that matters most is **overclaims ≤ 5%**: we would rather miss a real use than claim one the filing doesn't support.

| # | Check | How | Result | Bar |
|---|---|---|---|---|
| 1 | The search finds the AI passages | Read a sample of flagged paragraphs (precision) and swept 132,998 unflagged ones for misses (recall) | Precision **98.9%**; no clear miss | high precision, no systematic miss ✅ |
| 2 | People agree on the rules | Three of us labeled 80 passages on our own (50 mixed, then 30 hard ones) | Use vs. no use κ **0.60–0.72** ✅ · five detail levels κ 0.27 / 0.32 ✗ → we met and agreed a label for all 58 disagreements (Nov 7) | κ ≥ 0.6 |
| 3 | The agent matches people | Agent vs. the agreed labels on 48 passages it never saw during tuning | **81%** exact (κ 0.73), 85% use vs. no use, **0 overclaims**; all 7 misses cautious | overclaims ≤ 5% ✅ |
| 4 | Scores are robust | Changed the weights and rules, compared rankings; compared with Dong et al.'s word count | Ranking barely moves (Spearman ρ 0.95–1.00); Dong's count tracks *talk* (ρ 0.78) more than *use* (0.58) | stable under small weight changes ✅ |
| 5 | Anyone can reproduce it | A teammate who didn't build it reran everything from a fresh clone | Same 277 passages, **identical scores** | identical ✅ |
| 6 | The guardrail holds | 22 trick cases: fake quotes, tampered numbers, hidden instructions, "should I buy?" | Unsafe outputs: **0 of 18** with the guardrail, 2 without; correct answers blocked: 0 of 4 | 0 unsafe ✅ |

Details: [check 1](../part3-metrics/check1/results.md) · [round 1](../part3-metrics/labeling_round_1/results_round1.md) and [round 2](../part3-metrics/labeling_round_2/results_round2.md) · [check 3](../part3-metrics/check3_results.md) · [check 4](../part3-metrics/check4_results.md) · [check 5](../part3-metrics/check5_rerun.md) · [check 6](../part3-metrics/check6_results.md).

## What the checks changed
- **Check 2 failed on detail, so we changed the process, not the bar.** We found the rule people read two ways (AI risk talk marked "not about AI"), clarified it, ran a harder second round, then settled every disagreement together. Those 80 agreed labels became our answer key.
- **The answer key showed the early AI drafts leaned low.** On the 80 hardest passages, people found use or plans the drafts missed in 18; the reverse happened once. Swapping in the human labels raised Capital One from 3 to 20 and Principal from 0 to 18. Scores built only from AI labels can be too low, rarely too high, and the dashboard says so.
- **The strict score (specific use only) moves the ranking more** (ρ 0.69), so Julie chose the broad AI Use Score as the headline with the strict one beside it (Nov 10).

## People stay in the loop at scale
On the 76-firm S&P 500 Financials run (10-Ks and 10-Qs, FY2024–25) the guardrail held **200 of 2,353** labels (8.5%) for a person: under 0.70 confidence, or a quote not found word for word. They count as no use until reviewed; reviewers' decisions are applied with their names, and the agent's own labels are never edited (#170). **Review result (Shu and Yen-Chu, Nov 22; #182, #183):** 195 of the 200 reviewed (the other 5 are in the round 3 blind sample and wait for it). People kept the agent's evidence level on 140 (72%), raised 25 and lowered 30; 173 count as use after review, 22 don't (N or X). Since held labels count as no use until reviewed, the draft FY2025 index **rose from 7.2 to 8.6 equal-weighted and 9.4 to 10.2 cap-weighted**: the guardrail made the index cautious, as designed, and the review gave the use back where people confirmed it. Reviewers flagged 42 rows where the use is in a product sold to clients (#169). Final index: #134.

Before trusting firm types the agent wasn't checked on (insurers, asset managers and brokers, payments, exchanges), two of us label 10 passages per type, blind to the agent, with the same overclaim bar (#169). **[pending: round 3 result per firm type.]**

## Limits of the evaluation
- The human answer key is small (80 passages, 7 firms); κ on detail levels stayed below our bar until we agreed labels together.
- Check 3 measures agreement with *our* reading of the codebook, which was written for banks.
- Filings undercount use: tools known from the press (Bank of America's Erica, JPMorgan's LLM Suite) appear in no filing, so no check here can catch that.
