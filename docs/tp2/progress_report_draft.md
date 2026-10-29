# TP2 Progress Report: AI Adoption Index (Team 5): DRAFT OUTLINE

> **Due:** Fri Nov 6, 2026, 5:00 pm (Yen-Chu submits on Canvas) · **Length:** 1–3 pages · **Compiled by:** Mehul (by Wed Nov 4)
> **How we write it:** each owner writes **one short paragraph** for their section below by **Mon Nov 2**, replacing the `✍️` placeholders. Mehul combines and trims. Pre-filled facts come from the repo (last refreshed Oct 29); **update them with what actually happened by Nov 2.**
> **Rubric (50 pts):** progress vs. plan 10 · working prototype 12 · blockers 8 · scope updates 5 · board upkeep 5 · client meeting 10. Section numbers below match.
> **AI-use note (course GenAI policy):** this outline was drafted with Claude Code. Each author edits their own section, and the final report states how AI tools were used.

---

## 1. Progress against the TP1 plan (10 pts): Mehul
| TP1 scope commitment | Status (Oct 29) |
|---|---|
| Proof of concept on 5–6 large U.S. financial companies | 6 companies chosen Oct 4 (JPMorgan, Bank of America, Capital One, Wells Fargo, Schwab, Principal) **+ Citigroup as a benchmark** |
| Evidence dataset with source citations | Two SEC runs (#43, #48) consolidated into one version (#65): 74 filings → 277 AI passages, each linked to EDGAR. Earnings calls: Bloomberg via the CMU library (56 transcripts, team Drive only, terms under review in #62) |
| Team-derived taxonomy + quantitative measure | ✅ Categories approved Oct 25 (#64) and **frozen Oct 27** (#84): 11 use-case areas, evidence levels (D2/D1/P/N/X), topic + AGENT tag. Scoring: weights 3/1/0.5, ENT (general claims) = 1 point |
| Evaluation with human review | ✅ Plan v1.2 (6 checks). Round 1 (50 passages, 3 blind raters): real use vs. not κ 0.60–0.72 (meets the 0.6 bar); five levels κ 0.27 → rule clarified, round 2 (30 passages) due Oct 31. Agent vs. people: 96% on 29 unseen passages, overclaim 0–2%. Weight sensitivity (check 4) done; 22-case guardrail set |
| Hosted dashboard | ✅ Streamlit prototype (#73) + **SEC pilot scores tab with real preliminary scores** (#93, Oct 28), shown to Julie Oct 29. Hosting not yet chosen (#30) |
| Reproducible code + methodology | Downloader, passage finder, scorer, evaluation scripts in the repo; an independent re-download matched 168/168 passages |

*Draft (Claude, from the repo; Mehul to check):* We're on track on every TP1 commitment: the proof of concept, the evidence dataset, frozen categories, a working agent, and a dashboard on real preliminary scores, which Julie reviewed on Oct 29. One quality target is behind: agreement on the detailed five-level labels (κ 0.27, below our 0.6 bar). We traced it to one ambiguous rule and are re-testing in round 2. Two items are still open: dashboard hosting, and whether earnings-call transcripts can be used under their license. Julie's new request, a market-cap- and equal-weighted sector index, is being scoped (#97).

✍️ *Mehul: check and trim the draft above after round 2 (Nov 1).*

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
| Detailed-label agreement below the bar (κ 0.27) in round 1 | Traced it to one rule read two ways ("about AI": risk talk is N, not X); rewrote the rule to quote the codebook, added a 2-minute practice set, ran round 2 on 30 new passages (#89, #95) |
| Earnings-call transcripts: free sources not cleared; licensed data vs. a public repo | Bloomberg via the CMU library; transcript text stays out of the public repo and AI tools until the terms are reviewed (#62) |
| A team member's temporary absence | Tasks covered (Shu finalizes the taxonomy if needed); no deadline moved |

✍️ *Each owner: add any blocker from your area (one line).*

## 4. Scope updates since TP1 (5 pts): Mehul
- **Companies:** Capital One replaced Citigroup in the 6; **Citigroup kept as a benchmark** (Oct 4 / Oct 18).
- **Period:** filings from 2024–2026 (Shu's run adds FY2023).
- **Sources:** SEC 10-K/10-Q first; earnings calls from Bloomberg (CMU library) if the terms allow; no LinkedIn job postings.
- **Client meeting:** moved from mid-October to **Thu Oct 29, 10 am** (finals and fall break).
- **Method:** Julie is flexible (simple percentages are fine); we keep "real use vs. just talk" as our contribution.

- **Oct 29 with Julie:** check whether we can build a market-cap-weighted and an equal-weighted **sector index** on a defined public-company sample (a sector stock index or SIC codes). Sources limited to what we can legally get and verify (transcripts only if cleared, without giving extra points for having them). Partial years (FY2026) hidden until complete. Job postings stay out of scope.

✍️ *Mehul: add the team's Nov 1 answer on sector-index feasibility.*

## 5. Project board (5 pts): Mehul
✍️ *Screenshot of the board on Thu Nov 5, plus 1–2 sentences on how we use it (sprint milestone, owners, due dates, pinned "Who does what" issue #45).*

## 6. Client meeting (10 pts): Snehal
- **Thu Oct 29, 10–11 am ET**, with Julie Agnew, Dr. Rachel Chung and Hengkai Zheng invited.
- **Agenda:** test-run findings (Yen-Chu) → AI-use categories and agent (Shu) → dashboard (Snehal) → how we check results (Mehul) → data rules (Logan) → questions for Julie.

- **Notes from the [minutes](../../meetings/2026-10-29-client.md)** (for Snehal to turn into prose):
    - Julie was very positive: the dashboard is "extremely user-friendly", and the talk-vs-use finding is the most interesting part.
    - She confirmed that the source is SEC EDGAR for now.
    - She asked for hover definitions and for partial years to be hidden.
    - Her new request is a sector index (market-cap- and equal-weighted). On transcripts: be cautious, legally verifiable sources only.
    - Follow-up meeting: Nov 10, 13 or 19.

✍️ *Snehal: what Julie confirmed or changed, and the agreed direction for the final stretch.*

## 7. Evaluation and responsible AI (supports sections 1–3): Mehul and Logan
*Draft (Claude, from the repo; Mehul to check):* Three teammates labeled the same 50 passages independently. On the core question, real use or not, agreement met our bar (Cohen's κ 0.60–0.72 across pairs). On the five evidence levels it didn't (Fleiss κ 0.27), mostly because one rule was read two ways. We clarified it and are re-testing in round 2 ([results](../part3-metrics/labeling_round_1/results_round1.md)). Against the human majority, the agent agreed on 96% of the 29 passages it hadn't seen during tuning (κ 0.94). Its overclaim rate (saying a company uses AI when people said it doesn't) was 0–2% across runs, versus about 5% without our code-based guardrail (exact-quote check, specific-detail rule, human review below 0.7 confidence). A 22-case guardrail test set covers fake quotes and injected instructions. The scores' ranking doesn't change when the D2 weight changes (Spearman ρ 1.00). A word-count benchmark (Dong et al.) tracks how much firms *talk* about AI (ρ 0.78), not our use score (ρ 0.14), which supports separating the two ([check 4](../part3-metrics/check4_results.md)).

✍️ *Mehul: add the round 2 result and the guardrail with/without run (#77) once done.*
✍️ *Logan: one paragraph on the ethics memo (sources allowed, retention, citation).*
