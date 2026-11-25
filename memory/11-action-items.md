# 11 — Action Items (who is doing what, right now)

> **Read this to answer "what should I work on next?"** Updated after every meeting from `meetings/` minutes ([procedure](../meetings/README.md)). The shared spreadsheet remains the source of truth for owners and deadlines; this file mirrors it for AI tools.
> **Last updated:** 2026-11-24 afternoon (Julie on Snehal's email: "Your group has done an excellent job. Why don't you decide what you prefer"; Snehal proposes a live Zoom with Julie **Thu Dec 3, 10 am** (handover meeting), group to confirm. Earlier Nov 24: Mehul's Nov 29 drafts merged (#193): final README skeleton with owners, poster panel text, Responsible AI v0.5, How we worked v0.3. **Sun Nov 29 meeting has no time or invite yet** (not on Mehul's calendar). Earlier Nov 24: **TP3 final sprint plan below: read "🎯 Now" first.** Dr. Chung's takeaways filed ([minutes](../meetings/2026-11-23-advisor.md)); new #190 final-product repo + add Dr. Chung, #191 Julie's walkthrough + invite Dr. Chung; both team meetings happen: Sun Nov 29 and Tue Dec 1 in person (Snehal). Earlier Nov 23 evening: Dr. Chung via Snehal: **Dec 3 is a walk-around poster session in the rotunda**, so Julie can't simply join a talk remotely; open: a separate Zoom session with Julie and/or a recorded walkthrough, Snehal to ask Julie · TA's TP2 feedback only mentioned another team covering retirement providers and broker deals; team agreed not to add sectors 10 days out. Earlier Nov 23: ✅ Julie approved keeping the 10-Qs, replying to Snehal's email: "really good justification"; ✅ 76-firm sector index merged (#187, Yen-Chu): FY2025 8.6 EW / 10.2 CW, 76 firms, Ares float kept as Shu's estimate; ✅ Snehal met Dr. Chung Mon Nov 23 (handoff, poster, research inclusion; suggested Evident AI as related work), notes in the team Drive, key points to go on #143; Snehal booked **in-person final poster prep + run-through Tue Dec 1, 10–11 am**. Earlier Nov 22 night: round 3: Snehal is the second rater, settle Tue Nov 24; team meeting Sun Nov 29 = Dec 3 run-through. Earlier Nov 22: ✅ #170 review merged: 195 of 200, index 7.2 → 8.6 EW; 5 rows wait for round 3; Snehal: Dr. Chung meeting moved to Mon Nov 23, will email Julie about the 10-Qs and add the scoring method to the dashboard. Earlier Nov 21 evening: ✅ dashboard live at https://ai-adoption-index.streamlit.app, deployed by Mehul (#178 import fix, #180 light theme; #30 closed); ✅ Snehal's CSV downloads merged (#179, #155 closed); ✅ Shu's 10-Q rerun merged (#176): 606 filings, 2,353 passages, 200 held, draft FY2025 index 7.2 EW / 9.4 CW; #157 closed, still tell Julie; #170 split: Shu exchanges + payments (108 rows), Yen-Chu asset managers/brokers, insurers, banks (92). Earlier Nov 21: team kept the 10-Qs, Nov 19 group chat. Earlier Nov 19: no teammate pushes since Nov 17; Mehul's review step, SKILL.md v0.2 and Responsible AI v0.2 added. Earlier Nov 17: TP2 submission confirmed; all open TP3 issues assigned on GitHub with target dates, see #45; 76-firm S&P 500 Financials run merged (#168, #133 closed): 152 10-Ks, 1,876 passages, 170 held for a person, draft index FY2025 6.5 EW / 8.6 CW; 10-Q finding for #157 (Citi 53 → 9 without 10-Qs); new #169 round 3 pilot and #170 held-label review, owners to agree; TP2 submission not yet confirmed on #41. Earlier: TP2 final PDF ready for Yen-Chu to submit Fri Nov 13, 5 pm. Earlier: Nov 10 Julie follow-up filed: broad headline agreed, category detail enough, 10-K-only check, download button + method page, handover via Dr. Chung, Julie joins Dec 3 remotely. Earlier: Nov 8 team call filed: transcripts out, both index weightings, Tuesday plan; 7 of 9 scenarios added (#128) and check 4 updated (#129). Earlier: Julie confirmed Tue Nov 10, 7 pm; agreed labels done Sat Nov 7. Earlier: TP2 deadline moved to Fri Nov 13; earlier: round 2 scored; TP2 paragraphs, agent re-run and Bloomberg review merged; no Nov 1 meeting record in `meetings/`). Last meeting: [Nov 10 Julie follow-up](../meetings/2026-11-10-client.md) (transcript). Previous: [Nov 8 team call](../meetings/2026-11-08-internal.md), [Oct 29 client checkpoint](../meetings/2026-10-29-client.md).
> **Pinned summary for humans:** [#45 "Who does what"](https://github.com/MehulPardeshi/ai-adoption-index/issues/45), with @mentions per person.
> **GitHub:** each task below is an issue in the **"Sprint: Oct 18–Nov 13 (TP2)"** milestone (renamed Nov 8; was "Oct 18–Nov 6") on the [project board](https://github.com/users/MehulPardeshi/projects/1).

## Where we are
- ✅ TP1 submitted (Fri Oct 2). ✅ TP2 submitted (Fri Nov 13; confirmation received, #41 closed).
- 🏁 **TP3 (Nov 14 → Thu Dec 3, 5:00–6:20 pm):** ✅ 76-firm run (#168) → held-label review (#170) + round 3 pilot (#169) → full sector index (#134) → dashboard, hosting, README report, paper, poster, demo, handover.
- 🏁 **Sprint: Sun Oct 18 → Fri Nov 13 (TP2; extended from Nov 6).** ✅ Categories frozen, round 1 labels in, checks 2–4 run (Oct 27) → ✅ practice run Wed Oct 28 → ✅ **Julie Oct 29** (very positive; asked for a sector index, see below) → ✅ round 2 labels and scoring (Nov 4) → ✅ agreed labels (Sat Nov 7) → ✅ team call Sun Nov 8 ([minutes](../meetings/2026-11-08-internal.md)) → ✅ **Julie follow-up Tue Nov 10** ([minutes](../meetings/2026-11-10-client.md)) → TP2 compile Thu Nov 12 → submit **Fri Nov 13, 5 pm**.
- **Julie's answers (Nov 10):** broad headline with strict beside it · category codes are enough (no extra use-case detail) · check what 10-Qs add, then likely 10-K only · add a data download and the scoring method to the dashboard · handover per Dr. Chung's preference (at least a deployed link + user guide) · she joins Dec 3 remotely.
- **Julie's asks (Oct 29):** check whether a market-cap- and equal-weighted **sector index** on a defined public-company sample is feasible · dashboard hover definitions · hide partial years (FY2026) · sources we can legally get and verify only.
- **PoC companies:** JPMorgan Chase, Bank of America, Capital One, Wells Fargo, Charles Schwab, Principal Financial Group · **Period:** 2024–2026 · **Sources:** SEC 10-K/10-Q (74 filings, 277 AI passages), Dong baseline; earnings calls from **Bloomberg (CMU library): permission cleared Nov 4 (#62); left out of the index (team, Nov 8), future work**, with transcript text kept out of the public repo and dashboard; no LinkedIn job postings. **Citigroup** kept as a benchmark.
- **AI model:** DeepSeek (`deepseek-flash`), option B: one person pays (Shu), about $0.02 per run. Only public SEC text is sent. **Agent:** 7 tools.

## 🎯 Now: TP3 final sprint (Tue Nov 24 → Thu Dec 3)

**If you're a teammate's AI tool: find your person below, do their unchecked items in order, and post progress on the issue.** Everything else in this file is history and context.

**Next milestone: Sun Nov 29 team meeting = first full draft.** Every TP3 piece exists as a draft by then, so Tue Dec 1 (in person, 10–11 am) is only for making the poster together and a run-through. Then **Thu Dec 3, 5:00–6:20 pm: walk-around poster session in the rotunda**; Julie gets a separate Zoom or a recording (#191).

**What Dr. Chung expects (Nov 23, [minutes](../meetings/2026-11-23-advisor.md)):** a short research section, not a paper (link, abstract, a few talking points, how we build on it: manual → agentic); a small research panel on the poster; a creative, visual poster; handoff = Streamlit link + GitHub repo + user guide; Dr. Chung added to GitHub; a separate public repo with only the final product.

**Done for TP3 so far:** 76-firm run with 10-Qs (#168, #176) · held-label review 195/200 (#170) · 76-firm index merged, FY2025 8.6 EW / 10.2 CW (#187) · dashboard live with CSV downloads (#30, #155) · 10-Q check, Julie approved (#157) · Dr. Chung met (#143) · drafts: SKILL.md v0.3, Evaluation v0.3, Responsible AI v0.4, How we worked v0.2.

### Yen-Chu (@teddy0-0y)
- [ ] #134 Put the 76-firm index on the dashboard as the headline sector index (keep the 6-firm pilot as a second view) · **Sun Nov 29**
- [ ] #156 Scoring-method text on the dashboard (levels, 11 areas, highest level per area once a year, ÷33×100, EW/CW) · **Sun Nov 29**
- [ ] #170 Fill your 2 round 3 rows (NTRS, TROW) once #169 is settled, then rerun `apply_review` + `sector_index` (#134) · **Fri Nov 27**
- [ ] #166 README report: scope + project details sections · **Sun Nov 29** draft, final Tue Dec 1
- [ ] Your bio + GitHub link in the README (#166)

### Snehal (@snehalpaliwal)
- [x] #169 Independently label the 40 round 3 passages; uploaded as [rater_snehal.csv](../docs/part3-metrics/labeling_round_3/rater_snehal.csv)
- [ ] #169 Settle differences with Logan and create the agreed answer key; scheduled Tue Nov 24 after class (settlement not yet recorded)
- [x] #191 Emailed Julie (Nov 24); she left the choice to us · [ ] send Julie the Zoom for **Thu Dec 3, 10 am** once the group confirms · [ ] invite Dr. Chung to our poster · **Wed Nov 25**
- [ ] #141 Poster draft: layout + visuals; one panel per section (problem, method/agent, evaluation, results, research, responsible AI, what's next, QR to dashboard + repo) · **Sun Nov 29**; made together Tue Dec 1
- [ ] #142 User guide for Julie (`docs/user_guide.md`, with Shu): open the dashboard, read a score, download data, refresh with SKILL.md · **Sun Nov 29**
- [ ] #166 README visuals · **Sun Nov 29**
- [ ] Your bio + GitHub link in the README (#166)

### Logan (@MaiJialong)
- [ ] #169 Settle round 3 with Snehal **today, Tue Nov 24 after class**
- [ ] #137 Short research section (per Dr. Chung): Babina et al. 2024 link + abstract + 3–4 talking points (motivation; method vs ours; manual → agentic; what we add) + 1–2 lines on Evident AI. Start from the draft in [paper_discussion_plan.md](../docs/tp3/paper_discussion_plan.md). Also the poster's research panel · **Sun Nov 29**
- [ ] #138 References list (Babina, Dong, Evident AI, SEC sources, tools) · **Sun Nov 29**
- [ ] #139 Data retention + attribution paragraph in [responsible_ai.md](../docs/tp3/responsible_ai.md) (from the ethics memo §§4–5) · **Sun Nov 29**
- [ ] Your bio + GitHub link in the README (#166)

### Shu (@seanpushu)
- [ ] #170 Fill your 3 round 3 rows (FDS, FISV, XYZ) once #169 is settled · **Fri Nov 27**
- [ ] #135 Review SKILL.md v0.3 (especially the run commands); small PR or comment · **Sun Nov 29**
- [ ] #137 2–3 lines comparing our method with Dong et al. 2026 · **Sun Nov 29**
- [ ] #190 Propose the file list for the public final-product repo · **Sun Nov 29**
- [ ] #142 User guide with Snehal: the refresh part · **Sun Nov 29**
- [ ] #140 Code demo (agent labels a passage → score → dashboard) + recorded backup; reuse for Julie (#191) · **Tue Dec 1**
- [ ] Your bio + GitHub link in the README (#166)

### Mehul (@MehulPardeshi)
- [ ] #169 After the settle: merge #185 + Snehal's file, score the agent per firm type (bar: overclaim ≤5%), fill round 3 numbers into Evaluation + Responsible AI · **Thu Nov 26**
- [ ] Decide with the round 3 results: does AI in a product sold to clients count as the firm's own use? (Visa = 7.8% of FY2025 float) · **Sun Nov 29**
- [ ] #139 Finish Responsible AI after Logan's part · **Sun Nov 29**
- [ ] #135 Finish SKILL.md after Shu's review · **Sun Nov 29**
- [ ] #137 Review Logan's research section · **Mon Nov 30**
- [ ] #190 Create the public final-product repo + add Dr. Chung (needs her GitHub username) · **Wed Dec 2**
- [x] #166 Final README skeleton with an owner per section ([final_readme_draft.md](../docs/tp3/final_readme_draft.md), Nov 24) · [ ] swap it into README + refresh numbers · **Tue Dec 1**
- [x] #141 Poster panel text for Evaluation, Responsible AI, How we worked, What's next ([poster_panels_mehul.md](../docs/tp3/poster_panels_mehul.md), Nov 24)
- [x] Your bio + GitHub link (in the README draft)

### Everyone
- **Sun Nov 29:** team meeting (`UNCLEAR:` time; proposed 8 pm on Zoom, like Nov 8), walk through all drafts. Rewrite your section of [final_readme_draft.md](../docs/tp3/final_readme_draft.md) before it. **Tue Dec 1, 10–11 am, in person:** build the poster + run-through (Snehal's invite). **Thu Dec 3, 5:00 pm:** stand by the poster; each person can explain any panel.
- Before you start: `git pull origin main`. Work on a branch, open a PR, post progress on the issue.

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
| ✅ Sun Nov 8, 8–8:45 pm | Team call ([minutes](../meetings/2026-11-08-internal.md)): transcripts out, both index weightings, Tuesday plan, TP2 owners confirmed, no practice run |
| ✅ Tue Nov 10, 7–8 pm ET | Julie follow-up, the TP2 client meeting (#98) ([minutes](../meetings/2026-11-10-client.md)): very positive; agreed broad headline, category detail; 10-K check; download + method page; handover via Dr. Chung |
| ✅ Mon Nov 23 | Snehal met Dr. Chung (#143, [minutes](../meetings/2026-11-23-advisor.md)): short research section, poster in the rotunda, handoff = Streamlit + repo + user guide, public final-product repo, Evident AI · Julie approved keeping the 10-Qs (email reply to Snehal) · 76-firm index merged (#187) |
| Tue Nov 24, after class | Round 3 (#169): Snehal labels alone, then she and Logan settle disagreements |
| **Sun Nov 29** | Team meeting: first full draft of every TP3 piece (Snehal confirmed Nov 23: both meetings happen) |
| **Tue Dec 1, 10–11 am, in person** | Final poster prep + run-through (Snehal's invite; all 5). Deck (#141), demo (#140) and README report (#166) drafts needed before |
| Thu Dec 3, 10 am (proposed) | Zoom with Julie: poster walkthrough + live dashboard + handover (#191, #142). Recording as backup |
| **Thu Dec 3, 5:00–6:20 pm ET** | **Final presentation: walk-around poster session in the rotunda** (per Dr. Chung, Nov 23). Julie: separate Zoom (Dec 2–4) or a recording (#191, Snehal asks by Wed Nov 25) |

## By person

### Mehul Pardeshi (PM + Responsible AI + Evaluation lead)
| Task | Due |
|---|---|
| ✅ Eval plan v1.2 final · labeling kit · red-team set v0 · TP2 outline · Julie talking points · Dong brief · Oct 23 repo check · merged #63–#65, #69–#72 | Done Oct 18–23 |
| ✅ Labels collected (#79, #82, Logan's workbook converted); #66 and #68 merged; check 2 run: use/no-use κ 0.60–0.72 (meets bar), evidence-level Fleiss κ 0.27 (below bar; [results](../docs/part3-metrics/labeling_round_1/results_round1.md)) | Done Oct 27 |
| ✅ Check 3 (Shu, #85): on the 29 passages outside the tuning set, 96% exact vs. the human majority, κ 0.94, overclaim 0% (5% without the guardrail) | Done Oct 27 |
| ✅ Check 3 on the **agreed labels**, rounds 1+2 (Shu, #147): 48 unseen passages, 81% exact (κ 0.73), 85% use vs. no use, 0 overclaims, 7 cautious misses (3 already held by the guardrail → 90%); round 2 alone 74%. Replaces 96% in TP2, the slides (now 18–19) and the Responsible AI section | Done Nov 9 |
| ✅ Round 1 lessons + round 2 built: cheat sheet v2 (matches the frozen codebook, practice set), 30-passage targeted sample, workbook; scripts take `--round 2` | Done Oct 27 |
| ✅ Round 2 issue (#95) explains the unclear rule (the "about AI" N/X rule, not the use question) | Done Oct 28 |
| ✅ #95 Round 2 merged and scored; Logan's Numbers file converted · Adjudication: ✅ agreed labels merged (#124, Yen-Chu); 80-passage consensus set built. 9 scenarios still to fill (raters) | Done Nov 4 / Nov 8–9 |
| ✅ Check 4 first run ([results](../docs/part3-metrics/check4_results.md)): ranking robust to weights; strict-only scores all 6 firms 0 from filings; Dong tracks talk (ρ 0.78) not use (0.14) · ✅ guardrail set reviewed against the frozen codebook (22 cases) | Done Oct 27 |
| ✅ Check 1 done and confirmed (precision 98.9%, no clear recall miss; [results](../docs/part3-metrics/check1/results.md)) · ✅ check 5 dry run matched · ✅ check 6 replay · ✅ TP2 sections drafted | Done Nov 3 |
| ✅ #101 Check 4 rerun on the human consensus labels ([results](../docs/part3-metrics/check4_results.md)); updated Nov 9 with 7 more scenarios (#129): Capital One 20, Principal 18, ranking robust (ρ 0.99–1.00); consensus scores file for the dashboard. Rerun once the last 2 scenarios are in | Done Nov 8–9 |
| ✅ Check 4 final, all 80 scenarios in (#145; rerun Nov 9): FY2025 C 53, COF 20, PFG 18, WFC 11, JPM 6, SCHW 6, BAC 6 (was 3); ρ 0.95–1.00, strict 0.69. Sector index v0 merged (#146): FY2025 EW 11.2, CW 8.0 | Done Nov 9 |
| ✅ #102 Check 5: Logan's independent rerun matched ([results](../docs/part3-metrics/check5_rerun.md)) | Done Nov 8 |
| ✅ Presented "how we check results" and Logan's data rules (Logan absent) to Julie | Done Oct 29 |
| ✅ Follow-up-email points for Snehal (strict-vs-broad question; scores combine 10-K + 10-Q) are in #98 | Done Oct 29 |
| ✅ #77 Live 22-case guardrail run (Shu, #117) scored ([results](../docs/part3-metrics/check6_results.md)): 0/18 unsafe with the guardrail, 2/18 without; 0/4 false blocks | Done Nov 5 |
| ✅ Nov 21: deployed the dashboard on Streamlit Community Cloud (only the repo owner has the admin rights it needs) and fixed two bugs found on the way (#178, #180) · reviewed + merged #176 and #179 · refreshed README, SKILL.md v0.3, Evaluation v0.2, Responsible AI v0.3, How we worked v0.2 with the 10-Q rerun numbers | Done Nov 21 |
| ✅ Nov 19: drafts for the final README: [Evaluation section](../docs/tp3/evaluation_section.md) and [How we worked](../docs/tp3/how_we_worked.md) (board talking point), round 3 and #170 numbers pending · removed from round 3 labeling (Logan + a round 1–2 rater, suggested Yen-Chu) · ✅ human-review step built (`src.index.apply_review`, 8 tests; the run report now keeps filled-in reviews) so #170 → #134 works · ✅ SKILL.md v0.2 (76-firm run, review step; #135, Shu to review) · ✅ Responsible AI v0.2 (sector run, held labels, new firm types, 10-Q limit; #139, Logan's retention/attribution part still open) · still: review Logan's paper write-up (#137) once drafted | Nov 19–29 |
| ✅ #39 TP2 compiled · ✅ section 6 confirmed by Snehal (#163) · ✅ board public, cleaned, snapshot taken (#40) · ✅ **final PDF: [`docs/tp2/TP2_progress_report_Team5.pdf`](../docs/tp2/TP2_progress_report_Team5.pdf)** (3 pages + board snapshot page); numbers re-checked against the data, 56 tests pass, dashboard and agent demo run. Backup submitter | Done Nov 12 |
| TP2 sections 1, 3, 4, 7 updated through round 2; check the drafts and remove the markers at compile; trim everyone's paragraphs to 1–3 pages (agreed Nov 8) | Thu Nov 12 |
| ✅ Slides for Tuesday, now 18–19 after the Nov 10 reorder to match the agenda (how we check results; what the human labels changed; final numbers Nov 9) · ✅ deck check Nov 10: slide 15 now lists transcripts as "Future work" (Nov 8 decision), slide 21 has Julie's use-cases-next-to-scores question | Done Nov 8–10 |
| Sync Logan in the chat on the Nov 8 call | Mon Nov 9 |
| ✅ TP3: SKILL.md draft ([`skills/ai-adoption-index/`](../skills/ai-adoption-index/SKILL.md), Shu to review) · paper-discussion expectations + draft + proposed TP3 split ([plan](../docs/tp3/paper_discussion_plan.md); team to agree). ✅ Responsible AI section drafted ([responsible_ai.md](../docs/tp3/responsible_ai.md)) · ✅ board synced Nov 9 (#96, #97 closed; #132–#135 and #137–#143 added; TP3 milestone; PR #131 merged; README rewritten #136) · still: review the paper write-up once Logan drafts it | Done Nov 9 |

### Yen-Chu Chen (Dataset Builder)
| Task | Due |
|---|---|
| ✅ Category review (#33) · transcript source list (#62) | Done Oct 20–23 |
| ✅ #62 revised per Logan's 5 points (source-review table, 7 firms × 8 quarters; Motley Fool not cleared; Capital One, Wells Fargo and Schwab IR sites have no transcripts) | Done Oct 24 |
| ✅ Bloomberg transcripts collected (team Drive only) + Bloomberg rows in #62 · labels round 1 (#82) · Capital One sentences set to D1 by default in #84 (reopen #33 if you disagree) | Done Oct 26–27 |
| Keep the transcripts in CMU-only storage (no public text). #34 closed Nov 11: transcripts out of the index (Nov 8), future work | Ongoing |
| ✅ #97 Sector index: S&P 500 Financials, ~75 firms, public float from 10-K cover pages via SEC's API · Offered next: test the pull on our 7 firms, save the dated list | Done Nov 4 |
| ✅ Presented the test-run findings to Julie | Done Oct 29 |
| ✅ Labeling round 2 (#104, merged Nov 4) · ✅ TP2 blocker (#105) | Done Nov 3–4 |
| ✅ Scenarios for 7 of the 9 passages (#128, with Logan and Snehal) | Done Nov 8 |
| Check Canvas for the TP2 submission | Mon Nov 9 |
| ✅ Sector index plan presented to Julie (Nov 10); v0 built on the 6 PoC firms (#146) · ✅ full 76-firm version merged Nov 23 (#187) | Done |
| #159 Email Julie the cap-weighted worked example, with Snehal (one firm, numbers + 10-K page; Snehal: simplify, add greeting/sign-off, attach the scoring-logic slides). Julie may tweak the method | `UNCLEAR:` asap (Wed Nov 11) |
| ✅ #157 10-Q check: team kept the 10-Qs (Nov 19), Julie approved (Nov 23) | Done Nov 23 |
| **Submit TP2 on Canvas** | **Fri Nov 13, 5 pm** |

### Logan Mai (Market & User Researcher / BA)
| Task | Due |
|---|---|
| ✅ Ethics memo (#63) + DeepSeek retention review (#72) · #62 review · AI-tracker comparison · job-postings question answered (avoid LinkedIn) | Done Oct 22–25 |
| DeepSeek: Dr. Chung said in person after class (Oct 27) that it's OK, since CMU hasn't banned it; the team treats that as enough (Nov 8). Record her email in ethics memo §6 if it arrives | Email pending (not blocking) |
| ✅ CMU library confirmed with Bloomberg; 56 records and the ethics memo updated (#62) | Done Nov 4 |
| ✅ Labeling round 1 (converted to `rater_logan.csv`) | Done Oct 27 |
| ✅ Practice run (~3½ min). Absent from the Julie meeting; Mehul presented the data rules | Done Oct 29 |
| ✅ Labeling round 2 (converted to `rater_logan.csv`; please check it) · ✅ TP2 ethics paragraph (#114) | Done Nov 4 |
| ✅ #102 Check 5 independent rerun: `RESULT: MATCH` · slides updated for Tuesday | Done Nov 8 |
| ✅ Presented the data rules to Julie (Nov 10). Julie asked whether Bloomberg will be added to the index: restate in the follow-up email that transcripts are out (Nov 8 decision, future work) | Done Nov 10 |
| Share the research comparison (#137) with Julie as part of the deliverable (she asked for it Nov 10) | Dec 3 |

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
| Run the agent on the 30 round 2 passages and compare with the agreed labels (command in the [results](../docs/part3-metrics/labeling_round_2/results_round2.md)) | Mon Nov 9 |
| ✅ #133 76-firm S&P 500 Financials run merged (#168): 152 10-Ks FY2024–25, 1,876 passages, ~$1.03, 170 held; round 3 sample built; 10-Q finding for #157 | Done Nov 16 |
| ✅ Pipeline + cost slides presented to Julie (Nov 10): ~75 firms ≈ 1,650 passages, ~1 hour, under $1 a year, ~1 in 20 to a person; pilot 1 firm per new type first | Done Nov 10 |
| Review Mehul's SKILL.md draft ([`skills/ai-adoption-index/SKILL.md`](../skills/ai-adoption-index/SKILL.md)) | `UNCLEAR:` this week |
| ✅ #97 Sector index: ~73 min and ~$0.40 for one year on ~75 firms; 3–5% go to human review | Done Nov 4 |
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
| TP2 section 6 (client meeting): write it from the [Nov 10 minutes](../meetings/2026-11-10-client.md) · ✅ dashboard paragraph (#112), but update it for #152 (fictional tabs are gone; consensus scores + sector tab now) · ✅ labels (#111) | Wed Nov 11 |
| ✅ #96 Dashboard (Julie's feedback): click-to-open definitions, FY2026 hidden, story tab tidied (merged #126). Not yet on the human-agreed labels (see the Nov 8 decision) · ✅ agenda as a doc, email draft ready · ✅ slide deck copy in the Drive (client materials → TP2 checkpoint) | Done Nov 8 |
| #160 TP2 section 6 from the Nov 10 minutes + dashboard paragraph (Wed Nov 11) · ✅ Agenda to Julie; hosted the Nov 10 follow-up and demoed the dashboard | Done Nov 9–10 |
| ✅ #155 CSV downloads merged Nov 21 (#179) · #156 scoring-method explanation on the dashboard (owner `UNCLEAR:`; Yen-Chu has the content) | `UNCLEAR:` |
| #159 Follow-up email to Julie (with Yen-Chu): Yen-Chu's cap-weighting example, transcripts stay out of the index, Dec 3 time + Zoom link once confirmed (owner `UNCLEAR:`; client communication is Snehal's) | `UNCLEAR:` this week |
| ✅ #132 Dashboard on the consensus scores (`data/processed/sec/company_scores_consensus.csv`) with the "80 of 277 human-checked" note, plus a sector-overview tab (equal- and cap-weighted, six firms); mock data removed (PR #152, merged Nov 10) · ✅ screen recording in the deck (slide 11) | Done Nov 10 |
| ✅ #30 Dashboard live Nov 21 (Mehul deployed: Streamlit needs repo admin). Snehal: link is in the README; test it on your phone | Done Nov 21 |
| ✅ Met Dr. Chung Mon Nov 23 (#143): handoff expectations, poster, research inclusion, Evident AI. Notes in the team Drive; post the key decisions on #143 so they can be filed | Done Nov 23 / #143: asap |

### Everyone
- ✅ Raters: agreed labels (#124) and 7 of 9 scenarios (#128). Still to do: `BAC_2025-12-31_10-K_00264` and `SCHW_2024-12-31_10-K_00562` (`UNCLEAR:` who), by Mon Nov 9 noon
- ✅ Decided Nov 8: transcripts out of the index; sector index shows both weightings
- All: slides in the deck by **Mon Nov 9 night**; anticipate Julie's questions on your part. No practice run
- Open (blockers): handover plan (what Julie gets, where the data lives, auto-refresh or not, who links the agent to the dashboard). Julie deferred to Dr. Chung (Nov 10); committed so far: deployed link + user guide

### TP3 issues (proposed split, Nov 9; milestone "TP3: Nov 14–Dec 3 (final)")
| Issue | What | Who |
|---|---|---|
| #137 | Research paper write-up (Babina 2024) + Dong comparison | Logan (Shu: Dong lines; Mehul reviews) |
| #138 | References list | Logan |
| #139 | Responsible AI section (draft v0.1 done) | Mehul (Logan: retention + attribution) |
| #140 | Code demo for the final presentation | Shu |
| #141 | Poster / final deck (poster made together in person Tue Dec 1) | Snehal |
| #142 | Handover plan for Julie (after Tue Nov 10) | Shu + Snehal |
| #143 | ✅ Dr. Chung met Nov 23; takeaways filed | Done |
| #190 | Final-product public repo + add Dr. Chung to GitHub | Mehul (Shu: file list) |
| #191 | Julie's walkthrough (Zoom or recording) + invite Dr. Chung to the poster | Snehal (Shu: recording) |
| #134 | ✅ 76-firm index merged Nov 23 (#187): FY2024 6.4 EW / 6.6 CW, FY2025 8.6 EW / 10.2 CW; Ares FY2025 float kept as Shu's estimate. Left: rerun after the 5 round 3 rows; put the 76-firm index on the dashboard (it still shows the 6-firm pilot) | Yen-Chu |
| #169 | Labeling round 3: sector pilot, 40 passages, 2 raters (human labels only). Logan's labels done (PR #185, held open so Snehal labels blind); Snehal labels alone, then both settle disagreements **Tue Nov 24 after class** | Logan + Snehal (agreed Nov 22) |
| #170 | ✅ 195 of 200 held labels reviewed and merged Nov 22 (Shu #183, Yen-Chu #182): level kept on 72%, 173 confirmed as use; draft FY2025 index 7.2 → 8.6 EW, 9.4 → 10.2 CW. Left: the 5 round 3 blind rows after #169 | Shu + Yen-Chu |
| #157 | ✅ Closed Nov 21: keep the 10-Qs (Citi 53 → 9 without them); rerun merged (#176); ✅ Julie approved Nov 23 (Snehal's email) | Done |
| #135 | SKILL.md review (draft on main since PR #131) | Shu |
| #30 | ✅ Live Nov 21: https://ai-adoption-index.streamlit.app (deployed by Mehul; redeploys on every merge to main) | Done |
| #166 | README as the final project report (scope, visuals, details, What's next, bios) | Yen-Chu (scope/details) + Snehal (visuals) + everyone's bio (assigned Nov 17; target Dec 1) |

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
| Research paper discussion (TP3) | Logan (proposed Nov 9, #137) | Shu (Dong lines), Mehul (review) |

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
- ✅ Nov 8 team call: transcripts out of the index; both index weightings; Streamlit Community Cloud; Tuesday plan; TP2 owners; SKILL.md to Mehul
