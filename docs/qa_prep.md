# Q&A preparation: questions a professor of central banking is likely to ask

**Focus:** concepts, economic reasoning and econometric method, not Dutch trivia.

**Format for each question:**
- **Concept:** the key idea in one sentence.
- **Answer:** a model answer of 4–6 sentences.
- **Our case:** how it links to the Netherlands.
- **Follow-up:** the most likely next question, with a short answer.
- **Refs:** verified references only (see `03_references.md`).

Numbers come from `docs/02_findings.md`.

**Who answers by default.**
- **Zheng:** A1–A4 and B1–B3, the institutional and policy questions.
- **Diego:** A5–A6, B4–B6 and C1–C10, the reasoning and econometrics.
- The other speaker adds one sentence at most. Never two people answering at once.

---

## A. Macroprudential and banking concepts

### A1. Why is bank capital procyclical, and how does macroprudential regulation differ from microprudential regulation?
- **Concept:** Risk-sensitive capital rules bind hardest in downturns, so banks shrink lending exactly when the economy needs credit. Macroprudential policy targets that system-wide externality, not the soundness of each bank in isolation.
- **Answer:**
  - In a downturn, losses reduce capital and risk weights rise, so required capital goes up while available capital goes down.
  - Each bank restores its ratio by cutting assets, which is individually rational. Collectively, the credit crunch deepens the recession and raises losses further, a fire-sale and credit-supply externality.
  - Microprudential supervision asks "is this bank safe?" and is satisfied if every bank deleverages.
  - Macroprudential policy asks "is the system safe and still lending?" and sees that synchronised deleveraging is the problem.
  - The CCyB is the textbook macroprudential tool: it adds capital in good times and releases it in bad times, leaning against that procyclicality.
- **Our case:** In March 2020 the Netherlands had no releasable buffer. DNB had to improvise by cutting a *structural* buffer, which is exactly the gap the positive neutral CCyB now fills.
- **Follow-up:** "Isn't the capital conservation buffer already countercyclical?" Not in practice. Dipping into it triggers MDA restrictions, and banks avoid that (see A2).
- **Refs:** Repullo & Saurina (2011); Drehmann et al. (2010); BCBS (2024) d585.

### A2. Walk us through the capital stack. Which layers are usable, which are releasable, and why don't banks use their buffers?
- **Concept:** Requirements (P1, P2R) must be met at all times. Buffers (CCoB, systemic, CCyB) can in principle be used. Only the CCyB, and in some cases the systemic risk buffer, can be *released* by the authority.
- **Answer:**
  - From the bottom: Pillar 1 (4.5% CET1), the bank-specific Pillar 2 requirement, then the combined buffer requirement (capital conservation buffer 2.5%, O-SII/SRB, CCyB). Pillar 2 guidance sits on top and is not binding.
  - A bank whose CET1 falls into the combined buffer faces automatic limits on dividends, buybacks and bonuses, set by the maximum distributable amount (MDA).
  - "Usable" buffers are therefore not used in practice: banks fear the MDA restrictions, market stigma and rating pressure.
  - COVID evidence shows banks close to their buffer thresholds cut lending relative to others, even when supervisors encouraged buffer use.
  - A *released* CCyB is different: the requirement itself falls, so the bank's distance to the MDA trigger rises and there is no stigma.
- **Our case:** This is why DNB wanted releasable capital and moved capital from O-SII/SRB into the CCyB (slides 3 and 14).
- **Follow-up:** "Why not simply make the CCoB releasable?" That would need a change to EU law. A positive neutral CCyB achieves the same within the existing framework, which is part of why BCBS (2024) documents its spread.
- **Refs:** Couaillier, Lo Duca, Reghezza & Rodriguez d'Acri (2022); BCBS (2024) d585; Behn et al. (2023, ECB MPB 21).

### A3. What are risk-weighted assets, how does the Dutch mortgage risk-weight floor work, and how is a bank's CCyB rate computed?
- **Concept:** Capital ratios divide capital by risk-weighted assets, so both the risk weights and the geographic mix of exposures determine how much capital a buffer rate actually requires.
- **Answer:**
  - RWA weight each exposure by its estimated riskiness. Under internal models (IRB), Dutch mortgages had very low weights.
  - DNB's Article 458 measure set a floor on the *average* risk weight of IRB banks' Dutch mortgage portfolios. It was postponed in 2020, applied from January 2022, and expires on 30 November 2026.
  - A floor raises RWA, and therefore the capital needed for any given ratio, so it is a targeted capital tool for housing risk.
  - The CCyB rate a bank faces is a weighted average of the rates in the countries where its credit exposures are located, weighted by those exposures. The Dutch 2% applies only to Dutch exposures.
  - So a bank with large foreign books faces an institution-specific CCyB well below 2%, while a domestic lender faces almost the full 2%.
- **Our case:** This is why our swap calculation flags different bases. O-SII cuts apply to consolidated RWA, the CCyB only to Dutch exposures. The impact therefore differed by bank, as DNB itself noted.
- **Follow-up:** "Does the floor's expiry matter for the CCyB?" Yes. DNB says the expiry "underpins the importance of … the current CCyB of 2%", because it becomes the main capital buffer that also covers housing-related losses.
- **Refs:** DNB (24 Apr 2026); ESRB opinion on the Dutch Art. 458 measure (2024); DNB (2023) press release.

### A4. What are reciprocity and leakage, and how much do they matter for a national CCyB?
- **Concept:** Leakage is credit moving to lenders outside the tool's reach. Reciprocity extends the tool to foreign lenders.
- **Answer:**
  - A national capital requirement only binds domestically supervised banks. Foreign branches, cross-border lenders and non-banks can expand when domestic banks are constrained.
  - UK evidence shows exactly this: foreign branches offset a sizeable share of the credit reduction at regulated banks.
  - The EU makes CCyB reciprocity mandatory up to 2.5%, so any bank lending into the Netherlands must hold the Dutch rate on those exposures. That closes the cross-border bank channel.
  - Non-bank leakage remains: non-bank lenders such as insurers and pension funds are outside bank capital rules.
- **Our case:** Because the Dutch move was a normal-times buffer rather than a binding squeeze, the incentive to leak was small. We find no sign of contraction in bank credit itself.
- **Follow-up:** "So did lending shift to non-banks?" We have not measured non-bank mortgage shares. That is a limitation we would name, not a finding we can claim.
- **Refs:** Aiyar, Calomiris & Wieladek (2014); Cerutti, Claessens & Laeven (2017).

### A5. Why might higher capital requirements raise lending rates only a little? What does Modigliani–Miller say, and where does it fail?
- **Concept:** Under Modigliani–Miller, more equity lowers the required return on equity, so the overall funding cost barely changes. Frictions make the private cost positive but small.
- **Answer:**
  - MM (1958): in frictionless markets, a firm's funding cost does not depend on its leverage. More equity makes equity safer, and its required return falls.
  - For banks it fails partly, for four reasons:
    - Debt is tax-deductible, so substituting equity for debt loses a tax shield.
    - Implicit guarantees subsidise bank debt.
    - Debt overhang makes shareholders reluctant to issue equity that partly benefits creditors (Myers 1977).
    - Issuing equity is costly and signals bad news.
  - Admati et al. (2013) argue that much of the claimed cost is private rather than social, because the tax shield and the guarantee are transfers.
  - Empirically, pricing effects are small: Swiss banks most exposed to the sectoral CCyB raised mortgage rates by about 8bp more (Basten 2020).
  - The ECB finds costs fall further when the build-up is gradual and banks are profitable.
- **Our case:** Dutch new-business lending rates stayed inside the placebo band, banks met the buffer from retained earnings (net interest income +6.7%), and DNB expected no rise in lending rates.
- **Follow-up:** "Then why do banks lobby so hard against capital?" Because the cost to shareholders (lost tax shield and guarantee subsidy, diluted return on equity) is real even if the social cost is small.
- **Refs:** Modigliani & Miller (1958); Myers (1977); Admati, DeMarzo, Hellwig & Pfleiderer (2013); Basten (2020); Herrera, Scalone & Pirovano (2024, ECB MPB 24).

### A6. What distinguishes a positive neutral CCyB from the gap-based CCyB, and how is a 2% neutral rate calibrated?
- **Concept:** The gap-based CCyB is switched on only when credit grows above trend. A positive neutral CCyB is already filled when risks are "standard", so it can be released for any shock.
- **Answer:**
  - The original Basel design maps the credit-to-GDP gap into a buffer between 0 and 2.5%. In normal times the buffer is therefore zero, and nothing can be released when a non-credit shock like COVID hits.
  - A positive neutral rate sets a non-zero target in a standard risk environment, built gradually, raised further if risks rise, and released if they materialise.
  - Calibration approaches include historical losses, stress tests and models.
  - DNB matched the buffer to peak accumulated losses of €12bn (2007–16): 2% ≈ €6bn releasable, or up to €150bn of extra lending headroom.
  - The ECB's loss-based approach gives a euro-area range of 1.1–1.8%.
  - BCBS lists 17 jurisdictions with a positive neutral rate, ranging from 0.5% to 2%.
- **Our case:** NL is at the top of that range (with Sweden, the UK and Poland). It also explicitly took the 2020 buffer cut into account.
- **Follow-up:** "So is 2% too high?" It is defensible as a loss-based number and partly a re-composition of existing capital, but it sits above the ECB central range. That is a fair critique we acknowledge (slide 20).
- **Refs:** DNB (2022) framework; BCBS (2024) d585; De Nora, Pereira, Pirovano & Stammwitz (2025); Behn et al. (2023).

---

## B. Economic reasoning and policy design

### B1. What is the Tinbergen rule, and why should housing risk go to borrower-based measures and cyclical risk to the CCyB?
- **Concept:** You need at least as many independent instruments as targets, and each instrument should go to the target it affects most directly.
- **Answer:**
  - Tinbergen (1952): to reach *n* policy targets you need *n* instruments.
  - Housing risk is about borrowers' leverage and house-price dynamics. Loan-to-value and loan-to-income limits act directly on the flow of risky mortgages, and risk-weight floors on banks' exposure to them.
  - A CCyB raises the cost of *all* lending: a blunt tool for a sectoral problem, and weak against house prices.
  - Its comparative advantage is resilience against shocks of any origin, because it can be released.
  - Assigning housing to borrower-based measures and the floor, systemic size to the O-SII buffer, and unforeseeable shocks to the CCyB is the Tinbergen logic applied.
- **Our case:** DNB called housing "overheated" in 2022 but asked for tax and borrowing-rule changes rather than a higher CCyB. In 2023 it raised the CCyB while house prices fell (slides 12–13).
- **Follow-up:** "With the floor expiring, isn't the CCyB now doing housing's job?" Partly, as resilience against housing losses, not to steer house prices. DNB says exactly that.
- **Refs:** Tinbergen (1952); Akinci & Olmstead-Rumsey (2018); Cerutti, Claessens & Laeven (2017).

### B2. Rules versus discretion: why not a mechanical rule, and what is "guided discretion"?
- **Concept:** Rules buy credibility and predictability. Discretion buys flexibility but invites time inconsistency and inaction bias. Guided discretion tries to get both.
- **Answer:**
  - Kydland & Prescott (1977) show that discretionary policy can be time-inconsistent: once expectations are set, the policymaker is tempted to deviate.
  - In macroprudential policy the bigger risk is *inaction bias*: tightening in a boom is unpopular, and the costs are immediate while the benefits are invisible.
  - A mechanical rule guards against this, but only if the rule is good. The credit gap missed the GFC in NL and raised false alarms.
  - Guided discretion means an announced framework (phases, a neutral rate, a published dashboard) plus judgement, with each decision explained quarterly.
  - The positive neutral rate is itself a commitment device: it pre-commits to building the buffer in calm times, when the political cost is lowest.
- **Our case:** DNB pre-announced the 2% in 2020 and the 1pp-a-year path in 2022. It then followed it through falling house prices and rising rates. That is consistency with a rule-like path despite discretion.
- **Follow-up:** "How would you hold DNB accountable?" Through the published dashboard and quarterly explanations, and by checking that the buffer *is* released when a shock hits. That test has not happened yet.
- **Refs:** Kydland & Prescott (1977); DNB (2022) framework; Drehmann & Tsatsaronis (2014).

### B3. How does a CCyB increase interact with ECB monetary tightening? One monetary policy, national macroprudential policy: is that a problem?
- **Concept:** Tightening both at once could double-squeeze credit. But resilience built early lets monetary policy focus on inflation, and national macroprudential policy is the only country-specific lever in a currency union.
- **Answer:**
  - In 2022–23 the ECB raised rates sharply while several countries, including NL, raised CCyBs. Both tighten credit supply on the margin.
  - The ECB argues that early CCyB activation "helps monetary policy focus on its primary objective of price stability, thereby largely eliminating the potential for conflict" with financial stability.
  - Rate hikes also raised bank profits (net interest margins), which made building the buffer cheaper.
  - In a monetary union, monetary policy cannot respond to Dutch-specific financial conditions, so national macroprudential tools are the substitute for the lost national interest rate.
  - The CCyB is also insurance: if the rate shock had triggered a crisis, a released buffer would have offset it.
- **Our case:** Dutch lending rates did not diverge from euro-area peers around any CCyB date, and household credit grew faster. This is "no sign of contraction" (slide 17).
- **Follow-up:** "Shouldn't DNB have waited until the ECB stopped hiking?" The ECB's own simulations suggest activating during tightening mitigates costs. Waiting would also have meant entering a possible downturn with nothing to release.
- **Refs:** Detken, Hempell & Pirovano (2025, ECB MPB 31); Herrera, Scalone & Pirovano (2024, ECB MPB 24).

### B4. Wasn't the Dutch CCyB increase a disguised tightening? What is the difference between a normal-times buffer and a countercyclical tightening?
- **Concept:** A countercyclical tightening responds to rising risk and aims to restrain credit. A normal-times buffer is built regardless of the cycle, to have something to release.
- **Answer:**
  - The test is behavioural, so we compare predictions.
  - A tightening would track risk indicators, pause when house prices fall, and go above 2% when they rise again, with no offsetting cuts.
  - DNB did the opposite on every count: it raised while credit indicators fell, raised in 2023 while house prices fell, held at 2% when prices rose about 10% y/y in 2026, and cut O-SII/SRB buffers in 2020 and 2024.
  - In euros, the 2020 and 2024 structural cuts (≈ €6.0bn + €2.7bn, own estimate) roughly offset the €6.7bn CCyB relative to pre-COVID.
  - Relative to 2021 it *was* a modest increase, and we say so.
- **Our case:** This is our verdict table (slide 13) and swap chart (slide 14).
- **Follow-up:** "Why not keep the SRB and add the CCyB, for more resilience?" Because the goal was usability, not quantity. Releasable capital is worth more per euro in a crisis (Lang & Menno 2023), and stacking both would have been a real tightening.
- **Refs:** DNB (2020) press release; Knot (2023) statement; DNB FSR spring 2023; BCBS (2024) d585.

### B5. How do inflation and nominal GDP growth affect debt-to-GDP and the credit gap?
- **Concept:** Ratios fall when the denominator grows. High nominal GDP growth (from inflation) mechanically lowers debt/GDP and the credit gap, even if the debt stock rises.
- **Answer:**
  - The credit-to-GDP ratio is nominal credit divided by nominal GDP. With 11.6% inflation, nominal GDP surged, so the ratio and its gap fell even with no deleveraging.
  - This is a denominator effect and says little about cyclical risk.
  - The reverse caused the 2012 false alarm: falling GDP inflated the ratio during a bust (Repullo & Saurina).
  - So gaps and ratios must be read alongside levels and growth of real credit.
- **Our case:**
  - Dutch household debt/GDP fell from 110% (2019Q4) to 100% (2023Q1), but the stock of household debt *rose* 12% (€910bn → €1,016bn), because nominal GDP rose about 22%.
  - Part of the very negative gap in 2023 (−47pp) is this inflation effect.
- **Follow-up:** "Then is the negative gap meaningless?" Not meaningless, but biased downward in high inflation. That is another reason DNB used a broad dashboard.
- **Refs:** Repullo & Saurina (2011); Drehmann & Tsatsaronis (2014).

### B6. What is Growth-at-Risk, and how does a releasable buffer affect the lower tail?
- **Concept:** Growth-at-Risk (GaR) is a low quantile (e.g. the 5th percentile) of the predicted distribution of future GDP growth. Financial conditions move this lower tail much more than the median.
- **Answer:**
  - Adrian, Boyarchenko & Giannone (2019) estimate quantile regressions of future GDP growth on current financial conditions.
  - Tighter conditions shift the lower quantiles down sharply while the upper quantiles barely move, so downside risk is time-varying.
  - Macroprudential policy can be read as managing that lower tail: a buffer built in normal times costs a little median growth but, when released, limits the credit crunch in bad states.
  - Lang & Menno (2023) show the asymmetry: a 1pp higher requirement cuts lending by about 0.1% in normal times, while a 1pp release in bad times can raise lending by up to about 10%.
- **Our case:** The €6.7bn releasable buffer, up to €150bn of lending capacity, is a lower-tail insurance policy bought cheaply in normal times (slide 19).
- **Follow-up:** "Have you estimated GaR for the Netherlands?" No. We use the concept to interpret the policy, not as our own estimate.
- **Refs:** Adrian, Boyarchenko & Giannone (2019); Lang & Menno (2023).

---

## C. Econometrics and measurement

### C1. How does the HP filter work, and why λ = 400,000 for credit?
- **Concept:** The HP trend minimises the squared deviation of the series from the trend plus λ times the squared second differences of the trend. λ sets how smooth the trend is.
- **Answer:**
  - The trend τ solves min Σ(y_t − τ_t)² + λ Σ(Δ²τ_t)², a penalised least-squares problem. In matrix form, τ = (I + λD′D)⁻¹ y.
  - Higher λ means a smoother trend and longer cycles attributed to the "gap".
  - λ = 1,600 is standard for quarterly business cycles. Credit cycles are roughly four times longer.
  - Ravn & Uhlig (2002) show that λ should scale with the fourth power of the frequency (cycle-length) ratio, so 1,600 × 4⁴ ≈ 400,000. That is the Basel choice.
- **Our case:** We implement exactly this with sparse matrices. The one-sided version reproduces the official BIS gap within 0.00005pp (1971–2026).
- **Follow-up:** "Why scale by the fourth power?" Because the filter's frequency response depends on λ through the fourth power of frequency (the second-difference penalty).
- **Refs:** Hodrick & Prescott (1997); Ravn & Uhlig (2002); Drehmann et al. (2010).

### C2. One-sided versus two-sided filters, the end-point problem, and real-time versus quasi-real-time versus ex-post estimates.
- **Concept:**
  - A two-sided filter uses future data to estimate today's trend.
  - A one-sided filter uses only data up to today, as a policymaker must.
  - The difference at the sample end is the end-point problem.
- **Answer:**
  - The two-sided HP trend at date t depends on observations after t. At the end of the sample those are missing, so the trend is pulled toward the last observations and gets revised as new data arrive.
  - The one-sided (recursive) filter re-estimates the trend each quarter with data up to that quarter. The official Basel gap is one-sided.
  - Orphanides & van Norden (2002) distinguish three estimates:
    - *real-time:* data vintages as available then
    - *quasi-real-time:* the one-sided filter on today's revised data
    - *ex-post:* the two-sided filter on the full sample
  - They show most revisions come from the end-point problem, not from data revisions. Edge & Meisenzahl (2011) find the same for credit gaps.
- **Our case:** The Dutch gap in 2016Q1 was −0.6pp one-sided but +26.9pp two-sided. Our estimates are quasi-real-time, because we lack data vintages, and we say so.
- **Follow-up:** "How big are data revisions for Dutch GDP?" We have not measured them. That is precisely why we label our gap quasi-real-time.
- **Refs:** Orphanides & van Norden (2002); Edge & Meisenzahl (2011); Hamilton (2018).

### C3. What is Hamilton's critique of the HP filter, how does his regression filter work, and why h = 8 or h = 20?
- **Concept:** The HP filter creates spurious cycles and end-point bias. Hamilton instead defines the cycle as the part of y_{t+h} that cannot be forecast from information at t.
- **Answer:**
  - Hamilton (2018) shows three problems with the HP filter:
    - it can generate cyclical dynamics that are not in the data
    - end-of-sample values behave differently from mid-sample ones
    - statistically justified λ values differ wildly from those used in practice
  - His alternative regresses y_{t+h} on a constant and the four most recent values y_t, …, y_{t−3}. The residual is the cycle, so it is a forecast error over horizon h.
  - h = 8 quarters (two years) suits business cycles. h = 20 (five years) is the analogue for longer credit cycles.
  - It is one-sided by construction but sensitive to large shocks in the window.
- **Our case:** At the 2023 decision (data to 2022Q4) every Hamilton gap was negative. At the 2022 decision (data to 2021Q4) the h = 20 gap was negative, but the h = 8 gap was *positive* (+12.6pp ex post, +3.5pp in quasi-real time), because the 2020 GDP collapse and rebound fall inside its two-year window. This is why we never rely on a single filter, and why the official Basel gap is our reference.
- **Follow-up:** "BIS work argues HP is fine for credit gaps; who is right?" For early warning the HP gap performs well historically. Hamilton is right about its statistical properties. For the Netherlands the official one-sided HP gap and the h = 20 Hamilton gap both point to 0% at both decisions, so our conclusion does not hinge on the choice.
- **Refs:** Hamilton (2018); Drehmann & Tsatsaronis (2014).

### C4. How do you evaluate an early-warning indicator? Noise-to-signal, AUROC, type I and type II errors, and the policymaker's loss function.
- **Concept:** An indicator issues a signal when it crosses a threshold. Its quality is the trade-off between missed crises (type I) and false alarms (type II) across thresholds.
- **Answer:**
  - For a given threshold you count true signals, false alarms and missed crises.
  - The noise-to-signal ratio is the false-alarm rate divided by the hit rate; lower is better.
  - The ROC curve plots the hit rate against the false-alarm rate for all thresholds. The area under it (AUROC) summarises performance: 0.5 is a coin flip, 1 is perfect.
  - The chosen threshold depends on the policymaker's loss function: how costly a missed crisis is relative to a false alarm. Since crises are very costly, thresholds are usually set to keep missed crises low.
  - Drehmann & Juselius (2014) add policy requirements: signals must come early enough, given the 12-month implementation lag, and must be stable.
- **Our case:** In NL the credit gap missed the GFC (type I) and gave a false alarm in 2012 (type II). For a CCyB that must be built 12 months ahead, that record is poor (slide 9).
- **Follow-up:** "Then why does Basel still use the gap?" Across many countries it has one of the best AUROCs. Basel treats it as a *starting point*, not a mechanical trigger.
- **Refs:** Drehmann & Juselius (2014); Drehmann & Tsatsaronis (2014).

### C5. Why does the credit gap fail for the Netherlands specifically?
- **Concept:** The HP filter assumes a stable trend. Dutch credit/GDP has a strong structural trend and long swings, so the "trend" absorbs structural change and the gap reflects filter artefacts.
- **Answer:**
  - Dutch private credit rose from about 47% of GDP in 1961 to about 350% at its 2015 peak. That largely reflects structural financial deepening, notably a large mortgage market supported by favourable tax treatment (DNB's FSR 2022 itself criticises the tax breaks), not just cycles.
  - A filter with a very long implicit cycle extrapolates this trend. When the ratio then falls, the gap becomes deeply negative (−33/−47pp at the decisions) even if cyclical risk has not fallen.
  - The ratio is also non-stationary and sensitive to the denominator: GDP falls inflate it (2012), inflation deflates it (2022–23).
  - The result is a long series of type I and type II errors on Dutch data.
- **Our case:** This motivates DNB's dashboard approach. DNB itself notes in 2026 that its 2% is "above the 0% implied by the Basel buffer guide".
- **Follow-up:** "Would a different trend fix it, e.g. a shorter λ or log levels?" It would change the level but not the core problem: an unknown structural trend in a ratio with long swings.
- **Refs:** Drehmann & Tsatsaronis (2014); Repullo & Saurina (2011); Edge & Meisenzahl (2011).

### C6. What does difference-in-differences need to identify a causal effect, and why is your simple DiD not causal?
- **Concept:** DiD identifies an effect if, without treatment, treated and control units would have followed parallel trends; there is no anticipation; and there are no spillovers or contaminated controls (SUTVA).
- **Answer:**
  - DiD compares the change in the treated group with the change in controls, so common shocks cancel out.
  - It requires:
    - **parallel trends** in the counterfactual
    - **no anticipation**, so outcomes do not react before treatment
    - **SUTVA**, so the treatment of one unit does not affect others and controls are untreated
  - Our naive DiD (NL vs euro area, +0.96pp per quarter) fails on all three:
    - NL was deleveraging before 2022, so trends were not parallel.
    - The path was announced in 2020, so anticipation was likely.
    - France, Germany, Belgium and Ireland raised their own CCyBs, so the controls are contaminated.
  - Rate hikes were also a common shock with heterogeneous pass-through: Dutch mortgages have long fixed-rate periods.
- **Our case:** That is why we only claim "no sign of contraction" and use a cleaner design with placebo inference (C9) as supporting evidence.
- **Follow-up:** "Can you test parallel trends?" Partly, through pre-period coefficients. For household credit they are flat; for NFC credit they are not, so we drop the NFC result.
- **Refs:** Goodman-Bacon (2021); Callaway & Sant'Anna (2021).

### C7. What goes wrong with two-way fixed effects when adoption is staggered? Goodman-Bacon and Callaway–Sant'Anna.
- **Concept:** With staggered treatment timing and heterogeneous effects, the TWFE coefficient is a weighted average of all 2×2 comparisons. Some of them use already-treated units as controls and can carry negative weights.
- **Answer:**
  - Goodman-Bacon (2021) decomposes the TWFE DiD estimate into all two-group, two-period comparisons, weighted by group size and treatment variance.
  - When effects change over time, comparisons that use earlier-treated units as "controls" subtract part of the treatment effect, so the estimate can be biased or even have the wrong sign.
  - Callaway & Sant'Anna (2021) estimate group-time average treatment effects, ATT(g,t), comparing each adoption cohort only with not-yet-treated or never-treated units, and then aggregate them.
  - Euro-area CCyB increases are a textbook staggered rollout: DE Feb-23, FR Apr-23/Jan-24, IE, BE, NL May-24, PT, ES and others.
- **Our case:** We avoid the problem by using only never-treated (in 2021–25) controls: AT, FI, IT, MT, LU. A multi-country Callaway–Sant'Anna design would be the natural extension.
- **Follow-up:** "Why not run Callaway–Sant'Anna now?" Few cohorts and few never-treated countries make group-time estimates noisy, and our question concerns one country.
- **Refs:** Goodman-Bacon (2021); Callaway & Sant'Anna (2021).

### C8. How do you choose the event date in an event study, and why might a pre-announced framework produce a small announcement effect?
- **Concept:** If agents react to news, the right event date is when information arrives. A well-communicated policy may have been priced in long before the formal announcement.
- **Answer:**
  - Candidate dates are the announcement (news) and the effective date (binding).
  - Banks adjust capital planning when they *learn* of a future requirement, so lending effects can start at announcement or even earlier. Pricing effects may concentrate when the requirement binds.
  - With anticipation, pre-event coefficients move and the measured jump at the event date understates the total effect.
  - A positive neutral framework is designed to be predictable. The 2% was flagged in March 2020 and the path in February 2022, so little "news" arrived in May 2022 or May 2023.
- **Our case:**
  - Our three dates collapse four events: the second announcement and the first effective date fall in the same week of May 2023.
  - A small measured effect is consistent with no effect *and* with full anticipation. That is why we do not claim causality.
- **Follow-up:** "Then isn't the event study uninformative?" It rules out a large discontinuous contraction around the dates. What it cannot do is detect a smooth, fully anticipated effect.
- **Refs:** DNB (2020, 2022) announcements; our event study (`code/event_study.py`).

### C9. Could synthetic control do better here? What are its limits?
- **Concept:** Synthetic control builds a weighted combination of control countries that matches the treated unit's pre-treatment path, then uses it as the counterfactual. Inference comes from placebo permutations.
- **Answer:**
  - Abadie, Diamond & Hainmueller (2010) choose non-negative weights on donor units to reproduce the treated unit's pre-period outcomes and covariates.
  - It suits one treated unit, which is our case, and makes the counterfactual transparent.
  - Inference uses in-space placebos: apply the method to each donor and compare post/pre fit ratios. We use the same idea for our placebo band.
  - Limits here:
    - The clean donor pool is tiny (AT, FI, IT, MT, LU) and structurally different.
    - The Netherlands may lie outside the donors' convex hull: its very high household debt and long fixed-rate mortgages cannot be matched by weighting.
    - The contaminated donors cannot be used.
  - A poor pre-period fit would make the counterfactual unreliable.
- **Our case:** Our placebo-band event study is a "poor man's" version of this logic, and we treat it only as supporting evidence.
- **Follow-up:** "What if you widened the donor pool to non-euro countries?" Then monetary policy differs, which breaks comparability for lending rates. That is a worse trade-off.
- **Refs:** Abadie, Diamond & Hainmueller (2010).

### C10. Macroprudential decisions respond to risk, so they are endogenous. How does the literature identify their effects?
- **Concept:** If authorities tighten *because* risks are rising, outcomes would have moved anyway, which biases naive estimates. Identification needs variation in exposure that is unrelated to the decision.
- **Answer:**
  - Country-level regressions of credit on policy changes suffer reverse causality: policy reacts to credit and expected credit.
  - The leading solution uses bank-level heterogeneity in exposure to a common policy change. Banks differ in how much the rule binds them, which is plausibly unrelated to borrower demand. Firm × time fixed effects then absorb demand.
  - Jiménez, Ongena, Peydró & Saurina (2017) use Spanish dynamic provisioning and credit-register data this way. They find countercyclical buffers smooth credit supply, especially in bad times.
  - Basten (2020) exploits banks' different mortgage specialisation and capital cushions under the Swiss sectoral CCyB.
  - Cross-country panels instead use policy indices with controls, accepting weaker identification.
- **Our case:**
  - A normal-times buffer is *less* endogenous than a classic CCyB, because it was not triggered by credit growth. That helps interpretation.
  - Our country-level design still cannot separate supply from demand. A Dutch bank-level study (exposure to Dutch versus foreign assets, capital headroom) would be the next step.
- **Follow-up:** "Which Dutch banks would be most affected?" Domestic lenders with lower headroom face nearly the full 2%. Internationally diversified banks face a lower weighted CCyB. That is a natural treatment-intensity measure.
- **Refs:** Jiménez, Ongena, Peydró & Saurina (2017); Basten (2020); Cerutti, Claessens & Laeven (2017).

---

## Rapid-fire facts (if asked)

**The decision**

| Item | Value |
|---|---|
| CCyB path | 0 → 1% (ann. 25/27 May 2022, binding 25 May 2023) → 2% (ann. 31 May 2023, binding 31 May 2024) |
| CCyB amount | ≈ €3.3bn + €3.4bn |
| O-SII from 31 May 2024 | ING 2%, Rabobank 1.75%, ABN AMRO 1.25%, BNG and de Volksbank 0.25% |
| 2020 relief | SRB 3% → 2.5/2/1.5%; €8bn with the floor postponement; up to €200bn of lending |
| Calibration | peak losses €12bn → €6bn → €150bn |

**Indicators at the decisions**

| Item | Value |
|---|---|
| Credit-to-GDP gap | −33pp (2021Q4), −47pp (2022Q4) |
| Household debt-service ratio | 14.6% (22Q1), the lowest since 2005 |
| Household debt/GDP | 107% (22Q1); euro area 57.7% |
| House prices | +19% y/y (22Q1); real −9% (22Q2–23Q2) |

**Banks and borrowers**

| Item | Value |
|---|---|
| CET1 (sector) | 17.7% (end-2021), 16.3% (end-2022) |
| Net interest income | +6.7% in 2022 |
| Headroom, four banks | €42.3bn (2021), €35.5bn (2022) |
| CCyB share of headroom | ≈ 8% / ≈ 19% (upper bounds) |
| Bank credit 2022Q1–2026Q1 | NL +16.6%, euro area +7.9% |

## Answering rules for the session
- **Unknown fact:** "We haven't measured that; our evidence is…". Never guess a number.
- **Causality:** say "no sign of contraction", never "had no effect".
- **Strongest counter-evidence first:** housing in 2022, and the 2021 baseline. Concede, then explain.
- **Brevity:** one speaker per question, about 45 seconds, then stop.
