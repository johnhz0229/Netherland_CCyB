"""Stage 3: event study, Netherlands vs euro-area countries (supporting evidence only).

Outcomes (ECB Data Portal, monthly):
  mort_rate : MIR composite cost of borrowing for house purchase, new business (MIR.M.cc.B.A2C.AM.R.A.2250.EUR.N), %
  nfc_rate  : MIR composite cost of borrowing for NFCs, new business (MIR.M.cc.B.A2A.A.R.A.2240.EUR.N), %
  hh_growth : BSI MFI loans to households, adjusted for sales/securitisation, annual growth (BSI.M.cc.N.A.A20T.A.I.U2.2250.Z01.A), %
  nfc_growth: same for NFCs (… .2240 …), %

Design: y_ct = a_c + d_t + sum_k b_k * NL_c * 1[event-time bin k] + e_ct
  Event time is measured from the first announcement (May 2022), in 3-month bins from -24 to +45 months;
  bin [-3,-1] is the reference. The later dates (1% effective / 2% announced = May 2023, 2% effective = May 2024)
  fall at k = +12 and +24, so one coefficient path covers all four policy dates.
  Short-window version: average NL-minus-control change 6 months after vs 6 months before each distinct date.
Inference: one treated unit, so standard errors are not meaningful. We use a permutation (placebo) test:
  re-run the same regression assigning treatment to each control country in turn and report the rank of NL.
Controls: 'all' = every euro-area country with data; 'clean' = countries with no CCyB change announced or
  applied 2021-2025 according to the ESRB CCyB table (data/esrb_ccyb_rates.xlsx): AT, FI, IT, MT, LU (LU flat at 0.5%).

Usage: python code/event_study.py           (uses cached data/ecb_mir_bsi.csv if present)
       python code/event_study.py --refresh (re-download from data-api.ecb.europa.eu)
"""
import io
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import requests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
D, FIG = ROOT / 'data', ROOT / 'figures'
CACHE = D / 'ecb_mir_bsi.csv'
EA = ['AT', 'BE', 'CY', 'DE', 'EE', 'ES', 'FI', 'FR', 'GR', 'HR', 'IE', 'IT', 'LT', 'LU', 'LV', 'MT', 'NL', 'PT', 'SI', 'SK']
CLEAN = ['AT', 'FI', 'IT', 'MT', 'LU']
SERIES = {
    'mort_rate': 'MIR/M.{c}.B.A2C.AM.R.A.2250.EUR.N',
    'nfc_rate': 'MIR/M.{c}.B.A2A.A.R.A.2240.EUR.N',
    'hh_growth': 'BSI/M.{c}.N.A.A20T.A.I.U2.2250.Z01.A',
    'nfc_growth': 'BSI/M.{c}.N.A.A20T.A.I.U2.2240.Z01.A',
}
LABEL = {'mort_rate': 'Mortgage rate, new business (pp)', 'nfc_rate': 'NFC lending rate, new business (pp)',
         'hh_growth': 'Household loan growth, y/y (pp)', 'nfc_growth': 'NFC loan growth, y/y (pp)'}
START, EVENT0 = '2019-01', pd.Period('2022-05', 'M')
DATES = {'May-22: 1% announced': '2022-05', 'May-23: 1% effective + 2% announced': '2023-05', 'May-24: 2% effective': '2024-05'}


def download():
    rows = []
    for var, key in SERIES.items():
        url = 'https://data-api.ecb.europa.eu/service/data/' + key.format(c='+'.join(EA))
        r = requests.get(url, params={'format': 'csvdata', 'startPeriod': START, 'detail': 'dataonly'}, timeout=120)
        r.raise_for_status()
        df = pd.read_csv(io.StringIO(r.text))[['REF_AREA', 'TIME_PERIOD', 'OBS_VALUE']]
        df['var'] = var
        rows.append(df)
    out = pd.concat(rows).pivot_table(index=['REF_AREA', 'TIME_PERIOD'], columns='var', values='OBS_VALUE').reset_index()
    out.columns.name = None
    out.to_csv(CACHE, index=False)
    return out


def bins(k):
    """3-month event-time bins; bin b covers months [3b, 3b+2]; reference bin = -1 (months -3..-1)."""
    return np.floor_divide(k, 3)


def twfe(df, y, treated, ref=-1, kmin=-8, kmax=15):
    """OLS with country and month FE; returns {bin: coef} for treated x bin dummies."""
    d = df.dropna(subset=[y]).copy()
    d['b'] = bins(d['k']).clip(kmin, kmax)
    d['tr'] = (d['REF_AREA'] == treated).astype(float)
    X = [pd.get_dummies(d['REF_AREA'], drop_first=True, dtype=float), pd.get_dummies(d['TIME_PERIOD'], drop_first=True, dtype=float)]
    bl = [b for b in range(kmin, kmax + 1) if b != ref]
    ev = pd.DataFrame({f'b{b}': d['tr'] * (d['b'] == b) for b in bl}, index=d.index)
    Xm = pd.concat([pd.Series(1.0, index=d.index, name='c')] + X + [ev], axis=1).values
    beta, *_ = np.linalg.lstsq(Xm, d[y].values, rcond=None)
    coef = dict(zip(bl, beta[-len(bl):]))
    coef[ref] = 0.0
    return dict(sorted(coef.items()))


def short_window(df, y, treated, controls, date, w=6):
    """(treated - mean control) average over [date, date+w) minus over [date-w, date)."""
    t = pd.Period(date, 'M')
    d = df.dropna(subset=[y])
    gap = d[d.REF_AREA == treated].set_index('per')[y] - d[d.REF_AREA.isin(controls)].groupby('per')[y].mean()
    pre, post = gap[(gap.index >= t - w) & (gap.index < t)], gap[(gap.index >= t) & (gap.index < t + w)]
    return post.mean() - pre.mean()


def main():
    raw = download() if ('--refresh' in sys.argv or not CACHE.exists()) else pd.read_csv(CACHE)
    raw['per'] = pd.PeriodIndex(raw['TIME_PERIOD'], freq='M')
    raw['k'] = [(p - EVENT0).n for p in raw['per']]
    have = raw.groupby('REF_AREA')[list(SERIES)].count()
    print('Observations per country:\n', have.T.to_string())
    print('Sample:', raw.per.min(), '-', raw.per.max())

    results, perm_rows, short_rows = {}, [], []
    for ctrl_name, ctrl in [('all', [c for c in EA if c != 'NL']), ('clean', CLEAN)]:
        sub = raw[raw.REF_AREA.isin(ctrl + ['NL'])]
        for y in SERIES:
            units = [c for c in ctrl + ['NL'] if sub.loc[sub.REF_AREA == c, y].notna().sum() > 40]
            s = sub[sub.REF_AREA.isin(units)]
            res = {u: twfe(s, y, u) for u in units}            # NL + placebo runs
            results[(ctrl_name, y)] = res
            post = {u: np.mean([v for b, v in res[u].items() if b >= 0]) for u in units}
            pre = {u: np.mean([v for b, v in res[u].items() if b < -1]) for u in units}
            rank = sorted(post, key=lambda u: abs(post[u]), reverse=True).index('NL') + 1
            perm_rows.append({'controls': ctrl_name, 'outcome': y, 'n_units': len(units),
                              'NL avg post coef': post['NL'], 'NL avg pre coef': pre['NL'],
                              'rank of |NL post| among units (1=largest)': rank,
                              'permutation p (two-sided)': rank / len(units)})
            for lab, dt in DATES.items():
                short_rows.append({'controls': ctrl_name, 'outcome': y, 'date': lab,
                                   'NL - controls, 6m after vs 6m before': short_window(s, y, 'NL', [u for u in units if u != 'NL'], dt)})
    perm = pd.DataFrame(perm_rows)
    short = pd.DataFrame(short_rows).pivot_table(index=['controls', 'outcome'], columns='date',
                                                 values='NL - controls, 6m after vs 6m before', sort=False)
    pd.set_option('display.width', 250)
    print('\nAverage event-time coefficients and permutation ranks:\n', perm.round(2).to_string(index=False))
    print('\nShort-window changes (pp):\n', short.round(2).to_string())
    perm.round(3).to_csv(D / 'event_study_summary.csv', index=False)
    short.round(3).to_csv(D / 'event_study_short_windows.csv')
    coefs = pd.DataFrame({f'{c}|{y}': results[(c, y)]['NL'] for (c, y) in results})
    coefs.index = [f'{3*b}..{3*b+2}' for b in coefs.index]
    coefs.round(3).to_csv(D / 'event_study_coefs.csv')

    # ---- figure: NL coefficient path (clean controls) with placebo band
    plt.rcParams.update({'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
    fig, ax = plt.subplots(2, 2, figsize=(12, 7.2))
    for a, y in zip(ax.flat, SERIES):
        for ctrl_name, col, ls in [('clean', '#c0392b', '-'), ('all', '#1f3b73', '--')]:
            res = results[(ctrl_name, y)]
            x = np.array(list(res['NL'].keys())) * 3 + 1
            if ctrl_name == 'clean':
                plac = np.array([list(res[u].values()) for u in res if u != 'NL'])
                a.fill_between(x, plac.min(0), plac.max(0), color='grey', alpha=0.18, lw=0, label='Placebo range (clean controls as fake treated)')
            a.plot(x, list(res['NL'].values()), color=col, ls=ls, marker='o', ms=3, lw=1.6,
                   label=f'NL vs {"clean controls (AT, FI, IT, MT, LU)" if ctrl_name == "clean" else "all euro-area countries"}')
        a.axhline(0, color='k', lw=0.6)
        for m in (0, 12, 24):
            a.axvline(m, color='#7f8c8d', ls=':', lw=1)
        a.set_title(LABEL[y], loc='left', fontweight='bold')
        a.set_xlabel('months since first announcement (May 2022); bins of 3 months, ref. = months −3..−1')
    fig.suptitle('Dotted lines: 0 = May-22 (1% announced) · 12 = May-23 (1% binding, 2% announced) · 24 = May-24 (2% binding)',
                 fontsize=9, color='#555', x=0.01, ha='left')
    ax[0, 0].legend(frameon=False, fontsize=7.5, loc='lower left')
    fig.text(0.01, 0.005, 'Source: ECB Data Portal (MIR, BSI); ESRB CCyB table for control selection; own calculations. '
             'Two-way FE event study; one treated unit, so no causal claim; grey = placebo range.', fontsize=7.5, color='grey')
    plt.tight_layout(rect=(0, 0.02, 1, 0.97))
    plt.savefig(FIG / 'fig3_event_study.png', dpi=170)
    print('saved fig3')


if __name__ == '__main__':
    main()
