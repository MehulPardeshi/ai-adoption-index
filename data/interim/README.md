# data/interim/

Text **extracted** from public sources, kept in the repo so teammates can label and review it without re-downloading everything.

| Folder | What's in it | Source and license |
| --- | --- | --- |
| `sec/` | `ai_passages.csv`: every paragraph in our 10-K/10-Q filings that mentions AI, verbatim, with company, quarter and an EDGAR link. Window: periods 2023-12-31 → 2026-06-30 for the six PoC firms (extended Oct 22, #53), 2024-07-01 → 2026-06-30 for Citi | SEC EDGAR filings are public U.S. government records, free to reuse |

Rules:

- **Only public-domain or clearly reusable text goes here.** Earnings-call transcripts, news and anything licensed stay in `data/raw/` (gitignored) unless the [ethics memo](../../docs/part1-sourcing/ethics_memo.md) says otherwise.
- Full filings are **not** committed. `python3 src/edgar/download_sec_filings.py` recreates them in `data/raw/sec/`.
- Labels, scores and other derived results go in [`../processed/`](../processed/).
