# Labeling round 2 (30 passages)

> **Why a round 2:** round 1 met the bar on "real use vs. not" (κ 0.60–0.72) but not on the five evidence levels (Fleiss κ 0.27), mostly because the "about AI" rule was read two ways ([round-1 results](../labeling_round_1/results_round1.md)). Round 2 checks whether the clarified cheat sheet fixes that.
> **Raters:** Logan, Yen-Chu, Snehal (same as round 1). **Time:** about 30 minutes. **Submit by Sun Nov 1, before the team meeting.**

## What's different from round 1
- **Cheat sheet v2** ([`cheat_sheet.md`](cheat_sheet.md)): same rules, now word for word the frozen codebook. Changes are marked 🆕. The main one: **AI risks, threats and laws are still about AI** (`about_ai` = Y, evidence N).
- **Practice first:** six made-up passages with answers, in section 4 of the cheat sheet. Takes 2 minutes.
- **New passages:** none were in round 1. The sample targets the rules round 1 got wrong (how it was built is below).

## How to label (same as round 1)
1. Read the [cheat sheet](cheat_sheet.md) and do the practice set.
2. Copy [`labeling_workbook.xlsx`](labeling_workbook.xlsx) somewhere **outside the repo** (e.g. `labeling2_<yourname>.xlsx`) and fill in the four yellow columns. The second tab is the cheat sheet.
3. Convert it (this also checks it): `python3 -m src.eval.workbook_to_csv labeling2_<yourname>.xlsx <yourname> 2`
   This writes `rater_<yourname>.csv` in this folder. Or send the filled workbook to Mehul.
4. Open a pull request named "Labeling round 2: <name>".

**Rules:** label on your own, with your own judgment (AI tools only for opening files). Don't open `passage_labels_v0.csv`, `company_scores_v0.csv` or any `agent_labels_*.csv`. Don't discuss items until all three have submitted.

## How the sample was built
[`src/eval/make_labeling_sample_round2.py`](../../../src/eval/make_labeling_sample_round2.py), seed 20261027, reproducible.
- **Pool:** the 277 AI passages, minus everything raters saw in round 1, minus the guardrail test passages (their expected answers are public), minus repeats. Filings re-use risk paragraphs year after year, so passages whose first 25 words match count as one.
- **Problem:** round 1 used every "use" passage, so a random 30 would be almost all easy "just talk" passages, and agreement would look high for the wrong reason.
- **So it targets the round-1 weak spots** (strata from the AI-assisted draft labels, which raters never see):

| Stratum | Count | Tests |
|---|---|---|
| Every remaining D1 passage | 3 | Real use |
| N passages where the company talks about its **own** models or AI ("we use", "our models") | 12 | The D1-vs-N boundary: risk factors that admit use, hedged "may use" |
| Other N passages (risks, threats, laws) | 11 | The clarified "about AI" rule |
| X passages (definitions, headings, non-AI hits) | 4 | X vs. N |

**Known limits** (reported with the results):
- No D2 or P passages are left in the pool, so round 2 can't re-test D2 vs. D1 or P vs. N. Those get tested on new text (earnings calls if cleared, or FY2026 filings).
- Capital One is 13 of 30 passages, because it has the most AI risk text.
- 11 of the 30 are in the agent's tuning set, so check 3 reports the other 19 separately.

## Scoring (Mehul)
`python3 -m src.eval.irr --round 2` gives the same reports as round 1. Add `--ai-labels <agent labels>` for check 3.
