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
- `docs/03_references.md`: sources in three tiers (verified / cited but unread / unverified).
- `data/`: BIS data snapshot (downloaded 2026-10-01) and derived results.
- `code/fetch_data.py`: re-downloads the data from the BIS API. Never run with network access, so check it first.
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
- Network: in the cloud sandbox, stats.bis.org, data-api.ecb.europa.eu, dnb.nl and esrb.europa.eu are blocked by the egress policy; web search works.
