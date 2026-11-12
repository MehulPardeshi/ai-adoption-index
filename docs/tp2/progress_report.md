# TP2 Progress Report: AI Adoption Index (Team 5)

**Team:** Mehul Pardeshi (PM, evaluation), Yen-Chu Chen (dataset), Logan Mai (research, ethics), Shu Pu (agent), Snehal Paliwal (dashboard, client) · **Client:** Julie Agnew, William & Mary · **Repo:** [github.com/MehulPardeshi/ai-adoption-index](https://github.com/MehulPardeshi/ai-adoption-index) · **Board:** [project board](https://github.com/users/MehulPardeshi/projects/1) (snapshot attached)

We are building a public, quarterly-refreshable index of how financial services firms *use* AI, as opposed to how much they *talk* about it, from SEC filings, with an agent that labels the evidence and a dashboard for researchers.

## 1. Progress against the TP1 plan
| TP1 commitment | Status (Nov 12) |
|---|---|
| Proof of concept on 5–6 large U.S. financial firms | ✅ JPMorgan, Bank of America, Capital One, Wells Fargo, Schwab, Principal; Citigroup as a benchmark |
| Evidence dataset with citations | ✅ 74 SEC filings (10-K + 10-Q, FY2023–26) → 277 AI passages, each linked to EDGAR |
| Team-derived categories + measure | ✅ Frozen Oct 27: 11 use-case areas; evidence levels D2 (specific use, 3 pts), D1 (general use, 1), P (plan, 0.5), N/X (talk, 0); each area counts once a year at its highest level |
| Evaluation with human review | ✅ All 6 checks run (details in section 3) |
| Working agent | ✅ Runs end to end (section 2) |
| Dashboard | ✅ Streamlit, on the human-agreed scores, with a sector-index view; public link on Streamlit Community Cloud by Dec 3 (#30) |
| Reproducible pipeline | ✅ A teammate who didn't build it reran everything from a fresh clone: same 277 passages, identical scores |

We met every TP1 commitment. One quality target is behind: three raters agreed well on the main question, real AI use or not (κ 0.60–0.72, above our 0.6 bar), but not on the five detailed levels (κ 0.27, then 0.32 on a harder round). Instead of a majority vote, the raters settled all 58 disagreements together on Nov 7. Those 80 human-agreed passages are now our answer key and replace the AI draft labels in the scores. Current FY2025 AI Use Scores: Citi 53 (benchmark), Capital One 20, Principal 18, Wells Fargo 11, JPMorgan 6, Schwab 6, Bank of America 6.

## 2. Working prototype
The agent has 7 tools: fetch filings, find AI passages, classify a passage, verify the label, score companies, look up the Dong et al. baseline, and read labels. Only `classify_passage` calls the model (DeepSeek, temperature 0, fixed JSON schema, cached answers; all runs so far cost about $0.30, and only public SEC text is sent). Every label then passes a rule-based guardrail (`verify_label`): the quote must appear word for word in the filing, a "specific" label needs its detail inside the quote, and labels under 0.70 confidence are held for a person instead of being scored. Batch mode writes the score files the dashboard reads; chat mode lets the model choose its own tools to answer a question, and every claim must cite a quoted passage. Example: for Citi's Q3 2025 10-Q, the agent labels "Approximately 1 million automated code reviews completed by Citi's Generative AI tools year-to-date" as specific use in software engineering (confidence 0.95, guardrail passed), matching the team's agreed label. Demo: `python3 -m src.agent.chat --trace "How does Citigroup use AI in 2025?"` (add `AGENT_LLM_PROVIDER=mock` to run offline).

**Dashboard.** The Streamlit dashboard now uses consensus-based company scores from SEC 10-K and 10-Q filings instead of mock data. It presents individual-firm scores and a six-firm sector overview with equal- and market-cap-weighted series; Citigroup remains a company-level benchmark, not part of the sector index. The Company Scores view includes score definitions and scenario categories, and the sector table explains each column. An About-the-Data view explains the sources and limitations. The dashboard notes that 80 of 277 AI-related passages have human-agreed labels and the rest use AI-draft labels; scores describe disclosures, not verified firm-wide AI adoption. Incomplete FY2026 is hidden, and missing company-years remain blank rather than zero. Julie’s follow-up requests—the broad and strict scores side by side, a check of what 10-Qs add, a data download, and the scoring method on-page—are captured in the next steps.

**Sector index (Julie's Oct 29 request).** Feasible on the S&P 500 Financials (about 75 firms): one year of filings is about 1,650 passages, about an hour of model time and under $1. Firm size comes from public float on each 10-K cover page via SEC's free API. A v0 on our six firms gives FY2025 11.2 equal-weighted and 8.0 cap-weighted: the two largest banks, two thirds of the float, score low.

## 3. Evaluation and blockers
| Check | Result |
|---|---|
| 1. Search finds the AI passages | Precision 98.9%; no clear miss in a sweep of 132,998 unflagged paragraphs |
| 2. Raters agree | Use vs. not κ 0.60–0.72 ✅; five levels κ 0.27/0.32 ✗, so the disagreements were settled together |
| 3. Agent matches people | On 48 passages unseen during tuning: 81% exact (κ 0.73), **0 overclaims**; all 7 misses cautious |
| 4. Scores are robust | Ranking barely moves when weights change (Spearman ρ 0.95–1.00); Dong's word count tracks talk (ρ 0.78) more than use (0.58) |
| 5. Reproducible | Independent rerun: identical scores |
| 6. Guardrail holds | 22 trick cases (fake quotes, tampered numbers, injected instructions, investment advice): 0 of 18 unsafe got through with the guardrail, 2 without; no correct answer blocked |

| Blocker | How we handled it |
|---|---|
| Detailed-label agreement below the bar | Fixed the rule read two ways, ran a second round, then settled all disagreements together (Nov 7) |
| AI draft labels understated use | Swapping in the 80 human labels raised Capital One 3 → 20 and Principal 0 → 18; the drafts missed use or plans in 18 of 80. New filings go through the tested agent, and unsure labels go to a person |
| Licensed transcripts vs. a public repo | Bloomberg cleared through the CMU library (Nov 4); the team kept transcripts out of the index as future work (Nov 8). No transcript text in the repo |
| EDGAR blocked cloud downloads; big banks' filings incomplete | Ran locally with a declared User-Agent, paged the full history, added Wells Fargo's Exhibit 13 |
| No project funding for the model | Team vote: one teammate covers it (about $0.30 so far) |
| Job postings | Excluded on instructor advice (scraping limits; postings disappear) |
| Only ~3 working weeks after finals and fall break | One sprint (Oct 18–Nov 13) with one owner and date per task |

## 4. Scope updates since TP1
- **Companies:** Capital One replaced Citigroup in the six; Citigroup stays as a benchmark.
- **Sources:** SEC 10-K and 10-Q only. Earnings-call transcripts are cleared but left out of the index (future work); no LinkedIn data.
- **New: sector index**, equal- and market-cap-weighted, at Julie's request (Oct 29); feasibility confirmed, full ~75-firm run next.
- **From the Nov 10 meeting:** the broad AI Use Score is the headline, with the strict (specific-use only) score beside it; the category codes are enough detail; we'll check what the 10-Qs add and move to 10-K only if nothing material; the dashboard gets a data download and an on-page scoring method.

## 5. Project board
Every task is a GitHub issue with one owner and a due date, grouped by milestone ("Sprint: Oct 18–Nov 13 (TP2)" and "TP3: Nov 14–Dec 3"). A pinned issue (#45) lists who does what and is updated after each meeting; meeting minutes, decisions and action items are filed in the repo, and changes reach `main` only through reviewed pull requests. Snapshot attached.

## 6. Client meeting
We met Julie twice. On Oct 29 she reviewed the first dashboard, found the talk-vs-use gap the most interesting result, and asked for a sector index (equal- and market-cap-weighted), metric definitions and hidden partial years. At the Nov 10 follow-up we showed all three, the label checks and the six-firm index. Julie called the work "outstanding" and gave clear direction: the broad score as the headline with the strict one beside it; no extra use-case detail beyond the category codes; scores from 10-Ks only if the 10-Qs add nothing; a download button and the scoring method on the dashboard. For handover she deferred to Dr. Chung's preference; we committed to a deployed dashboard and a user guide, and she'll join the Dec 3 presentation remotely.

## 7. Next steps to Dec 3
~75-firm agent run and full sector index (#133, #134) · 10-Q check (#157) · dashboard download and method page (#155, #156) · hosting (#30) · handover plan with Dr. Chung (#142, #143) · research-paper comparison, Responsible AI section and SKILL.md (#137–#139, #135).

*AI use: drafted with Claude Code from the team's repo; each owner reviews their own section, and all numbers come from scripts in the repo.*
