# 01 — Team and Role Options

> **Read [`09-decisions-log.md`](09-decisions-log.md) first.** Once someone picks a role and it's logged there, that entry overrides the menu below.

This is a **menu, not an assignment.** The strengths, areas to watch, and stated interests are **self-reported on the signed team contract** (09/20–09/24/2026). The role options are suggestions that fit what each person wrote. Each person picks for themselves, and the team confirms by **majority vote** (per the contract).

Phone numbers live only in the signed contract (kept local, not committed). Use the WhatsApp group for urgent coordination.

---

## Established role (already happening, not an open option)

### Client communication: Snehal Paliwal (de facto lead)
- **In practice, Snehal is already handling client communication with Julie Agnew.** The PM confirmed this; it is not on the contract.
- **Mismatch worth raising:** on the contract, Snehal listed *"Client communication"* as an **area to watch**, not as a preferred role. Snehal may not realize how that reads on paper, or may want the role formally reflected (or may want support or backup on it).
- **Suggested action:** confirm this directly with Snehal before the **Thursday, Oct 1, 2026** meeting. If Snehal agrees, log it in `09-decisions-log.md` as a formal role, and consider naming a backup client contact.

---

## Role menu by person

### Mehul Pardeshi (mppardes@andrew.cmu.edu)
- **Strengths:** strategy, product thinking, client-facing communication, leadership, public speaking, team coordination
- **Areas to watch:** less hands-on with deep coding; may need to lean on teammates or deliberately carve out a technical piece
- **Stated interest:** Project Manager (coordination, timeline, deliverables), open to a defined technical-build task alongside PM duties
- **Proposed (2026-09-28, pending team vote):** **Project Manager + Responsible AI lead.** See [`team/mehul-pardeshi.md`](../team/mehul-pardeshi.md). This covers course requirement #7 (guardrails, with the with-vs-without comparison) and the README's Responsible AI section. It overlaps with Yen-Chu's option 3 below; if both want it, split it (e.g., Yen-Chu: data protection / req #6; Mehul: guardrails / req #7) and settle by vote.
- **Other role options:**
  1. **Project manager:** timeline, spreadsheet tracker, GitHub board hygiene, deliverable QA, TA liaison
  2. **PM + a scoped technical piece:** e.g., the refresh-protocol doc plus the dashboard's filter/drill-down layer, built with AI coding tools
  3. **Final presentation and narrative lead:** owns the "defend our design choices" story (10% of the client rubric) and the poster

### Yen-Chu Chen (yenchuc2@andrew.cmu.edu)
- **Strengths:** information security, AI-related work, some PM experience
- **Areas to watch:** client communication
- **Stated interest:** open ("help with creating dataset, or anything")
- **Role options:**
  1. **Data sourcing and ethics/legal lead:** robots.txt/ToS review, rate limiting, data retention, and the graded ethics memo. This is a natural fit for an infosec background.
  2. **Dataset builder:** EDGAR pulls, backfill of 8–12 quarters, and data-quality checks
  3. **Safety guardrails and data-protection lead:** course technical requirements #6 and #7 (protecting data, guardrails with vs. without comparison)

### Logan Mai (loganmai@andrew.cmu.edu)
- **Strengths:** AI-related work, user/market research
- **Areas to watch (self-reported):** analysis, research, evaluation
- **Stated interest:** business analyst, product management
- **Role options:**
  1. **Firm universe and sector research lead:** build out the retirement recordkeeper list (10+ firms) and verify which firms file with the SEC
  2. **Taxonomy co-coder (business-analyst lens):** read sample documents, propose categories, and write example sentences
  3. **Existing-trackers research:** compare our index against existing AI-adoption trackers and find the required recent research paper (course TP3)
  - *Note:* Logan listed analysis, research, and evaluation as areas to watch. Pairing with a teammate on any evaluation-heavy piece (e.g., the inter-rater check) may help.

### Shu Pu (shup@andrew.cmu.edu)
- **Strengths:** AI agents, LLMs, ML development, backend/API development
- **Areas to watch:** client-facing communication; translating technical detail into concise explanations
- **Stated interest:** AI Engineer responsible for AI solution design
- **Role options:**
  1. **AI engineer / solution architect:** overall pipeline design and the **5+ custom agentic tools** the course requires
  2. **NLP and metrics implementation lead:** once the team finalizes the metrics, implement scoring (mention density, sentiment, framing)
  3. **EDGAR pipeline and backend lead:** API client, storage, and the quarterly refresh job

### Snehal Paliwal (snehalp@andrew.cmu.edu)
- **Strengths:** product management, UI/UX, agentic workflows, communication
- **Areas to watch (self-reported):** client communication, product specs, AI build
- **Stated interest:** Product Management
- **Already doing:** client communication (see above)
- **Additional role options, alongside client comms:**
  1. **Product manager for the dashboard:** requirements from the client, the dashboard spec, UX, and the book-chapter "retirement-only view"
  2. **Dashboard UI/UX designer:** layout, filters, and evidence drill-down design
  3. **Agentic-workflow and skill-folder owner:** the course's `skill.md`/templates requirement

---

## Gaps to watch as a team
- **Inter-rater reliability (Part 3)** needs **at least two independent coders** scoring the same sentences. This cannot be one person's job by design.
- **Everyone must be able to discuss the entire project** at the final presentation (course policy), so rotate knowledge even when owners are set.

---

**How to pick:** create your own profile in [`team/`](../team/) (see [`team/README.md`](../team/README.md)) and open a pull request.

Remaining roles: TBD — to be picked by each person, logged in 09-decisions-log.md once chosen, decided by majority vote per the team contract.
