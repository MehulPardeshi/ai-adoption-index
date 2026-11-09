# Adjudication of the round 1 and 2 disagreements

Two copies of the same 58 passages (37 from round 1, 21 from round 2). The passage text, links and the three raters' labels are identical in both (checked Nov 8).

| File | What it is |
|---|---|
| [`adjudication_sorted_yenchu.xlsx`](adjudication_sorted_yenchu.xlsx) | **Use this one in the meeting.** Yen-Chu's version (shared Nov 7): the passages sorted into 6 groups by the question to settle, each with the rule to check and a time budget (~60 min). Colors: green = rule already clear, orange = discuss, red = all three differ |
| [`adjudication_sheet.xlsx`](adjudication_sheet.xlsx) | The original sheet in round order, made by `src/eval/make_adjudication_sheet.py` |

| Group | Question | Passages | Time |
|---|---|---|---|
| 1 Acronym list / definition | X vs. D2/N | 4 | 5 min |
| 2 Risk talk | N vs. X | 16 | 10 min |
| 3 Planned or just talk | P vs. N | 9 | 10 min |
| 4 Real use or talk | N vs. D1/D2 | 16 | 20 min |
| 5 Specific or general | D1 vs. D2 | 10 | 10 min |
| 6 Mixed | other | 3 | 5 min |

**Status (Nov 8):** Yen-Chu, Logan and Snehal agreed the labels on Sat Nov 7. The filled file is now in the repo: `agreed_evidence` is filled for all 58 passages on the "Sorted for meeting" tab.

**Still open (Nov 8, 8:44 pm):** the raters added scenarios to 7 of the 8 P passages. `BAC_2025-12-31_10-K_00264` (P) still has no scenario, and `SCHW_2024-12-31_10-K_00562` (unanimous D1, see below) still needs one. The raters add them.

**How to finish:** the three raters (Yen-Chu leads, with Logan and Snehal) fill in `agreed_evidence`, `agreed_scenarios` and, where useful, `note` on the "Sorted for meeting" tab, then share the file. Mehul commits it and reruns check 4 (#101) on the consensus labels.

**Rules:** the raters decide the labels themselves; no AI tool picks or suggests them. A passage with no agreement stays blank with a note; it is reported, not forced.

**Consensus files (Nov 8):** [`consensus_labels.csv`](consensus_labels.csv) holds all 80 human-labeled passages (58 agreed here plus 22 where the evidence was unanimous; for those, the scenarios at least 2 of 3 raters chose). [`labels_v0_plus_consensus.csv`](labels_v0_plus_consensus.csv) is the draft label file with these 80 swapped in, used for the [check 4 rerun](../check4_results.md). Rebuild both after the missing scenarios are added: `python3 -m src.eval.make_consensus_labels`. Besides the 8 P passages listed above, `SCHW_2024-12-31_10-K_00562` (unanimous D1) needs a scenario, because no two raters picked the same one.
