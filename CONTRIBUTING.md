# Contributing

## Before you start
1. Read [`memory/09-decisions-log.md`](memory/09-decisions-log.md), then `memory/00`–`10`.
2. Check the **shared spreadsheet** to see what you own and when it's due ([`docs/TASK_TRACKER.md`](docs/TASK_TRACKER.md)).
3. Non-coders: [`ONBOARDING_FOR_NON_CODERS.md`](ONBOARDING_FOR_NON_CODERS.md) walks you through everything.

## Branches and pull requests
- **Don't commit directly to `main`.** Create a branch named `<your-name>/<short-topic>`, e.g. `logan/firm-universe-recordkeepers`.
- Open a pull request (PR) and link the issue it addresses (write `Closes #<n>` in the PR description).
- **At least one teammate reviews** before merging. For deliverable docs (ethics memo, taxonomy, metrics, methodology), prefer two reviewers.
- Keep PRs small, and don't mix unrelated changes.

## What goes where
| You're changing… | Put it in… |
|---|---|
| A graded deliverable draft | `docs/partX-…/` |
| A team decision (role, tool, definition, date) | Append to `memory/09-decisions-log.md` (never edit old entries) |
| Background context agents should know | The relevant `memory/0X-….md` file |
| Code | `src/<module>/` |
| Exploration | `notebooks/` (clear large outputs before committing) |
| Raw downloaded text | `data/raw/`, which is **gitignored**. Never force-add it. |

## Rules that protect our grade
- **Taxonomy and metrics are team-derived.** Don't let an AI agent "finalize" them. Drafts stay marked DRAFT until the team votes.
- **Never commit secrets.** API keys go in `.env` (gitignored); `.env.example` shows the variable names only.
- **Never commit licensed or paywalled text.** Cite and paraphrase instead (see the ethics memo).
- **Cite AI assistance** in submitted deliverables, per the course's GenAI policy (syllabus).
- **Log decisions.** If it was decided in a meeting or by a WhatsApp vote, it goes in `09-decisions-log.md` the same day.

## Commit messages
Write in the imperative and keep it short: `Add recordkeeper firms to universe`, `Draft IRR sample plan`.

## GitHub Project board
The course grades a **kanban board** (TP3: 7%; TP1 must link to it; TP2 needs a snapshot).

**Status (2026-09-27):** ❌ **Not created yet.** Automated creation failed because the `gh` token lacks the `project` scope. The Week 1–6 issues (#1–#6) and the course-requirements checklist (#7) already exist. Once the board is created, log its link in `memory/09-decisions-log.md` and update this line.

To create it manually:

1. Go to github.com → your profile (or the repo) → **Projects** tab → **New project**.
2. Choose the **Board** template and name it **"AI Adoption Index"**.
3. Make sure the **Status** field has the columns **To Do**, **In Progress**, and **Done** (rename "Todo" if needed).
4. In the project's **⋯ → Settings → Manage access**, add all five teammates as **Write** collaborators. The repo also needs them as collaborators: repo **Settings → Collaborators**.
5. Link it to the repo: repo → **Projects** tab → **Link a project**.
6. Add the Week 1–6 milestone issues: in the board, click **+ Add item** → type `#` → pick each issue.
7. Optional: enable the built-in workflows (**⋯ → Workflows**) so closed issues move to Done automatically.

CLI alternative (the token needs the `project` scope first):
```bash
gh auth refresh -s project,read:project
```
```bash
gh project create --owner MehulPardeshi --title "AI Adoption Index"
```
Then do steps 3–7 in the web UI (the CLI can't switch a view to Board layout).
