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

**Still open:** 8 passages agreed as **P** have no `agreed_scenarios` yet (the rules require a scenario for D2/D1/P): `COF_2024-12-31_10-K_00357`, `COF_2025-12-31_10-K_00480`, `WFC_2025-12-31_10-K_01394`, `BAC_2025-12-31_10-K_00264`, `COF_2023-12-31_10-K_00354`, `C_2025-12-31_10-K_00670`, `JPM_2025-12-31_10-K_00493`, `JPM_2025-12-31_10-K_00547`. The raters add them.

**How to finish:** the three raters (Yen-Chu leads, with Logan and Snehal) fill in `agreed_evidence`, `agreed_scenarios` and, where useful, `note` on the "Sorted for meeting" tab, then share the file. Mehul commits it and reruns check 4 (#101) on the consensus labels.

**Rules:** the raters decide the labels themselves; no AI tool picks or suggests them. A passage with no agreement stays blank with a note; it is reported, not forced.
