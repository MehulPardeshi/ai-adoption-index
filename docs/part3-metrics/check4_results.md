# Check 4: do the scores make sense? (first run Oct 27; rerun on human labels Nov 8)

> **Run:** `python3 -m src.eval.check4_sensitivity` ([script](../../src/eval/check4_sensitivity.py)), by Mehul. **Labels:** the AI-assisted v0 draft labels (the only labels covering every filing). Rerun with `--labels` on the human consensus set after adjudication (Nov 1).
> **Status:** first run below; **rerun on the human consensus labels on Nov 8 (next section)**. Part (c), face validity, is covered by the deck's "what filings miss" slide (Erica and LLM Suite appear in no filing).

## Rerun on the human consensus labels (Nov 8, #101)

> **Run:** `python3 -m src.eval.make_consensus_labels`, then `python3 -m src.eval.check4_sensitivity --labels docs/part3-metrics/adjudication/labels_v0_plus_consensus.csv` (Claude, for Mehul). **Labels:** the 277 draft labels with the **80 human-labeled passages** (rounds 1 and 2) replaced by the raters' consensus ([`consensus_labels.csv`](adjudication/consensus_labels.csv)): 58 agreed by Yen-Chu, Logan and Snehal on Nov 7 (#124), and 22 where all three gave the same evidence level, with the scenarios at least 2 of the 3 chose. The other 197 passages keep their AI-assisted draft labels. The scenarios aren't filled in yet for 9 passages: the 8 agreed as P, plus one D1 where no two raters picked the same scenario (`SCHW_2024-12-31_10-K_00562`). They add nothing until filled in. At most that's about 1.5 points per new scenario (0.5 / 33) for the 6 FY2025 ones; the raters are adding them.

| Company | Baseline (draft) | **Baseline (consensus)** | ENT = 0 | D2 weight 2 | Strict |
|---|---|---|---|---|---|
| Citigroup (benchmark) | 48 | **52** | 42 | 36 | 45 |
| Capital One | 3 | **18** | 15 | 18 | 0 |
| Principal | 0 | **18** | 9 | 12 | 18 |
| Wells Fargo | 9 | **9** | 6 | 9 | 0 |
| Schwab | 0 | **6** | 3 | 6 | 0 |
| Bank of America | 6 | **3** | 0 | 3 | 0 |
| JPMorgan Chase | 3 | **3** | 3 | 3 | 0 |

Rank agreement with the consensus baseline (Spearman ρ, all 7 firms): ENT = 0 **0.96** · D2 weight 2 **0.99** · strict **0.75** (6 PoC firms: 0.94 · 0.99 · 0.54).
Dong et al. benchmark (FY2023 10-Ks, n = 6): Dong vs. our talk volume **0.78** (unchanged), Dong vs. our use score **0.58** (was 0.14).

**What changed and why:**
1. **The draft labels were cautious.** On the 80 passages, the human consensus matched the draft evidence level on 57 (71%). In 18 of the 23 differences, people saw use or a plan where the draft said N; only one went the other way. The sample was built from hard and disputed cases, so this isn't a random-sample error rate. Still, it says the draft-based scores (and the dashboard, which reads them) **understate** use.
2. **The ranking rules still hold.** Weights and the ENT rule barely move the order (ρ 0.94–0.99), so the conclusion from the first run stands.
3. **Firm order changed.** Capital One and Principal rise to 18 (Capital One: mostly one D1 passage the raters tagged with five use areas, where the draft had only ENT; five more passages moved from N to general D1 use, which adds little. Principal: the raters tagged its D2 training passage with the OPS and ENT areas as well as TALENT). Bank of America drops to 3.
4. **The strict measure is no longer flat.** Principal scores 18 counting only specific uses, so the first run's "all six score 0" no longer holds. A strict-only index would still be close to zero for five of the six firms.
5. **The talk-vs-use gap is smaller than the first run showed.** The use score now follows Dong more (0.58 vs. 0.14); talk volume still follows it most closely (0.78). With six firms neither number is reliable, so present this as a direction, not a finding.

**Next:** fill in the 9 missing scenarios and rerun (two commands above). Re-scoring the dashboard on the consensus labels is a team decision (it would mix human and draft labels).

## First run (Oct 27, draft labels)

### (a) Sensitivity: FY2025 AI Use Score under four rules

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

### (b) Benchmark: Dong et al. AI Intensity vs. our measures (FY2023 10-Ks)
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
