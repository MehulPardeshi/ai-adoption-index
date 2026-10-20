# Review of the paper behind the AI Intensity dataset (#25, meeting form 1b)

**By:** Shu Pu · **Date:** Oct 17, 2026 · Read from the SSRN PDF (human-downloaded; SSRN blocks automated access). Listed as #3 in [`docs/references.md`](../references.md).

Dong, F., Doukas, J. A., and Zhang, R., *"Artificial Intelligence Engagement, Firm Value, and Risk Transformation"*, working paper, SSRN 6051714 (2025).

## What the paper does
Builds a firm-year measure of **AI engagement** from the text of 10-K filings for U.S. public firms, 2010–2024, then relates it to firm value and risk.

**Dictionary.** ~500 AI terms drawn from standards documents (NIST AI RMF, OECD AI principles, EU AI Act, ISO/IEC 42001) rather than from word embeddings, grouped into **8 sub-dictionaries**: core AI concepts, model architectures, generative AI / LLMs, infrastructure and tooling, reinforcement learning, data and training, applications, and governance/ethics terms. The dictionary itself is **not published** with the dataset.

**Text processing.** Phrase-level matching on uni-, bi- and trigrams over the full 10-K text; ambiguous tokens (e.g. "AI", "ML") are counted only inside a longer phrase; no stemming. **AI Intensity = matches / total words × 1,000.** "Core" uses only the core-concepts and model-architecture sub-dictionaries; "All" uses all eight.

**Findings.** Higher AI intensity is associated with higher Tobin's Q, but also higher idiosyncratic volatility: AI shifts a firm's risk from systematic to firm-specific (the "risk transformation" in the title). Intensity jumps after 2022 (ChatGPT).

## What it means for us
1. **It counts words; it does not distinguish use from talk.** That gap is exactly our contribution (Yen-Chu: ~1 in 8 passages shows real use; Shu's run: ~85 % of unique passages are risk / regulation / cyber-threat language).
2. **It is our baseline, but it needs re-checking.** For Wells Fargo the dataset gives **0 every year**. Their WFC word count (~117.8k) matches the first file of the 10-K plus exhibits and excludes the ~110k-word `wfc-YYYYMMDD_d2.htm` body, so their parser appears to have missed that second file; our pass finds 5–12 AI mentions per WFC 10-K. PFG's 0 for FY2023 is genuine. Our six firms' rows are in `data/processed/sec/shu_run/dong_baseline_6firms.csv`.
3. **Annual only.** 10-K text, so no quarterly signal; our own 10-Q pass confirms 10-Qs carry almost no AI text. Quarterly movement must come from earnings calls (#34).
4. **Good candidate for TP3's research paper** (recent, peer-review-track working paper, directly on our method). Must be cited whenever the dataset is used.
5. **Dictionary design choice for the agent:** their standards-based phrase list is a defensible source for our own keyword list, and the "ambiguous token only inside a phrase" rule is worth copying for `AI`.
