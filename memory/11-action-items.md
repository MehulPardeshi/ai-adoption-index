# 11 — Action Items (who is doing what, right now)

> **Read this to answer "what should I work on next?"** Updated after every meeting from `meetings/` minutes ([procedure](../meetings/README.md)). The shared spreadsheet remains the source of truth for owners and deadlines; this file mirrors it for AI tools.
> **Last updated:** 2026-10-25, from the [Oct 25 meeting](../meetings/2026-10-25-internal.md) (capture form + transcript; Mehul absent). Previous: [Oct 18 meeting](../meetings/2026-10-18-internal.md).
> **Pinned summary for humans:** [#45 "Who does what"](https://github.com/MehulPardeshi/ai-adoption-index/issues/45), with @mentions per person.
> **GitHub:** each task below is an issue in the **"Sprint: Oct 18–Nov 6 (TP2)"** milestone on the [project board](https://github.com/users/MehulPardeshi/projects/1).

## Where we are
- ✅ TP1 submitted (Fri Oct 2).
- 🏁 **Sprint: Sun Oct 18 → Fri Nov 6 (TP2).** Categories approved Oct 25 (ENT = 1 point) → labels Tue Oct 27 → practice Wed Oct 28 → **Julie Thu Oct 29, 10–11 am ET** → TP2 report → submit **Fri Nov 6, 5 pm**.
- **PoC companies:** JPMorgan Chase, Bank of America, Capital One, Wells Fargo, Charles Schwab, Principal Financial Group · **Period:** 2024–2026 · **Sources:** SEC 10-K/10-Q (74 filings, 277 AI passages), Dong baseline; earnings calls from **Bloomberg (CMU library) if cleared**, with transcript text kept out of the public repo; no LinkedIn job postings. **Citigroup** kept as a benchmark.
- **AI model:** DeepSeek (`deepseek-flash`), option B: one person pays (Shu), about $0.02 per run. Only public SEC text is sent. **Agent:** 7 tools.

## Key dates
| Date | What |
|---|---|
| ✅ Oct 18–25 | Team meetings Oct 18 and Oct 25 · SEC runs consolidated (#65) · categories approved (#64 + ENT = 1) · ethics memo (#63, #72) · eval plan v1.2 final · dashboard prototype |
| Mon Oct 26 | Yen-Chu checks Bloomberg at the CMU library |
| **Tue Oct 27** | **Labels submitted** (Logan, Yen-Chu, Snehal) · Shu freezes the categories and re-runs the agent · Snehal sends Julie the agenda |
| **Wed Oct 28, 10 am** | **Practice run** (virtual) · agreement scores + check 3 · slides done · more questions for Julie |
| **Thu Oct 29, 10–11 am ET** | Julie, Dr. Chung and Hengkai checkpoint (Zoom) |
| Sun Nov 1 | Team meeting: Julie's feedback → TP2 |
| Mon Nov 2 | Everyone's paragraph in the [TP2 outline](../docs/tp2/progress_report_draft.md) |
| Wed Nov 4 / Thu Nov 5 | TP2 draft (Mehul) / board clean-up |
| **Fri Nov 6, 5 pm** | Yen-Chu submits TP2 (Mehul is the backup) |

## By person

### Mehul Pardeshi (PM + Responsible AI + Evaluation lead)
| Task | Due |
|---|---|
| ✅ Eval plan v1.2 final · labeling kit · red-team set v0 · TP2 outline · Julie talking points · Dong brief · Oct 23 repo check · merged #63–#65, #69–#72 | Done Oct 18–23 |
| Collect the raters' labels; merge #66, then #68 (retarget to `main`) | **Tue Oct 27** |
| Run `python3 -m src.eval.irr` (check 2) and check 3 on Shu's 50-passage agent run (report the 35 passages outside the tuning set separately) | Wed Oct 28 |
| Practice run; "how we check results" slide (4 min; script ready: [talking points v2](../docs/part3-metrics/julie_oct29_talking_points_mehul.md)) | Wed Oct 28 / Thu Oct 29 |
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
| Present the test-run findings to Julie (Shu covers if you're unavailable); your slides in the shared deck | Wed Oct 28 / Thu Oct 29 |
| **Submit TP2 on Canvas** | **Fri Nov 6, 5 pm** |

### Logan Mai (Market & User Researcher / BA)
| Task | Due |
|---|---|
| ✅ Ethics memo (#63) + DeepSeek retention review (#72) · #62 review · AI-tracker comparison · job-postings question answered (avoid LinkedIn) | Done Oct 22–25 |
| Post on #62 whether Bloomberg is approved, with its license terms | Before Yen-Chu downloads |
| Email Rachel: thank her for the LinkedIn reply, and confirm that sending public SEC text to DeepSeek is OK (`UNCLEAR:` the form says Dr. Chung) | Before Wed Oct 28 |
| **Labeling round 1:** label 50 passages **on your own** | **Tue Oct 27** |
| Present the data rules to Julie; your slides in the shared deck | Wed Oct 28 / Thu Oct 29 |

### Shu Pu (AI Engineer / Solution Architect)
| Task | Due |
|---|---|
| ✅ SEC runs consolidated (#65) · categories (#64) · first DeepSeek run (#66) + prompt tuning (#68) | Done Oct 22–23 |
| ✅ Confirmed in #66: official endpoint, public SEC text only (about 600 calls, about $0.21) · agreement numbers labeled "tuning-set (in-sample)" (#66, #68) | Done Oct 25 |
| Remove the DeepSeek key from the how-to Google Doc and rotate it (not yet confirmed) | **ASAP** |
| Freeze the categories: implement **ENT = 1 point** (`--ent-counts`) and update the taxonomy doc; re-run the agent on all 110 passages | **Tue Oct 27** |
| After the raters submit: run the agent on the 50-passage sample (check 3); give Snehal the scores file | Tue Oct 27 → Wed Oct 28 |
| **Agent runs end to end** on the six FY2025 10-Ks (TP2: 12 pts) | **Wed Oct 28** |
| Create the shared slide deck (Drive → Client materials → progress folder) | Wed Oct 28 |
| Cost note for Julie's handover (per run; one-time credit of about $10–20; no API key included) | `UNCLEAR:` before the next Julie meeting |
| Present the categories + agent demo to Julie | Thu Oct 29 |

### Snehal Paliwal (Dashboard PM + client communication)
| Task | Due |
|---|---|
| ✅ Dashboard prototype (Streamlit, fictional mock data) shown Oct 25 and merged (#73: overview → use-case cards → firm comparison, 14 tests) · AI-tracker comparison | Done Oct 25 |
| Record the prototype and upload it to the Drive | `UNCLEAR:` soon |
| First dashboard view with PoC data (Shu's scores file, after you've submitted your labels) | Wed Oct 28 |
| Add a dataset-level summary page. Keep **mock data until you've submitted your labels**; use Shu's real scores file afterwards | Before Thu Oct 29 |
| **Labeling round 1:** label 50 passages on your own with the [Excel workbook](../docs/part3-metrics/labeling_round_1/labeling_workbook.xlsx) | **Tue Oct 27** |
| Formal agenda to Julie | **Tue Oct 27** |
| Send the practice-run invite (Wed Oct 28, 10 am, virtual) | Before Wed |
| Host the Julie meeting, take notes, ask about recording; show the dashboard | Thu Oct 29 |
| Hosting choice (Streamlit Community Cloud vs. Vercel) | `UNCLEAR:` after Julie's feedback |

### Everyone
- Raters (Logan, Yen-Chu, Snehal): **your own judgment on every label** (AI is fine for finding files, not for picking labels); **submit on Tue Oct 27, not earlier**
- Add your slides to the shared deck; bring more questions for Julie: **Wed Oct 28** (practice run 10 am)
- Julie meeting **Thu Oct 29, 10 am**
- Your paragraph in the [TP2 outline](../docs/tp2/progress_report_draft.md): **Mon Nov 2**
- Schedule one more meeting with Julie before the final (`UNCLEAR:` owner)

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
- ✅ Oct 18 meeting: data, taxonomy proposals, model (DeepSeek), agent plan, dashboard plan
- ✅ Oct 25 meeting: categories approved (ENT = 1 point), DeepSeek option B, Bloomberg transcripts if cleared, Julie plan, practice run Wed Oct 28
