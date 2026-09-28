# 08 — Deliverables, Rubric, and Timeline

> **Read [`09-decisions-log.md`](09-decisions-log.md) first.** Two grading frames apply: the **client assignment brief** (A) and the **course team-project requirements** (B). Both are needed for a good grade.

---

## A. Client assignment brief: rubric and timeline

| Deliverable | Weight |
|---|---|
| Sourcing/ethics memo | 10% |
| Taxonomy + inter-rater reliability results | 20% |
| Metrics methodology write-up | 20% |
| Backfilled dataset (8+ quarters × chosen firms) | 20% |
| Dashboard | 20% |
| Final presentation defending design choices | 10% |

6-week timeline: Wk1 source review/ethics memo/firm universe, Wk2 draft taxonomy, Wk3 metrics + inter-rater testing, Wk4 backfill collection, Wk5 index construction/weighting, Wk6 dashboard + presentation.

- **Calendar mapping: TBD.** The brief is written for a generic 6-week module. If Week 1 starts Mon 9/28, Week 6 ends around Sun 11/8, which lines up with TP2 (due Fri 11/6). Fall break is 10/13 and 10/15. Log the team's agreed dates in 09.

---

## B. Course (95-891) team-project requirements

The team project is **20% of the course grade** (200 pts), plus **peer evaluation at 5%**.

### Key dates (from the syllabus; due Fridays at 5:00 pm)
> **How these dates were derived:** the syllabus schedule has a "Due Friday 5:00pm" column. It lists *Team Project #1* in the **Week 6** row (classes Tue 9/29 and Thu 10/1), which makes the due date **Fri Oct 2, 5:00 pm**. *Team Project #2* is in the **Week 10** row (classes 11/3 and 11/5), which makes it **Fri Nov 6**. The syllabus doesn't print these calendar dates itself, and its schedule is labeled "draft." **Confirm the exact deadlines in Canvas.**
| Item | Date |
|---|---|
| First client requirements meeting | Late September |
| **Team Project #1** (contract + client-meeting prep + scope doc with **kanban board link**) | **Fri Oct 2, 2026** |
| Fall break (no class) | Oct 13 and Oct 15 |
| **Team Project #2** (progress update: 1–3 page report + repo link + board snapshot) + early-Nov client meeting | **Fri Nov 6, 2026** |
| **Final project presentations** (TP3) | **Thu Dec 3, 2026** |

### TP1 before submitting (from the latest course instructions PDF)
- **Research the client's organization** (William & Mary) and the client (Julie Agnew) **before** the first client meeting.
- The first client requirements meeting must happen **before TP1 is due**. Ours is Thu 10/1; TP1 is due Fri 10/2.
- At that meeting, ask about: a specific actionable problem; constraints/context/examples; data needed (simulated/public) and whether an NDA is required; what success looks like by December; **a date/time for the progress-update meeting (late October or early November)**; and invite the client to the final poster presentation (then send a calendar invite; if she's remote, schedule a separate time to present).
- **TP1 rubric:** 30 points, criteria still "TBD" in the instructions.

### TP1 submission (3 docs)
1. Signed team contract
2. About 1-page client-meeting prep doc: who the client is, the problem as understood, and questions for the client
3. Project scope document (PMI-style; send to the client for approval) **with a link to the team's GitHub kanban board**

### TP2 submission
Progress vs. plan · working prototype/partial demo · blockers · updated scope · **project board snapshot** · repo link. Presented to the client in early November.

### TP2 rubric (50 pts; from the latest course instructions PDF)
| Criterion | Pts | What they look for |
|---|---|---|
| Progress vs. plan | 10 | Honest, specific comparison of TP1 scope to actual progress; meaningful work done |
| Working prototype/demo | 12 | A functioning (even if rough) **agentic AI component**: real build progress, not just planning docs |
| Blockers & problem-solving | 8 | Blockers clearly identified, with a credible plan to resolve them |
| Scope updates | 5 | If scope changed, the reasoning is sound and clearly explained |
| Project board upkeep | 5 | The kanban board reflects real, current task status |
| Client meeting quality | 10 | Client meeting held; team came away with clear, confirmed direction |

### Course technical requirements (TP3 must demonstrate all of these)
1. Accomplished using an **agentic workflow** (and/or helped the client set one up)
2. A **pretrained model** (e.g., an LLM) or a model trained from scratch, incorporated into the solution
3. **At least five custom agentic tools** with LLM-readable docstrings that make agent behavior more deterministic
4. A **skill folder** with `skill.md` and/or templates (used by the team, or designed for the client)
5. **Evaluation methods** for system performance
6. Methods to **protect client data or simulate test data** (and how simulated-data quality is ensured)
7. **Safety guardrails**, showing model behavior **with vs. without** the guardrails

### TP3 required repo contents
- **README as a comprehensive project report:** visuals, author list with GitHub profile links and bios, narrow project scope, project details, "What's next?", Responsible AI considerations, a **reference list with at least one high-quality research paper from the last 3 years**, and **no client identity without permission**
- **Runnable demo code** (.py / notebook / Colab) that runs live during the presentation; cite borrowed code
- An **externally hosted app/website** with agentic capabilities
- A **kanban project board** used throughout the semester

### TP3 rubric (120 pts; Excellent 100% / Satisfactory 75% / Unsatisfactory 50% / Poor 25%)
| Criterion | % |
|---|---|
| Code demo: technically challenging, logically sound | 7 |
| Website demo: creative use of vibe coding | 7 |
| Poster: visually effective, complete | 7 |
| GitHub repo organized and complete | 7 |
| GitHub kanban board visually organized | 7 |
| Research paper well chosen and discussed | 7 |
| References cited properly | 7 |
| Problem statement, rationale, and approach articulated | 9 |
| Business opportunities and challenges articulated | 9 |
| Technical components explained for a non-technical audience | 12 |
| Judges learned significant new knowledge about AI | 7 |
| Creativity | 7 |
| Team collaboration: all members engaged in presentation and Q&A | 7 |

### Course policies that affect how we work
- **Generative AI use** must be **acknowledged and cited** in submitted work where it's allowed (syllabus GenAI policy). Keep a running note of which tools produced what.
- **No late submissions for team work.**
- Help only from the instructional team, not other groups.
- Everyone must be able to discuss the **entire** project.
