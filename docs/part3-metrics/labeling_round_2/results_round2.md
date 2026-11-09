# Labeling round 2: results (check 2)

> **Run:** Wed Nov 4, 2026, by Mehul, with `python3 -m src.eval.irr --round 2`. **Raters:** Logan, Yen-Chu, Snehal (30 new passages each, labeled blind). All three files passed the format checks.
> Logan's file was converted from his Numbers workbook into [`rater_logan.csv`](rater_logan.csv) with the same checks as `workbook_to_csv.py`. Files: [`disagreements.csv`](disagreements.csv), [`ai_vs_humans.csv`](ai_vs_humans.csv).
> **Status:** results for the team to go through. Labels weren't changed after submission, and nothing here changes the rules.

## Headline
- **Evidence level (D2/D1/P/N/X): still below the bar.** Fleiss' kappa 0.32 across all three raters (target ≥ 0.60; round 1 was 0.27). One pair clears it: Logan vs. Yen-Chu, 0.67.
- **Use vs. no use: below the bar on two of three pairs** (0.45, 0.46, 0.71). Round 1 met it on all three (0.60–0.72).
- **The rule we fixed did get fixed.** In round 1, merging N and X raised Fleiss from 0.27 to 0.49. In round 2 merging them changes nothing (0.32 and 0.32), and no rater overuses X any more. The disagreement has moved to other rules.
- **Not like for like:** round 2 was built from the hard cases on purpose ([README](README.md)), so it can't show whether agreement rose or fell in general. It shows the clarified sheet alone doesn't get all three raters to the bar on hard passages.

| Pair | Evidence kappa (as labeled) | Evidence kappa (N and X merged) | Use/no-use kappa | Raw agreement (as labeled) |
|---|---|---|---|---|
| Logan vs. Snehal | 0.15 | 0.20 | 0.45 | 33% |
| Logan vs. Yen-Chu | **0.67** | 0.58 | 0.71 | 80% |
| Snehal vs. Yen-Chu | 0.27 | 0.35 | 0.46 | 43% |
| **Fleiss (all 3)** | **0.32** | **0.32** | 0.53 | All three agree on 9 of 30 |

29 of 30 passages have a majority. One has none (`JPM_2025-12-31_10-K_00501`: N, P, D1).

## Where people disagreed
21 of 30 passages have at least one disagreement ([`disagreements.csv`](disagreements.csv)).

1. **Planned vs. just talk (P vs. N):** the biggest gap. One rater marked 7 passages P; the other two marked none. Most are conditional risk sentences (e.g., "could require us to…"). The sheet says hedged risk language is N, so the question is whether that line is clear enough.
2. **Use vs. talk (N vs. D1):** the real boundary question. Even the closest pair split on 4 passages, mostly Capital One sentences that sit under a risk heading about "our use of AI".
3. **Acronym lists (X vs. D2):** three Capital One acronym lists were marked D2 FRAUD by one rater and X by the other two. The sheet's own example of X is an acronym list, so these are worth checking first; they may be a simple misreading.
4. **Specific vs. general (D1 vs. D2):** 2 passages for the closest pair, 3 for another.
5. **Scenarios:** overlap is 0.75 for the closest pair and 0.07–0.11 with the third rater, who often listed 4–6 areas where the others used ENT (general claims). The ENT rule may need a clearer example.

## What this means for the AI side
- **Draft labels vs. the human majority** (29 passages): 72% exact, κ 0.51, **overclaim 0%**, **underclaim 24%**. The draft labels say N on 7 passages where most raters said D1 or D2. They feed the dashboard's preliminary scores, so those scores may read low on this kind of sentence.
- **The agent:** only 11 of the 30 passages have agent labels, all in its tuning set. On the 10 with a majority it matches on 7, with no overclaims; the 3 misses are underclaims (one of them held at N by the guardrail for low confidence). Too few and in-sample, so this isn't a result. Check 3 on the other 19 needs a model run (Shu's key).

## Next steps (not decided here)
1. **Adjudication:** the team goes through the 21 passages here and the round 1 disagreements. The agreed labels become the consensus set for checks 3 and 4. Check 4's rerun (#101) waits for this.
2. **Rules to look at together:** P vs. N on hedged risk sentences; D1 for sentences under an "our use of AI" heading; when to use ENT. Any rule change is a team decision, and the categories stay frozen unless the team reopens them.
3. **Agent on the 30 passages** (about a cent): `python -m src.agent.run_batch --ids docs/part3-metrics/labeling_round_2/sample_passages.csv --labels-out data/processed/sec/agent_labels_round2.csv --scores-out data/processed/sec/agent_scores_round2.csv`, then report the 19 outside the tuning set separately. *(Nov 9: add `--run-info-out data/processed/sec/agent_run_info_round2.json`, then `python3 -m src.eval.check3_consensus` scores both rounds against the agreed labels: [check 3 results](../check3_results.md).)*
