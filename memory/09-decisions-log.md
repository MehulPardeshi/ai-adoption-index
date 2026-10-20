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
