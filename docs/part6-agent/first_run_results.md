# Agent first run: DeepSeek on the six FY2025 10-Ks (#35)

> **Owner:** Shu Pu · **Run:** Oct 23, 2026 · **Issue:** #35 · **Design:** [agent_design.md](agent_design.md)
> **Files:** [`agent_labels_v1.csv`](../../data/processed/sec/agent_labels_v1.csv), [`agent_scores_v1.csv`](../../data/processed/sec/agent_scores_v1.csv), [`agent_run_info.json`](../../data/processed/sec/agent_run_info.json)
> **Later update:** the three files were overwritten by the classify-v1.2 run ([prompt_tuning_v1.2.md](prompt_tuning_v1.2.md)). The v1.0 files described here are in commit `dcc44d8` (PR #66).
> **Reference labels:** `passage_labels_v0.csv` is **AI-assisted** (drafted with Claude; see the 2026-10-19 decision), so it is a reference here, not ground truth. Real accuracy comes from check 3, against the human raters, after Oct 27.

## Setup
| Item | Value |
|---|---|
| Passages | 90 AI passages from the FY2025 10-Ks of JPM (20), BAC (24), COF (32), WFC (7), SCHW (4), PFG (3) |
| Command | `python -m src.agent.run_batch --tickers JPM,BAC,COF,WFC,SCHW,PFG --year 2025 --forms 10-K` |
| Model | `deepseek-flash` = DeepSeek-V4.1-Flash-1017, checked against `GET /models` and DeepSeek's pricing and change-log pages. JSON mode and tool calling both tested |
| Settings | temperature 0, JSON mode, `PROMPT_VERSION` classify-v1.0 (unchanged from #60), guardrails on, confidence threshold 0.70, ENT not counted (default until the #33 vote) |
| Prompt tuning | none in this run. This is the v1 prompt as merged |

### A bug found and fixed before the run that counts
The first attempt lost **13 of 90 replies** (empty, or JSON cut off mid-object). This model thinks before it answers, and its reasoning tokens count toward `max_tokens`; the 500-token cap ran out first. The guardrail did its job (all 13 went to `needs_review`, none was scored), but the results were not usable. Fixes in this PR:
- `MAX_TOKENS_CLASSIFY` and `MAX_TOKENS_CHAT` raised to 4000 (`src/agent/config.py`).
- `llm.py` no longer caches a reply that hit the token limit or came back empty, so a rerun retries it; it also records `finish_reason`, reasoning tokens and a truncation count in the run's usage.
- `config.py` now loads `.env` before reading the model settings. Before, a `DEEPSEEK_MODEL` override in `.env` was silently ignored.

The rerun had **0 truncated replies**. Everything below is from the rerun.

## Cost
From `agent_run_info.json`: 90 calls, 161,468 prompt tokens (144,750 served from DeepSeek's cache, 16,718 not), 24,464 output tokens (17,161 of them reasoning).

| | Off-peak | Peak (01:00–04:00, 06:00–10:00 UTC weekdays) |
|---|---|---|
| This run | about **$0.018** | about $0.035 |

The account balance went from ¥19.99 to ¥19.82 (¥0.17, about $0.02) for all of today's calls: the model checks, the 3-passage smoke test, the failed first attempt and this run. That matches the #55 estimate (about $0.05 for all 245 passages; under $5 for the project). Shu paid with his own key, since the #55 funding vote is on Sun Oct 25.

## Agent vs. the draft labels (90 passages)
| Measure | After guardrail (`evidence_v0`) | Model's own call (`evidence_raw`) |
|---|---|---|
| Evidence-level agreement | **80/90 (88.9%)**, kappa 0.67 | 77/90 (85.6%), kappa 0.60 |
| Use vs. no-use kappa (D1/D2 vs. rest) | 0.70 | 0.61 |
| **Overclaim** (agent D1/D2, v0 N/P/X) | **6 (6.7%)**; target ≤ 5% | 9 (10.0%) |
| Underclaim (agent N/P/X, v0 D1/D2) | 1 (1.1%) | 1 (1.1%) |
| Scenario overlap (10 passages both D2/D1/P) | mean Jaccard 0.78, 7 exact | — |
| Topic agreement | 74/90 | — |

**Guardrail (`verify_status`):** pass 87, downgraded 0, needs_review 3. All three were D1 calls with confidence 0.60–0.62 (BAC_00247, COF_00375, COF_00475). The guardrail took the overclaim rate from 10.0% to 6.7%.

Confusion matrix, after the guardrail (rows = agent, columns = v0):

| | D2 | D1 | P | N | X | total |
|---|---|---|---|---|---|---|
| **D2** | 2 | 2 | 0 | 0 | 0 | 4 |
| **D1** | 0 | 6 | 0 | 5 | 1 | 12 |
| **P** | 0 | 0 | 0 | 0 | 0 | 0 |
| **N** | 0 | 1 | 0 | 69 | 1 | 71 |
| **X** | 0 | 0 | 0 | 0 | 3 | 3 |
| total | 2 | 9 | 0 | 74 | 5 | 90 |

## Company scores (FY2025)
| Ticker | Agent: AI Use | Agent: use scenarios | v0: AI Use | v0: use scenarios | Agent, ENT = 1 | v0, ENT = 1 |
|---|---|---|---|---|---|---|
| JPM | 9 | RISKM | 3 | RISKM | 9 | 3 |
| BAC | 3 | RISKM | 3 | OPS | 6 | 6 |
| COF | 3 | RISKM | 0 | — | 6 | 3 |
| WFC | 0 | — | 9 | CX OPS RISKM | 3 | 9 |
| SCHW | 27 | ADV FRAUD RISKM | 0 | — | 27 | 0 |
| PFG | 0 | — | 0 | — | 0 | 0 |

(v0 scores recomputed on the same 90 passages. The ENT columns use `score_companies.py --ent-counts`. Readiness and talk ratio are in the CSV.)

## What the disagreements show
1. **"Models" read as "AI" (the biggest problem).** Three use labels quote text that never mentions AI: JPM_02064 (the Model Risk Governance and Review function, coded D2), BAC_00279 (market-risk models, D1) and SCHW_00551 (a list of model uses, D2 with four scenarios). In each, the passage mentions AI elsewhere, but the quoted sentence is about models in general. These three labels produce almost all of the agent's AI Use points: JPM's 9, BAC's 3 and SCHW's 27. The guardrail checks that the quote is in the passage, not that it is about AI.
2. **Capital One risk factors read as own use.** Four COF overclaims (00310, 00369, 00371, 00372) are risk-factor sentences such as "our evolving use of AI". The agent treats them as the company stating its own general use (D1 ENT); v0 calls them risk talk (N) or a heading (X). Because they are ENT, they score 0 today. If ENT earns 1 point after the vote, they would add to COF's score.
3. **WFC: the ENT rule in action.** WFC_01363 ("We also use AI to help improve efficiency and further inform or automate certain business decisions, operations, and risk management practices…") is D1 in both, but the agent codes it ENT where v0 has RISKM;OPS;CX. That is the rule proposed in #64 (a general multi-area sentence counts once, as ENT), and it moves WFC from 9 to 0 (3 if ENT counts). The v0 labels predate that rule.
4. **One underclaim.** BAC_00281 ("take steps to leverage emerging technologies, such as automation, AI and robotics") is N for the agent and D1 OPS in v0. The agent reads it as a generic list inside a data-risk factor.
5. **Level differences that don't change use.** COF_00256 (N vs. X for a risk-factor bullet). JPM_02064 and SCHW_00551 are also D2 vs. v0's D1 (see 1).

## All disagreements
Evidence level after the guardrail; "agent raw" is the model's own call. Quotes are the agent's `quote` field, cut where marked; full passages are in `data/interim/sec/ai_passages.csv`.

| passage_id | Type | Agent (raw) | v0 | Agent quote | Source |
|---|---|---|---|---|---|
| BAC_2025-12-31_10-K_00279 | overclaim | D1 RISKM (same) | N | "The models that we use to assess and control our market risk exposures also reflect assumptions about the degree of correlation…" | [10-K](https://www.sec.gov/Archives/edgar/data/70858/000007085826000157/bac-20251231.htm) |
| COF_2025-12-31_10-K_00310 | overclaim | D1 ENT (same) | N | "our evolving use of AI" | [10-K](https://www.sec.gov/Archives/edgar/data/927628/000092762826000024/cof-20251231.htm) |
| COF_2025-12-31_10-K_00369 | overclaim | D1 ENT (same) | X | "our evolving use of AI" | [10-K](https://www.sec.gov/Archives/edgar/data/927628/000092762826000024/cof-20251231.htm) |
| COF_2025-12-31_10-K_00371 | overclaim | D1 ENT (same) | N | "our use of models and AI could result in inaccurate forecasts, ineffective risk management practices…" | [10-K](https://www.sec.gov/Archives/edgar/data/927628/000092762826000024/cof-20251231.htm) |
| COF_2025-12-31_10-K_00372 | overclaim | D1 ENT (same) | N | "the models or AI solutions that we or a third party create and use" | [10-K](https://www.sec.gov/Archives/edgar/data/927628/000092762826000024/cof-20251231.htm) |
| COF_2025-12-31_10-K_00373 | overclaim | D1 RISKM;GOV (same) | N | "Our risk reporting and risk management, including our business decisions that are based on information gathered through models and AI…" | [10-K](https://www.sec.gov/Archives/edgar/data/927628/000092762826000024/cof-20251231.htm) |
| BAC_2025-12-31_10-K_00281 | underclaim | N (same) | D1 OPS | — (v0 cites "take steps to leverage … automation, AI and robotics") | [10-K](https://www.sec.gov/Archives/edgar/data/70858/000007085826000157/bac-20251231.htm) |
| JPM_2025-12-31_10-K_02064 | level | D2 RISKM;GOV (same) | D1 RISKM | "A dedicated independent function, Model Risk Governance and Review ("MRGR"), defines and governs the Firm's policies…" | [10-K](https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/jpm-20251231.htm) |
| SCHW_2025-12-31_10-K_00551 | level | D2 RISKM;FRAUD;ADV;GOV (same) | D1 GOV | "estimating interest and credit risk for loans and other balance sheet assets" | [10-K](https://www.sec.gov/Archives/edgar/data/316709/000031670926000009/schw-20251231.htm) |
| COF_2025-12-31_10-K_00256 | level | N (same) | X | — | [10-K](https://www.sec.gov/Archives/edgar/data/927628/000092762826000024/cof-20251231.htm) |
| WFC_2025-12-31_10-K_01363 | scenario only | D1 ENT (same) | D1 RISKM;OPS;CX | "We also use AI to help improve efficiency and further inform or automate certain business decisions, operations, and risk management practices" | [10-K](https://www.sec.gov/Archives/edgar/data/72971/000007297126000133/wfc-20251231.htm) |

## Next (not in this PR)
- **Prompt tuning** (bump `PROMPT_VERSION` each time): tell the model that a sentence about models in general is not AI unless it names AI; risk-factor wording such as "our evolving use of AI" is N unless the passage says what the AI does (to agree with the codebook owner first).
- **Possible guardrail rule** (team decision, with Mehul for check 6): a D2/D1/P quote must contain an AI term (AI, artificial intelligence, machine learning, generative AI, LLM…). It would have caught all three cases in finding 1.
- After Taxonomy v0 is final (Oct 27): rerun with the final codebook, then the 50-passage sample for check 3 and the red-team run for check 6.

## Chat mode check (Oct 23)
`python -m src.agent.chat --trace "How does JPMorgan use AI in FY2025, and how does it compare with Dong?"` ran end to end with no code change. DeepSeek chose 4 tool calls on its own: `get_labels` (JPM FY2025, D2/D1) → `score_companies` → `lookup_baseline` (FY2023) → `get_labels` (all JPM FY2025 labels). Multi-turn tool calls work in thinking mode without sending `reasoning_content` back.

The answer:
- cited both verified JPM use labels (00150, AI training; 02064, MRGR) with passage_id and quote;
- reported AI Use 9, Readiness 44 and talk ratio 89%;
- gave Dong's FY2023 AI Intensity correctly (0.0571 core, 0.0913 all; 10-K filed 2024-02-16, 87,627 words; checked against `dong_baseline_6firms.csv`);
- explained that Dong counts words while our labels test for use, and that Dong stops at FY2023;
- ended with the "not investment merit" disclaimer from the guarded prompt.

The answer itself calls the MRGR passage "a control/oversight structure, not a named AI deployment", which is finding 1 above: the score counts it, the chat answer doesn't.
