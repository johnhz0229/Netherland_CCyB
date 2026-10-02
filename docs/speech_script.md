# Speaker script: "Refilling the Buffer in a Storm"

**Format:** one A4 page per slide.
- **Top:** the slide.
- **Below:** **SAY** (the spoken text, in order), **NUMBERS** (figures to quote), **TERMS** (plain-language definitions) and **NEXT** (the transition line).

**Build:** `python code/make_speaker_script.py && cd slides && latexmk -pdf speaker_script.tex` → `Netherlands_CCyB_speaker_script.pdf`.

**Timing and speakers:** ≈ 24.5 minutes in total.
- Zheng Huang: pages 1–9 and 18–22.
- Diego Gutiérrez: pages 10–17.
- Pages 23–24 are backup for questions.

Page numbers below are the numbers printed on the slides (n/24). All figures come from `docs/02_findings.md` and the sources cited on each slide.

---

## 1 · Title | Zheng | 0:15 | 0:00
SAY:
- Good morning. We are Zheng Huang and Diego Gutiérrez, Master of Financial Technology.
- Our case for Micro- and Macroprudential Management is the Netherlands: how and why De Nederlandsche Bank, DNB, raised its countercyclical capital buffer from zero to two percent.
NUMBERS:
- CCyB 0% → 2% (fully binding 31 May 2024)
TERMS:
- DNB: De Nederlandsche Bank, the Dutch central bank and macroprudential authority.
NEXT: "In short, here is the whole story on one slide."

## 2 · One-pager | Zheng | 0:45 | 0:15
SAY:
- This slide is the whole talk; you can come back to it at any point.
- DNB raised the buffer twice, to two percent, while the Basel reference indicator, the credit-to-GDP gap, pointed to zero.
- The three boxes answer the three questions of the assignment: environment, criteria and risks, implications.
- Our verdict: **normalisation, not tightening**. DNB was refilling a buffer, not fighting a credit boom.
- The cost to banks was small, it was largely offset by cutting other buffers, and we see **no sign of a contraction in lending**.
NUMBERS:
- Announcements: May 2022 (1%) and May 2023 (2%); binding 25 May 2023 and 31 May 2024
- Credit-to-GDP gap at the decisions: −33pp and −47pp → Basel guide 0%
- Inflation 11.6% (2022) · CET1 17.7% (end-2021) · €6.7bn releasable
TERMS:
- CCyB: Countercyclical capital buffer. Extra bank capital (0–2.5% of risk-weighted assets) built in good times, released in bad times.
- Credit-to-GDP gap: How far credit/GDP is above its long-run trend; the Basel starting point for the CCyB.
- O-SII: "Other systemically important institution". The O-SII buffer is an extra capital charge on large banks.
NEXT: "It starts in March 2020."

## 3 · March 2020 | Zheng | 1:30 | 1:00
SAY:
- March 2020: COVID hits Europe. Within three weeks, a string of countries **release** their countercyclical buffers, telling banks to use that capital to keep lending.
- Sweden and Norway had been at 2.5 percent, the maximum normally used. Denmark, Ireland and Lithuania were at one percent. Germany and Belgium cancelled increases that had been announced but not yet applied.
- The Netherlands could not do this. Its buffer was at **zero**, so there was **nothing to release**.
- So DNB improvised. On 17 March 2020 it cut the systemic buffers of ING, Rabobank and ABN AMRO and postponed a planned floor on mortgage risk weights. Together that freed about eight billion euros.
- And it made a promise *(pause)*: once things were back to normal, it would rebuild this capital as a two-percent countercyclical buffer. The whole story turns on that promise.
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

## 4 · The releasable layer | Zheng | 1:00 | 2:30
SAY:
- Not all capital is usable in a crisis. Read the stack from the bottom.
- First come **requirements** that must always be met: the legal minimum and the bank-specific Pillar 2 requirement.
- On top sits the **combined buffer**: the conservation buffer, the systemic buffer and the CCyB.
- The red dashed line is the MDA trigger. A bank whose capital falls below the top of the combined buffer automatically faces limits on dividends and bonuses. So banks avoid dipping into buffers, even when allowed to; markets punish it.
- The CCyB is the only layer the authority can **switch off**. When it is released, the requirement itself falls, and there is no stigma.
- In COVID, ECB research found that banks close to the MDA trigger cut lending anyway. Only explicitly released capital really works.
NUMBERS:
- Pillar 1 minimum 4.5% CET1 · capital conservation buffer 2.5%
- CCyB 0–2.5% of RWA (higher possible) · increases bind after 12 months · releases are immediate
TERMS:
- RWA: Risk-weighted assets. Assets weighted by riskiness (a mortgage counts less than a corporate loan).
- CET1: Common Equity Tier 1. The highest-quality capital (shares, retained earnings), as % of RWA.
- MDA: Maximum distributable amount. The cap on payouts that applies once capital falls below the combined buffer requirement.
- Pillar 2 requirement / guidance: The supervisor's bank-specific add-on (binding) / extra expectation (non-binding).
NEXT: "Two years later DNB refilled exactly that layer, at a strange moment."

## 5 · The question | Zheng | 1:00 | 3:30
SAY:
- In 2022 DNB keeps its promise, but look at the timing on the left: war in Ukraine, record energy prices, 11.6 percent inflation, ECB rate hikes, house prices about to turn. And the Basel indicator says zero.
- Raising capital requirements in a downturn is *procyclical*: it amplifies the cycle. That is exactly the mistake the CCyB was invented to prevent.
- So our question is: **was this the wrong moment?**
- We answer in three acts, the three questions of the assignment. The boxes show what each act covers, without overlap: the setting, the decision, the consequences.
NUMBERS:
- HICP inflation 11.6% (2022) · ECB first hike 21 Jul 2022 (+50bp)
- Credit-to-GDP gap −33pp (data to 2021Q4) and −47pp (data to 2022Q4)
TERMS:
- Procyclical: Policy that reinforces the cycle (tighter in bad times, looser in good times).
- Basel buffer guide: Gap below 2pp → 0% buffer; above 10pp → 2.5%; linear in between.
NEXT: "Act 1, the setting. The refill followed a path promised in 2020."

## 6 · Timeline | Zheng | 1:00 | 4:30
SAY:
- The path was set in March 2020 with the promise.
- In December 2020 the systemic risk buffer was folded into O-SII buffers under new EU rules, and in January 2022 the mortgage risk-weight floor finally came into force.
- In February 2022 DNB published its new CCyB framework. In May 2022 it announced one percent, just before the ECB began to hike in July. In May 2023 it announced two percent, together with lower O-SII buffers.
- Both changes became binding on the same day, 31 May 2024, and DNB has held the buffer at two percent every quarter since.
- Looking ahead: the mortgage floor expires at the end of November 2026.
NUMBERS:
- 17 Mar 2020 · 29 Dec 2020 · 1 Jan 2022 · Feb 2022 · 25 May 2022 · 31 May 2023 · 31 May 2024 · 30 Nov 2026
- ECB hikes: first on 21 Jul 2022; still hiking on 14 Sep 2023
TERMS:
- Announcement vs binding date: Banks get 12 months between a CCyB increase being announced and having to meet it.
- CRD V: The 2019 revision of the EU Capital Requirements Directive; it made the O-SII and systemic risk buffers additive, prompting DNB's conversion.
NEXT: "By then the economy had fully recovered, but the outlook was darkening."

## 7 · Macro | Zheng | 1:05 | 5:30
SAY:
- By the third quarter of 2021, Dutch GDP was back above its pre-COVID level; by the end of 2021 it was almost three percent larger than at the end of 2019. That recovery is the condition DNB's framework requires before building the buffer.
- Then the storm. DNB's spring 2022 Financial Stability Report: "the economic outlook has worsened due to the war in Ukraine and high inflation."
- Energy prices hit records, inflation reached 11.6 percent, and on 21 July 2022 the ECB raised rates by fifty basis points, its first hike.
- DNB also warned that higher funding costs would weigh on the debt sustainability of governments, firms and households.
- So the macro picture argued both ways: build now while the economy can take it, or wait because it is weakening.
NUMBERS:
- GDP above pre-COVID level: 2021Q3 (+1.9% q/q) · end-2021 ≈ +3% vs end-2019
- HICP 11.6% in 2022 (national CPI 10.0%)
- ECB +50bp on 21 Jul 2022
TERMS:
- HICP: Harmonised Index of Consumer Prices, the euro-area-comparable inflation measure.
- Basis point (bp): 0.01 percentage point; 50bp = 0.5pp.
NEXT: "In the financial system, credit was cold and only housing was hot."

## 8 · Credit and housing | Zheng | 1:15 | 6:35
SAY:
- Left panel, **housing was hot**. In early 2022 nominal house prices rose 19 percent year on year, and real prices were 16 percent above their 2007 peak. DNB itself called the housing market "overheated".
- But watch what happens next: as mortgage rates rose, real prices fell by about nine percent within a year.
- Middle panel, **credit was cold**. Household debt is high by international standards, about 107 percent of GDP versus 58 percent in the euro area, but it was falling.
- Right panel: the household debt-service ratio, the share of income spent on interest and repayments, was at its lowest since 2005.
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

## 9 · Banks | Zheng | 1:05 | 7:50
SAY:
- The banks were in good shape. The core capital ratio was 17.7 percent at the end of 2021, above the EU average, and 16.3 percent a year later.
- In DNB's 2023 stress test the four major banks would lose 3.8 points of capital and still end at 11.5 percent, above the 8 percent minimum.
- And rising rates were lifting profits: net interest income grew 6.7 percent in 2022. DNB wrote that higher rates "may ultimately have a positive impact on the profitability of financial institutions". Keep that sentence in mind; it is our twist later.
- The bottom row is Act 1 in one line: against raising now, war, inflation, rate hikes and a turning housing market. For raising now, a recovered economy, cold credit and strong, increasingly profitable banks.
NUMBERS:
- CET1 17.7% (end-2021; EU 15.7% in 2021Q3) → 16.3% (end-2022, in line with EU)
- Stress test (FSR 2023): −3.8pp → 11.5% at end-2025 (min. 8%)
- Net interest income +6.7% in 2022; 67.7% of bank income
TERMS:
- Stress test: A simulation of a severe recession to check whether capital stays above the minimum.
- Net interest income: Interest earned on loans minus interest paid on deposits and funding.
NEXT: **HAND-OVER:** "That was the setting. So why did DNB ignore its own rulebook? Diego."

## 10 · Why not the Basel rule? | Diego | 1:15 | 8:55
SAY:
- Thank you. So why ignore the rulebook? Because on Dutch data it has a poor record.
- The red line is the credit-to-GDP gap, credit relative to its long-run trend. The trend is estimated with a statistical smoother, the Hodrick-Prescott filter. Our own calculation matches the official BIS series almost exactly.
- On Dutch data, the rule failed three times. It **missed** the financial crisis: minus 13 points in 2007. It raised a **false alarm** in 2012, during a house-price bust, because falling GDP inflated the ratio. And it gets **revised**: 2016 read slightly negative in real time but plus 27 with today's data.
- Why so bad? Dutch credit rose from under 50 percent of GDP in the 1960s to around 350 percent at its 2015 peak. The filter treats that structural deepening as trend, so once the ratio falls the gap turns deeply negative.
- At the two decisions it read minus 33 and minus 47 points, so the rule said zero. DNB had good reason to use a different compass.
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

## 11 · DNB's framework | Diego | 1:15 | 10:10
SAY:
- That compass is DNB's 2022 framework, with four phases.
  - After a crisis, the buffer is released.
  - In normal times it should be at two percent, built up one point a year.
  - Only when risks are clearly elevated does it go above two percent.
  - In a crisis it is released.
- This is called a *positive neutral* buffer: already filled when risks are neither high nor low.
- Two percent is calibrated on history: Dutch banks' peak accumulated losses in past crises were about 12 billion euros. Two percent equals about six billion of releasable capital, and releasing it could support up to 150 billion of lending.
- DNB decides by *guided discretion*: a dashboard of indicators informs the decision but does not dictate it. It also chose two percent "taking into account the buffer reduction in March 2020".
- The Netherlands is not alone: seventeen jurisdictions run such a framework; Sweden, the UK and Poland also target two percent.
NUMBERS:
- Peak accumulated losses €12bn (2007–2016) → 2% ≈ €6bn → up to €150bn of lending
- Build-up: 1pp per year → 2% after two years
- 17 jurisdictions with a positive neutral CCyB (BCBS 2024); ECB loss-based range 1.1–1.8%
TERMS:
- Positive neutral CCyB: A CCyB kept above zero in a "standard" risk environment.
- Peak accumulated losses: The largest cumulative loss a bank suffered over a crisis period.
- Guided discretion: Decisions informed by a published set of indicators, with judgement, not a formula.
NEXT: "And its stated reasons were never credit growth."

## 12 · DNB's reasons | Diego | 1:00 | 11:25
SAY:
- **In 2022,** DNB wrote: "When the systemic risk buffers were lowered in March 2020, we also announced our intention to restore the buffers by raising the CCyB." It cited the strong recovery, described risks as "normal to elevated", and acknowledged the uncertainty of the war.
- **In 2023,** it said explicitly that the credit gap shows "no signs of excessive credit growth". The reasons it cited: investors' rising risk appetite, falling real-estate prices, debt sustainability of firms and governments, and banks made more robust by higher rates.
- In neither decision was credit growth the reason. Both rest on a normal-to-elevated risk picture, strong banks and the promise.
NUMBERS:
- 1% step: about €3.3bn of extra CET1 (announced 25/27 May 2022)
- 2% step: about €3.4bn (announced 31 May 2023)
TERMS:
- Cyclical systemic risk: Risk that builds up over the financial cycle (credit, asset prices, risk-taking) and can materialise system-wide.
NEXT: "So what was the buffer meant for?"

## 13 · Risks and tools | Diego | 1:15 | 12:25
SAY:
- DNB's reports name the financial-stability risks, and each was matched to a tool.
- **Shocks nobody can forecast** go to the CCyB, because it can be released whatever the source: the war, an energy shock, a sudden tightening of financial conditions, debt-sustainability problems, or bank turmoil abroad such as SVB and Credit Suisse in 2023.
- **The known hot spot, housing,** went to other tools: limits on loan-to-value and loan-to-income, tax reform, and the mortgage risk-weight floor.
- **The size of the big banks** goes to the O-SII buffer. The sector shrank from about 400 to 280 percent of GDP, which is why that buffer was cut.
- This is the Tinbergen principle: one instrument per target. DNB itself said more releasable capital is valuable "given the sensitivity of the Dutch economy to external events".
NUMBERS:
- Banking sector: ≈ 400% of GDP (when O-SII buffers were phased in) → 280% (end-2022)
- Risk-weight floor in force Jan 2022 – Nov 2026
TERMS:
- LTV / LTI: Loan-to-value / loan-to-income. Caps on mortgage size relative to house value or income.
- Tinbergen principle: Reach each policy target with its own instrument.
- Borrower-based measures: Rules on borrowers (LTV, LTI) rather than on bank capital.
NEXT: "Now we can test the evidence against both readings."

## 14 · The verdict | Diego | 1:30 | 13:40
SAY:
- Was DNB fighting overheating or normalising? Each makes different predictions. Row by row:
  - **Indicators.** Overheating says the buffer rises with them. In fact they all fell while the buffer went up.
  - **Path.** Normalisation says one point a year, stop at two. That is exactly what happened.
  - **2023.** House prices were falling and rates jumping. An overheating fighter would pause; DNB raised anyway.
  - **2024–26.** House prices rose again, about ten percent a year by early 2026. An overheating fighter would go above two percent; DNB held at two.
  - **Other buffers.** Normalising means cutting structural buffers to compensate. DNB did, twice.
- *(pause)* Five predictions, five matches.
- The strongest evidence against us is house prices at plus 19 percent in 2022. But DNB used other tools for housing, and when house prices fell, it raised the buffer anyway.
- That last row is the key to the whole story.
NUMBERS:
- Gap, debt-service ratio and household debt ratio all falling in 2022–23
- House prices +10% y/y (DNB, Mar 2026) · CCyB held at 2% since May 2024
TERMS:
- Phase 3 ("increased risk"): The framework phase in which the CCyB goes above 2%.
NEXT: "And that last row tells us the refill was a swap, not a squeeze."

## 15 · A swap, not a squeeze | Diego | 1:15 | 15:10
SAY:
- This waterfall is our own approximate calculation.
  - In 2020 the systemic-buffer cut released about six billion euros of required capital.
  - The CCyB then added 3.3 billion in 2023 and 3.4 billion in 2024.
  - In 2024 the O-SII cut released another 2.7 billion.
- Net, relative to before COVID: roughly unchanged, if anything slightly lower.
- DNB said the same: the 2020 plan would be "more or less capital-neutral", and in 2023 Governor Knot spoke of "a limited increase in the net capital requirements".
- Two caveats. The bases differ: the cuts apply to big banks' worldwide assets, the CCyB to all banks' Dutch exposures. And measured from 2021, not 2019, there was a modest increase.
- So capital was **moved**, from buffers that cannot be released into one that can. The UK did something similar.
NUMBERS:
- −6.0 (2020: ING 1.7, Rabo 2.4, ABN 1.9) · +3.3 (May-23) · +3.4 (May-24) · −2.7 (May-24 O-SII) → net ≈ −2.0 €bn vs pre-COVID
- Valued at end-2022 total RWA; BNG excluded
TERMS:
- Structural buffer: A capital charge for permanent features (size, interconnectedness), kept through the cycle.
- UK approach: The UK offset its 2% neutral CCyB by lowering Pillar 2A and resolution requirements.
NEXT: "So, was it the wrong moment?"

## 16 · The twist | Diego | 1:15 | 16:25
SAY:
- Here is the twist: the storm made it the **cheapest** moment.
- Headroom is the capital a bank holds above its requirement. The left panel shows it by bank: ING and Rabobank each had over ten billion euros, ABN AMRO about seven.
- In total the four banks had about 36 billion at the end of 2022. The full two-percent buffer is 6.7 billion, at most about a fifth, and that is an upper bound.
- Why so cheap? Rising rates lifted net interest income, so banks could build the buffer from retained earnings instead of cutting loans. Headroom shrank between 2021 and 2022 because risk-weighted assets grew and banks paid out capital, not because of the buffer.
- The ECB agrees: a gradual build-up with profitable banks "limits these economic costs", and activating buffers during the 2022–23 tightening "can mitigate implementation costs".
- Not the wrong moment. Arguably the right one.
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

## 17 · Borrowers | Diego | 1:15 | 17:40
SAY:
- We ran an event study: Dutch lending rates and loan growth compared with five euro-area countries that never changed their buffer (Austria, Finland, Italy, Malta, Luxembourg), around each policy date.
- How to read it: the red line is the Netherlands minus those countries; zero means no difference. The grey band shows how big differences get by pure chance. We pretend each control country raised its buffer and plot those "fake" effects.
- Left: Dutch mortgage rates stay inside the band at all three dates. Right: household credit actually grew faster.
- Honest detail: before 2022 the Netherlands had lagged, so part of that is catch-up.
- Our claim is modest. With one treated country this is "no sign of contraction", not a causal estimate. DNB's own verdict in September 2026: "no signs of constraints in bank credit supply".
NUMBERS:
- Dates: May-22 (1% announced) · May-23 (1% binding, 2% announced) · May-24 (2% binding)
- Bank credit 2022Q1–2026Q1: NL +16.6% vs euro area +7.9%; 2019–22: NL +4.3% vs +11.3%
TERMS:
- Event study: Tracks the difference between treated and control groups before and after an event.
- Placebo test: Rerun the analysis pretending an untreated country was treated, to see what chance alone produces.
NEXT: **HAND-OVER:** "So banks and borrowers were fine. What about the wider effects? Zheng."

## 18 · Monetary policy | Zheng | 1:05 | 18:55
SAY:
- Thank you. First, the buffer did not double the ECB's squeeze.
- The worry was a **double squeeze**, the ECB raising rates while DNB raised capital requirements.
- But Dutch lending rates did not diverge from their peers, and bank profits rose with rates.
- The ECB argues that early buffers "help monetary policy focus on its primary objective of price stability". Macroprudential policy looks after the financial system so that monetary policy can fight inflation.
- For a euro-area country this matters even more: one monetary policy for twenty countries, but national macroprudential policy. The CCyB is the Dutch-specific lever, and the insurance if a rate shock goes wrong.
NUMBERS:
- ECB hiking from Jul 2022 (first +50bp) to at least Sep 2023
TERMS:
- Macroprudential policy: Policy aimed at the stability of the financial system as a whole.
- Monetary policy: Interest-rate policy aimed at price stability (ECB, euro area-wide).
NEXT: "Through reciprocity, the 2% also reaches foreign lenders."

## 19 · Across borders | Zheng | 1:00 | 20:00
SAY:
- Under EU reciprocity, any foreign bank lending into the Netherlands must also hold the Dutch two percent on those loans. That limits leakage, lending simply moving to foreign banks, a known weakness of national capital rules. Lending can still leak to non-banks.
- And the Netherlands is part of a wider shift, shown in the table: Germany, France, Ireland and Belgium raised their buffers in 2023–24; Portugal and Spain follow in 2026.
- In 2023, five banking-union countries had positive-neutral frameworks, and the Netherlands had the highest rate.
NUMBERS:
- Germany 0.75% (Feb 2023) · France 1.0% (Jan 2024) · Ireland 1.5% (Jun 2024) · NL 2.0% (May 2024) · Belgium 1.0% (Oct 2024) · Portugal 0.75% (Jan 2026) · Spain 1.0% (Oct 2026)
- Positive-neutral rates in 2023: Cyprus 0.5%, Estonia and Lithuania 1.0%, Ireland 1.5%, NL 2.0%
TERMS:
- Reciprocity: Foreign banks apply the host country's CCyB rate to exposures there (mandatory in the EU up to 2.5%).
- Leakage: Credit shifting to lenders not covered by the rule (foreign branches, non-banks).
NEXT: "The result for the Netherlands:"

## 20 · Resilience | Zheng | 1:00 | 21:00
SAY:
- In 2020 the Netherlands had no capital that was releasable by design. Today it has about 6.7 billion euros, roughly half of the peak losses after the financial crisis, enough to support up to 150 billion of lending.
- ECB research shows why that is a good deal: raising requirements in normal times costs very little lending, about 0.1 percent per point, while a release in bad times can boost lending by up to ten percent.
- And its role is growing. The mortgage risk-weight floor expires at the end of November 2026, and DNB says this "underpins the importance" of the two-percent buffer.
NUMBERS:
- €0 → €6.7bn releasable · ≈ half of €12bn peak losses · up to €150bn of lending
- Lang & Menno (2023): −0.1% lending per +1pp (normal times) vs up to +10% per 1pp release (bad times)
TERMS:
- State-dependent effect: The impact of a policy depends on the state of the economy (small in good times, large in bad times).
NEXT: "The price is reliance on discretion."

## 21 · Critiques | Zheng | 1:00 | 22:00
SAY:
- **Credibility.** Without a mechanical rule, markets must trust DNB's judgement. That is the classic rules-versus-discretion trade-off: a rule is predictable but can be wrong, as we saw; discretion must be explained every quarter.
- **Calibration.** Why two percent? ECB estimates suggest 1.1 to 1.8.
- **Untested.** We do not yet know whether banks will lend released capital or hoard it.
- **Baseline.** Measured against 2021 rather than 2019, it *was* an increase of 3.3 billion before the O-SII offset.
- **Same profits, two claims.** The ECB lists the Netherlands among countries that levied excess-profit taxes on banks in 2022–23, partly the same earnings that fund the buffer.
NUMBERS:
- ECB loss-based range 1.1–1.8% vs NL 2% · +€3.3bn vs 2021 before the O-SII offset
TERMS:
- Rules vs discretion: The trade-off between predictable formulas and flexible judgement (Kydland & Prescott 1977).
- Excess-profit levy: A temporary tax on bank profits seen as windfalls from higher rates.
NEXT: "In short, the promise was kept."

## 22 · Conclusion | Zheng | 1:30 | 23:00
SAY:
- **Environment:** a recovered economy hit by war, inflation and rate hikes; credit cold; housing hot, then cooling; strong, profitable banks.
- **Criteria and risks:** a two-percent normal-times level calibrated on past losses, insuring against shocks no one can forecast. Housing went to other tools; structural buffers were cut in return.
- **Implications:** cheap, largely a swap, no sign of contraction, complementary to monetary policy, reciprocated abroad, and 6.7 billion euros now releasable. The price is reliance on discretion.
- The one idea to take away: this was less about *how much* capital banks hold and more about *which kind*.
- *(pause)* In March 2020, the Netherlands had nothing to release. **Next time, it will.** The best time to fill a buffer is when nobody thinks you need it, even in a storm. Thank you; we look forward to your questions.
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
