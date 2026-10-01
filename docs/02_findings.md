# Findings (as of 2026-10-01)

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
- DNB lowered O-SII buffers because banking-sector assets/GDP had fallen from about 400% to about 280% (exact amounts to be verified).

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

**Inputs and assumptions**
- DNB: 1% CCyB ≈ €3.3bn. This implies domestic-exposure RWA of about €330bn.
- Assumed overall CET1 requirement excluding the CCyB (P1 + P2R + CCoB + O-SII/SRB): 10%, 11% or 12%.
- Assumed total RWA: €330bn, €600bn or €750bn.
- €330bn is a lower bound. €600–750bn is a rough estimate for the large banks and **needs verification**.

| Date | CET1 | CCyB amount | CCyB as share of headroom (range) |
|---|---|---|---|
| 2021Q4 (1%) | 17.7% | €3.3bn | 6–18% |
| 2022Q4 (2%) | 16.3% | €6.7bn | 14–47% (47% is the extreme case: domestic RWA only and a 12% requirement) |

The full grid is in `data/nl_headroom_grid.csv`.

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

- [ ] Timing and size of DNB's O-SII/SRB cuts, and their net effect together with the CCyB increase.
- [ ] Dutch capital-release measures during COVID.
- [ ] Quarter in which Dutch GDP regained its pre-COVID level; exact 2022 HICP inflation.
- [ ] Total RWA and actual MDA requirements of the large Dutch banks (ING, Rabobank, ABN AMRO, de Volksbank annual reports), to replace the headroom assumptions.
- [ ] Bank-level event study / DiD. This needs ECB MIR/BSI or EBA transparency data; the ECB API was not reachable from the sandbox.
- [ ] Verify the literature marked "unverified" in `03_references.md`.
