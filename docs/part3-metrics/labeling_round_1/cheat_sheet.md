# Labeling cheat sheet (one page)

Keep this open while you label. The examples are **made up**, so they don't give away any answers in the sample.

## 1. Is it about AI? (`about_ai`)
`Y` if the passage is really about artificial intelligence or machine learning. `N` if the keyword matched something else (e.g., "predictive models" for ordinary credit scorecards).

## 2. Evidence level (`evidence`): ask "does THIS company say IT uses AI?"
| Code | Means | Made-up example |
|---|---|---|
| **D2** | Deployed **and specific**: names a tool, use, number, role or date | "Our AI assistant answered 3 million customer questions this year." |
| **D1** | Deployed but **general**: says it uses or governs AI, no specifics | "We use AI in parts of our business." |
| **P** | **Planned or expected** use | "We intend to expand our use of AI next year." |
| **N** | **No evidence of own use**: risks, threats, competitors, laws, trends, or hedged "**may** use" | "Criminals may use AI to commit fraud." · "We may use AI in pricing." |
| **X** | **Not substantive**: definition, acronym list, heading | "AI: artificial intelligence." |

**Tie-breakers**
- A passage that mixes levels gets the **highest** one.
- "**may** use / could include" → **N** (hedged).
- About **other** companies, criminals or the economy → **N**.
- Generic forward-looking-statement lists ("…technology changes, including AI") → **N**.
- A heading alone → **X**.

## 3. Scenarios (`scenarios`): only if D1 or D2
Separate several codes with `;`.

`CX` customer service · `ADV` advice/wealth/retirement · `CREDIT` lending/underwriting · `RISKM` risk & finance models · `FRAUD` fraud/AML/KYC · `SURV` compliance & trade surveillance · `CYBER` cyber defense · `DEV` software engineering · `PROD` employee productivity tools · `OPS` operations/data/reporting · `MKT` markets & trading · `ENT` enterprise-wide, area not named

Enablers: `GOV` governance/leadership · `TALENT` training/talent · `INVEST` investment/M&A

Proposed rule (pending the Oct 22 finalization): a general sentence listing several areas ("we use AI for A, B and C") counts **once, as ENT**.

## 4. Rules of the round
- Label **on your own**, and don't compare answers until all three raters are done.
- **Don't open** `passage_labels_v0.csv` or `company_scores_v0.csv`.
- If unsure, pick your best answer and write why in `note`.
