# Labeling cheat sheet, round 2 (one page)

> **v2, Oct 27.** Same rules as round 1. They now match the frozen codebook ([taxonomy §4](../../part2-taxonomy/sec_test_run_taxonomy_v0_DRAFT.md), #84) word for word. **What's new is marked 🆕.** The examples are **made up**, so they don't give away any answers in the sample.

## 1. Is it about AI? (`about_ai`)
`Y` if the passage talks about artificial intelligence or machine learning **in any way**. 🆕 That includes **AI risks, criminals or competitors using AI, AI laws, and AI trends**: those passages are about AI; they just get **N** in step 2.
`N` **only** if the keyword matched something that isn't AI at all (e.g., "predictive models" for ordinary credit scorecards). Then evidence is **X**.

## 2. Evidence level (`evidence`): ask "does THIS company say IT uses AI?"
| Code | Means | Made-up example |
|---|---|---|
| **D2** | Deployed **and specific**: names a tool, use case, number, 🆕 **oversight body**, role or date | "Our AI assistant answered 3 million customer questions this year." |
| **D1** | Deployed but **general**: says it uses or governs AI, no specifics | "We use AI in parts of our business." |
| **P** | **Planned or expected** use | "We intend to expand our use of AI next year." |
| **N** | **No evidence of own use**: risks, threats, competitors, laws, trends, or hedged "**may** use" | "Criminals may use AI to commit fraud." · "We may use AI in pricing." |
| **X** | **Not substantive**: definition, acronym list, heading, or a keyword hit that isn't about AI (`about_ai` = N) | "AI: artificial intelligence." |

**Tie-breakers**
- A passage that mixes levels gets the **highest** one.
- 🆕 A **risk-factor passage is still D1** if it says the company itself uses AI ("the models we use, including ones that use machine learning, may be wrong" → D1).
- "**may** use / could include" → **N** (hedged). Examples listed after "may include" earn no scenario.
- About **other** companies, criminals or the economy → **N**.
- Generic forward-looking-statement lists ("…technology changes, including AI") → **N**.
- A heading alone → **X**. 🆕 That holds even if the heading says "our use of AI"; label the paragraph under it on its own.

## 3. Scenarios (`scenarios`): required for D2, D1 and P; leave blank for N and X
Separate several codes with `;`. For **P**, use the scenario of the *planned* use.

`CX` customer service · `ADV` advice/wealth/retirement · `CREDIT` lending/underwriting · `RISKM` risk & finance models · `FRAUD` fraud/AML/KYC · `SURV` compliance & trade surveillance · `CYBER` cyber defense · `DEV` software engineering · `PROD` employee productivity tools · `OPS` operations/data/reporting · `MKT` markets & trading · `ENT` enterprise-wide, area not named

Enablers: `GOV` governance/leadership · `TALENT` training/talent · `INVEST` investment/M&A

🆕 **Rule (frozen Oct 27, #84):** a general sentence listing several areas ("we use AI for A, B and C") counts **once, as ENT**.

## 4. 🆕 Practice first (2 minutes, made-up passages)
Cover the answers, label these six, then check. If you miss one, re-read the rule next to it.

| # | Made-up passage | about_ai | evidence | scenarios | Rule |
|---|---|---|---|---|---|
| 1 | "Generative AI could let criminals create convincing fake identities, increasing our fraud losses." | Y | N | | About criminals' AI: about AI, but no own use |
| 2 | "New state laws on AI in lending may raise our compliance costs." | Y | N | | AI law: about AI, no own use |
| 3 | "We rely on models, including some that use machine learning, to estimate credit losses; these models may be inaccurate." | Y | D1 | RISKM | Risk factor that says the company uses AI |
| 4 | "Our predictive models for card underwriting use bureau scores and income data." | N | X | | Keyword hit, not AI |
| 5 | "In 2025 our AI Risk Committee, chaired by the Chief Risk Officer, reviewed 40 models." | Y | D2 | GOV | Names an oversight body and a number |
| 6 | "We expect to roll out AI assistants for our call-center staff next year." | Y | P | CX | Planned use |

## 5. Rules of the round
- Label **on your own**, and don't compare answers until all three raters are done.
- **Your own judgment on every label.** AI tools are fine for opening files, not for choosing labels.
- **Don't open** `passage_labels_v0.csv`, `company_scores_v0.csv` or any `agent_labels_*.csv`.
- If unsure, pick your best answer and write why in `note`.
