# Project: Netherlands CCyB group presentation (Frankfurt School, MSc FinTech)

## Context
- Two-person group presentation. Assignment: *Prepare a presentation on the country implementation of a change in CCyB.*
- The assignment asks for three things:
  - the economic and financial environment when the authority raised the CCyB
  - the criteria behind the decision and the financial-stability risks it addressed
  - an assessment of the wide-ranging implications
- Country: the Netherlands. DNB announced 0→1% in 2022 and 1→2% in 2023.
- Thesis: **normalisation, not tightening.** See `docs/01_storyline.md`.

## Layout
- `docs/01_storyline.md`: 22-slide storyline (latest).
- `docs/02_findings.md`: all results, numbers, limitations and open items. This is the source of truth for numbers.
- `slides/`: Beamer deck (`main.tex`, minimal academic theme: default Beamer + Palatino/newpx, white, hairline titles, one red accent; 20×11.25cm 16:9). Figures: `python slides/figs.py` (from repo root) → `slides/figs/*.pdf`; build: `cd slides && latexmk -pdf main.tex`. Needs texlive-latex-extra, texlive-fonts-extra (newpx), texlive-pictures; figures use TeX Gyre Pagella. Final PDF copied to `Netherlands_CCyB_slides.pdf`.
- Speaker script (A4, one page per slide: slide on top, SAY / NUMBERS / TERMS / NEXT below): source `docs/speech_script.md` → `python code/make_speaker_script.py` → `cd slides && latexmk -pdf speaker_script.tex` (needs `slides/main.pdf` built first) → `Netherlands_CCyB_speaker_script.pdf`.
- `docs/qa_prep.md`: 22 likely professor questions with model answers and verified references.
- Speakers: Zheng Huang (A: slides 1–8, 17–21), Diego Gutiérrez (B: slides 9–16). Course: Micro- & Macroprudential Management, Master of Financial Technology, Frankfurt School.
- `docs/03_references.md`: sources in three tiers (verified / cited but unread / unverified).
- `data/`: BIS data snapshot (downloaded 2026-10-01) and derived results.
- `code/fetch_data.py`: re-downloads the BIS data to `data/fresh/` and diffs it against the snapshot (`--replace` to overwrite). Last run 2026-10-01: no revisions.
- `code/gap.py`: HP (one-/two-sided) and Hamilton gaps → `data/nl_gaps.csv`.
- `code/fig1.py`: Fig. 1 (credit gap).
- `code/other.py`: indicator dashboard, CET1 headroom (bank data + assumption grid), O-SII offset, lending growth, Fig. 2.
- Run order: `python code/gap.py && python code/fig1.py && python code/other.py`
- Dependencies: numpy, pandas, scipy, matplotlib. The HP filter is implemented with scipy.sparse, so statsmodels is not needed.

## Rules
- Everything in English: communication, documents, slides, speaker notes.
- Every number must come from `data/`, from `docs/02_findings.md`, or from a new source you cite. Never invent numbers.
- Before citing anything marked "unverified" in `03_references.md`, verify it online. If you cannot, drop it or flag it.
- Be careful with causal language. On lending effects, say only "no sign of contraction".
- Headroom now uses bank disclosures (`data/nl_bank_capital.csv`); only the de Volksbank requirement is derived. The old assumption grid is a sensitivity check only.
- Network: full access since 2026-10-01. dnb.nl HTML pages and PDFs reject scripted clients (bot protection); BIS, ECB and ESRB work with curl/requests.
- `code/event_study.py`: Stage 3 event study (ECB MIR/BSI) → `figures/fig3_event_study.png`, `data/event_study_*.csv`.
