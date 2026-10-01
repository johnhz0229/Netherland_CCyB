# Prompt for Claude Code

(Start Claude Code inside the `ccyb_nl/` folder and paste everything below the line.)

---

I'm preparing a group presentation on the Dutch CCyB increases. This folder already contains the groundwork: storyline, analysis results, a data snapshot, reproducible code and two figures.

First, read these files in full:
- `CLAUDE.md`
- `docs/01_storyline.md`
- `docs/02_findings.md`
- `docs/03_references.md`

Then work through the stages below. After each stage, stop and give me a short report: what you did, what you found, and which conclusions changed. Wait for my go-ahead before continuing.

## Stage 1: Reproduce and refresh

1. Install dependencies and run `code/gap.py`, `code/fig1.py` and `code/other.py` in that order. Confirm that the output matches `docs/02_findings.md`.
2. Run `code/fetch_data.py` to re-download the data from the BIS API.
   - The script has never been run with network access; fix it if needed.
   - Compare the fresh data with the snapshot and list any differences.
   - If BIS has revised the series, update the results and note the revision in the findings.

## Stage 2: Close the open items (`docs/02_findings.md` §6)

Search primary sources (DNB, ECB, ESRB, BCBS, CBS, bank annual reports) and resolve each item:

- Timing and size of DNB's O-SII/SRB cuts, and the net effect on total capital requirements together with the CCyB increase.
- Dutch capital-release measures during COVID.
- The quarter in which Dutch GDP regained its pre-COVID level; 2022 HICP inflation.
- For ING, Rabobank, ABN AMRO and de Volksbank at end-2021 and end-2022:
  - CET1 ratio
  - total RWA
  - MDA trigger (or overall CET1 requirement)

  Use these to replace the assumptions in `other.py`, then recompute the CCyB's share of capital headroom.
- Verify every tier-C reference in `docs/03_references.md`: authors, year, title, outlet. Flag anything you cannot verify and keep it out of the slides.

Write every conclusion back into the findings, with a source link.

## Stage 3 (optional, ask me first): Strengthen the impact analysis

- If ECB MIR (new mortgage/corporate lending rates) and BSI (loan growth) country data are available, run an event study: the Netherlands vs euro-area countries.
  - Event windows: the two announcement dates and the two effective dates.
  - Plot the coefficients.
  - Discuss parallel trends and control-group contamination (France, Germany and Belgium raised their CCyBs over the same period).
- Present the results only as supporting evidence for "no sign of contraction".

## Stage 4: Build the slides

- Build an English 16:9 `.pptx` with python-pptx, following the 22-slide structure in `docs/01_storyline.md`.
- Use action titles (the title states the conclusion) and one core message per slide.
- Figures:
  - Use the figures in `figures/`, redrawn in a consistent style if needed.
  - Add two new figures: a capital-stack diagram (slide 3) and a Dutch timeline (slide 8).
  - Put the data source under every figure.
- Slide 1 (the one-pager) must make sense on its own.
- Slide 14 (normalisation vs overheating prediction table) is the analytical core of the talk; make it the clearest slide.
- The final slide lists references, verified ones only.
- When done, render every slide to an image and check it. Fix text overflow, overlaps and fonts that are too small.

## Stage 5: Speaker script and Q&A preparation

### Speaker script
- Write English speaker notes for every slide. Also save them to `docs/speech_script.md`.
- Total length: about 25 minutes (roughly 3,200–3,500 words).
- Mark the suggested time per slide and the hand-over points between the two speakers. My default split: I present Part I and the conclusion, my partner presents Part II. Propose a better split if you see one.
- Wherever a concept is used for the first time, explain it in one plain sentence for a non-specialist audience.

### Q&A preparation
Create `docs/qa_prep.md` with about 20 questions a professor of central banking and monetary economics is likely to ask. Focus on **concept explanations, economic reasoning and econometric methodology** rather than facts about the Netherlands.

For each question, give:
- the key concept in one sentence
- a model answer of 4–6 sentences
- how it links to our case
- the most likely follow-up question

Cover at least the following.

**Macroprudential and banking concepts**
- Procyclicality of bank capital and why it amplifies cycles; the difference between microprudential and macroprudential regulation.
- The capital stack: P1, P2R, P2G, CCoB, CCyB, O-SII/SRB. Which layers are usable and which are releasable; what the MDA is; why banks avoid dipping into buffers (stigma, buffer usability).
- Risk-weighted assets and risk weights; how the mortgage risk-weight floor works; the CCyB as a weighted average of exposure-location rates.
- Reciprocity and leakage: cross-border lending, branches, non-bank substitution.
- Why higher capital may not raise lending rates much: Modigliani–Miller and its limits (tax shield, debt overhang, equity-issuance costs); the evidence on loan-pricing effects.
- Positive neutral CCyB vs the gap-based CCyB; how the 2% is calibrated (peak accumulated losses, losses-to-buffer, stress tests).

**Economic reasoning and policy design**
- The Tinbergen rule and assigning instruments to targets: why housing risk goes to borrower-based measures and cyclical risk to the CCyB.
- Rules vs discretion: time inconsistency (Kydland–Prescott), inaction bias, communication and credibility; what "guided discretion" means.
- Interaction between macroprudential and monetary policy: CCyB normalisation during an ECB hiking cycle; one monetary policy for the euro area vs national macroprudential policy.
- Is the CCyB increase a disguised tightening? Explain the difference between a normal-times buffer and a countercyclical tightening.
- Denominator effects: how inflation and nominal GDP growth change debt/GDP and the credit gap.
- Growth-at-Risk: the concept, quantile regression, and how a releasable buffer affects the lower tail.

**Econometrics and measurement**
- How the HP filter works (penalised least squares); why λ = 400,000 for credit cycles (cycle length relative to business cycles, Ravn–Uhlig scaling).
- One-sided vs two-sided filters; the end-point problem; real-time vs quasi-real-time vs ex-post estimates (Orphanides–van Norden).
- Hamilton's (2018) critique of the HP filter (spurious cycles, end-point bias) and how the regression filter works; why h = 8 or h = 20.
- Early-warning indicator evaluation: noise-to-signal ratio, AUROC, type I vs type II errors, and the policymaker's loss function.
- Why the credit gap fails for the Netherlands: structural trend, financial deepening, non-stationarity.
- DiD identification: parallel trends, the no-anticipation assumption, SUTVA/spillovers, contaminated controls; why our naive DiD is not causal.
- Staggered adoption: the Goodman-Bacon decomposition and negative weights in two-way fixed-effects models; Callaway–Sant'Anna as a remedy.
- Event studies: choosing the event date (announcement vs effective date), anticipation effects; why a pre-announced framework can mean a small announcement effect.
- Synthetic control as an alternative identification strategy, and its limits in this setting.
- Endogeneity of macroprudential decisions (policy responds to risk) and how the literature tries to address it, e.g. bank-level exposure heterogeneity as in Jiménez et al. (2017).

Next to each answer, list only references that are verified (or that you have verified).

## Constraints

- Every number must come from `data/`, `docs/02_findings.md`, or a newly cited source. Never invent numbers.
- Everything in English: communication with me, documents, slides and notes.
