# Julie meeting (Oct 29): "How we check our results" (Mehul, ~3 minutes)

**One-line message:** *Our numbers are only useful if they're trustworthy, so we test every step, from finding AI text to the final score.*

1. **The problem we're guarding against (30 s).** A company that *mentions* AI a lot isn't necessarily *using* it. In our test run, only about 1 in 8 AI passages showed real use. So the most important thing to check is whether we're separating use from talk correctly.
2. **People check people (45 s).** Three of us label the same 50 passages separately, then we measure how often we agree (target: an agreement score of at least 0.6, "substantial"). Where we disagree, we fix the rule that caused it. *[Insert round-1 result: e.g., "We agreed on X of 50; the main confusion was …"]*
3. **People check the AI (45 s).** We compare the AI's labels with our human labels. The number we watch most is the **overclaim rate**: how often the AI says "this company uses AI" when people say it doesn't. Target: 5% or less. *[Insert result if ready.]*
4. **Safety checks (30 s).** The agent can only claim a company uses AI if it quotes the filing word for word, so it can't invent claims. We test this with 20 tricky cases (fake quotes, hidden instructions, paywalled sources), with and without the safety checks.
5. **Benchmark and reproducibility (30 s).** We compare with the Dong et al. AI Intensity data. It mostly counts AI words, and it scores Wells Fargo 0 because it missed the main report, which shows why checking matters. A teammate who didn't build the pipeline will rerun it to confirm the same numbers.

**Question for Julie:** *For your chapter, would you rather see a strict measure (only clearly stated uses) or a broader one (including general statements)? We can show both.*
