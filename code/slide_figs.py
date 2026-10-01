"""Figures for the slide deck, in one consistent style. Writes figures/slides/*.png.

Run after gap.py and other.py:  python code/slide_figs.py
Every number comes from data/ or docs/02_findings.md (policy dates/rates in §0, §0a).
"""
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / 'data'
OUT = ROOT / 'figures' / 'slides'
OUT.mkdir(parents=True, exist_ok=True)

ORANGE, BLUE, GREEN = '#E4572E', '#2F6DB5', '#1E9E6A'
INK, MUTED, GREY, GRID = '#14213D', '#6B7280', '#A3A9B3', '#E5E7EB'
TINT = '#EEF1F5'

plt.rcParams.update({
    'font.family': 'Liberation Sans', 'font.size': 11, 'text.color': INK,
    'axes.edgecolor': GREY, 'axes.labelcolor': MUTED, 'axes.spines.top': False,
    'axes.spines.right': False, 'xtick.color': MUTED, 'ytick.color': MUTED,
    'axes.grid': True, 'grid.color': GRID, 'grid.linewidth': 0.8, 'axes.axisbelow': True,
    'legend.frameon': False, 'savefig.dpi': 220, 'savefig.bbox': 'tight', 'savefig.pad_inches': 0.08,
})


def qidx(index):
    return pd.PeriodIndex(pd.Index(index).str.replace('-', ''), freq='Q').to_timestamp()


def save(fig, name):
    fig.savefig(OUT / name, transparent=False, facecolor='white')
    plt.close(fig)


# ---------------------------------------------------------------- 1. credit gap (slide 5)
g = pd.read_csv(D / 'nl_gaps.csv', index_col=0)
g.index = qidx(g.index)
g = g.loc['1985':]
fig, ax = plt.subplots(figsize=(8.6, 4.5))
ax.axhspan(2, 10, color=ORANGE, alpha=0.10, lw=0)
ax.text(pd.Timestamp('1985-06-01'), 11.2, 'Basel buffer-guide band (2–10pp)', fontsize=9, color=MUTED)
ax.axhline(0, color=INK, lw=0.8)
ax.plot(g.index, g['gap_hp2s'], color=GREY, lw=1.6, ls=(0, (4, 2)), label='Ex-post gap (two-sided HP)')
ax.plot(g.index, g['gap_ham20'], color=GREEN, lw=1.4, alpha=0.9, label='Hamilton gap (h = 20)')
ax.plot(g.index, g['gap_hp1s'], color=ORANGE, lw=2.4, label='Real-time gap (one-sided HP, λ = 400k) = BIS')
ax.axvspan(pd.Timestamp('2008-07-01'), pd.Timestamp('2009-07-01'), color=GREY, alpha=0.18, lw=0)
ax.text(pd.Timestamp('2008-08-01'), -82, 'GFC', fontsize=9, color=MUTED)
for d, lab in [('2022-04-01', 'May-22\n0→1%'), ('2023-04-01', 'May-23\n1→2%')]:
    ax.axvline(pd.Timestamp(d), color=INK, lw=0.9, ls=':')
ax.text(pd.Timestamp('2021-10-01'), 52, 'CCyB\ndecisions', fontsize=9, color=INK, ha='right')
for x, y, txt, xt, yt in [('2007-10-01', -13.4, 'Missed: −13pp\nbefore the GFC', '1996-01-01', -55),
                          ('2012-04-01', 16.8, 'False alarm: +17pp\nin a bust (2012)', '1999-06-01', 42),
                          ('2016-01-01', 26.9, 'Revised: −0.6pp real time\nvs +26.9pp ex post', '2013-06-01', 58)]:
    ax.annotate(txt, xy=(pd.Timestamp(x), y), xytext=(pd.Timestamp(xt), yt), fontsize=9.5, color=INK,
                arrowprops=dict(arrowstyle='-', color=INK, lw=0.7))
ax.set_ylabel('percentage points')
ax.set_ylim(-95, 72)
ax.legend(loc='lower left', fontsize=9.5, ncol=1)
save(fig, 'credit_gap.png')

# ---------------------------------------------------------------- 2. Basel buffer guide (slide 4)
fig, ax = plt.subplots(figsize=(5.6, 3.9))
x = np.linspace(-8, 16, 400)
ax.plot(x, np.clip((x - 2) / 8 * 2.5, 0, 2.5), color=INK, lw=2.4)
ax.axvspan(2, 10, color=ORANGE, alpha=0.10, lw=0)
ax.set_xlim(-8, 16); ax.set_ylim(-0.2, 3.0)
ax.set_xlabel('credit-to-GDP gap (pp)'); ax.set_ylabel('CCyB buffer guide (% of RWA)')
ax.annotate('L = 2pp: buffer starts', xy=(2, 0), xytext=(3.2, 0.55), fontsize=9.5,
            arrowprops=dict(arrowstyle='-', color=INK, lw=0.7))
ax.annotate('H = 10pp: maximum 2.5%', xy=(10, 2.5), xytext=(3.4, 2.75), fontsize=9.5,
            arrowprops=dict(arrowstyle='-', color=INK, lw=0.7))
ax.annotate('NL at the decisions:\n2022Q1 −37pp, 2023Q1 −55pp\n(off the scale) → guide = 0%',
            xy=(-8, 0), xytext=(-7.6, 1.15), fontsize=9.5, color=ORANGE,
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.2))
save(fig, 'buffer_guide.png')

# ---------------------------------------------------------------- 3. capital stack (slide 3)
# Stylised CET1 stack for a Dutch O-SII after 31 May 2024. Statutory rates: P1 4.5%, CCoB 2.5%,
# NL CCyB 2%. P2R and O-SII are bank-specific; heights for those two are illustrative.
layers = [  # (label, height, colour, right-hand note)
    ('Pillar 1 minimum  4.5%', 4.5, '#C9CED6', 'Minimum requirements\nbreach = resolution risk'),
    ('Pillar 2 requirement (P2R)\nbank-specific', 1.0, '#DADDE3', None),
    ('Capital conservation buffer  2.5%', 2.5, '#9FB6D6', 'Combined buffer\nusable, but dipping in\ntriggers MDA limits on\ndividends and bonuses'),
    ('O-SII buffer  0.25–2%\nbank-specific', 1.0, '#BFD0E6', None),
    ('CCyB  2% (NL, Dutch exposures)', 2.0, ORANGE, 'Releasable on demand\nby the authority'),
]
fig, ax = plt.subplots(figsize=(6.4, 5.0))
ax.set_xlim(0, 10); ax.set_ylim(-0.3, 13.6); ax.axis('off')
y = 0
spans = {}
for lab, h, col, note in layers:
    ax.add_patch(FancyBboxPatch((0.4, y + 0.06), 4.6, h - 0.12, boxstyle='round,pad=0,rounding_size=0.12',
                                fc=col, ec='white', lw=1.5))
    ax.text(2.7, y + h / 2, lab, ha='center', va='center', fontsize=9.5,
            color='white' if col == ORANGE else INK, fontweight='bold' if col == ORANGE else 'normal')
    spans[lab] = (y, y + h)
    y += h
mda = y
ax.add_patch(FancyBboxPatch((0.4, y + 0.06), 4.6, 1.0, boxstyle='round,pad=0,rounding_size=0.12',
                            fc='white', ec=GREY, lw=1.2, ls='--'))
ax.text(2.7, y + 0.56, 'Pillar 2 guidance (P2G)\nnon-binding, above MDA', ha='center', va='center', fontsize=9, color=MUTED)
ax.plot([0.2, 5.3], [mda, mda], color=INK, lw=1.6)
ax.text(5.45, mda, 'MDA trigger', va='center', fontsize=9.5, fontweight='bold', color=INK)


def brace(y0, y1, text, col=INK):
    ax.plot([5.3, 5.5, 5.5, 5.3], [y0 + 0.1, y0 + 0.1, y1 - 0.1, y1 - 0.1], color=col, lw=1.2)
    ax.text(5.7, (y0 + y1) / 2, text, va='center', fontsize=9.2, color=col)


brace(0, 5.5, 'Minimum requirements\n(P1 + P2R)')
brace(5.5, 9.0, 'Combined buffer: usable,\nbut dipping in triggers\nMDA payout limits')
brace(9.0, 11.0, 'Releasable on demand\nby the authority', ORANGE)
ax.text(0.4, -0.25, 'CET1 as % of risk-weighted assets (stylised; P2R and O-SII heights illustrative)',
        fontsize=8.5, color=MUTED, va='top')
save(fig, 'capital_stack.png')

# ---------------------------------------------------------------- 4. timeline (slide 8)
fig, ax = plt.subplots(figsize=(12.2, 4.4))
ax.step(pd.to_datetime(['2016-01-01', '2023-05-25', '2024-05-31', '2026-09-30']), [0, 1, 2, 2], where='post',
        color=ORANGE, lw=3, label='CCyB in force')
ax.step(pd.to_datetime(['2016-01-01', '2022-05-25', '2023-05-31', '2026-09-30']), [0, 1, 2, 2], where='post',
        color=INK, lw=1.4, ls=(0, (4, 2)), label='CCyB announced')
ax.set_xlim(pd.Timestamp('2019-07-01'), pd.Timestamp('2026-12-31'))
ax.set_ylim(-1.9, 3.15)
ax.set_yticks([0, 1, 2]); ax.set_yticklabels(['0%', '1%', '2%'])
ax.grid(axis='x', visible=False)
ax.spines['left'].set_visible(False)
ev = [  # date, label, y-text, colour
    ('2020-03-17', '17 Mar 2020\nSystemic buffer cut (3% → 2.5/2/1.5%);\n2% CCyB pre-announced as replacement', 2.55, INK),
    ('2020-12-29', '29 Dec 2020\nSRB converted\nto O-SII buffers', -1.05, MUTED),
    ('2022-01-01', '1 Jan 2022\nMortgage risk-\nweight floor', -1.05, MUTED),
    ('2022-02-15', 'Feb 2022\nNew CCyB framework:\n2% = normal times', 2.55, INK),
    ('2022-05-25', '25 May 2022\n1% announced\n(€3.3bn)', 1.45, ORANGE),
    ('2023-05-31', '31 May 2023 · 2% announced (€3.4bn)\nJun 2023 · O-SII cuts announced', 2.55, ORANGE),
    ('2024-05-31', '31 May 2024\n2% binding; O-SII\ncuts take effect', -1.05, ORANGE),
    ('2026-09-17', '17 Sep 2026\nheld at 2%', 1.0, INK),
]
for d, lab, yt, col in ev:
    t = pd.Timestamp(d)
    ax.plot([t, t], [0, yt], color=col, lw=0.7, ls=':', zorder=1)
    ax.text(t, yt, lab, fontsize=9, color=col, ha='center', va='bottom' if yt > 0 else 'top', linespacing=1.15)
ax.legend(loc='center left', bbox_to_anchor=(0.0, 0.62), fontsize=9.5)
ax.axhline(0, color=GREY, lw=0.8)
save(fig, 'timeline.png')

# ---------------------------------------------------------------- 5. stylised regimes (slide 7)
fig, ax = plt.subplots(figsize=(6.4, 3.7))
t = np.arange(0, 40)
gap_based = np.where(t < 24, 0, np.where(t < 30, (t - 24) * 0.4, 0))
pn = np.select([t < 4, t < 12, t < 24, t < 30], [0, np.minimum(2, (t - 4) * 0.25 + 0.25), 2,
                                                 2 + (t - 24) * 0.08], 0)
gap_based[30:] = 0
ax.step(t, pn, where='post', color=ORANGE, lw=2.6, label='Positive neutral (e.g. NL: 2% in normal times)')
ax.step(t, gap_based, where='post', color=INK, lw=1.8, ls=(0, (4, 2)), label='Gap-based (original Basel rule)')
for x0, x1, lab in [(0, 4, 'Recovery'), (4, 24, 'Normal'), (24, 30, 'Elevated'), (30, 40, 'Shock: release')]:
    ax.axvspan(x0, x1, color=TINT if lab != 'Shock: release' else '#FBE3DC', alpha=1, lw=0, zorder=0)
    ax.text((x0 + x1) / 2, 3.25, lab, ha='center', fontsize=9.5, color=MUTED)
ax.annotate('Positive neutral:\nthere is capital to release', xy=(30.3, 0.15), xytext=(31, 1.3), fontsize=9, color=ORANGE)
ax.annotate('Gap-based:\nlittle or nothing', xy=(30.3, 0.0), xytext=(31, 0.45), fontsize=9, color=INK)
ax.set_ylim(-0.1, 3.6); ax.set_xlim(0, 40)
ax.set_xticks([]); ax.set_ylabel('CCyB (% of RWA)')
ax.grid(axis='x', visible=False)
ax.legend(loc='upper left', bbox_to_anchor=(0.0, 0.93), fontsize=9)
save(fig, 'regimes.png')

# ---------------------------------------------------------------- 6. indicators (slide 13)
tc = pd.read_csv(D / 'nl_tc.csv', index_col=0)
dsr = pd.read_csv(D / 'nl_dsr.csv', index_col=0)
spp = pd.read_csv(D / 'nl_spp.csv', index_col=0)
for df in (tc, dsr, spp):
    df.index = qidx(df.index)
dec = [pd.Timestamp('2022-04-01'), pd.Timestamp('2023-04-01')]
fig, axs = plt.subplots(1, 3, figsize=(12.4, 3.6))
a = axs[0]
a.plot(spp.index, spp['R628'], color=ORANGE, lw=2.4)
pk = spp.loc[:'2019', 'R628'].max()
a.axhline(pk, color=MUTED, lw=1, ls=':')
a.text(spp.index[0], pk + 2, f'pre-GFC peak ({pk:.0f})', fontsize=9, color=MUTED)
a.set_title('Hot: real house prices (2010 = 100)', loc='left', fontsize=11, fontweight='bold', color=INK)
a = axs[1]
a.plot(tc.index, tc['H'], color=BLUE, lw=2.2, label='Households')
a.plot(tc.index, tc['N'], color=GREEN, lw=2.2, label='Non-financial corporates')
a.set_title('Cooling: debt-to-GDP (%)', loc='left', fontsize=11, fontweight='bold', color=INK)
a.legend(fontsize=9, loc='center left')
a = axs[2]
a.plot(dsr.index, dsr['H'], color=BLUE, lw=2.2, label='Households')
a.plot(dsr.index, dsr['P'], color=INK, lw=2.2, ls=(0, (4, 2)), label='Private non-financial')
a.set_title('Cool: debt-service ratio (% of income)', loc='left', fontsize=11, fontweight='bold', color=INK)
a.legend(fontsize=9, loc='center left')
for a in axs:
    for d in dec:
        a.axvline(d, color=INK, lw=0.8, ls=':')
    a.tick_params(labelsize=9)
fig.tight_layout(w_pad=2.5)
save(fig, 'indicators.png')
print('figures written to', OUT)
