# AI Adoption Index: Financial Services

**A living, quarterly-updated index of how financial services firms talk about and deploy AI, built only from public, legally accessible sources and shown on an interactive dashboard.**

> 🔒 Private repo. Client identity is confidential by default under the course's policy. **Get the client's permission before making this repo public or naming the client in the final README.**

## Context
- **Course:** 95-891 Introduction to AI, CMU Heinz College, Fall 2026, Section C. Team 5 / Project 5.
- **Client:** Julie Agnew, William & Mary. The dataset feeds a book chapter on **AI in retirement**, so **retirement plan providers/recordkeepers are the primary sector**.
- **Central caveat:** *mentioning* AI in a filing is not the same as *using* AI.

## The five parts
| Part | What | Working docs |
|---|---|---|
| 1 | Data sourcing (legal and ethical) + ethics memo | [`docs/part1-sourcing/`](docs/part1-sourcing/) |
| 1.5 | Firm universe by sector (retirement = primary) | [`docs/part1.5-firm-universe/`](docs/part1.5-firm-universe/) |
| 2 | Categorization taxonomy, **derived from real documents** | [`docs/part2-taxonomy/`](docs/part2-taxonomy/) |
| 3 | Metrics design + inter-rater reliability | [`docs/part3-metrics/`](docs/part3-metrics/) |
| 4 | Index construction, backfill, refresh protocol | [`docs/part4-index/`](docs/part4-index/) |
| 5 | Interactive dashboard | [`docs/part5-dashboard/`](docs/part5-dashboard/) |

Source briefs: [`docs/source-materials/`](docs/source-materials/)

## Rubric (client assignment brief)
| Deliverable | Weight |
|---|---|
| Sourcing/ethics memo | 10% |
| Taxonomy + inter-rater reliability results | 20% |
| Metrics methodology write-up | 20% |
| Backfilled dataset (8+ quarters × chosen firms) | 20% |
| Dashboard | 20% |
| Final presentation defending design choices | 10% |

6-week timeline: Wk1 source review/ethics memo/firm universe, Wk2 draft taxonomy, Wk3 metrics + inter-rater testing, Wk4 backfill collection, Wk5 index construction/weighting, Wk6 dashboard + presentation.

The **course** grades the team project separately (TP1 due 10/2, TP2 due 11/6, final presentation 12/3), with agentic-AI technical requirements. See [`memory/08-deliverables-and-rubric.md`](memory/08-deliverables-and-rubric.md).

## For AI-agent contributors (Cursor / Claude Code / Codex)
**[`/memory/`](memory/) is the single source of truth.** Read [`memory/09-decisions-log.md`](memory/09-decisions-log.md) first, then `00`–`10` in order. New to AI coding tools? Start with [`ONBOARDING_FOR_NON_CODERS.md`](ONBOARDING_FOR_NON_CODERS.md).

## How we track work
- **Shared spreadsheet:** ownership and deadlines (source of truth, per the team contract)
- **GitHub Issues + [Project board](https://github.com/users/MehulPardeshi/projects/1):** engineering-level detail

Details: [`docs/TASK_TRACKER.md`](docs/TASK_TRACKER.md). Contribution workflow: [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Repository layout
```
docs/            deliverable drafts per Part + source briefs + TASK_TRACKER.md
memory/          project memory for humans and AI agents (read 09 first)
data/raw/        downloaded source text (gitignored; see the ethics memo)
data/processed/  derived metrics and cited evidence
src/             Python package skeleton: edgar/, nlp/, index/, dashboard/
notebooks/       exploration notebooks
```

## Setup
**TODO:** the tech stack hasn't been chosen yet (EDGAR client, NLP tooling, dashboard tool). Once the team decides and logs it in `memory/09-decisions-log.md`, add real setup steps here and pin dependencies in `requirements.txt`.

For now:
```bash
cp .env.example .env   # then fill in your own values locally; never commit .env
```

## Team
Mehul Pardeshi · Yen-Chu Chen · Logan Mai · Shu Pu · Snehal Paliwal. TA: Hengkai Zheng.
Roles: see [`memory/01-team-and-roles.md`](memory/01-team-and-roles.md) (being chosen; final picks go in the decisions log).
