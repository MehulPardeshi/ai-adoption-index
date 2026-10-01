# CLAUDE.md

Before doing **any** work in this repo:

1. Read [`memory/09-decisions-log.md`](memory/09-decisions-log.md) **first**. It overrides everything else in `/memory/`.
2. Then read the rest of [`/memory/`](memory/) in numeric order: `00` → `11`. `11-action-items.md` shows who is doing what right now.
3. **Given meeting notes or minutes?** Follow [`meetings/README.md`](meetings/README.md).

Everything project-specific (context, team, norms, scope limits, deliverables) lives in `/memory/`. It is not repeated here.

## Git safety rules (always follow; teammates are new to git)

At the **start of every session**, before editing anything:
1. Run `git config core.hooksPath .githooks` (it turns on the team guardrails; safe to repeat).
2. Run `git fetch origin`. If the user has no uncommitted work, `git switch main && git pull`.
3. Never edit on `main`. Create or switch to a branch named `<name>/<topic>` first.

**Before every commit and push:** run `git pull origin main` into the current branch and resolve any conflicts *with the user*, explaining them in plain language.

**Never** commit or push directly to `main`, force-push, or use `--no-verify`. Changes reach `main` only through a pull request.
