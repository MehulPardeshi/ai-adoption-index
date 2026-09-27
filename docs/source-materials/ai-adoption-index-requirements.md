<!-- Text conversion of "AI Adoption Index project requirements.docx" (pandoc). The .docx is the original. -->

# **Assignment: Building an AI Adoption Index for Financial Services Firms**

## **Overview**

Students will design and build a system that tracks how financial firms talk about and deploy artificial intelligence over time, using only publicly available, legally accessible sources. The end product is a living, quarterly-updated **AI Adoption Index** displayed on a dashboard, backed by a taxonomy of AI-use categories that students themselves develop and defend.

This assignment blends financial-statement literacy, NLP/text-analytics, index construction methodology, and data visualization — while forcing students to confront real questions about measurement validity (What does “using AI” even mean? How do you quantify vague corporate language?).

## **Learning Objectives**

By the end of this project, students should be able to:

> 1\. Source and legally collect unstructured financial text data (transcripts, filings, press releases, news).
>
> 2\. Build and justify a categorization taxonomy from empirical evidence rather than assuming categories up front.
>
> 3\. Apply text-analytics techniques (frequency counts, specificity scoring, sentiment analysis) to noisy corporate language.
>
> 4\. Construct a composite index with defensible weighting and normalization choices.
>
> 5\. Backfill historical data and design a repeatable, quarterly-refresh pipeline.
>
> 6\. Communicate findings through an interactive dashboard aimed at a non-technical audience (e.g., analysts, regulators, journalists).

## **Part 1 — Data Sourcing (Legally and Ethically)**

Students should only use sources that are legally scrapable/accessible and citable. Approved source types:

| Source Type | Examples | Notes |
|----|----|----|
| Regulatory filings | SEC EDGAR (10-K, 10-Q, 8-K, DEF 14A) | Use EDGAR’s official APIs/bulk data, not scraping the HTML front end where an API exists |
| Earnings call transcripts | Company IR pages, Seeking Alpha (check ToS), Motley Fool transcripts | Many firms post official transcripts/PDFs on investor relations pages |
| Press releases | Company newsrooms, Business Wire, PR Newswire |  |
| News articles | Reuters, Bloomberg, WSJ, Financial Times (respecting paywalls and ToS) | Consider using licensed news APIs (e.g., NewsAPI, GDELT) rather than raw scraping |
| Financial databases | Bloomberg Terminal, Refinitiv/LSEG, S&P Capital IQ, WRDS (if available through the institution) | Use if your school provides access |
| Company websites | Careers pages (AI job postings), product pages, technology/innovation pages |  |

**Required ethics/legal checkpoint (graded):** Before scraping anything, each team must submit a one-page memo covering: - robots.txt and Terms of Service review for each target site - Rate-limiting and request-header practices to avoid being a bad actor - Data storage/retention plan (raw text vs. derived metrics) - Attribution/citation plan for any quoted material

This is a good moment to flag: **SEC EDGAR is the gold-standard backbone** for this project since it’s free, structured, comprehensive, and explicitly built for this kind of use (full-text search API, XBRL structured data, bulk downloads).

## **Part 1.5 — Define the Firm Universe by Sector**

Before students touch the AI-use taxonomy, have them segment the firm universe itself. This matters for two reasons: it lets you make apples-to-apples comparisons *within* a sector (a bank and a retirement plan provider will talk about AI very differently), and — since this dataset feeds a book chapter on AI in retirement — it guarantees the retirement-plan-provider slice is deliberately built out rather than an afterthought.

Suggested sector categories and starting firms (students should refine and expand these, and instructors should adjust based on which chapter/sector needs the deepest coverage):

| Sector | Example Firms | Why they matter to the index |
|----|----|----|
| **Investment/Asset Management Firms** | T. Rowe Price, BlackRock, Vanguard, Fidelity, State Street, Invesco | Core “investment advice/portfolio construction” AI use cases; heavy public disclosure via fund commentary and 10-Ks |
| **Retirement Plan Providers / Recordkeepers** | Fidelity, Empower, Voya, Principal, Vanguard, T. Rowe Price, TIAA, Alight | **Primary focus for the book chapter** — track AI in plan design, participant advice/robo-guidance, auto-enrollment/auto-escalation optimization, retirement income modeling, and participant-facing chatbots |
| **Banks (Universal/Commercial)** | JPMorgan Chase, Bank of America, Wells Fargo, Citigroup, U.S. Bank | Fraud detection, credit underwriting, back-office automation, customer service AI |
| **Insurance Companies** | MetLife, Prudential, Nationwide, Lincoln Financial | Underwriting, claims automation, and (overlapping with retirement) annuity/income-product AI use |
| **Broker-Dealers/Wealth Management** | Charles Schwab, Morgan Stanley, Merrill Lynch, Edward Jones | Robo-advisory, advisor-productivity tools, client-facing recommendation engines |
| **Fintech/AI-Native Firms** | Betterment, Wealthfront, Personal Capital/Empower Personal Wealth | Useful as a “high AI-intensity” benchmark group to contrast against incumbents |
| **Pension Funds/Sovereign & Public Plans** (optional) | CalPERS, state teacher retirement systems | Useful if the book chapter wants an institutional-investor angle on retirement, not just recordkeepers |

Notes for implementation:

> • **Some firms belong to more than one sector** (e.g., Fidelity and T. Rowe Price are both asset managers and retirement recordkeepers). Have students tag firms with all applicable sector labels rather than forcing a single category — this becomes a filterable dimension on the dashboard rather than a data-cleaning problem.
>
> • Because the retirement slice feeds the book chapter directly, consider requiring **deeper backfill and a larger firm count** for Retirement Plan Providers than for the other sectors (e.g., 10+ firms there vs. 5–8 in the others).
>
> • Retirement-specific sub-taxonomy to layer on top of Part 2’s general categories: **participant advice/robo-guidance, retirement income/decumulation modeling, plan design & auto-features optimization, plan sponsor-facing analytics, and participant engagement/chatbots.** These can be sub-tags within “client-facing advice” and “portfolio construction” rather than wholly new top-level categories, so the general taxonomy still holds across sectors.
>
> • Add **sector** and **firm** as filterable fields on the dashboard (Part 5) so the book chapter can pull a clean retirement-only view without excluding that data from the broader cross-sector index.

### **Mapping Sectors to Standard Industry Codes**

None of the standard classification systems has a clean “retirement plan provider” bucket, since recordkeeping is a business line, not a legal entity type — the same firm can be chartered as an investment adviser, insurer, or bank holding company depending on structure. Students should treat the table below as a starting filter for pulling EDGAR filings by code, and should explicitly note in their methodology write-up that they’re layering a *functional* taxonomy (what the firm does) on top of a *legal/regulatory* one (what the firm is classified as) — the mismatch itself is worth a paragraph in the book chapter.

| Sector (functional) | SIC Code(s) | NAICS Code(s) | GICS Sub-Industry (approx.) |
|----|----|----|----|
| Investment/Asset Management Firms | 6282 (Investment Advice), 6726 (Investment Offices) | 523900 / 523930 (Investment Advice/Portfolio Mgmt) | Asset Management & Custody Banks |
| Retirement Plan Providers/Recordkeepers | No dedicated code — filers typically appear under 6282, 6311, or 6020/6022 depending on charter; 6371 (Pension/Retirement Funds) exists but is sparsely used by EDGAR filers | 525110 (Pension Funds); some recordkeeping arms fall under 523900 | No dedicated sub-industry — split across Asset Management & Custody Banks and Life & Health Insurance |
| Banks (Universal/Commercial) | 6020 (National Commercial Banks), 6021, 6022 (State Commercial Banks), 6712 (Bank Holding Companies) | 522110 (Commercial Banking) | Diversified Banks, Regional Banks |
| Insurance Companies | 6311 (Life Insurance), 6321 (Accident & Health Insurance), 6411 (Insurance Agents/Brokers) | 524113 (Direct Life Insurance Carriers), 524114 (Direct Health/Medical) | Life & Health Insurance, Multi-line Insurance |
| Broker-Dealers/Wealth Management | 6211 (Security Brokers, Dealers) | 523110 (Investment Banking and Securities Dealing) | Investment Banking & Brokerage |
| Fintech/AI-Native Firms | Varies — often 6199 (Finance Services) or 7372 (Prepackaged Software) depending on how the firm self-classifies | 522320 (Financial Transactions Processing), 511210 (Software Publishers) | Financial Exchanges & Data, Application Software |
| Pension Funds/Sovereign & Public Plans (optional) | 6371 (Pension, Health, and Welfare Funds) | 525110 (Pension Funds) | Not typically covered by GICS (most are not publicly traded entities) |

Practical use: SIC code is the most directly actionable for this project, since it’s embedded in every EDGAR filer’s header and can be used to filter EDGAR’s full-text search and bulk-data downloads by sector before students even start reading transcripts. GICS is more useful later, for framing peer-group comparisons the way equity research already does (e.g., comparing your index against how sell-side analysts group “Asset Management & Custody Banks”).

## **Part 2 — Build the Categorization Taxonomy**

Rather than handing students a fixed taxonomy, have them derive one inductively from a sample of ~30–50 documents, then formalize it. A starter list they can react to, refine, split, or merge — not to just copy:

> • **Client-facing advice** — robo-advisors, chatbots, personalized recommendations
>
> • **Portfolio construction/optimization** — asset allocation, factor models, rebalancing algorithms
>
> • **Trading & execution** — algo trading, smart order routing, market-making
>
> • **Risk management** — credit risk scoring, market risk modeling, stress testing
>
> • **Fraud detection & AML/KYC** — anomaly detection, transaction monitoring
>
> • **Compliance & regulatory** — surveillance, regulatory reporting automation
>
> • **Back-office/operations** — document processing, reconciliation, settlement automation
>
> • **Underwriting** — insurance, lending
>
> • **Customer service** — chatbots, call-center automation
>
> • **Research & analytics** — earnings summarization, sentiment scoring of markets, alt-data analysis
>
> • **HR/internal productivity** — recruiting, coding copilots, internal knowledge tools
>
> • **Marketing** — personalization, ad targeting

Deliverable: a taxonomy document with clear inclusion/exclusion rules and 2–3 example sentences per category pulled from real filings (properly cited/paraphrased, not scraped verbatim into the report).

## **Part 3 — Metrics Design**

Have students propose, test, and justify a metrics battery. Suggested starting metrics, each of which has real measurement tradeoffs worth discussing in class:

| Metric | What it captures | Design challenge |
|----|----|----|
| **AI mention density** | Words/sentences dedicated to AI, as % of total document length | Normalize by document length and type (a 10-K ≠ a press release) |
| **Category breadth** | Number of distinct use-case categories mentioned per quarter | Risk of overcounting vague mentions |
| **Specificity score** | 1–5 rubric: does the firm name a specific tool/model/outcome, or just say “we use AI”? | Requires a hand-coded rubric + inter-rater reliability check between team members |
| **Sentiment/tone** | Positive (opportunity-framed) vs. cautious (risk-framed) vs. neutral | Financial-domain sentiment models (e.g., Loughran-McDonald dictionary) outperform generic sentiment tools here |
| **Forward vs. retrospective framing** | Is AI discussed as a future plan or a deployed capability? | Requires tense/modal-verb tagging |
| **Repetition/consistency** | Does the same use case reappear quarter over quarter (real deployment) or disappear (hype)? | Requires entity/topic tracking across time |
| **Investment signal** | Capex, headcount, or partnership announcements tied to AI | Cross-reference with 8-Ks and press releases |

**Methodological requirement:** students must run an inter-rater reliability check (e.g., Cohen’s kappa) on the specificity score, since it’s the most subjective metric — this teaches them that “creative metrics” still need validity checks.

## **Part 4 — Constructing the AI Adoption Index**

Ask each team to:

> 1\. Choose a **unit of analysis** (per firm-sector per quarter) using the sector universe defined in Part 1.5.
>
> 2\. **Normalize** each metric (z-scores or min-max scaling within the peer universe) so metrics on different scales can be combined.
>
> 3\. Propose a **weighting scheme** (equal-weighted to start; let advanced teams test alternative weights and justify them, e.g., specificity weighted more heavily than raw mention count).
>
> 4\. **Backfill** at least 8–12 historical quarters per firm to establish a baseline trend, sourced primarily from EDGAR’s full-text search (which covers filings back many years) and archived transcripts/press releases.
>
> 5\. Document a **refresh protocol**: exactly what to re-run each quarter (new filings, new transcripts, re-scored specificity/sentiment) so the index is genuinely maintainable, not a one-off.
>
> 6\. Include a **methodology appendix** — this is the most important academic artifact, since a reader should be able to reproduce the index from it.

Discussion prompt for class: how does this resemble (or differ from) how real indices are built — e.g., the Fed’s textual sentiment indices, the “AI mentions in earnings calls” indices some sell-side research desks already publish? This is a good moment to have students search for and compare against any existing AI-adoption trackers, so they understand where their contribution is novel vs. replicative.

## **Part 5 — Dashboard**

Deliverable: an interactive dashboard (tools: Tableau, Power BI, or a Python app using Streamlit/Dash/Plotly) that shows:

> • Index trend line per firm and peer-group average, over time
>
> • Category breakdown (stacked bar or treemap) per firm per quarter
>
> • Sentiment trend over time
>
> • A firm-comparison view (radar/spider chart across categories)
>
> • Drill-down to the underlying quoted evidence (paraphrased, cited) for any data point, for auditability

## **Suggested Deliverables & Rubric Weighting**

| Deliverable                                         | Weight |
|-----------------------------------------------------|--------|
| Sourcing/ethics memo                                | 10%    |
| Taxonomy document + inter-rater reliability results | 20%    |
| Metrics methodology write-up                        | 20%    |
| Backfilled dataset (min. 8 quarters × chosen firms) | 20%    |
| Dashboard                                           | 20%    |
| Final presentation defending index design choices   | 10%    |

## **Suggested Timeline (for a ~6-week module)**

> 1\. **Week 1:** Source review, ethics memo, pick firm universe
>
> 2\. **Week 2:** Draft taxonomy from sample documents
>
> 3\. **Week 3:** Metrics design + inter-rater reliability testing
>
> 4\. **Week 4:** Backfill data collection and coding
>
> 5\. **Week 5:** Index construction, weighting experiments
>
> 6\. **Week 6:** Dashboard build and final presentation

## **Notes for the Instructor**

> • Consider providing a small seed dataset (e.g., 5 firms × 4 quarters, pre-scraped) so all teams start from common ground and grading is comparable, while still requiring them to do the harder backfill work themselves.
>
> • The EDGAR full-text search API (efts.sec.gov/LATEST/search-index) is a strong anchor point since it’s free, well-documented, and lets students search filings by keyword across the whole market.
>
> • Watch for teams treating “mentions AI” as equivalent to “uses AI” — this is the central methodological trap of the assignment, and a good class discussion point: press releases and filings are marketing/legal documents, not ground truth about internal operations.
>
> • Consider a bonus track for teams that validate their index against an external proxy (e.g., correlating the index with AI-related job postings or AI patent filings by the same firms).
