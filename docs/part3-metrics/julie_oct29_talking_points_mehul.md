# Julie meeting (Thu Oct 29): "How we check results" (Mehul, 0:33–0:37)

> **v3, Oct 27:** a simple, plain-language read-aloud script (about 3½–4 minutes) and Q&A prep. v1 was the Oct 19 talking points.
> **Round-1 results filled in Oct 27** (see [`results_round1.md`](labeling_round_1/results_round1.md)). Agent results (check 3) added from Shu's #85.
> **Slide:** slide 9 in the team deck, "How we check results" (4 cards). **Final version Oct 27**, after check 4 and the round-2 build.

## Script (read aloud): simple version
*Short sentences, everyday words. About 3½–4 minutes at a calm pace. Bold = say it a little slower.*

**Hand-off in:** "Thanks, Snehal. All of this is only useful if the numbers are right. So in the next four minutes, I'll explain how we check them."

**1. The problem (30 s)**
"Banks talk about AI a lot. But **talking about AI is not the same as using it.** In our first test, only about **one in eight** AI mentions described something the bank actually does. The rest were risks, rules or general talk. So everything we check comes back to one question: can we tell real use apart from talk?"

**2. Do our people agree? (1 min)**
"First, we checked ourselves. Three of us read the same **50 passages**, separately, and labeled each one. Then we measured how often we agreed. We use a standard agreement score, where **0.6 or higher is good.**
On the main question, 'is this real use or not?', we agreed well. We scored **between 0.6 and 0.7**, so we passed.
On the more detailed labels, we didn't pass yet. We scored **0.27.** When we looked into it, we found the reason: **one of our rules could be read two different ways.** So we rewrote it more clearly, added a short practice exercise, and **we're running a second round now.**
That's the point of testing: we find the confusing rule and we fix it."

**3. Does the AI agree with us? (1 min)**
"Second, we compared our AI agent with our human answers. The mistake we care about most is the AI saying a bank **uses AI when it doesn't.** We call that an overclaim. For a public index that names real banks, that's the worst mistake to make.
The results are good. On passages the AI had **never seen before**, it agreed with us **96% of the time**, and it made **no overclaims**. Across repeated runs it's between **0 and 2%**, so we'll report that range to be safe."

**4. Safety checks (40 s)**
"Third, safety. The AI can only say a bank uses AI if it can **quote the exact words** from the bank's report, and we check that the quote is really there. So it can't make things up.
We also built **22 trick tests**, like fake quotes and hidden instructions. Here's why the safety check matters: **without it, the overclaims go up to about 5%.** With it, they're close to zero."

**5. Comparing with others (30 s)**
"Last, we compared our results with an existing research dataset that **counts how often AI words appear** in reports. That dataset tells you **how much a bank talks about AI**, but not **whether it actually uses it.** Ours separates the two, and that's what's new about our index."

**Close + question for Julie (30 s)**
"So, four checks: **people check people, people check the AI, safety tests, and a comparison with outside data.**
One question for you, Julie. Right now, a general line like 'we use AI across the bank' gets **one point**, and a specific example gets **three.** We tried a stricter version that counts **only specific examples**, and from reports alone, **all six banks score zero**, because reports rarely name their AI tools. Would it help your chapter to see both versions side by side?"

**Hand-off out:** "Now Logan will walk us through our data rules."

### If you need the exact numbers (only if asked)
- Agreement on "real use or not": 0.60–0.72 · detailed labels: 0.27 (two raters on their own: 0.61)
- AI vs. people: 29 passages it had never seen, 96% agreement, overclaim 0% (0–2% across runs); about 5% without the safety check
- Comparison: the word-count measure matches our "talk" numbers (0.78), not our "use" numbers (0.14). It scores Wells Fargo 0, because it missed the main part of their report.

## Q&A prep (short answers)

| If asked… | Say |
|---|---|
| **What is kappa? Why 0.6?** | "It's a score for how often people agree, after taking out the times they'd agree just by luck. 0.6 is the standard line for good agreement (it's called kappa)." |
| **Are 50 passages enough?** | "For a first round, yes: it's enough to find unclear rules. We picked the hard cases on purpose. We missed the bar on the fine scale, so we clarified the rules and a second round on 30 new passages is running." |
| **What if the raters disagree a lot?** | "Then the rule is unclear, not the people. We look at the disagreements, rewrite the rule, and re-test. The agreed labels become the reference set for checking the AI." |
| **Why not just trust the AI?** | "It's fast, but it can overclaim or invent things. That's why every claim needs an exact quote, and why we measure it against people." |
| **Why focus on overclaiming, not missed cases?** | "Overclaiming is the costly error: it tells your readers a company does something it doesn't. We still report missed cases, and we also test how much AI text our search misses." |
| **Couldn't the raters be biased?** | "They label separately and don't see the AI's answers. One rater had seen earlier draft labels, so we report each pair's agreement separately and flag it if it looks off." |
| **Did you use AI to label?** | "Not for the human labels. Those are each person's own judgment. AI-drafted labels are only ever on the AI side of the comparison." |
| **How confident are the current numbers?** | "The test-run numbers are early. The human-checked results go into our progress report next week, and the full validation into the final in December." |
| **Can my students rerun this?** | "Yes. That's the point of the rerun check. The code and instructions are in the repo, and we'll hand over the agent setup with a cost estimate, without our API key." |
| **How much does the AI cost?** | "Very little. All our runs so far cost about 21 cents in total, and we only send public SEC text." (Shu can give details.) |
| **Does the score depend on your weights?** | "We tested that. Changing the weights doesn't change the ranking at all. Giving general statements zero points moves two banks slightly. A strict measure (specific uses only) puts all six banks at zero from filings, which is why we want earnings calls." |
| **How do you compare to other AI rankings?** | "Most trackers count announcements or enterprise surveys. Ours is built from what companies disclose in their filings, and it separates use from talk." (Logan did the comparison.) |
| **Anything about data or licensing** | "Logan covers that next, under data rules." |
| Something you don't know | "Good question. I'll check with the team and follow up in writing after the meeting." |

## Questions for Julie (team list from Oct 25, if time allows)
1. Are these 6 companies (+ Citi as a benchmark) and 2024–2026 right for your chapter?
2. Strict measure (specific uses only) or broader (including general statements)? *(asked in the script)*
3. What should we add next: more companies, earnings calls, or job postings?
4. What do you need from us for the book: charts, a table, the dataset, or a written summary?
