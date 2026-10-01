"""Figures for the Beamer deck (slides/main.tex), drawn in one style with the slide font (Fira Sans).

Run from the repo root:  python slides/figs.py   -> slides/figs/*.pdf
Every number comes from data/ (see docs/02_findings.md). The event-study panels re-estimate from the
cached ECB data via code/event_study.py.
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[1]
D, OUT = ROOT / 'data', ROOT / 'slides' / 'figs'
OUT.mkdir(exist_ok=True)
sys.path.insert(0, str(ROOT / 'code'))

# ---- style: slide palette and font
FIRA = Path('/usr/share/texlive/texmf-dist/fonts/opentype/public/fira')
for f in ['FiraSans-Book.otf', 'FiraSans-Regular.otf', 'FiraSans-Medium.otf', 'FiraSans-SemiBold.otf', 'FiraSans-Bold.otf']:
    if (FIRA / f).exists():
        font_manager.fontManager.addfont(str(FIRA / f))
NAVY, RED, GREY, LIGHT, GOLD, GREEN = '#1F3B73', '#C0392B', '#7F8C8D', '#D5DBE5', '#E0A100', '#2E8B57'
plt.rcParams.update({
    'font.family': 'Fira Sans', 'font.size': 8.5, 'axes.titlesize': 9, 'axes.labelsize': 8,
    'xtick.labelsize': 7.5, 'ytick.labelsize': 7.5, 'legend.fontsize': 7.5, 'lines.markersize': 3,
    'axes.spines.top': False, 'axes.spines.right': False, 'axes.edgecolor': '#555555',
    'axes.titleweight': 'semibold', 'axes.titlelocation': 'left', 'axes.titlepad': 8,
    'savefig.bbox': 'tight', 'savefig.pad_inches': 0.04, 'pdf.fonttype': 3,
})


def qidx(s):
    return pd.PeriodIndex(pd.Index(s).str.replace('-', ''), freq='Q').to_timestamp()


def save(fig, name):
    fig.savefig(OUT / f'{name}.pdf')
    plt.close(fig)
    print('saved', name)


# ---------------------------------------------------------------- 1. credit gap (slide 9)
def fig_gap():
    g = pd.read_csv(D / 'nl_gaps.csv', index_col=0)
    g.index = qidx(g.index)
    g = g.loc['1990':]
    fig, ax = plt.subplots(figsize=(7.6, 3.15))
    ax.axhspan(2, 10, color=GOLD, alpha=0.18, lw=0)
    ax.text(pd.Timestamp('1990-03-01'), 12.5, 'Basel buffer guide > 0 when gap is 2–10pp (shaded)', fontsize=7, va='bottom', color='#8a6d00')
    ax.axhline(0, color='k', lw=0.6)
    ax.axvspan(pd.Timestamp('2008-07-01'), pd.Timestamp('2009-07-01'), color=GREY, alpha=0.15, lw=0)
    ax.plot(g.index, g['gap_hp2s'], color=GREY, lw=1.6, ls=(0, (2, 2)), label='Ex-post gap (two-sided HP, 2026 view)')
    ax.plot(g.index, g['gap_bis'].fillna(g['gap_hp1s']), color=RED, lw=1.8, label='Real-time gap (one-sided HP) = official BIS gap')
    kw = dict(fontsize=7.5, arrowprops=dict(arrowstyle='-|>', color='#333', lw=0.8, mutation_scale=9))
    ax.annotate('Missed: −13pp\non the eve of the GFC', xy=(pd.Timestamp('2007-10-01'), -13.4), xytext=(pd.Timestamp('1997-06-01'), -38), **kw)
    ax.annotate('False alarm: +17pp\nin a bust (2012)', xy=(pd.Timestamp('2012-04-01'), 16.8), xytext=(pd.Timestamp('2001-01-01'), 30), **kw)
    ax.annotate('Rewritten: 2016Q1\n−0.6pp then, +26.9pp now', xy=(pd.Timestamp('2016-01-01'), 26.9), xytext=(pd.Timestamp('2017-03-01'), 36), **kw)
    for d, v, lab in [('2021-10-01', -32.7, 'May-22 decision:\ngap −33pp'), ('2022-10-01', -46.8, 'May-23 decision:\ngap −47pp')]:
        ax.plot(pd.Timestamp(d), v, 'o', color=NAVY, ms=5, zorder=5)
    ax.annotate('At the decisions: −33pp and −47pp\n(latest data: 2021Q4, 2022Q4) → guide = 0%', xy=(pd.Timestamp('2022-10-01'), -46.8),
                xytext=(pd.Timestamp('2011-01-01'), -52), color=NAVY, fontweight='semibold', **{k: v for k, v in kw.items() if k != 'fontsize'}, fontsize=7.5)
    ax.set_ylabel('percentage points')
    ax.set_ylim(-62, 45)
    ax.legend(frameon=False, loc='lower left', ncol=1)
    save(fig, 'gap')


# ---------------------------------------------------------------- 2. credit cold / housing hot (slide 7)
def fig_indicators():
    spp = pd.read_csv(D / 'nl_spp.csv', index_col=0); spp.index = qidx(spp.index)
    tc = pd.read_csv(D / 'nl_tc.csv', index_col=0); tc.index = qidx(tc.index)
    dsr = pd.read_csv(D / 'nl_dsr.csv', index_col=0); dsr.index = qidx(dsr.index)
    gap = pd.read_csv(D / 'nl_gaps.csv', index_col=0); gap.index = qidx(gap.index)
    dec = [pd.Timestamp('2022-05-01'), pd.Timestamp('2023-05-01')]
    fig, ax = plt.subplots(1, 3, figsize=(8.2, 2.65))

    a = ax[0]
    a.plot(spp.index, spp['R628'], color=RED, lw=1.6)
    peak = spp['R628'].loc[:'2012'].max()
    a.axhline(peak, color=GREY, ls=':', lw=1)
    a.text(spp.index[1], peak + 2, '2007 peak', fontsize=7, color=GREY)
    a.set_title('Real house prices (2010 = 100)')
    a.annotate('+19% y/y\n(nominal, 22Q1)', xy=(pd.Timestamp('2022-01-01'), spp.loc['2022-01-01', 'R628']),
               xytext=(pd.Timestamp('2012-06-01'), 128), fontsize=7, arrowprops=dict(arrowstyle='-|>', lw=0.7, color='#333'))
    a.annotate('−9% real\n(22Q2–23Q2)', xy=(pd.Timestamp('2023-04-01'), spp.loc['2023-04-01', 'R628']),
               xytext=(pd.Timestamp('2016-01-01'), 100), fontsize=7, arrowprops=dict(arrowstyle='-|>', lw=0.7, color='#333'))

    a = ax[1]
    a.plot(tc.index, tc['H'], color=NAVY, lw=1.6, label='Household debt / GDP')
    a.set_title('Household debt (% of GDP)')
    a.text(tc.index[-1], tc['H'].iloc[-1] + 1.5, f"{tc['H'].iloc[-1]:.0f}%", fontsize=7, color=NAVY, ha='right')
    a.text(pd.Timestamp('2006-01-01'), 96, 'Euro area 2022Q1: 58%', fontsize=7, color=GREY)

    a = ax[2]
    a.plot(dsr.index, dsr['H'], color=NAVY, lw=1.6)
    a.set_title('Household debt-service ratio (%)')
    a.annotate('14.6% (22Q1):\nlowest since 2005', xy=(pd.Timestamp('2022-01-01'), 14.6), xytext=(pd.Timestamp('2007-01-01'), 14.0),
               fontsize=7, arrowprops=dict(arrowstyle='-|>', lw=0.7, color='#333'))
    for a in ax:
        for d in dec:
            a.axvline(d, color=GOLD, lw=1.4, alpha=0.9)
        a.set_xlim(pd.Timestamp('2005-01-01'), pd.Timestamp('2026-06-01'))
    ax[0].text(dec[0], ax[0].get_ylim()[0] + 1, ' CCyB\n decisions', fontsize=6.8, color='#8a6d00', va='bottom')
    fig.tight_layout(w_pad=2.5)
    save(fig, 'indicators')


# ---------------------------------------------------------------- 3. event study (slide 16)
def fig_event():
    import event_study as es
    raw = pd.read_csv(D / 'ecb_mir_bsi.csv')
    raw['per'] = pd.PeriodIndex(raw['TIME_PERIOD'], freq='M')
    raw['k'] = [(p - es.EVENT0).n for p in raw['per']]
    fig, ax = plt.subplots(1, 2, figsize=(8.2, 2.75))
    for a, y, title in [(ax[0], 'mort_rate', 'Mortgage lending rate, NL minus controls (pp)'),
                        (ax[1], 'hh_growth', 'Household loan growth, NL minus controls (pp)')]:
        sub = raw[raw.REF_AREA.isin(es.CLEAN + ['NL'])]
        units = [c for c in es.CLEAN + ['NL'] if sub.loc[sub.REF_AREA == c, y].notna().sum() > 40]
        res = {u: es.twfe(sub[sub.REF_AREA.isin(units)], y, u) for u in units}
        x = np.array(list(res['NL'].keys())) * 3 + 1
        plac = np.array([list(res[u].values()) for u in units if u != 'NL'])
        a.fill_between(x, plac.min(0), plac.max(0), color=LIGHT, lw=0, label='Placebo range (each control as fake treated)')
        a.plot(x, list(res['NL'].values()), color=RED, lw=1.8, marker='o', ms=3.5, label='Netherlands')
        a.axhline(0, color='k', lw=0.6)
        for m, lab in [(0, 'May-22\n1% announced'), (12, 'May-23\n1% binding,\n2% announced'), (24, 'May-24\n2% binding')]:
            a.axvline(m, color=GOLD, lw=1.4)
        a.set_title(title)
        a.set_xlabel('months since first announcement (May 2022)')
    lo, hi = ax[0].get_ylim()
    for m, lab in [(0, '1% ann.'), (12, '1% binding /\n2% ann.'), (24, '2% binding')]:
        ax[0].text(m + 0.6, hi * 0.97, lab, fontsize=6.8, color='#8a6d00', va='top')
    ax[0].legend(frameon=False, loc='lower left', fontsize=7)
    fig.tight_layout(w_pad=2.5)
    save(fig, 'event')


# ---------------------------------------------------------------- 4. headroom by bank (slide 15)
def fig_headroom():
    b = pd.read_csv(D / 'nl_bank_capital.csv')
    b['head'] = (b.cet1_pct - b.cet1_req_pct) / 100 * b.rwa_eur_bn
    banks = ['ING', 'Rabobank', 'ABN AMRO', 'de Volksbank']
    h21 = b[b.date == '2021-Q4'].set_index('bank').loc[banks, 'head']
    h22 = b[b.date == '2022-Q4'].set_index('bank').loc[banks, 'head']
    fig, ax = plt.subplots(1, 2, figsize=(8.2, 2.85), gridspec_kw={'width_ratios': [1.35, 1]})
    a = ax[0]
    y = np.arange(len(banks))
    a.barh(y + 0.2, h21.values, height=0.38, color=LIGHT, label='end-2021')
    a.barh(y - 0.2, h22.values, height=0.38, color=NAVY, label='end-2022')
    for i, (v1, v2) in enumerate(zip(h21.values, h22.values)):
        a.text(v1 + 0.3, i + 0.2, f'€{v1:.1f}bn', va='center', fontsize=7, color='#333')
        a.text(v2 + 0.3, i - 0.2, f'€{v2:.1f}bn', va='center', fontsize=7, color=NAVY)
    a.set_yticks(y, banks); a.invert_yaxis()
    a.set_title('CET1 headroom above requirement / MDA, by bank')
    a.set_xlim(0, 20.5); a.legend(frameon=False, loc='lower right')
    a.set_xlabel('€ bn')
    a = ax[1]
    tot = [h21.sum(), h22.sum()]; cc = [3.3, 6.7]
    xs = np.arange(2)
    a.bar(xs, tot, color=LIGHT, width=0.55, label='Headroom, 4 banks')
    a.bar(xs, cc, color=RED, width=0.55, label='CCyB (sector-wide)')
    for i in range(2):
        a.text(i, tot[i] + 0.8, f'€{tot[i]:.1f}bn', ha='center', fontsize=7.5)
        a.text(i + 0.31, cc[i] / 2, f'€{cc[i]:.1f}bn\n= {cc[i]/tot[i]*100:.0f}%', ha='left', va='center', color=RED, fontsize=7.5, fontweight='semibold')
    a.set_xticks(xs, ['end-2021\n(1% step)', 'end-2022\n(full 2%)']); a.set_xlim(-0.5, 1.95)
    a.set_title('CCyB as share of headroom (upper bound)')
    a.set_ylim(0, 48); a.legend(frameon=False, loc='upper right', fontsize=7)
    fig.tight_layout(w_pad=3)
    save(fig, 'headroom')


# ---------------------------------------------------------------- 5. the swap (slide 14)
def fig_swap():
    b = pd.read_csv(D / 'nl_bank_capital.csv')
    r22 = b[b.date == '2022-Q4'].set_index('bank')['rwa_eur_bn']
    cut20 = sum(v / 100 * r22[k] for k, v in {'ING': 0.5, 'Rabobank': 1.0, 'ABN AMRO': 1.5}.items())
    cut24 = sum(v / 100 * r22[k] for k, v in {'ING': 0.5, 'Rabobank': 0.25, 'ABN AMRO': 0.25, 'de Volksbank': 0.75}.items())
    steps = [('Mar-2020\nsystemic\nbuffer cut', -cut20, GREY), ('May-2023\nCCyB 1%\nbinding', 3.3, RED),
             ('May-2024\nCCyB 2%\nbinding', 3.4, RED), ('May-2024\nO-SII\ncut', -cut24, GREY)]
    fig, ax = plt.subplots(figsize=(5.4, 3.45))
    level = 0.0
    for i, (lab, v, col) in enumerate(steps):
        bottom = level if v >= 0 else level + v
        ax.bar(i, abs(v), bottom=bottom, color=col, width=0.6)
        if v >= 0:
            ax.text(i, bottom + abs(v) + 0.25, f'{v:+.1f}', ha='center', fontsize=8, fontweight='semibold', color=col)
        else:
            ax.text(i, bottom - 0.25, f'{v:+.1f}', ha='center', va='top', fontsize=8, fontweight='semibold', color=col)
        if i < len(steps) - 1:
            ax.plot([i + 0.3, i + 0.7], [level + v, level + v], color='#555', lw=0.8, ls=':')
        level += v
    ax.bar(len(steps), level, color=NAVY, width=0.6)
    ax.text(len(steps), level - 0.6, f'{level:+.1f}', ha='center', va='top', fontsize=8, fontweight='semibold', color=NAVY)
    ax.axhline(0, color='k', lw=0.8)
    ax.text(4.35, 0.2, 'pre-COVID level', fontsize=7, color='#333', ha='right')
    ax.set_xticks(range(len(steps) + 1), [s[0] for s in steps] + ['Net vs\npre-COVID'])
    ax.set_ylabel('€ bn of CET1 required (cumulative)')
    ax.set_ylim(-7.5, 1.8)
    save(fig, 'swap')
    return cut20, cut24, level


if __name__ == '__main__':
    fig_gap(); fig_indicators(); fig_event(); fig_headroom(); print('swap', fig_swap())
