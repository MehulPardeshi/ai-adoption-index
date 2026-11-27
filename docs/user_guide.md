# Using the AI Adoption Index Dashboard

Open the [AI Adoption Index dashboard](https://ai-adoption-index.streamlit.app) to explore scores based on what financial firms report in SEC annual (10-K) and quarterly (10-Q) filings. The dashboard does not check whether firms use AI in practice.

## Choose a view

The dashboard has three tabs:

- **Sector Overview** compares annual scores for six selected firms: JPMorgan Chase, Bank of America, Capital One, Wells Fargo, Charles Schwab, and Principal Financial Group. The chart shows two ways of combining their AI Use Scores. Equal weighting gives each firm the same influence. Market-cap weighting gives more influence to firms with a larger public float, based on SEC filings. This is a small research sample, not a measure of the entire financial-services sector.
- **Company Scores** lets you compare individual firms for a fiscal year and look at their scores over time. Citigroup appears here as a benchmark, but it is not part of the six-firm sector index.
- **About the Data** describes the sources, score definitions, and limits of the data.

In **Sector Overview**, the question marks above the table explain its columns.

## Compare company scores

In **Company Scores**:

1. Choose a fiscal year.
2. Select the firms you want to compare. All firms are selected by default.
3. Review the table. The scenario names show the areas of AI use represented in the scores.
4. Choose an **Annual trend metric** below the table to see how that measure changes over time.
5. Select the question mark beside a metric name to read its definition.

Compare the same metric and fiscal year when looking across firms. A firm with no score for a year is marked as unavailable. It is not treated as having a score of zero.

## Understand the scores

Passages in company filings are assigned an evidence level. The levels used in scoring are:

| Level | What it means | Points |
|---|---|---:|
| D2 | The company describes a specific use of AI. | 3 |
| D1 | The company says it uses AI, but gives few details. | 1 |
| P | The company describes a plan to use AI. | 0.5 |
| N | The passage does not show the company's own AI use. It may discuss risks, regulation, or AI more generally. | 0 |
| X | The passage is not substantive AI evidence and is left out of scoring. | Not scored |

For each business area, the scoring keeps the strongest evidence for that firm and year. The **AI Use Score** combines these results across areas and scales them to 0 to 100. Repeated mentions in one area do not automatically add points. The **Readiness Score** summarizes disclosures about AI governance, talent, and investment. **Talk Ratio (%)** is the share of substantive AI passages that do not show evidence of the company's own AI use. A higher Talk Ratio means more of those passages describe AI without showing the company's own use. It does not mean the company talks about AI more often overall.

Keep these points in mind when reading a score:

- People agreed on labels for 80 of 277 passages. The remaining passages use AI-generated draft labels that were not reviewed one by one by a person.
- A score of zero means the available disclosures contained no use that received points. It does not prove that the firm does not use AI.
- The dashboard hides incomplete fiscal years. It does not show passage-level quotes or citations, so the scores cannot be checked against individual passages from this page.
- These scores describe disclosures, not verified company-wide adoption or organizational readiness. They are not investment advice.

## Download the data

The download buttons are above their respective tables:

- **Download company scores (CSV)** saves scores for all firms and complete fiscal years. The download is not limited to the firms or year selected in the comparison. The file is named `ai_adoption_index_company_scores.csv`.
- **Download sector index (CSV)** saves annual sector results, including both weighting methods, public float, and the firms included. The file is named `ai_adoption_index_sector_index.csv`.

Open a CSV in a spreadsheet program if you want to sort, filter, or do your own calculations.

## Updating the index

The dashboard does not update itself when new filings are published. A yearly refresh is a manual process: collect the new SEC filings, run the labeling workflow, review passages that need attention, recalculate the scores, and update the data used by the dashboard.

The [AI Adoption Index skill](../skills/ai-adoption-index/SKILL.md) contains the setup steps, commands, and checks for maintainers. It is a technical process, not a button in the dashboard. Follow the skill rather than editing score files by hand.
