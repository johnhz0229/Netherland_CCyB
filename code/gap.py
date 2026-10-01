import numpy as np, pandas as pd
from scipy import sparse
from scipy.sparse.linalg import spsolve

from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
D = str(ROOT / 'data') + '/'
FIG = str(ROOT / 'figures') + '/'
df = pd.read_csv(D + 'nl_bis.csv', index_col=0)
y_all = df['ratio']
LAM = 400_000


def hp_trend(y, lam=LAM):
    y = np.asarray(y, float)
    n = len(y)
    e = np.ones(n)
    Dm = sparse.diags([e[:-2], -2 * e[:-2], e[:-2]], [0, 1, 2], shape=(n - 2, n))
    A = sparse.eye(n) + lam * (Dm.T @ Dm)
    return spsolve(A.tocsc(), y)


def one_sided(y, lam=LAM, min_obs=40):
    out = np.full(len(y), np.nan)
    for t in range(min_obs - 1, len(y)):
        out[t] = hp_trend(y[: t + 1], lam)[-1]
    return out


def hamilton(y, h, p=4):
    """full-sample Hamilton regression filter: y_{t+h} on const, y_t..y_{t-p+1}"""
    y = np.asarray(y, float)
    n = len(y)
    idx = np.arange(p - 1 + h, n)
    X = np.column_stack([np.ones(len(idx))] + [y[idx - h - j] for j in range(p)])
    b, *_ = np.linalg.lstsq(X, y[idx], rcond=None)
    cyc = np.full(n, np.nan)
    cyc[idx] = y[idx] - X @ b
    return cyc


def hamilton_rt(y, h, p=4, min_obs=60):
    """real-time Hamilton: at each t, estimate using data up to t only"""
    y = np.asarray(y, float)
    n = len(y)
    out = np.full(n, np.nan)
    for t in range(min_obs, n):
        out[t] = hamilton(y[: t + 1], h, p)[-1]
    return out


# --- 1. Replicate BIS one-sided gap: try start years
res = {}
for start in ['1961-Q1', '1970-Q1', '1980-Q1']:
    y = y_all.loc[start:].values
    tr = one_sided(y)
    s = pd.Series(y - tr, index=y_all.loc[start:].index)
    cmp = pd.concat([s, df['gap_bis']], axis=1).dropna()
    res[start] = (cmp.iloc[:, 0] - cmp.iloc[:, 1]).abs().mean()
print('mean abs diff vs BIS gap by start:', res)

y = y_all.values
idx = y_all.index
out = pd.DataFrame(index=idx)
out['ratio'] = y
out['gap_bis'] = df['gap_bis']
out['gap_hp1s'] = y - one_sided(y)            # real-time-style (one-sided) HP
out['gap_hp2s'] = y - hp_trend(y)             # ex-post two-sided HP (end-2026 view)
out['gap_ham8'] = hamilton(y, 8)              # Hamilton h=2y, ex-post
out['gap_ham20'] = hamilton(y, 20)            # Hamilton h=5y (credit-cycle horizon), ex-post
out['gap_ham8_rt'] = hamilton_rt(y, 8)
out['gap_ham20_rt'] = hamilton_rt(y, 20)

# "vintage" gaps: what a two-sided HP would have shown with data up to decision date
for q in ['2022-Q1', '2023-Q1']:
    t = list(idx).index(q)
    tr = hp_trend(y[: t + 1])
    out.loc[q, 'gap_hp2s_vintage'] = y[t] - tr[-1]

# 5y and 3y change in credit-to-GDP (simple growth indicator)
out['chg_3y'] = out['ratio'] - out['ratio'].shift(12)
out['chg_5y'] = out['ratio'] - out['ratio'].shift(20)

out.to_csv(D + 'nl_gaps.csv')
pts = ['2007-Q4', '2008-Q4', '2012-Q2', '2016-Q1', '2019-Q4', '2020-Q1', '2021-Q4',
       '2022-Q1', '2022-Q2', '2023-Q1', '2023-Q2', '2024-Q4', '2026-Q1']
pd.set_option('display.width', 200)
print(out.loc[pts].round(1).to_string())

# Basel buffer guide mapping: 0 if gap<2, 2.5 if gap>10, linear between
def guide(g):
    return np.clip((g - 2) / 8 * 2.5, 0, 2.5)
print('\nBasel buffer guide at decisions:')
for q in ['2022-Q1', '2023-Q1']:
    print(q, {c: round(float(guide(out.loc[q, c])), 2) for c in ['gap_bis', 'gap_hp1s', 'gap_hp2s', 'gap_ham8', 'gap_ham20']})

# Historical: when did gap exceed 2pp / 10pp (BIS & own one-sided)
for c in ['gap_hp1s', 'gap_ham20']:
    s = out[c].dropna()
    print(c, 'quarters >2pp since 1975:', (s.loc['1975-Q1':] > 2).sum(), 'of', len(s.loc['1975-Q1':]),
          '| last >2pp:', s[s > 2].index[-1] if (s > 2).any() else None)
