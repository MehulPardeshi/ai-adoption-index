# Firm Universe by Sector (Part 1.5): WORKING DOC

> **Status:** reference tables pre-filled from the brief. **The firm list itself is not decided.** Finalize by majority vote and log it in [`memory/09-decisions-log.md`](../../memory/09-decisions-log.md).
> Background and rationale: [`memory/03-sectors-and-firms.md`](../../memory/03-sectors-and-firms.md)

## Targets
- **Retirement Plan Providers / Recordkeepers: PRIMARY FOCUS, 10+ firms** (feeds the client's book chapter)
- Other sectors: **5–8 firms each**
- Pension Funds: optional
- **Multi-sector tagging:** a firm gets **every** sector tag that applies. Don't force a single category.

## Reference: sector → industry codes (from the brief)

| Sector (functional) | SIC Code(s) | NAICS Code(s) | GICS Sub-Industry (approx.) |
|---|---|---|---|
| Investment/Asset Management | 6282 (Investment Advice), 6726 (Investment Offices) | 523900 / 523930 | Asset Management & Custody Banks |
| Retirement Plan Providers/Recordkeepers | No dedicated code; filers typically appear under 6282, 6311, or 6020/6022 depending on charter. 6371 (Pension/Retirement Funds) exists but is sparsely used by EDGAR filers | 525110 (Pension Funds); some recordkeeping arms under 523900 | No dedicated sub-industry; split across Asset Management & Custody Banks and Life & Health Insurance |
| Banks (Universal/Commercial) | 6020, 6021, 6022, 6712 (Bank Holding Companies) | 522110 | Diversified Banks, Regional Banks |
| Insurance Companies | 6311 (Life), 6321 (Accident & Health), 6411 (Agents/Brokers) | 524113, 524114 | Life & Health Insurance, Multi-line Insurance |
| Broker-Dealers/Wealth Management | 6211 (Security Brokers, Dealers) | 523110 | Investment Banking & Brokerage |
| Fintech/AI-Native | Varies; often 6199 (Finance Services) or 7372 (Prepackaged Software) | 522320, 511210 | Financial Exchanges & Data, Application Software |
| Pension Funds/Sovereign & Public Plans (optional) | 6371 | 525110 | Not typically covered by GICS |

**SIC is the practical filter** for EDGAR queries. Remember the **functional vs. legal classification mismatch** paragraph for the methodology.

## Reference: brief's example firms (starting point only)

| Sector | Example firms (brief) |
|---|---|
| Investment/Asset Mgmt | T. Rowe Price, BlackRock, Vanguard, Fidelity, State Street, Invesco |
| Retirement Recordkeepers | Fidelity, Empower, Voya, Principal, Vanguard, T. Rowe Price, TIAA, Alight |
| Banks | JPMorgan Chase, Bank of America, Wells Fargo, Citigroup, U.S. Bank |
| Insurance | MetLife, Prudential, Nationwide, Lincoln Financial |
| Broker-Dealers/Wealth | Charles Schwab, Morgan Stanley, Merrill Lynch, Edward Jones |
| Fintech/AI-Native | Betterment, Wealthfront, Personal Capital/Empower Personal Wealth |
| Pension Funds (optional) | CalPERS, state teacher retirement systems |

⚠️ Some examples are private, mutually owned, or subsidiaries and may have **no EDGAR filings**. Verify each one.

## Working firm list (TO FILL IN)

<!-- One row per firm. Sector tags = semicolon-separated. "EDGAR coverage" = which forms exist, over which quarters. -->
| Firm | CIK | SIC (from EDGAR header) | Sector tag(s) | Retirement? (Y/N) | EDGAR coverage (forms, quarters) | Non-EDGAR sources | Include? | Notes |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## Open questions
- Which recordkeepers beyond the brief's list get us to 10+?
- For private firms with no filings, is IR/press-release-only coverage enough to include them?
- Do we include the optional pension-fund sector? (Ask the client.)
