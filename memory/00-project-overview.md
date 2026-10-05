# 00 — Project Overview

> **2026-10-01 kickoff clarification:** See [minutes](../meetings/2026-10-01-client.md) and the latest decisions log. the proof of concept covers **5–6 big U.S. financial companies** (e.g., JPMorgan; decided 2026-10-01, superseding the 4–5-bank figure in the transcript excerpts) and permits a simpler team-designed measure. Final coverage, taxonomy, and metrics remain open; quarterly automation is desired only if feasible. Earlier targets below remain brief material, not confirmed client commitments. Course/rubric obligations must be checked with the instructor before reducing graded requirements.


> **Read [`09-decisions-log.md`](09-decisions-log.md) first.** Anything decided there overrides this file.

## Mission (one line)
Build an **AI Adoption Index** that tracks how **financial services firms** talk about and deploy AI over time, using only public, legally accessible sources, and publish it as a **living, quarterly-updated index on an interactive dashboard**, backed by a taxonomy the team **derives and defends itself**.

## Course context
- **Course:** 95-891 Introduction to Artificial Intelligence, CMU Heinz College, Fall 2026, Section C
- **Instructor:** Dr. Rachel Chung. Course email: i2ai@andrew.cmu.edu
- **Team:** Team 5 / Project 5 (5 students; roster in [`01-team-and-roles.md`](01-team-and-roles.md))
- **Project TA:** Hengkai Zheng (hengkaiz@andrew.cmu.edu)
  - **Confirmed 2026-10-04** as our project TA/advisor. (The syllabus lists Hengkai under Section A; the project assignment is separate.)

## Client
- **Julie Agnew, William & Mary.** The dataset feeds a **book chapter she is writing on AI in retirement**.
- **Co-client:** the kickoff agenda also lists **Dr. Rachel Chung (Heinz College)**, our course instructor, as a client.
- **Two teams, one client:** **Team 15** (Megan Lin, Trisha Sharma, Vidushi Bist, Yu-Hsuan Li, Han Yang) has the same client and topic. Per the course instructions, teams work on the topic **separately**. Both attended the joint kickoff on 2026-10-01.
- That's why **Retirement Plan Providers / Recordkeepers are the primary sector** (see [`03-sectors-and-firms.md`](03-sectors-and-firms.md)).
- **Naming permission (2026-10-01):** Julie said **yes**: we may name her and the book chapter in the repo, poster and LinkedIn. **No NDA.** (The course's confidentiality-by-default rule is satisfied by her explicit permission.)
- **The book:** Pension Research Council (Olivia Mitchell, Wharton) volume from its AI-and-retirement conference; our index feeds the introductory chapter by Julie Agnew and Rachel Chung.
- **Historical note (superseded by the permission above):** the course says client identity is confidential by default. The repo is private. **Before making it public, presenting outside the class, or posting on LinkedIn, get the client's permission** (per the course project instructions). The final README must not name the client without that permission.

## Two sets of requirements (both apply)
1. **Client assignment brief:** `docs/source-materials/AI Adoption Index project requirements.docx` (text copy: [`ai-adoption-index-requirements.md`](../docs/source-materials/ai-adoption-index-requirements.md)). This defines Parts 1–5, the 6-week timeline, and the deliverable weights.
2. **Course project requirements:** `docs/source-materials/i2ai course project instructions (latest).pdf` (text copy: [`i2ai-course-project-instructions-latest.md`](../docs/source-materials/i2ai-course-project-instructions-latest.md)). This is **newer than the older .docx version** and takes precedence where they differ. This defines TP1/TP2/TP3 and the **agentic-AI technical requirements**: 5+ custom agentic tools, a skill folder, guardrails, evaluation, a GitHub kanban board, and a hosted app.

Both are summarized in [`08-deliverables-and-rubric.md`](08-deliverables-and-rubric.md).

## The central methodological trap
**"Mentions AI" ≠ "uses AI."** Filings and press releases are legal and marketing documents, not ground truth about internal operations. Every metric and dashboard claim should be framed with this in mind (from the instructor notes in the brief).

## Team goals beyond the grade (from the signed contract)
1. **Ship a dashboard that actually works end to end**, not just a polished deck. It should be something each of us can point to as a real technical build on a résumé.
2. **The client is happy with the result.** It meets her needs (the contract lists this one twice).
3. **Accomplish the scope we promise.** Follow through on what we say we will do.

## Scope guardrails for AI agents working in this repo
- The **taxonomy (Part 2)** and **metrics (Part 3)** are graded on the team deriving them from real documents. **Do not write "final" versions of either** and do not implement working classification or scoring logic unless the decisions log says the team has finalized the design.
- **Do not assign roles** to people unless 09 records the decision.
