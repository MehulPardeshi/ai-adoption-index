# 10 — Glossary (plain language)

Written for someone with **no finance or NLP background**. If a term confuses you, add it here.

## Finance and regulatory sources
- **SEC (Securities and Exchange Commission):** the US government agency that regulates public companies and markets. Public companies must file reports with it.
- **EDGAR:** the SEC's free public database of company filings. It has official APIs (programmatic access) and bulk downloads, which we use instead of scraping web pages. The SEC asks every automated request to include a **User-Agent** identifying who you are, and limits request speed (about 10 requests per second at most).
- **CIK (Central Index Key):** EDGAR's unique ID number for each filer. It's how you look a company up reliably, since names change.
- **10-K:** a company's **annual report**. Long and detailed, with sections on business, risks, and financials. It often has a "risk factors" section where AI shows up as a *risk*.
- **10-Q:** the **quarterly report**. A shorter, unaudited version of the 10-K, filed for the other three quarters.
- **8-K:** a **"something important just happened"** report (e.g., an acquisition, a new executive, a major partnership). Useful for our "investment signal" metric.
- **DEF 14A (proxy statement):** sent to shareholders before the annual meeting. It covers board members, executive pay, and votes. It sometimes mentions AI strategy or AI-related board expertise.
- **Earnings call transcript:** the written record of the quarterly call where executives discuss results with analysts. It's where firms often talk about AI most informally.
- **Investor Relations (IR) page:** the section of a company website where it posts filings, transcripts, and presentations for investors.
- **Recordkeeper (retirement):** the firm that runs the back end of a workplace retirement plan such as a 401(k). It tracks each employee's account, processes contributions, and often provides the participant website and app. Our **primary sector**.
- **Plan sponsor vs. participant:** the *sponsor* is the employer offering the retirement plan. The *participant* is the employee saving in it.
- **Decumulation:** the "spending down" phase of retirement, turning savings into income.
- **Auto-enrollment / auto-escalation:** plan features that automatically sign employees up, or automatically raise their savings rate over time.

## Industry classification codes
- **SIC (Standard Industrial Classification):** an older 4-digit US industry code. **Every EDGAR filer has one in its filing header**, so it's our most practical way to filter filings by sector (e.g., 6211 = security brokers, 6311 = life insurance).
- **NAICS (North American Industry Classification System):** the newer 6-digit replacement for SIC, used by government statistics.
- **GICS (Global Industry Classification Standard):** the industry scheme used by stock-market index providers and equity analysts. It's useful for "peer group" framing.
- **Why none of them fit perfectly:** "Retirement recordkeeper" is a *business line*, not a legal type of company, so we tag firms by what they *do*, on top of how they're *classified*.

## Text analytics / NLP
- **NLP (Natural Language Processing):** using computers to analyze human language (text).
- **Taxonomy:** a structured set of categories (here, types of AI use cases) with rules for what goes in each.
- **Inductive (derivation):** building categories *from the data up* by reading real documents first, rather than deciding categories in advance. The brief requires this for Part 2.
- **Inclusion / exclusion rules:** the written test for whether a sentence belongs in a category ("include if…", "exclude if…").
- **Mention density:** how much of a document is about AI, as a share of its total length.
- **Specificity score:** our 1–5 rating of how concrete an AI statement is. "We are exploring AI" is low. "We deployed tool X, which cut call-handling time by Y%" is high. The exact anchors are for the team to define.
- **Sentiment / tone:** whether language is positive, negative, or neutral. In finance, words like "liability" or "risk" mean something different than in everyday text, which is why generic tools misfire.
- **Loughran-McDonald dictionary:** a word list built specifically for financial documents (positive, negative, uncertainty, litigious, etc.). It's the standard for financial-text sentiment.
- **Forward-looking vs. retrospective:** "we *will* deploy" (plan) vs. "we *deployed*" (done). It's often detected through tense and modal verbs (will, may, plan to, expect).
- **Modal verb:** words like *may, might, could, will, should* that signal possibility or intent rather than fact.
- **LLM (Large Language Model):** an AI model like Claude or GPT that reads and writes text. Here it could be used to help classify or score sentences, but it still needs human validation.

## Measurement and validity
- **Inter-rater reliability (IRR):** do two people using the same rubric give the same score? If not, the rubric is too vague to trust.
- **Cohen's kappa (κ):** a number measuring agreement between **two** raters, *correcting for agreement you'd get by chance*. 1 = perfect agreement; 0 = no better than chance. As a rough convention, above ~0.6 is often called "substantial." For **ordered** scales like 1–5, a **weighted kappa** gives partial credit for near-misses (a 3 vs. a 4 is less wrong than a 1 vs. a 5). For **more than two** raters, people use pairwise kappas or **Fleiss' kappa**. Which one we use is a team decision.
- **Validity:** does the metric measure what we claim? (Mentioning AI isn't the same as using it.)
- **Reliability:** does the metric give consistent results when repeated?

## Index construction
- **Index:** a single number combining several metrics, tracked over time (like a stock index combines many stock prices).
- **Unit of analysis:** the "row" we score. Here, one **firm-sector-quarter** (e.g., "Voya, Retirement, 2025 Q2").
- **Normalization:** putting metrics on a common scale so they can be added together.
- **Z-score:** how many standard deviations a value is above or below the group average. 0 = average; +1 = one standard deviation above.
- **Min-max scaling:** rescales values so the lowest is 0 and the highest is 1.
- **Peer universe:** the group you compare against when normalizing (e.g., all recordkeepers, or all firms).
- **Weighting:** how much each metric counts in the final index. **Equal-weighted** = every metric counts the same.
- **Backfill:** collecting and scoring *historical* data (past quarters) so the index has a trend from day one.
- **Refresh protocol:** the step-by-step checklist for updating the index each quarter.
- **Calendar vs. fiscal quarter:** some firms' financial years don't start in January, so their "Q1" may not match the calendar Q1.

## Course / tooling terms
- **Agentic workflow:** an AI setup where a model plans and takes multi-step actions (using tools), not just one-shot Q&A.
- **Agentic tool:** a function an AI agent can call (e.g., "fetch filings for CIK X"), with a docstring written so the agent knows exactly when and how to use it.
- **Guardrails:** checks that stop an AI system from doing harmful or wrong things (e.g., refusing to quote paywalled text verbatim).
- **Kanban board:** a board of task cards in columns (To Do / In Progress / Done).
- **Repo (repository):** this project folder, tracked by git and hosted on GitHub.
