# Earnings-call transcript sources (for Logan's review)

**By:** Yen-Chu Chen · **Date:** Oct 20, 2026 · **Issue:** #34 · **Status:** PROPOSAL. Nothing is collected from a source until Logan clears it in the [ethics memo](ethics_memo.md).

**Ask for Logan:** please approve or reject each source below. Company websites are low-risk. **Motley Fool is the one that really needs a decision**, because 3 of the 7 companies depend on it.

**Period:** calls for the quarters Q3 2024 to Q2 2026 (8 calls per company), the same window as the SEC test run, so the two can be compared.

## 1. Proposed sources per company

| Company | Source | Format | Checked |
|---|---|---|---|
| JPMorgan Chase | Company IR: [jpmorganchase.com/ir/quarterly-earnings](https://www.jpmorganchase.com/ir/quarterly-earnings), "Earnings Transcript" per quarter | PDF | Oct 20 (Yen-Chu, in browser) |
| Citigroup | Company IR: [citigroup.com/global/investors/quarterly-earnings](https://www.citigroup.com/global/investors/quarterly-earnings), "Transcript" per quarter | PDF | Oct 20 |
| Principal Financial | Company IR: [investors.principal.com/financials/quarterly-results](https://investors.principal.com/financials/quarterly-results), transcripts for 2023–2026 | PDF | Oct 20 |
| Bank of America | Company IR: [investor.bankofamerica.com/quarterly-earnings](https://investor.bankofamerica.com/quarterly-earnings), historical transcripts available | PDF | Oct 20 (Yen-Chu, in browser) |
| Wells Fargo | **Motley Fool** (company IR has release, presentation, supplement and webcast, but no transcript) | Web page | Oct 20 |
| Charles Schwab | **Motley Fool** (company IR has presentations and webcasts; the last transcript posted is from 2019) | Web page | Oct 20 |
| Capital One | **Motley Fool** (company IR not yet checked for transcripts; switch to IR if it has them) | Web page | Oct 20 |

**Not used:** Yahoo Finance (transcripts need a Silver/Gold subscription) and Seeking Alpha (paywalled). The team rule is no paywalled sources.

## 2. Terms of use: what we found

| Site | Terms | What it means for us |
|---|---|---|
| Company IR sites (JPM, Citi, PFG, BAC) | Not reviewed clause by clause yet | Published by the companies for investors. Low risk for reading and analysis; **Logan to confirm**. |
| Motley Fool (fool.com) | Couldn't open the US terms or robots.txt from our tools. The Canadian site's [Terms of Service](https://www.fool.ca/terms-of-service/) say: no "automated means, including without limitation, agents, robots, scripts, or spiders"; content is for "individual, non-commercial use only"; no reproducing or republishing. US terms are probably similar; **Logan to check the US version**. | **No scraping.** At most, read pages one at a time by hand. Transcripts are free to read and include past quarters; they're produced by "Motley Fool Transcribing" and may contain errors. |
| Backup: company webcasts (WFC, SCHW) | Not reviewed | If Motley Fool is rejected: transcribe the companies' own webcast recordings ourselves (e.g., with Whisper). Official source, but more work. **Logan to confirm** this is allowed. |

## 3. How we'd handle the text (proposed)

- **Collection:** download company PDFs by hand or one at a time, nothing at high volume. **No automated access to Motley Fool.**
- **Storage (proposed, Logan to confirm in the memo):**
  - **Each person's computer:** `data/raw/transcripts/<TICKER>/<TICKER>_<YYYY>Q<n>.pdf`. `data/raw/` is gitignored, so the files never get pushed.
  - **Sharing with teammates:** a `transcripts` folder in the team's private Drive, shared with the 5 team members only (no public link). [`data/raw/README.md`](../../data/raw/README.md) already says raw files are shared through the location the ethics memo names, not through git.
  - **No transcript text goes into GitHub** without a documented basis for redistribution.
- **In the repo:** only derived results: AI-related short quotes with a source link and speaker role, labels and scores.
- **Evidence rule:** only statements by company management count as evidence; analyst questions are context (see Taxonomy v0).

## 4. Decisions needed

- [ ] Company IR transcripts (JPM, Citi, PFG, BAC): approve?
- [ ] Motley Fool, manual reading only, for WFC, SCHW, COF: approve?
- [ ] If Motley Fool is rejected: approve self-transcribing the company webcasts, or skip transcripts for those 3 companies?
- [ ] Short quotes (one or two sentences) from transcripts in the repo and on the dashboard: OK?
- [ ] Storage: local `data/raw/transcripts/` plus a private team Drive folder: OK? (Google Drive or CMU OneDrive, whichever you name in the memo)
