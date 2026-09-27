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
**➡️ Spreadsheet: `TODO — paste link here once created`**

Once the spreadsheet exists, paste the link above **and** add a dated entry to [`memory/09-decisions-log.md`](../memory/09-decisions-log.md).

## Rules of thumb
1. **Ownership conflict?** The spreadsheet wins. Update the GitHub issue's assignee to match.
2. **New engineering task found mid-build?** Open a GitHub issue. If it's big enough to affect a deadline, also add a spreadsheet row.
3. **Missed deadline?** Follow the conflict-resolution steps in [`memory/02-team-norms.md`](../memory/02-team-norms.md). The backlog item goes on *both* trackers.
4. **Each week-milestone issue** (Week 1–6) links to its `docs/partX` folder, which is where the actual work product lives.

## GitHub Project board
- **Link:** https://github.com/users/MehulPardeshi/projects/1
- Columns: **To Do / In Progress / Done**
- Setup steps and status: see [`CONTRIBUTING.md`](../CONTRIBUTING.md#github-project-board)
