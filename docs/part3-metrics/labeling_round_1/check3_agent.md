# Check 3: the agent vs. the human raters on the 50-passage sample

> **Run:** Tue Oct 27, 2026, by Shu. Agent: DeepSeek `deepseek-flash` (V4.1-Flash-1017), prompt `classify-v1.5`, temperature 0, guardrails on.
> **Files:** [`agent_labels_sample.csv`](../../../data/processed/sec/agent_labels_sample.csv) (the 50 labels), [`ai_vs_humans_agent.csv`](ai_vs_humans_agent.csv) (differences), [`check3_agent_output.txt`](check3_agent_output.txt) (raw `irr.py` output). Mehul's round-1 files are untouched.
> **Command:** `python -m src.agent.run_batch --ids docs/part3-metrics/labeling_round_1/sample_passages.csv --labels-out data/processed/sec/agent_labels_sample.csv --scores-out data/processed/sec/agent_scores_sample.csv`, then `python -m src.eval.irr --ai-labels data/processed/sec/agent_labels_sample.csv`.

## What was compared
The human majority is the level (D2 / D1 / P / N / X) that at least two of the three raters (Logan, Yen-Chu, Snehal) gave a passage. 43 of the 50 passages have one; the other 7 are three-way splits and are left out, as in `irr.py`.

The agent's prompt was tuned on Oct 23 against 110 passages (the six firms' FY2025 10-Ks plus Citi's). 21 of the 50 sample passages are in that set, so they are **in-sample**. The honest number is the one for the **29 passages outside the tuning set**.

## Results
| | All 50 | **Outside the tuning set (29)** | Inside the tuning set (21) |
|---|---|---|---|
| Passages with a human majority | 43 | **25** | 18 |
| Exact agreement with the majority | 41/43 (95%) | **24/25 (96%)** | 17/18 (94%) |
| Cohen's kappa (evidence level) | 0.93 | **0.94** | 0.91 |
| Use vs. no-use agreement | 42/43 | **24/25** | 18/18 |
| Use vs. no-use kappa | 0.95 | **0.92** | 1.00 |
| **Overclaim** (agent D2/D1/P, humans N/X; bar ≤ 5%) | **0 (0%)** | **0 (0%)** | 0 (0%) |
| Underclaim (agent N/X, humans D1/D2) | 1 (2%) | 1 (4%) | 0 |
| needs_review (guardrail held the label at N) | 2 | 1 | 1 |

Against each rater (all 50): kappa 0.80 with Logan, 0.66 with Yen-Chu, 0.31 with Snehal; use/no-use kappa 0.92 / 0.72 / 0.80. The low Snehal number is the N-vs-X reading described in [`results_round1.md`](results_round1.md), not a use/no-use disagreement.

**Compared with the AI-assisted draft labels** (results_round1.md: 95% exact, kappa 0.93, overclaim 0%, underclaim 2% on the same 43 items): the agent lands on the same numbers, and it got there without anyone having seen the draft labels or the human labels while the prompt was written.

## Caveat: the human majority is itself noisy
Round-1 agreement between the humans on the evidence level was low (Fleiss' kappa 0.27). One rater read "not about AI → X" as covering AI-risk passages, which the codebook means as N. The majority is still usable for use vs. no-use (pairwise kappa 0.60–0.72), but the exact-level numbers above should be read as provisional until the 50 items are adjudicated. The 7 passages with no majority are listed at the end; the agent agrees with Logan on 5 of them.

## Every difference from the majority
No overclaims. The two differences:

| passage_id | Set | Agent | Raters | Agent's quote / reason |
|---|---|---|---|---|
| JPM_2025-12-31_10-K_00150 | in-sample | D1 TALENT (conf 0.78) | Logan D2, Yen-Chu D2, Snehal D1 → majority **D2** | "The Firm offers voluntary training programs and educational resources to all employees covering a broad variety of topics such as leadership and management, artificial intelligence, data literacy…". Agent: no named program or metric, so D1. Level only; use/no-use agrees |
| SCHW_2026-03-31_10-Q_00047 | new | N (conf 0.72) | Logan N, Yen-Chu D1, Snehal D1 → majority **D1** | Passage is one bullet: "The Company's development and deployment of artificial intelligence capabilities;" (a forward-looking-statement list item). Agent: "a generic bullet list item naming AI capabilities as a factor, with no company statement of use". The codebook's rule 4 (forward-looking list items are N, BOILER) backs the agent; two raters read it as use. **The underclaim** |

## Where the guardrail mattered
Two labels went to `needs_review` because the model's confidence was under 0.70, and both would have been overclaims:

| passage_id | Model's call | Confidence | Raters |
|---|---|---|---|
| BAC_2025-12-31_10-K_00247 | D1 ENT ("reliance on third-party AI models further increases our risks") | 0.68 | Logan N, Yen-Chu N, Snehal X |
| COF_2024-12-31_10-K_00357 | D1 RISKM | 0.60 | Logan N, Yen-Chu N, Snehal P |

Without the guardrail the overclaim rate would be 2/43 (5%), right at the bar. This is the with-vs-without difference for check 6, seen on real data.

## Two things to know about this run
1. **Prompt version bumped to v1.5.** PR #64 (merged Oct 24) changed the codebook text the prompt is generated from (the wider X definition, the AGENT topic). The rules are those of v1.4, but the prompt text is not identical, so the Oct 23 cache did not apply and all 50 passages were fresh DeepSeek calls (about one cent). `PROMPT_VERSION` now says so.
2. **Run-to-run variance at temperature 0.** The sample was run twice with the same prompt text (once before the version bump). The first run put BAC_00247 at confidence 0.70, exactly the threshold, so it passed as D1 and counted as an overclaim (91% exact, kappa 0.85, overclaim 2%); the second run gave 0.68 and sent it to review (the numbers above). Four of the 21 in-sample labels also differed from the Oct 23 file in the first run, one in the second. The committed run is now cached, so reruns from this repo reproduce it; a rerun from a fresh cache may not. Reporting a range (overclaim 0–2%) is safer than a point.

## The 7 passages with no human majority
| passage_id | Agent | Logan | Yen-Chu | Snehal |
|---|---|---|---|---|
| BAC_2024-12-31_10-K_00279 | N | P | N | D1 |
| BAC_2025-12-31_10-K_00281 | N | P | N | D1 |
| COF_2025-06-30_10-Q_01555 | X | N | D1 | X |
| C_2025-12-31_10-K_00831 | D2 | D2 | N | D1 |
| C_2025-12-31_10-K_01476 | P | P | N | X |
| JPM_2024-12-31_10-K_00155 | D1 | D2 | N | D1 |
| PFG_2026-06-30_10-Q_01339 | D2 | P | N | D2 |

These are the adjudication cases. Three of them (BAC_00279, BAC_00281, C_01476) are the "risk factor that mentions own use" and "plan vs. talk" questions from the round-1 discussion.
