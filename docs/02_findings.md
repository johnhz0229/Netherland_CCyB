# Findings (as of 2026-10-01; Stage 1–2 update same day)

All numbers can be reproduced from `data/` with the scripts in `code/`. Data come from BIS statistics (data.bis.org). Policy facts come from DNB primary documents.

---

## 0. Policy facts (verified against DNB sources)

| Date | Event | Source |
|---|---|---|
| 2016–2021 | Dutch CCyB at 0%; nothing to release during COVID | DNB |
| Feb 2022 | DNB publishes its new CCyB framework (positive neutral, 2% in normal times) | DNB Analytical framework (Feb 2022) |
| 2022-05-25 | 0→1% announced, effective 2023-05-25; about €3.3bn additional CET1 | DNB press release 2022 |
| 2023-05-31 | 1→2% announced, effective 2024-05-31; about €3.4bn additional CET1 | DNB press release 2023 |
| 2024 – 2026-09-17 | Repeated decisions to maintain 2% | DNB news (latest 2026-09-17) |

**DNB framework**
- Four phases:
  - recovery: 0%
  - normal: 2%, built up by 1pp per year over two years
  - elevated risk: >2%
  - materialisation: release
- Calibration:
  - peak accumulated losses (PAL) 2007–2016 ≈ €12bn
  - 2% ≈ €6bn of releasable CET1
  - enough to support up to about €150bn of lending
- Guided discretion rather than a mechanical rule.

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
  - 2021Q4: 17.7% (EU average 15.7%)
  - end-2022: 16.3%
- Stress tests:
  - FSR 2022: CET1 falls from 16.6% to 13.3%.
  - FSR 2023: the four large banks fall from 15.2% to 11.5%.
  - Both remain above the 8% minimum.
- Net interest income: +6.7% in 2022, 67.7% of income (FSR 2023).
- DNB lowered O-SII buffers because banking-sector assets/GDP had fallen from about 400% to about 280%. Timing and size: see §0a.

---

## 0a. Systemic buffers, COVID relief and the net effect of the CCyB (Stage 2, new)

**Verification level.** In this sandbox, direct fetches of dnb.nl, esrb.europa.eu, ecb.europa.eu and bis.org are blocked by the egress policy. The facts below were confirmed through search-engine extracts of the primary pages linked. Before the slides are final, open each link once in a browser.

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
- DNB's March 2020 press release: *"The reduction in the buffer requirements will be compensated by a gradual increase in the countercyclical capital buffer to 2% of Dutch risk-weighted exposures. In effect, the total buffer requirement for these banks will eventually return to the current level."*
- So the 2% CCyB was pre-announced two years before the 2022 framework. In part it **re-composes the capital stack**, moving capital from a non-releasable systemic buffer into a releasable cyclical one. This strengthens the normalisation thesis, and slides 6, 8 and 15 should say it.
- Capital freed in March 2020: DNB's press release says **€8bn** in total; the ESRB COVID page says **€5bn** for the systemic-buffer cut. Both figures appear in the sources. Our reading, **not confirmed**, is that the €8bn also includes the postponed mortgage risk-weight floor announced the same day. On slides, use "€5bn from the systemic-buffer cut (ESRB)" or cite DNB's €8bn as "combined measures".
- 2023 decision: DNB states that raising the CCyB and lowering the O-SII buffers *"will cause a limited increase in the net capital requirements for the Dutch banking sector"* ([DNB 2023 CCyB press release](https://www.dnb.nl/en/sector-news/supervision-2023/dnb-raises-countercyclical-capital-buffer-ccyb-from-1-0-to-2-0/)).
  - **Own calculation:** the O-SII cuts valued at end-2022 total RWA (§3) come to about **€2.7bn** (ING €1.7bn, Rabobank €0.6bn, ABN AMRO €0.3bn, de Volksbank €0.1bn; BNG excluded).
  - Against the €3.4bn second CCyB step, that is a **net increase of about €0.7bn**. This is approximate: the O-SII applies to global consolidated RWA, the CCyB only to Dutch exposures.
- **Bank-level asymmetry.** Over 2020–24, ING's systemic buffer fell by 1.0pp (3%→2%), Rabobank's by 1.25pp and ABN AMRO's by 1.75pp. The 2% CCyB applies only to Dutch exposures.
  - For a bank whose RWA is largely abroad, such as ING, the CCyB adds much less than 2pp to its overall requirement. ING reported a fully loaded CCyB of 47bp in its 2022 SREP release ([ING 2022 SREP](https://www.ing.com/Newsroom/News/Press-releases/ING-Group-2022-SREP-process-completed.htm); confirmed through a search extract).
  - So for ING the net combined requirement fell over 2020–24, while for domestic banks it roughly returned to the pre-COVID level, as DNB intended.

**Other Dutch and euro-area COVID capital relief (2020)**
- 17 Mar 2020: DNB postponed the mortgage risk-weight floor (Art. 458 CRR). It was originally notified in Jan 2020 to start around Sep 2020, and finally took effect on **1 Jan 2022**. Sources: [ESRB opinion on the Dutch Art. 458 measure (2024)](https://www.esrb.europa.eu/pub/pdf/other/esrb.opinion241028_report~29d9b314d3.en.pdf); [DNB, "Risk weight measure on bank mortgage loans expires" (2026)](https://www.dnb.nl/en/sector-news/supervision-2026/q2/risk-weight-measure-on-bank-mortgage-loans-expires/). The second source also means the floor itself has since expired; check the date before saying "currently in force" on any slide.
- 12 Mar 2020 (ECB Banking Supervision, all significant banks, including the Dutch ones):
  - banks could operate temporarily below P2G, the capital conservation buffer and the LCR
  - P2R composition was front-loaded, so only 56.25% of it had to be met with CET1
  - the ECB estimated the relief at €120bn of CET1 across the euro area
  - Source: [ECB press release, 12 Mar 2020](https://www.bankingsupervision.europa.eu/press/pr/date/2020/html/ssm.pr200312~43351ac3ac.en.html).
- The Dutch CCyB stayed at 0% throughout 2020, so there was nothing to release ([DNB, Sep 2020](https://www.dnb.nl/en/sector-news/2020/dnb-leaves-countercyclical-buffer-unchanged-at-0-september-2020)).

**Macro facts**
- GDP regained its pre-COVID (2019Q4) level in **2021Q3** (+1.9% q/q). By end-2021 it was almost 3% above end-2019. Source: CBS, reported in [NL Times, 16 Nov 2021](https://nltimes.nl/2021/11/16/dutch-economy-back-pre-covid-level-3rd-quarter); CBS background: [CBS, 2022 week 8](https://www.cbs.nl/en-gb/news/2022/08/dutch-economy-shows-faster-pandemic-recovery-than-neighbouring-countries).
  - Q2 2021 was almost back at the end-2019 level, but the 2021Q1 lockdown caused a dip.
- 2022 inflation: **HICP 11.6%** (annual average); national CPI 10.0%. Source: [CBS, "Inflation rate 10.0 percent in 2022"](https://www.cbs.nl/en-gb/news/2023/02/inflation-rate-10-0-percent-in-2022). Use HICP on slides, because it is the euro-area-comparable measure.

---

## 1. Test 1: the credit-to-GDP gap (`figures/fig1_nl_credit_gap.png`)

**Method**
- HP filter with λ = 400,000 (quarterly data), sample from 1961Q1.
- The one-sided (recursive) HP filter replicates the official BIS gap with a mean absolute error of 0.00002pp. So the BIS gap is itself a one-sided measure.
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
- [ ] Bank-level event study / DiD (Stage 3, optional). The ECB data API is blocked in this sandbox too.
- [x] Tier-C literature verified. See `03_references.md`.
- [ ] **New:** BIS data refresh is still pending. `code/fetch_data.py` is hardened but cannot reach stats.bis.org from this environment; run it once with network access.
- [ ] **New:** a source for "long fixed-rate mortgages slow rate pass-through" (§2) is still needed.
- [ ] **New:** confirm on the DNB page whether the €8bn (2020) includes the risk-weight-floor postponement.

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
