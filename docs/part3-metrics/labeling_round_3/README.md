# Labeling round 3: the sector pilot (new firm types)

**Why.** The agent was tuned and checked on bank filings (check 3: 81% exact on 48 unseen passages,
0 overclaims). The S&P 500 Financials index (#133, #134) adds insurers, asset managers and brokers,
payment firms and exchanges. On Nov 10 we told Julie we'd check those types before trusting their
scores: two people label about 10 passages per type on their own, and we compare the agent with them
using the same bar as now (overclaim at most 5%). A type that misses gets its own rules and a rerun.

**The sample** (`sample_passages.csv`, built by `python3 -m src.eval.make_sector_pilot_sample` after
the agent run): 40 passages, 10 per new type, from firms outside our 7 proof-of-concept firms. Per type,
up to 5 passages the agent calls use (where an overclaim would show), up to 1 plan, the rest no use;
at most 2 per firm; fixed seed. It holds **no labels**. The agent's labels are in `agent_key.csv`:
raters don't open it.

**How to label** (same tools and cheat sheet as rounds 1 and 2):
1. `python3 -m src.eval.make_labeling_workbook 3` builds the Excel workbook in this folder.
2. Each rater saves a copy as `labeling_<name>.xlsx` and fills it in alone, using the
   [round 2 cheat sheet](../labeling_round_2/cheat_sheet.md) (CREDIT already covers underwriting,
   insurance included). When a real use fits no area well, for example insurance claims handling,
   pick the closest one and say so in the note: those notes tell us whether the 11 areas need a
   change for that firm type.
3. `python3 -m src.eval.workbook_to_csv labeling_<name>.xlsx <name> 3` writes `rater_<name>.csv`.
4. The two raters settle their disagreements together; the agreed label is the answer key.

**Raters and status:** Logan and Snehal were assigned as the two raters for issue #169. They label independently before comparing answers. Snehal's independent labels are in `rater_snehal.csv`; Logan's are in `Labeling3_workbook_Logan.csv`. They settled their disagreements on Nov 24: the agreed labels (the answer key) are in `Labeling3_final.csv`.

**Results:** [results_round3.md](results_round3.md) (`python3 -m src.eval.round3_results`): 2 overclaims in 40 (5%, at the bar). Decision (Nov 24): no per-type rules or rerun; the 1-in-10 result for two types is noted as a limit (memory/09).
