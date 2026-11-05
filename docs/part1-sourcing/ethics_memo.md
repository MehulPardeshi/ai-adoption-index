# Data Sourcing Ethics & Legal Memo

**To:** Julie Agnew (Client); Hengkai Zheng (TA)  
**From:** Team 5 — Prepared by Logan Mai  
**Date:** October 18, 2026 · **Updated:** November 4, 2026
**Re:** Legal and ethical sourcing plan for the AI Adoption Index  
**Status:** General policy proposals remain subject to team review. Bloomberg project uses are cleared within the scope confirmed through CMU Libraries (November 4 update below); this is not blanket clearance of other sources.

## 1. Sources we plan to use

| Source | Access method | Research purpose | Proposed disposition |
|---|---|---|---|
| SEC EDGAR 10-K/10-Q filings | Official submissions API and direct EDGAR archive downloads | Traceable corporate AI disclosures | Allow under SEC access and reuse policies |
| Bloomberg earnings-call transcripts | Manual downloads through authorized CMU library terminals | Supplement filings with operational detail | Approved for the described 56-transcript project, including retention, restricted CMU sharing, described analysis and derived-result publication; no public transcript text |
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

Company-hosted transcript decisions are recorded separately in [the source-review table](transcript_source_review.csv) and [Logan's decision summary](transcript_review_decisions_logan.md). Reading approval does not establish storage or full-text sharing permission. Bloomberg clearance does not extend to separately obtained company-website, FactSet or Motley Fool material.

### Bloomberg confirmation — recorded November 4, 2026

CMU librarian Ryan Splenda confirmed with Bloomberg that it has no issues with the team's described project and that the team may proceed. This supersedes the earlier Bloomberg permission holds in the source review. The basis is Ryan's follow-up email excerpt supplied by Logan, together with his earlier detailed reply; November 4 is the date this update was recorded, not an asserted email date. The review record is [PR #62](https://github.com/MehulPardeshi/ai-adoption-index/pull/62#pullrequestreview-5777589775).

| Use | Decision and boundary |
|---|---|
| Access and download | Approved for authorized CMU terminal access and the described 56 manually downloaded transcripts (seven companies, eight quarters). This does not authorize automated terminal collection or unlimited future downloads. |
| Storage and retention | Approved for project copies retained in the manner described to the library. Follow that arrangement; do not infer a new retention period from this approval. |
| Team sharing | Approved in restricted CMU-only storage, including sharing with Prof. Chung and additional CMU students. No public or unrestricted external redistribution. |
| Analysis | Approved for the described local analysis and paid DeepSeek classification of selected passages. External processing is limited to that described workflow; it is not permission for model training/fine-tuning or arbitrary third-party services. |
| Publication | Approved for citations, methodology, derived labels and aggregate scores without transcript text in the public repository, dashboard or other public outputs. |

This is project-specific permission communicated through the library, not a general Bloomberg licence amendment. Preserve attribution and document notices. Permission clearance does not decide whether transcripts should be included in the index or resolve the client's concerns about coverage and automated refresh.

## 3. Rate limiting and request headers

SEC requests must identify the project and contact email through User-Agent and remain below the [SEC ceiling of 10 requests/second per user across machines](https://www.sec.gov/about/developer-resources). The current downloader includes 0.25-second pauses and exponential retry delays for 429/503 responses. Before further bulk runs, implement download caching and coordinate concurrent jobs; stop on access denial rather than bypassing restrictions.

## 4. Data storage and retention

**Raw text:** Keep permitted originals in gitignored `data/raw/` on access-controlled team devices; do not upload full documents to GitHub.  
**Bloomberg copies:** The existing team Drive `earning calls` folder and permitted local copies may be retained within the arrangement described to Ryan. Keep access restricted to CMU users and disable public links. The described external AI processing is the scoped exception to the external-sharing restriction.

**Derived outputs:** Store labels, scores and cited paraphrases in `data/processed/`. Necessary SEC excerpts may remain in `data/interim/`, supported by SEC’s reuse policy and source links; other verbatim material requires separate clearance.  
**Bloomberg public outputs:** Publish only the approved citations, methodology, derived labels and scores; no transcript text. This is separate from the SEC excerpt allowance above.

**Retention:** Proposed rule: delete raw copies within 30 days after final grading unless a documented reproducibility need and applicable permissions justify longer retention. Retain permitted derived outputs and provenance; align the data-folder instructions upon adoption. This proposed schedule does not replace the Bloomberg retention arrangement described to the library or establish a provider-side deletion deadline.

## 5. Attribution and citation

Record company, document type, reporting period, filing/publication date, source URL, passage locator and retrieval date. Preserve notices and distinguish quotations from paraphrases. Educational purpose alone does not establish fair use, and no fixed quotation length guarantees it ([U.S. Copyright Office](https://www.copyright.gov/fair-use/more-info.html)).

## 6. Other risks

Exclude unnecessary personal data; do not bypass logins or paywalls. Upload source text to external AI services only after checking source permissions and provider retention terms. Report disclosure-based evidence, not independently verified deployment or business impact. The SEC pilot predates this memo: review existing extracts against this policy and document remediation. Acknowledge AI assistance; humans remain responsible for source verification and approval.

**DeepSeek retention review — checked October 23, 2026.** The [official Privacy Policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html) (updated February 10, 2026), under “How Long Do We Keep Your Personal Data,” provides no fixed deletion deadline: retention depends on purpose and legal requirements; input personal data may remain while an account exists, with further retention for specified business/legal purposes. Unneeded data are deleted or anonymized. The policy also describes processing/storage in China, model-improvement uses, and applicable deletion/training-opt-out requests via privacy@deepseek.com; it does not promise zero retention. The [Open Platform Terms](https://cdn.deepseek.com/policies/en-US/deepseek-open-platform-terms-of-service.html) (effective April 29, 2026), §§4.1 and 5.5, require input-processing rights and refer to that policy for the developer's personal data, while excluding downstream end-user processing rules. These documents do not establish a fixed API prompt/output retention period; obtain provider clarification before relying on one.

**Current project disposition — updated November 4, 2026:** Hosted DeepSeek inputs may include necessary, permitted public SEC passages and selected Bloomberg passages within the workflow confirmed through CMU Libraries above. Exclude secrets, confidential material, unnecessary personal data and transcripts from uncleared sources. Bloomberg permission resolves the source-use question for the described paid service; payment and that permission do not establish a provider no-training commitment, zero retention or a fixed API deletion deadline. The October 23 provider-policy review above remains the recorded review; no new provider guarantee is asserted by this update. Record the actual service/endpoint and applicable settings used; a different provider or materially expanded workflow requires its own review. Our §4 deletion schedule governs team copies, not provider-held data.

The earlier request to confirm the SEC run's endpoint and payload is addressed by the operator confirmation below. It is an operator report, not an independent payload audit. The team's October 25 acceptance of retention risk was specific to public SEC text and is not rewritten as a new team vote on Bloomberg use.

**Operator confirmation, October 25, 2026 ([PR #66](https://github.com/MehulPardeshi/ai-adoption-index/pull/66#issuecomment-6394497045)).** Shu confirmed:
- the run used the official endpoint `https://api.deepseek.com`, with no override;
- only public SEC 10-K passage text was sent (the 90 FY2025 passages of the six PoC firms plus Citi's 20), with the codebook prompt and made-up examples. No transcripts, personal data, keys or files;
- each passage was sent once per prompt version (about 600 calls in all), at a total cost of about $0.21.

The team accepted the residual retention risk for public SEC text at the October 25 meeting (decision 3).

<!-- AI assistance: OpenAI Codex assisted with research and drafting. Original source checks: October 18, 2026; DeepSeek policy review added October 23, 2026. Bloomberg project clearance recorded November 4, 2026 from correspondence supplied by Logan; general policy proposals remain subject to team review. -->
