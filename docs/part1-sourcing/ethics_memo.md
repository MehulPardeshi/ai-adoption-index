# Data Sourcing Ethics & Legal Memo: TEMPLATE

> **Graded: 10% of the client rubric.** One page max. Must be **submitted before any scraping or bulk collection begins** (per the brief).
> **Status:** TEMPLATE, not started. Owner and due date: see the shared spreadsheet ([`docs/TASK_TRACKER.md`](../TASK_TRACKER.md)).
> Context: [`memory/00-project-overview.md`](../../memory/00-project-overview.md), brief Part 1.

---

**To:** Julie Agnew (client); Hengkai Zheng (TA)
**From:** Team 5
**Date:** YYYY-MM-DD
**Re:** Legal and ethical sourcing plan for the AI Adoption Index

## 1. Sources we plan to use
<!-- Fill in after the Week-1 source review. Only list sources we will actually use. -->
| Source | Access method (API / bulk / page) | Why this source | Approved? |
|---|---|---|---|
| SEC EDGAR (10-K, 10-Q, 8-K, DEF 14A) | Official APIs / bulk data (**not** HTML scraping) | | |
| Earnings call transcripts | | | |
| Press releases | | | |
| News | Licensed API preferred (e.g., NewsAPI, GDELT) | | |
| _other_ | | | |

## 2. robots.txt and Terms of Service review
<!-- For EACH target site: link to robots.txt, link to ToS, the relevant clause, and our conclusion (allowed / allowed with limits / not allowed → not using). Date checked. -->
| Site | robots.txt | ToS clause | Conclusion | Checked on |
|---|---|---|---|---|
| | | | | |

## 3. Rate limiting and request headers
<!-- e.g., the SEC's published fair-access limits, the User-Agent string format, backoff/retry policy, caching so we never re-download. -->
- 

## 4. Data storage and retention
<!-- Raw text vs. derived metrics: where each lives, who can access it, how long we keep it, when we delete it.
     Must match data/raw/README.md and .gitignore (raw text is NOT committed to GitHub). -->
- **Raw text:**
- **Derived metrics / scores:**
- **Retention and deletion:**

## 5. Attribution and citation
<!-- How the taxonomy doc, dashboard drill-down, and book-chapter data cite sources. Paraphrase vs. short quote rules. -->
- 

## 6. Other risks (optional)
<!-- e.g., paywalls, personal data in documents, LLM API data handling. -->
