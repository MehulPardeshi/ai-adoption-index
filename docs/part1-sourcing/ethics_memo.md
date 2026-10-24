# Data Sourcing Ethics & Legal Memo

**To:** Julie Agnew (Client); Hengkai Zheng (TA)  
**From:** Team 5 — Prepared by Logan Mai  
**Date:** October 18, 2026  
**Re:** Legal and ethical sourcing plan for the AI Adoption Index  
**Status:** Proposed policy for team review; not retrospective approval of prior collection.

## 1. Sources we plan to use

| Source | Access method | Research purpose | Proposed disposition |
|---|---|---|---|
| SEC EDGAR 10-K/10-Q filings | Official submissions API and direct EDGAR archive downloads | Traceable corporate AI disclosures | Allow under SEC access and reuse policies |
| Company-hosted earnings-call transcripts | Direct downloads after source-specific review | Supplement filings with operational detail | Hold collection until applicable terms and document rights are verified |
| AI Intensity Dataset | Author-provided GitHub download | Academic comparison and benchmarking | Academic analysis with required citation; confirm redistribution rights before republishing |

The [dataset README](https://github.com/FengDong-Elon/ai-intensity-dataset) expressly identifies academic research and requires citation of Dong, Doukas and Zhang. It does not establish unrestricted redistribution rights. LinkedIn, restricted career-site data, news and standalone press releases are excluded from this collection phase.

## 2. robots.txt and Terms of Service review

**Checked October 18, 2026.** Access permission and redistribution permission are assessed separately; robots.txt is not a content licence.

| Site | Evidence reviewed | Conclusion |
|---|---|---|
| SEC | [robots.txt](https://www.sec.gov/robots.txt) allows the EDGAR data archive path; [SEC FAQ](https://www.sec.gov/files/about/webmaster-faq.htm) permits access and reuse of public filing content | Allow cited filing text, subject to fair-access controls. The API host’s robots.txt could not be retrieved; API access is documented in SEC developer guidance |
| LinkedIn | [robots.txt](https://www.linkedin.com/robots.txt) disallows general crawlers; [User Agreement §8.2](https://www.linkedin.com/legal/user-agreement) restricts scraping and unauthorized copying/use | Exclude absent applicable authorization |
| JPMorganChase | [robots.txt](https://www.jpmorganchase.com/robots.txt); [Copyright Notices](https://www.jpmorganchase.com/legal/terms-and-conditions) restrict copying, storage and distribution, subject to statutory exceptions | No blanket transcript clearance; require documented permission or a specific fair-use assessment |
| Bank of America IR | [Terms of Use](https://investor.bankofamerica.com/terms-of-use) do not establish a general reuse licence; [robots.txt](https://investor.bankofamerica.com/robots.txt) could not be retrieved | Pending document-level and access review |

Other company transcript sources remain unreviewed and uncleared.

## 3. Rate limiting and request headers

SEC requests must identify the project and contact email through User-Agent and remain below the [SEC ceiling of 10 requests/second per user across machines](https://www.sec.gov/about/developer-resources). The current downloader includes 0.25-second pauses and exponential retry delays for 429/503 responses. Before further bulk runs, implement download caching and coordinate concurrent jobs; stop on access denial rather than bypassing restrictions.

## 4. Data storage and retention

**Raw text:** Keep permitted originals in gitignored `data/raw/` on access-controlled team devices; do not upload full documents to GitHub.  
**Derived outputs:** Store labels, scores and cited paraphrases in `data/processed/`. Necessary SEC excerpts may remain in `data/interim/`, supported by SEC’s reuse policy and source links; other verbatim material requires separate clearance.  
**Retention:** Proposed rule: delete raw copies within 30 days after final grading unless a documented reproducibility need and applicable permissions justify longer retention. Retain permitted derived outputs and provenance; align the data-folder instructions upon adoption.

## 5. Attribution and citation

Record company, document type, reporting period, filing/publication date, source URL, passage locator and retrieval date. Preserve notices and distinguish quotations from paraphrases. Educational purpose alone does not establish fair use, and no fixed quotation length guarantees it ([U.S. Copyright Office](https://www.copyright.gov/fair-use/more-info.html)).

## 6. Other risks

Exclude unnecessary personal data; do not bypass logins or paywalls. Upload source text to external AI services only after checking source permissions and provider retention terms. Report disclosure-based evidence, not independently verified deployment or business impact. The SEC pilot predates this memo: review existing extracts against this policy and document remediation. Acknowledge AI assistance; humans remain responsible for source verification and approval.

**DeepSeek retention review — checked October 23, 2026.** The [official Privacy Policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html) (updated February 10, 2026), under “How Long Do We Keep Your Personal Data,” provides no fixed deletion deadline: retention depends on purpose and legal requirements; input personal data may remain while an account exists, with further retention for specified business/legal purposes. Unneeded data are deleted or anonymized. The policy also describes processing/storage in China, model-improvement uses, and applicable deletion/training-opt-out requests via privacy@deepseek.com; it does not promise zero retention. The [Open Platform Terms](https://cdn.deepseek.com/policies/en-US/deepseek-open-platform-terms-of-service.html) (effective April 29, 2026), §§4.1 and 5.5, require input-processing rights and refer to that policy for the developer's personal data, while excluding downstream end-user processing rules. These documents do not establish a fixed API prompt/output retention period; obtain provider clarification before relying on one.

**Proposed project disposition:** Limit hosted DeepSeek inputs to necessary, permitted public SEC passages, excluding secrets, confidential material, unnecessary personal data and uncleared transcripts. Our §4 deletion schedule governs team copies, not provider-held data. The prior run reported in [PR #66](https://github.com/MehulPardeshi/ai-adoption-index/pull/66) preceded this review: its operator should confirm the endpoint and submitted material, record any remediation, and obtain team acceptance of residual retention risk. This is conditional support for the public-SEC use case, not retrospective approval or evidence that the actual payload has been audited. Third-party hosting requires its own policy review.

<!-- AI assistance: OpenAI Codex assisted with research and drafting. Original source checks: October 18, 2026; DeepSeek policy review added October 23, 2026. Team review and approval remain pending. -->
