# TP3: research paper discussion and handover split (DRAFT, Mehul, Nov 9)

> Agreed at the Nov 8 call: first find what the course expects, then Mehul splits the paper discussion along with the other handover tasks ([minutes](../../meetings/2026-11-08-internal.md)). **Status:** expectations confirmed from the course files below. The split is a **proposal for the team**, and the draft text is for the owners to rewrite.

## What the course asks for (from the [project instructions](../source-materials/i2ai-course-project-instructions-latest.md))
| Where | Requirement |
|---|---|
| README | "Reference list, including at least one high-quality research paper (not news/blog/LinkedIn), published within the last 3 years" |
| Presentation | "Research paper: the required paper and how it informed your approach" |
| Rubric (7% of 120) | "Research paper is well chosen and well discussed verbally and on the poster" |
| Rubric (7%) | "References are cited properly" |

- **No length is given.** Plan on one README section (~250–400 words), one poster panel and about 1 minute in the talk.
- The rubric grades the discussion **verbally and on the poster**, so the README text alone isn't enough.
- **Snehal asks Dr. Chung (Tue Nov 10 if she joins, otherwise by email):** is a README section plus a poster panel enough? Does a working paper (Dong et al.) count as a second reference, or only peer-reviewed work?

## Our papers (decided Oct 25)
| Role | Paper | Why it qualifies |
|---|---|---|
| **Main (the "required paper")** | Babina, Fedyk, He & Hodson (2024), *Artificial intelligence, firm growth, and product innovation*, Journal of Financial Economics 151, 103745. https://doi.org/10.1016/j.jfineco.2023.103745 | Peer-reviewed, top finance journal, 2024 (within 3 years) |
| Comparison method | Dong, Doukas & Zhang (2026), *Artificial Intelligence Engagement, Firm Value, and Risk Transformation*, SSRN working paper | Recent and on our exact question (AI from 10-K text); **not peer-reviewed**, so it can't be the only paper |

## Draft README section (owners rewrite; check every claim against the PDF before it ships)
> **Research foundation.** Our main paper is Babina et al. (2024, *Journal of Financial Economics*). It measures firms' AI investment from the skills in their **job postings and employee résumés**, rather than from what firms say. It finds that AI-investing firms grow faster in sales, employment and market value, mainly through **product innovation**, and that the gains go mostly to larger firms. Two lessons shaped our index. First, **what a firm does is a better measure than what it says**: that's why we separate real use (D2/D1) from talk (N) instead of counting AI words. Second, **AI benefits concentrate in large firms**: that's why our sector index offers a market-cap-weighted view next to the equal-weighted one.
>
> We compare our measure with Dong et al. (2026), who build an AI-intensity score from 10-K word counts. On our six pilot firms, their score tracks how much firms *talk* about AI (ρ 0.78) more than our *use* score (ρ 0.58). That's a direction only (six firms), but it supports the idea that talk and use differ ([check 4](../part3-metrics/check4_results.md)).
>
> **How we differ from both:** job-posting data (Babina) is licensed and costly, and word counts (Dong) can't tell use from risk talk. We read public SEC filings with an AI agent, and every "uses AI" claim must quote the filing word for word. So anyone can rerun the index for free, and every score traces back to a sentence.

**Verify before it ships:** Babina et al.'s data sources (job postings + résumés), the outcomes (sales, employment, valuations; product innovation as the channel), and the "larger firms" finding. Use page numbers from the PDF. Shu's [Dong review](../reviews/2026-10-17_dong-et-al-paper-review_shu.md) and Mehul's [Dong brief](../reviews/2026-10-19_dong-paper-brief_mehul.md) cover Dong.

## Proposed TP3 split (for the team to change)
Based on roles and what each person already owns. Final presentation **Thu Dec 3**.

| Piece (from the TP3 requirements) | Proposed owner | Notes |
|---|---|---|
| Paper discussion: README section, poster panel, 1-minute talk | **Logan** (Babina, how it shaped our approach) + **Shu** (a few lines comparing our method with Dong's); Mehul reviews | Start from the draft above; Shu already reviewed Dong |
| References list, cited properly | **Logan** | Builds on the ethics memo sources and `docs/references.md` |
| Responsible AI section | **Mehul** (Logan adds the data/legal-sourcing part from the ethics memo) | ✅ Draft: [responsible_ai.md](responsible_ai.md) (Nov 9) |
| Skill folder (`skills/ai-adoption-index/`) | **Mehul** drafts (done Nov 9), **Shu** reviews | Requirement 4 |
| Runnable code demo (one concept) | **Shu** | e.g., one passage → label → guardrail → score |
| Hosted app (Streamlit Community Cloud) | **Snehal** | #30, decided Nov 8 |
| Sector index (equal + market-cap-weighted) | **Yen-Chu** (+ Shu's 75-firm run) | Decided Nov 8 |
| Handover package for Julie (what she gets, data location, how to refresh) | **Shu** + **Snehal** | Depends on Julie's answer Tue Nov 10; the skill's Task 1 is the how-to |
| README: concept visuals, scope, project details, "What's next?", author list with bios | **Yen-Chu** (scope, details) · **Snehal** (visuals) · everyone (own bio + GitHub link) | |
| Poster | **Snehal** (owner since Oct 1) | Everyone sends one panel |
| Kanban board tidy-up + "how we used it" talking point | **Mehul** | |

**Next:** agree on the split at the next team meeting (or in the chat after Tuesday), then turn it into GitHub issues under a TP3 milestone.
