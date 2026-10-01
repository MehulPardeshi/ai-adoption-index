---
name: process-meeting-notes
description: File Gemini (or other) meeting notes into the AI Adoption Index repo, updating the decisions log, action items, roles and TP docs. Use whenever someone pastes or attaches meeting minutes, a meeting transcript, or says "process these notes".
---

Follow the procedure in `meetings/README.md` ("What the AI tool must do") exactly. Steps:
1. Pull main and branch.
2. Create `meetings/YYYY-MM-DD-<type>.md` from `meetings/_TEMPLATE.md`.
3. Append decisions to `memory/09-decisions-log.md`.
4. Update `memory/11-action-items.md`.
5. Ripple updates only where the meeting changed something.
6. Open a PR listing the spreadsheet rows the human must copy.

Never invent owners, dates or decisions; mark them `UNCLEAR:`. Never finalize the taxonomy or metrics.
