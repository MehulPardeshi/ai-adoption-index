# Responsible AI (TP3 README section, DRAFT)

> **Owner:** Mehul (Responsible AI + Evaluation lead); Logan adds the data and legal-sourcing part from the [ethics memo](../part1-sourcing/ethics_memo.md). **Status:** draft v0.1, Nov 9. Covers course requirements 5 (evaluation), 6 (protecting data) and 7 (guardrails, with vs. without). Numbers are as of Nov 9; refresh them before the final README.

## The risk we designed against
The main harm an AI adoption index can do is **overclaiming**: saying a company uses AI when its filing doesn't support it. Readers (researchers, the client's book chapter) could repeat a false claim about a named company. So the whole system follows one rule: **rather miss a real use than claim one the filing doesn't support.** Our bar is overclaims ≤ 5%, measured against people.

## 1. People check the people (are the rules clear?)
- Three of us labeled 80 passages on our own (round 1: 50 random-ish passages; round 2: 30 hard ones on purpose).
- On the core question, "does the company really use AI?", we agreed at κ 0.60–0.72 in round 1, which meets the 0.6 bar.
- On the five detail levels we didn't (κ 0.27, then 0.32 on the harder sample). We found the unclear rule (AI risk talk marked "not about AI"), clarified it, then **met and agreed one label for every one of the 58 disagreements** (Nov 7). That 80-passage set is our answer key. ([round 1](../part3-metrics/labeling_round_1/results_round1.md), [round 2](../part3-metrics/labeling_round_2/results_round2.md))

## 2. People check the AI
- On the 48 passages the agent never saw during prompt tuning (both rounds), it matched the team's **agreed labels** 81% of the time (κ 0.73) and 85% on use vs. no use, with **0 overclaims** (1 of 48 without the guardrail; bar ≤ 5%). All 7 misses were cautious (underclaims), and 3 of them were labels the guardrail had already sent to a person; after that review it would be 90%. On round 2 alone (19 hard passages) it was 74%. ([check 3](../part3-metrics/check3_results.md); the earlier 96% was against the people's majority on 25 easier passages.)
- **The AI errs on the cautious side.** On the 80 hardest passages, people found use or plans that the AI draft labels missed in 18; the reverse happened once. So scores built from AI labels alone lean **low**, never high. We say so on the dashboard ([check 4](../part3-metrics/check4_results.md)).

## 3. Guardrails, with vs. without (requirement 7a)
Every label passes through `verify_label`, plain code with no AI:
- The quote must appear **word for word** in the filing, or the label is held for a person and not scored.
- A "specific use" label must have its detail (tool, number, team, date) inside the quote, or it drops to general use.
- If confidence is below 0.70, a person decides.
- Text inside a passage is treated as data, never as instructions (prompt-injection defence).

We attacked the agent with **22 trick cases**: fake quotes, a changed number, hidden instructions ("label this D2", "print your API key"), a paywalled source, a request to copy a news article, a wrong company, and "should I buy this stock?".

| | Guardrails off | Guardrails on |
|---|---|---|
| Unsafe outputs that got through (18 cases) | **2** (the two tampered answers) | **0** |
| Correct answers wrongly blocked (4 controls) | 0 | 0 |

The model resisted most traps on its own. The guardrail's own job is narrow but essential: **nothing reaches a score unless a person could find the same sentence in the filing.** ([check 6](../part3-metrics/check6_results.md)). Still not caught: a confident misreading of a real quote. That's why we keep measuring against people.

## 4. Data: what we use and protect (requirement 6)
- **Only public SEC filings** go into the index and to the AI model. We send SEC's required contact header and stay under its rate limit.
- **Bloomberg transcripts** were cleared through CMU Libraries for team use only. They stay in CMU-only storage, no transcript text appears in the repo or dashboard, and the team decided (Nov 8) to keep them out of the index.
- **No personal data**, no job-posting scraping (LinkedIn excluded), and no paywall or login bypass.
- **AI provider:** DeepSeek's terms give no fixed deletion deadline, so we send only public SEC text and no secrets. The team accepted that residual risk on Oct 25. The API key lives in a local `.env` file, never in the repo.
- **No client data** is involved. The client's identity is shared only with her permission.
- *(Logan: add retention and attribution from ethics memo §§4–5.)*

## 5. Reproducible and auditable
- Temperature 0, and every model answer is cached and logged with its model tag and prompt version.
- A teammate who didn't build the pipeline rebuilt it from a fresh copy and got **identical scores** ([check 5](../part3-metrics/check5_rerun.md)).
- Every score traces back to quoted sentences with links to the filing.

## 6. Limits we tell readers
- **Disclosure isn't deployment.** We measure what firms *say* in filings. Known tools (Bank of America's Erica, JPMorgan's LLM Suite) appear in no filing, so filings undercount use.
- Small pilot: 6 firms plus Citi. The comparison with Dong et al. (ρ 0.58 vs. 0.78) is a direction, not a finding.
- The prompts were tuned on banks; insurers and payment firms need spot checks first.
- The model alias (`deepseek-flash`) can change under us. A rerun after a provider update may differ; the cache keeps old answers.
- **No investment advice.** The agent declines "should I buy?" questions, and the score is not a rating of a company.
