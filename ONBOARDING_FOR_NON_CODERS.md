# Onboarding for Non-Coders

**You don't need to know how to code to contribute here.** AI coding tools (Cursor, Claude Code, Codex) can read this whole project, explain it, and help you write documents *or* code. This repo has a `/memory/` folder written specifically so those tools understand our project the moment you open it.

---

## Step 0: Get access (one time)
1. Make a free GitHub account if you don't have one, and send your username to the PM so you get added to the repo.
2. Accept the invite email from GitHub.
3. Install **one** of the tools below.

## Step 1: Open the project in an AI tool

### Option A: Cursor (the easiest if you like a visual editor)
1. Download Cursor from cursor.com and sign in.
2. On the start screen, click **Clone repo** and paste the repo URL (the PM will share it). Pick a folder to save it in.
3. Open the chat panel (**Cmd+L** on Mac, **Ctrl+L** on Windows).
4. Cursor automatically loads our rules file (`.cursor/rules/project-context.mdc`), which tells it to read `/memory/`.

### Option B: Claude Code (a terminal or desktop app)
1. Install Claude Code (see the Claude Code docs), or use the Claude desktop app's **Code** tab.
2. Clone the repo. In a terminal:
   ```bash
   git clone <repo-url>
   ```
3. Open the folder in Claude Code. It automatically reads `CLAUDE.md`, which tells it to read `/memory/`.

### Option C: Codex (OpenAI)
1. Install the Codex CLI or use the Codex app, and sign in.
2. Clone the repo as above and open the folder. Codex reads `AGENTS.md`, which points to `/memory/`.

## Step 2: Your first prompt (copy and paste this)

```
Read /memory/ in order, then tell me what I could help with given my role options in 01-team-and-roles.md
```

Add your name at the end, e.g. "…given my role options in 01-team-and-roles.md. I'm Logan."

---

## Example prompts: non-technical tasks

**Finding taxonomy example sentences**
```
I'm reading JPMorgan's 2024 10-K for our taxonomy work. Here is a passage: <paste passage>. Which sentences describe a concrete AI use case, and which are vague? Don't assign final categories. Just explain what each sentence says, so I can decide myself.
```

**Drafting the ethics memo**
```
Help me draft section 2 (robots.txt and Terms of Service review) of docs/part1-sourcing/ethics_memo.md for SEC EDGAR. Tell me exactly which pages I should check myself and what to look for. Leave clearly marked placeholders wherever I need to verify something.
```

**Reviewing a metric definition**
```
Read docs/part3-metrics/metrics.md and memory/05-metrics-draft.md. Our team is considering "AI mention density". What are the ways this metric could mislead us, especially comparing a 10-K to a press release? Give me questions to bring to our next team meeting, not a final definition.
```

**Prepping for the client meeting**
```
Using memory/00 through 08, draft 5 questions we should ask the client on Thursday about the retirement recordkeeper sector and what she needs for the book chapter.
```

## Example prompts: technical tasks

**Implementing an EDGAR client**
```
Check memory/09-decisions-log.md to confirm the team has approved EDGAR tooling. Then, in src/edgar/, implement a small client that looks up a company's CIK and lists its 10-K and 10-Q filings using the SEC's official JSON APIs. Read the User-Agent from .env, stay under the SEC's rate limit, and add docstrings an LLM agent could read. Explain each step as you go. I'm learning.
```

**Building a dashboard chart**
```
Read memory/07-dashboard-spec.md and docs/part5-dashboard/dashboard_spec.md. Using the dashboard tool recorded in 09-decisions-log.md, build view #1 (index trend line per firm + peer average) using clearly labeled FAKE sample data, so we can review the layout before real data exists.
```

---

## Ground rules (the tools know these too, but you should as well)
- **The taxonomy and metrics are ours to derive.** If an AI tool offers to "finalize the taxonomy" or "write the scoring logic," say no until the team has voted. Part 2 and Part 3 are graded on *us* doing this from real documents.
- **Record decisions.** After a meeting, append to `memory/09-decisions-log.md` (you can ask the AI: *"Add a decisions-log entry for: …"*).
- **Check what it writes.** AI tools make confident mistakes, especially about finance facts and citations. Verify against the source.
- **Cite AI help** in anything we submit (course policy).
- **Never paste API keys or passwords into chat.** They go in `.env` only.
- **Saving your work** (the AI tool can do this for you if you ask): *"Create a branch called <yourname>/<topic>, commit my changes, push, and open a pull request."*
