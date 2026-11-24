# Final README draft (TP3 project report, #166)

> **Status:** skeleton v0.1, Mehul, Nov 24. Each section names its owner. **Rewrite your section in place by Sun Nov 29**; Mehul swaps this into `README.md` on Tue Dec 1 (the current README's setup and commands move to a "For developers" section at the end). Starter text marked *(starter)* is a placeholder for the owner to replace. Course list of what the README needs: concept visuals, narrow scope, project details, What's next, Responsible AI, references with ≥1 recent research paper, authors with GitHub links and bios.

---

# AI Adoption Index: Financial Services

**How much do large U.S. financial firms actually *use* AI, as opposed to just *talking* about it?** We read every 10-K and 10-Q of the 76 S&P 500 Financials firms with an AI agent, had people check its work, and turned it into a yearly index on a [live dashboard](https://ai-adoption-index.streamlit.app).

**Headline (FY2025):** sector AI Use Score **8.6** (equal-weighted) / **10.2** (market-cap-weighted), up from 6.4 / 6.6 in FY2024. 65 of 76 firms disclose some AI use or plans; 11 disclose none.

<!-- Snehal: concept visual here (pipeline diagram: filings → agent → human check → score → dashboard) -->

## 1. The problem and our scope · owner: Yen-Chu
*(starter)* Our client, Julie Agnew (William & Mary; named with her permission), is writing a book chapter on AI in financial services and retirement. Press releases and AI word counts can't tell real use from hype. We built a repeatable, public-data measure of **disclosed** AI use:
- **Firms:** the 76 S&P 500 Financials (banks, insurers, asset managers and brokers, payments and consumer finance, exchanges and data), after a 6-firm pilot plus Citi.
- **Source:** SEC 10-K and 10-Q filings only, FY2024–2025 (606 filings, 2,353 AI passages). Free and public, so anyone can rerun it.
- **Out of scope:** earnings-call transcripts (licensed; team decision Nov 8), job postings, firms outside Financials.

## 2. How it works · owner: Shu (agent), Yen-Chu (data + index)
*(starter)*
1. **Find:** download filings from SEC EDGAR and pull out every passage mentioning AI.
2. **Label:** an AI agent (DeepSeek, 7 custom tools) labels each passage with one of 11 business areas and a level: specific use (D2), general use (D1), plans, risk talk, or not about AI. It must quote the filing word for word.
3. **Guardrail:** labels under 0.70 confidence, or whose quote isn't found in the filing, go to a person (200 of 2,353).
4. **Score:** each area counts once a year at its highest level; the firm's AI Use Score = points ÷ 33 × 100.
5. **Index:** the sector index averages firm scores equal-weighted and weighted by public float.
6. **Dashboard:** Streamlit, with firm drill-down, the method, and CSV downloads.

## 3. Results · owner: Yen-Chu (+ Snehal: chart)
*(starter)*
- FY2025 index **8.6 EW / 10.2 CW**. Cap-weighted is higher because Visa (45) and Mastercard (27) score high and carry weight, while Berkshire (0) and JPMorgan (3) disclose little.
- Highest FY2025 scores: Robinhood 48, Citi 48, Visa 45, FactSet 45, Nasdaq 38.
- **Talk ≠ use:** on the pilot, Dong et al.'s AI word count tracks talk (ρ 0.78) more than use (ρ 0.58).

## 4. Evaluation · owner: Mehul ✅
Full text: [evaluation_section.md](evaluation_section.md) (v0.3; round 3 numbers added after #169). Short version: six checks, each with a bar set in advance; the one that matters most is **overclaims ≤ 5%**. The agent matched people on 81% of unseen passages with **0 overclaims**; scores reproduce exactly from a fresh copy; the guardrail stopped all 18 unsafe trick cases (2 got through without it); people reviewed 195 of the 200 held labels and kept the agent's level on 72%.

## 5. Responsible AI · owner: Mehul ✅ (+ Logan: retention and attribution)
Full text: [responsible_ai.md](responsible_ai.md) (v0.5). Short version: designed against overclaiming named companies; people check the AI at every scale; only public SEC text goes to the model; transcripts stay out; every score traces to a quoted sentence; no investment advice.

## 6. Research foundation · owner: Logan (+ Shu: Dong lines)
*(per Dr. Chung: paper link, abstract, 3–4 talking points.)* Babina, Fedyk, He & Hodson (2024), *Artificial intelligence, firm growth, and product innovation*, JFE 151, 103745, https://doi.org/10.1016/j.jfineco.2023.103745. Talking points: motivation · how their method relates to ours · how we build on it (licensed job-posting data → agentic reading of public filings) · what we add. Related: Dong, Doukas & Zhang (2026); the [Evident AI Index](https://evidentinsights.com/ai-index/). Starter text: [paper_discussion_plan.md](paper_discussion_plan.md).

## 7. What's next · owner: Mehul (starter) → team
*(starter)*
- Settle whether AI in products sold to clients counts as the firm's own use (Visa alone is 7.8% of FY2025 float).
- Add retirement-plan recordkeepers outside the S&P 500 (the client's chapter focus) and FY2026 once complete.
- Add earnings-call transcripts if a licence allows public use.
- Grow the human answer key beyond 80 passages, especially for insurers and exchanges.
- Yearly refresh with the [skill folder](../../skills/ai-adoption-index/SKILL.md) (about an hour, under $1).

## 8. How we worked · owner: Mehul ✅
Full text: [how_we_worked.md](how_we_worked.md). Every task was an issue with one owner and a date on a public board; 127 reviewed pull requests from all five of us; every meeting filed in the repo.

## 9. Handoff · owner: Snehal + Shu
Live dashboard · this repo (and the public final-product repo, #190) · user guide (`docs/user_guide.md`, #142) · skill folder for the yearly refresh (#135).

## 10. References · owner: Logan
*(see #138)*

## Authors · everyone: 2–3 lines + GitHub link
- **Mehul Pardeshi** ([@MehulPardeshi](https://github.com/MehulPardeshi)): project manager and Responsible AI + evaluation lead. Ran the client relationship with Snehal, designed the six evaluation checks and the human-review step, and kept the board, minutes and decisions in the repo.
- **Yen-Chu Chen** ([@teddy0-0y](https://github.com/teddy0-0y)): *(bio)*
- **Logan Mai** ([@MaiJialong](https://github.com/MaiJialong)): *(bio)*
- **Shu Pu** ([@seanpushu](https://github.com/seanpushu)): *(bio)*
- **Snehal Paliwal** ([@snehalpaliwal](https://github.com/snehalpaliwal)): *(bio)*

CMU Heinz College, 95-891 Introduction to AI, Fall 2026 (Team 5). Faculty advisor: Dr. Tingting (Rachel) Chung. Client: Julie Agnew, William & Mary.
