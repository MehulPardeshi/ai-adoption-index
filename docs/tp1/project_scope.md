# Project Scope: AI Adoption Index

**Prepared by:** Team 5: Logan Mai, Yen-Chu Chen, Mehul Pardeshi, Shu Pu, Snehal Paliwal
**Date:** October 5, 2026 · **Version:** 1.1, updated with the team's October 4 planning decisions (v1.0 submitted October 2)
**Project board:** https://github.com/users/MehulPardeshi/projects/1

## 1. Project objective
Build a reproducible, evidence-based index of how large U.S. financial institutions adopt artificial intelligence. It will draw only on public, citable sources and go beyond simple counts of AI mentions. The index will serve two audiences: **financial professionals** asking which AI applications are relevant to their business, and **students** asking which skills the industry needs. It will also provide supporting evidence for Dr. Agnew and Dr. Chung's introductory chapter in the Pension Research Council volume on AI and retirement.

## 2. Deliverables
- **Proof of concept:** an initial study of **six large U.S. publicly traded financial companies**: JPMorgan Chase, Bank of America, Capital One, Wells Fargo, Charles Schwab and Principal Financial Group. That's four major banks plus two wealth and retirement firms. It covers filings from **2024–2026** and produces preliminary findings and a first dashboard view: a company view with click-in detail, and categories such as investment in AI, AI built into products, and AI-related jobs. The team expects to expand coverage after the proof of concept.
- **Evidence dataset:** source citations for every data point, with documented coverage and limitations.
- **Use-case taxonomy and measure:** team-developed AI use-case categories and a documented quantitative measure, validated by human review. The calculation, weighting and classification approach will be chosen after reviewing the client-provided papers and the proof-of-concept results. Simple percentages are acceptable to the client.
- **Interactive dashboard:** built with Streamlit and hosted online, with firm and subsector views, transparent firm membership, cited evidence, and links to related research and indices.
- **Reproducible codebase and methodology on GitHub:** evaluation results, a runnable demonstration, and a documented refresh procedure.

## 3. In scope
- **Public, citable and permitted sources**, starting with SEC EDGAR filings (10-K, 10-Q) and earnings-call transcripts from company investor-relations pages. Job-posting data (e.g., Handshake, LinkedIn) will be used only if the team's ethics and legal review confirms access is permitted under each platform's terms; automated collection from these platforms is not planned. The final source set will be proposed after the proof of concept and confirmed with the client.
- **Review of the AI Intensity Dataset** and its associated paper, verifying the methodology before reusing or describing it.
- **Distinguishing concrete, reported AI applications from generic mentions and future plans.** Public disclosure is evidence of a stated activity, not direct verification of internal deployment.
- **Course technical requirements:** an agentic workflow, a pretrained model, at least five documented custom agent tools, a skill folder, evaluation methods, data-protection methods, and safety guardrails with a with/without comparison.

## 4. Out of scope
- Comprehensive coverage of all financial institutions during the proof of concept.
- Proprietary data (e.g., CFO survey microdata), restricted university career-site data, or any collection outside permitted access.
- Claims that missing public evidence proves non-adoption, or that reported use proves business impact.
- Guaranteed publication, a particular firm ranking, or a finalized composite score.
- Guaranteed hosting or support after the course ends.

**Candidates for later phases**, subject to feasibility and client agreement: cross-subsector expansion, firm-size weighting, keyword-trend visualizations, and automated quarterly updates.

## 5. Acceptance criteria
- The proof of concept can be demonstrated end to end, with traceable source evidence for every reported figure.
- Firm inclusion, time coverage, treatment of missing evidence, category definitions and calculation choices are documented.
- An independent reviewer can reproduce the reported figures from the documented inputs and procedure.
- An evaluation approach, designed by the team's Evaluation Lead, compares automated extraction and classification against human review and reports findings and limitations. Specific methods and thresholds will be defined during the project.
- The dashboard clearly identifies the covered firms and supports the agreed views.
- All course-required agentic components, documentation, evaluation and the runnable demonstration are present.

## 6. Constraints
- Public and citable evidence only; the level of disclosure varies across firms and sources.
- **No project funding.** The team will use free tools, publicly accessible data and free service tiers. Any proposed cost requires a team decision and an identified funding source.
- The semester timeline and team capacity limit coverage.
- The taxonomy and metrics must be developed and validated by the team.
- Course grading requirements apply alongside the client's methodological flexibility; any differences will be reconciled with the instructor.
- No NDA is required. The client has permitted the team to name her and the book chapter. All work must be reproducible.

## 7. Assumptions
- The proof of concept will establish feasible data access and historical depth.
- Client-provided reference papers will inform the methodology once received.
- Teams 5 and 15 work independently, with separate progress checks and updates.
- Hosting, ongoing costs and post-course maintenance will be agreed later.

## 8. Milestones
| Milestone | Date / status |
|---|---|
| Client kickoff meeting | October 1, 2026 (completed) |
| TP1 scope submission | October 2, 2026, 5:00 pm |
| Company list finalized | October 4, 2026 (completed) |
| Proof-of-concept results ready | Thursday, October 29, 2026 |
| Client progress meeting and scope review | Thursday, October 29, 2026, 1:00–2:00 pm (proposed; to be confirmed with the client) |
| TP2 progress submission | November 6, 2026 |
| Final presentation | December 3, 2026 (client to attend in person if possible) |

## 9. Stakeholders and roles
- **Client:** Dr. Julie Agnew, William & Mary
- **Instructor and chapter co-author:** Dr. Rachel Chung, Carnegie Mellon University, Heinz College
- **Project team:** Team 5 (below)
- **Related team:** Team 15, working independently on the same topic
- **Intended users:** financial professionals and students

| Team member | Role |
|---|---|
| Mehul Pardeshi | Project Manager; Responsible AI and Evaluation Lead |
| Yen-Chu Chen | Dataset Builder |
| Logan Mai | Market & User Researcher / Business Analyst |
| Shu Pu | AI Engineer / Solution Architect |
| Snehal Paliwal | Dashboard Product Manager and client communication lead |

## 10. Open items
- Company coverage beyond the proof of concept
- Taxonomy development process
- Measure, denominator, weighting and normalization
- Which of the original assignment requirements still apply (to be confirmed with the instructor)
- Progress-meeting date
- Hosting and post-course maintenance

Scope changes will be documented in the project's GitHub repository, and material changes will be reviewed with the client.

## 11. Client approval
| Item | Detail |
|---|---|
| Submitted to client | October 2, 2026 |
| Approved by | |
| Approval date | |
| Comments | |
