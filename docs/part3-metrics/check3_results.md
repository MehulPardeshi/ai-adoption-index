# Check 3: the agent vs. the team's agreed labels

> **Generated** 2026-11-09 by `python3 -m src.eval.check3_consensus` (rerun it after any new agent run). **Answer key:** [`consensus_labels.csv`](adjudication/consensus_labels.csv), the evidence level the raters agreed for each of the 80 passages people labeled (round 1: 50, round 2: 30).
> **Agent labels:** [`agent_labels_sample.csv`](../../data/processed/sec/agent_labels_sample.csv). deepseek-flash@DeepSeek-V4.1-Flash-1017, prompt `classify-v1.5`, run 2026-10-27. Guardrails on.
> **Tuning set:** the 110 passages in [`agent_labels_v1.csv`](../../data/processed/sec/agent_labels_v1.csv) the prompt was tuned on (Oct 23). **Unseen** = the rest, the honest test.

## Agent vs. agreed labels

| Passages | n | Exact level | κ (level) | Use vs. no use | κ (use) | **Overclaim** | Underclaim | Overclaim without guardrail | Held for review | Scenario overlap |
|---|---|---|---|---|---|---|---|---|---|---|
| Round 1, **unseen** | 29 | 25/29 (86%) | 0.79 | 26/29 (90%) | 0.78 | 0/29 (0%) | 3/29 (10%) | 1/29 (3%) | 1 | 0.72 (n=16) |
| Round 1, tuning set | 21 | 14/21 (67%) | 0.51 | 20/21 (95%) | 0.90 | 0/21 (0%) | 1/21 (5%) | 1/21 (5%) | 1 | 0.64 (n=11) |
| Round 2 | 30 | *not run yet* | | | | | | | | |

**Overclaim** = the agent says use (D1/D2) where the agreed label is N, P or X; bar ≤ 5%. **Underclaim** = the reverse. κ = Cohen's kappa (bar ≥ 0.60); on small groups read it as a direction only. *Overclaim without guardrail* scores the model's own call before `verify_label`. *Scenario overlap* = mean Jaccard of the area codes where both sides gave D2/D1/P.

## The draft labels on the same passages (what the dashboard's preliminary scores read)

| Passages | n | Exact level | κ (level) | Use vs. no use | κ (use) | Overclaim | Underclaim | Scenario overlap |
|---|---|---|---|---|---|---|---|---|
| Round 1 | 50 | 41/50 (82%) | 0.73 | 48/50 (96%) | 0.92 | 0/50 (0%) | 2/50 (4%) | 0.58 (n=30) |
| Round 2 | 30 | 16/30 (53%) | 0.34 | 21/30 (70%) | 0.29 | 0/30 (0%) | 9/30 (30%) | 0.00 (n=3) |
| All rounds | 80 | 57/80 (71%) | 0.59 | 69/80 (86%) | 0.73 | 0/80 (0%) | 11/80 (14%) | 0.53 (n=33) |
| Same passages as the agent | 50 | 41/50 (82%) | 0.73 | 48/50 (96%) | 0.92 | 0/50 (0%) | 2/50 (4%) | 0.58 (n=30) |

## Where the guardrail mattered

| passage_id | Round | Set | Model's call | Confidence | Agreed | Effect |
|---|---|---|---|---|---|---|
| BAC_2025-12-31_10-K_00247 | 1 | tuning | D1 | 0.68 | N | stopped an overclaim |
| COF_2024-12-31_10-K_00357 | 1 | unseen | D1 | 0.6 | P | stopped an overclaim |

## Every difference from the agreed label (11)

Also in [`check3_differences.csv`](check3_differences.csv), with the agent's quote.

| passage_id | Round | Set | Kind | Agent | Confidence | Guardrail | Agreed | Draft |
|---|---|---|---|---|---|---|---|---|
| BAC_2024-12-31_10-K_00279 | 1 | unseen | underclaim | N | 0.88 | pass | D1 ENT | D1 |
| COF_2025-06-30_10-Q_01555 | 1 | unseen | underclaim | X | 0.62 | pass | D1 ENT | N |
| SCHW_2026-03-31_10-Q_00047 | 1 | unseen | underclaim | N | 0.72 | pass | D1 ENT | P |
| BAC_2025-12-31_10-K_00281 | 1 | tuning | underclaim | N | 0.78 | pass | D1 ENT | D1 |
| COF_2024-12-31_10-K_00357 | 1 | unseen | level differs | N | 0.6 | needs_review | P CREDIT;FRAUD;MKT;OPS;RISKM | N |
| COF_2025-12-31_10-K_00480 | 1 | tuning | level differs | N | 0.84 | pass | P OPS;PROD;TALENT | N |
| C_2025-12-31_10-K_00131 | 1 | tuning | level differs | D2 OPS | 0.9 | pass | D1 ENT;GOV;OPS | D2 |
| C_2025-12-31_10-K_00831 | 1 | tuning | level differs | D2 GOV | 0.88 | pass | D1 GOV | D2 |
| C_2025-12-31_10-K_01476 | 1 | tuning | level differs | P ENT | 0.7 | pass | N | P |
| JPM_2025-12-31_10-K_00150 | 1 | tuning | level differs | D1 TALENT | 0.78 | pass | D2 TALENT | D1 |
| WFC_2025-12-31_10-K_01394 | 1 | tuning | level differs | N | 0.85 | pass | P ENT;PROD;TALENT | N |

## Notes
- Round 2's 30 passages were picked on purpose to be hard (the rule questions from round 1), so its numbers are expected to be lower than round 1's ([round 2 results](labeling_round_2/results_round2.md)).
- The first check 3 compared the agent with the **human majority** (96% on 25 unseen passages, [report](labeling_round_1/check3_agent.md)). The agreed labels are stricter: they cover all passages, including the 3-way splits the majority left out.
- Temperature 0 is not fully deterministic: a fresh run can move a label near the 0.70 threshold (round 1 overclaim was 0–2% across two runs). Cached answers make a rerun from the same machine identical.
