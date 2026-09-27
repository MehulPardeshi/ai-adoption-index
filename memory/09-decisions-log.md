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
