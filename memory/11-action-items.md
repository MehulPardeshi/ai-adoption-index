# 11 — Action Items (who is doing what, right now)

> **Read this to answer "what should I work on next?"** Updated after every meeting from `meetings/` minutes ([procedure](../meetings/README.md)). The shared spreadsheet remains the source of truth for owners and deadlines; this file mirrors it for AI tools.
> **Last updated:** 2026-10-25 (dashboard status refreshed; other assignments remain as logged Oct 23). Before that: 2026-10-19, from the [Oct 18 meeting](../meetings/2026-10-18-internal.md) (capture form + transcript). Previous: [Oct 4 meeting](../meetings/2026-10-04-internal.md).
> **Pinned summary for humans:** [#45 "Who does what"](https://github.com/MehulPardeshi/ai-adoption-index/issues/45), with @mentions per person.
> **GitHub:** each task below is an issue in the **"Sprint: Oct 18–Nov 6 (TP2)"** milestone on the [project board](https://github.com/users/MehulPardeshi/projects/1).

## Where we are
- ✅ TP1 submitted (Fri Oct 2).
- 💤 **Oct 5–17: finals, then fall break.** No project work expected, apart from Snehal's email to Julie and the optional review of her materials.
- 🏁 **Sprint: Sun Oct 18 → Fri Nov 6 (TP2).** Test run on 6 companies → show Julie **Thu Oct 29, 10–11 am ET** (confirmed) → TP2 report → submit **Fri Nov 6, 5 pm**.
- **PoC companies:** JPMorgan Chase, Bank of America, Capital One, Wells Fargo, Charles Schwab, Principal Financial Group · **Period:** 2024–2026 · **Sources:** SEC 10-K/10-Q, AI Intensity GitHub dataset (Shu's Dong baseline), earnings calls (cleared sources only); job postings pending guidance from Rachel/mentor. **Citigroup** kept as a benchmark.
- **AI model:** DeepSeek (`deepseek-flash`). Real cost so far is about $0.02 per run (Shu paid), so #55 is small but still needs a team decision. Local Ollama model as fallback. **Agent:** 7 tools.

## Key dates
| Date | What |
|---|---|
| ~~Mon Oct 5~~ ✅ | Snehal emailed Julie (Oct 10–11); Julie reviewed the scope and sent the Vanguard paper |
| ✅ Sun Oct 18 | Team meeting ([minutes](../meetings/2026-10-18-internal.md)) |
| ✅ Oct 19–23 | Capture-form boxes · SEC runs consolidated (#65) · taxonomy finalized (#64) · ethics memo draft (#63) · eval plan v1.2 final (#29 closed) |
| Sat Oct 24 | AI-tracker comparison (Logan + Snehal) |
| **Sun Oct 25, 8–9 pm** | Team meeting · votes: ethics memo approval, ENT 0 vs 1 point, DeepSeek payment · dashboard mock-up (Snehal) · practice-run day chosen · everyone has read the Dong paper |
| Mon Oct 26 | Snehal sends Julie the agenda |
| Tue Oct 27 | Taxonomy v0 final · labeling round 1 done (Logan, Yen-Chu, Snehal; each separately) |
| Wed Oct 28 | Agent runs end to end on the six FY2025 10-Ks · agreement scores · first dashboard view · practice run (Tue or Wed) |
| **Thu Oct 29, 10–11 am ET** | ✅ Confirmed: "Checkpoint: AI Adoption Index [Team 5]" on Zoom, with Julie, Dr. Chung and Hengkai invited (calendar invite from Snehal, Oct 11) |
| Sun Nov 1 | Team meeting: Julie's feedback → split the TP2 report |
| Wed Nov 4 / Thu Nov 5 | TP2 report draft / board clean-up |
| **Fri Nov 6, 5 pm** | Yen-Chu submits TP2 |

## By person

### Mehul Pardeshi (PM + Responsible AI + Evaluation lead)
| Task | Due |
|---|---|
| ✅ Reviewed Julie's materials · Evaluation plan v1.1 · labeling kit · `irr.py` | Done Oct 18–19 |
| ✅ Form boxes answered (6a, 6b, 6d, 8a, 9a; see the minutes' follow-up) · red-team set v0 · labeling cheat sheet · TP2 outline · Julie talking points | Done Oct 19 |
| Bring the DeepSeek funding options to the team vote (#55) | Sun Oct 25 |
| ✅ Merged #63 (ethics memo, as a draft), #64 (taxonomy), #65 (consolidation), #69 (rater X rule) | Done Oct 23 |
| Merge #66, then #68 (retarget to `main`), **on or after Tue Oct 27** once all three raters have submitted | Tue Oct 27 |
| ✅ Dong paper read in full; [verified brief](../docs/reviews/2026-10-19_dong-paper-brief_mehul.md), with 3 corrections to earlier notes | Done Oct 19 |
| Labeling round 1: **no longer a rater**. Snehal confirmed as replacement (Oct 20). Collect the raters' workbooks and convert them | Tue Oct 27 |
| Run `python3 -m src.eval.irr`; share agreement scores + AI overclaim rate | Wed Oct 28 |
| Red-team set: ✅ v0 drafted (20 cases). Shu wires it in; first with/without run | ~Nov 3 |
| Present "how we check our results" to Julie | Thu Oct 29 |
| TP2: everyone fills the [outline](../docs/tp2/progress_report_draft.md) by Mon Nov 2; Mehul combines by Wed Nov 4; board clean-up Thu Nov 5 | Wed Nov 4 / Thu Nov 5 |

### Yen-Chu Chen (Dataset Builder): excused absence on Oct 18; tasks resume when available
| Task | Due |
|---|---|
| ✅ Reviewed Shu's taxonomy proposals (agreed in #33; Shu's #64 applies them) | Done Oct 20–22 |
| ✅ Consolidation merged (#65: 277 passages, 74 filings) | Done Oct 23 |
| **Earnings-call transcripts:** Logan reviewed #62 on Oct 23: **not cleared yet**. Add his source-review table (URL, company/quarter, rights holder, terms, date checked; separate decisions for access, local storage, team sharing and publication), use Motley Fool's US terms, and check Capital One's IR site. Don't collect until cleared. Collect for the 6 companies (+ Citi), and record each source for Logan to review. Collect only cleared sources; no transcript text in GitHub without a documented basis | **Sun Oct 25** |
| **Labeling round 1:** label 50 passages on your own (don't reopen the AI-assisted draft labels) | **Tue Oct 27** |
| Present the test-run findings to Julie (Shu covers if you're unavailable) | Thu Oct 29 |
| **Submit TP2 on Canvas** | **Fri Nov 6, 5 pm** |

### Logan Mai (Market & User Researcher / BA)
| Task | Due |
|---|---|
| ✅ **Ethics memo** draft in #63 (`docs/part1-sourcing/ethics_memo.md`) | Done Oct 22 |
| Ethics memo final: team approval Sun Oct 25; add DeepSeek's data-retention terms (§6) | **Sun Oct 25** |
| Ask Rachel/mentor (Hengkai) for guidance on job-posting data (they come and go; can we cite company careers pages?) | Fri Oct 23 |
| ✅ Reviewed #62 (transcript sources): not cleared; changes requested from Yen-Chu | Done Oct 23 |
| Compare existing AI-adoption trackers (with Snehal) | Sat Oct 24 |
| Read the Dong et al. paper | Sun Oct 25 |
| **Labeling round 1:** label 50 passages **on your own**, following [`labeling_round_1/README.md`](../docs/part3-metrics/labeling_round_1/README.md) | **Tue Oct 27** |
| Present the data rules (ethics) to Julie | Thu Oct 29 |

### Shu Pu (AI Engineer / Solution Architect)
| Task | Due |
|---|---|
| ✅ Second SEC run + Dong baseline + Dong paper review (PR #48); taxonomy answers (PR #50) | Done Oct 19 |
| ✅ SEC runs consolidated (#65) · taxonomy finalized with Yen-Chu (#64) | Done Oct 22 |
| ✅ First DeepSeek run (#66) + prompt tuning to classify-v1.4 with a Citi benchmark (#68). Agreement so far is vs. the AI-assisted draft labels, not humans (see memory/09, Oct 23). Merge after Oct 27 | Done Oct 22–23 |
| Remove the DeepSeek key from the how-to Google Doc and rotate it | **ASAP** |
| ✅ Agent v1 merged (#60): 7 tools, guardrail, batch/chat/red-team runners, 19 offline tests. **Not yet connected to DeepSeek** | Done Oct 20 |
| **Agent runs end to end** on the six FY2025 10-Ks and writes a CSV for the dashboard (TP2: 12 pts) | **Wed Oct 28** |
| Present the categories + the AI agent to Julie | Thu Oct 29 |

### Snehal Paliwal (Dashboard PM + client communication)
| Task | Due |
|---|---|
| ✅ Dashboard mock-up (Streamlit) now demonstrates a fictional firm-to-record-to-comparison journey using real firm names only as selectors; confirm hosting (Streamlit Community Cloud vs. Vercel) | **Sun Oct 25** |
| First dashboard view with PoC data: per company, the AI use cases, with click-through to detail | Wed Oct 28 |
| Compare existing AI trackers (with Logan) | Sat Oct 24 |
| Read the Dong et al. paper | Sun Oct 25 |
| Send Julie the agenda (suggested: by Mon Oct 26) | Mon Oct 26 |
| **Labeling round 1 (confirmed Oct 20, replacing Mehul):** label 50 passages on your own with the [Excel workbook](../docs/part3-metrics/labeling_round_1/labeling_workbook.xlsx), about 40 min | **Tue Oct 27** |
| Host the Julie meeting + show the dashboard | Thu Oct 29 |

### Everyone
- Read the Dong et al. paper: **Sun Oct 25** (Shu's review + Mehul's brief with our companies' numbers are in `docs/reviews/`)
- Raters (Logan, Yen-Chu, Snehal): use the Excel labeling workbook; **submit on Tue Oct 27, not earlier**. Mehul runs the analysis
- Write your paragraph in the [TP2 outline](../docs/tp2/progress_report_draft.md): **Mon Nov 2**
- Practice run (Tue or Wed, chosen Oct 25), then the Julie meeting **Thu Oct 29, 10 am**

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
- **Dashboard:** a Streamlit interface prototype is now present in `src/dashboard/` and uses synthetic fixtures only. It does not load project data, source evidence, or scoring rules. This is a UI simulation, not the PoC data view; the latter remains due Wed Oct 28.
- Snehal asked Julie (Oct 10) whether rescoping away from Dr. Chung's original brief is OK; the answer isn't recorded yet.

## Completed
- ✅ Team contract signed (9/20–9/24), section 4 filled in before TP1
- ✅ Repo, kanban board, shared tracker; all members invited (9/27–9/28)
- ✅ Roles approved (10/1); kickoff meeting with Julie (10/1)
- ✅ TP1 submitted (10/2): contract, prep doc, scope v1.0
- ✅ Oct 4 meeting: PoC companies, period, sources, timeline and dates decided
