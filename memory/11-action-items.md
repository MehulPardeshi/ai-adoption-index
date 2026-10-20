# 11 — Action Items (who is doing what, right now)

> **Read this to answer "what should I work on next?"** Updated after every meeting from `meetings/` minutes ([procedure](../meetings/README.md)). The shared spreadsheet remains the source of truth for owners and deadlines; this file mirrors it for AI tools.
> **Last updated:** 2026-10-19, from the [Oct 18 meeting](../meetings/2026-10-18-internal.md) (capture form + transcript). Previous: [Oct 4 meeting](../meetings/2026-10-04-internal.md).
> **Pinned summary for humans:** [#45 "Who does what"](https://github.com/MehulPardeshi/ai-adoption-index/issues/45), with @mentions per person.
> **GitHub:** each task below is an issue in the **"Sprint: Oct 18–Nov 6 (TP2)"** milestone on the [project board](https://github.com/users/MehulPardeshi/projects/1).

## Where we are
- ✅ TP1 submitted (Fri Oct 2).
- 💤 **Oct 5–17: finals, then fall break.** No project work expected, apart from Snehal's email to Julie and the optional review of her materials.
- 🏁 **Sprint: Sun Oct 18 → Fri Nov 6 (TP2).** Test run on 6 companies → show Julie **Thu Oct 29, 10–11 am ET** (confirmed) → TP2 report → submit **Fri Nov 6, 5 pm**.
- **PoC companies:** JPMorgan Chase, Bank of America, Capital One, Wells Fargo, Charles Schwab, Principal Financial Group · **Period:** 2024–2026 · **Sources:** SEC 10-K/10-Q, AI Intensity GitHub dataset (Shu's Dong baseline), earnings calls (cleared sources only); job postings pending guidance from Rachel/mentor. **Citigroup** kept as a benchmark.
- **AI model:** DeepSeek (≈$20–30; ⚠️ funding source needed), local Ollama model as fallback. **Agent:** 7 tools.

## Key dates
| Date | What |
|---|---|
| ~~Mon Oct 5~~ ✅ | Snehal emailed Julie (Oct 10–11); Julie reviewed the scope and sent the Vanguard paper |
| ✅ Sun Oct 18 | Team meeting ([minutes](../meetings/2026-10-18-internal.md)) |
| Mon Oct 19 EOD | Everyone finishes their blank boxes in the Oct 18 capture form |
| Wed Oct 22 | SEC runs consolidated (Shu + Yen-Chu) · taxonomy proposals finalized (Shu, if Yen-Chu is still out) · ethics memo draft in the repo (Logan, Wed Oct 21) |
| Fri Oct 23 | Ethics memo final · Logan asks Rachel/mentor about job postings · eval plan v1 final |
| **Sun Oct 25, 8–9 pm** | Team meeting · dashboard mock-up (Snehal) · DeepSeek funding settled · practice-run day chosen · everyone has read the Dong paper |
| Tue Oct 27 | Taxonomy v0 final · labeling round 1 done (Mehul, Logan, Yen-Chu, each separately) |
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
| ✅ Dong paper: [reading brief](../docs/reviews/2026-10-19_dong-paper-brief_mehul.md) (skim the PDF intro/conclusion to confirm) | Done Oct 19 |
| **Labeling round 1:** fill in the [Excel workbook](../docs/part3-metrics/labeling_round_1/labeling_workbook.xlsx) **on your own** (~40 min; no one can do this for you, since it's the human-rater check); submit Tue Oct 27 | **Tue Oct 27** |
| Run `python3 -m src.eval.irr`; share agreement scores + AI overclaim rate | Wed Oct 28 |
| Red-team set: ✅ v0 drafted (20 cases). Shu wires it in; first with/without run | ~Nov 3 |
| Present "how we check our results" to Julie | Thu Oct 29 |
| TP2: everyone fills the [outline](../docs/tp2/progress_report_draft.md) by Mon Nov 2; Mehul combines by Wed Nov 4; board clean-up Thu Nov 5 | Wed Nov 4 / Thu Nov 5 |

### Yen-Chu Chen (Dataset Builder): excused absence on Oct 18; tasks resume when available
| Task | Due |
|---|---|
| Review Shu's taxonomy proposals in your doc (marked ▶ SHU). If you're unavailable, Shu finalizes | Wed Oct 22 |
| Consolidate your SEC run with Shu's (yours as the base) | Wed Oct 22 |
| Earnings-call transcript **source list** for Logan to clear; collect only cleared sources; no transcript text in GitHub | TBD |
| **Labeling round 1:** label 50 passages on your own (don't reopen the AI-assisted draft labels) | **Tue Oct 27** |
| Present the test-run findings to Julie (Shu covers if you're unavailable) | Thu Oct 29 |
| **Submit TP2 on Canvas** | **Fri Nov 6, 5 pm** |

### Logan Mai (Market & User Researcher / BA)
| Task | Due |
|---|---|
| **Ethics memo:** move the draft from Google Drive into `docs/part1-sourcing/ethics_memo.md` for review. Note that SEC filings are public *company* filings, not government records | Wed Oct 21 |
| Ethics memo final | **Fri Oct 23** |
| Ask Rachel/mentor (Hengkai) for guidance on job-posting data (they come and go; can we cite company careers pages?) | Fri Oct 23 |
| Review the transcript sources' permissions (when Yen-Chu sends the list) | TBD |
| Compare existing AI-adoption trackers (with Snehal) | Sat Oct 24 |
| Read the Dong et al. paper | Sun Oct 25 |
| **Labeling round 1:** label 50 passages **on your own**, following [`labeling_round_1/README.md`](../docs/part3-metrics/labeling_round_1/README.md) | **Tue Oct 27** |
| Present the data rules (ethics) to Julie | Thu Oct 29 |

### Shu Pu (AI Engineer / Solution Architect)
| Task | Due |
|---|---|
| ✅ Second SEC run + Dong baseline + Dong paper review (PR #48); taxonomy answers (PR #50) | Done Oct 19 |
| Consolidate the two SEC runs into one version (Yen-Chu's as the base, plus your extras) | Wed Oct 22 |
| Finalize the taxonomy proposals if Yen-Chu is still unavailable | Wed Oct 22 |
| DeepSeek: confirm the cost and a funding source with Mehul; pin the model version; Ollama fallback | Sun Oct 25 |
| Build `classify_passage`, `verify_label`, `lookup_baseline` (7 tools in total) | Wed Oct 28 |
| **Agent runs end to end** on the six FY2025 10-Ks and writes a CSV for the dashboard (TP2: 12 pts) | **Wed Oct 28** |
| Present the categories + the AI agent to Julie | Thu Oct 29 |

### Snehal Paliwal (Dashboard PM + client communication)
| Task | Due |
|---|---|
| Dashboard mock-up (Streamlit) on a separate branch in our repo; confirm hosting (Streamlit Community Cloud vs. Vercel) | **Sun Oct 25** (moved from Fri Oct 23) |
| First dashboard view with PoC data: per company, the AI use cases, with click-through to detail | Wed Oct 28 |
| Compare existing AI trackers (with Logan) | Sat Oct 24 |
| Read the Dong et al. paper | Sun Oct 25 |
| Send Julie the agenda (suggested: by Mon Oct 26) | Mon Oct 26 |
| Host the Julie meeting + show the dashboard | Thu Oct 29 |

### Everyone
- Finish your blank boxes in the Oct 18 capture form: **Mon Oct 19 EOD** (2b, 6a, 6b, 6d, 8a, 8c, 8d, 8e, 9a still open)
- Read the Dong et al. paper: **Sun Oct 25** (Shu's review + Mehul's brief with our companies' numbers are in `docs/reviews/`)
- Raters (Mehul, Logan, Yen-Chu): use the Excel labeling workbook; **submit on Tue Oct 27, not earlier**
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
- Snehal asked Julie (Oct 10) whether rescoping away from Dr. Chung's original brief is OK; the answer isn't recorded yet.

## Completed
- ✅ Team contract signed (9/20–9/24), section 4 filled in before TP1
- ✅ Repo, kanban board, shared tracker; all members invited (9/27–9/28)
- ✅ Roles approved (10/1); kickoff meeting with Julie (10/1)
- ✅ TP1 submitted (10/2): contract, prep doc, scope v1.0
- ✅ Oct 4 meeting: PoC companies, period, sources, timeline and dates decided
