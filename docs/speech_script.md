# Speaker script: "Refilling the Buffer in a Storm"

**Format:** one A4 page per slide.
- **Top:** the slide.
- **STORY:** what to say out loud, in order.
- **LIKELY CHALLENGES:** questions the professor may ask on this slide, with short answers: definitions of the basic concepts and the logic behind each claim.

**Build:** `python code/make_speaker_script.py && cd slides && latexmk -pdf speaker_script.tex` → `Netherlands_CCyB_speaker_script.pdf`.

**Timing:** ≈ 23 minutes of speaking at about 120 words per minute (pages 1–22). Pages 23–26 are backup for questions. Q&A is separate.

All figures come from `docs/02_findings.md` and the sources cited on each slide. Longer model answers: `docs/qa_prep.md`.

---

## 1 · Title | 0:30
STORY:
- Good morning. Our case is the Netherlands.
- In 2022 and 2023 the Dutch central bank, De Nederlandsche Bank or DNB, raised its countercyclical capital buffer from zero to two percent. We want to explain why it did that, and whether it was a good idea.
LIKELY CHALLENGES:
- Q: What is the CCyB, in one sentence?
  - A capital buffer of 0–2.5% of risk-weighted assets on domestic exposures that is built up in good times and released in bad times, so banks can absorb losses and keep lending.
- Q: Who decides it in the Netherlands?
  - De Nederlandsche Bank (DNB), the Dutch central bank and designated macroprudential authority. It reviews the rate every quarter.
- Q: What exactly changed?
  - 0% → 1% (announced May 2022, binding 25 May 2023) → 2% (announced 31 May 2023, binding 31 May 2024). It has been held at 2% since.

## 2 · One-pager | 1:00
STORY:
- Here is the whole story on one slide. DNB raised the buffer in two steps, to one percent and then to two percent. Yet at both decisions the indicator at the centre of the Basel rules, the credit-to-GDP gap, was deeply negative, so the rulebook said the buffer should be zero.
- The three columns follow the three questions of the assignment: the environment, the criteria and risks, and the implications.
- Our verdict is that this was **normalisation, not tightening**. DNB was refilling an empty buffer, not fighting a credit boom. The price is that the policy relies on DNB's judgement rather than on a rule.
LIKELY CHALLENGES:
- Q: Define the credit-to-GDP gap.
  - Credit to the private non-financial sector as a share of GDP, minus its long-run trend from a one-sided HP filter (λ = 400,000). It is the Basel starting point for setting the CCyB.
- Q: What is the Basel buffer guide?
  - A mapping from the gap to a buffer rate: below 2pp → 0%; above 10pp → 2.5%; linear in between. With gaps of −33 and −47pp it gives 0%.
- Q: What do you mean by 'normalisation, not tightening'?
  - Normalisation means returning the buffer to its planned normal-times level regardless of the cycle. Tightening means raising it because risk is building up. We test which one fits the evidence on page 14.
- Q: Isn't raising capital always a tightening?
  - Not if other requirements are cut at the same time. The 2020 and 2024 cuts in structural buffers roughly offset the CCyB relative to pre-COVID (page 15).

## 3 · March 2020 | 1:15
STORY:
- The story starts in March 2020. When COVID hit, our neighbours reacted within three weeks: eight European countries cut their countercyclical buffers, as the chart shows. Sweden and Norway had been at two and a half percent; Denmark, Ireland and Lithuania at one percent. Buffers built in good times were used exactly as intended.
- The Netherlands was at **zero**, the red dot at the bottom. There was nothing to release.
- So DNB improvised. It cut the systemic buffers of ING, Rabobank and ABN AMRO and postponed a planned floor on mortgage risk weights. This freed about eight billion euros of capital, enough to support up to 200 billion euros of lending. But those buffers were never designed to be released.
- And DNB made a promise *(pause)*: once things were back to normal, it would rebuild this capital as a two-percent countercyclical buffer.
LIKELY CHALLENGES:
- Q: What does 'release' mean legally?
  - The authority lowers the CCyB rate with immediate effect. The requirement itself falls, so banks can use that capital to absorb losses or lend without breaching any requirement.
- Q: If the Dutch CCyB was 0%, what did DNB release in 2020?
  - It cut the systemic risk buffers of ING, Rabobank and ABN AMRO (3% → 2.5/2/1.5%) and postponed the mortgage risk-weight floor. Together about €8bn, supporting up to €200bn of lending.
- Q: Why was that a 'workaround'?
  - Systemic buffers are structural charges for the size and importance of banks. They are not meant to move with the cycle, so cutting them blurred their purpose. That is why DNB promised to restore the capital as a releasable 2% CCyB.
- Q: Which countries released, and by how much?
  - Norway 2.5→1%, Sweden 2.5→0%, Iceland 2→0%, Czech Republic 1.75→1%, Denmark, Lithuania and Ireland 1→0%, France 0.25→0%. Belgium and Germany cancelled planned increases (ESRB table).

## 4 · The releasable layer | 1:10
STORY:
- Why did an empty buffer matter? Because not all bank capital can be used in a crisis.
- Read the stack from the bottom: first the minimum requirements, then the buffers on top. The red dashed line is the MDA trigger. If a bank falls below it, its dividends and bonuses are restricted automatically, and markets read that as weakness. So in COVID, banks close to this line cut lending rather than use buffers they were formally allowed to use.
- The countercyclical buffer is different. The authority can switch it off, so the requirement itself falls, with no penalty and no stigma. It is the only truly **releasable** layer. And while an increase binds only after twelve months, a release is immediate, so the buffer must be filled before a crisis.
LIKELY CHALLENGES:
- Q: Define CET1 and RWA.
  - CET1 (Common Equity Tier 1) is the highest-quality capital: shares and retained earnings. RWA (risk-weighted assets) weight each exposure by its riskiness, so capital ratios are CET1 / RWA.
- Q: Walk through the capital stack.
  - Pillar 1 minimum 4.5% CET1, then the bank-specific Pillar 2 requirement, then the combined buffer requirement: capital conservation buffer 2.5%, O-SII/systemic buffer and CCyB. Pillar 2 guidance sits on top and is not binding.
- Q: What is the MDA trigger?
  - The maximum distributable amount. If CET1 falls below the top of the combined buffer requirement, dividends, buybacks and bonuses are automatically restricted.
- Q: Buffers are 'usable' anyway; why do banks not use them?
  - Falling below the MDA trigger means payout limits, market stigma and rating pressure. COVID evidence shows banks close to the trigger cut lending instead (Couaillier et al., 2022). A released CCyB avoids this because the requirement itself falls.
- Q: Why is the 12-month lag important?
  - An increase binds only 12 months after the announcement, but a release is immediate. So the buffer must be filled before a crisis; it cannot be built once the shock arrives.

## 5 · The question | 1:00
STORY:
- Two years later, in 2022, DNB began to refill the buffer, and the timing looks strange. On the left is the storm: war, record energy prices, 11.6 percent inflation, the first ECB rate hikes and a housing market about to turn. And the Basel indicator said zero. On the right is the decision: one percent, then two percent.
- Raising capital requirements in a downturn can amplify the cycle. That is exactly the procyclical mistake the buffer was invented to avoid.
- So our question is: **was this the wrong moment?** Was DNB tightening into a slowdown, fighting a hidden boom, or doing something else? We answer in three acts, one for each question of the assignment.
LIKELY CHALLENGES:
- Q: What is procyclicality?
  - Policy or behaviour that reinforces the cycle: tighter in bad times, looser in good times. Raising capital in a downturn can force banks to cut lending exactly when the economy needs it.
- Q: Why was this moment suspicious?
  - War, 11.6% inflation (2022), ECB hikes from July 2022 and a turning housing market, while the Basel indicator said 0%. On the surface it looks like the procyclical mistake the CCyB was designed to avoid.
- Q: How do the three acts map to the assignment?
  - Act 1 = economic and financial environment; Act 2 = criteria and financial-stability risks; Act 3 = wide-ranging implications.

## 6 · Timeline | 1:00
STORY:
- Act one is the setting, and it starts with the timeline. In March 2020 DNB cut the systemic buffers and made its promise. In February 2022 it published a framework with two percent as the normal level. In May 2022 it announced one percent, two months before the ECB's first hike. In May 2023 it announced two percent, together with lower buffers for the largest banks, and both became binding in May 2024.
- Since then DNB has held two percent at every quarterly review. So the path was two equal steps, a year apart, and then a stop. Keep that pattern in mind for our verdict.
LIKELY CHALLENGES:
- Q: Announcement date vs binding date?
  - Banks get 12 months between an increase being announced and having to meet it. So 1% was announced in May 2022 and binding in May 2023; 2% announced in May 2023 and binding in May 2024.
- Q: Was the increase a response to ECB tightening?
  - No. The 1% was announced on 25 May 2022, two months before the ECB's first hike on 21 July 2022, and the path had been promised in 2020.
- Q: Why did the systemic risk buffer become an O-SII buffer in December 2020?
  - CRD V made the O-SII and systemic risk buffers additive, so DNB converted the large banks' systemic risk buffers into O-SII buffers from 29 December 2020.

## 7 · Macro | 0:55
STORY:
- What did the economy look like? The left panel shows that real GDP was back above its pre-COVID level during 2021, which is the condition DNB's framework sets before rebuilding the buffer.
- Then the storm arrived. Inflation, in the middle, peaked at 17 percent in September 2022, and on the right the ECB moved its deposit rate from minus half a percent to four percent in fourteen months. DNB warned that higher funding costs could strain the debt of governments, firms and households.
- So the macro picture argued **both ways**: build while the economy can take it, or wait because it is weakening.
LIKELY CHALLENGES:
- Q: Why does the recovery matter for the decision?
  - DNB's framework only builds the buffer once the economy has recovered from a crisis (phase 1 → phase 2). GDP was back above its pre-COVID level during 2021.
- Q: Which inflation measure do you use?
  - HICP, the harmonised index used across the euro area: 11.6% average in 2022 and a peak of 17.1% in September 2022. The national CPI was 10.0% in 2022.
- Q: Why GDP 'in 2021' rather than a quarter?
  - In current data GDP is back above 2019Q4 in 2021Q2; the first CBS estimate dated it to 2021Q3. Data revisions explain the difference, so we say 2021.
- Q: Define a basis point.
  - 0.01 percentage point. The ECB's first hike was +50bp; the deposit rate went from −0.5% to 4% in fourteen months.

## 8 · Credit and housing | 1:00
STORY:
- What about the financial system? On the left you see housing, and housing was hot. Nominal house prices rose 19 percent in a single year, real prices were well above their 2007 peak, and DNB itself called the market overheated. But as mortgage rates rose, real prices fell by about nine percent.
- In the middle is household debt. It is high, at 107 percent of GDP against 58 percent in the euro area, but it was **falling**. On the right is the share of income that households spend on interest and repayments. It was the lowest since 2005.
- So if there was a boom, it was in house prices, not in credit.
LIKELY CHALLENGES:
- Q: Define the debt-service ratio.
  - Interest plus principal payments as a share of household income. At 14.6% in 2022Q1 it was the lowest since 2005.
- Q: Real vs nominal house prices?
  - Real prices are nominal prices deflated by consumer prices. Nominal prices rose 19% y/y in 2022Q1, but real prices fell about 9% between 2022Q2 and 2023Q2.
- Q: Household debt is 107% of GDP. Isn't that a risk in itself?
  - Yes, it is a structural vulnerability, which is why the buffer exists. But it was falling, so it is not a sign of a cyclical credit boom.
- Q: Didn't debt/GDP fall only because inflation raised nominal GDP?
  - Partly. Debt/GDP fell from 110% (2019Q4) to 100% (2023Q1) while the debt stock rose 12%, because nominal GDP grew about 22%. That is a denominator effect, and another reason not to read ratios mechanically.

## 9 · Banks | 1:00
STORY:
- Finally, the banks. Dutch banks entered the storm with a core capital ratio of 17.7 percent, two points above the EU average. In DNB's 2023 stress test, the four largest banks fell by 3.8 points in a severe recession but stayed at 11.5 percent, well above the minimum.
- Rising rates also **lifted their profits**: net interest income grew 6.7 percent in 2022. Please remember this, because it will come back in act three.
- So act one in one sentence: war, inflation, rate hikes and a turning housing market argued against raising the buffer, while a recovered economy, cold credit and strong banks argued for it.
LIKELY CHALLENGES:
- Q: What does a stress test show?
  - A simulation of a severe recession to check whether capital stays above the minimum. In DNB's 2023 test the four largest banks fell by 3.8pp, from 15.2% to 11.5%, still above the 8% minimum used.
- Q: Define net interest income.
  - Interest earned on loans minus interest paid on deposits and funding. It rose 6.7% in 2022 and makes up 67.7% of Dutch banks' income.
- Q: Why does profitability matter for the CCyB?
  - Banks can meet a higher requirement from retained earnings instead of cutting assets. Higher rates raised profits, which made the build-up cheaper (page 16).

## 10 · Why not the Basel rule? | 1:30
STORY:
- Act two is the decision, and the first question is: why did DNB ignore the rulebook? Because on Dutch data the rulebook has a poor record.
- The red line is the credit-to-GDP gap: how far credit relative to GDP is above its long-run trend. Under the Basel guide the buffer starts when the gap exceeds two points. We rebuilt the gap ourselves, and it matches the official BIS series almost exactly.
- Look at its record. It **missed** the financial crisis, reading minus 13 on the eve of 2008. It raised a **false alarm** in 2012, in the middle of a bust. And it gets **revised**: 2016 read slightly negative at the time and plus 27 with today's data. The reason is that Dutch credit grew from about 50 to 350 percent of GDP, and the filter mistakes that structural rise for a trend.
- At the two decisions the gap read minus 33 and minus 47. Taken literally, the rule said zero.
LIKELY CHALLENGES:
- Q: How does the HP filter work, and why λ = 400,000?
  - It finds a smooth trend that balances fit against smoothness. λ = 1,600 is standard for business cycles; credit cycles are about four times longer, and λ scales with the fourth power of that ratio: 1,600 × 4⁴ ≈ 400,000.
- Q: One-sided vs two-sided filter?
  - One-sided uses only data up to each date, which is what policymakers see; it is the official BIS/Basel gap. Two-sided also uses later data, so it is hindsight. 2016Q1: −0.6pp one-sided vs +26.9pp two-sided.
- Q: Type I vs type II error?
  - A missed crisis (no signal before a crisis, e.g. −13pp before 2008) vs a false alarm (signal without a crisis, e.g. +17pp in 2012).
- Q: Why does the gap fail especially in the Netherlands?
  - Credit/GDP rose from about 47% (1961) to 352% (2015) for structural reasons such as a large, tax-favoured mortgage market. The filter treats this as trend and then produces large negative gaps when the ratio falls.
- Q: Then why does Basel still use it?
  - Across many countries it is one of the better early-warning indicators. Basel treats it as a starting point, not a mechanical trigger.

## 11 · DNB's framework | 1:15
STORY:
- So DNB used its own compass. Its 2022 framework has four phases: release after a crisis, **two percent in normal times**, more than two percent when risks are clearly elevated, and release again in a crisis. This is a positive neutral buffer: it is already filled when risks are neither high nor low.
- The two percent comes from history, not from credit growth. At the peak, past crises cost Dutch banks about 12 billion euros. Two percent is about six billion euros of releasable capital, roughly half of those losses, and enough to support up to 150 billion euros of lending. The ECB's own estimates range from 1.1 to 1.8 percent, so two percent is at the top of the range, but not outside it.
- Seventeen jurisdictions now work this way, and Sweden, the UK and Poland also target two percent.
LIKELY CHALLENGES:
- Q: Define a positive neutral CCyB.
  - A CCyB kept above zero when risks are neither high nor low, so there is always something to release, whatever the source of the shock. BCBS (2024) lists 17 jurisdictions using one.
- Q: What model did DNB use for 2%?
  - No econometric model. It sized the buffer on history: peak accumulated losses of Dutch banks in 2007–16 were about €12bn; 2% ≈ €6bn of releasable capital, about half of those losses, supporting up to €150bn of lending.
- Q: Define peak accumulated losses.
  - The largest cumulative loss over a crisis period, from the start of losses to their worst point.
- Q: What is guided discretion?
  - A published framework (phases, neutral rate, indicator dashboard) plus judgement. DNB: there is 'no mechanical link between the indicator values and the level of the CCyB'.
- Q: Is 2% too high?
  - The ECB's loss-based estimates give 1.1–1.8% for the euro area, so 2% is at the top. DNB also took the 2020 buffer cut into account. We list this as a critique on page 21.

## 12 · DNB's reasons | 1:00
STORY:
- What reasons did DNB actually give? In May 2022 it wrote that it was **restoring the buffers** it had lowered in March 2020. It acknowledged the uncertainty from the war, but said the robust recovery justified a gradual build-up.
- In May 2023 it went further. It wrote that the credit gap showed **no signs of excessive credit growth**. Instead it pointed to investors' rising risk appetite, falling property prices, the debt sustainability of firms and governments, and banks that were robust, partly thanks to higher rates.
- So both decisions rested on the same three pillars: a normal-to-elevated risk picture, strong banks and the 2020 promise. Credit growth was never the reason.
LIKELY CHALLENGES:
- Q: Define cyclical systemic risk.
  - Risk that builds up over the financial cycle (credit, asset prices, risk-taking) and can materialise system-wide, as opposed to structural risk from the size or concentration of the banking sector.
- Q: Did DNB ever cite credit growth?
  - No. In 2023 it wrote that the gap showed 'no signs of excessive credit growth' and pointed to risk appetite, falling property prices, debt sustainability and strong banks.
- Q: Isn't 'uncertainty' an argument to wait?
  - It cuts both ways. Uncertainty is exactly why a releasable buffer is valuable; DNB judged the recovery strong enough to build it gradually.

## 13 · Risks and tools | 1:10
STORY:
- Which risks was the buffer meant to cover? DNB matched each risk with its own tool.
- The top row is **shocks nobody can forecast**: war, an energy shock, a sudden tightening of financial conditions, or bank turmoil abroad like Silicon Valley Bank and Credit Suisse in 2023. These go to the countercyclical buffer, because it can be released whatever the source of the shock.
- **Housing**, the known hot spot, was handled by borrower limits, tax reform and a mortgage risk-weight floor. The **size of the big banks** is handled by the structural buffer for systemically important banks.
- This is the Tinbergen principle: one instrument per target. If housing had been the target, the countercyclical buffer would have been the wrong tool, because it raises the cost of all lending.
LIKELY CHALLENGES:
- Q: State the Tinbergen principle.
  - To reach n independent policy targets you need at least n instruments, and each instrument should go to the target it affects most directly (Tinbergen, 1952).
- Q: Define LTV and LTI.
  - Loan-to-value and loan-to-income limits: caps on the size of a mortgage relative to the house value or the borrower's income. They are borrower-based measures.
- Q: What does the mortgage risk-weight floor do?
  - It sets a minimum average risk weight on Dutch mortgages for banks using internal models (Art. 458 CRR), raising RWA and capital for housing risk. In force January 2022 to November 2026.
- Q: Why not use the CCyB against housing?
  - It raises the cost of all lending, not just mortgages, so it is blunt for a sectoral problem and weak at steering house prices. Its comparative advantage is resilience against any shock.
- Q: Define O-SII.
  - Other systemically important institution. The O-SII buffer is a structural charge for size and interconnectedness, not designed to be released.

## 14 · The verdict | 1:10
STORY:
- Now we can test the two readings. If DNB was fighting a boom, the buffer should follow credit and prices. If it was normalising, it should follow a fixed path back to its normal level. Row by row:
- **Credit indicators:** they all fell while the buffer rose. **The path:** one point a year and a stop at two, exactly as normalisation predicts. **2023:** prices falling and rates jumping; a boom fighter would pause, but DNB raised. **2024 to 2026:** house prices up about ten percent again; a boom fighter would go above two percent, but DNB held. **Other buffers:** normalisation means cutting structural buffers in return, and DNB did so twice.
- *(pause)* Five predictions, five matches for normalisation, and none for overheating. This is the core of our argument.
LIKELY CHALLENGES:
- Q: Why is this a valid test?
  - The two hypotheses make different, observable predictions about the path, the timing and the other buffers. Five out of five fit normalisation and none fits overheating. Charts for each row: Appendix A1–A2.
- Q: What is framework phase 3?
  - 'Increased risk': the phase in which DNB would set the CCyB above 2%. It has not gone there, even when house prices rose about 10% a year in 2024–25.
- Q: Couldn't DNB be fighting a boom it expected later?
  - Then it would have raised further when house prices rebounded in 2024–25. It held at 2%.
- Q: Is this causal evidence?
  - No. It is a consistency test of DNB's behaviour against two explanations, not an estimate of effects.

## 15 · A swap, not a squeeze | 1:05
STORY:
- And the last row shows that the refill was a swap, not a squeeze. By our estimate, the 2020 cut released about six billion euros, the two countercyclical steps added 3.3 and 3.4 billion, and the 2024 cut released another 2.7 billion. Net, compared with before COVID, banks hold roughly the same required capital, or slightly less. DNB called it more or less capital-neutral for the three large banks.
- Two caveats: the bases differ, so the numbers are approximate, and compared with 2021 the refill was a modest increase.
- So capital was **moved** from buffers that cannot be released into one that can. The total stayed similar; what changed is who can use it, and when.
LIKELY CHALLENGES:
- Q: Define a structural buffer.
  - A capital charge for permanent features of a bank, such as size and interconnectedness (O-SII, systemic risk buffer). It is kept through the cycle and not meant to be released.
- Q: How did you compute the swap?
  - Own estimate: buffer cuts valued at end-2022 RWA of the four largest banks (−€6.0bn in 2020, −€2.7bn in 2024), plus DNB's sector-wide CCyB amounts (+€3.3bn, +€3.4bn). Net about −€2.0bn vs pre-COVID.
- Q: What are the caveats?
  - Different bases: O-SII applies to consolidated RWA, the CCyB only to Dutch exposures; the CCyB amounts include foreign and small banks; BNG is excluded. Relative to 2021 the refill was a modest increase.
- Q: Why not keep the structural buffers and add the CCyB?
  - The goal was usability, not quantity. Releasable capital is worth more per euro in a crisis, and stacking both would have been a real tightening.
- Q: Did other countries do this?
  - Yes. The UK offset its 2% neutral CCyB by lowering Pillar 2A and resolution requirements.

## 16 · The twist | 1:05
STORY:
- So, was it the wrong moment? We think not. The storm actually made it the **cheapest** moment.
- Headroom is the capital a bank holds above its requirement. At the end of 2022 Rabobank had 14.2 billion euros, ING 12.6, ABN AMRO 7.1 and de Volksbank 1.7, about 36 billion in total. The first step of 3.3 billion used eight percent of that, and the full buffer of 6.7 billion at most a fifth.
- And here is the twist. The same rising rates that made the moment look dangerous lifted bank profits, so banks could build the buffer from retained earnings instead of cutting loans. ECB research agrees that profitable banks and a gradual build-up keep the costs low.
LIKELY CHALLENGES:
- Q: Define headroom.
  - CET1 capital above a bank's requirement, i.e. above its MDA trigger. Headroom = (CET1 ratio − requirement) × RWA.
- Q: Where do the bank numbers come from?
  - Bank disclosures for ING, Rabobank and ABN AMRO. Only de Volksbank's requirement is derived (4.5% + 1.41% P2R + 2.5% + 1.0% O-SII).
- Q: Why is 19% an upper bound?
  - We compare DNB's sector-wide CCyB amount (all banks, Dutch exposures) with the headroom of only four banks, so the true share is lower.
- Q: Doesn't Modigliani–Miller say capital is free?
  - In frictionless markets more equity lowers the required return on equity, so funding costs barely change. Taxes, implicit guarantees and issuance costs make it costly in practice, but the cost is small when banks can retain earnings.
- Q: Did headroom fall because of the CCyB?
  - No. It fell from €42.3bn to €35.5bn mainly through RWA growth and payouts; the first CCyB step only bound in May 2023.

## 17 · Borrowers | 1:10
STORY:
- Did borrowers pay instead? We compare Dutch lending with five euro-area countries that never changed their buffer: Austria, Finland, Italy, Malta and Luxembourg.
- The red line is the Netherlands minus those countries. The grey band shows the differences that arise by chance, when we pretend each control country was the one that raised its buffer. Mortgage rates stay **inside the band** at all three dates. Household credit actually grew **faster**: Dutch bank credit grew 16.6 percent from early 2022 to early 2026, against 7.9 percent in the euro area, partly as a catch-up after lagging before.
- So we find **no sign of contraction**. With only one treated country this is not a causal estimate, but DNB reached the same conclusion in September 2026.
LIKELY CHALLENGES:
- Q: What is an event study?
  - We track the difference between the Netherlands and control countries month by month before and after each CCyB date, with country and month fixed effects.
- Q: What is a placebo test here?
  - We rerun the estimate pretending each control country was treated. The range of these fake effects (the grey band) shows what chance alone produces.
- Q: Why these five controls?
  - Austria, Finland, Italy, Malta and Luxembourg did not change their CCyB in 2021–25, so they are clean. Countries that raised their own buffers would contaminate the comparison.
- Q: Why is it not causal?
  - One treated country, a small control group, a pre-announced path (anticipation) and the Dutch housing rebound. So we only say 'no sign of contraction'.
- Q: Why did Dutch credit grow faster?
  - Partly catch-up: in 2019–22 Dutch bank credit grew 4.3% vs 11.3% in the euro area; in 2022Q1–2026Q1 it grew 16.6% vs 7.9%.

## 18 · Monetary policy | 0:55
STORY:
- A natural worry is that two tightenings at once, higher policy rates and higher capital requirements, would choke credit. The chart shows that this did not happen. Dutch mortgage rates, in red, followed the ECB's deposit rate, in grey, and moved closely with mortgage rates in the control countries, in blue.
- The ECB argues that building buffers early lets monetary policy focus on its main goal, price stability. With one monetary policy for twenty countries, the countercyclical buffer is the **Dutch-specific lever**. It is also insurance in case a rate shock goes wrong.
LIKELY CHALLENGES:
- Q: Macro- vs monetary policy?
  - Monetary policy sets interest rates for price stability across the euro area. Macroprudential policy targets the stability of the financial system and can be set nationally.
- Q: Didn't both policies tighten at once?
  - Both tighten credit at the margin, but Dutch mortgage rates moved with the ECB rate and with the control countries, and bank profits rose with rates.
- Q: Why is a national lever useful in a currency union?
  - The ECB cannot react to Dutch-specific financial conditions. The CCyB is the country-specific tool, and a buffer built early lets monetary policy focus on price stability (ECB, 2025).

## 19 · Across borders | 0:55
STORY:
- The buffer also reaches across borders. Under EU reciprocity, foreign banks that lend into the Netherlands must also hold the Dutch two percent on those loans. This limits leakage to foreign lenders, which is a known weakness of national capital rules, although lending can still move to non-banks.
- And the Netherlands is part of a European shift. The chart shows the rates and the dates from which they apply. Germany, France, Ireland, Belgium, Portugal and Spain have all raised their buffers since 2023. The Netherlands was early and set the highest rate, but it was not alone.
LIKELY CHALLENGES:
- Q: Define reciprocity.
  - Foreign banks apply the Dutch CCyB rate to their Dutch exposures. In the EU this is mandatory up to 2.5%.
- Q: Define leakage.
  - Credit shifting to lenders not covered by the rule, such as foreign branches or non-banks. Reciprocity closes the foreign-bank channel; non-banks remain outside.
- Q: Did lending move to non-banks?
  - We have not measured non-bank mortgage shares, so we cannot claim either way. That is a limitation.
- Q: Was the Netherlands an outlier?
  - It was early and at the top (2%), but Germany, France, Ireland, Belgium, Portugal and Spain all raised their buffers since 2023.

## 20 · Resilience | 1:05
STORY:
- The result is shown in this chart. In March 2020 the Netherlands had no releasable capital at all. Today it has **6.7 billion euros**, about half of the peak losses after the financial crisis, and enough to support up to 150 billion euros of lending.
- This buffer is cheap to hold and powerful to release. Research on European banks suggests that a one-point increase in normal times reduces lending by only about 0.1 percent, while a one-point release in bad times can raise lending by up to ten percent.
- And its role is growing. The floor on mortgage risk weights expires in November 2026, and DNB says that this underlines the importance of the two-percent buffer.
LIKELY CHALLENGES:
- Q: Define a state-dependent effect.
  - The impact of a policy depends on the state of the economy. Lang & Menno (2023): +1pp in normal times cuts lending by about 0.1%; a 1pp release in bad times can raise it by up to about 10%.
- Q: How much is releasable now?
  - About €6.7bn (€3.3bn + €3.4bn), about half of the €12bn peak losses after the GFC, supporting up to €150bn of lending.
- Q: Why does the floor expiry matter?
  - From 30 November 2026 the mortgage risk-weight floor no longer adds capital for housing risk; DNB says this 'underpins the importance' of the 2% CCyB.

## 21 · Critiques | 1:00
STORY:
- Of course there is a price, and we see five critiques.
- **Credibility:** without a rule, markets must trust DNB's judgement, so DNB has to explain every decision. **Calibration:** why two percent, when the ECB's estimates range from 1.1 to 1.8? **Untested:** the buffer has never been released, and in 2020 many banks did not use the buffers they were allowed to use. **Baseline:** compared with 2021 rather than 2019, it was an increase. **Profits:** the same profits that fund the buffer were also targeted by levies on excess profits.
- None of these overturns our verdict, but they define what DNB must get right next time.
LIKELY CHALLENGES:
- Q: Rules vs discretion?
  - Rules give predictability and credibility; discretion gives flexibility but risks inaction or time inconsistency (Kydland & Prescott, 1977). DNB's pre-announced path is a commitment device within discretion.
- Q: Will banks actually use released capital?
  - Untested in the Netherlands. A released CCyB lowers the requirement itself, so it avoids the MDA stigma that stopped banks using buffers in 2020.
- Q: Isn't the baseline choice convenient?
  - Yes, it matters: vs pre-COVID the refill is roughly neutral; vs 2021 it was an increase of €3.3bn before the O-SII offset. We show both.
- Q: What about excess-profit levies?
  - The ECB lists the Netherlands among countries with levies on banks' excess profits in 2022–23, which partly claim the same earnings that fund the buffer.

## 22 · Conclusion | 1:05
STORY:
- Let us conclude with the three questions of the assignment. The **environment** was a recovered economy hit by war, inflation and rate hikes, with cold credit, a cooling housing market and strong banks. The **criteria** were a two-percent normal level calibrated on past losses, as insurance against shocks nobody can forecast. The **implications**: the refill was cheap, largely a swap, with no sign of contraction, and it leaves 6.7 billion euros ready to release, at the price of more discretion.
- *(pause)* In March 2020 the Netherlands had nothing to release. **Next time, it will.** The best time to fill a buffer is when nobody thinks you need it, even in a storm. Thank you, and we look forward to your questions.
LIKELY CHALLENGES:
- Q: What is your main contribution?
  - Showing, with a testable comparison, that the Dutch increase was a refill of releasable capital rather than a response to a credit boom, and that it was cheap when it happened.
- Q: What would change your verdict?
  - DNB going above 2% while credit indicators rise, or evidence that lending contracted around the binding dates.
- Q: Would you recommend this to other countries?
  - Where the gap is unreliable and buffers are mostly structural, yes: build a releasable buffer in normal times, gradually, and offset structural charges. The cost is greater reliance on judgement.

## 23 · Glossary | backup
STORY:
- Backup only. Use it when a question involves a term; point to the row and give the one-line definition.
LIKELY CHALLENGES:
- Q: Use this page to define any term quickly.
  - Point to the term and give the one-line definition; then return to the slide being discussed.

## 24 · Methods and references | backup
STORY:
- Backup for method questions.
  - **Credit gap:** one-sided and two-sided HP filter (λ = 400,000), plus Hamilton regression filter.
  - **Headroom:** (CET1 ratio minus requirement) × total RWA, per bank.
  - **Event study:** two-way fixed effects, three-month bins, placebo inference over five never-treated countries.
- All references are verified.
LIKELY CHALLENGES:
- Q: How exactly is the event study specified?
  - Two-way fixed effects: outcome on NL × 3-month event-time bins, with country and month fixed effects; placebo inference over clean controls (AT, FI, IT, MT, LU).
- Q: How is headroom computed?
  - (CET1 ratio − CET1 requirement/MDA trigger) × total RWA per bank; the CCyB amount is sector-wide, so shares are upper bounds.

## 25 · Appendix A1: verdict rows 1–2 | backup
STORY:
- The left panel shows the path: two steps of one point, a year apart, then held at two percent, exactly as normalisation predicts.
- The other three panels show the credit indicators. Between the two announcements the credit gap, the debt-service ratio and household debt all fell, so the buffer did not follow credit.
LIKELY CHALLENGES:
- Q: Why does the path matter?
  - A boom fighter's buffer follows risk indicators; a normalising buffer follows a pre-announced timetable. The CCyB moved in two equal steps a year apart while the gap, debt service and household debt all fell.

## 26 · Appendix A2: verdict rows 3–5 | backup
STORY:
- On the left, house prices: in 2023 they were falling, yet DNB announced two percent. In 2024 and 2025 they grew about ten percent a year, yet DNB held at two percent.
- In the middle, the ECB deposit rate stood at 3.25 percent when the second step was announced.
- On the right, the systemic buffers of the three large banks were cut in 2020 and again in 2024, which is what normalisation predicts.
LIKELY CHALLENGES:
- Q: Why show house prices and the ECB rate?
  - They are the two conditions under which a boom fighter would have behaved differently: pause in 2023 when prices fell and rates jumped, go above 2% in 2024–25 when prices rose about 10%.
- Q: What does the right panel prove?
  - That structural buffers were cut twice (2020 and 2024), which only makes sense if the CCyB was replacing them rather than adding to them.
