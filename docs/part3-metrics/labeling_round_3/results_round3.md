# Labeling round 3 results: the new firm types (#169)

Logan and Snehal each labeled the 40 pilot passages alone (10 per new firm type, firms outside our 7 proof-of-concept firms), then agreed one label per passage (Nov 24). The agent's labels were hidden from both. Built by `python3 -m src.eval.round3_results`.

## People vs. people

- Same evidence level on 23 of 40 (κ 0.42); same use vs. no-use call on 32 of 40 (κ 0.60, bar 0.6).
- As in rounds 1 and 2, people agree on the use call and less on the detail level.

## Agent vs. the agreed labels

| Firm type | n | Exact level | κ (level) | Use vs. no use | **Overclaim** | Underclaim | Held for review |
|---|---|---|---|---|---|---|---|
| Insurers | 10 | 80% | 0.66 | 90% | **0 (0%)** | 1 | 0 |
| Asset managers and brokers | 10 | 60% | 0.47 | 70% | **1 (10%)** | 2 | 2 |
| Payments and consumer finance | 10 | 50% | 0.33 | 80% | **1 (10%)** | 1 | 2 |
| Exchanges and data | 10 | 60% | 0.42 | 80% | **0 (0%)** | 2 | 1 |
| **All 40** | 40 | 62% | 0.47 | 80% | **2 (5%)** | 6 | 5 |

Overclaim = the agent says use (D1/D2) where the agreed label is N, P or X; bar ≤ 5%. The guardrail changed no overclaim here (without it: 2). Held = sent to a person by the guardrail; a held label counts as no use until someone reviews it.

## The overclaims

- `FIS_2024-12-31_10-K_00181` (Payments and consumer finance): agent D1, agreed N (Logan X, Snehal N).
- `NTRS_2024-12-31_10-K_00359` (Asset managers and brokers): agent D1, agreed X (Logan D1, Snehal X).

Both are AI risk-factor sentences that mention "our use of AI" without saying what the AI does: the same borderline the team clarified in round 2, not something new about the firm type. Neither is a specific-use (D2) claim.

## How to read it

- Across the 40 passages the agent meets the bar: 2 overclaims (5%).
- Per type, 10 passages is too few to tell types apart: one passage is 10%. Two types have one overclaim each, two have none.
- The agent errs cautious here too: 6 underclaims vs. 2 overclaims, and the agreed label was higher than the agent's on most level differences. Index scores for these types lean low.
- 5 labels were held by the guardrail; the agreed labels give the people's answer for them (see `round3_differences.csv`).
