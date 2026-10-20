# Dong, Doukas & Zhang: reading brief (Mehul, for the Oct 25 meeting)

> **Paper:** Dong, F., Doukas, J. A., and Zhang, R., *"Artificial Intelligence Engagement, Firm Value, and Risk Transformation"*, working paper, SSRN 6051714 (2025). Dataset: github.com/FengDong-Elon/ai-intensity-dataset. **Cite both whenever we use the data.**
> **How this brief was made:** prepared with Claude Code from (1) Shu's notes from reading the full paper ([review](2026-10-17_dong-et-al-paper-review_shu.md)), (2) the dataset's README, and (3) our own analysis of Dong's numbers for our six companies (`data/processed/sec/shu_run/dong_baseline_6firms.csv`). SSRN blocks automated access, so the PDF itself wasn't machine-read. Mehul to skim the paper's introduction and conclusion to confirm.

## The paper in 5 bullets
1. **What they measure:** "AI engagement" = how much a company's **10-K annual report** talks about AI, for U.S. public firms, **2010–2024**, one score per firm per year.
2. **How:** a dictionary of **~500 AI terms** taken from standards documents (NIST AI RMF, OECD AI principles, EU AI Act, ISO/IEC 42001), in **8 groups**: core AI concepts; model architectures; generative AI/LLMs; infrastructure; reinforcement learning/robotics; data and training; compliance; robustness/security/AI risk. Ambiguous words like "AI" only count inside longer phrases.
3. **The score:** **AI Intensity = AI-term matches ÷ total words × 1,000.** "Core" uses only the core-concepts and model groups; "All" uses all 8.
4. **Findings:** firms that talk more about AI have **higher value** (Tobin's Q) but also **more firm-specific risk**: AI shifts risk from market-wide to company-specific ("risk transformation"). AI talk **jumps after 2022** (ChatGPT).
5. **Limits:** it **counts words; it can't tell real use from talk**. The dictionary isn't published, it covers annual reports only (no quarterly signal), and the data stops in 2024.

## What their data says about OUR companies (FY2023 annual reports, the latest they cover)
| Company | AI Intensity (All, per 1,000 words) | AI-term matches | Note |
|---|---|---|---|
| Bank of America | 0.24 | 21 | Highest; average quadrupled from 0.05 (2010–22) to 0.21 (2023–24) |
| Capital One | 0.19 | 16 | |
| JPMorgan Chase | 0.09 | 8 | An unexplained 2015 spike (0.45) is worth a look |
| Charles Schwab | 0.07 | 5 | |
| Principal Financial | 0.00 | 0 | Genuine: we also find 0 for FY2023 |
| Wells Fargo | **0.00** | **0** | **Data defect:** their parser missed the 10-K body (Exhibit 13); we find 5–12 mentions per year |

- **Risk talk dominates even in their measure:** across our six companies, **27 of 50 matches (54%) are in the "Robustness, Security & AI-Specific Risk" group**, 19 are generic "core AI concept" terms, and **none** are in the "Infrastructure & Deployment" group. That matches our finding that only about 1 in 8 AI passages shows actual use.
- **AI is still a tiny share of these reports:** even the highest (Bank of America, 0.24 per 1,000 words) is about one AI term per 4,000 words; the six-company average is about 0.1 (one per 10,000).

## Why it matters for us (talking points)
1. **It's our baseline, and our contribution is clear next to it:** they measure *how much firms talk*; we separate *use from talk* (Label B: D2/D1/P/N/X).
2. **Evaluation check 4b:** their scores should track our *talk* volume more than our *use* score. If they do, that shows our measure adds information. Re-count Wells Fargo on the full filing first.
3. **For Julie:** the Wells Fargo zero shows why checking matters. A widely usable dataset can silently miss a major bank.
4. **Ideas worth borrowing:** a standards-based term list is a defensible source for our keyword list, and the "count 'AI' only inside phrases" rule cuts false positives.
5. **TP3 research paper:** a strong candidate (2025, directly on our method). Confirm its posting date on SSRN.

## Questions to raise on Sunday
- Do we adopt any of their 8 groups as a check on our keyword list?
- Who re-counts Wells Fargo on the full 10-K for the comparison? (Shu's run already reads it.)
