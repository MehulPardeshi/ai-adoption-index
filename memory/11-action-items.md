# 11 — Action Items (who is doing what, right now)

> **Read this to answer "what should I work on next?"** Updated after every meeting from `meetings/` minutes ([procedure](../meetings/README.md)). The shared spreadsheet remains the source of truth for owners and deadlines; this file mirrors it for AI tools.
> **Last updated:** 2026-10-29 (Julie checkpoint). Last meeting: [Oct 29 client checkpoint](../meetings/2026-10-29-client.md) (transcript). Previous: [Oct 28 practice run](../meetings/2026-10-28-internal.md).
> **Pinned summary for humans:** [#45 "Who does what"](https://github.com/MehulPardeshi/ai-adoption-index/issues/45), with @mentions per person.
> **GitHub:** each task below is an issue in the **"Sprint: Oct 18–Nov 6 (TP2)"** milestone on the [project board](https://github.com/users/MehulPardeshi/projects/1).

## Where we are
- ✅ TP1 submitted (Fri Oct 2).
- 🏁 **Sprint: Sun Oct 18 → Fri Nov 6 (TP2).** ✅ Categories frozen, round 1 labels in, checks 2–4 run (Oct 27) → ✅ practice run Wed Oct 28 → ✅ **Julie Oct 29** (very positive; asked for a sector index, see below) → round 2 labels Sat Oct 31 → TP2 report → submit **Fri Nov 6, 5 pm** → Julie follow-up on Nov 10, 13 or 19 (team to pick).
- **Julie's asks (Oct 29):** check whether a market-cap- and equal-weighted **sector index** on a defined public-company sample is feasible · dashboard hover definitions · hide partial years (FY2026) · sources we can legally get and verify only.
- **PoC companies:** JPMorgan Chase, Bank of America, Capital One, Wells Fargo, Charles Schwab, Principal Financial Group · **Period:** 2024–2026 · **Sources:** SEC 10-K/10-Q (74 filings, 277 AI passages), Dong baseline; earnings calls from **Bloomberg (CMU library) if cleared**, with transcript text kept out of the public repo; no LinkedIn job postings. **Citigroup** kept as a benchmark.
- **AI model:** DeepSeek (`deepseek-flash`), option B: one person pays (Shu), about $0.02 per run. Only public SEC text is sent. **Agent:** 7 tools.

## Key dates
| Date | What |
|---|---|
| ✅ Oct 18–25 | Team meetings Oct 18 and Oct 25 · SEC runs consolidated (#65) · categories approved (#64 + ENT = 1) · ethics memo (#63, #72) · eval plan v1.2 final · dashboard prototype |
| Mon Oct 26 | Yen-Chu checks Bloomberg at the CMU library |
| **Tue Oct 27** | **Labels submitted** (Logan, Yen-Chu, Snehal) · Shu freezes the categories and re-runs the agent · Snehal sends Julie the agenda |
| ✅ Wed Oct 28, 10 am | Practice run: ~27 min, pauses after each section, transition slides ([minutes](../meetings/2026-10-28-internal.md)) |
| ✅ Thu Oct 29, 10–11 am ET | Julie checkpoint ([minutes](../meetings/2026-10-29-client.md)) |
| Sat Oct 31 (afternoon) | Round 2 labels in (raters upload together) |
| Sun Nov 1 | Team meeting: Julie's feedback, sector-index feasibility, transcripts yes/no, round 1 + 2 disagreements → TP2 |
| Mon Nov 2 | Everyone's paragraph in the [TP2 outline](../docs/tp2/progress_report_draft.md) |
| Wed Nov 4 / Thu Nov 5 | TP2 draft (Mehul) / board clean-up |
| **Fri Nov 6, 5 pm** | Yen-Chu submits TP2 (Mehul is the backup) |
| Tue Nov 10, Fri Nov 13 or Thu Nov 19 | Julie follow-up (Nov 12 doesn't work for her; Snehal proposes one) |

## By person

### Mehul Pardeshi (PM + Responsible AI + Evaluation lead)
| Task | Due |
|---|---|
| ✅ Eval plan v1.2 final · labeling kit · red-team set v0 · TP2 outline · Julie talking points · Dong brief · Oct 23 repo check · merged #63–#65, #69–#72 | Done Oct 18–23 |
| ✅ Labels collected (#79, #82, Logan's workbook converted); #66 and #68 merged; check 2 run: use/no-use κ 0.60–0.72 (meets bar), evidence-level Fleiss κ 0.27 (below bar; [results](../docs/part3-metrics/labeling_round_1/results_round1.md)) | Done Oct 27 |
| ✅ Check 3 (Shu, #85): on the 29 passages outside the tuning set, 96% exact, κ 0.94, overclaim 0% (5% without the guardrail) | Done Oct 27 |
| ✅ Round 1 lessons + round 2 built: cheat sheet v2 (matches the frozen codebook, practice set), 30-passage targeted sample, workbook; scripts take `--round 2` | Done Oct 27 |
| ✅ Asked the raters for round 2 at the practice run (due Sat Oct 31) · Tell the raters which rule was unclear: the "about AI" N/X rule, not the use question (Logan asked) | Before Sat Oct 31 |
| Score round 2 with `python3 -m src.eval.irr --round 2`; lead adjudication at the Nov 1 meeting | Sat Oct 31 → Sun Nov 1 |
| ✅ Check 4 first run ([results](../docs/part3-metrics/check4_results.md)): ranking robust to weights; strict-only scores all 6 firms 0 from filings; Dong tracks talk (ρ 0.78) not use (0.14) · ✅ guardrail set reviewed against the frozen codebook (22 cases) | Done Oct 27 |
| Prepare the search-recall sheet (check 1) for Mehul to hand-check (~100 paragraphs, ~1 hour); rerun check 4 on the consensus labels after adjudication | Nov 1–3 |
| ✅ Presented "how we check results" and Logan's data rules (Logan absent) to Julie | Done Oct 29 |
| Give Snehal the points for the follow-up email: the strict-vs-broad question (not asked in the meeting) and the "all annual" correction (scores combine 10-K and 10-Q passages) | Fri Oct 30 |
| First guardrail with/without run, with Shu (#77) | ~Nov 3 |
| TP2: combine the paragraphs by Wed Nov 4; board clean-up Thu Nov 5; backup submitter | Nov 4–6 |

### Yen-Chu Chen (Dataset Builder)
| Task | Due |
|---|---|
| ✅ Category review (#33) · transcript source list (#62) | Done Oct 20–23 |
| ✅ #62 revised per Logan's 5 points (source-review table, 7 firms × 8 quarters; Motley Fool not cleared; Capital One, Wells Fargo and Schwab IR sites have no transcripts) | Done Oct 24 |
| **Earnings calls:** check Bloomberg at the CMU library (option E in #62); add Bloomberg rows to the review table. Before downloading, record Bloomberg's terms in the #62 source-review table (separate decisions for access, local storage, team-drive sharing, publication). **No transcript text in the public repo**; derived labels and scores are fine. If Bloomberg isn't usable, go without transcripts | **Mon Oct 26** |
| Rule on the 3 Capital One sentences, so Shu can freeze the categories | **Tue Oct 27** |
| **Labeling round 1:** label 50 passages on your own (your own judgment, not AI suggestions) | **Tue Oct 27** |
| ✅ Presented the test-run findings to Julie | Done Oct 29 |
| **Labeling round 2:** 30 passages, on your own ([materials](../docs/part3-metrics/labeling_round_2/)); upload with the others | **Sat Oct 31 (afternoon)** |
| **Submit TP2 on Canvas** | **Fri Nov 6, 5 pm** |

### Logan Mai (Market & User Researcher / BA)
| Task | Due |
|---|---|
| ✅ Ethics memo (#63) + DeepSeek retention review (#72) · #62 review · AI-tracker comparison · job-postings question answered (avoid LinkedIn) | Done Oct 22–25 |
| Post on #62 whether Bloomberg is approved, with its license terms | Before Yen-Chu downloads |
| DeepSeek: Dr. Chung said in person after class (Oct 27) that it's OK, since CMU hasn't banned it. Logan asked her to confirm by email; record the email in ethics memo §6 when it arrives | Email pending |
| CMU library (Ryan Splenda) emailed Oct 27 about the Bloomberg uses (download, team Drive, external AI, publishing); Bloomberg full text paused until he replies | Waiting on reply |
| ✅ Labeling round 1 (converted to `rater_logan.csv`) | Done Oct 27 |
| ✅ Practice run (~3½ min). Absent from the Julie meeting; Mehul presented the data rules | Done Oct 29 |
| Bloomberg: Julie asked us to confirm with the librarian that the manual terminal downloads are allowed; share his reply on #62 | Waiting on reply |
| Labeling round 2 (30 passages): `UNCLEAR:` not heard agreeing at the practice run | Sat Oct 31 (afternoon) |

### Shu Pu (AI Engineer / Solution Architect)
| Task | Due |
|---|---|
| ✅ SEC runs consolidated (#65) · categories (#64) · first DeepSeek run (#66) + prompt tuning (#68) | Done Oct 22–23 |
| ✅ Confirmed in #66: official endpoint, public SEC text only (about 600 calls, about $0.21) · agreement numbers labeled "tuning-set (in-sample)" (#66, #68) | Done Oct 25 |
| Remove the DeepSeek key from the how-to Google Doc and rotate it (not yet confirmed) | **ASAP** |
| ✅ Categories frozen (#33): ENT = 1 point is the scorer's default, taxonomy doc marked frozen, Capital One risk-factor sentences = D1 (default; Yen-Chu can reopen). Scores recomputed | Done Tue Oct 27 |
| Re-run the agent on the 110 tuning passages with prompt classify-v1.5 (the #64 codebook text changed the prompt; see #85), so the dashboard scores and check 3 use the same prompt | Wed Oct 28 |
| After the raters submit: run the agent on the 50-passage sample (check 3); give Snehal the scores file | Tue Oct 27 → Wed Oct 28 |
| **Agent runs end to end** on the six FY2025 10-Ks (TP2: 12 pts) | **Wed Oct 28** |
| Create the shared slide deck (Drive → Client materials → progress folder) | Wed Oct 28 |
| Cost note for Julie's handover (per run; one-time credit of about $10–20; no API key included) | `UNCLEAR:` before the next Julie meeting |
| ✅ Presented the categories + agent demo to Julie | Done Oct 29 |

### Snehal Paliwal (Dashboard PM + client communication)
| Task | Due |
|---|---|
| ✅ Dashboard prototype (Streamlit, fictional mock data) shown Oct 25 and merged (#73: overview → use-case cards → firm comparison, 14 tests) · AI-tracker comparison | Done Oct 25 |
| Record the prototype and upload it to the Drive | `UNCLEAR:` soon |
| ✅ First dashboard view with PoC data: SEC pilot scores tab (#93, merged Oct 28; 40 tests pass) | Done Oct 28 |
| Fix the data-transparency tab (timed out in the practice run) · transition slides + final deck order | **Before Thu Oct 29** |
| Add a dataset-level summary page. Keep **mock data until you've submitted your labels**; use Shu's real scores file afterwards | Before Thu Oct 29 |
| **Labeling round 1:** label 50 passages on your own with the [Excel workbook](../docs/part3-metrics/labeling_round_1/labeling_workbook.xlsx) | **Tue Oct 27** |
| Formal agenda to Julie | **Tue Oct 27** |
| Send the practice-run invite (Wed Oct 28, 10 am, virtual) | Before Wed |
| ✅ Hosted the Julie meeting and showed the dashboard | Done Oct 29 |
| Thank-you email to Julie + propose the follow-up date (Tue Nov 10, Fri Nov 13 or Thu Nov 19) after checking the team's schedules | `UNCLEAR:` no date set (suggest Fri Oct 30) |
| Dashboard (Julie's feedback): hover definitions for each metric; hide FY2026 / partial years until complete | Before the follow-up |
| **Labeling round 2:** 30 passages, on your own; upload with the others | **Sat Oct 31 (afternoon)** |
| Hosting choice (Streamlit Community Cloud vs. Vercel) | `UNCLEAR:` after Julie's feedback |

### Everyone
- Raters (Logan, Yen-Chu, Snehal): **your own judgment on every label** (AI is fine for finding files, not for picking labels); **submit on Tue Oct 27, not earlier**
- Add your slides to the shared deck; bring more questions for Julie: **Wed Oct 28** (practice run 10 am)
- Julie meeting **Thu Oct 29, 10 am**
- Your paragraph in the [TP2 outline](../docs/tp2/progress_report_draft.md): **Mon Nov 2**
- Julie follow-up: tell Snehal which of Tue Nov 10, Fri Nov 13 or Thu Nov 19 work for you
- Sector-index feasibility (Julie's ask): `UNCLEAR:` owner; discuss Sun Nov 1 (sample from a sector index or SIC codes, market-cap data, agent cost at scale)
- Finish your pending TP2 work this weekend (Mehul's ask)

## Deliverable owners (whole project)
| Deliverable | Owner | Support |
|---|---|---|
| Ethics / legal sourcing memo (10%) | Logan | All |
| Taxonomy derivation (20% with IRR) | Yen-Chu, Shu | All |
| IRR raters | All (design: Mehul) | All |
| Metrics methodology write-up (20%) | All | All |
| Index construction + methodology appendix | Mehul, Snehal | All |
| Final presentation / poster | Snehal | All |
| Evaluation & validation design | Mehul | — |
| Research paper (TP3) | TBD; Julie to provide candidates | — |

## Progress since Oct 4 (seen in the repo)
- **Yen-Chu, PR #43 (✅ merged Oct 18 as a DRAFT):** SEC test run. #27 and #32 closed; #33 stays open until Shu reviews it and the team agrees.
  - 56 filings, Q3 2024–Q2 2026, for the 6 PoC companies, **plus Citigroup as an extra comparison**.
  - 245 AI passages, of which only 32 (13%) describe actual AI use.
  - **DRAFT** Taxonomy v0 codebook and **DRAFT** scoring.
  - Open questions for tonight: keep or drop Citigroup; were the draft labels set by hand or AI-assisted (matters for the IRR round); is verbatim SEC text OK under the ethics memo (Logan).

## Unowned / open
- Julie's paper: ✅ received (Vanguard report; see `docs/references.md`). Links to her other papers have been requested.
- **Dashboard:** `src/dashboard/` now has the SEC pilot scores tab (#93: preliminary, AI-assisted v0 scores from `company_scores_v0.csv`) alongside the fictional mock-up tabs. Hosting is still open.
- Snehal asked Julie (Oct 10) whether rescoping away from Dr. Chung's original brief is OK; the answer isn't recorded yet.

## Completed
- ✅ Team contract signed (9/20–9/24), section 4 filled in before TP1
- ✅ Repo, kanban board, shared tracker; all members invited (9/27–9/28)
- ✅ Roles approved (10/1); kickoff meeting with Julie (10/1)
- ✅ TP1 submitted (10/2): contract, prep doc, scope v1.0
- ✅ Oct 4 meeting: PoC companies, period, sources, timeline and dates decided
- ✅ Oct 18 meeting: data, taxonomy proposals, model (DeepSeek), agent plan, dashboard plan
- ✅ Oct 25 meeting: categories approved (ENT = 1 point), DeepSeek option B, Bloomberg transcripts if cleared, Julie plan, practice run Wed Oct 28
- ✅ Oct 28 practice run: ~27 min; pauses after each section; transition slides; round 2 Sat Oct 31
- ✅ Oct 29 Julie checkpoint: very positive; asked for a sector index (market-cap- and equal-weighted); dashboard hover definitions; hide partial years; follow-up Nov 10/13/19
