# Agent re-run of the 110 passages with classify-v1.5, timed (#35, #97)

> **Owner:** Shu Pu · **Run:** Wed Nov 4, 2026 · **Files:** [`agent_labels_v1.csv`](../../data/processed/sec/agent_labels_v1.csv), [`agent_scores_v1.csv`](../../data/processed/sec/agent_scores_v1.csv), [`agent_run_info.json`](../../data/processed/sec/agent_run_info.json)

**Citi's numbers quoted in the slides and the TP2 example did not change:** `C_2025-12-31_10-K_00131` is still D2 OPS, `C_2025-12-31_10-K_00673` is still D1 ENT, and Citi's FY2025 AI Use Score is still 12.

The 110 passages are the six firms' FY2025 10-Ks (90) plus Citi's (20). Until now `agent_labels_v1.csv` was still labeled with v1.4, while check 3 used v1.5. Both now use the same prompt.

## Run facts
| | |
|---|---|
| Date and time | Nov 4, 2026, 21:46:34–21:50:29 UTC (4:46 pm ET, off-peak) |
| Prompt and model | `classify-v1.5`, `deepseek-flash` (DeepSeek-V4.1-Flash-1017), temperature 0, guardrails on, ENT = 1 point |
| Passages | 110 |
| New calls | 89 |
| Cache hits | 21 (the labeling-sample passages from the check 3 run; all 21 match `agent_labels_sample.csv`) |
| Wall time | **235 seconds** |
| **Seconds per new call** | **2.64** (one sequential run; cache hits take almost no time, so new calls are the right divisor) |
| Prompt tokens | 240,282 (202,752 cache hits, 37,530 misses) |
| Output tokens | 23,277 (16,373 of them reasoning) |
| Truncated replies | 0 |
| Cost | **about $0.020** off-peak, the rate this run paid; it would be about $0.040 at peak. About $0.00023 per new call |

Prices per 1M tokens, off-peak: cache hit $0.003, miss $0.15, output $0.60. Peak is double.

## Labels that changed, v1.4 → v1.5
8 of 110 changed in evidence level or scenarios, after the guardrail.

| passage_id | v1.4 | v1.5 | Note |
|---|---|---|---|
| JPM_2025-12-31_10-K_00497 | N | X | Risk-factor lead-in line, read as a heading (confidence 0.60) |
| COF_2025-12-31_10-K_00256 | N | X | Risk-factor heading; now matches the draft labels |
| COF_2025-12-31_10-K_00310 | N | X | AI appears only in a cross-reference to a heading |
| COF_2025-12-31_10-K_00371 | D1 ENT | D1 RISKM | Scenario only |
| COF_2025-12-31_10-K_00372 | D1 ENT | N | The model still says D1 ENT, but at confidence 0.60; the guardrail sent it to review |
| COF_2025-12-31_10-K_00373 | D1 RISKM | D1 RISKM;GOV | Scenario added |
| COF_2025-12-31_10-K_00977 | N | X | Underwriting models with no mention of AI: the "search hit not actually about AI" wording added in #64 |
| C_2025-12-31_10-K_01476 | N (needs_review) | P ENT | The codebook's own P example now passes, at confidence 0.70, exactly the threshold |

The rules are the same as v1.4; only the codebook text from #64 changed. COF_00977 follows directly from that text. The others can't be separated from run-to-run variance, which we already saw at temperature 0 in check 3.

## FY2025 AI Use Score per firm (ENT = 1 in both)
| Firm | v1.4 | v1.5 |
|---|---|---|
| JPM | 3 | 3 |
| BAC | 3 | 3 |
| COF | 6 | 6 |
| WFC | 3 | 3 |
| SCHW | 0 | 0 |
| PFG | 0 | 0 |
| Citi (benchmark) | 12 | 12 |

No AI Use Score moved. Two other columns did: COF's readiness went from 0 to 11 and its talk ratio from 83% to 85%; Citi's talk ratio went from 82% to 76%.

## Guardrail (`verify_status`)
| | v1.4 | v1.5 |
|---|---|---|
| pass | 107 | 105 |
| downgraded | 0 | 0 |
| needs_review | 3 | 5 |

All five held at N for confidence below 0.70: JPM_00504 (model said P TALENT, 0.62), BAC_00247 (D1 ENT, 0.68), COF_00372 (D1 ENT, 0.60), COF_00469 (D1 ENT, 0.68) and COF_00475 (D1 ENT, 0.62). That is 4.5% of the passages.

## Against the draft labels
The draft labels are AI-assisted, so they are a reference, not ground truth; check 3 against the humans is in [`check3_agent.md`](../part3-metrics/labeling_round_1/check3_agent.md).

| | v1.4 | v1.5 |
|---|---|---|
| Six firms: evidence agreement | 85/90 | 84/90 |
| Six firms: overclaim | 3 (3.3%) | 2 (2.2%) |
| Six firms: underclaim | 1 | 1 |
| Citi: evidence agreement | 19/20 | 20/20 |
