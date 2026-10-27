# TP2 Progress Report: AI Adoption Index (Team 5): DRAFT OUTLINE

> **Due:** Fri Nov 6, 2026, 5:00 pm (Yen-Chu submits on Canvas) · **Length:** 1–3 pages · **Compiled by:** Mehul (by Wed Nov 4)
> **How we write it:** each owner writes **one short paragraph** for their section below by **Mon Nov 2**, replacing the `✍️` placeholders. Mehul combines and trims. Pre-filled facts come from the repo (last refreshed Oct 27); **update them with what actually happened by Nov 2.**
> **Rubric (50 pts):** progress vs. plan 10 · working prototype 12 · blockers 8 · scope updates 5 · board upkeep 5 · client meeting 10. Section numbers below match.
> **AI-use note (course GenAI policy):** this outline was drafted with Claude Code. Each author edits their own section, and the final report states how AI tools were used.

---

## 1. Progress against the TP1 plan (10 pts): Mehul
| TP1 scope commitment | Status (Oct 19; update by Nov 2) |
|---|---|
| Proof of concept on 5–6 large U.S. financial companies | 6 companies chosen Oct 4 (JPMorgan, Bank of America, Capital One, Wells Fargo, Schwab, Principal) **+ Citigroup as a benchmark** |
| Evidence dataset with source citations | Two SEC runs (#43, #48) consolidated into one version (#65): 74 filings → 277 AI passages, each linked to EDGAR. Earnings calls: Bloomberg via the CMU library (56 transcripts, team Drive only, terms under review in #62) |
| Team-derived taxonomy + quantitative measure | Categories approved Oct 25 (#64): scenario codes, evidence level (D2/D1/P/N/X), topic + AGENT tag. Scoring: weights 3/1/0.5, ENT (general claims) = 1 point. Freeze due Oct 27 (Shu) |
| Evaluation with human review | Evaluation plan v1.2 final (6 checks); labeling round 1 (50 passages, 3 blind raters) due Oct 27; 20-case guardrail test set |
| Hosted dashboard | Streamlit prototype on mock data merged (#73, Oct 25) → first view with PoC data (Oct 28) |
| Reproducible code + methodology | Downloader, passage finder, scorer, evaluation scripts in the repo; an independent re-download matched 168/168 passages |

✍️ *Mehul: 3–4 sentences on what's on track vs. behind (update after Oct 29).*

## 2. Working prototype: the agentic AI component (12 pts): Shu
- **Design:** 7 tools: `fetch_sec_filings`, `find_ai_passages`, `score_companies` (built); `fetch_transcripts`, `classify_passage`, `verify_label`, `lookup_baseline` (to build).
- **Target for Oct 28:** runs end to end on the six FY2025 10-Ks: fetch → find AI passages → classify → verify quote → score → CSV for the dashboard.
- **Model:** DeepSeek `deepseek-flash` (temperature 0, fixed JSON schema). Funding decided Oct 25 (#55): one person pays; all runs so far about $0.21. Only public SEC text is sent.
- **Built so far:** first DeepSeek run on the six FY2025 10-Ks (#66) and prompt tuning (#68). Agreement there is in-sample (tuning set), not validation.

✍️ *Shu: what the agent actually does by Nov 2, one example output, and where the demo code is.*

✍️ *Snehal: one paragraph on the dashboard view that uses the agent's output.*

## 3. Blockers and how we handled them (8 pts): Mehul (with input from each owner)
| Blocker | How we handled it |
|---|---|
| Finals + fall break left about 3 working weeks | Re-planned on Oct 4 into an Oct 18–Nov 6 sprint, with one owner and date per task |
| Draft labels were mislabeled as hand-coded; they were AI-assisted | Caught by the author (Oct 19); moved to the AI side of evaluation check 3; added a third blind human rater |
| Two separate SEC runs (Yen-Chu, Shu) | Consolidated into one version (#65, Oct 23) |
| Benchmark data defect: the Dong et al. dataset scores Wells Fargo 0 every year (its parser missed the 10-K body) | Documented as a known limitation; no re-count (team decision Oct 25) |
| Model cost vs. "no funding" scope constraint | Team vote Oct 25 (#55): one teammate covers it (about $0.21 so far); only public text is sent |
| Unclear whether job-posting data may be used | Asked Rachel (#54): avoid LinkedIn |
| Earnings-call transcripts: free sources not cleared; licensed data vs. a public repo | Bloomberg via the CMU library; transcript text stays out of the public repo and AI tools until the terms are reviewed (#62) |
| A team member's temporary absence | Tasks covered (Shu finalizes the taxonomy if needed); no deadline moved |

✍️ *Each owner: add any blocker from your area (one line).*

## 4. Scope updates since TP1 (5 pts): Mehul
- **Companies:** Capital One replaced Citigroup in the 6; **Citigroup kept as a benchmark** (Oct 4 / Oct 18).
- **Period:** filings from 2024–2026 (Shu's run adds FY2023).
- **Sources:** SEC 10-K/10-Q first; earnings calls from Bloomberg (CMU library) if the terms allow; no LinkedIn job postings.
- **Client meeting:** moved from mid-October to **Thu Oct 29, 10 am** (finals and fall break).
- **Method:** Julie is flexible (simple percentages are fine); we keep "real use vs. just talk" as our contribution.

✍️ *Mehul: add any changes agreed with Julie on Oct 29.*

## 5. Project board (5 pts): Mehul
✍️ *Screenshot of the board on Thu Nov 5, plus 1–2 sentences on how we use it (sprint milestone, owners, due dates, pinned "Who does what" issue #45).*

## 6. Client meeting (10 pts): Snehal
- **Thu Oct 29, 10–11 am ET**, with Julie Agnew, Dr. Rachel Chung and Hengkai Zheng invited.
- **Agenda:** test-run findings (Yen-Chu) → AI-use categories and agent (Shu) → dashboard (Snehal) → how we check results (Mehul) → data rules (Logan) → questions for Julie.

✍️ *Snehal: what Julie confirmed or changed, and the agreed direction for the final stretch.*

## 7. Evaluation and responsible AI (supports sections 1–3): Mehul and Logan
✍️ *Mehul: labeling round 1 results (agreement scores, AI overclaim rate) and the first guardrail with/without run, if ready.*
✍️ *Logan: one paragraph on the ethics memo (sources allowed, retention, citation).*
