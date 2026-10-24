# Earnings-call transcript sources (for Logan's review)

**By:** Yen-Chu Chen · **First draft:** Oct 20, 2026 · **Revised:** Oct 24, 2026 after [Logan's review](https://github.com/MehulPardeshi/ai-adoption-index/pull/62) · **Issue:** #34
**Status:** PROPOSAL. **Nothing is collected** until Logan clears each source in the [ethics memo](ethics_memo.md). Every decision column below reads "pending (Logan)".

**Period:** calls for Q3 2024 to Q2 2026 (8 per company), the same window as the SEC test run.

**Source-review table (one row per transcript, 56 rows):** [`transcript_source_review.csv`](transcript_source_review.csv). Columns: company, quarter, document URL, rights holder, notice on the document, applicable terms (URL and summary), date checked, and four **separate decisions: access, local storage, team sharing, publication**.

## 1. What we found (checked Oct 24, 2026)

| Company | Official transcripts for Q3 2024–Q2 2026 | Rights holder (from the documents) | Site terms (summary) |
|---|---|---|---|
| JPMorgan Chase | ✅ 8 of 8 PDFs on [IR](https://www.jpmorganchase.com/ir/quarterly-earnings) | **Unclear.** No copyright notice in the 3 PDFs searched. JPMorgan's site terms claim its content; the layout looks like a transcript vendor's | [Terms](https://www.jpmorganchase.com/legal/terms-and-conditions): no copying, distribution or "stored for subsequent use" without written consent, except fair use (17 U.S.C. § 107) |
| Citigroup (extra comparison) | ✅ 8 of 8 PDFs on [IR](https://www.citigroup.com/global/investors/quarterly-earnings) | **Citigroup Inc.** ("Copyright © \<year\> Citigroup Inc." on every page; 4 of 8 checked) | [Terms](https://www.citigroup.com/global/terms): same wording as JPMorgan's; also bans data scraping |
| Principal Financial | ✅ 8 of 8 PDFs on [IR](https://investors.principal.com/financials/quarterly-results) | **Q3 2024–Q1 2025:** unclear (Principal-branded, no notice). **Q2 2025–Q2 2026:** **FactSet CallStreet, LLC** ("Copyright © 2001–\<year\> FactSet CallStreet, LLC"; all 8 checked) | [Terms](https://www.principal.com/terms-of-use): "download and print copyrighted materials for your personal non-commercial use only"; no modifying, transmitting or distributing without written consent. FactSet's own terms not yet reviewed |
| Bank of America | ⚠️ 2 of 8 on [IR](https://investor.bankofamerica.com/quarterly-earnings) (Q1–Q2 2026). The page lists Q1 2021–Q3 2026, but transcripts start in 2026; older quarters have release, presentation and supplement only | **Unclear.** BAC-branded accessible (ADA) versions, no notice | [IR terms of use](https://investor.bankofamerica.com/terms-of-use) don't address copying or reuse |
| Wells Fargo | ❌ None. IR posts release, presentation, supplement and webcast only | — | — |
| Charles Schwab | ❌ None. IR posts presentations and webcasts; last transcript is from 2019 | — | — |
| Capital One | ❌ None. [IR](https://investor.capitalone.com/financial-information/quarterly-results) posts release, financial supplement and presentation; the webcast is linked from the news release | — | — |

**Key point (Logan's point 1):** a company hosting a transcript doesn't settle who owns it. Principal's newer transcripts belong to **FactSet CallStreet**, so FactSet's terms matter, not just Principal's.

## 2. Motley Fool: US terms (Logan's point 2)

[The Motley Fool's Rules](https://www.fool.com/legal/terms-and-conditions/fool-rules/), last updated Jan 29, 2026:

- **§7 Intellectual property:** "You may make one copy of the Content for your personal, non-commercial use"; any other copying, distribution, **storing** or transmission needs prior written permission. Content may not be posted to bulletin boards, blogs, chat rooms **or intranets**. "You further agree not to **create abstracts from or scrape** our Content."
- **§8 Conduct:** no "automated means, including, without limitation, agents, robots, scripts, or spiders" to access, monitor, copy or harvest data.

**What this means:** one personal reading copy only. No shared team folder (an intranet), and no "abstracts", which likely covers our AI passage extracts and summaries. **Logan isn't clearing Motley Fool for the shared corpus or the dashboard**, and these terms support that. So Wells Fargo, Schwab and Capital One have **no usable transcript source** for now.

## 3. Verbatim excerpts vs. derived data (Logan's point 3)

| Type | Examples | Proposed handling |
|---|---|---|
| **Verbatim excerpts** | Quoted sentences from a transcript | **Not published** (repo or dashboard) until Logan documents a basis per source. Stays in local, permitted storage only |
| **Derived data** | Labels (D2/D1/P/N), scenario codes, counts, scores, the source URL, speaker role (management vs. analyst) | Can go in the repo, if the memo agrees. Contains no transcript text |

We drop the earlier assumption that "one or two sentences" is automatically fine.

## 4. Storage proposal (Logan's point 4)

Only material that the terms allow for each use goes into each place:

| Place | What | Owner | Access | Retention / deletion |
|---|---|---|---|---|
| Personal computer, `data/raw/transcripts/` (gitignored) | PDFs that pass "access" and "local storage" | Each team member, for their own copy | That person only | Delete at project end (proposed: by **Dec 31, 2026**) or whenever Logan withdraws clearance |
| Team Drive folder `transcripts/` | **Only** sources that pass "team sharing" (none yet) | Yen-Chu (Dataset Builder) | 5 team members, view only, no public link | Same as above; owner deletes the folder |
| GitHub | Derived data only (section 3) | — | Repo collaborators | Follows the repo |

## 5. Options for the gaps (Logan's point 5)

| Option | Covers | Permissions check needed |
|---|---|---|
| A. Company IR only | JPM, Citi, Principal (8 quarters each), BAC (2026) | Per-source review in the CSV, including FactSet's terms for Principal's newer transcripts |
| B. Self-transcribe the companies' own webcasts (e.g., Whisper) | WFC, SCHW, COF, BAC pre-2026 | Separate check: webcast replay terms (e.g., edge.media-server.com) and whether a transcript we make is a derivative work |
| C. Motley Fool | WFC, SCHW, COF | Not cleared (see section 2) |
| D. No transcripts for those companies | — | None. They're scored from SEC filings only, and the dashboard says so |

**Proposal:** start with A once cleared. Choose B or D for the other companies after Logan's decision. C stays off.

## 6. Decisions needed from Logan

- [ ] For each row in [`transcript_source_review.csv`](transcript_source_review.csv): **access / local storage / team sharing / publication**
- [ ] FactSet CallStreet terms for Principal's Q2 2025–Q2 2026 transcripts: who reviews them?
- [ ] Option B (self-transcribing webcasts): worth a permissions check, or go with D?
- [ ] Storage and retention plan in section 4: OK?

*Research and drafting assisted by Claude. Documents and terms were opened in a browser on Oct 24, 2026, and the copyright notices were read from the PDFs themselves.*
