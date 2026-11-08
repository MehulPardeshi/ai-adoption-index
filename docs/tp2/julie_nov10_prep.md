# Julie follow-up, Tue Nov 10: prep (DRAFT for the Sun Nov 8 team call)

> **When:** Tue Nov 10, 7:00–8:00 pm ET, Zoom (Snehal hosts; link in the calendar invite, not here).
> **Who has accepted (calendar, checked Sun Nov 8):** Julie, Dr. Chung, Snehal, Logan, Shu, Yen-Chu, Mehul. Hengkai hasn't replied.
> **Why it matters:** this is the TP2 client meeting. The rubric gives **10 points** for "client meeting held; team came away with clear, confirmed direction." Section 6 of the TP2 report is written from it (Snehal, Wed Nov 11).
> **Status:** a draft for the team to change on Sunday night. Presenters and the final agenda are the team's call.

## Still open from the email thread
On Nov 2 Snehal emailed Julie a follow-up from the Oct 29 meeting with three questions. Julie hasn't answered them by email; she accepted the calendar invite instead. Ask them on Tuesday:
1. The dashboard mock showed annual reports only, but the scores combine **10-Ks and 10-Qs**. Which does she want displayed?
2. Should **specific use cases** sit next to each firm's score?
3. (Answered by us.) Fiscal years: all 7 firms' 10-Ks end Dec 31.

## Proposed agenda (~40 min, then questions)
| # | Item | Who (proposed, mirrors Oct 29) | Min |
|---|---|---|---|
| 1 | What changed since Oct 29 | Snehal | 2 |
| 2 | **Sector index: feasible** (#97). S&P 500 Financials, ~75 firms; size from public float (SEC's free API); about an hour of model time and under $1 per year of filings. Prompts were tuned on banks, so insurers and payment firms get spot-checked first | Yen-Chu, Shu | 8 |
| 3 | Dashboard changes she asked for: hover definitions, FY2026 hidden (#96) | Snehal | 5 |
| 4 | Transcripts: CMU Libraries cleared Bloomberg for the project (Nov 4). The team's recommendation (decide Sunday), with her Oct 29 guidance: manual pulls don't fit an automated index; no extra points just for having transcripts | Logan | 5 |
| 5 | How reliable the labels are: the team adjudicated the disagreements (Nov 7) into a consensus set; agent vs. people 96% on passages it hadn't seen; guardrail test 0/18 unsafe | Mehul | 8 |
| 6 | Questions for Julie (below) | All | 10 |
| 7 | Next steps and dates to Dec 3 | Snehal | 2 |

## Questions for Julie (pick on Sunday)
- 10-K + 10-Q or 10-K only on the dashboard? (from the Nov 2 email)
- Use cases next to each firm's score? (from the Nov 2 email)
- Headline index: **market-cap-weighted or equal-weighted**? We'd show both if she wants; public float is below full market cap.
- Transcripts: leave them out, or a base score plus a separate "with transcripts" view?
- What she'd like to receive at handover (the code, the run cost per year, the method write-up).
- Research paper: she offered candidates (TP3 needs one high-quality paper from the last 3 years). Any she'd recommend?
- Will she join the final presentation on Thu Dec 3?

## Before Tuesday
| What | Who | When |
|---|---|---|
| Decide on transcripts and the headline weighting (items 4 and 6) | Team | Sun Nov 8 call |
| Agree on the agenda and presenters | Team | Sun Nov 8 call |
| Send the agenda to Julie (as on Oct 27) | Snehal | Mon Nov 9 |
| Share the agreed-label sheet; Mehul commits it and reruns check 4 (#101) | Raters → Mehul | Mon Nov 9 |
| Dashboard changes (#96) | Snehal | Mon Nov 9 |
| Short practice run (optional; Oct 28 ran ~27 min) | Team | `UNCLEAR:` Mon or Tue |

## Mehul's part (item 5, ~5 min): how reliable the labels are
Plain-language points, from the repo results (check 4 rerun on the agreed labels: Nov 8).
- **People first.** Three of us labeled the same passages on our own. On the main question, "does this passage describe real AI use?", we agreed well in round 1 (κ 0.60–0.72). On the five detailed levels we didn't (κ 0.27, then 0.32 on a harder sample). So the team went through all 58 disagreements together on Nov 7 and agreed one label for each. That agreed set is now the answer key.
- **The AI against people.** On 29 passages it never saw during tuning, the agent matched the people's majority 96% of the time (24 of 25). It almost never claims use that people didn't see (0–2%, about 5% without our checks).
- **Safety checks.** We tried to trick it 18 ways (fake quotes, a changed number, hidden instructions, paywalled sources, "should I buy this stock?"). With our checks on, nothing unsafe got through and no correct answer was blocked. Without them, 2 of the 18 got through.
- **The scores hold up, and the human labels raise them.** Changing how much "deployed" use is worth barely changes the ranking (ρ 0.99). Swapping in our 80 human-agreed labels raises Capital One and Principal from near 0 to 18 and Schwab to 6: the AI draft labels were cautious (people saw use or plans the draft missed in 18 of 80 hard passages, the reverse once). Talk volume still tracks the Dong et al. word count most closely (0.78 vs. 0.58 for our use score; six firms, so a direction only) ([check 4 rerun](../part3-metrics/check4_results.md)).
- **One thing to ask her:** counting only specific uses, five of the six PoC firms score 0 from filings alone (Principal is the exception; Citi names deployed tools). Earnings calls are where executives name tools, so this ties to the transcripts decision. Our suggestion: keep the broader measure as the headline and show the strict one beside it. Does she agree?

Links: [round 2](../part3-metrics/labeling_round_2/results_round2.md) · [check 4](../part3-metrics/check4_results.md) · [check 6](../part3-metrics/check6_results.md) · [evaluation plan](../part3-metrics/evaluation_plan.md)
