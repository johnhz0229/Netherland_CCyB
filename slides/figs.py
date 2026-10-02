"""Figures for the Beamer deck (slides/main.tex), drawn in one style with the slide font (TeX Gyre Pagella).

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
PAGELLA = Path('/usr/share/texmf/fonts/opentype/public/tex-gyre')
for f in ['texgyrepagella-regular.otf', 'texgyrepagella-bold.otf', 'texgyrepagella-italic.otf']:
    if (PAGELLA / f).exists():
        font_manager.fontManager.addfont(str(PAGELLA / f))
NAVY, RED, GREY, LIGHT, GOLD, GREEN = '#1F3B73', '#A93226', '#7A7A7A', '#E3E3E3', '#8C8C8C', '#3A3A3A'
plt.rcParams.update({
    'font.family': 'TeX Gyre Pagella', 'font.size': 8.5, 'axes.titlesize': 9, 'axes.labelsize': 8,
    'xtick.labelsize': 7.5, 'ytick.labelsize': 7.5, 'legend.fontsize': 7.5, 'lines.markersize': 3,
    'axes.spines.top': False, 'axes.spines.right': False, 'axes.edgecolor': '#9A9A9A', 'axes.linewidth': 0.6,
    'xtick.color': '#555555', 'ytick.color': '#555555', 'xtick.major.width': 0.6, 'ytick.major.width': 0.6,
    'axes.labelcolor': '#444444', 'text.color': '#222222', 'axes.titlecolor': '#222222',
    'axes.titleweight': 'normal', 'axes.titlelocation': 'left', 'axes.titlepad': 8,
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
    fig, ax = plt.subplots(figsize=(7.3, 1.85))
    ax.axhspan(2, 10, color=GOLD, alpha=0.12, lw=0)
    ax.axhline(0, color='k', lw=0.6)
    ax.axvspan(pd.Timestamp('2008-07-01'), pd.Timestamp('2009-07-01'), color=GREY, alpha=0.15, lw=0)
    ax.plot(g.index, g['gap_hp2s'], color=GREY, lw=1.6, ls=(0, (2, 2)), label='Ex-post gap (two-sided HP, 2026 view)')
    ax.plot(g.index, g['gap_bis'].fillna(g['gap_hp1s']), color=RED, lw=1.8, label='Real-time gap (one-sided HP) = official BIS gap')
    kw = dict(fontsize=7.5, arrowprops=dict(arrowstyle='-|>', color='#333', lw=0.8, mutation_scale=9))
    ax.annotate('Missed: −13pp\non the eve of the GFC', xy=(pd.Timestamp('2007-10-01'), -13.4), xytext=(pd.Timestamp('1997-06-01'), -38), **kw)
    ax.annotate('False alarm: +17pp\nin a bust (2012)', xy=(pd.Timestamp('2012-04-01'), 16.8), xytext=(pd.Timestamp('2005-03-01'), 32), **kw)
    ax.annotate('Revised: 2016Q1 read −0.6pp\nin real time, +26.9pp today', xy=(pd.Timestamp('2016-01-01'), 26.9), xytext=(pd.Timestamp('2017-03-01'), 36), **kw)
    for d, v, lab in [('2021-10-01', -32.7, 'May-22 decision:\ngap −33pp'), ('2022-10-01', -46.8, 'May-23 decision:\ngap −47pp')]:
        ax.plot(pd.Timestamp(d), v, 'o', color=NAVY, ms=5, zorder=5)
    ax.annotate('At the decisions: −33pp and −47pp → Basel guide 0%', xy=(pd.Timestamp('2021-10-01'), -32.7),
                xytext=(pd.Timestamp('2004-06-01'), -55), color=NAVY, **{k: v for k, v in kw.items() if k != 'fontsize'}, fontsize=7.5)
    ax.set_ylabel('percentage points')
    ax.set_ylim(-62, 45)
    ax.legend(frameon=False, loc='upper left', ncol=1, fontsize=7)
    save(fig, 'gap')


# ---------------------------------------------------------------- 2. credit cold / housing hot (slide 7)
def fig_indicators():
    spp = pd.read_csv(D / 'nl_spp.csv', index_col=0); spp.index = qidx(spp.index)
    tc = pd.read_csv(D / 'nl_tc.csv', index_col=0); tc.index = qidx(tc.index)
    dsr = pd.read_csv(D / 'nl_dsr.csv', index_col=0); dsr.index = qidx(dsr.index)
    gap = pd.read_csv(D / 'nl_gaps.csv', index_col=0); gap.index = qidx(gap.index)
    dec = [pd.Timestamp('2022-05-01'), pd.Timestamp('2023-05-01')]
    fig, ax = plt.subplots(1, 3, figsize=(7.3, 2.1))

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
            a.axvline(d, color=GREY, lw=0.8, ls='--')
        a.set_xlim(pd.Timestamp('2005-01-01'), pd.Timestamp('2026-06-01'))
    ax[0].text(dec[0], ax[0].get_ylim()[0] + 1, ' CCyB\n decisions', fontsize=6.8, color='#555555', va='bottom')
    fig.tight_layout(w_pad=2.5)
    save(fig, 'indicators')


# ---------------------------------------------------------------- 3. event study (slide 16)
def fig_event():
    import event_study as es
    raw = pd.read_csv(D / 'ecb_mir_bsi.csv')
    raw['per'] = pd.PeriodIndex(raw['TIME_PERIOD'], freq='M')
    raw['k'] = [(p - es.EVENT0).n for p in raw['per']]
    fig, ax = plt.subplots(1, 2, figsize=(7.3, 2.05))
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
            a.axvline(m, color=GREY, lw=0.8, ls='--')
        a.set_title(title)
        a.set_xlabel('months since first announcement (May 2022)')
    lo, hi = ax[0].get_ylim()
    for m, lab in [(0, '1% ann.'), (12, '1% binding /\n2% ann.'), (24, '2% binding')]:
        ax[0].text(m + 0.6, hi * 0.97, lab, fontsize=6.8, color='#555555', va='top')
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
    fig, ax = plt.subplots(1, 2, figsize=(6.6, 1.75), gridspec_kw={'width_ratios': [1.35, 1]})
    a = ax[0]
    y = np.arange(len(banks))
    a.barh(y, h22.values, height=0.55, color=NAVY)
    for i, v2 in enumerate(h22.values):
        a.text(v2 + 0.3, i, f'€{v2:.1f}bn', va='center', fontsize=7.5, color=NAVY)
    a.set_yticks(y, banks); a.invert_yaxis()
    a.set_title('CET1 headroom above the requirement, end-2022')
    a.set_xlim(0, 17.5)
    a.set_xlabel('€ bn')
    a = ax[1]
    tot = [h21.sum(), h22.sum()]; cc = [3.3, 6.7]
    xs = np.arange(2)
    a.bar(xs, tot, color=LIGHT, width=0.55, label='Headroom, 4 banks')
    a.bar(xs, cc, color=RED, width=0.55, label='CCyB (sector-wide)')
    for i in range(2):
        a.text(i, tot[i] + 0.8, f'€{tot[i]:.1f}bn', ha='center', fontsize=7.5)
        a.text(i, cc[i] + 1.2, f'€{cc[i]:.1f}bn = {cc[i]/tot[i]*100:.0f}%', ha='center', va='bottom', color=RED, fontsize=7.5)
    a.set_xticks(xs, ['end-2021\n(1% step)', 'end-2022\n(full 2%)']); a.set_xlim(-0.6, 1.6)
    a.set_title('CCyB (red) within total headroom (grey)')
    a.set_ylim(0, 48)
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
    fig, ax = plt.subplots(figsize=(4.2, 2.4))
    level = 0.0
    for i, (lab, v, col) in enumerate(steps):
        bottom = level if v >= 0 else level + v
        ax.bar(i, abs(v), bottom=bottom, color=col, width=0.6)
        if v >= 0:
            ax.text(i, bottom + abs(v) + 0.25, f'{v:+.1f}', ha='center', fontsize=8, fontweight='bold', color=col)
        else:
            ax.text(i, bottom - 0.25, f'{v:+.1f}', ha='center', va='top', fontsize=8, fontweight='bold', color=col)
        if i < len(steps) - 1:
            ax.plot([i + 0.3, i + 0.7], [level + v, level + v], color='#555', lw=0.8, ls=':')
        level += v
    ax.bar(len(steps), level, color=NAVY, width=0.6)
    ax.text(len(steps), level - 0.6, f'{level:+.1f}', ha='center', va='top', fontsize=8, fontweight='bold', color=NAVY)
    ax.axhline(0, color='k', lw=0.8)
    ax.text(4.35, 0.2, 'pre-COVID level', fontsize=7, color='#333', ha='right')
    ax.set_xticks(range(len(steps) + 1), [s[0] for s in steps] + ['Net vs\npre-COVID'])
    ax.set_ylabel('€ bn of CET1 required (cumulative)')
    ax.set_ylim(-7.5, 1.8)
    save(fig, 'swap')
    return cut20, cut24, level


# ---------------------------------------------------------------- 6. spring-2020 releases (slide 3)
def fig_releases():
    # ESRB CCyB table, announcements Mar-Apr 2020 (docs/02_findings.md, "CCyB releases in spring 2020")
    rows = [('Norway', 2.5, 1.0, '13 Mar'), ('Sweden', 2.5, 0.0, '16 Mar'), ('Iceland', 2.0, 0.0, '18 Mar'),
            ('Czech Republic', 1.75, 1.0, '26 Mar'), ('Denmark', 1.0, 0.0, '12 Mar'), ('Lithuania', 1.0, 0.0, '31 Mar'),
            ('Ireland', 1.0, 0.0, '1 Apr'), ('France', 0.25, 0.0, '1 Apr'), ('Netherlands', 0.0, 0.0, '')]
    fig, ax = plt.subplots(figsize=(4.3, 2.4))
    for i, (c, a, b, d) in enumerate(rows):
        nl = c == 'Netherlands'
        if a > b:
            ax.annotate('', xy=(b, i), xytext=(a, i), arrowprops=dict(arrowstyle='-|>', color=NAVY, lw=1.3, mutation_scale=9, shrinkA=3, shrinkB=2))
            ax.plot(a, i, 'o', color=NAVY, ms=5.5)
            ax.text(a + 0.07, i, f'{a:g} → {b:g}%  ({d})', va='center', fontsize=7.5, color='#444')
        else:
            ax.plot(0, i, 'o', color=RED, ms=6.5)
            ax.text(0.09, i, 'at 0%: nothing to release', va='center', fontsize=8, color=RED)
    ax.set_yticks(range(len(rows)), [r[0] for r in rows])
    ax.get_yticklabels()[-1].set_color(RED)
    ax.invert_yaxis(); ax.set_xlim(-0.08, 3.6)
    ax.set_xlabel('CCyB rate before → after the release (%)')
    ax.spines['left'].set_visible(False); ax.tick_params(axis='y', length=0)
    ax.xaxis.grid(True, color='#EDEDED', lw=0.6); ax.set_axisbelow(True)
    save(fig, 'releases')


# ---------------------------------------------------------------- 7. macro: recovery, then the storm (slide 7)
def fig_macro():
    d = pd.read_csv(D / 'nl_macro.csv', index_col=0, parse_dates=True).loc['2019-01-01':'2024-12-01']
    dec = [pd.Timestamp('2022-05-25'), pd.Timestamp('2023-05-31')]
    fig, ax = plt.subplots(1, 3, figsize=(7.3, 2.05))
    g = d['gdp'].dropna()
    a = ax[0]; a.plot(g.index, g, color=NAVY, lw=1.7, marker='o', ms=2.5)
    a.axhline(100, color=GREY, lw=0.7, ls=':'); a.text(pd.Timestamp('2024-12-01'), 98.2, 'pre-COVID level\n(2019Q4 = 100)', fontsize=6.8, color=GREY, ha='right', va='top')
    a.set_title('Real GDP, index'); a.set_ylim(88, 112)
    a.annotate('back above\npre-COVID\nlevel in 2021', xy=(pd.Timestamp('2021-06-01'), g.loc['2021-06-01']), xytext=(pd.Timestamp('2019-02-01'), 104.5),
               fontsize=7, arrowprops=dict(arrowstyle='-|>', lw=0.7, color='#333'))
    h = d['hicp'].dropna()
    a = ax[1]; a.plot(h.index, h, color=RED, lw=1.7)
    a.axhline(0, color='k', lw=0.5); a.set_title('HICP inflation, % y/y')
    a.annotate(f'peak {h.max():.1f}% ({h.idxmax():%b %Y})\n2022 average 11.6%', xy=(h.idxmax(), h.max()), xytext=(pd.Timestamp('2019-02-01'), 13),
               fontsize=7, arrowprops=dict(arrowstyle='-|>', lw=0.7, color='#333'))
    r = d['dfr'].dropna()
    a = ax[2]; a.step(r.index, r, where='post', color=NAVY, lw=1.7)
    a.axhline(0, color='k', lw=0.5); a.set_title('ECB deposit facility rate, %')
    a.annotate('first hike\nJul 2022', xy=(pd.Timestamp('2022-07-27'), 0), xytext=(pd.Timestamp('2019-06-01'), 2.2),
               fontsize=7, arrowprops=dict(arrowstyle='-|>', lw=0.7, color='#333'))
    for a in ax:
        for x in dec:
            a.axvline(x, color=GREY, lw=0.8, ls='--')
        a.set_xlim(pd.Timestamp('2019-01-01'), pd.Timestamp('2024-12-31'))
        a.xaxis.set_major_locator(matplotlib.dates.YearLocator(2)); a.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%Y'))
    ax[2].text(dec[1] + pd.Timedelta(days=20), 0.25, 'CCyB\ndecisions', fontsize=6.8, color='#555')
    fig.tight_layout(w_pad=2.2)
    save(fig, 'macro')


# ---------------------------------------------------------------- 8. bank capital and the stress test (slide 9)
def fig_banks():
    fig, ax = plt.subplots(1, 2, figsize=(6.4, 2.1), gridspec_kw={'width_ratios': [1, 1.25]})
    a = ax[0]
    a.bar([0, 1], [17.7, 15.7], color=[NAVY, LIGHT], width=0.55)
    for x, v, lab in [(0, 17.7, 'Dutch banks\nend-2021'), (1, 15.7, 'EU average\n2021Q3')]:
        a.text(x, v + 0.4, f'{v:.1f}%', ha='center', fontsize=8.5, color=NAVY if x == 0 else '#444')
    a.set_xticks([0, 1], ['Dutch banks\nend-2021', 'EU average\n2021Q3']); a.set_ylim(0, 21)
    a.set_title('Core capital (CET1) ratio, % of RWA'); a.set_yticks([])
    a.spines['left'].set_visible(False)
    a = ax[1]
    a.bar([0, 1], [15.2, 11.5], color=[NAVY, '#7F93B8'], width=0.55)
    a.axhline(8, color=RED, lw=1.1, ls='--'); a.text(0.5, 8.4, 'minimum: 8%', fontsize=7.5, color=RED, ha='center', va='bottom')
    for x, v in [(0, 15.2), (1, 11.5)]:
        a.text(x, v + 0.4, f'{v:.1f}%', ha='center', fontsize=8.5, color=NAVY)
    a.annotate('', xy=(0.75, 11.5), xytext=(0.3, 15.2), arrowprops=dict(arrowstyle='-|>', color='#555', lw=0.8))
    a.text(0.58, 14.2, '−3.8pp', fontsize=7.5, color='#444')
    a.set_xticks([0, 1], ['start\nend-2022', 'after a severe\nrecession, end-2025']); a.set_ylim(0, 21); a.set_xlim(-0.5, 1.5)
    a.set_title("DNB stress test, four largest banks' CET1 ratio"); a.set_yticks([])
    a.spines['left'].set_visible(False)
    fig.tight_layout(w_pad=3)
    save(fig, 'banks')


# ---------------------------------------------------------------- 9. lending rates vs policy rate (slide 18)
def fig_rates():
    import event_study as es
    m = pd.read_csv(D / 'ecb_mir_bsi.csv'); m['t'] = pd.to_datetime(m['TIME_PERIOD'])
    nl = m[m.REF_AREA == 'NL'].set_index('t')['mort_rate']
    ctl = m[m.REF_AREA.isin(es.CLEAN)].groupby('t')['mort_rate'].mean()
    r = pd.read_csv(D / 'nl_macro.csv', index_col=0, parse_dates=True)['dfr'].dropna()
    fig, ax = plt.subplots(figsize=(4.3, 2.4))
    ax.step(r.loc['2019':].index, r.loc['2019':], where='post', color=GREY, lw=1.2, label='ECB deposit facility rate')
    ax.plot(ctl.index, ctl, color=NAVY, lw=1.6, label='Mortgage rate, five controls (average)')
    ax.plot(nl.index, nl, color=RED, lw=1.9, label='Mortgage rate, Netherlands')
    for x in [pd.Timestamp('2022-05-25'), pd.Timestamp('2023-05-31'), pd.Timestamp('2024-05-31')]:
        ax.axvline(x, color=GREY, lw=0.7, ls='--')
    ax.text(pd.Timestamp('2022-06-10'), -0.9, '1% ann.', fontsize=6.8, color='#555')
    ax.text(pd.Timestamp('2023-06-15'), -0.9, '2% ann.', fontsize=6.8, color='#555')
    ax.text(pd.Timestamp('2024-06-15'), -0.9, '2% binding', fontsize=6.8, color='#555')
    ax.axhline(0, color='k', lw=0.5)
    ax.set_ylim(-1.1, 4.6); ax.set_ylabel('% per year'); ax.set_xlim(pd.Timestamp('2019-01-01'), nl.index.max())
    end = nl.index.max()
    for s_, lab, col in [(nl, 'Netherlands', RED), (ctl, 'Controls', NAVY), (r, 'ECB deposit\nrate', GREY)]:
        ax.text(end + pd.Timedelta(days=45), s_.loc[:end].iloc[-1], lab, fontsize=7, color=col, va='center')
    ax.set_xlim(pd.Timestamp('2019-01-01'), end + pd.Timedelta(days=330))
    save(fig, 'rates')


# ---------------------------------------------------------------- 10. the European wave (slide 19)
def fig_europe():
    # ESRB CCyB table (Sep 2026): first post-COVID positive rate and the date it applies from (docs/02_findings.md)
    rows = [('Germany', '2023-02-01', 0.75), ('France', '2024-01-01', 1.0), ('Ireland', '2024-06-01', 1.5),
            ('Netherlands', '2024-05-31', 2.0), ('Belgium', '2024-10-01', 1.0), ('Portugal', '2026-01-01', 0.75),
            ('Spain', '2026-10-01', 1.0)]
    fig, ax = plt.subplots(figsize=(4.3, 2.4))
    for c, d, v in rows:
        nl = c == 'Netherlands'
        x = pd.Timestamp(d)
        ax.vlines(x, 0, v, color=RED if nl else '#B5B5B5', lw=2.2 if nl else 1.4)
        ax.plot(x, v, 'o', color=RED if nl else NAVY, ms=7 if nl else 5.5)
        dx, ha = (pd.Timedelta(days=-20), 'right') if c == 'Ireland' else (pd.Timedelta(0), 'center')
        ax.text(x + dx, v + (0.06 if c == 'Ireland' else 0.12), f'{c}\n{v:g}%', ha=ha, va='bottom', fontsize=7.5, color=RED if nl else '#333', fontweight='bold' if nl else 'normal')
    ax.axhline(0, color='k', lw=0.6)
    ax.set_ylim(0, 2.65); ax.set_xlim(pd.Timestamp('2022-07-01'), pd.Timestamp('2027-03-01'))
    ax.set_ylabel('CCyB rate (%)'); ax.set_xlabel('date the new rate applies from')
    ax.yaxis.grid(True, color='#EDEDED', lw=0.6); ax.set_axisbelow(True)
    ax.xaxis.set_major_locator(matplotlib.dates.YearLocator()); ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%Y'))
    save(fig, 'europe')


# ---------------------------------------------------------------- 11. resilience: releasable capital (slide 20)
def fig_resilience():
    fig, ax = plt.subplots(figsize=(6.4, 1.45))
    rows = [('Releasable CCyB capital, March 2020', 0.0, LIGHT), ('Releasable CCyB capital, since May 2024', 6.7, RED),
            ('Peak accumulated losses of Dutch banks, 2007–16', 12.0, '#B5B5B5')]
    for i, (lab, v, col) in enumerate(rows):
        ax.barh(i, v, color=col, height=0.55)
        ax.text(v + 0.15, i, f'€{v:g}bn' if v else '€0', va='center', fontsize=8.5, color=RED if i == 1 else '#333')
    ax.set_yticks(range(3), [r[0] for r in rows]); ax.invert_yaxis()
    ax.set_xlim(0, 14); ax.set_xlabel('€ bn'); ax.spines['left'].set_visible(False); ax.tick_params(axis='y', length=0)
    save(fig, 'resilience')


# ---------------------------------------------------------------- 12. appendix: the verdict table, row by row (slide 14)
DEC = [pd.Timestamp('2022-05-25'), pd.Timestamp('2023-05-31')]


def _ccyb_series():
    # announced rate path (ESRB/DNB): 0% until May-22, 1% announced May-22, 2% announced May-23
    idx = pd.date_range('2019-01-01', '2026-06-30', freq='D')
    s = pd.Series(0.0, index=idx)
    s[s.index >= DEC[0]] = 1.0
    s[s.index >= DEC[1]] = 2.0
    return s


def _style(a, title):
    a.set_title(title, fontsize=8)
    for x in DEC:
        a.axvline(x, color=GREY, lw=0.7, ls='--')
    a.set_xlim(pd.Timestamp('2019-01-01'), pd.Timestamp('2026-06-30'))
    a.xaxis.set_major_locator(matplotlib.dates.YearLocator(2)); a.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%Y'))


def fig_verdict_a():
    gap = pd.read_csv(D / 'nl_gaps.csv', index_col=0); gap.index = qidx(gap.index)
    dsr = pd.read_csv(D / 'nl_dsr.csv', index_col=0); dsr.index = qidx(dsr.index)
    tc = pd.read_csv(D / 'nl_tc.csv', index_col=0); tc.index = qidx(tc.index)
    fig, ax = plt.subplots(1, 4, figsize=(7.3, 1.75))
    c = _ccyb_series()
    a = ax[0]
    a.step(c.index, c, where='post', color=RED, lw=1.9)
    a.set_ylim(-0.2, 3.2); _style(a, 'CCyB rate (announced), %')
    a.text(pd.Timestamp('2019-02-01'), 2.55, 'two steps of 1pp,\na year apart,\nthen held at 2%', fontsize=6.6, color='#444', va='center')
    for a, s, title in [(ax[1], gap['gap_bis'].fillna(gap['gap_hp1s']), 'Credit-to-GDP gap, pp'),
                        (ax[2], dsr['H'], 'Debt service, % of income'),
                        (ax[3], tc['H'], 'Household debt, % of GDP')]:
        s = s.loc['2019':]
        a.plot(s.index, s, color=NAVY, lw=1.6)
        _style(a, title)
    fig.tight_layout(w_pad=1.6)
    save(fig, 'verdict_a')


def fig_verdict_b():
    spp = pd.read_csv(D / 'nl_spp.csv', index_col=0); spp.index = qidx(spp.index)
    r = pd.read_csv(D / 'nl_macro.csv', index_col=0, parse_dates=True)['dfr'].dropna()
    fig, ax = plt.subplots(1, 3, figsize=(7.3, 1.8), gridspec_kw={'width_ratios': [1.15, 0.85, 1.2]})
    a = ax[0]
    h = spp['N771'].loc['2019':]
    a.bar(h.index, h, width=70, color=[RED if v < 0 else '#B9C3D6' for v in h])
    a.axhline(0, color='k', lw=0.5)
    _style(a, 'House prices, nominal % y/y')
    a.annotate('2023: falling\n→ DNB raised', xy=(pd.Timestamp('2023-04-01'), -4.0), xytext=(pd.Timestamp('2019-03-01'), -6.5),
               fontsize=6.8, arrowprops=dict(arrowstyle='-|>', lw=0.7, color='#333'))
    a.annotate('2024–25: ≈ +10%\n→ DNB held at 2%', xy=(pd.Timestamp('2024-10-01'), 10.8), xytext=(pd.Timestamp('2024-07-01'), 15.5),
               fontsize=6.8, ha='center', arrowprops=dict(arrowstyle='-|>', lw=0.7, color='#333'))
    a.set_ylim(-9, 21)
    a = ax[1]
    rr = r.loc['2021-06':'2024-06']
    a.step(rr.index, rr, where='post', color=NAVY, lw=1.7)
    a.axhline(0, color='k', lw=0.5)
    a.set_title('ECB deposit rate, %', fontsize=8)
    for x in DEC:
        a.axvline(x, color=GREY, lw=0.7, ls='--')
    a.text(DEC[1] + pd.Timedelta(days=20), 0.3, '2% announced:\nrate at 3.25%', fontsize=6.5, color='#444')
    a.xaxis.set_major_locator(matplotlib.dates.YearLocator()); a.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%Y'))
    a = ax[2]
    # systemic buffers of the large banks, % of RWA (docs/02_findings.md, section 0a)
    banks = ['ING', 'Rabobank', 'ABN AMRO']
    vals = {'until Mar 2020': [3.0, 3.0, 3.0], 'from Mar 2020': [2.5, 2.0, 1.5], 'from May 2024': [2.0, 1.75, 1.25]}
    cols = ['#B5B5B5', '#7F93B8', NAVY]
    x = np.arange(len(banks)); w = 0.26
    for k, (lab, v) in enumerate(vals.items()):
        a.bar(x + (k - 1) * w, v, width=w * 0.92, color=cols[k], label=lab)
        for xi, vi in zip(x + (k - 1) * w, v):
            a.text(xi, vi + 0.05, f'{vi:g}', ha='center', fontsize=6, color='#333')
    a.set_xticks(x, banks); a.set_ylim(0, 4.4)
    a.set_title('Systemic buffer by bank, % of RWA', fontsize=8)
    a.legend(frameon=False, fontsize=6.3, ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.0), handlelength=1, columnspacing=0.8)
    fig.tight_layout(w_pad=1.6)
    save(fig, 'verdict_b')


if __name__ == '__main__':
    fig_gap(); fig_indicators(); fig_event(); fig_headroom(); print('swap', fig_swap())
    fig_releases(); fig_macro(); fig_banks(); fig_rates(); fig_europe(); fig_resilience()
    fig_verdict_a(); fig_verdict_b()
