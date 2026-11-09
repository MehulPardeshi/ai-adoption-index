# AI Adoption Index: Financial Services

**A quarterly index of how financial services firms describe and use AI. It is built only from public, legally accessible sources (SEC 10-K/10-Q filings) and shown on an interactive dashboard.**

> Public repo. Julie Agnew gave permission on Oct 1, 2026 to name her and the book chapter ([minutes](meetings/2026-10-01-client.md)). No transcript text, licensed material, Zoom links or private emails go in this repo.

- **Course:** 95-891 Introduction to AI, CMU Heinz College, Fall 2026, Section C. Team 5 / Project 5. TA: Hengkai Zheng.
- **Client:** Julie Agnew, William & Mary. The dataset feeds a book chapter on **AI in retirement**, so retirement plan providers and recordkeepers are the primary sector.
- **Central caveat:** *mentioning* AI in a filing is not the same as *using* AI. The index scores evidence of use, and a person checks the AI's labels.

## 👋 Start here (everyone)
1. **What should I do?** See the pinned issue [#45 "Who does what"](https://github.com/MehulPardeshi/ai-adoption-index/issues/45) or [`memory/11-action-items.md`](memory/11-action-items.md). Each task is an issue on the [project board](https://github.com/users/MehulPardeshi/projects/1).
2. **What happened lately?** Read the newest file in [`meetings/`](meetings/). Or ask your AI tool: *"Read memory/09 and 11, and tell me what changed on main since <date>."*
3. **Using Claude Code, Cursor or Codex?** It reads [`CLAUDE.md`](CLAUDE.md) / [`AGENTS.md`](AGENTS.md) automatically. It turns on the team guardrails, keeps you off `main` and opens PRs for you. New to this? See [`ONBOARDING_FOR_NON_CODERS.md`](ONBOARDING_FOR_NON_CODERS.md).
4. **Changing something?** Make a branch `<yourname>/<topic>`, then open a pull request. Never push to `main`. Details: [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Where we are (Nov 9, 2026)
| Milestone | Status |
|---|---|
| TP1: project scope | ✅ submitted Oct 2 |
| Categories (taxonomy) | ✅ frozen Oct 27 ([codebook](docs/part2-taxonomy/taxonomy.md)) |
| Labels: 80 passages × 3 raters, agreed labels for the 58 disagreements | ✅ Nov 7 |
| Agent (DeepSeek, 7 tools, guardrails) | ✅ runs end to end; round 2 + ~75-firm run in progress (#133) |
| All 6 evaluation checks | ✅ done ([evaluation plan](docs/part3-metrics/evaluation_plan.md)) |
| Dashboard (Streamlit) | ✅ prototype; switching to the human-agreed scores (#132); hosting on Streamlit Community Cloud (#30) |
| Sector index (equal- and market-cap-weighted) | 📋 plan for Julie on Tue Nov 10; build after (#134) |
| **Julie follow-up** | **Tue Nov 10, 7 pm ET** ([prep](docs/tp2/julie_nov10_prep.md)) |
| **TP2: progress report** | **due Fri Nov 13, 5 pm** ([draft](docs/tp2/progress_report_draft.md)) |
| **TP3: final presentation, paper discussion, SKILL.md, handover** | **Thu Dec 3** ([plan and split](docs/tp3/paper_discussion_plan.md)) |

**Current scores (FY2025, human-agreed labels):** Citi 53 (benchmark), Capital One 20, Principal 18, Wells Fargo 11, JPMorgan 6, Schwab 6, Bank of America 3. Ranking is stable (ρ 0.99–1.00). See [check 4](docs/part3-metrics/check4_results.md).

## Setup (5 minutes)
```bash
git clone https://github.com/MehulPardeshi/ai-adoption-index.git
cd ai-adoption-index
git config core.hooksPath .githooks          # team guardrails (stops commits/pushes to main and out-of-date branches)
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env                          # only needed for the agent: add DEEPSEEK_API_KEY (ask Shu)
```

## Common commands (run from the repo root)
| I want to… | Command |
|---|---|
| Open the dashboard | `python3 -m streamlit run src/dashboard/app.py` |
| Run all tests (offline, no key) | `python3 -m unittest discover -s tests -t .` |
| Download SEC filings | `python3 -m src.edgar.download_sec_filings` |
| Run the agent on passages | `python3 -m src.agent.run_batch --tickers JPM,COF --year 2025 --forms 10-K` |
| Try the agent without a key | `AGENT_LLM_PROVIDER=mock python3 -m src.agent.run_batch --limit 20` |
| Ask the agent a question | `python3 -m src.agent.chat --trace "How does JPMorgan use AI in FY2025?"` |
| Rebuild the agreed labels | `python3 -m src.eval.make_consensus_labels` |
| Compare the agent with the agreed labels (check 3) | `python3 -m src.eval.check3_consensus` |
| Score companies | `python3 -m src.index.score_companies --labels docs/part3-metrics/adjudication/labels_v0_plus_consensus.csv --out data/processed/sec/company_scores_consensus.csv` |
| Check how robust the ranking is | `python3 -m src.eval.check4_sensitivity --labels docs/part3-metrics/adjudication/labels_v0_plus_consensus.csv` |

The full refresh routine (download → agent → human review → score → dashboard → check) is in the skill file [`skills/ai-adoption-index/SKILL.md`](skills/ai-adoption-index/SKILL.md). Agent details are in [`docs/part6-agent/agent_design.md`](docs/part6-agent/agent_design.md).

## Where things live
| Folder | What's in it |
|---|---|
| [`memory/`](memory/) | Project memory for humans and AI tools. **Read [`09-decisions-log.md`](memory/09-decisions-log.md) first**, then `00`–`11`. |
| [`meetings/`](meetings/) | Minutes of every meeting. Give your AI tool a capture form or notes and it files them ([how](meetings/README.md)). |
| [`docs/part1-sourcing/`](docs/part1-sourcing/) | Data sources + ethics memo (Logan) |
| [`docs/part1.5-firm-universe/`](docs/part1.5-firm-universe/) | Which firms, by sector |
| [`docs/part2-taxonomy/`](docs/part2-taxonomy/) | The codebook: categories and scoring rules |
| [`docs/part3-metrics/`](docs/part3-metrics/) | Metrics, rater agreement, the 6 evaluation checks, red-team tests |
| [`docs/part4-index/`](docs/part4-index/) | Index method + refresh protocol |
| [`docs/part5-dashboard/`](docs/part5-dashboard/) | Dashboard spec |
| [`docs/part6-agent/`](docs/part6-agent/) | Agent design, runs, prompt tuning |
| [`docs/tp1/`](docs/tp1/) · [`docs/tp2/`](docs/tp2/) · [`docs/tp3/`](docs/tp3/) | Course submissions: scope, progress report + Julie prep, final (paper plan, Responsible AI) |
| [`docs/reviews/`](docs/reviews/) · [`docs/source-materials/`](docs/source-materials/) | Paper reviews; the client brief, syllabus and course instructions |
| [`skills/ai-adoption-index/`](skills/ai-adoption-index/) | SKILL.md (TP3 requirement): how anyone, or any AI tool, refreshes the index |
| [`src/`](src/) | Code: `edgar/` downloads, `agent/` the AI agent, `eval/` checks, `index/` scoring, `dashboard/` the app |
| [`data/processed/`](data/processed/) | Scores and labels the dashboard reads. `data/raw/` stays local (gitignored) |
| [`tests/`](tests/) | Offline tests (no API key needed) |
| [`team/`](team/) | One profile per teammate |

## Team and roles
| Member | Role | GitHub |
|---|---|---|
| Mehul Pardeshi | Project Manager + Responsible AI + Evaluation lead | @MehulPardeshi |
| Yen-Chu Chen | Dataset Builder (SEC data, sector index) | @teddy0-0y |
| Logan Mai | Market & User Researcher (ethics memo, research paper) | @MaiJialong |
| Shu Pu | AI Engineer / Solution Architect (agent) | @seanpushu |
| Snehal Paliwal | Dashboard Product Manager + client communication | @snehalpaliwal |

Roles confirmed Oct 1 ([`memory/01-team-and-roles.md`](memory/01-team-and-roles.md)).

## How we track work
- **Issues + [project board](https://github.com/users/MehulPardeshi/projects/1)**, grouped by milestone: "Sprint: Oct 18–Nov 13 (TP2)" and "TP3: Nov 14–Dec 3 (final)".
- **Shared spreadsheet:** owners and deadlines (source of truth, per the team contract). See [`docs/TASK_TRACKER.md`](docs/TASK_TRACKER.md).

## Grading
- **Client brief:** sourcing/ethics memo 10% · taxonomy + rater agreement 20% · metrics write-up 20% · backfilled dataset 20% · dashboard 20% · final presentation 10%.
- **Course:** TP1 (Oct 2), TP2 (Nov 13), final presentation (Dec 3), with agentic-AI technical requirements. See [`memory/08-deliverables-and-rubric.md`](memory/08-deliverables-and-rubric.md).
