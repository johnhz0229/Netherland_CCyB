import pandas as pd, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
D = str(ROOT / 'data') + '/'
FIG = str(ROOT / 'figures') + '/'
g = pd.read_csv(D + 'nl_gaps.csv', index_col=0)
g.index = pd.PeriodIndex(g.index.str.replace('-', ''), freq='Q').to_timestamp()
g = g.loc['1985':]

plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False})
fig, ax = plt.subplots(2, 1, figsize=(11, 8), sharex=True, gridspec_kw={'height_ratios': [1, 1.4]})

a = ax[0]
a.plot(g.index, g['ratio'], color='#1f3b73', lw=2, label='Credit-to-GDP (private non-financial, %)')
a.plot(g.index, g['ratio'] - g['gap_hp1s'], color='#c0392b', lw=1.4, ls='--', label='One-sided HP trend (real-time, = BIS)')
a.plot(g.index, g['ratio'] - g['gap_hp2s'], color='#7f8c8d', lw=1.4, ls=':', label='Two-sided HP trend (ex-post, 2026 view)')
a.set_ylabel('% of GDP'); a.legend(frameon=False, loc='upper left')
a.set_title('Netherlands: credit-to-GDP and its trend', loc='left', fontweight='bold')

b = ax[1]
b.axhspan(2, 10, color='#f5b041', alpha=0.15, label='Basel buffer-guide band (2–10pp)')
b.axhline(0, color='k', lw=0.6)
b.plot(g.index, g['gap_hp1s'], color='#c0392b', lw=2, label='Real-time gap (one-sided HP, λ=400k) = BIS')
b.plot(g.index, g['gap_hp2s'], color='#7f8c8d', lw=1.5, ls=':', label='Ex-post gap (two-sided HP)')
b.plot(g.index, g['gap_ham20'], color='#27ae60', lw=1.3, alpha=0.8, label='Hamilton gap (h=5y)')
for d, lab, yy, ha in [('2022-04-01', 'May-22: 0→1%  ', 45, 'right'), ('2023-04-01', '  May-23: 1→2%', 30, 'left')]:
    b.axvline(pd.Timestamp(d), color='#1f3b73', lw=1, ls='--')
    b.text(pd.Timestamp(d), yy, lab, fontsize=8, ha=ha, color='#1f3b73')
b.annotate('2012: gap +17pp in a\nhouse-price bust/recession', xy=(pd.Timestamp('2012-04-01'), 16.8), xytext=(pd.Timestamp('2001-06-01'), 42),
           fontsize=8, arrowprops=dict(arrowstyle='->', color='k', lw=0.7))
b.annotate('2007: gap −13pp\nbefore the GFC', xy=(pd.Timestamp('2007-10-01'), -13.4), xytext=(pd.Timestamp('1999-01-01'), -35),
           fontsize=8, arrowprops=dict(arrowstyle='->', color='k', lw=0.7))
b.axvspan(pd.Timestamp('2008-07-01'), pd.Timestamp('2009-07-01'), color='grey', alpha=0.15)
b.text(pd.Timestamp('2008-09-01'), -50, 'GFC', fontsize=8, color='grey')
b.set_ylabel('percentage points'); b.legend(frameon=False, loc='lower left', fontsize=8.5)
b.set_title('Credit-to-GDP gap: what DNB could see vs what we see now', loc='left', fontweight='bold')
fig.text(0.01, 0.005, 'Source: BIS credit-to-GDP statistics (WS_CREDIT_GAP, Q.NL.P.A); own calculations. '
         'Real-time = one-sided HP on current-vintage data (quasi-real-time).', fontsize=7.5, color='grey')
plt.tight_layout(rect=(0, 0.02, 1, 1))
plt.savefig(FIG + 'fig1_nl_credit_gap.png', dpi=180)
print('ok')
