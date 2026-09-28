# Task Tracking: Two Complementary Systems

The team contract says work is tracked in a **shared spreadsheet**. The course also requires a **GitHub kanban board**. We use both, for different jobs. **Neither replaces the other.**

| | Shared spreadsheet | GitHub Issues + Project board |
|---|---|---|
| **Purpose** | High-level: **who owns what, by when** | Granular: engineering tasks and bugs that come up during the build |
| **Granularity** | Deliverables and major tasks (e.g., "Ethics memo draft") | Sub-tasks (e.g., "EDGAR client: handle 429 rate-limit responses") |
| **Authority** | ✅ **Source of truth for ownership and deadlines** (contract-mandated) | Sits underneath the spreadsheet. Owner shows **TBD** until the spreadsheet assigns it |
| **Who updates it** | Everyone; reviewed at Sunday meetings | Whoever is working the task |
| **Graded?** | Part of team process | **Yes:** the kanban board is graded in TP3 (7%) and a snapshot goes in TP2 |

## Shared spreadsheet link
**➡️ Tracker (Excel Online, CMU OneDrive):** https://andrewcmu-my.sharepoint.com/:x:/g/personal/mppardes_andrew_cmu_edu/IQBkCeheAvmPSrU1SkxKTJkZAdr85cdpnKE8PpNSuGpDSG4?e=OGs7Ky

Tabs: **README / Tasks / Roles / Meetings**. The original format lives in [`docs/tracker/team_tracker.xlsx`](tracker/team_tracker.xlsx). **The online sheet is the live version.** The .xlsx is only the starting template and is not kept up to date.

## Keeping the spreadsheet and GitHub in sync
They track **different levels** of work, so they don't need to mirror each other row for row. They connect through links:

1. **The spreadsheet links down.** When a spreadsheet task has engineering work under it, paste the GitHub issue URL in its **GitHub issue** column.
2. **GitHub links up.** When an issue belongs to a spreadsheet task, put the task ID in the issue title, e.g. `[T11] Draft scope doc`.
3. **Whoever changes a status updates both.** Closing an issue that finishes a spreadsheet task means setting that row to **Done** too. (Closed issues move to **Done** on the board automatically.)
4. **Weekly reconcile at the Sunday meeting (PM, ~5 min):** open the board and the Tasks tab side by side and fix mismatches: owners, statuses, missing links.
5. **Ownership conflict?** The spreadsheet wins.

Optional automation (not set up): Microsoft Power Automate, which CMU provides through Microsoft 365, can add a Tasks row whenever a GitHub issue is opened. It is one-way only, needs the Tasks tab formatted as an Excel table, and the GitHub connector may require a license CMU doesn't include. Only worth trying if the manual routine above starts slipping.

## Rules of thumb
1. **Ownership conflict?** The spreadsheet wins. Update the GitHub issue's assignee to match.
2. **New engineering task found mid-build?** Open a GitHub issue. If it's big enough to affect a deadline, also add a spreadsheet row.
3. **Missed deadline?** Follow the conflict-resolution steps in [`memory/02-team-norms.md`](../memory/02-team-norms.md). The backlog item goes on *both* trackers.
4. **Each week-milestone issue** (Week 1–6) links to its `docs/partX` folder, which is where the actual work product lives.

## GitHub Project board
- **Link:** https://github.com/users/MehulPardeshi/projects/1
- Columns: **To Do / In Progress / Done**
- Setup steps and status: see [`CONTRIBUTING.md`](../CONTRIBUTING.md#github-project-board)
