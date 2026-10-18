# 11 — Action Items (who is doing what, right now)

> **Read this to answer "what should I work on next?"** Updated after every meeting from `meetings/` minutes ([procedure](../meetings/README.md)). The shared spreadsheet remains the source of truth for owners and deadlines; this file mirrors it for AI tools.
> **Last updated:** 2026-10-18, from the email thread with Julie (Oct 10–11) and the repo status. Previous update: [Oct 4 meeting](../meetings/2026-10-04-internal.md).
> **Pinned summary for humans:** [#45 "Who does what"](https://github.com/MehulPardeshi/ai-adoption-index/issues/45), with @mentions per person.
> **GitHub:** each task below is an issue in the **"Sprint: Oct 18–Nov 6 (TP2)"** milestone on the [project board](https://github.com/users/MehulPardeshi/projects/1).

## Where we are
- ✅ TP1 submitted (Fri Oct 2).
- 💤 **Oct 5–17: finals, then fall break.** No project work expected, apart from Snehal's email to Julie and the optional review of her materials.
- 🏁 **Sprint: Sun Oct 18 → Fri Nov 6 (TP2).** Test run on 6 companies → show Julie **Thu Oct 29, 10–11 am ET** (confirmed) → TP2 report → submit **Fri Nov 6, 5 pm**.
- **PoC companies:** JPMorgan Chase, Bank of America, Capital One, Wells Fargo, Charles Schwab, Principal Financial Group · **Period:** 2024–2026 · **Sources:** SEC 10-K/10-Q, AI Intensity GitHub dataset, earnings calls; LinkedIn only if the ethics memo clears it.

## Key dates
| Date | What |
|---|---|
| ~~Mon Oct 5~~ ✅ | Snehal emailed Julie (Oct 10–11); Julie reviewed the scope and sent the Vanguard paper |
| **Sun Oct 18, 8–9 pm** | Team meeting: decide the AI model and agent tools; everyone brings research + an action plan |
| Fri Oct 23 | Ethics memo final · SEC filings downloaded · eval plan v1 · agent design · dashboard tool/sketch |
| Sun Oct 25 | Team meeting: progress check |
| Wed Oct 28 | Taxonomy v0 done (Tue Oct 27) · first working agent · first labeling round · first dashboard view · practice run |
| **Thu Oct 29, 10–11 am ET** | ✅ Confirmed: "Checkpoint: AI Adoption Index [Team 5]" on Zoom, with Julie, Dr. Chung and Hengkai invited (calendar invite from Snehal, Oct 11) |
| Sun Nov 1 | Team meeting: Julie's feedback → split the TP2 report |
| Wed Nov 4 / Thu Nov 5 | TP2 report draft / board clean-up |
| **Fri Nov 6, 5 pm** | Yen-Chu submits TP2 |

## By person

### Mehul Pardeshi (PM + Responsible AI + Evaluation lead)
| Task | Due |
|---|---|
| ✅ Reviewed Julie's materials: [summary](../docs/reviews/2026-10-18_client-materials-review_mehul.md) | Done Oct 18 |
| ✅ Evaluation plan v1 drafted: [`docs/part3-metrics/evaluation_plan.md`](../docs/part3-metrics/evaluation_plan.md) (team review Oct 18; finalize by Fri Oct 23) | Fri Oct 23 |
| Labeling round 1: kit ready ([`labeling_round_1/`](../docs/part3-metrics/labeling_round_1/README.md)). Label your 50 blind by Tue Oct 27; run `python3 -m src.eval.irr` Wed Oct 28 | Tue Oct 27 / Wed Oct 28 |
| Red-team test set for the guardrails (evaluation check 6), with Shu | Wed Oct 28 |
| Compile the TP2 report draft (1–3 pages) | Wed Nov 4 |
| Clean up the GitHub board; screenshot for TP2 | Thu Nov 5 |
| Responsible AI: guardrail ideas for the agent (with/without comparison, course req. #7) | ongoing |

### Yen-Chu Chen (Dataset Builder)
| Task | Due |
|---|---|
| Before Oct 18: review Julie's paper/GitHub; research; bring an action plan | Sun Oct 18 |
| Download SEC 10-K/10-Q (2024–2026) for the 6 companies (with Shu) | Fri Oct 23 |
| Read 10–15 sample reports; list how companies use AI (with Shu) | Sat Oct 24 |
| Taxonomy v0: first categories (with Shu) | Tue Oct 27 |
| Collect earnings-call transcripts for the 6 companies | TBD (confirm Oct 18) |
| Assess LinkedIn as a source, **only after** Logan's ethics memo clears it | after Oct 23 |
| **Submit TP2 on Canvas** | **Fri Nov 6, 5 pm** |

### Logan Mai (Market & User Researcher / BA)
| Task | Due |
|---|---|
| Before Oct 18: review Julie's paper/GitHub; research; bring an action plan | Sun Oct 18 |
| **Ethics / legal sourcing memo** (incl. whether LinkedIn and earnings calls may be used) | Draft Wed Oct 21; **final Fri Oct 23** |
| Compare existing AI-adoption trackers (with Snehal) | Sat Oct 24 |
| **Labeling round 1:** label 50 passages blind (about an hour), following [`labeling_round_1/README.md`](../docs/part3-metrics/labeling_round_1/README.md) | **Tue Oct 27** |

### Shu Pu (AI Engineer / Solution Architect)
| Task | Due |
|---|---|
| Before Oct 18: research free AI models + agent tool ideas; review the AI Intensity GitHub dataset | Sun Oct 18 |
| Download SEC filings (with Yen-Chu) | Fri Oct 23 |
| Agent design: at least 5 custom tools | Fri Oct 23 |
| Sample reading + taxonomy v0 (with Yen-Chu) | Sat Oct 24 / Tue Oct 27 |
| **First working AI agent** (TP2's 12-point item) | Wed Oct 28 |

### Snehal Paliwal (Dashboard PM + client communication)
| Task | Due |
|---|---|
| ✅ Emailed Julie; Oct 29, 10 am meeting booked; asked Julie for links to the other papers | Done Oct 11 |
| Before Oct 18: review Julie's paper/GitHub; research; bring an action plan | Sun Oct 18 |
| Dashboard: Streamlit mock-up; check hosting (Vercel vs Streamlit Community Cloud) | Start Fri Oct 23 |
| First dashboard view with PoC data | Wed Oct 28 |
| Compare existing AI trackers (with Logan) | Sat Oct 24 |
| Lead the progress meeting with Julie | Thu Oct 29 |

### Everyone
- Practice run of what we show Julie: **Wed Oct 28**
- Discuss labeling disagreements (round 1 results): **Wed Oct 28**

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
