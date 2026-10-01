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
