# 09 — Decisions Log (APPEND-ONLY)

> ## ⚠️ This file OVERRIDES everything else in `/memory/`.
> Files 00–08 and 10 contain **drafts, menus, and starter lists**. Once the team makes a decision and records it here, **this log wins** over whatever those files say. AI agents: read this file **first**, and treat later entries as overriding earlier ones.

## Rules
- **Append only.** Never edit or delete past entries. To reverse a decision, add a new entry that references the old one.
- Add entries **after every meeting** (Thursday client meetings, Sunday internal meetings) and whenever a majority vote happens in the WhatsApp chat.
- Decisions are made by **majority vote** (team contract). Note the vote or who agreed.
- Things to log here include **final role picks**, **the shared spreadsheet link**, tool choices (dashboard tool, NLP stack), the firm list, taxonomy versions, metric definitions, and calendar dates for Weeks 1–6.

## Entry template
```
### YYYY-MM-DD — <short title>
- **Decision:** <what was decided>
- **Context / why:** <one or two lines>
- **Decided by:** <majority vote at Sunday meeting / client request / etc.>
- **Supersedes:** <link to earlier entry, or "—">
- **Follow-ups:** <owner per the spreadsheet, or "—">
```

---

## Log

<!-- Append new entries below this line, newest at the bottom. -->

### 2026-09-24 — Team contract adopted
- **Decision:** Team contract agreed at a Sunday internal meeting and signed by all five members (09/20–09/24/2026). Its norms are summarized in `02-team-norms.md`.
- **Context / why:** Required for Team Project #1 (due Fri 2026-10-02).
- **Decided by:** All members (signed).
- **Supersedes:** —
- **Follow-ups:** Next meeting is Thu 2026-10-01. Open items: role picks from `01-team-and-roles.md`, formalizing Snehal's client-communication role, the shared spreadsheet link, the blank "Expectations / Attendance" section of the contract.

### 2026-09-27 — GitHub repo and kanban board set up
- **Decision:** Engineering backlog lives in the private repo `MehulPardeshi/ai-adoption-index`, with the kanban board at https://github.com/users/MehulPardeshi/projects/1 (columns To Do / In Progress / Done). Week 1–6 milestone issues (#1–#6) and the course-requirements checklist (#7) are seeded, all unassigned.
- **Context / why:** The course requires a GitHub kanban board (TP1 scope doc must link it; TP3 grades it at 7%). Per the contract, the shared spreadsheet remains the source of truth for owners and deadlines.
- **Decided by:** PM setup (infrastructure only; no project-content decisions).
- **Supersedes:** —
- **Follow-ups:** Invite teammates to the repo and the board; add the spreadsheet link to `docs/TASK_TRACKER.md`.

### 2026-09-27 — Thu Oct 1 meeting is the first client requirements meeting
- **Decision:** The Thu 2026-10-01 meeting (2:00–3:00 pm slot) is with the client, Julie Agnew. It serves as the course's "first client requirements meeting."
- **Context / why:** TP1 (due Fri 2026-10-02) needs a client-meeting prep doc (client, problem as understood, questions) and a scope document with the kanban board link. The scope doc goes to the client for approval.
- **Decided by:** PM (confirmed schedule).
- **Supersedes:** Clarifies the "next meeting" follow-up in the 2026-09-24 entry.
- **Follow-ups:** Prepare client questions before Thursday. Snehal (de facto client comms) to confirm the role formally.

### 2026-09-28 — Shared tracker created
- **Decision:** The contract-mandated shared spreadsheet is an Excel Online workbook on CMU OneDrive: https://andrewcmu-my.sharepoint.com/:x:/g/personal/mppardes_andrew_cmu_edu/IQBkCeheAvmPSrU1SkxKTJkZAdr85cdpnKE8PpNSuGpDSG4?e=OGs7Ky. It has Tasks / Roles / Meetings tabs, and its format comes from `docs/tracker/team_tracker.xlsx`. It syncs with GitHub through links plus a weekly reconcile (see `docs/TASK_TRACKER.md`).
- **Context / why:** The PM created it so its format matches the repo structure.
- **Decided by:** PM setup (the tracker itself was already agreed in the contract).
- **Supersedes:** —
- **Follow-ups:** Teammates add their rows to the Roles tab; owners for TP1 tasks T08, T10, T11, T13 to be set at the setup call.

### 2026-09-28 — Teammates invited to repo and board
- **Decision:** All five members have access. Invites (write access) went to the repo and the kanban board for @teddy0-0y (Yen-Chu Chen), @MaiJialong (Logan Mai), @seanpushu (Shu Pu) and @snehalpaliwal (Snehal Paliwal); Mehul (@MehulPardeshi) is the owner.
- **Context / why:** Needed before teammates clone the repo and submit their `team/` profiles.
- **Decided by:** PM setup.
- **Supersedes:** —
- **Follow-ups:** Each member accepts the invite email, then runs the setup prompt (ONBOARDING_FOR_NON_CODERS.md, Step 2).

### 2026-09-30 — Kickoff agenda set; joint meeting with Team 15
- **Decision:** The Thu 2026-10-01 kickoff is a **joint meeting of Team 5 and Team 15** with the clients **Dr. Julie Agnew (William & Mary)** and **Dr. Rachel Chung (Heinz College)**. Agenda: `docs/tp1/client_meeting_agenda.md` (original PDF alongside).
- **Context / why:** First client requirements meeting, which must happen before TP1 (due Fri 2026-10-02). The agenda covers what the index measures, firm and data scope, taxonomy, and the book-chapter framing.
- **Decided by:** Team (agenda prepared for the client).
- **Supersedes:** —
- **Follow-ups:** Raise the TP1 items not on the agenda (NDA, progress-meeting date, final-presentation invite, confidentiality) during Next Steps; the note-taker records answers for the scope doc.

### 2026-10-01 — Meeting minutes via Gemini note-taker
- **Decision:** Every meeting is recorded with the Gemini note-taker. Afterwards, a teammate uploads the notes to an AI tool, which files them in `meetings/` and updates `memory/09` (decisions), `memory/11-action-items.md` (tasks by person) and affected files, through a PR. Procedure: `meetings/README.md`.
- **Context / why:** Keeps every teammate's AI tool current on decisions and assignments, so each person can ask "what's next for me?"
- **Decided by:** PM.
- **Supersedes:** —
- **Follow-ups:** Decide who uploads notes after each meeting (capture form, O-6).

### 2026-10-01 — Public and permitted evidence
- **Decision:** Use public, citable evidence collected within applicable access rules.
- **Context / why:** Source selection; restricted university career data are excluded.
- **Decided by:** Julie Agnew, client direction in supplied kickoff excerpts; minutes pending team review.
- **Supersedes:** Earlier draft assumptions only where inconsistent; no course requirement is waived.
- **Follow-ups:** See [kickoff minutes](../meetings/2026-10-01-client.md); owners and dates TBD.

### 2026-10-01 — Methodology flexibility
- **Decision:** The team may choose the index methodology; earlier construction guidance is not mandatory and simple percentages are acceptable.
- **Context / why:** Final taxonomy, metrics, weighting, and normalization remain undecided. Course grading requirements still need reconciliation with the instructor.
- **Decided by:** Julie Agnew, client direction in supplied kickoff excerpts; minutes pending team review.
- **Supersedes:** Earlier draft assumptions only where inconsistent; no course requirement is waived.
- **Follow-ups:** See [kickoff minutes](../meetings/2026-10-01-client.md); owners and dates TBD.

### 2026-10-01 — Transparent and reproducible results
- **Decision:** Make the analysis verifiable and reproducible through GitHub, with transparent firm inclusion.
- **Context / why:** Public client identity and book references still require explicit permission.
- **Decided by:** Julie Agnew, client direction in supplied kickoff excerpts; minutes pending team review.
- **Supersedes:** Earlier draft assumptions only where inconsistent; no course requirement is waived.
- **Follow-ups:** See [kickoff minutes](../meetings/2026-10-01-client.md); owners and dates TBD.

### 2026-10-01 — Feasible scope revisions
- **Decision:** The team may propose a narrower achievable scope to Julie.
- **Context / why:** The 4–5-bank pilot is a recommendation; broader coverage and quarterly automation are not firm commitments.
- **Decided by:** Julie Agnew, client direction in supplied kickoff excerpts; minutes pending team review.
- **Supersedes:** Earlier draft assumptions only where inconsistent; no course requirement is waived.
- **Follow-ups:** See [kickoff minutes](../meetings/2026-10-01-client.md); owners and dates TBD.

### 2026-10-01 — Team roles approved
- **Decision:** All five proposed roles were approved unchanged.
- **Context / why:** Yen-Chu supplied the completed B1 role-vote table, showing Yes for every member, and confirmed the decision occurred today.
- **Decided by:** Team role vote, as recorded in the capture form.
- **Supersedes:** Pending-role status in team profiles and earlier role menus, including pending confirmation of Snehal's client-communication role.
- **Follow-ups:** Mirror these roles in the shared spreadsheet; individual task assignments and deadlines still require confirmation.

| Member | Confirmed role |
|---|---|
| Mehul Pardeshi | Project Manager + Responsible AI lead |
| Yen-Chu Chen | Dataset Builder |
| Logan Mai | Market & User Researcher / Business Analyst |
| Shu Pu | AI Engineer / Solution Architect |
| Snehal Paliwal | Dashboard Product Manager, including client communication |

### 2026-10-01 — Evaluation design responsibility clarified
- **Decision:** The Responsible AI Lead (Mehul Pardeshi) will design the evaluation and validation approach.
- **Context / why:** Yen-Chu clarified this responsibility during scope refinement; no sampling method or acceptance threshold was selected.
- **Decided by:** Proposed by Yen-Chu during scope refinement; accepted by Mehul Pardeshi on 2026-10-01.
- **Supersedes:** Unassigned evaluation-design responsibility only.
- **Follow-ups:** Define the approach and mirror the task in the shared spreadsheet; deadline TBD.

### 2026-10-01 — Client logistics confirmed (capture form)
- **Decision:** No NDA. We **may name Julie Agnew and the book chapter** in the repo, poster and LinkedIn. Teams 5 and 15 get **separate** progress checks and updates. Julie will **review and approve** our scope document. Communication by **email**, with a follow-up after 24 hours. The team develops both the index definition and the calculation method. Public sources only.
- **Context / why:** Answers N-1 to N-8 and I-B in the kickoff capture form filled in by Snehal (`meetings/2026-10-01-client-capture-form.docx`).
- **Decided by:** Julie Agnew (client answers).
- **Supersedes:** The confidentiality-by-default note in `00-project-overview.md`; the UNCLEAR NDA/naming items in the kickoff minutes.
- **Follow-ups:** Confirm the PoC size with Julie (4–5 banks per the excerpts vs 5–6 big financial companies per the form); schedule the progress meeting on a Thursday or Friday; send the Dec 3 invite.

### 2026-10-01 — Mehul's role expanded to include Evaluation lead
- **Decision:** Mehul Pardeshi's role is **Project Manager + Responsible AI + Evaluation lead**.
- **Context / why:** Mehul accepted ownership of evaluation and validation design (course requirement #5, including inter-rater reliability).
- **Decided by:** Mehul Pardeshi (accepted).
- **Supersedes:** The role title in the 2026-10-01 "Team roles approved" entry.
- **Follow-ups:** Mirror the title in the spreadsheet's Roles tab.

### 2026-10-01 — TP1 submission and client follow-up owners
- **Decision:** **Yen-Chu** submits TP1 on Canvas (Fri 10/2, 5 pm). **Snehal** sends the scope document and the follow-up email to Julie (PoC size, progress-meeting date, Dec 3 invite).
- **Context / why:** TP1 deadline; Snehal is the confirmed client-communication lead.
- **Decided by:** PM (Mehul).
- **Supersedes:** "TBD" owners for these tasks in `11-action-items.md`.
- **Follow-ups:** —

### 2026-10-01 — Proof-of-concept size: 5–6 big financial companies
- **Decision:** The proof of concept covers **5–6 big U.S. financial companies** (e.g., JPMorgan).
- **Context / why:** The transcript excerpts recorded "4–5 major publicly traded banks"; the capture form (N-1) recorded the client asking for "5–6 big financial companies… as a proof of concept on dashboard". Mehul chose to follow the capture form.
- **Decided by:** Mehul Pardeshi (PM), based on the client's recorded answer.
- **Supersedes:** "4–5-bank pilot" wording in earlier entries and drafts, and the open PoC-size follow-up in "Client logistics confirmed (capture form)".
- **Follow-ups:** Snehal states the 5–6-company PoC in the scope email to Julie; the firm list is chosen at the Sun 2026-10-04 meeting.

### 2026-10-01 — Deliverable owners and TP1 tasks (capture form Part B)
- **Decision:** Snehal is the formal client-communication lead. Deliverable owners: **ethics memo: Logan**; **taxonomy: Yen-Chu and Shu**; **IRR raters: all**; **metrics write-up: all**; **index construction + methodology appendix: Mehul and Snehal**; **presentation/poster: Snehal**; research paper: Julie to provide candidates, team owner TBD. TP1: prep doc, scope and review by all; Snehal sends the scope and calendar invites, with the **progress meeting targeted mid-October**; Yen-Chu submits on Canvas.
- **Context / why:** Part B of the kickoff capture form, filled in after the meeting.
- **Decided by:** Team (capture form).
- **Supersedes:** "Unowned" deliverables in `11-action-items.md`.
- **Follow-ups:** Still open: Week 1–6 dates, dashboard tool, contract section 4, TA confirmation, Team 15 coordination, who uploads meeting notes. Paper link from Julie needed.

### 2026-10-04 — Proof-of-concept plan and sprint (internal meeting)
- **Decision:**
  - **Companies:** JPMorgan Chase, Bank of America, Capital One, Wells Fargo, Charles Schwab, Principal Financial Group.
  - **Period:** 2024–2026.
  - **Sources:** SEC 10-K/10-Q (Shu), the AI Intensity GitHub dataset (Shu), earnings calls (Yen-Chu), LinkedIn (Yen-Chu, **only if the ethics memo confirms permitted access**, per scope v1.0).
  - **What we show Julie:** a company view with click-in detail; index categories (investment in AI, AI in final products, AI-related jobs).
  - **Client progress meeting:** proposed Thu Oct 29, 1–2 pm.
  - **Timeline:** Mehul's prep-doc timeline and due dates accepted, including **Yen-Chu submitting TP2 on Fri Nov 6**.
  - **Dashboard:** Streamlit; Vercel proposed for deployment (to verify).
  - **Hengkai Zheng** confirmed as project TA.
  - Work **fully separately from Team 15**.
  - Ask Dr. Chung about grading requirements after scoping is finalized with Julie.
  - **Next meeting:** Sun Oct 18, 8–9 pm.
- **Context / why:** Finals (Oct 5–9) and fall break (Oct 12–16) leave a working window of Oct 18–Nov 6 before TP2.
- **Decided by:** Team (all five attended), recorded in the capture form. No transcript.
- **Supersedes:**
  - "PoC before fall break" and "client progress meeting mid-October" (scope v1.0 and earlier entries);
  - Mehul's proposals of Citigroup (replaced by Capital One), 2 years (now 2024–2026), and 10-K/10-Q only (sources widened);
  - the open TA question;
  - the blank-contract-section-4 note.
- **Follow-ups:**
  - Snehal emails Julie by Mon Oct 5.
  - Scope v1.1 with the new dates goes to Julie.
  - Owner for the Dr. Chung question is TBD.
  - Per-person tasks are in `11-action-items.md` and in the GitHub sprint milestone.

### 2026-10-11 — Client progress meeting confirmed: Thu Oct 29, 10–11 am ET
- **Decision:** The client checkpoint is **Thu Oct 29, 2026, 10:00–11:00 am ET** on Zoom ("Checkpoint: AI Adoption Index [Team 5]"). Invited: all of Team 5, Julie Agnew, Dr. Rachel Chung and Hengkai Zheng.
- **Context / why:**
  - On Oct 10, Snehal thanked Julie for reviewing the scope, asked whether rescoping away from Dr. Chung's original brief is OK, and asked for links to the other papers.
  - On Oct 11, Snehal confirmed 10 am and sent the invite.
  - Julie shared the Vanguard *Megatrends: AI, demographics and the U.S. economy* report.
- **Decided by:** Snehal (client lead), with Julie.
- **Supersedes:** the "Thu Oct 29, 1–2 pm (proposed)" time from the 2026-10-04 entry.
- **Follow-ups:**
  - Record Julie's answer on rescoping when it arrives.
  - The practice run stays Wed Oct 28.
  - Materials are listed in `docs/references.md`.

### 2026-10-18 — Evaluation design for labeling round 1; Dr. Chung grading question dropped
- **Decision:**
  - **Labeling round 1 (evaluation check 2):** 50 passages from the SEC test run, chosen by stratified sampling (all 32 deployed/planned passages plus 18 random "just talk" ones, after dropping repeats and definitions; seed 20261018).
  - **Raters:** Yen-Chu's existing hand labels plus **Mehul and Logan labeling blind**.
  - **Provisional pass mark:** kappa ≥ 0.60, revisited after round 1.
  - **Separately:** the team won't pursue asking Dr. Chung which original-brief requirements still apply. Issue #42 is closed.
- **Context / why:** Evaluation plan v1 (`docs/part3-metrics/evaluation_plan.md`) by the Evaluation Lead.
- **Decided by:** Mehul Pardeshi (Evaluation Lead / PM), with the eval plan up for team review on Oct 18.
- **Supersedes:** the open Dr. Chung follow-ups in the 2026-10-04 entry.
- **Follow-ups:**
  - Logan confirms availability to label by Tue Oct 27.
  - The team reviews the provisional pass marks.

### 2026-10-19 — SEC draft labels are AI-assisted; Yen-Chu becomes the third blind human rater
- **Decision:**
  - The 245 draft labels in `passage_labels_v0.csv` are **AI-assisted** (drafted with Claude, not reviewed passage by passage), so they are **not** a human rater.
  - They become the **AI side of evaluation check 3**, compared with the human majority.
  - Labeling round 1 has **three blind human raters: Mehul, Logan and Yen-Chu** (all by Tue Oct 27).
  - `src/eval/irr.py` keeps human agreement (check 2) separate from AI vs. humans (check 3, with the overclaim rate).
- **Context / why:** Yen-Chu flagged the error on Oct 19 and corrected the wording in PR #49. The #43 doc had called the labels hand-coded.
- **Decided by:** Mehul Pardeshi (Evaluation Lead), on Yen-Chu's suggestion.
- **Supersedes:** the rater setup in the 2026-10-18 "Evaluation design for labeling round 1" entry.
- **Follow-ups:**
  - Note in TP2 that Yen-Chu had seen the AI draft labels beforehand, so her agreement with the AI may be inflated.
  - Record the AI assistance per the course GenAI policy.

### 2026-10-18 — Internal meeting: data, taxonomy proposals, sources, model, agent, dashboard
- **Decision:** See the [minutes](../meetings/2026-10-18-internal.md) for all 14 decisions. The main ones:
  - **Data:** keep Citigroup as a benchmark. Consolidate Yen-Chu's and Shu's SEC runs (hers as the base).
  - **Taxonomy:** Shu's proposals (weights 3/1/0.5; a general multi-area sentence counts once, as ENT; keep "predictive models" but label non-AI hits X) are pending Yen-Chu's review, or Shu finalizes by Wed Oct 22.
  - **Sources and ethics:**
    - keep the necessary SEC passages, with full citations;
    - earnings calls only from cleared sources, with no transcript text in GitHub without a documented redistribution basis;
    - job postings: Logan asks Rachel/mentor for guidance.
  - **AI model:** **DeepSeek** (temperature 0, fixed JSON schema), local Ollama model as fallback.
  - **Agent:** **7 tools** (adds `lookup_baseline`); runs end to end on the six FY2025 10-Ks by Oct 28.
  - **Dashboard:** Streamlit; mock-up on a branch in our repo by Oct 25.
  - **Julie meeting:** presenter split accepted.
  - Everyone reads the Dong paper.
- **Context / why:** First meeting after fall break. Yen-Chu was absent (excused). Source: capture form + transcript.
- **Decided by:** Team (Mehul, Snehal, Shu, Logan).
- **Supersedes:**
  - the "free model only" assumption: DeepSeek costs about $20–30. ⚠️ The scope constraint says any cost needs a team decision **and an identified funding source**, which is still open;
  - the Oct 4 "LinkedIn pending the memo" note, now replaced by asking Rachel/mentor;
  - the dashboard mock-up date (Oct 23 → Oct 25).
- **Follow-ups:**
  - **Labeling round:** the form's "Logan and Mehul can work together" means coordinating timing only. Each labels separately.
  - Unanswered form boxes are due Oct 19 EOD.

### 2026-10-19 — Labeling round 1: Mehul steps back as a rater; Snehal asked to replace him
- **Decision:**
  - Mehul (Evaluation Lead) **won't label**. He designs the round, runs `src/eval/irr.py` and leads the discussion of disagreements.
  - **Snehal is asked to take his place as the third blind human rater** (about 40 min with the Excel workbook, by Tue Oct 27). **Pending her agreement.**
  - **Fallback:** if Snehal can't, check 2 runs with **two raters (Logan + Yen-Chu)**, and TP2 notes that Yen-Chu had seen the AI-assisted draft labels.
- **Context / why:** Mehul couldn't commit the time to label. AI-generated labels can't stand in for a human rater (see the 2026-10-19 entry on AI-assisted labels). Separating the analyst from the raters is also methodologically cleaner.
- **Decided by:** Mehul Pardeshi (Evaluation Lead / PM).
- **Supersedes:** the rater list (Mehul, Logan, Yen-Chu) in the earlier 2026-10-19 entry.
- **Follow-ups:** Snehal confirms on WhatsApp. If she agrees, she labels by Tue Oct 27.

### 2026-10-20 — Snehal confirmed as rater; scenario rule fixed; Yen-Chu's answers; agent v1; model cost
- **Decision:**
  - **Snehal confirmed** as the third rater (with Logan and Yen-Chu). Fallback: two raters.
  - **Scenario rule:** scenario codes are required for **D2, D1 and P** (as in `src/nlp/taxonomy_v0.py`), not only D1/D2. Fixed in the rater instructions, workbook, checker, `irr.py` and red-team case RT20.
  - **Yen-Chu:** keep Citigroup (agrees). She'll **collect earnings-call transcripts before Sun Oct 25**, recording each source for Logan's review.
  - **Agent v1 merged** (#60): 7 tools, guardrail, red-team runner, 19 offline tests. Not yet connected to DeepSeek.
- **Context / why:**
  - Shu caught the scenario mismatch in #60, before labeling started.
  - #60 estimates **about $0.05 per run and under $5 for the project**, which shrinks the #55 funding question.
- **Decided by:** Snehal and Yen-Chu (WhatsApp / capture form); Mehul (Evaluation Lead) for the scenario fix.
- **Supersedes:** "Snehal pending" in the 2026-10-19 entry; the D1/D2-only scenario rule in the labeling kit; "transcripts after the Julie meeting / team decides".
- **Follow-ups:** The #55 vote on Sunday uses the new cost estimate. The first real agent run follows.

### 2026-10-23 — Repo check before the Oct 25 meeting: X rule mid-round, agent results kept separate from check 3
- **Decision:**
  - **X rule widened mid-round (#64):** a search hit that isn't really about AI is now **X**. The cheat sheet, the workbook and the README say "`about_ai` = N → X". `irr.py` turns any rater's `about_ai` = N into X, so raters who labeled before the change aren't counted as disagreeing.
  - **Agent results aren't check 3.** Shu's first DeepSeek run and prompt tuning (#66, #68) report 94% agreement and 2.2% overclaim. Both are measured against the **AI-assisted draft labels**, on the same 90 passages the prompt was tuned on. The ≤ 5% overclaim bar is measured against the **human majority** after Oct 27.
  - **15 of the 50 labeling-sample passages are in the 90-passage tuning set.** Check 3 reports the other 35 separately.
  - **Keep the raters blind:** the agent's output files (#66, #68) are merged only **after the raters submit on Tue Oct 27**, and the README adds them to the "don't open" list.
- **Context / why:**
  - The agent files contain labels for 15 sample passages.
  - Tuning and testing on the same items overstates accuracy.
  - #65 (consolidation, 245 → 277 passages) only adds rows. All 50 sample passages are present and unchanged.
- **Also noted for Sunday:**
  - The ethics memo draft (#63) §6 asks us to check a provider's data-retention terms before sending text to an external AI. The DeepSeek run already sent public SEC passages, so record DeepSeek's terms and confirm.
  - The agent how-to guide (a Google Doc) contains the DeepSeek key in plain text. Remove it from the doc and rotate the key. No key is in the repo: every branch and its history was checked on Oct 23.
- **Decided by:** Mehul Pardeshi (Evaluation Lead / PM).
- **Supersedes:** nothing; adds to the 2026-10-20 entry.
- **Follow-ups:**
  - ✅ #63 (as a draft), #64, #65 and #69 merged Oct 23 by Mehul.
  - Merge #66, then #68 (retargeted to `main`), on or after Oct 27.
  - On Sunday: the ENT 0-vs-1 vote and approval of the ethics memo.

### 2026-10-25 — Internal meeting: categories approved, ENT = 1 point, DeepSeek option B, Bloomberg transcripts, Julie plan
- **Decision:**
  - **Categories approved:** codes and evidence levels (3a); the #64 rules: weights 3/1/0.5, a "we use AI for A, B, C" sentence counts once as ENT, non-AI "predictive models" hits are X (3b); AGENT topic tag (3d). No separate "how AI is used" tag; the team says the scenario codes already cover it (3e).
  - **ENT earns 1 point** in the AI Use Score (was 0). TP2 must explain that ENT is a general, umbrella-level claim. Shu freezes the categories and re-runs the agent on Tue Oct 27, after Yen-Chu rules on 3 Capital One sentences.
  - **DeepSeek: option B** (one person pays; Shu offered, at most about $5). The team accepts the retention risk because only public SEC text is sent. Logan double-checks with the instructor. Long term: hand Julie the setup without our API key, plus a cost note.
  - **Earnings calls: Bloomberg through the CMU library**, if allowed for this use (Logan agreed in principle). Yen-Chu checks Mon Oct 26 and downloads manually. Transcript text stays out of the **public** repo (the Oct 18 decision still applies). Bloomberg's terms go into the #62 source-review table first.
  - **Job postings:** avoid LinkedIn as a source (per the instructor's reply; form 1a).
  - **TP3 papers:** Babina et al. (2024) as the main paper, Dong et al. (2026) as the comparison method. No Wells Fargo recount (5c).
  - **Julie meeting (Thu Oct 29):** agenda 6a accepted, on simplified slides. Demo both the dashboard (mock data, for usability feedback) and the agent. Snehal sends the formal agenda by Tue Oct 27, takes notes, and asks about recording. Practice run Wed Oct 28, 10 am, virtual.
  - **TP2:** everyone writes their own section by Mon Nov 2. Yen-Chu submits; Mehul is the backup. Next team meeting Sun Nov 1. Schedule one more meeting with Julie before the final.
- **Context / why:**
  - ENT: Yen-Chu argued that a clear "we use AI" is still evidence of use; Shu agreed. Without it, Wells Fargo scored 0.
  - DeepSeek cost so far is about $0.02 per run.
  - Bloomberg came up after Logan didn't clear the third-party transcript sites (#62).
- **Decided by:** the team (Snehal, Shu, Logan, Yen-Chu) at the Oct 25 meeting. Mehul was absent (unwell).
- **Supersedes:**
  - ENT = 0 points (the 2026-10-20 scoring and the #64 "Open (vote)" row).
  - "Transcript sources pending Logan's review" (now Bloomberg, if cleared).
  - The 5b "TP3 paper options".
  - Agenda to Julie "by Mon Oct 26" (now Tue Oct 27).
- **Follow-ups:**
  - Shu implements ENT = 1 in the scorer and codebook doc (`score_companies.py --ent-counts` exists) and freezes the categories by Tue Oct 27.
  - Logan posts Bloomberg's terms on #62.
  - Raters label with their own judgment; AI only for finding files.

### 2026-10-25 — Follow-ups after the meeting: DeepSeek run confirmed, transcript review revised
- **Decision:**
  - The ethics memo's §6 remediation note is closed. Shu confirmed in #66 that the first runs used the official DeepSeek endpoint and sent only public SEC 10-K passage text (110 passages, about 600 calls, about $0.21). The confirmation is recorded in the memo.
  - Yen-Chu's earnings-call collection deadline moves to **Mon Oct 26**, because the source changed to Bloomberg (as agreed at the meeting).
  - #62 merges once Logan signs off on the four decisions per source, including Bloomberg.
- **Context / why:** Logan's §6 asked the operator to confirm the endpoint and payload. Yen-Chu revised #62 per Logan's five points on Oct 24: a source-review table with only links and rights metadata, no transcript text.
- **Decided by:** Mehul (PM), recording teammates' confirmations.
- **Supersedes:** nothing.
- **Follow-ups:** Shu confirms the key is out of the how-to Google Doc and rotated. Logan reviews Bloomberg's academic terms on #62.

### 2026-10-27 — Categories frozen; labeling round 1 and check 3 results (no meeting)
- **Decision:**
  - **Categories frozen** (#84, closes #33). ENT = 1 point is the scorer's default (`--no-ent` keeps the old rule as a sensitivity check). The three Capital One risk-factor sentences are D1, applied by default because #33 had no reply; Yen-Chu can reopen.
  - **Labeling round 1 is the official record as submitted.** No labels were changed after submission; Logan's Numbers workbook was converted to `rater_logan.csv` without changes.
- **Results (facts, not decisions):**
  - Check 2: real use vs. not κ 0.60–0.72 (meets the bar); the five evidence levels, Fleiss κ 0.27 (0.49 with N/X merged). Most of the gap: one rater read "about AI" as "about AI use" ([results](../docs/part3-metrics/labeling_round_1/results_round1.md)).
  - Check 3 (#85): on the 29 passages outside the tuning set, 96% exact, κ 0.94, overclaim 0% (0–2% across runs), about 5% without the guardrail. The clean set is 29, not 35: 6 sample passages are also among the 20 Citi tuning passages.
  - DeepSeek: Prof. Chung told Logan after class that it's OK, since CMU hasn't banned it; Logan asked her to confirm by email.
  - Bloomberg: Logan emailed the CMU business librarian about download, team sharing, external AI processing and publication. Full-text use stays paused until he replies.
- **Context / why:** the planned Oct 27 steps (labels in → merge #66/#68 → scores) all happened.
- **Decided by:** Shu (freeze, per the Oct 25 team vote); Mehul (PM/Evaluation lead) for the round-1 record.
- **Supersedes:** "re-count Wells Fargo" (already dropped on Oct 25); the "35 non-tuning passages" figure in the eval plan.
- **Follow-ups (for the Wed Oct 28 practice run):** clarify the "about AI" rule in the cheat sheet, go through the disagreements together, and run round 2 on 30 new passages (team to decide). Record Prof. Chung's email in ethics memo §6 when it arrives.

### 2026-10-28 — Practice run: meeting format, round 2 timing, Julie follow-up
- **Decision:**
  - **Julie meeting format:** pause for questions after each section. Snehal opens by saying Julie can also stop us at any time. Simple transition slides go between sections; the deck order is as Snehal reordered it in the call. Shu keeps his agent-output example slide.
  - **Labeling round 2** isn't needed before Julie. The raters aim for **Sat Oct 31 (afternoon)** and upload together.
  - **Julie follow-up:** Snehal asks Julie on Thursday for **Thu Nov 12, 10 am**.
- **Context / why:**
  - The full run-through took about 27 minutes (target 40), leaving time for questions.
  - Round 2 by Thursday was too tight with midterms. Mehul's script already says the second round is running.
  - The follow-up gives Julie a second look after round 2 and Julie's feedback are in.
- **Decided by:** the team at the Oct 28 practice run ([minutes](../meetings/2026-10-28-internal.md)). Round 2 timing: Yen-Chu proposed, Snehal agreed (Logan not recorded).
- **Supersedes:**
  - Round 2 "by Sun Nov 1" (now Sat Oct 31).
  - The Oct 25 "schedule one more meeting with Julie" with no owner (now Snehal, proposing Nov 12).
- **Follow-ups:**
  - Snehal fixes the dashboard's data-transparency tab before Thursday.
  - Mehul tells the raters which rule was unclear (the "about AI" N/X rule, not the use question) before Saturday.

### 2026-10-29 — Client checkpoint with Julie: sector-index request, transcript caution, follow-up date
- **Decision:**
  - The team researches whether a **sector index** is feasible: **market-cap-weighted and equal-weighted** AI scores per sector, on a defined sample of public companies (e.g., a financial-sector stock index or SIC codes), keeping the per-firm drill-down. Julie accepts a realistic version if the full one isn't possible.
  - **Sources:** Julie is fine with restricting the index to what we can legally get and verify. Manually pulled sources (Bloomberg at a terminal) don't fit an automated index. She expects the library to say no; we confirm with the librarian.
  - **Follow-up meeting:** Nov 12 is off (Julie has a board meeting). The team picks Tue Nov 10, Fri Nov 13 or Thu Nov 19.
- **Context / why:**
  - Julie wants an index she can use in the chapter ("larger firms weigh more" vs. "how the whole industry is doing"), not only firm-by-firm views.
  - She liked the dashboard and the "talk vs. use" finding. She asked for hover definitions and for partial years (FY2026) to be hidden. Citi's drop from 48 to 0 is a partial-year effect.
  - All 7 firms' fiscal years end Dec 31 (checked from the 10-K periods), so the years line up.
- **Decided by:** Julie (client) with Snehal for the team, at the Oct 29 checkpoint ([minutes](../meetings/2026-10-29-client.md)).
- **Supersedes:** the Oct 28 plan to ask for a follow-up on Thu Nov 12.
- **Not decided:** whether to adopt market-cap weighting (the method stays equal-weighted until the team decides after the feasibility check), and how transcripts are used, if at all. Both go to the Sun Nov 1 meeting.
- **Follow-ups:** Snehal sends the thank-you and proposes a date. The follow-up email also corrects "all annual" (the scores combine 10-K and 10-Q passages) and asks Mehul's strict-vs-broad question.

### 2026-11-03 — Eval checks 1, 5 and 6 run; robo-advice flagged (facts, no decision)
- **Results:** Check 1: search precision 98.9%; no clear recall miss (confirmed by Mehul). Check 5 dry run: 277/277 passages and identical scores from a fresh download (not independent; a teammate still has to run it). Check 6 replay: the rules stop invented quotes and low-confidence claims, 0 false blocks, but can't catch a confident misreading of a real quote.
- **Open for the team (not decided):** filings describe robo-advice (Schwab Intelligent Portfolios) without saying AI, so it isn't flagged. It's closest to Julie's chapter and Schwab scores 0. Counting it would change the frozen taxonomy scope, so it stays a documented limitation unless the team and Julie decide otherwise.
- **Dates (Mehul, PM):** round 2 and TP2 paragraphs Wed Nov 4; compile Thu Nov 5.
- **Decided by:** Mehul for the dates; the results are facts.

### 2026-11-04 — Bloomberg permission review cleared for the described project
- **Decision:** Logan updates the 56 Bloomberg source records in #62 to approved for the described manual download/retention, CMU-only sharing, analysis (including the described paid DeepSeek workflow), and publication of methodology/citations/derived labels and scores without transcript text.
- **Evidence:** Logan supplied Ryan Splenda's follow-up relaying that Bloomberg has no issues with the team's project and the team may proceed. Email date not supplied; November 4 is the review-update date. See `docs/part1-sourcing/transcript_review_decisions_logan.md`.
- **Decided by:** Logan (source-review decision), based on CMU Libraries' communication with Bloomberg; not a new team vote on index inclusion.
- **Supersedes:** the Bloomberg permission holds recorded October 27 and the pending library confirmation from October 29, within the described project scope only.
- **Follow-ups:** preserve CMU-only storage/sharing and no public transcript text. Provider retention/no-training guarantees are not established by this approval. Team inclusion/automation decisions and non-Bloomberg source reviews remain separate.

### 2026-11-04 — Round 2 scored; TP2 paragraphs and agent re-run merged
- **Results (facts, not decisions):** round 2 five-level Fleiss κ 0.32 (bar 0.60); Logan vs. Yen-Chu 0.67; use/no-use 0.45–0.71. The N/X rule is fixed (merging them no longer changes κ); disagreement moved to P vs. N, N vs. D1, and acronym lists. The sample targets hard cases, so it isn't like for like with round 1 ([results](../docs/part3-metrics/labeling_round_2/results_round2.md)).
- **Sector index (#97):** Yen-Chu and Shu report it's feasible on the S&P 500 Financials (~75 firms; estimated ~73 min and ~$0.40 for one year of 10-Ks and 10-Qs; size from public float via SEC's free API). Market-cap weighting is still the team's decision.
- **Agent:** `agent_labels_v1.csv` is now classify-v1.5 (#110); #35 closed. No FY2025 AI Use Score moved. The dashboard reads `company_scores_v0.csv`, so it doesn't change.
- **Dates (Mehul, PM):** check 4 rerun (#101) moved to Mon Nov 9, since it waits for adjudication.
- **Open for the team:** adjudicate the disagreements; whether transcripts go in the index (the Bloomberg permission is cleared, see the entry above; the team's Oct 25 acceptance of DeepSeek retention risk covered public SEC text only).
- **`UNCLEAR:`** Julie's follow-up: Snehal reported on the group chat that Julie is requesting 7 pm on Tuesday. Assumed Tue Nov 10, the Tuesday she offered; not confirmed.
- **Decided by:** Mehul for the date; the rest are facts or remain open.

### 2026-11-05 — Check 6 live guardrail run scored (#77)
- **Results (facts, not decisions):** Shu's live run (#117, 22 cases × guardrails off/on, `classify-v1.5`) scored per `guardrail_redteam_v0.md`. Unsafe-pass 0/18 with the guardrail, 2/18 without (the tampered outputs RT08, RT09, caught by the exact-quote check and sent to human review); false blocks 0/4 in both modes. The model handled the other 16 traps on its own, so the with/without gap is 2 cases. Details and limits: `docs/part3-metrics/check6_results.md`.
- **Wording fix:** total model spend is about $0.30 (not "under $0.30"); TP2 draft updated.
- **Open:** RT21 came back D1/ENT, the case file expects RISKM (same score); left as is unless Mehul updates the case.
- **Decided by:** facts; scored by Claude from the CSV, Mehul to confirm.

### 2026-11-07 — TP2 deadline moved to Fri Nov 13; Saturday check-in; "5 agents" is five agentic tools
- **Deadline (fact, reported not documented):** on Fri Nov 6 a teammate couldn't find the TP2 submission on Canvas. Mehul and Snehal both said the instructor moved TP2 to "next Friday" in class, and the class slide lists "Due next Friday: Lab4, Team Project #2". So TP2 is now due **Fri Nov 13, 5 pm** (was Nov 6). The syllabus file still shows the old week; check Canvas when the submission opens.
- **Re-plan (Mehul, PM):** adjudication Sun Nov 8 / Mon Nov 9 → Julie follow-up Tue Nov 10 (7 pm, unconfirmed) → check 4 rerun (#101) after adjudication → compile Thu Nov 12 → submit Fri Nov 13. TP2 can now include the Nov 10 meeting and the adjudicated labels.
- **Team check-in:** Yen-Chu, Snehal and Logan agreed (Fri Nov 6) to a quick meeting "tomorrow at 5" (Sat Nov 7, 5 pm). `UNCLEAR:` whether Mehul and Shu were asked; the Sunday Nov 8 meeting for the disagreement review is separate.
- **"5 agents" (Snehal's reminder):** the course requirement is **at least five custom agentic tools** with LLM-readable docstrings (requirement 3), not five agents. The agent has seven (`fetch_sec_filings`, `find_ai_passages`, `classify_passage`, `verify_label`, `score_companies`, `lookup_baseline`, `get_labels`). Requirement 4, a skill folder with a `SKILL.md` for the solution, has no agent skill folder yet (TP3 item).
- **Decided by:** the instructor (deadline); Mehul for the re-plan.

### 2026-11-08 — Saturday check-in held; adjudication sheet sorted
- **Facts:** the Sat Nov 7, 5 pm check-in happened (Logan, Snehal and Yen-Chu on the call per the group chat). Yen-Chu then shared `adjudication_sorted_yenchu.xlsx`: the same 58 passages and rater labels (checked against the repo sheet, no differences), sorted into 6 groups by question (acronym lists; risk talk N vs. X; P vs. N; N vs. D1/D2; D1 vs. D2; mixed) with a ~60-minute plan. No agreed labels yet. Committed in `docs/part3-metrics/adjudication/`.
- **`UNCLEAR:`** what else the Nov 7 check-in decided (no notes received); whether Mehul and Shu attended; the time of the Sunday review.
- **Decided by:** facts only.

### 2026-11-08 (later) — Julie confirmed for Tue Nov 10; agreed labels done; team call tonight
- **Julie follow-up (fact):** Snehal's calendar invite "Checkpoint 2: AI Adoption Index [Team 5]" is set for **Tue Nov 10, 7–8 pm ET** on Zoom. Julie and Dr. Chung accepted it, as did all five of us; Hengkai hasn't replied (checked in Mehul's CMU calendar, Nov 8). Snehal proposed 6:30 pm by email on Nov 2 and Nov 4 and got no email reply, so the calendar acceptance is the confirmation. This resolves the `UNCLEAR:` in the Nov 4 entry. It is the TP2 client meeting.
- **Still unanswered from Snehal's Nov 2 email:** whether the dashboard should show 10-K only or 10-K + 10-Q, and whether to show specific use cases next to each score. To ask on Tuesday ([prep](../docs/tp2/julie_nov10_prep.md)).
- **Adjudication (fact):** Snehal posted on Nov 8 that Yen-Chu, Logan and she "did the agreed labeling" at the Sat Nov 7 check-in. The filled sheet hasn't been shared, so check 4's rerun (#101) waits for it.
- **Team call:** Snehal invited the team to a Zoom check-in **Sun Nov 8, 8–9 pm** (Mehul accepted).
- **`UNCLEAR:`** whether Mehul and Shu attended on Nov 7 (Snehal's reminder tagged only Logan and Yen-Chu); anything else decided there.
- **Decided by:** facts only; scheduling by Snehal.

### 2026-11-08 (evening) — Agreed labels merged; check 4 rerun on the human consensus
- **Facts:** Yen-Chu merged the raters' agreed labels (#124; only the agreed columns changed, all 58 have an evidence level). The consensus set is 80 passages: 58 agreed + 22 with unanimous evidence (their scenarios = those at least 2 of 3 raters chose; a counting rule, not a judgment). 9 passages still need a scenario (8 agreed P + one D1 with no majority).
- **Check 4 rerun (#101):** with the 80 human labels swapped into the draft labels, FY2025 Capital One 3 → 18, Principal 0 → 18, Schwab 0 → 6, BAC 6 → 3, Citi 48 → 52. Ranking robust to weights (ρ 0.94–0.99). Drafts matched the consensus on 57/80 evidence levels; in 18 of the 23 differences people saw use or plans the draft didn't, so the draft-based scores (and the dashboard) understate use. The strict measure is no longer all zero (Principal 18). Dong vs. use score 0.58 (was 0.14), vs. talk 0.78: the talk-vs-use gap is smaller than first reported ([results](../docs/part3-metrics/check4_results.md)).
- **Open (team):** whether to re-score the dashboard on the consensus-overlaid labels (mixes human and draft labels).
- **Decided by:** facts; run by Claude for Mehul.

### 2026-11-08 (night) — Check 5 passed; dashboard polish merged; Tuesday slides
- **Check 5 (fact):** Logan, who didn't build the pipeline, reran it from a fresh clone (commit `4c3fd3e`, Python 3.12.4): 77 filings and 282 passages (the extra 3 Citi filings and 5 passages are expected), no sample text differences, identical scores, `RESULT: MATCH` (#102, closed). It covers redownloading and rescoring from saved labels, not a fresh AI-labeling run ([results](../docs/part3-metrics/check5_rerun.md)).
- **Dashboard (fact):** Snehal's #126 merged (click-to-open metric definitions, FY2026 hidden, tidier story tab; 30 tests pass). It doesn't change scores, so the dashboard still shows the draft-label scores.
- **Tuesday (fact):** Snehal put a slide deck copy in the team Drive (client materials → TP2 checkpoint folder) for everyone to add slides; the agenda is a doc and the email to Julie goes out Mon morning. Logan can't join the Sun Nov 8 call and asked to be synced in the chat.
- **Open (team, tonight):** Snehal asked whether to put the agreed labels into the dashboard. Mehul's suggestion: yes, after the raters fill the 9 missing scenarios (Mon noon); Claude reruns the scores and Snehal points the dashboard at them with a note that 80 of 277 passages are human-checked.
- **Decided by:** facts only.

### 2026-11-08 (meeting) — Team call: transcripts out, both index weightings, Tuesday plan
Source: [minutes](../meetings/2026-11-08-internal.md) (filled capture form + Zoom transcript; Logan absent).
- **Transcripts:** earnings-call transcripts are **left out of the index** and listed as future work (option A). Bloomberg stays cleared for team use only. This settles the open question from Nov 4; #34 can close or move to future work. Julie may still comment on Tuesday.
- **Sector index:** show **both** equal-weighted and market-cap-weighted. Market cap comes from each 10-K's aggregate market value. Yen-Chu builds the calculation; on Tue Nov 10 we explain the plan and the high-level pipeline (Shu adds 1–2 slides); dashboard integration comes after Tuesday.
- **Dashboard:** switches to the human-agreed labels after the raters' Monday-noon scenarios. Hosting: **Streamlit Community Cloud** (#30).
- **Tuesday:** agenda and questions accepted, plus "definition of done" for handover. No practice run (midterms). We record the meeting. Slides in by Mon night.
- **TP2:** owners confirmed (section 6 Snehal Wed; Mehul compiles, trims to 1–3 pages and takes the board snapshot Thu; Yen-Chu submits Fri 5 pm and checks Canvas Mon).
- **TP3:** Mehul drafts SKILL.md and Shu reviews it. For the paper discussion, first find the expectations (and ask Dr. Chung), then Mehul splits it with the other handover tasks.
- **DeepSeek:** fine to use (Dr. Chung's in-person OK, per Logan's Oct 27 message); the email confirmation is still not in the repo.
- **Open:** handover scope (the repo includes internal notes), where the data lives (CSV in GitHub now; Supabase suggested, Shu thinks it isn't needed), who links the agent to the dashboard, and whether to auto-refresh. Ask Julie Tuesday, then Dr. Chung.
- **Decided by:** the team on the call (Mehul, Snehal, Yen-Chu, Shu).

### 2026-11-09 — Raters' scenarios added; check 4 updated
- **Facts:** at the end of the Nov 8 call the raters added scenarios for 7 of the 9 passages (#128, Yen-Chu; codes from the rater columns). Still missing: `BAC_2025-12-31_10-K_00264` (P) and `SCHW_2024-12-31_10-K_00562` (D1). Check 4 rerun (#129): FY2025 Citi 53, Capital One 20, Principal 18, Wells Fargo 11, JPMorgan 6, Schwab 6, BofA 3; ranking robust (ρ 0.99–1.00); conclusions unchanged. `data/processed/sec/company_scores_consensus.csv` is ready for the dashboard.
- **Decided by:** facts; run by Claude for Mehul.

### 2026-11-10 (meeting) — Julie follow-up: broad headline, category detail, 10-K check, handover via Dr. Chung
Source: [minutes](../meetings/2026-11-10-client.md) (Zoom transcript; the opening section isn't recorded).
- **Headline measure:** broad AI Use Score as the headline, strict (specific use only) beside it. Julie agreed to the team's proposal.
- **Use cases:** no detail beyond the category codes next to each score; filings aren't detailed enough and transcripts are out. Settles her Nov 2 question.
- **10-K vs. 10-Q:** Julie prefers 10-Ks only. The team first runs a quick check of what the 10-Qs add; if nothing material, scores move to 10-K only. Until then the scores still combine both (each category counted once a year).
- **Dashboard:** keep the metric drop-down; add a download of the firm × year scores (CSV; format is the team's choice) and a visible explanation of the scoring method.
- **Handover:** Julie defers to Dr. Chung's preference. The team committed to a deployed link and a user guide; Julie was positive about the code being on GitHub for others to adapt.
- **Also:** Julie wants the research comparison (TP3 paper) shared with her, and will join the Dec 3 presentation remotely (syllabus slot 5:00–6:20 pm ET, to confirm). Mehul corrected the human-review threshold to 0.70 (Oct 29 said 0.3).
- **Open:** Julie may adjust the cap-weighting after Yen-Chu's worked example; the transcripts-out decision needs restating in the follow-up email (Julie asked whether Bloomberg would be added).
- **Decided by:** Julie (client), on the team's proposals.
