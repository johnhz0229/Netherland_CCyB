import pandas as pd, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
D = str(ROOT / 'data') + '/'
FIG = str(ROOT / 'figures') + '/'
gap = pd.read_csv(D + 'nl_gaps.csv', index_col=0)
dsr = pd.read_csv(D + 'nl_dsr.csv', index_col=0)
tc = pd.read_csv(D + 'nl_tc.csv', index_col=0)
spp = pd.read_csv(D + 'nl_spp.csv', index_col=0)
bank = pd.read_csv(D + 'bank_credit_ea.csv', index_col=0)
print('tc cols', list(tc.columns), 'check H+N vs ratio 2022-Q1:', tc.loc['2022-Q1', ['H', 'N']].sum(), gap.loc['2022-Q1', 'ratio'])

# ---------- A. indicator dashboard: level at decision vs 2005-2019 distribution
ind = pd.DataFrame({
    'Credit gap (BIS, pp)': gap['gap_bis'],
    'HH debt/GDP (%)': tc['H'],
    'NFC debt/GDP (%)': tc['N'],
    'DSR private NF (%)': dsr['P'],
    'DSR households (%)': dsr['H'],
    'Real house prices (2010=100)': spp['R628'],
    'Nominal HPI yoy (%)': spp['N771'],
}).loc['2005-Q1':]
hist = ind.loc['2005-Q1':'2019-Q4']
rows = []
for name in ind.columns:
    r = {'indicator': name, 'mean 05-19': hist[name].mean(), 'max 05-19': hist[name].max()}
    for q in ['2007-Q4', '2022-Q1', '2023-Q1', '2026-Q1']:
        v = ind.loc[q, name]
        r[q] = v
        r[q + ' pctile'] = (hist[name] < v).mean() * 100
    rows.append(r)
dash = pd.DataFrame(rows).set_index('indicator')
pd.set_option('display.width', 250)
print(dash.round(1).to_string())
dash.round(2).to_csv(D + 'nl_indicator_dashboard.csv')

# ---------- B. CET1 headroom: robust lower bound using only DNB numbers
# DNB: CCyB 1% = EUR3.3bn (2022) -> domestic exposure RWA base ~EUR330bn; 2% total ~EUR6.7bn
cet1 = {'2021-Q4': 17.7, '2022-Q4': 16.3}   # DNB FSR spring 2022 / 2023
ccyb_eur = {'2021-Q4': 3.3, '2022-Q4': 3.3 + 3.4}
rwa_dom = 330.0
print('\nHeadroom grid (EUR bn), lower bound = headroom computed on domestic RWA only')
out = []
for q, c in cet1.items():
    for req in [10.0, 11.0, 12.0]:            # assumed overall CET1 requirement excl. CCyB (P1+P2R+CCoB+O-SII/SRB)
        for rwa_tot in [rwa_dom, 600, 750]:
            head = (c - req) / 100 * rwa_tot
            out.append([q, c, req, rwa_tot, round(head, 1), ccyb_eur[q], round(ccyb_eur[q] / head * 100, 0)])
hg = pd.DataFrame(out, columns=['date', 'CET1 %', 'req ex-CCyB %', 'RWA bn', 'headroom bn', 'CCyB bn', 'CCyB as % of headroom'])
print(hg.to_string(index=False))
hg.to_csv(D + 'nl_headroom_grid.csv', index=False)

# ---------- B2. CET1 headroom from bank disclosures (replaces the assumption grid as the headline)
# CET1 ratio, total RWA and CET1 requirement / MDA trigger per bank: data/nl_bank_capital.csv (sources inside).
# Numerator = DNB's sector-wide CCyB amount, so the share is an upper bound for the four banks.
bk = pd.read_csv(D + 'nl_bank_capital.csv')
bk['headroom bn'] = (bk['cet1_pct'] - bk['cet1_req_pct']) / 100 * bk['rwa_eur_bn']
print('\nCET1 headroom over requirement / MDA, by bank (EUR bn):')
print(bk[['bank', 'date', 'cet1_pct', 'rwa_eur_bn', 'cet1_req_pct', 'headroom bn']].round(1).to_string(index=False))
agg = bk.groupby('date').agg(rwa=('rwa_eur_bn', 'sum'), headroom=('headroom bn', 'sum'))
agg['CCyB bn'] = agg.index.map(ccyb_eur)
agg['CCyB as % of headroom'] = agg['CCyB bn'] / agg['headroom'] * 100
agg['agg CET1 % (RWA-weighted)'] = bk.assign(c=bk.cet1_pct * bk.rwa_eur_bn).groupby('date')['c'].sum() / agg['rwa']
print(agg.round(1).to_string())
agg.round(2).to_csv(D + 'nl_headroom_actual.csv')

# O-SII cuts effective 31 May 2024 (DNB, June 2023), valued at end-2022 total RWA (consolidated basis).
# BNG (1% -> 0.25%) is not in the bank sample, so the total is a lower bound.
osii_cut_pp = {'ING': 0.5, 'Rabobank': 0.25, 'ABN AMRO': 0.25, 'de Volksbank': 0.75}
r22 = bk[bk.date == '2022-Q4'].set_index('bank')['rwa_eur_bn']
osii_eur = sum(osii_cut_pp[k] / 100 * r22[k] for k in osii_cut_pp)
print(f"\nO-SII cut valued at end-2022 RWA: EUR {osii_eur:.1f}bn (excl. BNG) vs CCyB 1->2% step EUR 3.4bn "
      f"-> net change ~ EUR {3.4 - osii_eur:+.1f}bn")

# ---------- C. bank credit growth NL vs peers (descriptive)
yoy = bank.pct_change(4) * 100
idx = bank / bank.loc['2022-Q1'] * 100
print('\nBank credit to private NF sector, yoy %:')
print(yoy.loc[['2022-Q1', '2022-Q4', '2023-Q2', '2023-Q4', '2024-Q2', '2024-Q4', '2025-Q4', '2026-Q1']].round(1).to_string())
print('\nIndex 2022-Q1=100 at 2024-Q2 (1% effective May-23, 2% effective May-24) and 2026-Q1:')
print(idx.loc[['2023-Q2', '2024-Q2', '2026-Q1']].round(1).to_string())
# naive DiD: NL minus euro area, avg qoq growth pre (2019Q1-2022Q1) vs post (2022Q2-2025Q4)
qoq = bank.pct_change() * 100
pre, post = qoq.loc['2019-Q2':'2022-Q1'], qoq.loc['2022-Q2':'2025-Q4']
did = (post['NL'].mean() - post['XM'].mean()) - (pre['NL'].mean() - pre['XM'].mean())
print(f"\nNaive DiD (NL-EA, avg qoq %): pre {pre['NL'].mean()-pre['XM'].mean():.2f}, post {post['NL'].mean()-post['XM'].mean():.2f}, DiD {did:.2f} pp/qtr")

# ---------- Figures
plt.rcParams.update({'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
fig, ax = plt.subplots(2, 2, figsize=(12, 7.5))
t = pd.PeriodIndex(ind.index.str.replace('-', ''), freq='Q').to_timestamp()
dec = [pd.Timestamp('2022-04-01'), pd.Timestamp('2023-04-01')]

def mark(a):
    for d in dec:
        a.axvline(d, color='#1f3b73', ls='--', lw=0.9)

a = ax[0, 0]
a.plot(t, ind['Real house prices (2010=100)'], color='#c0392b', lw=2)
a.axhline(hist['Real house prices (2010=100)'].max(), color='grey', ls=':', lw=1)
a.text(t[0], hist['Real house prices (2010=100)'].max() + 2, 'pre-GFC peak', fontsize=8, color='grey')
a.set_title('Real residential property prices (2010=100)', loc='left', fontweight='bold'); mark(a)

a = ax[0, 1]
a.plot(t, ind['HH debt/GDP (%)'], color='#1f3b73', lw=2, label='Households')
a.plot(t, ind['NFC debt/GDP (%)'], color='#27ae60', lw=2, label='Non-financial corporates')
a.set_title('Debt-to-GDP by sector (%)', loc='left', fontweight='bold'); a.legend(frameon=False); mark(a)

a = ax[1, 0]
a.plot(t, ind['DSR households (%)'], color='#1f3b73', lw=2, label='Households')
a.plot(t, ind['DSR private NF (%)'], color='#8e44ad', lw=2, label='Private non-financial')
a.set_title('Debt service ratio (% of income)', loc='left', fontweight='bold'); a.legend(frameon=False); mark(a)

a = ax[1, 1]
tb = pd.PeriodIndex(idx.index.str.replace('-', ''), freq='Q').to_timestamp()
for c, col, lw in [('NL', '#c0392b', 2.4), ('XM', 'k', 1.8), ('DE', '#7f8c8d', 1), ('FR', '#2980b9', 1), ('BE', '#f39c12', 1), ('AT', '#27ae60', 1)]:
    a.plot(tb, idx[c], color=col, lw=lw, label={'XM': 'Euro area'}.get(c, c))
a.axvline(pd.Timestamp('2023-04-01'), color='#1f3b73', ls=':', lw=0.9)
a.axvline(pd.Timestamp('2024-04-01'), color='#1f3b73', ls=':', lw=0.9)
a.text(pd.Timestamp('2023-05-01'), 84, '1% binding', fontsize=7.5, color='#1f3b73')
a.text(pd.Timestamp('2024-05-01'), 84, '2% binding', fontsize=7.5, color='#1f3b73')
a.set_title('Bank credit to private NF sector (index 2022Q1=100)', loc='left', fontweight='bold')
a.legend(frameon=False, ncol=3, fontsize=8)
fig.text(0.01, 0.005, 'Source: BIS (WS_TC, WS_DSR, WS_SPP); own calculations. Dashed lines: CCyB announcements May-22 and May-23.', fontsize=7.5, color='grey')
plt.tight_layout(rect=(0, 0.02, 1, 1))
plt.savefig(FIG + 'fig2_nl_indicators.png', dpi=170)
print('saved')
