# Julie meeting (Thu Oct 29): "How we check results" (Mehul, 0:33–0:37)

> **v2, Oct 27:** a read-aloud script (about 4 minutes, roughly 500 words) and Q&A prep. v1 was the Oct 19 talking points.
> **Round-1 results filled in Oct 27** (see [`results_round1.md`](labeling_round_1/results_round1.md)). Agent results (check 3) added from Shu's #85.
> **Slide:** one simple slide: the 4 checks as 4 boxes (People check people · People check the AI · Safety tests · Benchmark and rerun).

## Script (read aloud)

**Hand-off in (from Snehal):** *"Thanks, Snehal. Everything you've just seen is only useful if the numbers behind it are trustworthy. So I'll take four minutes on how we check them."*

**1. The risk we're guarding against (about 30 s)**
"The biggest risk in a project like this is confusing *talking* about AI with *using* it. Banks mention AI constantly: in risk sections, in regulatory language, in general statements. In our first test run, only about **one in eight** AI passages described something the company actually does. So our checks focus on one question: are we separating real use from talk correctly?"

**2. People check people (about 1 min)**
"First, we test our own rules. Three teammates, Logan, Yen-Chu and Snehal, each labeled the same **50 passages** on their own, without seeing each other's answers or the AI's. We deliberately included the hardest cases, so this is a strict test. Then we measure how often they agree, using a standard agreement score called kappa. Our bar is **0.6**, which the research literature calls 'substantial' agreement."
- **Results (round 1, Oct 27):** "On the most important question, whether a passage shows real use or not, our raters agreed well: kappa **0.60 to 0.72**, which meets our bar. On the finer five-level scale we're not there yet: two raters reached **0.61**, but across all three it was **0.27**. Most of that gap came from one rule being read two ways. 'Not about AI' was read as 'not about AI *use*'. That's exactly what this test is for: we're clarifying the wording, and we'll run a second round on 30 new passages."
- *(Don't name the rater. If asked: "a wording issue in our rules, not a person issue.")*
"Where people disagree, we don't just average it out. We fix the rule that caused the confusion."

**3. People check the AI (about 1 min)**
"Second, we compare the agent's labels with the human labels on those same 50 passages. The number we watch most closely is the **overclaim rate**: how often the AI says a company *uses* AI when the people say it doesn't. For a public index that names real companies, overclaiming is the worst mistake, so our bar is **5% or less**.
The results are strong. On the 29 passages the agent had never seen while we were building it, it matched the human majority **96%** of the time, and it overclaimed **zero** times. One honest caveat: across repeated runs we see 0 to 2%, so we quote it as a range. And the safety check earned its place: without it, the overclaim rate would have been about **5%**, right at our limit."

**4. Safety checks (about 40 s)**
"Third, guardrails. The agent can only say a company uses AI if it quotes the filing **word for word**, and a separate check confirms the quote really exists. So it can't invent a claim. We've built **20 trick test cases**: made-up quotes, hidden instructions inside a passage, a request to copy a paywalled transcript, and a few genuine cases that must *not* be blocked. We'll run the agent with and without the guardrails and show you the difference side by side."

**5. Benchmark and rerun (about 30 s)**
"Finally, we compare against an existing academic dataset, Dong and colleagues' AI Intensity measure. It mostly counts AI words, and when we compared them, that's exactly what we found: it lines up with how much a bank *talks* about AI, not with how much it *uses* it. That difference is what our index adds. It also scores Wells Fargo zero every year, because its text extraction missed the main report, which is a good example of why checking matters. And a teammate who didn't build the pipeline will rerun it from scratch to confirm they get the same numbers."

**Close + question for Julie (about 20 s)**
"So in short: people check people, people check the AI, we stress-test the guardrails, and we benchmark and rerun. One question for you: right now, a general statement like 'we use AI across the bank' earns **one point**, and a specific, named use earns **three**. For your chapter, would a **strict** version that counts only specific uses be useful alongside it? We tested it already: from filings alone, a strict measure scores all six banks at zero, because filings rarely name specific tools. So the broader measure, plus earnings calls, is what separates them. We can show both."

**Hand-off out:** *"Logan will now walk through the data rules."*

## Q&A prep (short answers)

| If asked… | Say |
|---|---|
| **What is kappa? Why 0.6?** | "It's agreement corrected for luck. Two people would agree sometimes just by chance, and kappa removes that. 0.6 is the usual 'substantial' line (Landis and Koch, 1977)." |
| **Are 50 passages enough?** | "For a first round, yes: it's enough to find unclear rules. We picked the hard cases on purpose. If we miss the bar, we fix the rules and run a second round on 30 new passages." |
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
