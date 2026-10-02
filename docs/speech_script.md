# Speaker script: "Refilling the Buffer in a Storm"

**Format:** one A4 page per slide.
- **Top:** the slide.
- **Below:** **SAY** (the spoken text, in order), **NUMBERS** (figures to quote), **TERMS** (plain-language definitions) and **NEXT** (the transition line).

**Build:** `python code/make_speaker_script.py && cd slides && latexmk -pdf speaker_script.tex` → `Netherlands_CCyB_speaker_script.pdf`.

**Timing and speakers:** ≈ 19:35 minutes of speaking at about 120 words per minute, leaving 3–4 minutes of the 25 for hand-overs, pointing at charts and pauses. Q&A is separate.
- Zheng Huang: pages 1–9 and 18–22.
- Diego Gutiérrez: pages 10–17.
- Pages 23–24 are backup for questions.

Page numbers below are the numbers printed on the slides (n/24). All figures come from `docs/02_findings.md` and the sources cited on each slide.

---


## 1 · Title | Zheng | 0:20 | 0:00
SAY:
- Good morning. We are Zheng Huang and Diego Gutiérrez.
- Our case is the Netherlands: why the Dutch central bank, DNB, raised its countercyclical capital buffer from zero to two percent.
NUMBERS:
- CCyB 0% → 2% (fully binding 31 May 2024)
TERMS:
- DNB: De Nederlandsche Bank, the Dutch central bank and macroprudential authority.
NEXT: "In short, here is the whole story on one slide."

## 2 · One-pager | Zheng | 0:40 | 0:20
SAY:
- DNB raised the buffer twice, to two percent, while the Basel indicator, the credit-to-GDP gap, pointed to **zero**.
- The three boxes answer the three questions of the assignment: environment, criteria and risks, implications.
- Our verdict: **normalisation, not tightening**. DNB refilled a buffer; it did not fight a boom. It cost banks little, was largely offset by cuts elsewhere, and we see no sign of a contraction in lending.
NUMBERS:
- Announcements: May 2022 (1%) and May 2023 (2%); binding 25 May 2023 and 31 May 2024
- Credit-to-GDP gap at the decisions: −33pp and −47pp → Basel guide 0%
- Inflation 11.6% (2022) · CET1 17.7% (end-2021) · €6.7bn releasable
TERMS:
- CCyB: Countercyclical capital buffer. Extra bank capital (0–2.5% of risk-weighted assets) built in good times, released in bad times.
- Credit-to-GDP gap: How far credit/GDP is above its long-run trend; the Basel starting point for the CCyB.
- O-SII: "Other systemically important institution". The O-SII buffer is an extra capital charge on large banks.
NEXT: "It starts in March 2020."

## 3 · March 2020 | Zheng | 1:25 | 1:00
SAY:
- March 2020: COVID hits. Within three weeks our neighbours **release** their countercyclical buffers so that banks can keep lending.
- Sweden and Norway were at 2.5 percent; Denmark, Ireland and Lithuania at one percent.
- The Netherlands was at **zero**. There was nothing to release.
- France and Ireland followed on the first of April, and Belgium and Germany cancelled increases they had already announced. Across Europe, buffers built in good times were being used exactly as intended.
- So DNB improvised. It cut the systemic buffers of ING, Rabobank and ABN AMRO and postponed a mortgage rule, freeing about eight billion euros.
- DNB said this capital could support up to 200 billion euros of lending. But it was a workaround: these buffers were never designed to be released, so the cut had to be negotiated and explained bank by bank.
- And it made a promise *(pause)*: once things were normal, it would rebuild this capital as a two-percent countercyclical buffer.
NUMBERS:
- Releases (rate in force → new rate):
  - Denmark 1.0% → 0% (12 Mar)
  - Norway 2.5% → 1.0% (13 Mar)
  - Sweden 2.5% → 0% (16 Mar)
  - Lithuania 1.0% → 0% (31 Mar)
  - France 0.25% → 0% (1 Apr)
  - Ireland 1.0% → 0% (1 Apr)
- Cancelled pending increases: Belgium 0.5% (27 Mar) · Germany 0.25% (31 Mar)
- Also: Iceland 2.0% → 0% · Czech Republic 1.75% → 1.0%
- NL: systemic buffers 3% → 2.5% (ING) / 2% (Rabo) / 1.5% (ABN AMRO); €8bn freed (incl. the floor postponement); up to €200bn of lending
TERMS:
- Release: The authority lowers the CCyB rate with immediate effect, so banks may use that capital to absorb losses and keep lending.
- Systemic (risk) buffer: A structural capital charge on large banks; not designed to be released.
- Mortgage risk-weight floor: A minimum average risk weight on Dutch mortgages for banks using internal models.
NEXT: "That empty buffer mattered, because not all capital can be released."

## 4 · The releasable layer | Zheng | 1:00 | 2:25
SAY:
- Read the stack from the bottom: first the requirements banks must always meet, then the buffers on top.
- The red dashed line is the MDA trigger. Below it, dividends and bonuses are automatically restricted. So banks avoid using buffers even when they are allowed to; in COVID, banks near that line cut lending instead.
- The CCyB is different. The authority can switch it off, so the requirement itself falls and there is no stigma. It is the only truly **releasable** layer.
- A release is also immediate, while an increase only binds after twelve months. That asymmetry is why the buffer has to be filled before the crisis, not during it.
NUMBERS:
- Pillar 1 minimum 4.5% CET1 · capital conservation buffer 2.5%
- CCyB 0–2.5% of RWA (higher possible) · increases bind after 12 months · releases are immediate
TERMS:
- RWA: Risk-weighted assets. Assets weighted by riskiness (a mortgage counts less than a corporate loan).
- CET1: Common Equity Tier 1. The highest-quality capital (shares, retained earnings), as % of RWA.
- MDA: Maximum distributable amount. The cap on payouts that applies once capital falls below the combined buffer requirement.
- Pillar 2 requirement / guidance: The supervisor's bank-specific add-on (binding) / extra expectation (non-binding).
NEXT: "Two years later DNB refilled exactly that layer, at a strange moment."

## 5 · The question | Zheng | 0:50 | 3:25
SAY:
- Now look at 2022: war, record energy prices, 11.6 percent inflation, ECB rate hikes and a housing market about to turn. And the Basel indicator says zero.
- Under the Basel guide, a gap below two points means a zero buffer, and the gap was more than thirty points below that threshold.
- Raising capital in a downturn amplifies the cycle, which is exactly what the CCyB is meant to avoid.
- So our question: **was this the wrong moment?** We answer it in three acts, which are the three questions of the assignment.
NUMBERS:
- HICP inflation 11.6% (2022) · ECB first hike 21 Jul 2022 (+50bp)
- Credit-to-GDP gap −33pp (data to 2021Q4) and −47pp (data to 2022Q4)
TERMS:
- Procyclical: Policy that reinforces the cycle (tighter in bad times, looser in good times).
- Basel buffer guide: Gap below 2pp → 0% buffer; above 10pp → 2.5%; linear in between.
NEXT: "Act 1, the setting. The refill followed a path promised in 2020."

## 6 · Timeline | Zheng | 0:35 | 4:15
SAY:
- After the promise in 2020, DNB published its framework in February 2022 and announced one percent in May 2022, just before the ECB began to hike.
- In May 2023 it announced two percent, together with lower buffers for the largest banks. Both became binding on 31 May 2024.
- It has held two percent every quarter since. The mortgage floor expires in November 2026.
NUMBERS:
- 17 Mar 2020 · 29 Dec 2020 · 1 Jan 2022 · Feb 2022 · 25 May 2022 · 31 May 2023 · 31 May 2024 · 30 Nov 2026
- ECB hikes: first on 21 Jul 2022; still hiking on 14 Sep 2023
TERMS:
- Announcement vs binding date: Banks get 12 months between a CCyB increase being announced and having to meet it.
- CRD V: The 2019 revision of the EU Capital Requirements Directive; it made the O-SII and systemic risk buffers additive, prompting DNB's conversion.
NEXT: "By then the economy had fully recovered, but the outlook was darkening."

## 7 · Macro | Zheng | 0:45 | 4:50
SAY:
- By the third quarter of 2021 GDP was back above its pre-COVID level. That recovery is what DNB's framework requires before building the buffer.
- Then came the storm: war in Ukraine, record energy prices, inflation of 11.6 percent and the ECB's first hike in July 2022. DNB warned that higher funding costs would strain debt sustainability.
- So the macro picture argued **both ways**: build while the economy can take it, or wait because it is weakening.
NUMBERS:
- GDP above pre-COVID level: 2021Q3 (+1.9% q/q) · end-2021 ≈ +3% vs end-2019
- HICP 11.6% in 2022 (national CPI 10.0%)
- ECB +50bp on 21 Jul 2022
TERMS:
- HICP: Harmonised Index of Consumer Prices, the euro-area-comparable inflation measure.
- Basis point (bp): 0.01 percentage point; 50bp = 0.5pp.
NEXT: "In the financial system, credit was cold and only housing was hot."

## 8 · Credit and housing | Zheng | 0:55 | 5:35
SAY:
- Left: **housing was hot**. Nominal prices rose 19 percent in a year, and DNB itself called the market overheated. But as mortgage rates rose, real prices fell about nine percent.
- In real terms prices were 16 percent above their 2007 peak, so the level was high even after correcting for inflation.
- Middle: household debt is high, 107 percent of GDP against 58 in the euro area, but it was **falling**.
- Right: the share of income spent on debt service was the lowest since 2005.
- If there was a boom, it was in house prices, not in credit.
NUMBERS:
- Nominal house prices +19.0% y/y (2022Q1); real index 129 vs 2007 peak 111 (+16%)
- Real house prices −9.2% (2022Q2–2023Q2)
- Household debt/GDP: 110% (2019Q4) → 107% (2022Q1) → 100% (2023Q1); euro area 57.7% (2022Q1)
- Debt-service ratio, households: 14.6% (2022Q1)
TERMS:
- Debt-service ratio: Interest plus principal payments as a share of income.
- Real house prices: Nominal prices deflated by consumer prices.
NEXT: "And the banks entered this storm well capitalised."

## 9 · Banks | Zheng | 0:45 | 6:30
SAY:
- Core capital was 17.7 percent of risk-weighted assets at the end of 2021, above the EU average, and in DNB's stress test the big banks stayed well above the minimum.
- Rising rates also **lifted profits**: net interest income grew 6.7 percent in 2022. Remember that, because it comes back.
- Act 1 in one line: war, inflation, rate hikes and a turning housing market argued against raising now; a recovered economy, cold credit and strong banks argued for it.
NUMBERS:
- CET1 17.7% (end-2021; EU 15.7% in 2021Q3) → 16.3% (end-2022, in line with EU)
- Stress test (FSR 2023): −3.8pp → 11.5% at end-2025 (min. 8%)
- Net interest income +6.7% in 2022; 67.7% of bank income
TERMS:
- Stress test: A simulation of a severe recession to check whether capital stays above the minimum.
- Net interest income: Interest earned on loans minus interest paid on deposits and funding.
NEXT: **HAND-OVER:** "That was the setting. So why did DNB ignore its own rulebook? Diego."

## 10 · Why not the Basel rule? | Diego | 1:30 | 7:15
SAY:
- Thank you. So why ignore the rulebook? Because on Dutch data it has a poor record.
- The red line is the credit-to-GDP gap, credit relative to its long-run trend. We rebuilt it and match the official BIS series.
- Under the Basel guide the buffer starts when the gap exceeds two points and reaches its maximum at ten. So everything depends on this one number being reliable.
- It **missed** the financial crisis, at minus 13 in 2007. It raised a **false alarm** in 2012, during a bust. And it gets **revised**: 2016 read slightly negative at the time and plus 27 today.
- The reason: Dutch credit grew from about 50 to 350 percent of GDP, and the filter mistakes that structural rise for trend.
- One-sided means the filter only uses data available at each date, which is what a policymaker actually sees. That is why the signal can change years later, once new data arrive.
- At the two decisions it read minus 33 and minus 47. The rule said zero.
NUMBERS:
- Gap: −13.4pp (2007Q4) · +16.8pp (2012Q2) · 2016Q1 −0.6pp real time vs +26.9pp ex post
- −32.7pp (2021Q4) and −46.8pp (2022Q4) at the decisions
- Credit/GDP 47% (1961) → 352% (2015Q1 peak)
- Replication error ≤ 0.00005pp (1971–2026)
TERMS:
- HP filter: Splits a series into a smooth trend and a cycle; λ = 400,000 for credit cycles.
- One-sided vs two-sided filter: One-sided uses only data up to each date (what policymakers see); two-sided also uses later data (hindsight).
- False alarm / missed crisis: Type II / type I errors of an early-warning indicator.
NEXT: "So DNB used its own compass instead."

## 11 · DNB's framework | Diego | 1:10 | 8:45
SAY:
- DNB's 2022 framework has four phases: release after a crisis, **two percent in normal times**, more when risks are high, and release again in a crisis.
- This is a *positive neutral* buffer: already filled when risks are neither high nor low.
- The two percent comes from history. Past crises cost Dutch banks about 12 billion euros at the peak. Two percent is about six billion of releasable capital, enough to support up to 150 billion of lending.
- The ECB's own loss-based estimates give 1.1 to 1.8 percent, so two percent is at the top of that range but not outside it. We come back to that in the critiques.
- Seventeen jurisdictions now work this way; Sweden, the UK and Poland also target two percent.
NUMBERS:
- Peak accumulated losses €12bn (2007–2016) → 2% ≈ €6bn → up to €150bn of lending
- Build-up: 1pp per year → 2% after two years
- 17 jurisdictions with a positive neutral CCyB (BCBS 2024); ECB loss-based range 1.1–1.8%
TERMS:
- Positive neutral CCyB: A CCyB kept above zero in a "standard" risk environment.
- Peak accumulated losses: The largest cumulative loss a bank suffered over a crisis period.
- Guided discretion: Decisions informed by a published set of indicators, with judgement, not a formula.
NEXT: "And its stated reasons were never credit growth."

## 12 · DNB's reasons | Diego | 0:35 | 9:55
SAY:
- In 2022 DNB wrote that it was **restoring the buffers** it had lowered in March 2020, citing the recovery and a normal-to-elevated risk picture.
- In 2023 it said the credit gap showed **no signs of excessive credit growth**, and pointed instead to risk appetite, falling property prices, debt sustainability and strong banks.
- Credit growth was never the reason.
NUMBERS:
- 1% step: about €3.3bn of extra CET1 (announced 25/27 May 2022)
- 2% step: about €3.4bn (announced 31 May 2023)
TERMS:
- Cyclical systemic risk: Risk that builds up over the financial cycle (credit, asset prices, risk-taking) and can materialise system-wide.
NEXT: "So what was the buffer meant for?"

## 13 · Risks and tools | Diego | 0:55 | 10:30
SAY:
- Each risk got its own tool.
- This matters for our question. If housing had been the target, the CCyB would be the wrong tool: it hits all lending, not just mortgages.
- **Shocks nobody can forecast**, such as war, an energy shock, a sudden tightening or bank turmoil abroad, go to the CCyB, because it can be released whatever the source.
- **Housing**, the known hot spot, went to borrower limits, tax reform and a mortgage risk-weight floor. The **size of the big banks** goes to the systemic buffer.
- One instrument per target: the Tinbergen principle.
NUMBERS:
- Banking sector: ≈ 400% of GDP (when O-SII buffers were phased in) → 280% (end-2022)
- Risk-weight floor in force Jan 2022 – Nov 2026
TERMS:
- LTV / LTI: Loan-to-value / loan-to-income. Caps on mortgage size relative to house value or income.
- Tinbergen principle: Reach each policy target with its own instrument.
- Borrower-based measures: Rules on borrowers (LTV, LTI) rather than on bank capital.
NEXT: "Now we can test the evidence against both readings."

## 14 · The verdict | Diego | 1:15 | 11:25
SAY:
- Overheating or normalisation? Each predicts something different. Row by row:
- If DNB was fighting a boom, the buffer should follow credit and prices. If it was refilling, it should follow a fixed path back to its normal level. These readings make different predictions, so we can test them.
- **Indicators.** Overheating says the buffer rises with them. They all fell while the buffer rose.
- **Path.** Normalisation says one point a year, then stop at two. That is exactly what happened.
- **2023.** Prices falling, rates jumping. An overheating fighter pauses; DNB raised.
- **2024 to 2026.** Prices up ten percent again. An overheating fighter goes above two; DNB held.
- **Other buffers.** Normalising means cutting structural buffers in return. DNB did, twice.
- *(pause)* Five out of five.
- Every observation fits normalisation, and none fits overheating. This is the core of our argument.
NUMBERS:
- Gap, debt-service ratio and household debt ratio all falling in 2022–23
- House prices +10% y/y (DNB, Mar 2026) · CCyB held at 2% since May 2024
TERMS:
- Phase 3 ("increased risk"): The framework phase in which the CCyB goes above 2%.
NEXT: "And that last row tells us the refill was a swap, not a squeeze."

## 15 · A swap, not a squeeze | Diego | 1:00 | 12:40
SAY:
- In euros, by our own estimate: the 2020 cut released about six billion; the CCyB then added 3.3 and 3.4 billion; the 2024 cut released another 2.7 billion.
- Net, compared with before COVID, the requirement is roughly unchanged. DNB called it "more or less capital-neutral".
- Two caveats: the bases differ, and compared with 2021 rather than 2019 it was a modest increase.
- So capital was **moved**, from buffers that cannot be released into one that can.
- Think of it as moving money from a locked savings account into a current account that the authority can open in a crisis. The total is similar; what changes is who can use it, and when.
NUMBERS:
- −6.0 (2020: ING 1.7, Rabo 2.4, ABN 1.9) · +3.3 (May-23) · +3.4 (May-24) · −2.7 (May-24 O-SII) → net ≈ −2.0 €bn vs pre-COVID
- Valued at end-2022 total RWA; BNG excluded
TERMS:
- Structural buffer: A capital charge for permanent features (size, interconnectedness), kept through the cycle.
- UK approach: The UK offset its 2% neutral CCyB by lowering Pillar 2A and resolution requirements.
NEXT: "So, was it the wrong moment?"

## 16 · The twist | Diego | 1:00 | 13:40
SAY:
- No. The storm made it the **cheapest** moment.
- Headroom is capital above a bank's requirement. The four big banks had about 36 billion euros at the end of 2022; the full buffer of 6.7 billion is **at most a fifth** of that.
- Bank by bank: Rabobank had 14.2 billion of headroom, ING 12.6, ABN AMRO 7.1, and even the smallest, de Volksbank, 1.7 billion. The first step of 3.3 billion was only 8 percent of the total.
- And rising rates lifted profits, so banks could build the buffer from retained earnings instead of cutting loans.
- ECB research agrees: profitable banks and a gradual build-up keep the costs low, also during the 2022 to 2023 tightening.
NUMBERS:
- Headroom end-2021 / end-2022 (€bn):
  - ING 16.9 / 12.6
  - Rabobank 15.7 / 14.2
  - ABN AMRO 7.9 / 7.1
  - de Volksbank 1.9 / 1.7
- Total headroom €42.3bn / €35.5bn → CCyB €3.3bn = 8%, €6.7bn = 19%
TERMS:
- Headroom: CET1 capital above the bank's requirement (its MDA trigger).
- Retained earnings: Profits kept in the bank instead of being paid out.
NEXT: "And borrowers did not pay either."

## 17 · Borrowers | Diego | 1:15 | 14:40
SAY:
- We compare Dutch lending with five euro-area countries that never changed their buffer.
- The controls are Austria, Finland, Italy, Malta and Luxembourg. They kept their buffer unchanged throughout, so any difference is not driven by their own policy.
- The red line is the Netherlands minus those countries. The grey band shows the differences that arise by chance, when we pretend each control country was treated.
- Mortgage rates stay **inside the band** at all three dates. Household credit grew **faster**, partly as catch-up.
- In numbers: Dutch bank credit grew 16.6 percent from early 2022 to early 2026, against 7.9 percent in the euro area. Between 2019 and 2022 it had lagged, 4.3 against 11.3 percent. That is the catch-up.
- So: **no sign of contraction**, though not a causal estimate. DNB reached the same view in September 2026.
NUMBERS:
- Dates: May-22 (1% announced) · May-23 (1% binding, 2% announced) · May-24 (2% binding)
- Bank credit 2022Q1–2026Q1: NL +16.6% vs euro area +7.9%; 2019–22: NL +4.3% vs +11.3%
TERMS:
- Event study: Tracks the difference between treated and control groups before and after an event.
- Placebo test: Rerun the analysis pretending an untreated country was treated, to see what chance alone produces.
NEXT: **HAND-OVER:** "So banks and borrowers were fine. What about the wider effects? Zheng."

## 18 · Monetary policy | Zheng | 0:35 | 15:55
SAY:
- Thank you. First, the buffer did not double the ECB's squeeze: Dutch lending rates moved with their peers, and bank profits rose with rates.
- The ECB argues that building buffers early lets monetary policy focus on inflation.
- With one monetary policy for twenty countries, the CCyB is the **Dutch-specific lever**, and insurance if a rate shock goes wrong.
NUMBERS:
- ECB hiking from Jul 2022 (first +50bp) to at least Sep 2023
TERMS:
- Macroprudential policy: Policy aimed at the stability of the financial system as a whole.
- Monetary policy: Interest-rate policy aimed at price stability (ECB, euro area-wide).
NEXT: "Through reciprocity, the 2% also reaches foreign lenders."

## 19 · Across borders | Zheng | 0:30 | 16:30
SAY:
- Foreign banks lending into the Netherlands must hold the Dutch two percent too, which limits leakage to foreign lenders. Leakage to non-banks remains.
- And Europe is moving the same way: Germany, France, Ireland and Belgium raised their buffers in 2023 and 2024, and Portugal and Spain follow in 2026.
NUMBERS:
- Germany 0.75% (Feb 2023) · France 1.0% (Jan 2024) · Ireland 1.5% (Jun 2024) · NL 2.0% (May 2024) · Belgium 1.0% (Oct 2024) · Portugal 0.75% (Jan 2026) · Spain 1.0% (Oct 2026)
- Positive-neutral rates in 2023: Cyprus 0.5%, Estonia and Lithuania 1.0%, Ireland 1.5%, NL 2.0%
TERMS:
- Reciprocity: Foreign banks apply the host country's CCyB rate to exposures there (mandatory in the EU up to 2.5%).
- Leakage: Credit shifting to lenders not covered by the rule (foreign branches, non-banks).
NEXT: "The result for the Netherlands:"

## 20 · Resilience | Zheng | 0:55 | 17:00
SAY:
- In 2020 the Netherlands had no releasable capital. Today it has **6.7 billion euros**, about half of past peak losses and enough to support up to 150 billion of lending.
- It is cheap to hold and powerful to release: research suggests a release in bad times raises lending far more than the build-up costs in good times.
- In numbers: a one-point build-up in normal times reduces lending by about 0.1 percent, while a one-point release in bad times can raise it by up to ten percent.
- And with the mortgage floor expiring in November 2026, it matters even more.
NUMBERS:
- €0 → €6.7bn releasable · ≈ half of €12bn peak losses · up to €150bn of lending
- Lang & Menno (2023): −0.1% lending per +1pp (normal times) vs up to +10% per 1pp release (bad times)
TERMS:
- State-dependent effect: The impact of a policy depends on the state of the economy (small in good times, large in bad times).
NEXT: "The price is reliance on discretion."

## 21 · Critiques | Zheng | 0:50 | 17:55
SAY:
- **Credibility:** without a rule, markets must trust DNB's judgement, so it has to explain itself every quarter.
- **Calibration:** why two percent, when ECB estimates suggest 1.1 to 1.8?
- **Untested:** will banks lend released capital, or hoard it?
- In 2020 many banks did not use the buffers they were allowed to use. A released CCyB is different, because the requirement itself falls, but that has not yet been tested in the Netherlands.
- **Baseline:** compared with 2021, it was an increase.
- **Profits:** the same bank profits were also targeted by excess-profit levies.
NUMBERS:
- ECB loss-based range 1.1–1.8% vs NL 2% · +€3.3bn vs 2021 before the O-SII offset
TERMS:
- Rules vs discretion: The trade-off between predictable formulas and flexible judgement (Kydland & Prescott 1977).
- Excess-profit levy: A temporary tax on bank profits seen as windfalls from higher rates.
NEXT: "In short, the promise was kept."

## 22 · Conclusion | Zheng | 0:50 | 18:45
SAY:
- **Environment:** a recovered economy in a storm, cold credit, cooling housing and strong banks.
- **Criteria and risks:** a two-percent normal level based on past losses, for shocks nobody can forecast, with housing left to other tools.
- **Implications:** cheap, largely a swap, no sign of contraction, and 6.7 billion euros now releasable, at the price of discretion.
- *(pause)* In March 2020 the Netherlands had nothing to release. **Next time, it will.** The best time to fill a buffer is when nobody thinks you need it. Thank you.
NUMBERS:
- 0% → 2% · −33 / −47pp gap · ≤ 1/5 of headroom · €6.7bn releasable
TERMS:
- Normalisation: Returning the buffer to its normal-times level, not reacting to overheating.
NEXT: Questions; leave the conclusion slide up, or go to page 23 or 24.

## 23 · Glossary | both | backup | Q&A
SAY:
- Backup only. Use it when a question involves a term; point to the row and give the one-line definition.
NUMBERS:
- (definitions only)
TERMS:
- All key terms of the talk are on the slide
NEXT: Back to the question.

## 24 · Methods and references | both | backup | Q&A
SAY:
- Backup for method questions.
  - **Credit gap:** one-sided and two-sided HP filter (λ = 400,000), plus Hamilton regression filter.
  - **Headroom:** (CET1 ratio minus requirement) × total RWA, per bank.
  - **Event study:** two-way fixed effects, three-month bins, placebo inference over five never-treated countries.
- All references are verified.
NUMBERS:
- Data: BIS, ECB Data Portal (MIR, BSI), ESRB, DNB, bank reports
TERMS:
- Two-way fixed effects: Regression with country and time dummies, so differences are measured relative to common trends.
NEXT: Back to the question.
