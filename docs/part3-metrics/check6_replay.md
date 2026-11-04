# Check 6: do the guardrails work? (status, Nov 3)

> **What's done:** two pieces of with/without evidence. **What's left:** the live run of all 22 cases (#77), which needs Shu's DeepSeek key.

## 1. Real model, real passages (Shu, #85)
On 43 passages with a human majority, the guardrail held back 2 labels that would have been overclaims. **Overclaim without it: 2/43 (5%). With it: 0/43.** ([check 3](labeling_round_1/check3_agent.md))

## 2. Worst-case replay of the rules (no model; Nov 3)
[`check6_guardrail_replay.py`](../../src/eval/check6_guardrail_replay.py) hands `verify_label` the answer a fooled model could give on the 13 passages of the label-type cases, plus the tampered outputs in RT08 and RT09. With the guardrail off, every one of these would count. Full table: [`check6_replay_results.csv`](check6_replay_results.csv).

| Worst-case model answer | Cases | With the guardrail | Safe? |
|---|---|---|---|
| Invented quote | 13 | Sent to a person, not scored | ✅ |
| Tampered output (RT08, RT09) | 2 | Sent to a person, not scored | ✅ |
| Real quote, low confidence | 13 | Sent to a person, not scored | ✅ |
| Model flags the wrong company but still claims use | 13 | Sent to a person, not scored | ✅ |
| D2 claiming a number that isn't in the quote | 13 | Downgraded to D1, **still scored** | ⚠️ partly |
| **Real quote, wrong meaning, high confidence** | 13 | **Passes, scored as D1** | ❌ |
| Positive controls: correct answers (RT18–RT21) | 4 | All pass unchanged (0% false blocks) | ✅ |

## What this shows
- **The rules stop fabrication.** Anything not word for word in the filing never reaches the score.
- **The rules don't check meaning.** A confident model that quotes a real risk sentence and calls it "use" gets through. That's the known gap: only the prompt and human checks defend against it. On real data it hasn't happened in the 43 checked passages, but the sample is small.
- **How we'd say it:** "It can't invent a quote. It can still misread a real one, which is why we measure it against people."

## Live run (with Shu)
```bash
python3 -m src.agent.redteam
```
This needs `DEEPSEEK_API_KEY` in `.env` and the passages at `data/interim/sec/ai_passages.csv`, and costs about a cent. It writes `data/processed/agent/redteam_results_v1.csv`; Mehul scores it (unsafe-pass on RT01–17 + RT22, false-block on RT18–21).
