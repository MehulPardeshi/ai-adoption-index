# Contributing

## Before you start
1. Read [`memory/09-decisions-log.md`](memory/09-decisions-log.md), then `memory/00`–`10`.
2. Check the **shared spreadsheet** to see what you own and when it's due ([`docs/TASK_TRACKER.md`](docs/TASK_TRACKER.md)).
3. Non-coders: [`ONBOARDING_FOR_NON_CODERS.md`](ONBOARDING_FOR_NON_CODERS.md) walks you through everything.

## Git guardrails (because GitHub's own branch protection needs a paid plan on private repos)
| Layer | What it does | Where |
|---|---|---|
| **Local git hooks** | Refuse commits on `main`; refuse commits when your branch is missing new commits from `main`; refuse pushes to `main` | `.githooks/`, turned on per clone with `git config core.hooksPath .githooks` |
| **AI-tool rules** | Cursor, Claude Code and Codex are told to install the hooks, pull first, work on a branch, and never push to `main` | `CLAUDE.md`, `AGENTS.md`, `.cursor/rules/project-context.mdc` |
| **PR checks (GitHub Actions)** | A red ❌ on any PR that's behind `main` (fix: click **Update branch**) or that commits `.env`, raw data, or the signed contract | `.github/workflows/pr-checks.yml` |

**Rule for reviewers:** don't merge a PR with a red ❌. The checks can't physically block the merge until branch protection is on (see below), so this relies on us.

**Upgrade path:** if the repo owner gets **GitHub Pro** (free with the GitHub Student Developer Pack, education.github.com), turn on branch protection for `main`: require a pull request, require the two PR checks to pass, and require branches to be up to date. That makes the rules impossible to skip.

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

**Board:** https://github.com/users/MehulPardeshi/projects/1 (private; linked to this repo)

**Status (2026-09-27):** ✅ Created. It has a **Board** view (columns **To Do / In Progress / Done**) and a **Table** view. Issues #1–#7 start in To Do.

**Still to do by hand (web UI):**
1. **Share the board with teammates:** project **⋯ → Settings → Manage access** → add each teammate as **Write**. Being a repo collaborator does *not* automatically give access to a private user-owned project.
2. **Check the automations:** **⋯ → Workflows** → make sure "Item closed" and "Pull request merged" set Status to **Done**, and "Item added" sets **To Do**. The columns were renamed, so re-select the target option if a workflow shows a blank value.

**Recreating the board from scratch** (only if it's ever deleted):
1. Repo → **Projects** tab → **New project** → **Board** template → name it **"AI Adoption Index"**.
2. Rename the Status options to **To Do / In Progress / Done**.
3. Link it to the repo, and add issues with **+ Add item** → `#`.

CLI alternative (the token needs the `project` scope first):
```bash
gh auth refresh -s project,read:project
```
```bash
gh project create --owner MehulPardeshi --title "AI Adoption Index"
```
Then finish the setup in the web UI.
