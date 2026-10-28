# Labeling round 1: results (check 2, plus a check 3 preview)

> **Run:** Tue Oct 27, 2026, by Mehul, with `python3 -m src.eval.irr`. **Raters:** Logan, Yen-Chu, Snehal (50 passages each, labeled blind). All three files passed the format checks.
> Logan's file was converted from his Numbers workbook into [`rater_logan.csv`](rater_logan.csv) with the same checks as `workbook_to_csv.py`. Files: [`disagreements.csv`](disagreements.csv), [`ai_vs_humans.csv`](ai_vs_humans.csv).
> **Status:** results for team discussion on Wed Oct 28. Nothing here changes the rules yet; any rule change is a team decision.

## Headline
- **Use vs. no use: met the bar.** Kappa 0.72 / 0.72 / 0.60 across the three pairs (target ≥ 0.60).
- **Evidence level (D2/D1/P/N/X): below the bar.** Fleiss' kappa 0.27 across all three raters. The cleanest pair (Logan vs. Yen-Chu) reached **0.61**.
- **Most of the gap comes from one rule read two ways.** One rater marked AI risk passages (e.g., "AI system failures… biased output") as "not about AI" (→ X). The codebook means "about AI, but no use" (→ N). That rater used X 18 times and N 0 times; the other two used N 20 and 25 times.

| Pair | Evidence kappa (as labeled) | Evidence kappa (N and X merged) | Use/no-use kappa | Raw agreement (as labeled) |
|---|---|---|---|---|
| Logan vs. Snehal | 0.21 | 0.48 | 0.72 | 34% |
| Logan vs. Yen-Chu | **0.61** | 0.61 | 0.72 | 74% |
| Snehal vs. Yen-Chu | 0.16 | 0.39 | 0.60 | 30% |
| **Fleiss (all 3)** | **0.27** | **0.49** | | |

The as-labeled numbers are the official round-1 result. The merged column is a sensitivity check, not a replacement. Labels were not changed after submission.

## Where people disagreed (other than N vs. X)
1. **Planned vs. just talk (P vs. N):** 4 of Logan and Yen-Chu's 13 disagreements. When does "we are exploring / investing in AI" count as a plan?
2. **Specific vs. general use (D2 vs. D1):** the most common Logan–Snehal disagreement (7 items). What counts as "naming something specific": a named tool, a number, or a described use case?
3. **Use vs. talk (D1/D2 vs. N):** 7 Logan–Yen-Chu items. To review in adjudication.

## Check 3 preview (not the final check 3)
- **AI-assisted draft labels vs. the human majority** (43 of 50 items have a majority): 95% accuracy, kappa 0.93, **overclaim 0%**, underclaim 2%.
  - Caveat: Yen-Chu drafted those labels with AI and had seen them before rating (known limitation in the evaluation plan). Her agreement with them is 0.60, against Logan's 0.80, so this doesn't look like anchoring.
- **Shu's agent (`agent_labels_v1.csv`)** has labels for 21 of the 50 passages, all from its tuning set, so this is **in-sample only**. On the 18 with a human majority it agreed on use/no-use 18/18, with 17/18 exact (one D1 vs. D2) and no overclaims.
- **Update, Oct 27 evening: the real check 3 is done** (Shu, #85, [`check3_agent.md`](check3_agent.md)). The agent ran on all 50 with prompt classify-v1.5. On the **29 passages outside the tuning set** (not 35: 6 sample passages are also among the 20 Citi passages used for tuning): 96% exact, κ 0.94, **overclaim 0%** (0–2% across runs), underclaim 4%. Without the guardrail it would have been 5% (two low-confidence calls were held back), which is useful evidence for check 6.

## Proposed next steps (for the team to decide on Oct 28 / Nov 1)
1. **Clarify the cheat sheet:** "about AI = N only if the passage isn't about AI at all; AI risks, threats and regulation are about AI → N". Add one-line tests for P vs. N and D2 vs. D1.
2. **Adjudicate** the 50 items in a short session. The agreed labels become the consensus set for checks 3 and 4.
3. **Round 2,** as in the evaluation plan: 30 new passages with the clarified rules, to show whether agreement improves. Same raters if possible.
