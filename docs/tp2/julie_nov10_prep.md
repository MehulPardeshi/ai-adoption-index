# Julie follow-up, Tue Nov 10: prep (agreed at the Sun Nov 8 team call)

> **When:** Tue Nov 10, 7:00–8:00 pm ET, Zoom (Snehal hosts; link in the calendar invite, not here).
> **Who has accepted (calendar, checked Sun Nov 8):** Julie, Dr. Chung, Snehal, Logan, Shu, Yen-Chu, Mehul. Hengkai hasn't replied.
> **Why it matters:** this is the TP2 client meeting. The rubric gives **10 points** for "client meeting held; team came away with clear, confirmed direction." Section 6 of the TP2 report is written from it (Snehal, Wed Nov 11).
> **Status:** agenda and questions accepted at the Nov 8 call ([minutes](../../meetings/2026-11-08-internal.md)). Everyone checks the order of their slides; we record the meeting; no practice run.

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
| 4 | Transcripts: CMU Libraries cleared Bloomberg for the project (Nov 4). **Team decision (Nov 8): leave transcripts out of the index; future work.** Matches her Oct 29 guidance: manual pulls don't fit an automated index; no extra points just for having transcripts | Logan | 5 |
| 5 | How reliable the labels are: the team adjudicated the disagreements (Nov 7) into a consensus set; agent vs. agreed labels 81% on 48 passages it hadn't seen, 0 overclaims; guardrail test 0/18 unsafe | Mehul | 8 |
| 6 | Questions for Julie (below) | All | 10 |
| 7 | Next steps and dates to Dec 3 | Snehal | 2 |

## Questions for Julie (pick on Sunday)
- 10-K + 10-Q or 10-K only on the dashboard? (from the Nov 2 email)
- Use cases next to each firm's score? (from the Nov 2 email)
- Headline index: **market-cap-weighted or equal-weighted**? We'd show both if she wants; public float is below full market cap.
- Transcripts: we're leaving them out (future work). Does she agree?
- Handover, "definition of done": what does she want to receive (code, data, a how-to-update guide), and does it need to refresh itself? (Our main open question.)
- What she'd like to receive at handover (the code, the run cost per year, the method write-up).
- Research paper: she offered candidates (TP3 needs one high-quality paper from the last 3 years). Any she'd recommend?
- Will she join the final presentation on Thu Dec 3?

## Before Tuesday
| What | Who | When |
|---|---|---|
| ✅ Transcripts out; index shows both weightings | Team | Sun Nov 8 call |
| ✅ Agenda and questions agreed | Team | Sun Nov 8 call |
| Slides in the deck; anticipate Julie's questions | All | Mon Nov 9 night |
| 1–2 slides on the high-level pipeline and how the index will be shown | Shu | Before Tue |
| Send the agenda to Julie (as on Oct 27) | Snehal | Mon Nov 9 |
| ✅ Agreed labels committed and check 4 rerun (#124, #125, #128, #129) | Raters → Mehul | Done Nov 8–9 |
| Dashboard changes (#96) | Snehal | Mon Nov 9 |
| ~~Practice run~~ | Team | Not doing it (midterms; decided Nov 8) |

## Mehul's part (item 5, ~5 min): how reliable the labels are
Plain-language points, from the repo results (check 4 rerun on the agreed labels: Nov 8, updated Nov 9). Slides 18–19 in the team deck (reordered Nov 10 to follow the agenda: index → dashboard → data sources → reliability → next steps).
- **People first.** Three of us labeled the same passages on our own. On the main question, "does this passage describe real AI use?", we agreed well in round 1 (κ 0.60–0.72). On the five detailed levels we didn't (κ 0.27, then 0.32 on a harder sample). So the team went through all 58 disagreements together on Nov 7 and agreed one label for each. That agreed set is now the answer key.
- **The AI against people.** On 48 passages it never saw during tuning, the agent matched the team's agreed labels 81% of the time (κ 0.73; 85% on use vs. no use). It never claimed use that people didn't agree on (0 of 48). All 7 misses were cautious, and 3 of them had already been sent to a person by the guardrail (90% after that review). Round 2, the hard set: 74%. ([check 3](../part3-metrics/check3_results.md))
- **Safety checks.** We tried to trick it 18 ways (fake quotes, a changed number, hidden instructions, paywalled sources, "should I buy this stock?"). With our checks on, nothing unsafe got through and no correct answer was blocked. Without them, 2 of the 18 got through.
- **The scores hold up, and the human labels raise them.** Changing how much "deployed" use is worth, or dropping general use, barely changes the ranking (ρ 0.95–1.00). Swapping in our 80 human-agreed labels raises Capital One from 3 to 20, Principal from 0 to 18, Wells Fargo from 9 to 11, JPMorgan and Schwab to 6; Bank of America stays 6 and Citi goes 48 → 53 (final, all scenarios in, #145): the AI draft labels were cautious (people saw use or plans the draft missed in 18 of 80 hard passages, the reverse once). Talk volume still tracks the Dong et al. word count most closely (0.78 vs. 0.58 for our use score; six firms, so a direction only) ([check 4 rerun](../part3-metrics/check4_results.md)).
- **One thing to ask her:** counting only specific uses, five of the six PoC firms score 0 from filings alone (Principal is the exception; Citi names deployed tools). Earnings calls are where executives name tools, so this ties to the transcripts decision. Our suggestion: keep the broader measure as the headline and show the strict one beside it. Does she agree?

Links: [round 2](../part3-metrics/labeling_round_2/results_round2.md) · [check 4](../part3-metrics/check4_results.md) · [check 6](../part3-metrics/check6_results.md) · [evaluation plan](../part3-metrics/evaluation_plan.md)
