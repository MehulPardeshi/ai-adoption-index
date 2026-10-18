# Review of Julie's materials (#25)

**By:** Mehul Pardeshi · **Date:** Oct 18, 2026 · Sources are listed in [`docs/references.md`](../references.md)

## 1. Vanguard, *AI, demographics, and the U.S. economy: Quantifying the coming tug-of-war* (Megatrends series, June 2024, 33 pp.)
Authors: Joseph Davis (Global Chief Economist), Kevin Khang, Lukas Brandl-Cheng and colleagues, Vanguard research.

**Main argument.** The coming decade is a tug-of-war between **AI-driven productivity** and **demographics-driven deficits** from an aging population. Vanguard's Megatrends Model covers 130 years of data and finds these slow-moving forces drove about 60% of the change in per-capita GDP growth and stock valuations.

**Scenarios to 2040** (average real U.S. GDP growth, 2028–2040):

| Scenario | Growth | Vanguard's probability |
|---|---|---|
| AI is transformational, productivity surges | ~3.1% | **45–55% (most likely)** |
| AI disappoints, deficits dominate | ~1.0% | 30–40% |
| Status quo | ~2.0% | least likely |

**On labor:** Vanguard estimated AI time savings across 800+ occupations. **73% of the occupations analyzed have AI-complementary tasks with more than 20% potential time savings** (BLS/O*NET data, July 2023).

**A useful idea, the J-curve:** after a general-purpose technology arrives (electricity, PCs), productivity often *dips* before it rises, while firms invest and reorganize. AI adoption may show up as investment and talk before measurable results.

**Why it matters for us**
- It **frames the book chapter**: AI matters for retirement because of the aging workforce and pressure on public finances. Good context for the dashboard's "why this matters" text.
- Its three ways technology affects work could become an **optional lens** for our use cases: *augmentation* (helps workers), *efficiency* (automates tasks) and *transformation* (new products and models).
- It's **macro-level**, not a firm-level measure, so it doesn't give us a measurement method.
- It's an industry research report, not peer-reviewed. For TP3's "high-quality research paper" requirement, the Dong et al. paper below is a stronger candidate.

## 2. AI Intensity Dataset (GitHub: FengDong-Elon/ai-intensity-dataset)
- **What:** firm-year scores of "AI engagement" from 10-K text for **U.S. public firms, 2010–2024**, keyed by SEC CIK. It has an overall measure plus subcomponents. Released Jan 2026 as a single 4.9 MB zipped CSV.
- **Method:** not described in the README; it's in the paper below. Julie's description from the kickoff is that it essentially counts AI words in annual reports.
- **Rule:** we **must cite the paper** if we use the data.
- **Why it matters for us**
  - It's the **closest existing benchmark** to our SEC work. Our contribution is separating *use* from *talk*: Yen-Chu found only 13% of AI passages show actual use.
  - **Planned use:** evaluation check 4b compares our 2024 numbers with their score for our 7 companies. If their score tracks our *talk* volume more than our *use* score, that shows our measure adds something new.
  - Its coverage ends in 2024, so it overlaps only our FY2024 data.

## 3. The paper behind the dataset
Dong, F., Doukas, J., and Zhang, R., *"Artificial Intelligence Engagement, Firm Value, and Risk Transformation"*, working paper, SSRN abstract 6051714.
- SSRN blocks automated access, so **this still needs a human read**: someone opens it in a browser.
- Things to check:
  - their word list;
  - which 10-K sections they use;
  - how they normalize;
  - whether banks are included or excluded;
  - the posting date, since it's a likely TP3 research-paper candidate if it's within 3 years.

## My takeaways for tonight
1. Our "use vs. talk" approach is a real step beyond word counts, and the AI Intensity Dataset gives us a ready-made baseline to prove it.
2. The Vanguard report is good framing for Julie's chapter, not a method.
3. **Actions:**
   - one person reads the Dong et al. paper;
   - download the AI Intensity data and pull out our 7 companies (for evaluation check 4b);
   - Snehal is already chasing Julie's other paper links.
