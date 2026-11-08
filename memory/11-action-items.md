# 11 — Action Items (who is doing what, right now)

> **Read this to answer "what should I work on next?"** Updated after every meeting from `meetings/` minutes ([procedure](../meetings/README.md)). The shared spreadsheet remains the source of truth for owners and deadlines; this file mirrors it for AI tools.
> **Last updated:** 2026-11-08 (Julie confirmed Tue Nov 10, 7 pm; agreed labels done Sat Nov 7, file not yet shared; team call Sun Nov 8, 8 pm; see the Nov 8 decisions-log entries. Earlier: TP2 deadline moved to Fri Nov 13; earlier: round 2 scored; TP2 paragraphs, agent re-run and Bloomberg review merged; no Nov 1 meeting record in `meetings/`). Last meeting: [Oct 29 client checkpoint](../meetings/2026-10-29-client.md) (transcript). Previous: [Oct 28 practice run](../meetings/2026-10-28-internal.md).
> **Pinned summary for humans:** [#45 "Who does what"](https://github.com/MehulPardeshi/ai-adoption-index/issues/45), with @mentions per person.
> **GitHub:** each task below is an issue in the **"Sprint: Oct 18–Nov 13 (TP2)"** milestone (renamed Nov 8; was "Oct 18–Nov 6") on the [project board](https://github.com/users/MehulPardeshi/projects/1).

## Where we are
- ✅ TP1 submitted (Fri Oct 2).
- 🏁 **Sprint: Sun Oct 18 → Fri Nov 13 (TP2; extended from Nov 6).** ✅ Categories frozen, round 1 labels in, checks 2–4 run (Oct 27) → ✅ practice run Wed Oct 28 → ✅ **Julie Oct 29** (very positive; asked for a sector index, see below) → ✅ round 2 labels and scoring (Nov 4) → ✅ agreed labels (Sat Nov 7) → team call **Sun Nov 8, 8 pm** → **Julie follow-up Tue Nov 10, 7 pm (confirmed;** [prep](../docs/tp2/julie_nov10_prep.md)**)** → TP2 compile Thu Nov 12 → submit **Fri Nov 13, 5 pm**.
- **Julie's asks (Oct 29):** check whether a market-cap- and equal-weighted **sector index** on a defined public-company sample is feasible · dashboard hover definitions · hide partial years (FY2026) · sources we can legally get and verify only.
- **PoC companies:** JPMorgan Chase, Bank of America, Capital One, Wells Fargo, Charles Schwab, Principal Financial Group · **Period:** 2024–2026 · **Sources:** SEC 10-K/10-Q (74 filings, 277 AI passages), Dong baseline; earnings calls from **Bloomberg (CMU library): permission cleared Nov 4 (#62), inclusion in the index not decided**, with transcript text kept out of the public repo and dashboard; no LinkedIn job postings. **Citigroup** kept as a benchmark.
- **AI model:** DeepSeek (`deepseek-flash`), option B: one person pays (Shu), about $0.02 per run. Only public SEC text is sent. **Agent:** 7 tools.

## Key dates
| Date | What |
|---|---|
| ✅ Oct 18–25 | Team meetings Oct 18 and Oct 25 · SEC runs consolidated (#65) · categories approved (#64 + ENT = 1) · ethics memo (#63, #72) · eval plan v1.2 final · dashboard prototype |
| ✅ Oct 26–27 | Bloomberg transcripts collected (team-only) · round 1 labels in · categories frozen (#84) · checks 2–4 run · agenda sent |
| ✅ Wed Oct 28, 10 am | Practice run: ~27 min, pauses after each section, transition slides ([minutes](../meetings/2026-10-28-internal.md)) |
| ✅ Thu Oct 29, 10–11 am ET | Julie checkpoint ([minutes](../meetings/2026-10-29-client.md)) |
| ✅ Wed Nov 4 | Round 2 labels all in and scored: Fleiss κ 0.32 ([results](../docs/part3-metrics/labeling_round_2/results_round2.md)) |
| Sun Nov 1 | `UNCLEAR:` team meeting: no minutes in the repo. Open items from its agenda (sector-index feasibility, transcripts yes/no, disagreements) still need an answer |
| ✅ Wed Nov 4 | TP2 paragraphs merged: Shu (#109), Snehal's dashboard (#112), Logan (#114), Yen-Chu (#105). Section 6 (client meeting) still needs Snehal's confirmation |
| ~~Thu Nov 5~~ **Thu Nov 12** | TP2 draft combined + board snapshot (Mehul); includes the Nov 10 Julie follow-up, the adjudicated labels and the check 4 rerun if they land |
| ~~Fri Nov 6, 5 pm~~ **Fri Nov 13, 5 pm** | Yen-Chu submits TP2 (Mehul is the backup). Deadline change per the instructor in class (Mehul, Snehal); not in the syllabus file. Check Canvas once the submission opens |
| ✅ Sat Nov 7, 5 pm | Check-in (Logan, Snehal, Yen-Chu); they agreed the labels for the 58 disagreements (per Snehal, Nov 8). The filled sheet isn't shared yet |
| **Sun Nov 8, 8–9 pm** | Team call on Zoom (Snehal): Julie prep, transcripts and weighting decisions, TP2 owners ([prep](../docs/tp2/julie_nov10_prep.md)) |
| **Tue Nov 10, 7–8 pm ET** | **Julie follow-up, confirmed** (Julie accepted Snehal's calendar invite; Dr. Chung also accepted). This is the TP2 client meeting (#98) |

## By person

### Mehul Pardeshi (PM + Responsible AI + Evaluation lead)
| Task | Due |
|---|---|
| ✅ Eval plan v1.2 final · labeling kit · red-team set v0 · TP2 outline · Julie talking points · Dong brief · Oct 23 repo check · merged #63–#65, #69–#72 | Done Oct 18–23 |
| ✅ Labels collected (#79, #82, Logan's workbook converted); #66 and #68 merged; check 2 run: use/no-use κ 0.60–0.72 (meets bar), evidence-level Fleiss κ 0.27 (below bar; [results](../docs/part3-metrics/labeling_round_1/results_round1.md)) | Done Oct 27 |
| ✅ Check 3 (Shu, #85): on the 29 passages outside the tuning set, 96% exact, κ 0.94, overclaim 0% (5% without the guardrail) | Done Oct 27 |
| ✅ Round 1 lessons + round 2 built: cheat sheet v2 (matches the frozen codebook, practice set), 30-passage targeted sample, workbook; scripts take `--round 2` | Done Oct 27 |
| ✅ Round 2 issue (#95) explains the unclear rule (the "about AI" N/X rule, not the use question) | Done Oct 28 |
| ✅ #95 Round 2 merged and scored; Logan's Numbers file converted · Adjudication: ✅ agreed labels merged (#124, Yen-Chu); 80-passage consensus set built. 9 scenarios still to fill (raters) | Done Nov 4 / Nov 8–9 |
| ✅ Check 4 first run ([results](../docs/part3-metrics/check4_results.md)): ranking robust to weights; strict-only scores all 6 firms 0 from filings; Dong tracks talk (ρ 0.78) not use (0.14) · ✅ guardrail set reviewed against the frozen codebook (22 cases) | Done Oct 27 |
| ✅ Check 1 done and confirmed (precision 98.9%, no clear recall miss; [results](../docs/part3-metrics/check1/results.md)) · ✅ check 5 dry run matched · ✅ check 6 replay · ✅ TP2 sections drafted | Done Nov 3 |
| ✅ #101 Check 4 rerun on the human consensus labels ([results](../docs/part3-metrics/check4_results.md)): Capital One and Principal rise to 18, ranking robust (ρ 0.94–0.99), drafts understated use (18 of 80). Rerun once the raters add the 9 missing scenarios | Done Nov 8 |
| #102 Check 5: get Logan or Snehal to run the [steps](../docs/part3-metrics/check5_rerun.md) (~20 min) | Mon Nov 9 |
| ✅ Presented "how we check results" and Logan's data rules (Logan absent) to Julie | Done Oct 29 |
| ✅ Follow-up-email points for Snehal (strict-vs-broad question; scores combine 10-K + 10-Q) are in #98 | Done Oct 29 |
| ✅ #77 Live 22-case guardrail run (Shu, #117) scored ([results](../docs/part3-metrics/check6_results.md)): 0/18 unsafe with the guardrail, 2/18 without; 0/4 false blocks | Done Nov 5 |
| #39 / #40 TP2: combine the paragraphs and take the board snapshot; backup submitter | Nov 12–13 |
| TP2 sections 1, 3, 4, 7 updated through round 2; check the drafts and remove the markers at compile | Thu Nov 12 |

### Yen-Chu Chen (Dataset Builder)
| Task | Due |
|---|---|
| ✅ Category review (#33) · transcript source list (#62) | Done Oct 20–23 |
| ✅ #62 revised per Logan's 5 points (source-review table, 7 firms × 8 quarters; Motley Fool not cleared; Capital One, Wells Fargo and Schwab IR sites have no transcripts) | Done Oct 24 |
| ✅ Bloomberg transcripts collected (team Drive only) + Bloomberg rows in #62 · labels round 1 (#82) · Capital One sentences set to D1 by default in #84 (reopen #33 if you disagree) | Done Oct 26–27 |
| Keep the transcripts in CMU-only storage (no public text). Bloomberg cleared Nov 4 (#62); #34 waits for the team's decision on the index | Team decision |
| ✅ #97 Sector index: S&P 500 Financials, ~75 firms, public float from 10-K cover pages via SEC's API · Offered next: test the pull on our 7 firms, save the dated list | Done Nov 4 |
| ✅ Presented the test-run findings to Julie | Done Oct 29 |
| ✅ Labeling round 2 (#104, merged Nov 4) · ✅ TP2 blocker (#105) | Done Nov 3–4 |
| **Submit TP2 on Canvas** | **Fri Nov 13, 5 pm** |

### Logan Mai (Market & User Researcher / BA)
| Task | Due |
|---|---|
| ✅ Ethics memo (#63) + DeepSeek retention review (#72) · #62 review · AI-tracker comparison · job-postings question answered (avoid LinkedIn) | Done Oct 22–25 |
| DeepSeek: Dr. Chung said in person after class (Oct 27) that it's OK, since CMU hasn't banned it. Logan asked her to confirm by email; record the email in ethics memo §6 when it arrives | Email pending |
| ✅ CMU library confirmed with Bloomberg; 56 records and the ethics memo updated (#62) | Done Nov 4 |
| ✅ Labeling round 1 (converted to `rater_logan.csv`) | Done Oct 27 |
| ✅ Practice run (~3½ min). Absent from the Julie meeting; Mehul presented the data rules | Done Oct 29 |
| ✅ Labeling round 2 (converted to `rater_logan.csv`; please check it) · ✅ TP2 ethics paragraph (#114) | Done Nov 4 |

### Shu Pu (AI Engineer / Solution Architect)
| Task | Due |
|---|---|
| ✅ SEC runs consolidated (#65) · categories (#64) · first DeepSeek run (#66) + prompt tuning (#68) | Done Oct 22–23 |
| ✅ Confirmed in #66: official endpoint, public SEC text only (about 600 calls, about $0.21) · agreement numbers labeled "tuning-set (in-sample)" (#66, #68) | Done Oct 25 |
| Remove the DeepSeek key from the how-to Google Doc and rotate it (not yet confirmed) | **ASAP** |
| ✅ Categories frozen (#33): ENT = 1 point is the scorer's default, taxonomy doc marked frozen, Capital One risk-factor sentences = D1 (default; Yen-Chu can reopen). Scores recomputed | Done Tue Oct 27 |
| ✅ Re-ran the 110 passages with classify-v1.5, timed (#110; no FY2025 AI Use Score moved) | Done Nov 4 |
| ✅ Check 3 on the 50-passage sample (#85) · shared slide deck | Done Oct 27–28 |
| ✅ #35 Agent runs end to end (#66, #68, #84, #110) · ✅ TP2 section 2 (#109) | Done Nov 4 |
| After TP2: run the agent on the 30 round 2 passages for check 3 (command in the [results](../docs/part3-metrics/labeling_round_2/results_round2.md)) | Mon Nov 9 |
| ✅ #97 Sector index: ~73 min and ~$0.40 for one year on ~75 firms; 3–5% go to human review | Done Nov 4 |
| Cost note for Julie's handover (per run; one-time credit of about $10–20; no API key included) | `UNCLEAR:` before the next Julie meeting |
| ✅ Presented the categories + agent demo to Julie | Done Oct 29 |

### Snehal Paliwal (Dashboard PM + client communication)
| Task | Due |
|---|---|
| ✅ Dashboard prototype (Streamlit, fictional mock data) shown Oct 25 and merged (#73: overview → use-case cards → firm comparison, 14 tests) · AI-tracker comparison | Done Oct 25 |
| Record the prototype and upload it to the Drive | `UNCLEAR:` soon |
| ✅ First dashboard view with PoC data: SEC pilot scores tab (#93, merged Oct 28; 40 tests pass) | Done Oct 28 |
| ✅ Labels round 1 (#79) · agenda to Julie · practice-run invite · transition slides · dataset summary metrics on the SEC tab (#93) | Done Oct 27–29 |
| ✅ Hosted the Julie meeting and showed the dashboard | Done Oct 29 |
| ✅ #98 Julie follow-up set: Tue Nov 10, 7–8 pm, Zoom; Julie and Dr. Chung accepted. Her Nov 2 email questions (10-K vs. 10-Q on the dashboard; use cases next to scores) are unanswered, so ask them on Tuesday | Done Nov 4–8 |
| Send Julie the agenda for Tuesday ([draft](../docs/tp2/julie_nov10_prep.md)) | Mon Nov 9 |
| TP2 section 6 (client meeting): confirm or replace the draft (can now cover the Nov 10 follow-up too) · ✅ dashboard paragraph (#112) · ✅ labels (#111) | Wed Nov 11 |
| #96 Dashboard (Julie's feedback): hover definitions for each metric; hide FY2026 / partial years; check the transparency tab loads | Mon Nov 9 |
| #30 Hosting choice (Streamlit Community Cloud vs. Vercel; TP3 needs a hosted app) | Fri Nov 13 |

### Everyone
- ✅ Raters: agreed labels for the round 1 and 2 disagreements (Sat Nov 7; merged #124). Still to do: scenarios for the 9 passages listed in the [adjudication README](../docs/part3-metrics/adjudication/README.md)
- Team decisions still open (Sun Nov 8 call, before Julie): transcripts in the index or not; market-cap or equal weighting as the headline
- Julie follow-up Tue Nov 10, 7 pm: agenda and presenters on the Sun Nov 8 call ([prep](../docs/tp2/julie_nov10_prep.md))

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
- ✅ Rescoping: on Oct 29 Julie said the way we came back with the scope and changes was "just perfect" (resolves the Oct 10 question).

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
