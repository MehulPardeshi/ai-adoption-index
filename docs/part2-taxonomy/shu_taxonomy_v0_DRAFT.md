# Taxonomy v0 (draft) — how the six PoC firms talk about AI in SEC filings

Prepared by Shu Pu (data: 66 filings, 10-K + 10-Q, filed 2024-01-01 to 2026-08-07; see `data/processed/sec/shu_run/`). **DRAFT** — to be merged into Yen-Chu's `sec_test_run_taxonomy_v0_DRAFT.md` (#33) before the team votes.
Status: draft for the Oct 18 team meeting. To be merged with Yen-Chu's reading before taxonomy v0 goes to Mehul on Oct 27.

Firms: JPMorgan Chase (JPM), Bank of America (BAC), Capital One (COF), Wells Fargo (WFC), Charles Schwab (SCHW), Principal Financial (PFG).

## 1. What the filings actually contain

274 keyword hits across 66 filings, 169 unique passages after removing text repeated across quarters. Almost all of it sits in Risk Factors (Item 1A), the forward-looking-statements boilerplate, and the model-risk part of MD&A. There is very little "we deployed X" language in 10-K/10-Q; that lives in annual letters, earnings calls and press releases, which are out of scope for the PoC.

| Firm | 10-K FY2023 (hits / per 1k words) | 10-K FY2024 | 10-K FY2025 | 10-Qs (typical) | Character of the text |
|---|---|---|---|---|---|
| COF | 36 / 0.35 | 43 / 0.40 | 68 / 0.58 | 1 hit (boilerplate), except Q2-2025 (46, Discover deal) | Most concrete. Names model use cases, says it builds GenAI capabilities, discusses agentic commerce. |
| BAC | 17 / 0.15 | 42 / 0.36 | 40 / 0.35 | 1–2 hits (boilerplate) | Almost entirely risk language, but FY2024 adds "internal processes and governance frameworks" for AI; FY2025 adds autonomous agents. |
| JPM | 6 / 0.04 | 19 / 0.12 | 33 / 0.21 | 0 hits in 2024–2025, 1 in 2026 | Risk + regulation + model risk; FY2025 adds a dedicated risk factor on generative and agentic AI. |
| WFC | 5 / 0.04 | 6 / 0.05 | 12 / 0.11 | 0 until 2026, then 2 | One recurring "we also use AI to…" sentence; FY2025 names a Head of Artificial Intelligence. |
| SCHW | 1 / 0.01 | 2 / 0.03 | 5 / 0.07 | 0 until 2026, then 1–2 | Model risk + fraud; 2026 10-Q adds "development and deployment of AI capabilities" as a forward-looking item. |
| PFG | 0 | 6 / 0.05 | 7 / 0.06 | 0 (1 in Q2-2026) | Almost nothing until FY2024; 2026 10-Q discloses acquiring Beam Benefits, "AI at its core". |

Observations worth telling Julie:
- Disclosure intensity roughly doubled or tripled from FY2023 to FY2025 at every firm. The change is mostly new or expanded risk factors, not new deployments.
- 10-Qs add almost nothing beyond the 10-K; quarterly granularity from SEC text alone will be flat. Earnings calls will be needed for quarter-to-quarter movement.
- The Dong et al. baseline gives WFC 0 for every year because its parser missed the second document (`_d2.htm`) that holds the annual report body; our pass finds 5–12 hits per year.

## 2. Proposed categories (dimension A: what the AI is used for)

Each category lists an anchor passage. Accession numbers point to `ai_passages_all.json`; the agent should cite these the same way.

### A1. Risk, credit and financial modeling
AI/ML inside the models used for credit decisions, loss forecasting, capital, valuation, stress testing.
- COF 10-K FY2025 (0000927628-26-000024): "determining the pricing of products, identifying potentially fraudulent transactions, grading loans, extending credit, measuring market and interest rate risks, predicting deposit levels or loan losses, assessing capital adequacy, estimating the value of financial instruments…"
- JPM 10-K FY2024 (0000019617-25-000270), MD&A model risk: "models… including those based upon machine learning or artificial intelligence techniques… valuation of positions and measurement of risk, assessing regulatory capital requirements, conducting stress testing, evaluating the allowance for credit losses."
- SCHW 10-K FY2024 (0000316709-25-000010): "Model uses at Schwab include… calculating capital requirements… estimating interest and credit risk… identifying and preventing fraud… guidance in the management of client portfolios. Schwab manages model risk, including use of artificial intelligence…"
- COF 10-K FY2023/FY2025: credit cards "underwritten using an automated underwriting system based on predictive models that we have developed" (no AI keyword, but this is the deployed system; flag for discussion).

### A2. Fraud detection and financial crime
AI used by the firm to detect fraud, and (separately, see C-dimension) AI used by attackers.
- COF FY2025: "identifying potentially fraudulent transactions" (firm use).
- SCHW FY2024: "identifying and preventing fraud and other financial crimes" (model use).
- WFC FY2025, BAC FY2024/25, COF FY2024/25, JPM FY2024/25: generative AI enabling identity fraud, synthetic voice/video, harder authentication (threat, not adoption).

### A3. Operations, automation and internal efficiency
AI to automate business decisions, operations, data management, software development.
- WFC 10-K FY2023/FY2024/FY2025 (0000072971-24-000064 etc.): "We also use artificial intelligence to help further inform or automate certain business decisions, operations, and risk management practices, as well as to improve our customer service" — FY2025 adds "to help improve efficiency… enhance our models and data management activities."
- COF FY2025: "software development… and other operational functions."
- BAC FY2023–25: "implement emerging technologies, such as automation, AI, machine learning and robotics" in data management.
- BAC 10-Q 2026: forward-looking statement now mentions "the ability to achieve potential benefits, such as increased productivity and cost savings."

### A4. Customer experience, service and personalization
- COF FY2025: "personalizing customer experiences."
- WFC FY2023–25: "to improve our customer service."
- SCHW 10-Q Q1-2026: "The Company's development and deployment of artificial intelligence capabilities" listed among forward-looking items.

### A5. Products and competitive positioning
AI as something competitors may deploy faster; AI as part of product strategy; agentic commerce.
- JPM FY2025 (0001628280-26-008131): "If JPMorganChase does not keep pace with rapidly changing technological advances, including the adoption of generative AI, it risks losing clients…"; "replacement or disintermediation of direct customer relationships if AI agents autonomously manage or intermediate financial decisions."
- COF FY2025: "the growth of agentic commerce, in which autonomous AI agents initiate and execute transactions on behalf of users."
- BAC FY2025: "we expect greater AI adoption by our third parties, clients, counterparties… including emerging third-party AI services and autonomous AI agents."
- PFG 10-Q Q2-2026: acquisition of Beam Benefits, "a cloud-native technology stack with artificial intelligence at its core" (product/distribution via acquisition).

### A6. Workforce and skills
- JPM FY2024/25: "advances in technology, such as automation, AI and data science, could lead to workforce displacement… compete for employment candidates who possess more advanced technological skills"; "over-reliance on AI could… hinder… critical thinking, problem-solving, judgment."
- JPM FY2024: voluntary training programs covering "artificial intelligence, data literacy."
- PFG FY2025: "In 2025, we implemented enterprise-wide artificial intelligence and data literacy training."
- WFC FY2025: Saul Van Beurden named "Co-CEO of Consumer Banking and Lending, and Head of Artificial Intelligence since November 2025."
- COF FY2025: "advances in technology, such as automation and AI, may lead to workforce evolution."

### A7. Governance, model risk and responsible AI
- BAC FY2024: "To address AI-related risks, we have implemented internal processes and governance frameworks."
- JPM FY2025: dedicated risk factor on "generative and agentic AI systems… AI system failures, inappropriate use… inaccurate or biased output."
- COF FY2023–25: "policies, programs, processes and practices governing how data, models and AI are acquired, validated, stored, protected, processed and analyzed."
- SCHW FY2024: model inventory, independent validation, annual review.

### A8. Regulation and compliance exposure
- JPM FY2024/25: "Data, privacy, cybersecurity and artificial intelligence regulation"; EU AI Act phased in from Feb 2025.
- PFG FY2024: "EU AI Act, Colorado AI Act, and other AI-related legislation."
- COF FY2025: Colorado and California AI laws; IP ownership of GenAI output unresolved.
- BAC FY2025: AI laws "imposing various obligations, including AI governance and risk management, transparency and consumer disclosures."

### A9. Cybersecurity threat from AI (external)
Not adoption by the firm, but the most frequent AI mention in every filing. Keep as a category so the agent can separate it out rather than count it as adoption.
- All six firms, every 10-K: AI enabling phishing, social engineering, vulnerability discovery, deepfakes.

## 3. Dimension B: stance (the deployed / planned / buzzword question)

Proposed labels for `classify_passage`:

| Label | Definition | Example |
|---|---|---|
| deployed | Present-tense statement that the firm uses AI for a named purpose. | WFC "We also use artificial intelligence to… automate certain business decisions"; COF model-use list; SCHW model uses. |
| planned / investing | Future or ongoing investment, no named live use. | COF "We continue to invest in building new capabilities that use new AI technologies, such as generative AI"; SCHW "development and deployment of AI capabilities"; PFG Beam acquisition (pending close). |
| governance | Describes controls, policies, training, org roles around AI. | BAC governance frameworks; PFG/JPM AI literacy training; WFC Head of AI. |
| risk / external | AI framed as a risk source, a competitor's weapon, or a regulatory burden. No claim of use. | Cyber-threat passages; "competitors may deploy AI faster"; EU AI Act. |
| boilerplate | Forward-looking-statement lists, acronym tables, cross-references. | BAC/COF forward-looking bullets repeated in every 10-Q; "AI: Artificial Intelligence" in acronym lists. |

Rough tally from the 169 unique passages using a keyword heuristic (to be replaced by human labels on Oct 28): deployed 9, planned 5, governance 4, boilerplate 7, risk/external 144. Even allowing for the heuristic being crude, the point for Julie holds: roughly 85% of AI mentions in these filings are about AI as a threat, a competitor's tool, or a regulation, not as something the firm says it does.

## 4. Dimension C (optional): Vanguard's augmentation / efficiency / transformation

From the Vanguard Megatrends report Julie shared. Only apply to `deployed` and `planned` passages.
- augmentation: AI helps employees do more (WFC "inform… business decisions"; JPM training).
- efficiency: AI replaces or automates tasks (WFC "automate… operations"; BAC "productivity and cost savings"; COF "software development").
- transformation: AI changes the product or the business model (COF agentic commerce; JPM AI agents intermediating customer relationships; PFG Beam).

## 5. Open questions for the Oct 18 meeting

1. Do we count model-risk passages (JPM, SCHW, COF) as adoption? They are the clearest evidence that AI/ML is inside production models, but the firms frame them as risk.
2. Automated underwriting at COF uses "predictive models" without the word AI. Should the dictionary include "predictive model", "automated underwriting", "algorithmic"?
3. Dong et al.'s 8 technical categories (GenAI/LLM, infrastructure, RL…) barely appear in these filings; only "generative AI" and "agentic" show up. Keep the technical dimension as a tag, not a category.
4. 10-Q text is nearly empty of AI content. Confirm with Julie whether quarterly points should come from earnings calls (Yen-Chu's source) instead.
