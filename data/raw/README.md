# data/raw/

Downloaded source documents (EDGAR filings, transcripts, press releases, news text) land here.

**Everything in this folder except this README and `.gitkeep` is gitignored.** That is deliberate:

- Some sources (transcripts, news) are licensed or ToS-restricted and must not be redistributed via GitHub.
- The retention policy for raw text (how long we keep it, where, and when we delete it) **must match what the team writes in [`docs/part1-sourcing/ethics_memo.md`](../../docs/part1-sourcing/ethics_memo.md)**. If the memo and this folder's handling disagree, the memo wins. Update this README to match once the memo is final.
- To share raw files with teammates, use the location the ethics memo designates (TBD), not git.

Derived, non-verbatim outputs (scores, counts, paraphrased/cited evidence) go in [`../processed/`](../processed/).
