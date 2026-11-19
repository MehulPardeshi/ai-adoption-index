# Human review checklist

Use it for (a) every row the guardrail held (`verify_status = needs_review`) and (b) a spot-check of at least 20 scored passages per refresh, more for new kinds of firms (insurers, payment companies).

For each passage, read the full paragraph and its filing section, then answer:

1. **Is this the filing company itself talking?** If it's about competitors, regulators, vendors or the industry in general → **N**.
2. **Is it about AI at all?** If it's a definition, a heading, or AI is mentioned only in passing → **X**.
3. **Does it say the company uses AI now?**
   - It names a tool, a number, a team, a date or a specific process → **D2** (3 points)
   - It says it uses AI, with no detail → **D1** (1 point)
   - It says it plans or expects to use AI → **P** (0.5 points)
   - It's risk talk, rules, or "may use" → **N** (0 points)
4. **Where is it used?** For D2/D1/P pick one or more areas: CX, ADV, CREDIT, RISKM, FRAUD, SURV, CYBER, DEV, PROD, OPS, MKT, or ENT (general). Enablers: GOV, TALENT, INVEST.
5. **Is the quote really in the filing, word for word?** If not, the label can't count.
6. **Unsure between two levels?** Pick the lower one and write one line why.

**Where to record it.** For held rows, fill `review_queue.csv`: `review_evidence`, `review_scenarios` (codes separated by `;`, empty for N/X), `reviewer` = your name, `review_note` = one line why. Then run `python3 -m src.index.apply_review`; it lists any row to fix and writes the reviewed labels and scores. For spot-checks of scored rows, write any disagreement in a note and raise it with the team instead of editing the agent's labels. Add the counts to the [refresh log](refresh_log.md).

**Questions that came up on the sector run (decide as a team, then write the answer here):**
- AI in a product the firm sells to clients (e.g. a broker's AI assistant, a card network's fraud scoring): count as the firm's own use, or not?
- Insurance claims handling and underwriting fit CREDIT/OPS today; note it when the fit is poor.

Full definitions and examples: [labeling cheat sheet](../../../docs/part3-metrics/labeling_round_2/cheat_sheet.md) · [codebook](../../../docs/part2-taxonomy/taxonomy.md).
