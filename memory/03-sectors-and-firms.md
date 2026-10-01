# 03 — Sectors and Firm Universe (Part 1.5)

> **2026-10-01 kickoff clarification:** See [minutes](../meetings/2026-10-01-client.md) and the latest decisions log. Julie recommended a 4–5-bank pilot and permits a simpler team-designed measure. Final coverage, taxonomy, and metrics remain open; quarterly automation is desired only if feasible. Earlier targets below remain brief material, not confirmed client commitments. Course/rubric obligations must be checked with the instructor before reducing graded requirements.


> **Read [`09-decisions-log.md`](09-decisions-log.md) first.** The firm lists below are the **brief's suggested starting examples**, not a final universe. The working file is [`docs/part1.5-firm-universe/firm_universe.md`](../docs/part1.5-firm-universe/firm_universe.md).

## Why segment by sector first
- It allows apples-to-apples comparison within a sector (a bank and a recordkeeper talk about AI very differently).
- It guarantees the **retirement slice** (the client's book chapter) is deliberately built out, not an afterthought.

## Sectors
| Sector | Status | Target firm count |
|---|---|---|
| **Retirement Plan Providers / Recordkeepers** | **PRIMARY FOCUS** (feeds the book chapter) | **10+** (brief says "consider requiring"; treat as our target) |
| Investment / Asset Management | Core | 5–8 |
| Banks (Universal / Commercial) | Core | 5–8 |
| Insurance | Core | 5–8 |
| Broker-Dealers / Wealth Management | Core | 5–8 |
| Fintech / AI-Native | **Benchmark group** ("high AI-intensity" contrast) | 5–8 |
| Pension Funds / Sovereign & Public Plans | **Optional** | — |

## Multi-sector tagging rule
Firms can belong to **multiple sectors** (e.g., Fidelity and T. Rowe Price are both asset managers and recordkeepers). **Tag, don't force a single category.** Sector becomes a filterable dashboard field, not a data-cleaning problem.

## Retirement sub-taxonomy (layered on the general taxonomy)
These are sub-tags, mostly under "client-facing advice" and "portfolio construction." They are not new top-level categories.
- Participant advice / robo-guidance
- Retirement income / decumulation modeling
- Plan design & auto-features optimization (auto-enroll, auto-escalate)
- Plan sponsor analytics
- Participant engagement / chatbots

## Brief's example firms (starting point, to refine and expand)
| Sector | Example firms from the brief |
|---|---|
| Investment/Asset Mgmt | T. Rowe Price, BlackRock, Vanguard, Fidelity, State Street, Invesco |
| Retirement Recordkeepers | Fidelity, Empower, Voya, Principal, Vanguard, T. Rowe Price, TIAA, Alight |
| Banks | JPMorgan Chase, Bank of America, Wells Fargo, Citigroup, U.S. Bank |
| Insurance | MetLife, Prudential, Nationwide, Lincoln Financial |
| Broker-Dealers/Wealth | Charles Schwab, Morgan Stanley, Merrill Lynch, Edward Jones |
| Fintech/AI-Native | Betterment, Wealthfront, Personal Capital/Empower Personal Wealth |
| Pension Funds (optional) | CalPERS, state teacher retirement systems |

**Check before committing to a firm:** several of these are **privately held, mutually owned, or subsidiaries** (e.g., Vanguard and Fidelity are not publicly traded). Such firms may have **no 10-K/10-Q on EDGAR**. For each firm, confirm there is an EDGAR CIK with usable filings, or plan non-EDGAR sources (IR pages, press releases). Record the outcome in the firm-universe doc.

## Mapping sectors to industry codes
There is **no clean "retirement plan provider" code**. Recordkeeping is a business line, not a legal entity type. We are layering a **functional taxonomy** (what the firm does) on top of a **legal/regulatory one** (how it's classified). The brief says to **write a paragraph about this mismatch** in the methodology; it's also useful for the book chapter.

| Sector (functional) | SIC | NAICS | GICS sub-industry (approx.) |
|---|---|---|---|
| Investment/Asset Mgmt | 6282 (Investment Advice), 6726 (Investment Offices) | 523900 / 523930 | Asset Management & Custody Banks |
| Retirement Recordkeepers | No dedicated code; filers appear under 6282, 6311, or 6020/6022 by charter. 6371 exists but is sparsely used | 525110; some under 523900 | None; split across Asset Mgmt & Custody Banks and Life & Health Insurance |
| Banks | 6020, 6021, 6022, 6712 (Bank Holding Cos.) | 522110 | Diversified Banks, Regional Banks |
| Insurance | 6311 (Life), 6321 (Accident & Health), 6411 (Agents/Brokers) | 524113, 524114 | Life & Health Insurance, Multi-line Insurance |
| Broker-Dealers/Wealth | 6211 (Security Brokers, Dealers) | 523110 | Investment Banking & Brokerage |
| Fintech/AI-Native | Varies; often 6199 or 7372 | 522320, 511210 | Financial Exchanges & Data, Application Software |
| Pension Funds (optional) | 6371 | 525110 | Not typically covered |

**Practical use:** **SIC is the actionable filter**. It's in every EDGAR filer header, so it can filter full-text search and bulk downloads by sector. GICS is more useful later, for framing peer groups the way equity research does.
