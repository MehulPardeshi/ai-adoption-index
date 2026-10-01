# meetings/: minutes of every meeting

Every team or client meeting is recorded with the **Gemini note-taker**. Afterwards, **someone uploads the Gemini notes to an AI tool** (Claude Code, Cursor or Codex), which files them here and updates the rest of the repo. That keeps every teammate's AI tool up to date on decisions and on who's doing what.

## After every meeting (person uploading the notes)
1. Export or copy the Gemini notes (summary + transcript if available).
2. Open the repo in your AI tool and **just paste or attach the notes**. No special wording needed: the tool recognizes meeting notes (and a filled-in meeting capture form) and processes them automatically. Adding a line like "notes from today's client meeting" helps it label the meeting type.
3. Review the pull request the AI opens, then merge it.
4. Copy any new or changed task rows into the shared **spreadsheet**. It's still the source of truth for owners and deadlines; the AI tool can't edit it.

## What the AI tool must do (processing procedure)
**Trigger:** the user shares content that looks like meeting notes, minutes, a transcript, a Gemini summary, or a filled-in capture form (e.g. `docs/tp1/Kickoff_Capture_Form_*.docx`), **even with no instructions**. Briefly confirm ("Looks like minutes from the <date> meeting; filing them now"), then:

1. **Branch:** `git pull` on main, then create `<name>/minutes-YYYY-MM-DD`.
2. **File the minutes:** create `meetings/YYYY-MM-DD-<internal|client|setup>.md` from [`_TEMPLATE.md`](_TEMPLATE.md). Fill every section from the notes. **Don't invent anything.** If the notes are unclear about an owner, date or decision, write `UNCLEAR:` and list it under *Open questions*. Keep the raw Gemini notes in a collapsed `<details>` block at the bottom.
3. **Decisions → [`memory/09-decisions-log.md`](../memory/09-decisions-log.md):** append one entry per real decision (append-only, newest at the bottom). Only things the team or client actually decided; a suggestion is not a decision.
4. **Tasks → [`memory/11-action-items.md`](../memory/11-action-items.md):** add new tasks under each owner, move finished ones to *Completed*, and update *Next steps*.
5. **Ripple updates, only where the meeting changed something:**
   - Role confirmed? Set `Role status:` in that person's `team/` profile and update `memory/01-team-and-roles.md`.
   - Client answers? Update the relevant `memory/0X` file and `docs/tp1/project_scope.md`.
   - New engineering work? Open GitHub issues titled `[<task ID>] …`.
6. **Pull request:** title it `Minutes: <date> <type>`. In the description, list every file changed, and the rows the human must copy into the spreadsheet.
7. **Never** finalize the taxonomy or metrics from minutes (they're team-derived and graded), and never assign a role or task that the notes don't actually show someone agreeing to.

## Open pull requests: reminders, not blocks
- Your AI tool reminds you of your open PRs (and pushed branches without a PR) at the start of every session.
- A daily GitHub Action (`.github/workflows/open-work-reminder.yml`) pings the author of any PR open for **more than 2 days**, and keeps one issue, **"📋 Open work reminder"**, listing all open PRs and stray branches. The PM checks it at the Sunday reconcile.
- We don't *block* new PRs while one is open: a PR is often just waiting for a reviewer, and people legitimately work on two things at once.

## Asking "what should I work on?"
Any teammate can ask their AI tool: `I'm <name>. Based on memory/11-action-items.md and the latest file in meetings/, what are my open tasks and what should I do next?`
