# Check 1: did we find the AI text?

> **Run:** Nov 3, 2026 ([script](../../../src/eval/make_recall_sample.py), seed 20261103), on the 74 official filings re-downloaded from EDGAR.
> **Status: reviewed and confirmed by Mehul (Evaluation lead), Nov 3**, with the four borderline items checked one by one. Sample: [`recall_sample.csv`](recall_sample.csv).

## Precision: meets the bar (≥ 0.95)
- **98.9%** of flagged passages use an AI term in the AI sense (274 of 277); on the 245-passage test-run window, 99.2% (243 of 245).
- The 3 misses are the same Capital One paragraph across years: "underwritten using an automated underwriting system based on predictive models". AI isn't named. They're labeled N, so they don't affect the use score.
- The human raters agree: Logan and Yen-Chu marked all 50 round-1 passages as about AI. (The third rater's "not about AI" marks are the round-1 misread rule, not false hits.)
- 26 of the 277 are headings, acronym lists or glossaries that do mention AI. They're labeled X and kept out of the scores.

## Recall: no clear miss found
132,998 paragraphs weren't flagged. We can't read them all, so we did two things.

**Sweep of all of them for wording the search could miss:**

| Wording | Paragraphs |
|---|---|
| Spelling variants (e.g., "machine‑learning" with other hyphens, "A.I.") | 0 |
| Assistants and bots ("virtual assistant", "digital assistant", "robotic") | 0 |
| "Intelligent systems", "cognitive computing" | 0 |
| Product names (Erica, LLM Suite, ChatGPT, OpenAI) | 0 |
| "Deep fakes" | 3 |
| Robo or automated advice | 6 |

**Sample of 100 near-miss paragraphs** (all 10 distinct "algorithm" paragraphs, plus "automation", "emerging technology", "machine", "model"): **0 name AI** and **4 borderline** (2 distinct paragraphs):
- **Schwab Intelligent Portfolios** (items 11, 54): "fully automated online investment advisory service", "robo-advice technology".
- **Capital One's "deep fakes"** (items 34, 52): a cyber threat; it would be N, so no score effect.

## What this means
1. **The search isn't losing explicit AI language.** The limit is what filings say, not how we search: Erica and LLM Suite appear in no filing.
2. **Open question for the team: does robo-advice count?** Filings describe it without saying AI, so our search doesn't flag it. It's in the advice and retirement area closest to Julie's chapter, and Schwab scores 0. Counting it would change the scope of the taxonomy (frozen #84), so it's a team and client decision. For now it's a documented limitation.

## Limits
- The sample is targeted, so this isn't a statistical recall rate. Zero misses in 100 gives roughly a 3% upper bound for near-miss paragraphs like these (rule of three), not for all text.
- A paragraph can describe AI with none of the words we swept; only reading everything would rule that out.
