# Findings (as of 2026-10-01; Stage 1–2 update same day)

All numbers can be reproduced from `data/` with the scripts in `code/`. Data come from BIS statistics (data.bis.org). Policy facts come from DNB primary documents.

---

## 0. Policy facts (verified against DNB sources)

| Date | Event | Source |
|---|---|---|
| 2016–2021 | Dutch CCyB at 0%; nothing to release during COVID | DNB |
| Feb 2022 | DNB publishes its new CCyB framework (positive neutral, 2% in normal times) | DNB Analytical framework (Feb 2022) |
| 2022-05-25 | 0→1% announced in the FSR (press release dated 27 May 2022), effective 2023-05-25; about €3.3bn additional CET1 | DNB press release 2022 (read directly) |
| 2023-05-31 | 1→2% announced, effective 2024-05-31; about €3.4bn additional CET1 | DNB press release 2023 (read directly) |
| 2023-05-31 | O-SII cuts announced, effective 2024-05-31 | DNB news item 31 May 2023 (read directly) |
| 2024 – 2026-09-17 | Repeated decisions to maintain 2% | DNB news (26 Mar 2026 read directly; 17 Sep 2026 item seen as the latest on dnb.nl) |
| 2026-04-24 | DNB decides not to extend the mortgage risk-weight floor; it expires 30 Nov 2026. DNB says this "underpins the importance of … the current CCyB of 2%" | DNB news item 24 Apr 2026 (read directly) |

**DNB framework**
- Four phases:
  - recovery: 0%
  - normal: 2%, built up by 1pp per year over two years
  - elevated risk: >2%
  - materialisation: release
- Phase names in the framework: 1 recovery, 2 normality, 3 increased risk, 4 materialisation. The build-up is "in principle … at a rate of 1% per year in order to reach the neutral level of 2% after two years".
- Calibration:
  - peak accumulated losses (PAL) 2007–2016 ≈ €12bn
  - 2% ≈ €6bn of releasable CET1
  - enough to support up to about €150bn of lending
- The framework adds that 2% is appropriate *"also taking into account the impact of the buffer reduction in March 2020"*.
- Guided discretion rather than a mechanical rule: *"there is no mechanical link between the indicator values and the level of the CCyB. DNB will take decisions on the basis of guided discretion."*
- ✔ Verified verbatim in the framework PDF (user-supplied copy, 2026-10-01).

**Criteria DNB cited**
- 2022:
  - "cyclical risks are at 'normal' to elevated levels"
  - the economy had recovered from COVID
  - banks are well capitalised
  - no increase in lending rates expected
- 2023:
  - the credit-to-GDP gap shows no excessive credit growth
  - house prices are falling
  - institutional investors' risk appetite is rising
  - concerns about corporate and government debt sustainability
  - banks' position and profitability are robust, partly due to higher rates

**Bank capital**
- CET1 ratio (FSR 2022/2023):
  - 2019Q4: 16.9%
  - 2021Q4: 17.7% (EU average 15.7% in **2021Q3**) ✔ FSR spring 2022, verbatim
  - end-2022: 16.3% ✔ FSR spring 2023 ("average core capital ratio of 16.3%", "in line with the European average")
- Stress tests:
  - FSR 2022: average CET1 of Dutch banks falls from 16.6% to 13.3% ✔
  - FSR 2023: the average CET1 of the four major banks falls by 3.8pp, to 11.5% at end-2025; the starting point printed is 15.2% at end-2022 ✔ (two-column layout; the 15.2% is the stress-test base)
  - Both remain above the 8% minimum.
- Net interest income: +6.7% in 2022, 67.7% of income (FSR 2023) ✔ verbatim.
- DNB lowered O-SII buffers because the banking sector "at the time represented around 400% of GDP" and "fell to 280% of GDP at the end of 2022" (FSR 2023, ✔ verbatim). Timing and size: see §0a.

---

## 0a. Systemic buffers, COVID relief and the net effect of the CCyB (Stage 2, new)

**Verification level (updated after network access was opened).**
- Read directly:
  - DNB press releases of 27 May 2022, 31 May 2023 (CCyB and O-SII), 25 Sep 2020, 26 Mar 2026 and 24 Apr 2026
  - ESRB O-SII notifications of 27 Nov 2020 and 31 May 2023
  - the ESRB COVID-19 measures page
  - the ESRB CCyB table
- DNB PDFs (FSR, CCyB framework) and the DNB 2020 press release could not be downloaded, because the site's bot protection blocks scripted access. Those items rest on search extracts and secondary summaries, as marked.

**History of the systemic buffers of the large Dutch banks (CET1, % of total consolidated RWA)**

| Bank | Until Mar 2020 (SRB) | 17 Mar 2020 decision | O-SII from 29 Dec 2020 | O-SII from 31 May 2024 (decided Jun 2023) |
|---|---|---|---|---|
| ING | 3% | 2.5% | 2.5% | 2.0% |
| Rabobank | 3% | 2.0% | 2.0% | 1.75% |
| ABN AMRO | 3% | 1.5% | 1.5% | 1.25% |
| de Volksbank | — (O-SII 1%) | — | 1.0% | 0.25% |
| BNG | — (O-SII 1%) | — | 1.0% | 0.25% |

Sources:
- 2020 cut: [DNB press release, 17 Mar 2020, "DNB lowers bank buffer requirements to support lending"](https://www.dnb.nl/en/general-news/press-releases-2015-2020/dnb-lowers-bank-buffer-requirements-to-support-lending/) and [ESRB COVID-19 measures, Netherlands](https://www.esrb.europa.eu/home/search/coronavirus/countries/html/esrb.covidpmc_thenetherlands.en.html).
- Conversion to O-SII from 29 Dec 2020 (CRD V): [ESRB notification, 27 Nov 2020](https://www.esrb.europa.eu/pub/pdf/other/esrb.notification20201127_OSII_NL~7c4e3115cf.EN.pdf).
- 2023 cut: [DNB, "DNB adjusts O-SII buffers" (2023)](https://www.dnb.nl/en/sector-news/supervision-2023/dnb-adjusts-o-sii-buffers/) and [ESRB notification, 31 May 2023](https://www.esrb.europa.eu/pub/pdf/other/Esrb.notification230531_OSII_NL~a94ebd83a4.en.pdf).

**Key finding: the CCyB was announced as the replacement for the 2020 systemic-buffer cut.**
- DNB press release, 17 Mar 2020 (✔ read verbatim, user-supplied copy): *"Combined, these measures will free up EUR 8 billion in capital. … As the total impact on lending could rise to a maximum of EUR 200 billion, it is paramount that banks use this freed-up capital to support lending, and not to pay dividend or share repurchases. … Once the situation is back to normal, DNB will compensate the systemic buffers reduction by gradually increasing the countercyclical capital buffer to 2% of Dutch risk-weighted exposures. This will bring back the capital requirements to the current level … This compensatory arrangement will work out more or less capital-neutral for the three large banks involved, and the same effect is envisaged for the other banks."*
- **Primary confirmation (read directly):**
  - ESRB notification, 27 Nov 2020: *"The reduction of the systemic buffers went hand in hand with DNB's outspoken intention to build up a 2% countercyclical capital buffer (CCyB) in the future. This would bring the capital level of these three banks back to roughly their original levels. In other words, the decision was prompted by the desire to keep the current level of the capital requirement constant, but modify the composition."*
  - ESRB notification, 31 May 2023: *"The policy actions in 2020 shifted DNB's buffer requirement composition – which heavily focussed on structural buffers – to a more balanced mix and enlarged the amount of releasable capital at DNB's disposal."*
  - DNB press release, 27 May 2022: *"Because it is important to rebuild buffers after a crisis, DNB also immediately expressed its intention on 17 March 2020 to apply a 2% CCyB in the Netherlands in time."* and *"The CCyB brings the amount of 'fixed' and releasable buffer capital into better balance."*
- So the 2% CCyB was pre-announced two years before the 2022 framework. In part it **re-composes the capital stack**, moving capital from a non-releasable systemic buffer into a releasable cyclical one. This strengthens the normalisation thesis, and slides 6, 8 and 15 should say it.
- Capital freed in March 2020: **€8bn for the two measures combined** (systemic-buffer cut plus postponement of the mortgage risk-weight floor), supporting up to €200bn of lending. ✔ DNB press release, verbatim (above).
  - The "€5bn" figure from a search extract **does not appear** on the ESRB page. It is dropped.
- 2023 decision, now verified in two primary sources:
  - Klaas Knot, introductory statement to the Standing Parliamentary Committee for Finance, **7 June 2023** (✔ verbatim): *"Taken together, the raising of the CCyB and the lowering of the O-SII will cause a limited increase in the net capital requirements for the Dutch banking sector. The combination of these two changes will nevertheless have different impacts on individual banks."*
  - FSR spring 2023 (✔ verbatim): *"Although the impact on each bank differs, the combination of these measures slightly increases the capital requirements for the banking sector as a whole."*
  - The sentence is not in the 31 May 2023 CCyB press release.
  - **Own calculation:** the O-SII cuts valued at end-2022 total RWA (§3) come to about **€2.7bn** (ING €1.7bn, Rabobank €0.6bn, ABN AMRO €0.3bn, de Volksbank €0.1bn; BNG excluded).
  - Against the €3.4bn second CCyB step, that is a **net increase of about €0.7bn**. This is approximate: the O-SII applies to global consolidated RWA, the CCyB only to Dutch exposures.
- **Bank-level asymmetry.** Over 2020–24, ING's systemic buffer fell by 1.0pp (3%→2%), Rabobank's by 1.25pp and ABN AMRO's by 1.75pp. The 2% CCyB applies only to Dutch exposures.
  - For a bank whose RWA is largely abroad, such as ING, the CCyB adds much less than 2pp to its overall requirement. ING reported a fully loaded CCyB of 47bp in its 2022 SREP release ([ING 2022 SREP](https://www.ing.com/Newsroom/News/Press-releases/ING-Group-2022-SREP-process-completed.htm); confirmed through a search extract).
  - So for ING the net combined requirement fell over 2020–24, while for domestic banks it roughly returned to the pre-COVID level, as DNB intended.

**International comparison: BCBS (2024), d585 (✔ read in full, user-supplied copy)**
- Table 1 lists **17 jurisdictions** with a positive neutral CCyB: 7 BCBS members and 10 non-BCBS EU countries. South Africa is still at the proposal stage.
- Target rates range from 0.5% to 2%. **2% targets:** Netherlands (31 May 2024), Sweden (22 Jun 2023), United Kingdom (5 Jul 2023) and **Poland** (24 Sep 2026). Slide 7 should add Poland.
- Box 2 on the Netherlands: calibrated on historical losses and previous buffer releases, and the switch *"shifted the composition of buffers in the Netherlands, reducing the large predominance of structural buffers and increasing the amount of releasable capital"*.
- The Netherlands and Sweden both used "two steps of 1% over two years".
- **The UK did the same kind of offset:** its rise to a 2% neutral rate was offset by cutting Pillar 2A by 50% of the CCyB increase, with the other 50% offset through lower resolution requirements. Our "partly a swap" reading is therefore not unusual internationally. Good for slide 7 or 19.

**Latest DNB decision, 17 Sep 2026 (✔ read verbatim, user-supplied copy)**
- 2% maintained, *"above the 0% implied by the Basel buffer guide"*, because DNB *"bases its decision on a broader assessment instead of only the credit-to-GDP gap"*. This is the puzzle of slide 1, in DNB's own words, still true in 2026.
- *"Bank lending growth in particular has been relatively strong, suggesting no signs of constraints in bank credit supply."* DNB's own wording matches our "no sign of contraction" (slide 17).
- Property prices +7% in real terms over two years (residential and commercial). Next reassessment in 2026Q4.

**Other Dutch and euro-area COVID capital relief (2020)**
- 17 Mar 2020: DNB postponed the mortgage risk-weight floor (Art. 458 CRR). It was originally notified in Jan 2020 to start around Sep 2020, and finally took effect on **1 Jan 2022**. It was extended twice, most recently in 2024.
  - On 24 Apr 2026 DNB decided not to extend it, so it **expires 30 Nov 2026**. DNB's reason: housing systemic risks "have gradually declined" and banks are less vulnerable.
  - DNB adds that the expiry "underpins the importance of … the current countercyclical capital buffer (CCyB) of 2%". This matters for slide 15: by end-2026 the housing-specific capital tool goes away and the 2% CCyB becomes the main buffer.
  - Sources: [DNB, 24 Apr 2026](https://www.dnb.nl/en/sector-news/supervision-2026/q2/risk-weight-measure-on-bank-mortgage-loans-expires/) (read directly); [ESRB opinion on the Dutch Art. 458 measure (2024)](https://www.esrb.europa.eu/pub/pdf/other/esrb.opinion241028_report~29d9b314d3.en.pdf).
- 12 Mar 2020 (ECB Banking Supervision, all significant banks, including the Dutch ones):
  - banks could operate temporarily below P2G, the capital conservation buffer and the LCR
  - P2R composition was front-loaded, so only 56.25% of it had to be met with CET1
  - the ECB estimated the relief at €120bn of CET1 across the euro area
  - Source: [ECB press release, 12 Mar 2020](https://www.bankingsupervision.europa.eu/press/pr/date/2020/html/ssm.pr200312~43351ac3ac.en.html).
- The Dutch CCyB stayed at 0% throughout 2020, so there was nothing to release ([DNB, Sep 2020](https://www.dnb.nl/en/sector-news/2020/dnb-leaves-countercyclical-buffer-unchanged-at-0-september-2020)).

**Macro facts**
- GDP regained its pre-COVID (2019Q4) level in **2021Q3** (+1.9% q/q). By end-2021 it was almost 3% above end-2019. Source: CBS, reported in [NL Times, 16 Nov 2021](https://nltimes.nl/2021/11/16/dutch-economy-back-pre-covid-level-3rd-quarter); CBS background: [CBS, 2022 week 8](https://www.cbs.nl/en-gb/news/2022/08/dutch-economy-shows-faster-pandemic-recovery-than-neighbouring-countries).
  - Q2 2021 was almost back at the end-2019 level, but the 2021Q1 lockdown caused a dip.
- ECB first rate hike: **21 July 2022, +50bp** on all three key rates ([ECB monetary policy decision, 21 Jul 2022](https://www.ecb.europa.eu/press/pr/date/2022/html/ecb.mp220721~53e5bdd317.en.html), read directly).
- 2022 inflation: **HICP 11.6%** (annual average); national CPI 10.0%. Source: [CBS, "Inflation rate 10.0 percent in 2022"](https://www.cbs.nl/en-gb/news/2023/02/inflation-rate-10-0-percent-in-2022). Use HICP on slides, because it is the euro-area-comparable measure.

---

## 1. Test 1: the credit-to-GDP gap (`figures/fig1_nl_credit_gap.png`)

**Method**
- HP filter with λ = 400,000 (quarterly data), sample from 1961Q1.
- The one-sided (recursive) HP filter replicates the official BIS gap with a mean absolute error of 0.00002pp and a maximum of 0.00005pp. After the Stage 1 refresh the official gap is available from 1971, so this now holds over all 221 quarters, 1971Q1–2026Q1. So the BIS gap is itself a one-sided measure.
- We also compute:
  - a two-sided HP gap (ex-post view)
  - the Hamilton (2018) regression filter, with h = 8 and h = 20, p = 4, both full-sample and recursive
- **Limitation:** we use current-vintage data, not real-time vintages, so this is quasi-real-time; GDP revisions are not captured.

| Quarter | Ratio % | Real-time gap (BIS) | Ex-post 2-sided HP | Hamilton h=8 | Hamilton h=20 |
|---|---|---|---|---|---|
| 2007Q4 | 275.7 | −13.4 | −16.9 | −9.9 | +7.4 |
| 2012Q2 | 331.8 | **+16.8** | +20.9 | +12.8 | +49.2 |
| 2016Q1 | 345.8 | −0.6 | **+26.9** | +8.5 | +22.5 |
| 2020Q1 | 322.7 | −33.5 | +3.4 | −17.1 | −43.8 |
| **2022Q1** | 316.0 | **−37.2** | −1.1 | −3.0 | −39.0 |
| **2023Q1** | 291.2 | **−54.6** | −24.4 | −65.9 | −47.4 |
| 2026Q1 | 263.4 | −47.2 | −47.2 | −10.5 | −87.4 |

**Conclusions**
1. At both decision dates, every measure maps to a Basel buffer-guide value of 0%.
2. **Missed signal:** the real-time gap was −13pp on the eve of the GFC, and it was negative throughout 2006–2009.
3. **False signal:** the gap was +17pp in 2012, during a house-price bust and double-dip recession. Falling GDP inflated the ratio, which is the Repullo & Saurina critique.
4. **Revision:** in 2016Q1 the gap read −0.6pp in real time and +26.9pp ex post (cf. Edge & Meisenzahl 2011).
5. Credit/GDP rose from about 47% in 1961 to about 350% in 2015. This strong structural trend distorts the HP trend.

---

## 2. Test 2: other risk indicators (`figures/fig2_nl_indicators.png`)

Percentiles show where each value sits in the 2005–2019 distribution.

| Indicator | 2005–19 mean | 2007Q4 | 2022Q1 (pctile) | 2023Q1 (pctile) | 2026Q1 |
|---|---|---|---|---|---|
| Household debt/GDP % | 119.0 | 116.0 | 107.1 (0) | 100.4 (0) | 94.6 |
| NFC debt/GDP % | 197.9 | 160.2 | 208.9 (53) | 190.9 (42) | 168.8 |
| DSR, private non-financial % | 32.6 | 28.3 | 30.1 (25) | 28.4 (3) | 26.1 |
| DSR, households % | 18.7 | 18.2 | 14.6 (0) | 13.5 (0) | 13.1 |
| Real house prices, 2010=100 | 95.7 | 111.0 | 129.1 (100) | 121.2 (100) | 133.8 |
| Nominal house prices, y/y % | 1.9 | 5.2 | 19.0 (100) | 0.1 (37) | 5.1 |

**Reading household debt correctly**
- It is low relative to the Netherlands' own history but among the highest in the world.
- Household debt/GDP in 2022Q1 (BIS): CH 124.7, AU 116.0, **NL 107.1**, CA 104.8, DK 97.1, SE 93.1, NO 85.4, GB 83.5, US 75.9, FR 66.0, **euro area 57.7**, DE 54.2.
- The decline in the ratio comes entirely from the denominator. The stock of household debt rose:
  - €910bn in 2019Q4
  - €1,016bn in 2023Q1 (+12%)
  - €1,119bn in 2026Q1 (+23%)
  - over the same periods nominal GDP rose about 22% and 43%
- The low DSR partly reflects long fixed-rate mortgages, which slow the pass-through of rate hikes. This is general knowledge; a source still needs to be found.

**Conclusion:** all credit indicators are cool; only house prices are hot. Household debt is structurally high but is not building up cyclically.

---

## 3. Test 3: banks' capacity to absorb the buffer (CET1 headroom)

**Updated in Stage 2: actual bank data replace the assumptions.** Inputs are in `data/nl_bank_capital.csv`, which also lists the source for every cell. Results are in `data/nl_headroom_actual.csv`.

| Bank | CET1 2021 | RWA 2021 €bn | Req./MDA 2021 | CET1 2022 | RWA 2022 €bn | Req./MDA 2022 |
|---|---|---|---|---|---|---|
| ING | 15.9% | 313.1 | 10.51% | 14.5% | 331.5 | 10.71% |
| Rabobank | 17.4% | 211.9 | 10.00% ¹ | 16.0% | 240.4 | 10.10% |
| ABN AMRO | 16.3% | 117.7 | 9.6% | 15.2% | 128.6 | 9.7% |
| de Volksbank | 22.7% | 14.0 | 9.41% ² | 20.3% | 15.3 | 9.41% ² |
| **Sum / RWA-weighted** | **16.6%** | **656.7** | | **15.3%** | **715.8** | |

¹ Implied by Rabobank's statement that its CET1 ratio of 17.4% was "740bp above the MDA trigger".
² Own derivation: P1 4.5% + P2R-CET1 1.41% + CCoB 2.5% + O-SII 1.0%. The P2R-CET1 of 1.41% is from the Pillar 3 report (= 56.25% × 2.5% P2R). The NL CCyB was 0% at both dates. **Flag as derived.**

Notes on the requirement column:
- ING's 2022 figure is the fully loaded requirement for 2022, phased in during the year.
- ABN AMRO's figures are MDA triggers excluding the AT1 shortfall.
- Requirements include foreign CCyBs but not the Dutch CCyB, which became binding only in May 2023 and May 2024. So the headroom is measured *before* the Dutch CCyB, which is the right base.

Sources (links in `data/nl_bank_capital.csv` source column; documents):
- ING: [ING 2021 SREP release](https://www.globenewswire.com/news-release/2022/02/03/2378106/0/en/ING-Group-2021-SREP-process-completed.html), [Form 20-F 2022](https://www.sec.gov/Archives/edgar/data/1039765/000162828023007425/ing-20221231.htm), [20-F 2021](https://www.sec.gov/Archives/edgar/data/0001039765/000156276222000122/ing20f2021.htm)
- Rabobank: [Annual Report 2022 key figures](https://media.rabobank.com/m/4daed9a2b72c970e/original/Annual-Report-Key-Figures-2022-EN.pdf), [Pillar 3 2022](https://media.rabobank.com/m/2bed51e529b32a6e/original/Pillar-3-Year-Report-2022-EN.pdf), [Investor presentation FY2021](https://media.rabobank.com/m/c6e3140f411b46c/original/Investor-Presentation-FY-2021.pdf)
- ABN AMRO: [Q4 2021 report](https://assets.ctfassets.net/1u811bvgvthc/3aF00xJGYcPJeXjYRsGngv/8d8bca5ff42cc84d7d8b521bd6afc847/ABN_AMRO_Bank_Quarterly_Report_fourth_quarter_2021.pdf), [Q4 2022 report](https://assets.ctfassets.net/1u811bvgvthc/3plS4djgLKLqbnuNbP3NvJ/a809cd9a5e248f0995828af7cda7421e/ABN_AMRO_Bank_Quarterly_Report_fourth_quarter_2022.pdf)
- de Volksbank: [Full-year Financial Report 2022](https://corporate.asnbank.nl/assets/files/jaarcijfers/Full-Year-Financial-Report-2022.pdf), [Pillar 3 2021](https://corporate.asnbank.nl/assets/files/jaarcijfers/De-Volksbank-Pillar-3-Report-2021.pdf)

**Result**

| Date | Headroom over req./MDA, 4 banks | CCyB amount (DNB, sector-wide) | CCyB as share of headroom |
|---|---|---|---|
| 2021Q4 (1% step) | €42.3bn | €3.3bn | **≈ 8%** |
| 2022Q4 (cumulative 2%) | €35.5bn | €6.7bn | **≈ 19%** |

- The share is an **upper bound**: the numerator covers the whole Dutch sector, while the denominator covers only the four banks.
- The new figures sit inside the old assumption range (6–47%), at the low end for 2022. The 47% extreme case is ruled out: it assumed domestic RWA of only €330bn, but actual total RWA was €716bn.
- Headroom fell from €42bn to €36bn mostly because RWA rose (Rabobank +€28.5bn; ING cites Russia downgrades, FX and the mortgage risk-weight floor) and because of distributions. The CCyB was not the cause; it was not yet binding.
- The old assumption grid stays in `data/nl_headroom_grid.csv` as a sensitivity check.
- The RWA-weighted CET1 of the four banks (16.6%, 15.3%) is slightly below DNB's sector figures (17.7%, 16.3%) because of differences in sample and basis.
- **Slide wording:** "The full 2% buffer absorbs at most about a fifth of the large banks' CET1 headroom."

---

## 4. Test 4: effect on lending (descriptive)

BIS data on bank credit to the private non-financial sector, in national currency:

| | NL | Euro area | DE | FR | BE | AT |
|---|---|---|---|---|---|---|
| y/y 2023Q2 | 0.6 | 1.7 | 3.5 | 2.5 | 3.3 | 3.1 |
| y/y 2024Q2 | 3.0 | 0.3 | 0.4 | 0.0 | 3.1 | −0.1 |
| y/y 2026Q1 | 6.3 | 3.2 | 1.5 | 1.2 | 4.9 | 1.5 |
| Index 2026Q1 (2022Q1=100) | **116.6** | 107.9 | 108.2 | 104.9 | 113.3 | 106.9 |

**Naive difference-in-differences** (NL minus euro area, average q/q growth):
- before: −0.54pp
- after: +0.42pp
- DiD: +0.96pp per quarter

**This is not causal.**
- The control countries were also raising their CCyBs over the same period (FR, DE, BE).
- The Netherlands was deleveraging beforehand, so parallel trends fail.
- Rate hikes were a common shock.

**Defensible wording:** "no sign that the CCyB constrained lending", consistent with DNB's expectation of no increase in lending rates.

### 4b. Stage 3: event study with ECB MIR/BSI data (`code/event_study.py`, `figures/fig3_event_study.png`)

**Data**
- ECB Data Portal, monthly, 2019-01 to 2026-08, 20 euro-area countries:
  - MIR new-business composite cost of borrowing for house purchase and for NFCs
  - BSI annual growth of MFI loans to households and NFCs, adjusted for sales and securitisation
- Cached in `data/ecb_mir_bsi.csv`.

**Design**
- Two-way fixed-effects event study: country FE, month FE, and NL × 3-month event-time bins from −24 to +47 months around the first announcement (May 2022); reference = months −3..−1.
- The four policy dates collapse to three distinct months:
  - May-22: 1% announced
  - **May-23: 1% binding and 2% announced, in the same week**
  - May-24: 2% binding

  So the second announcement and the first effective date cannot be separated.
- Inference: one treated unit, so we use a permutation test, re-running the regression with each control as a fake treated unit.

**Controls**
- "All": 19 euro-area countries.
- "Clean": **AT, FI, IT, MT, LU**, the countries with no CCyB change in 2021–2025 according to the ESRB CCyB table (`data/esrb_ccyb_rates.xlsx`).
- Every other euro-area country raised its CCyB over the window (e.g. FR 0.5% Apr-23 and 1% Jan-24, DE 0.75% Feb-23, BE 0.5% Apr-24 and 1% Oct-24, IE up to 1.5% Jun-24). Including them biases the NL effect towards zero.

**Results** (`data/event_study_summary.csv`, `data/event_study_short_windows.csv`, `data/event_study_coefs.csv`)

| Outcome | NL avg post coef. (all / clean) | Pre-trend avg (all / clean) | Permutation rank of NL, \|post\| (all / clean) |
|---|---|---|---|
| Mortgage rate (pp) | −0.08 / −0.00 | 0.03 / 0.10 | 18 of 20 / 6 of 6 |
| NFC lending rate (pp) | −0.02 / +0.21 | 0.02 / 0.16 | 19 of 19 / 5 of 6 |
| Household loan growth (pp) | **+2.52 / +5.18** | −0.06 / −0.43 | 8 of 20 / 2 of 6 |
| NFC loan growth (pp) | +2.57 / +1.75 | 1.33 / −1.40 | 11 of 20 / 6 of 6 |

Short windows, 6 months after vs 6 months before each date (NL minus controls, pp):
- Rates move between −0.25 and +0.37pp. These are small next to the placebo range.
- Household loan growth is positive at all three dates.
- NFC loan growth is −3.2pp at May-22, then positive at the two later dates.

**Reading**
1. **Lending rates:** NL is indistinguishable from the controls. Its coefficients are among the *smallest* in absolute value (rank 18/20 and 19/19), and the path stays inside the placebo band throughout. There is no sign of a pricing effect, which is consistent with Basten (2020)'s small pricing effects and with DNB's own expectation.
2. **Lending volumes:**
   - Dutch household loan growth rose *relative to* the controls after 2022 (+2.5pp vs all, +5.2pp vs clean; flat pre-trend). Against the clean controls it leaves the placebo band after about 12 months.
   - NFC loan growth has a visible pre-trend (±1.3–1.4pp), so parallel trends fail there and the NFC result is uninformative.
3. **What it does *not* show:** a causal effect.
   - With one treated country, rates are confounded by mortgage-market structure. Dutch mortgages have long fixed-rate periods, so new-business rates respond differently to ECB hikes.
   - Household growth is confounded by the Dutch housing-market rebound (real house prices +10% y/y in 2026Q1 according to DNB's Mar-2026 release).
   - The "all" controls are contaminated by their own CCyB increases; the "clean" group is small (5) and structurally different (IT, AT, FI, MT, LU).
4. **Slide wording:** "Event-study evidence: Dutch lending rates moved in line with euro-area peers and household credit grew faster. No sign of contraction around any of the three CCyB dates." Present it only as supporting evidence.

---

## 5. Core interpretation: the normalisation hypothesis

| Prediction | Normalisation | Overheating response | Evidence |
|---|---|---|---|
| Link to cyclical indicators | None | Rises with them | Gap, DSR and household debt/GDP all falling ✓ |
| Path | +1pp per year, stop at 2% | Follows risk | 2022→1%, 2023→2%, held since ✓ |
| 2023: house prices falling, rates jumping | Raise anyway | Pause | Raised ✓ |
| 2024–26: house prices rising again | Stay at 2% | Raise further | Held at 2% ✓ |

- **Strongest counter-evidence:** house prices +19% y/y in 2022Q1.
- **Response:** housing risk is handled by borrower-based measures and the mortgage risk-weight floor. The CCyB is not the assigned instrument for it.

---

## 6. Open items / to verify

- [x] Timing and size of the O-SII/SRB cuts and the net effect with the CCyB. See §0a: 2020 SRB cut explicitly to be compensated by the 2% CCyB; 2023 O-SII cut ≈ €2.7bn vs CCyB +€3.4bn → net ≈ +€0.7bn (own calc; DNB: "limited increase").
- [x] Dutch COVID capital relief. See §0a: SRB cut (€5bn, ESRB; DNB headline €8bn combined), risk-weight floor postponed to 2022, ECB P2G/CCoB/P2R relief.
- [x] GDP back above pre-COVID in 2021Q3; 2022 HICP 11.6% (CPI 10.0%).
- [x] Bank CET1/RWA/MDA for ING, Rabobank, ABN AMRO and de Volksbank. See §3; the de Volksbank requirement is derived (flagged).
- [x] Country-level event study (Stage 3), see §4b. A bank-level design (EBA transparency data) remains possible future work.
- [x] Tier-C literature verified. See `03_references.md`.
- [x] BIS data refresh done after network access was opened: no revisions, no new quarter (2026Q2 not yet published). See §7.
- [ ] **New:** a source for "long fixed-rate mortgages slow rate pass-through" (§2) is still needed.
- [x] The €8bn (2020) covers the systemic-buffer cut and the risk-weight-floor postponement combined (§0a).
- [x] DNB FSR 2022/2023, the CCyB framework, the 2020 press release, the Knot speech (7 Jun 2023), the 17 Sep 2026 decision and BCBS d585 were supplied by the user and read in full. All tier-A numbers are confirmed (§0, §0a).

---

## 7. Revision log

**2026-10-01, Stage 1**
- All three scripts reproduce §1–§5 exactly. The one-sided HP replicates the BIS gap with MAE 2.4e-05pp.
- BIS refresh **not possible**: stats.bis.org (and data.bis.org) return HTTP 403 from the sandbox egress proxy. **No revision check was possible; the snapshot of 2026-10-01 stands.**
- `fetch_data.py` was rewritten to write to `data/fresh/`, diff against the snapshot, send an SDMX-CSV Accept header and retry. The diff logic was tested offline.
- Data issue found: in `data/nl_tc.csv`, column `P` is a copy of the DSR series (`nl_dsr.csv` P), not private-sector debt/GDP. It is unused by all scripts, so no result changes; a refresh will fix it.

**2026-10-01, Stage 2: conclusions that changed**
1. **Headroom:** 6–47% → **≈8% (2021) / ≈19% (2022)** with actual bank data. "Low cost" is confirmed and sharper.
2. **The CCyB is partly a swap, not purely an addition.**
   - DNB said in March 2020 that the 2% CCyB would compensate for the systemic-buffer cut.
   - The 2023 O-SII cut offsets about 80% of the second CCyB step (own calc).
   - Slide 6 ("nothing to release") must be nuanced: the CCyB was empty, but DNB *did* release the systemic buffer instead. That is evidence for the thesis that releasable capital was missing.
3. **Calibration benchmark:** the ECB losses-to-buffer paper (De Nora et al. 2025, ECB WP 3061) gives **1.1–1.8%**, not "about 1–1.5%". Slide 7 needs correcting.
4. **Jiménez et al. (2017)** studies Spanish *dynamic provisioning*, not the CCyB. Cite it as evidence on countercyclical capital buffers in general, not on the CCyB.
5. **Couaillier et al. (2022)** is confirmed as ECB WP 2644, later published in JMCB 2025: banks close to their buffers cut lending in COVID. This supports slide 6.

**2026-10-01, after network access was opened**
- **BIS refresh** (`python code/fetch_data.py`, first successful run):
  - all 7 series are identical to the snapshot on overlapping observations, with **no revisions** and no new quarter
  - two differences, both improvements:
    - (a) the official BIS trend and gap are now available from 1971 rather than 2005
    - (b) `nl_tc.csv` column `P` is now the correct private non-financial debt/GDP series (the snapshot bug is fixed)
  - the snapshot was replaced and all scripts re-run; every result in §1–§5 is unchanged
  - the replication now covers 1971–2026 (MAE 0.00002pp, max 0.00005pp)
- **Direct verification corrected three Stage 2 claims:**
  - the "limited increase" quote comes from a DNB parliamentary statement, not the press release
  - "€5bn (ESRB)" is dropped
  - the 1% press release is dated 27 May 2022, though the FSR announcement was on 25 May
- **New fact:** the mortgage risk-weight floor expires 30 Nov 2026.
- **Stage 3** added (§4b): lending rates show no difference from peers, and household credit growth is higher. This supports "no sign of contraction"; it is not causal.

**2026-10-01, user-supplied primary documents (7 files)**
- All Stage-2 items that had rested on search extracts are now verified verbatim: PAL €12bn / €6bn / €150bn; €8bn and €200bn; "compensate … CCyB to 2%"; "limited increase" (Knot, 7 Jun 2023) plus "slightly increases" (FSR 2023); CET1 17.7% / 16.3%; stress tests; NII +6.7%; 400%→280%.
- Additions and precisions:
  - EU average 15.7% refers to 2021Q3
  - FSR 2023 stress test = −3.8pp to 11.5% for the four major banks
  - 2020 release: the swap was meant to be "more or less capital-neutral for the three large banks"
  - BCBS: 17 jurisdictions, and **Poland** also targets 2%; the UK offset its 2% neutral rate against P2A and resolution requirements
  - 17 Sep 2026: DNB itself says lending shows "no signs of constraints in bank credit supply"
- No number in the storyline had to be withdrawn.

**2026-10-01, storyline v4 sources (read directly)**
- **DNB FSR spring 2022:**
  - *"When the systemic risk buffers for ABN AMRO, Rabobank and ING were lowered in March 2020, we also announced our intention to restore the buffers by raising the CCyB. The risk profile is currently dominated by uncertainty caused by the war in Ukraine, but at the same time the robust economic recovery following the COVID-19 pandemic provides grounds for a gradual build-up of the CCyB."*
  - *"In the event of a sharp rise in financial stability risks during the build-up period, we will reconsider the increase."*
  - *"Finally, the overheated housing market calls for further measures. Tax breaks, loose borrowing rules and subsidies for first-time buyers ultimately lead to higher house prices and should therefore be phased out."* So DNB did call housing overheated, and assigned other tools to it.
  - *"The higher interest rates may ultimately have a positive impact on the profitability of financial institutions."*
  - Monetary policy: *"postponing normalisation of monetary policy unnecessarily could lead to financial stability risks … a sudden tightening of financial conditions could also have a negative impact on financial stability."*
  - Risk list: war in Ukraine, energy and commodity prices, high inflation, rapid tightening of financial conditions, debt sustainability, corporate insolvencies, cyber risk, housing and household mortgage debt.
- **DNB FSR spring 2023 risk list:**
  - persistent inflation and tightening financial conditions
  - "very rapid transition from a low-for-long environment"
  - US bank failures and Credit Suisse
  - house prices falling since Aug 2022
  - commercial real estate: about 52% of exposures to be refinanced 2022–24; CRE is 10% of bank assets
- **ECB Macroprudential Bulletin 21 (Apr 2023), Behn, Pereira, Pirovano & Testa:** positive-neutral frameworks in LT, EE, IE, CY and NL; neutral rates CY 0.5%, EE/LT 1.0%, IE 1.5%, NL 2.0%. https://www.ecb.europa.eu/press/financial-stability-publications/macroprudential-bulletin/html/ecb.mpbu202304_01~6eef01bb6a.en.html
- **ECB Macroprudential Bulletin 24 (Jun 2024), Herrera, Scalone & Pirovano:** "a gradual build-up of the buffer and favourable banking sector conditions (e.g. high profitability) limit these economic costs". https://www.ecb.europa.eu/press/financial-stability-publications/macroprudential-bulletin/html/ecb.mpbu202406_01~0ed53a85fa.en.html
- **ECB Macroprudential Bulletin 31 (Aug 2025), Detken, Hempell & Pirovano:**
  - Early CCyB activation "helps monetary policy focus on its primary objective of price stability, thereby largely eliminating the potential for conflict".
  - Box 2: activating buffers during the 2022Q4–2023Q3 tightening "can mitigate implementation costs".
  - It lists the Netherlands among countries with 2022–23 excess-profit bank levies.
  - https://www.ecb.europa.eu/press/financial-stability-publications/macroprudential-bulletin/html/ecb.mpbu20250818_01.en.html

**2026-10-01, Beamer deck: swap waterfall (slide "A swap, not a squeeze"), own calculation**
- 2020 systemic-buffer cut, valued at end-2022 total RWA: ING 0.5pp × €331.5bn = €1.7bn; Rabobank 1.0pp × €240.4bn = €2.4bn; ABN AMRO 1.5pp × €128.6bn = €1.9bn → **≈ €6.0bn**.
  - This is consistent with DNB's €8bn for the systemic cut plus the floor postponement combined.
- 2024 O-SII cut ≈ €2.7bn (§0a). CCyB +€3.3bn (May-23) and +€3.4bn (May-24), DNB's sector-wide figures.
- Cumulative change vs the pre-COVID requirement ≈ **−€2.0bn**, i.e. roughly unchanged or slightly lower. Relative to 2021 it is an increase.
- Caveats on the slide:
  - different exposure bases (consolidated RWA vs Dutch exposures)
  - CCyB amounts include foreign and small banks
  - BNG excluded
  - RWA date is end-2022, not 2020
- Code: `slides/figs.py` (`fig_swap`).

**2026-10-01: CCyB releases in spring 2020 (ESRB CCyB table, `data/esrb_ccyb_rates.xlsx`), used in the speaker script**

Rate in force → new rate, by announcement date:
- Denmark 1.0% → 0% (12 Mar; a pending 1.5%/2.0% was scrapped)
- Norway 2.5% → 1.0% (13 Mar)
- Sweden 2.5% → 0% (16 Mar)
- Iceland 2.0% → 0% (18 Mar)
- Czech Republic 1.75% → 1.0% (26 Mar)
- Belgium: pending 0.5% cancelled (27 Mar)
- Lithuania 1.0% → 0% (31 Mar)
- Germany: pending 0.25% cancelled (31 Mar)
- France 0.25% → 0% (1 Apr; a pending 0.5% was scrapped)
- Ireland 1.0% → 0% (1 Apr)
- Slovakia: pending 2.0% cancelled; 1.5% kept, then cut to 1.0% from Aug 2020

The UK is not in the ESRB table and is therefore not quoted.
