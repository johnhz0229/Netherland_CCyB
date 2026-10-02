# Speaker script: "Refilling the Buffer in a Storm"

**Format:** one A4 page per slide.
- **Top:** the slide.
- **Below:** **SAY** (the spoken text, in order), **NUMBERS** (figures to quote), **TERMS** (plain-language definitions) and **NEXT** (the transition line).

**Build:** `python code/make_speaker_script.py && cd slides && latexmk -pdf speaker_script.tex` → `Netherlands_CCyB_speaker_script.pdf`.

**Timing and speakers:** ≈ 23:15 minutes of speaking at about 120 words per minute, which leaves about 1 minutes of the 25 for hand-overs, pointing at charts and pauses. Q&A is separate.
- Zheng Huang: pages 1–9 and 18–22.
- Diego Gutiérrez: pages 10–17.
- Pages 23–24 are backup for questions.

Page numbers below are the numbers printed on the slides (n/24). All figures come from `docs/02_findings.md` and the sources cited on each slide.

---


## 1 · Title | Zheng | 0:30 | 0:00
SAY:
- Good morning. We are Zheng Huang and Diego Gutiérrez, and our case is the Netherlands.
- In 2022 and 2023 the Dutch central bank, De Nederlandsche Bank or DNB, raised its countercyclical capital buffer from zero to two percent. We want to explain why it did that, and whether it was a good idea.
NUMBERS:
- CCyB 0% → 2% (fully binding 31 May 2024)
TERMS:
- DNB: De Nederlandsche Bank, the Dutch central bank and macroprudential authority.
NEXT: "In short, here is the whole story on one slide."

## 2 · One-pager | Zheng | 1:00 | 0:30
SAY:
- Here is the whole story on one slide. DNB raised the buffer in two steps, to one percent and then to two percent. Yet at both decisions the indicator at the centre of the Basel rules, the credit-to-GDP gap, was deeply negative, so the rulebook said the buffer should be zero.
- The three columns follow the three questions of the assignment: the environment, the criteria and risks, and the implications.
- Our verdict is that this was **normalisation, not tightening**. DNB was refilling an empty buffer, not fighting a credit boom. The price is that the policy relies on DNB's judgement rather than on a rule.
NUMBERS:
- Announcements: May 2022 (1%) and May 2023 (2%); binding 25 May 2023 and 31 May 2024
- Credit-to-GDP gap at the decisions: −33pp and −47pp → Basel guide 0%
- Inflation 11.6% (2022) · CET1 17.7% (end-2021) · €6.7bn releasable
TERMS:
- CCyB: Countercyclical capital buffer. Extra bank capital (0–2.5% of risk-weighted assets) built in good times, released in bad times.
- Credit-to-GDP gap: How far credit/GDP is above its long-run trend; the Basel starting point for the CCyB.
- O-SII: "Other systemically important institution". The O-SII buffer is an extra capital charge on large banks.
NEXT: "It starts in March 2020."

## 3 · March 2020 | Zheng | 1:15 | 1:30
SAY:
- The story starts in March 2020. When COVID hit, our neighbours reacted within three weeks: eight European countries cut their countercyclical buffers, as the chart shows. Sweden and Norway had been at two and a half percent; Denmark, Ireland and Lithuania at one percent. Buffers built in good times were used exactly as intended.
- The Netherlands was at **zero**, the red dot at the bottom. There was nothing to release.
- So DNB improvised. It cut the systemic buffers of ING, Rabobank and ABN AMRO and postponed a planned floor on mortgage risk weights. This freed about eight billion euros of capital, enough to support up to 200 billion euros of lending. But those buffers were never designed to be released.
- And DNB made a promise *(pause)*: once things were back to normal, it would rebuild this capital as a two-percent countercyclical buffer.
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

## 4 · The releasable layer | Zheng | 1:10 | 2:45
SAY:
- Why did an empty buffer matter? Because not all bank capital can be used in a crisis.
- Read the stack from the bottom: first the minimum requirements, then the buffers on top. The red dashed line is the MDA trigger. If a bank falls below it, its dividends and bonuses are restricted automatically, and markets read that as weakness. So in COVID, banks close to this line cut lending rather than use buffers they were formally allowed to use.
- The countercyclical buffer is different. The authority can switch it off, so the requirement itself falls, with no penalty and no stigma. It is the only truly **releasable** layer. And while an increase binds only after twelve months, a release is immediate, so the buffer must be filled before a crisis.
NUMBERS:
- Pillar 1 minimum 4.5% CET1 · capital conservation buffer 2.5%
- CCyB 0–2.5% of RWA (higher possible) · increases bind after 12 months · releases are immediate
TERMS:
- RWA: Risk-weighted assets. Assets weighted by riskiness (a mortgage counts less than a corporate loan).
- CET1: Common Equity Tier 1. The highest-quality capital (shares, retained earnings), as % of RWA.
- MDA: Maximum distributable amount. The cap on payouts that applies once capital falls below the combined buffer requirement.
- Pillar 2 requirement / guidance: The supervisor's bank-specific add-on (binding) / extra expectation (non-binding).
NEXT: "Two years later DNB refilled exactly that layer, at a strange moment."

## 5 · The question | Zheng | 1:00 | 3:55
SAY:
- Two years later, in 2022, DNB began to refill the buffer, and the timing looks strange. On the left is the storm: war, record energy prices, 11.6 percent inflation, the first ECB rate hikes and a housing market about to turn. And the Basel indicator said zero. On the right is the decision: one percent, then two percent.
- Raising capital requirements in a downturn can amplify the cycle. That is exactly the procyclical mistake the buffer was invented to avoid.
- So our question is: **was this the wrong moment?** Was DNB tightening into a slowdown, fighting a hidden boom, or doing something else? We answer in three acts, one for each question of the assignment.
NUMBERS:
- HICP inflation 11.6% (2022) · ECB first hike 21 Jul 2022 (+50bp)
- Credit-to-GDP gap −33pp (data to 2021Q4) and −47pp (data to 2022Q4)
TERMS:
- Procyclical: Policy that reinforces the cycle (tighter in bad times, looser in good times).
- Basel buffer guide: Gap below 2pp → 0% buffer; above 10pp → 2.5%; linear in between.
NEXT: "Act 1, the setting. The refill followed a path promised in 2020."

## 6 · Timeline | Zheng | 1:00 | 4:55
SAY:
- Act one is the setting, and it starts with the timeline. In March 2020 DNB cut the systemic buffers and made its promise. In February 2022 it published a framework with two percent as the normal level. In May 2022 it announced one percent, two months before the ECB's first hike. In May 2023 it announced two percent, together with lower buffers for the largest banks, and both became binding in May 2024.
- Since then DNB has held two percent at every quarterly review. So the path was two equal steps, a year apart, and then a stop. Keep that pattern in mind for our verdict.
NUMBERS:
- 17 Mar 2020 · 29 Dec 2020 · 1 Jan 2022 · Feb 2022 · 25 May 2022 · 31 May 2023 · 31 May 2024 · 30 Nov 2026
- ECB hikes: first on 21 Jul 2022; still hiking on 14 Sep 2023
TERMS:
- Announcement vs binding date: Banks get 12 months between a CCyB increase being announced and having to meet it.
- CRD V: The 2019 revision of the EU Capital Requirements Directive; it made the O-SII and systemic risk buffers additive, prompting DNB's conversion.
NEXT: "By then the economy had fully recovered, but the outlook was darkening."

## 7 · Macro | Zheng | 0:55 | 5:55
SAY:
- What did the economy look like? The left panel shows that real GDP was back above its pre-COVID level during 2021, which is the condition DNB's framework sets before rebuilding the buffer.
- Then the storm arrived. Inflation, in the middle, peaked at 17 percent in September 2022, and on the right the ECB moved its deposit rate from minus half a percent to four percent in fourteen months. DNB warned that higher funding costs could strain the debt of governments, firms and households.
- So the macro picture argued **both ways**: build while the economy can take it, or wait because it is weakening.
NUMBERS:
- GDP above pre-COVID level in 2021 (CBS first estimate: 2021Q3; current ECB vintage: 2021Q2, +3.7% vs 2019Q4 by end-2021)
- HICP 11.6% average in 2022, peak 17.1% (Sep 2022); national CPI 10.0%
- ECB deposit rate −0.50% → 4.00% (Jul 2022 – Sep 2023); first hike +50bp on 21 Jul 2022
TERMS:
- HICP: Harmonised Index of Consumer Prices, the euro-area-comparable inflation measure.
- Basis point (bp): 0.01 percentage point; 50bp = 0.5pp.
NEXT: "In the financial system, credit was cold and only housing was hot."

## 8 · Credit and housing | Zheng | 1:00 | 6:50
SAY:
- What about the financial system? On the left you see housing, and housing was hot. Nominal house prices rose 19 percent in a single year, real prices were well above their 2007 peak, and DNB itself called the market overheated. But as mortgage rates rose, real prices fell by about nine percent.
- In the middle is household debt. It is high, at 107 percent of GDP against 58 percent in the euro area, but it was **falling**. On the right is the share of income that households spend on interest and repayments. It was the lowest since 2005.
- So if there was a boom, it was in house prices, not in credit.
NUMBERS:
- Nominal house prices +19.0% y/y (2022Q1); real index 129 vs 2007 peak 111 (+16%)
- Real house prices −9.2% (2022Q2–2023Q2)
- Household debt/GDP: 110% (2019Q4) → 107% (2022Q1) → 100% (2023Q1); euro area 57.7% (2022Q1)
- Debt-service ratio, households: 14.6% (2022Q1)
TERMS:
- Debt-service ratio: Interest plus principal payments as a share of income.
- Real house prices: Nominal prices deflated by consumer prices.
NEXT: "And the banks entered this storm well capitalised."

## 9 · Banks | Zheng | 1:00 | 7:50
SAY:
- Finally, the banks. Dutch banks entered the storm with a core capital ratio of 17.7 percent, two points above the EU average. In DNB's 2023 stress test, the four largest banks fell by 3.8 points in a severe recession but stayed at 11.5 percent, well above the minimum.
- Rising rates also **lifted their profits**: net interest income grew 6.7 percent in 2022. Please remember this, because it will come back in act three.
- So act one in one sentence: war, inflation, rate hikes and a turning housing market argued against raising the buffer, while a recovered economy, cold credit and strong banks argued for it.
NUMBERS:
- CET1 17.7% (end-2021; EU 15.7% in 2021Q3) → 16.3% (end-2022, in line with EU)
- Stress test (FSR 2023): 15.2% (end-2022) −3.8pp → 11.5% at end-2025 (min. 8%)
- Net interest income +6.7% in 2022; 67.7% of bank income
TERMS:
- Stress test: A simulation of a severe recession to check whether capital stays above the minimum.
- Net interest income: Interest earned on loans minus interest paid on deposits and funding.
NEXT: **HAND-OVER:** "That was the setting. So why did DNB ignore its own rulebook? Diego."

## 10 · Why not the Basel rule? | Diego | 1:30 | 8:50
SAY:
- Thank you, Zheng. Act two is the decision, and the first question is: why did DNB ignore the rulebook? Because on Dutch data the rulebook has a poor record.
- The red line is the credit-to-GDP gap: how far credit relative to GDP is above its long-run trend. Under the Basel guide the buffer starts when the gap exceeds two points. We rebuilt the gap ourselves, and it matches the official BIS series almost exactly.
- Look at its record. It **missed** the financial crisis, reading minus 13 on the eve of 2008. It raised a **false alarm** in 2012, in the middle of a bust. And it gets **revised**: 2016 read slightly negative at the time and plus 27 with today's data. The reason is that Dutch credit grew from about 50 to 350 percent of GDP, and the filter mistakes that structural rise for a trend.
- At the two decisions the gap read minus 33 and minus 47. Taken literally, the rule said zero.
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

## 11 · DNB's framework | Diego | 1:15 | 10:20
SAY:
- So DNB used its own compass. Its 2022 framework has four phases: release after a crisis, **two percent in normal times**, more than two percent when risks are clearly elevated, and release again in a crisis. This is a positive neutral buffer: it is already filled when risks are neither high nor low.
- The two percent comes from history, not from credit growth. At the peak, past crises cost Dutch banks about 12 billion euros. Two percent is about six billion euros of releasable capital, roughly half of those losses, and enough to support up to 150 billion euros of lending. The ECB's own estimates range from 1.1 to 1.8 percent, so two percent is at the top of the range, but not outside it.
- Seventeen jurisdictions now work this way, and Sweden, the UK and Poland also target two percent.
NUMBERS:
- Peak accumulated losses €12bn (2007–2016) → 2% ≈ €6bn → up to €150bn of lending
- Build-up: 1pp per year → 2% after two years
- 17 jurisdictions with a positive neutral CCyB (BCBS 2024); ECB loss-based range 1.1–1.8%
TERMS:
- Positive neutral CCyB: A CCyB kept above zero in a "standard" risk environment.
- Peak accumulated losses: The largest cumulative loss a bank suffered over a crisis period.
- Guided discretion: Decisions informed by a published set of indicators, with judgement, not a formula.
NEXT: "And its stated reasons were never credit growth."

## 12 · DNB's reasons | Diego | 1:00 | 11:35
SAY:
- What reasons did DNB actually give? In May 2022 it wrote that it was **restoring the buffers** it had lowered in March 2020. It acknowledged the uncertainty from the war, but said the robust recovery justified a gradual build-up.
- In May 2023 it went further. It wrote that the credit gap showed **no signs of excessive credit growth**. Instead it pointed to investors' rising risk appetite, falling property prices, the debt sustainability of firms and governments, and banks that were robust, partly thanks to higher rates.
- So both decisions rested on the same three pillars: a normal-to-elevated risk picture, strong banks and the 2020 promise. Credit growth was never the reason.
NUMBERS:
- 1% step: about €3.3bn of extra CET1 (announced 25/27 May 2022)
- 2% step: about €3.4bn (announced 31 May 2023)
TERMS:
- Cyclical systemic risk: Risk that builds up over the financial cycle (credit, asset prices, risk-taking) and can materialise system-wide.
NEXT: "So what was the buffer meant for?"

## 13 · Risks and tools | Diego | 1:10 | 12:35
SAY:
- Which risks was the buffer meant to cover? DNB matched each risk with its own tool.
- The top row is **shocks nobody can forecast**: war, an energy shock, a sudden tightening of financial conditions, or bank turmoil abroad like Silicon Valley Bank and Credit Suisse in 2023. These go to the countercyclical buffer, because it can be released whatever the source of the shock.
- **Housing**, the known hot spot, was handled by borrower limits, tax reform and a mortgage risk-weight floor. The **size of the big banks** is handled by the structural buffer for systemically important banks.
- This is the Tinbergen principle: one instrument per target. If housing had been the target, the countercyclical buffer would have been the wrong tool, because it raises the cost of all lending.
NUMBERS:
- Banking sector: ≈ 400% of GDP (when O-SII buffers were phased in) → 280% (end-2022)
- Risk-weight floor in force Jan 2022 – Nov 2026
TERMS:
- LTV / LTI: Loan-to-value / loan-to-income. Caps on mortgage size relative to house value or income.
- Tinbergen principle: Reach each policy target with its own instrument.
- Borrower-based measures: Rules on borrowers (LTV, LTI) rather than on bank capital.
NEXT: "Now we can test the evidence against both readings."

## 14 · The verdict | Diego | 1:10 | 13:45
SAY:
- Now we can test the two readings. If DNB was fighting a boom, the buffer should follow credit and prices. If it was normalising, it should follow a fixed path back to its normal level. Row by row:
- **Credit indicators:** they all fell while the buffer rose. **The path:** one point a year and a stop at two, exactly as normalisation predicts. **2023:** prices falling and rates jumping; a boom fighter would pause, but DNB raised. **2024 to 2026:** house prices up about ten percent again; a boom fighter would go above two percent, but DNB held. **Other buffers:** normalisation means cutting structural buffers in return, and DNB did so twice.
- *(pause)* Five predictions, five matches for normalisation, and none for overheating. This is the core of our argument.
NUMBERS:
- Gap, debt-service ratio and household debt ratio all falling in 2022–23
- House prices +10% y/y (DNB, Mar 2026) · CCyB held at 2% since May 2024
TERMS:
- Phase 3 ("increased risk"): The framework phase in which the CCyB goes above 2%.
NEXT: "And that last row tells us the refill was a swap, not a squeeze."

## 15 · A swap, not a squeeze | Diego | 1:05 | 14:55
SAY:
- And the last row shows that the refill was a swap, not a squeeze. By our estimate, the 2020 cut released about six billion euros, the two countercyclical steps added 3.3 and 3.4 billion, and the 2024 cut released another 2.7 billion. Net, compared with before COVID, banks hold roughly the same required capital, or slightly less. DNB called it more or less capital-neutral for the three large banks.
- Two caveats: the bases differ, so the numbers are approximate, and compared with 2021 the refill was a modest increase.
- So capital was **moved** from buffers that cannot be released into one that can. The total stayed similar; what changed is who can use it, and when.
NUMBERS:
- −6.0 (2020: ING 1.7, Rabo 2.4, ABN 1.9) · +3.3 (May-23) · +3.4 (May-24) · −2.7 (May-24 O-SII) → net ≈ −2.0 €bn vs pre-COVID
- Valued at end-2022 total RWA; BNG excluded
TERMS:
- Structural buffer: A capital charge for permanent features (size, interconnectedness), kept through the cycle.
- UK approach: The UK offset its 2% neutral CCyB by lowering Pillar 2A and resolution requirements.
NEXT: "So, was it the wrong moment?"

## 16 · The twist | Diego | 1:05 | 16:00
SAY:
- So, was it the wrong moment? We think not. The storm actually made it the **cheapest** moment.
- Headroom is the capital a bank holds above its requirement. At the end of 2022 Rabobank had 14.2 billion euros, ING 12.6, ABN AMRO 7.1 and de Volksbank 1.7, about 36 billion in total. The first step of 3.3 billion used eight percent of that, and the full buffer of 6.7 billion at most a fifth.
- And here is the twist. The same rising rates that made the moment look dangerous lifted bank profits, so banks could build the buffer from retained earnings instead of cutting loans. ECB research agrees that profitable banks and a gradual build-up keep the costs low.
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

## 17 · Borrowers | Diego | 1:10 | 17:05
SAY:
- Did borrowers pay instead? We compare Dutch lending with five euro-area countries that never changed their buffer: Austria, Finland, Italy, Malta and Luxembourg.
- The red line is the Netherlands minus those countries. The grey band shows the differences that arise by chance, when we pretend each control country was the one that raised its buffer. Mortgage rates stay **inside the band** at all three dates. Household credit actually grew **faster**: Dutch bank credit grew 16.6 percent from early 2022 to early 2026, against 7.9 percent in the euro area, partly as a catch-up after lagging before.
- So we find **no sign of contraction**. With only one treated country this is not a causal estimate, but DNB reached the same conclusion in September 2026.
NUMBERS:
- Dates: May-22 (1% announced) · May-23 (1% binding, 2% announced) · May-24 (2% binding)
- Bank credit 2022Q1–2026Q1: NL +16.6% vs euro area +7.9%; 2019–22: NL +4.3% vs +11.3%
TERMS:
- Event study: Tracks the difference between treated and control groups before and after an event.
- Placebo test: Rerun the analysis pretending an untreated country was treated, to see what chance alone produces.
NEXT: **HAND-OVER:** "So banks and borrowers were fine. What about the wider effects? Zheng."

## 18 · Monetary policy | Zheng | 0:55 | 18:15
SAY:
- Thank you, Diego. A natural worry is that two tightenings at once, higher policy rates and higher capital requirements, would choke credit. The chart shows that this did not happen. Dutch mortgage rates, in red, followed the ECB's deposit rate, in grey, and moved closely with mortgage rates in the control countries, in blue.
- The ECB argues that building buffers early lets monetary policy focus on its main goal, price stability. With one monetary policy for twenty countries, the countercyclical buffer is the **Dutch-specific lever**. It is also insurance in case a rate shock goes wrong.
NUMBERS:
- ECB hiking from Jul 2022 (first +50bp) to at least Sep 2023
TERMS:
- Macroprudential policy: Policy aimed at the stability of the financial system as a whole.
- Monetary policy: Interest-rate policy aimed at price stability (ECB, euro area-wide).
NEXT: "Through reciprocity, the 2% also reaches foreign lenders."

## 19 · Across borders | Zheng | 0:55 | 19:10
SAY:
- The buffer also reaches across borders. Under EU reciprocity, foreign banks that lend into the Netherlands must also hold the Dutch two percent on those loans. This limits leakage to foreign lenders, which is a known weakness of national capital rules, although lending can still move to non-banks.
- And the Netherlands is part of a European shift. The chart shows the rates and the dates from which they apply. Germany, France, Ireland, Belgium, Portugal and Spain have all raised their buffers since 2023. The Netherlands was early and set the highest rate, but it was not alone.
NUMBERS:
- Germany 0.75% (Feb 2023) · France 1.0% (Jan 2024) · Ireland 1.5% (Jun 2024) · NL 2.0% (May 2024) · Belgium 1.0% (Oct 2024) · Portugal 0.75% (Jan 2026) · Spain 1.0% (Oct 2026)
- Positive-neutral rates in 2023: Cyprus 0.5%, Estonia and Lithuania 1.0%, Ireland 1.5%, NL 2.0%
TERMS:
- Reciprocity: Foreign banks apply the host country's CCyB rate to exposures there (mandatory in the EU up to 2.5%).
- Leakage: Credit shifting to lenders not covered by the rule (foreign branches, non-banks).
NEXT: "The result for the Netherlands:"

## 20 · Resilience | Zheng | 1:05 | 20:05
SAY:
- The result is shown in this chart. In March 2020 the Netherlands had no releasable capital at all. Today it has **6.7 billion euros**, about half of the peak losses after the financial crisis, and enough to support up to 150 billion euros of lending.
- This buffer is cheap to hold and powerful to release. Research on European banks suggests that a one-point increase in normal times reduces lending by only about 0.1 percent, while a one-point release in bad times can raise lending by up to ten percent.
- And its role is growing. The floor on mortgage risk weights expires in November 2026, and DNB says that this underlines the importance of the two-percent buffer.
NUMBERS:
- €0 → €6.7bn releasable · ≈ half of €12bn peak losses · up to €150bn of lending
- Lang & Menno (2023): −0.1% lending per +1pp (normal times) vs up to +10% per 1pp release (bad times)
TERMS:
- State-dependent effect: The impact of a policy depends on the state of the economy (small in good times, large in bad times).
NEXT: "The price is reliance on discretion."

## 21 · Critiques | Zheng | 1:00 | 21:10
SAY:
- Of course there is a price, and we see five critiques.
- **Credibility:** without a rule, markets must trust DNB's judgement, so DNB has to explain every decision. **Calibration:** why two percent, when the ECB's estimates range from 1.1 to 1.8? **Untested:** the buffer has never been released, and in 2020 many banks did not use the buffers they were allowed to use. **Baseline:** compared with 2021 rather than 2019, it was an increase. **Profits:** the same profits that fund the buffer were also targeted by levies on excess profits.
- None of these overturns our verdict, but they define what DNB must get right next time.
NUMBERS:
- ECB loss-based range 1.1–1.8% vs NL 2% · +€3.3bn vs 2021 before the O-SII offset
TERMS:
- Rules vs discretion: The trade-off between predictable formulas and flexible judgement (Kydland & Prescott 1977).
- Excess-profit levy: A temporary tax on bank profits seen as windfalls from higher rates.
NEXT: "In short, the promise was kept."

## 22 · Conclusion | Zheng | 1:05 | 22:10
SAY:
- Let us conclude with the three questions of the assignment. The **environment** was a recovered economy hit by war, inflation and rate hikes, with cold credit, a cooling housing market and strong banks. The **criteria** were a two-percent normal level calibrated on past losses, as insurance against shocks nobody can forecast. The **implications**: the refill was cheap, largely a swap, with no sign of contraction, and it leaves 6.7 billion euros ready to release, at the price of more discretion.
- *(pause)* In March 2020 the Netherlands had nothing to release. **Next time, it will.** The best time to fill a buffer is when nobody thinks you need it, even in a storm. Thank you, and we look forward to your questions.
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

## 25 · Appendix A1: verdict rows 1–2 | both | backup | Q&A
SAY:
- (Only if asked about page 14.) The left panel shows the path: two steps of one point, a year apart, then held at two percent, exactly as normalisation predicts.
- The other three panels show the credit indicators. Between the two announcements the credit gap, the debt-service ratio and household debt all fell, so the buffer did not follow credit.
NUMBERS:
- CCyB announced: 1% (25 May 2022), 2% (31 May 2023); held at 2% since
- Gap −33pp (2021Q4) → −47pp (2022Q4); household debt 107% (2022Q1) → 100% (2023Q1) of GDP; debt-service ratio 14.6% (2022Q1)
TERMS:
- Debt-service ratio: Interest plus principal payments as a share of income.
NEXT: Return to page 14 or 15.

## 26 · Appendix A2: verdict rows 3–5 | both | backup | Q&A
SAY:
- (Only if asked about page 14.) On the left, house prices: in 2023 they were falling, yet DNB announced two percent. In 2024 and 2025 they grew about ten percent a year, yet DNB held at two percent.
- In the middle, the ECB deposit rate stood at 3.25 percent when the second step was announced.
- On the right, the systemic buffers of the three large banks were cut in 2020 and again in 2024, which is what normalisation predicts.
NUMBERS:
- House prices, nominal y/y (BIS): −4.0% (2023Q2); +10.8% (2024Q4 and 2025Q1); +5.1% (2026Q1)
- ECB deposit rate 3.25% on 31 May 2023
- Systemic buffers: ING 3 → 2.5 → 2.0%; Rabobank 3 → 2.0 → 1.75%; ABN AMRO 3 → 1.5 → 1.25% (until Mar 2020 / from Mar 2020 / from May 2024)
TERMS:
- O-SII buffer: Structural capital charge on systemically important banks; replaced the systemic risk buffer from 29 Dec 2020.
NEXT: Return to page 14 or 15.

