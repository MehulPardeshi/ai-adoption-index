# Prompt tuning: classify-v1.0 → v1.4 (#35)

> File name kept from the v1.2 write-up; the v1.3 / v1.4 round is at the end.

> **Owner:** Shu Pu · **Date:** Oct 23, 2026 · **Builds on:** [first_run_results.md](first_run_results.md) (#66) · **Code:** [`src/agent/prompts.py`](../../src/agent/prompts.py)
> Same 90 FY2025 10-K passages (plus Citi's 20 as a benchmark, see below), same model (`deepseek-flash` = DeepSeek-V4.1-Flash-1017), guardrails on. Reference labels are still the **AI-assisted** draft labels (`passage_labels_v0.csv`), not ground truth.

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

## Citigroup as a benchmark (added Oct 23)
Citi is not one of the six PoC firms; the team keeps it as a benchmark (Oct 18 decision), and the v0 scores file already has a Citi row. So the agent files now cover **7 firms, 110 passages** (the six firms' 90 labels came from the cache; only Citi's 20 were new calls). Citi matters for a second reason: its 10-K has the only real D2 use among the seven, so it tests whether the v1.2 rules still find genuine use or just suppress everything.

**Citi FY2025 10-K, 20 passages:** evidence agreement with v0 17/20. The agent finds Citi's use (D1 ENT on "Citi has used AI and machine learning tools for many years and has more recently begun to broadly deploy Generative AI"; D1 OPS on AI for regulatory-report data governance; D1 GOV on the board Technology Committee), so the rules are not over-suppressing. The three differences:

| passage_id | Agent | v0 | What happened |
|---|---|---|---|
| C_2025-12-31_10-K_00831 | D1 GOV (model said **D2 GOV**, guardrail downgraded) | D2 GOV | The model named the right body (`specific` = "Technology Committee") but quoted the sentence after it ("Its responsibilities include ... Citi's approach to Generative AI"), so the body is not inside the quote and rule 5 of `verify_label` dropped it to D1. A correct D2 lost to quote selection; the guardrail worked as designed |
| C_2025-12-31_10-K_00131 | D1 OPS | D2 OPS | "applied technology solutions leveraging AI to support governance of data reported in key regulatory reports": no named tool, number, body, role or date, so D1 fits the codebook's D2 rule better than v0 does |
| C_2025-12-31_10-K_01476 | N | P ENT | "productivity assumptions tied to AI-driven operation model changes may materialize more slowly than expected". **This is the codebook's own P example**, and the agent missed it. The prompt has no P example and no rule for P; add one in the next prompt version (after the Oct 27 codebook freeze) |

Scores for Citi's 10-K alone under v1.2: agent AI Use **3** (OPS; 6 if ENT earns 1 point), v0 9 (12 with ENT); readiness 11 vs. 33 (the downgraded Technology Committee D2). Both gaps close in v1.4 (round 2 below). Citi's higher v0 score in `company_scores_v0.csv` (45) also counts its 10-Qs, which the agent has not labeled yet.

## Caveats
- **In-sample tuning.** The rules were written after looking at disagreements on these same 90 passages, so v1.2's numbers here are optimistic. The real test is check 3: human raters on the 50-passage sample (after Oct 27).
- **Overlap with the labeling sample:** 15 of the 90 passages are in `sample_passages.csv`. One of the passages I tuned on, **SCHW_2025-12-31_10-K_00551**, is among them; Mehul may want to report check 3 with and without it. The few-shot examples are still made up, so no sample passage is in the prompt.
- **v0 is AI-assisted.** Agreement with v0 isn't accuracy. Where v0 and the codebook seem to disagree (COF_00372/00373), these runs can't settle it.

## Cost
v1.2: 90 calls, 216,458 prompt tokens (191,872 cached), 25,221 output tokens (18,129 reasoning). That's about $0.02 off-peak or $0.04 peak; this run fell in DeepSeek's peak window (06:00–10:00 UTC). The balance went from ¥19.82 to ¥19.35 for the chat check plus the v1.1 and v1.2 runs, so about ¥0.64 (≈ $0.09) for everything on Oct 23.

## Round 2: v1.3 and v1.4 (Oct 23, after the Citi check)
Two prompt changes, both already required by the codebook:
- **Rule 3, P:** a stated intention, expectation or ongoing build is P, not hedging, including when it is framed as a risk that the plan slips; P takes a scenario. One made-up P example added.
- **Rule 8, quote holds the specific:** the D2 quote must contain the `specific` item; if the body is named in the sentence before the AI statement, quote both sentences.

**v1.3** fixed both Citi cases but brought back the few-shot-company confusion: with seven examples all called "Northwind Bank", the model flagged 3 real passages `company_mismatch` ("not the requested Northwind Bank") and sent 6 six-firm passages to review (JPM's AI-training label among them). **v1.4** keeps the v1.3 rules and gives each example its own made-up bank, with the security rule saying that without a "Requested company:" line there is no mismatch. v1.4 is the version kept.

| Six PoC firms (90 passages), after guardrail | v1.2 | v1.3 | **v1.4** |
|---|---|---|---|
| Evidence agreement with v0 | 85/90 | 86/90 | **85/90** |
| Cohen's kappa | 0.82 | 0.84 | 0.83 |
| Overclaim (target ≤ 5%) | 2 | 0 | **3 (3.3%)** |
| Underclaim | 2 | 2 | **1** |
| Scenario overlap (Jaccard) | 0.89 | 0.83 | 0.90 |
| needs_review | 1 | 6 | 2 |
| Spurious `company_mismatch` | 0 | 3 | 0 |

| Citi benchmark (20 passages) | v1.2 | v1.3 | **v1.4** |
|---|---|---|---|
| Evidence agreement with v0 | 17/20 | 19/20 | **19/20** |
| C_00831 Technology Committee | D1 (D2 downgraded) | D2 | **D2 pass** |
| C_00131 AI for regulatory-report data governance | D1 | D1 | **D2** (as v0) |
| C_01476 (the codebook's P example) | N | P OPS | P OPS at confidence 0.62 → needs_review |
| Citi AI Use / readiness (10-K only) | 3 / 11 | 3 / 33 | **9 / 33** (v0: 9 / 33) |

**What moved on the six firms, v1.2 → v1.4** (all Capital One; all in the risk-factor-says-own-use question already open with Yen-Chu):
- COF_00197 ("development and use of ... AI technologies") back to D1 ENT at 0.72 (v0 D1 ENT): the underclaim fixed.
- COF_00371 ("significant risks involved in using models and AI, and we cannot assure that our use will...") now D1 ENT (v0 N): the extra overclaim.
- COF_00373 now D1 **RISKM** instead of ENT;GOV (v0 N), so **COF scores 3** instead of 0. If Yen-Chu rules these risk-factor own-use sentences N, the three overclaims disappear and COF returns to 0; if she rules D1, v1.4's overclaim count is 0.
- COF_00375 and COF_00469: raw D1 at 0.55–0.62, held at N by the confidence rule (needs_review).

Verdict against the keep rule ("six-firm numbers must not get worse"): agreement and kappa unchanged, one underclaim traded for one overclaim, one more passage to review; the Citi benchmark and the Northwind bug are clearly better. Kept.

## Next
- Agree the COF risk-factor question (00371, 00372, 00373) with Yen-Chu (codebook owner) before the Oct 27 taxonomy freeze; rerun with the final codebook then (bump `PROMPT_VERSION`).
- Then the 50-passage sample for check 3 and the red-team run for check 6, with Mehul.
- Still open for the team: a rule-based guardrail check that a use quote names AI. The prompt rule now does this; a code check in `verify_label` would make it hold without relying on the model.
