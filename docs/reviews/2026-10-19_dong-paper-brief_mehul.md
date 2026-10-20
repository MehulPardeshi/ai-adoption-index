# Dong, Doukas & Zhang: reading brief (Mehul, for the Oct 25 meeting)

> **Paper:** Dong, F., Doukas, J. A., and Zhang, R., *"Artificial Intelligence Engagement, Firm Value, and Risk Transformation"*, working paper, SSRN 6051714 (63 pp.; the version we have is dated **January 2026**; not yet peer-reviewed). Dataset: github.com/FengDong-Elon/ai-intensity-dataset. **Cite both whenever we use the data.**
> **Status:** ✅ **checked against the full paper** (PDF supplied by Mehul on Oct 19; kept locally, not committed, because it's the authors' copyrighted work). Prepared with Claude Code, plus our own analysis of Dong's numbers for our companies (`data/processed/sec/shu_run/dong_baseline_6firms.csv`).

## The paper in 6 bullets
1. **What they measure:** "AI engagement" = how intensively a company's **full 10-K annual report** discusses AI. One score per firm per year, **all U.S. public firms, 2010–2024** (financial firms included). They deliberately use 10-Ks rather than earnings calls, which they see as conversational and prone to hype or "AI-washing".
2. **The dictionary:** about **500 terms and phrases** curated from AI standards (NIST AI RMF, OECD AI Recommendation, EU AI Act, ISO/IEC 42001) plus technical glossaries, in **8 non-overlapping groups**: core AI concepts; model architectures; generative AI/LLMs; data, training & evaluation; robustness, security & AI-specific risk; infrastructure & deployment; reinforcement learning & robotics; AI compliance categories. They **exclude** broad ethics words (fairness, equity, sustainability). **The term list isn't published.**
3. **Matching:** phrase-level (1–3-word) exact matching on lower-cased full text, without stemming. Everyday words with AI meanings (**model, network, learning**) count only inside an AI phrase (e.g., "neural network"). A manual check of random filings found few false positives.
4. **The score:** **AI Intensity = AI-term matches ÷ total words × 1,000.** **Core** = only the core-concept and model-architecture groups; **All** = all 8 groups. The authors treat **Core as the better proxy** for real engagement, and most results use Core.
5. **Findings** (associations, not proven causation):
   - Firms whose AI talk rises later show **faster sales growth, more investment, higher profitability and slower employment growth**. AI talk also tracks AI hiring, AI patents, automation and R&D.
   - **Higher valuations:** one standard deviation more AI talk goes with about **+0.19 Tobin's Q** (also higher P/E and EV/EBITDA), and tests suggest it's not just reverse causality.
   - **Why:** mostly a **lower cost of equity** (investors see less risk), not higher expected cash flows. Analysts forecast these firms more accurately.
   - **"Risk transformation":** after 2020, high-AI firms **move more with technology-sector stocks**, and they reacted more positively to the ChatGPT (Nov 2022) and GPT-4 (Mar 2023) launches.
   - Governance: CEO incentives and **boards with technology expertise** go with more AI talk; boards with **legal** expertise with less.
6. **Limits:**
   - It **counts AI vocabulary; it doesn't tell real use from talk** (risk-factor mentions count the same as deployments).
   - The term list isn't public, coverage is annual only, the data stops in 2024, and it's a working paper.

### ⚠️ Corrections to our earlier notes
- **The risk finding:** Shu's review says AI shifts risk "from systematic to firm-specific (higher idiosyncratic volatility)". The paper actually reports a **lower cost of equity**, a **better information environment**, and **more exposure to technology-sector (systematic) risk**. I've added a note to Shu's review.
- **The "count only inside a phrase" rule** is about everyday words like *model, network, learning*, not specifically "AI".
- **Date:** January 2026 (the version we have), not 2025.

## What their data says about OUR companies (FY2023 annual reports, the latest they cover)
| Company | AI Intensity (All) | AI Intensity (Core) | Matches | Note |
|---|---|---|---|---|
| Bank of America | 0.24 | 0.11 | 21 | Average rose from 0.05 (2010–22) to 0.21 (2023–24) |
| Capital One | 0.19 | 0.07 | 16 | |
| JPMorgan Chase | 0.09 | 0.06 | 8 | An unexplained 2015 spike (0.45) is worth a look |
| Charles Schwab | 0.07 | 0.01 | 5 | |
| Principal Financial | 0.00 | 0.00 | 0 | Genuine: we also find 0 for FY2023 |
| Wells Fargo | **0.00** | **0.00** | **0** | **Data defect:** their parser missed the 10-K body (Exhibit 13); we find 5–12 mentions per year |

- **Our banks are AI-heavy talkers by their yardstick.** The all-firm average for All is about **0.035** in 2024, and more than half of all firm-years score **zero**. Bank of America's 0.24 is about **7×** the all-firm average. On Core, the Finance industry averaged about **0.008** in 2018–2024, and Bank of America (0.11), Capital One (0.07) and JPMorgan (0.06) are far above it.
- **Risk talk dominates even in their measure:** across our six companies, **27 of 50 matches (54%) are in the "robustness, security & AI-specific risk" group**, 19 are core-concept terms, and **none** are in "infrastructure & deployment". This fits our finding that only about 1 in 8 AI passages shows real use.
- **Markets didn't reward AI talk in finance:** around the ChatGPT and GPT-4 launches, high-AI firms beat low-AI firms overall, but in the **"Money" (finance) industry the difference was about zero and not significant**.

## Why it matters for us (talking points)
1. **It's our baseline, and our contribution is clear next to it:** they measure *how much firms talk about AI*; we separate *use from talk* (evidence levels D2/D1/P/N/X). Their own data shows over half of our banks' AI vocabulary is risk-related.
2. **Evaluation check 4b:** compare with their **Core** score (the authors' preferred one). We expect it to track our *talk* volume more than our *use* score. Re-count Wells Fargo on the full filing first.
3. **Earnings calls, a trade-off to discuss:** the authors avoid calls because of hype. We want calls because they name real products (Erica, LLM Suite). Our evidence levels and "management statements only" rule are how we control the hype. That's worth saying to Julie.
4. **For Julie:** the Wells Fargo zero shows why checking matters. A dataset many will use can silently miss a major bank.
5. **Ideas worth borrowing:** a standards-based term list; counting ambiguous words only inside AI phrases; their 8 groups as a cross-check on our keyword list.
6. **TP3 research paper:** this is relevant and recent (Jan 2026) but **not yet peer-reviewed**. A stronger peer-reviewed option they build on: **Babina, Fedyk, He & Hodson (2024), "Artificial intelligence, firm growth, and product innovation", *Journal of Financial Economics* 151.** Consider citing both.

## Questions for Sunday
- Do we use their 8 groups to sanity-check our keyword list?
- Who re-counts Wells Fargo on the full 10-K for the comparison? (Shu's run already reads it.)
- Which research paper do we pick for TP3: Dong et al. (working paper) or Babina et al. (2024, peer-reviewed), or both?
