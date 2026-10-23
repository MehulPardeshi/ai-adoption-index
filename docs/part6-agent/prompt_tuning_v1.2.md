# Prompt tuning: classify-v1.0 → v1.2 (#35)

> **Owner:** Shu Pu · **Date:** Oct 23, 2026 · **Builds on:** [first_run_results.md](first_run_results.md) (#66) · **Code:** [`src/agent/prompts.py`](../../src/agent/prompts.py)
> Same 90 FY2025 10-K passages, same model (`deepseek-flash` = DeepSeek-V4.1-Flash-1017), guardrails on. Reference labels are still the **AI-assisted** draft labels (`passage_labels_v0.csv`), not ground truth.

## What changed in the prompt
The first run showed two patterns: sentences about **models** read as **AI use**, and Capital One **risk-factor headings** read as own use. All changes put existing codebook rules ([`sec_test_run_taxonomy_v0_DRAFT.md`](../part2-taxonomy/sec_test_run_taxonomy_v0_DRAFT.md), "Rules for unclear cases") into the prompt. None adds a new code or changes what a code means.

| Rule | Change | Codebook basis |
|---|---|---|
| 5 | A risk-factor heading ("We face risks from ... our evolving use of AI") is X; bullet items that describe a risk are N; a cross-reference that only repeats a heading earns nothing | "Risk-factor headings are X, even when they say 'our evolving use of AI'" (was missing from the prompt) |
| 9 | ENT only when the listed uses span several scenarios; if they all fall under one (valuation, stress tests, credit losses → RISKM), use that scenario | RISKM's own example is JPMorgan's "ML/AI models for valuation, stress tests and credit losses" |
| 11 (new) | Models are not AI: model, analytics or algorithm uses count only if the passage says those models use AI | Codebook definition of D1 ("the company says it uses AI") |
| 12 (new) | The D2/D1/P quote must itself name AI; a D2 named body must sit in that AI sentence | Same; makes the rule checkable |
| Security | `company_mismatch` only when a "Requested company:" line differs; the made-up few-shot company is never the requested one | Fixes a v1.1 regression (below) |
| Few-shot | Two more **made-up** examples (models listed + AI review → D1 GOV; a risk-factor heading → X). Still no real passages | Keeps labeling-sample answers out of the prompt |

### The v1.1 attempt (not kept)
v1.1 had rules 11, 12 and a broader rule 5 ("headings and summary bullets are X"). It cut overclaims to 1, but:
- turned 5 risk-factor **bullet items** into X;
- coded JPM_02064 as D1 ENT instead of RISKM;
- made the model flag **7 passages `company_mismatch`** ("not the requested Northwind Bank"). With six few-shot examples from the same made-up bank, the model took it for the requested company. All 7 were N/X anyway, but the flag blocks any use label, so it could hide real use.

v1.2 fixes all three. `PROMPT_VERSION` was bumped for each attempt, so neither reused cached answers.

## Results (90 passages, after the guardrail)
| Measure | v1.0 (#66) | v1.1 | **v1.2** |
|---|---|---|---|
| Evidence agreement with v0 | 80/90 (88.9%) | 83/90 (92.2%) | **85/90 (94.4%)** |
| Cohen's kappa | 0.67 | 0.78 | **0.82** |
| Use vs. no-use kappa | 0.70 | 0.90 | 0.79 |
| **Overclaim** (target ≤ 5%) | 6 (6.7%) | 1 (1.1%) | **2 (2.2%)** |
| Underclaim | 1 (1.1%) | 1 (1.1%) | 2 (2.2%) |
| Overclaim before the guardrail (`evidence_raw`) | 9 (10.0%) | 5 (5.6%) | 2 (2.2%) |
| Scenario overlap (mean Jaccard) | 0.78 | 0.75 | **0.89** (8 of 9 exact) |
| needs_review | 3 | 4 | 1 |
| Spurious `company_mismatch` flags | 0 | 7 | 0 |
| Use labels whose quote doesn't name AI | 3 | 0 | 0 |

Confusion matrix, v1.2 after the guardrail (rows = agent, columns = v0):

| | D2 | D1 | P | N | X | total |
|---|---|---|---|---|---|---|
| **D2** | 2 | 0 | 0 | 0 | 0 | 2 |
| **D1** | 0 | 7 | 0 | 2 | 0 | 9 |
| **P** | 0 | 0 | 0 | 0 | 0 | 0 |
| **N** | 0 | 2 | 0 | 72 | 1 | 75 |
| **X** | 0 | 0 | 0 | 0 | 4 | 4 |
| total | 2 | 9 | 0 | 74 | 5 | 90 |

### Company scores (FY2025, AI Use; ENT not counted)
| Ticker | v0 | v1.0 | **v1.2** | Why v1.2 differs from v1.0 |
|---|---|---|---|---|
| JPM | 3 (RISKM) | 9 | **3 (RISKM)** | JPM_02064 is D1 RISKM: the model-risk body (MRGR) isn't tied to AI, so no D2 |
| BAC | 3 (OPS) | 3 | **0** | BAC_00279 (market-risk models) is now N; v0's OPS comes from BAC_00281, an underclaim in all three versions |
| COF | 0 | 3 | **0** | COF_00373 is now ENT;GOV, not RISKM |
| SCHW | 0 | 27 | **0** | SCHW_00551 is D1 GOV: the listed model uses aren't said to use AI |
| WFC | 9 | 0 | 0 | Unchanged: the #64 ENT rule (3 if ENT earns 1 point) |
| PFG | 0 | 0 | 0 | — |

## Remaining disagreements with v0 (v1.2)
| passage_id | Agent | v0 | Comment |
|---|---|---|---|
| COF_2025-12-31_10-K_00372 | D1 ENT (conf 0.70) | N | "the models or AI solutions that we or a third party create and use". **For Yen-Chu:** the codebook says a risk factor is still D1 if it says the company uses AI; v0 may be the inconsistent one here |
| COF_2025-12-31_10-K_00373 | D1 ENT;GOV (conf 0.75) | N | "our business decisions that are based on information gathered through models and AI". Same question |
| BAC_2025-12-31_10-K_00281 | N | D1 OPS | "take steps to leverage emerging technologies, such as automation, AI and robotics". Generic list or own use? |
| COF_2025-12-31_10-K_00197 | N (raw P ENT, needs_review at 0.62) | D1 ENT | "A key part of our strategic focus is the development and use of ... AI technologies". The guardrail sent it to a human |
| COF_2025-12-31_10-K_00256 | N | X | A summary bullet that repeats a heading; X vs. N doesn't change any score |
| WFC_2025-12-31_10-K_01363 | D1 ENT | D1 RISKM;OPS;CX | Scenario only: the #64 ENT rule, pending the Sun Oct 25 vote |

The two COF ENT labels score 0 today. If ENT earns 1 point after the vote, COF goes to 3.

## Caveats
- **In-sample tuning.** The rules were written after looking at disagreements on these same 90 passages, so v1.2's numbers here are optimistic. The real test is check 3: human raters on the 50-passage sample (after Oct 27).
- **Overlap with the labeling sample:** 15 of the 90 passages are in `sample_passages.csv`. One of the passages I tuned on, **SCHW_2025-12-31_10-K_00551**, is among them; Mehul may want to report check 3 with and without it. The few-shot examples are still made up, so no sample passage is in the prompt.
- **v0 is AI-assisted.** Agreement with v0 isn't accuracy. Where v0 and the codebook seem to disagree (COF_00372/00373), these runs can't settle it.

## Cost
v1.2: 90 calls, 216,458 prompt tokens (191,872 cached), 25,221 output tokens (18,129 reasoning). That's about $0.02 off-peak or $0.04 peak; this run fell in DeepSeek's peak window (06:00–10:00 UTC). The balance went from ¥19.82 to ¥19.35 for the chat check plus the v1.1 and v1.2 runs, so about ¥0.64 (≈ $0.09) for everything on Oct 23.

## Next
- Agree the COF_00372/00373 question with Yen-Chu (codebook owner) before the Oct 27 taxonomy freeze; rerun with the final codebook then (bump `PROMPT_VERSION`).
- Then the 50-passage sample for check 3 and the red-team run for check 6, with Mehul.
- Still open for the team: a rule-based guardrail check that a use quote names AI. The prompt rule now does this; a code check in `verify_label` would make it hold without relying on the model.
