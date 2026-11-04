# Check 4: do the scores make sense? (first run, Oct 27)

> **Run:** `python3 -m src.eval.check4_sensitivity` ([script](../../src/eval/check4_sensitivity.py)), by Mehul. **Labels:** the AI-assisted v0 draft labels (the only labels covering every filing). Rerun with `--labels` on the human consensus set after adjudication (Nov 1).
> **Status:** first run. Part (c), face validity, is covered by the deck's "what filings miss" slide (Erica and LLM Suite appear in no filing).

## (a) Sensitivity: FY2025 AI Use Score under four rules

| Company | **Baseline** (3/1/0.5, ENT = 1) | ENT = 0 | D2 weight 2 | **Strict** (specific uses only) |
|---|---|---|---|---|
| Citigroup (benchmark) | 48 | 45 | 33 | 45 |
| Wells Fargo | 9 | 9 | 9 | 0 |
| Bank of America | 6 | 3 | 6 | 0 |
| Capital One | 3 | 0 | 3 | 0 |
| JPMorgan Chase | 3 | 3 | 3 | 0 |
| Principal | 0 | 0 | 0 | 0 |
| Schwab | 0 | 0 | 0 | 0 |

Rank agreement with the baseline (Spearman ρ, all 7 firms): ENT = 0 **0.92** · D2 weight 2 **1.00** · strict **0.62**.

**What it shows:**
1. **The weights don't drive the ranking.** Changing the D2 weight from 3 to 2 leaves the order unchanged (ρ = 1.00); it only shrinks Citi's lead.
2. **The ENT rule matters a little.** Giving general statements 0 points instead of 1 drops Bank of America and Capital One by 3 each, and the order mostly holds (ρ 0.92; 0.87 without Citi).
3. **A strict measure can't separate our six firms using filings alone.** Counting only specific uses, all six score **0**. In FY2025 filings their only specific (D2) statements are about governance and training (Wells Fargo's Head of AI, Principal's AI training), which count toward readiness, not use. Only Citi names specific deployed tools.
   - **This answers our question for Julie in advance:** a strict-only index would be flat for the six firms unless we add earnings calls, where executives name tools. That's an argument for keeping the broader measure and showing the strict one alongside it.

## (b) Benchmark: Dong et al. AI Intensity vs. our measures (FY2023 10-Ks)
FY2023 is the latest year in the Dong data (10-Ks filed early 2024).

| Company | Dong AI Intensity (All) | Our AI passages ("talk") | Our AI Use Score |
|---|---|---|---|
| Bank of America | 0.238 | 8 | 3 |
| Capital One | 0.187 | 11 | 3 |
| JPMorgan Chase | 0.091 | 2 | 3 |
| Schwab | 0.066 | 1 | 0 |
| Principal | 0.000 | 0 | 0 |
| Wells Fargo | 0.000 | 2 | 9 |

Spearman ρ: Dong vs. our talk volume **0.78**; Dong vs. our use score **0.14**.

**What it shows:** Dong's word-count measure follows how much a company *talks* about AI, not whether it *uses* it, as the evaluation plan predicted. That gap is what our index adds. Wells Fargo is the clearest case: 0 in Dong, because its parser missed the 10-K body, but the highest use score of the six in our data.

## Limits
- **Six firms (seven with Citi):** these correlations are indicative, not statistically strong.
- **Draft labels:** these are AI-assisted. The human consensus labels replace them after adjudication.
- **Fiscal-year coverage differs across firms** (filings from Q3 2024 onward plus Shu's FY2023 10-Ks), so FY2025 is the only year compared across all firms.
