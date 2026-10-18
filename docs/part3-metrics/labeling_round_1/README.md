# Labeling round 1: instructions for raters

**Raters:** Mehul, Logan · **Deadline:** Tue Oct 27 (end of day) · **Time:** about 60–75 minutes
**Why:** this is our inter-rater reliability check (evaluation check #2). We test whether two people using the same rules give the same labels. See the [evaluation plan](../evaluation_plan.md).

## Before you start (5 min)
1. Pull the latest `main`.
2. Read **section 4 ("Taxonomy v0")** of [`sec_test_run_taxonomy_v0_DRAFT.md`](../../part2-taxonomy/sec_test_run_taxonomy_v0_DRAFT.md), especially the **evidence-level table** and the **"Rules for unclear cases"**. That's your rulebook.
3. **Stay blind:**
   - **don't** open `data/processed/sec/passage_labels_v0.csv` or `company_scores_v0.csv`;
   - **don't** discuss items with the other rater until you've both submitted.

## Labeling
1. Copy `rater_TEMPLATE.csv` to `rater_<yourname>.csv` (e.g., `rater_logan.csv`). It opens in Excel or Google Sheets.
2. Read each passage in `sample_passages.csv`. The `item` numbers match the template, and `source_url` links to the full filing if you need context.
3. Fill in four columns for each item:

| Column | What to enter |
|---|---|
| `about_ai` | `Y` if the passage is really about artificial intelligence, otherwise `N` |
| `evidence` | **One of:** `D2` (deployed, specific: names a tool, use, metric, role or date) · `D1` (says the company uses or governs AI, no specifics) · `P` (plans or expects to use AI) · `N` (risk, threat, trend, regulation, hedged "may use" talk, or analyst questions) · `X` (definition, acronym list, heading) |
| `scenarios` | **Only if D1 or D2:** one or more codes separated by `;`. Codes: `CX`, `ADV`, `CREDIT`, `RISKM`, `FRAUD`, `SURV`, `CYBER`, `DEV`, `PROD`, `OPS`, `MKT`, `ENT`, plus the enablers `GOV`, `TALENT`, `INVEST`. Leave blank otherwise |
| `note` | Optional: why you were unsure |

Tips: a mixed passage gets its **highest** level. "May use" is **N**. Text about *other* companies or criminals using AI is **N**.

## Submit
Save the file in this folder and open a pull request named "Labeling round 1: <name>", **only after you've finished**. Mehul then runs:

```bash
python3 -m src.eval.irr
```

That prints the agreement scores and writes `disagreements.csv`, which the team discusses on Wed Oct 28.

_Sample built by `python3 -m src.eval.make_labeling_sample` (seed 20261018): 50 passages, no labels shown._
