# How we worked: board, repo and meetings (TP3 talking point, DRAFT)

> **Owner:** Mehul (PM). **Status:** draft v0.1, Nov 19. For the poster/deck (#141), the 1-minute "how we used the board" point, and a short "How we worked" part of the README (#166). Refresh the numbers on Dec 1.

**One-line version for the talk:** every task was a GitHub issue with one owner and a date, every change went through a reviewed pull request, and every meeting ended up in the repo, so anyone could see who was doing what at any moment.

## The board
- **Public kanban board** ([link](https://github.com/users/MehulPardeshi/projects/1)): To Do → In Progress → Done, used from TP1 to Dec 3.
- **Two milestones:** "Sprint: Oct 18–Nov 13 (TP2)", closed when TP2 was submitted, and "TP3: Nov 14–Dec 3".
- **One owner and a target date per issue**, with @mentions so GitHub notifies people; a pinned issue (#45) lists who does what and is rewritten after every meeting.
- As of Nov 19: **57 issues**, 38 closed.

## The repo
- **Changes reach `main` only through pull requests: 112 merged so far, from all five of us.**
- **Automatic checks on every pull request:** the branch must include the latest `main`, and no secrets or raw data may be committed. Local git hooks stop a commit or push straight to `main`, because most of us were new to git.
- **A daily "open work" issue (#15)** lists open pull requests and branches nobody has finished.
- **Tests:** 80 automated tests run offline (mock model, fake EDGAR).

## Meetings and decisions
- **8 meetings in the repo** (3 with Julie, 5 team calls), each filed from a capture form or transcript into `meetings/`.
- **Decisions log** (`memory/09-decisions-log.md`) and **action items** (`memory/11-action-items.md`) are updated after each meeting, so the board, the pinned issue and the docs say the same thing.
- **AI-assisted project management:** we used Claude Code to file minutes, keep the board in sync and check pull requests; people made every decision and produced every human label (no AI-written rater labels).

## What we'd keep / change
- **Keep:** one owner per task; minutes in the repo; checks that block a bad merge.
- **Change:** set target dates when a task is created, not later; agree the second rater for each labeling round at the meeting.
