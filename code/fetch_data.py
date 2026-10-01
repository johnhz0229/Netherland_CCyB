"""Re-download all BIS series used in this project (SDMX REST v2, CSV) and compare with the snapshot.

Usage:
    python code/fetch_data.py            -> writes fresh files to data/fresh/ and prints a diff vs data/
    python code/fetch_data.py --replace  -> same, then overwrites data/*.csv with the fresh files

The snapshot in data/ was downloaded on 2026-10-01. As of 2026-10-01 this script has still not been run
successfully: stats.bis.org is blocked by the sandbox egress policy (HTTP 403 on CONNECT).
Changes vs the first draft (which had never been executed):
  - writes to data/fresh/ by default instead of silently overwriting the snapshot
  - sends an SDMX-CSV Accept header (the v2 API negotiates format via Accept; ?format=csv kept as fallback)
  - retries with backoff; clear error if the host is unreachable
  - output index/column names match the snapshot files so the diff is like-for-like
  - nl_tc.csv: column P is private non-financial debt/GDP. NOTE: in the 2026-10-01 snapshot column P
    is a copy of the DSR series (data/nl_dsr.csv, P); no script uses it, but a refresh will fix it.
"""
import io
import sys
import time
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
FRESH = DATA / 'fresh'
BASE = 'https://stats.bis.org/api/v2/data/dataflow/BIS/{flow}/{ver}/{key}'
HEADERS = {'Accept': 'application/vnd.sdmx.data+csv;version=1.0.0'}


def get(flow, ver, key, start=None):
    params = {'format': 'csv'}
    if start:
        params['startPeriod'] = start
    url = BASE.format(flow=flow, ver=ver, key=key)
    for i, wait in enumerate([0, 2, 4, 8, 16]):
        time.sleep(wait)
        try:
            r = requests.get(url, params=params, headers=HEADERS, timeout=60)
            r.raise_for_status()
            df = pd.read_csv(io.StringIO(r.text))
            df['OBS_VALUE'] = pd.to_numeric(df['OBS_VALUE'], errors='coerce')
            return df
        except requests.RequestException as e:
            if i == 4:
                sys.exit(f'Could not download {flow}/{key}: {e}')


def wide(df, col, index_name='q'):
    out = df.pivot_table(index='TIME_PERIOD', columns=col, values='OBS_VALUE').sort_index()
    out.index.name = index_name
    out.columns.name = None
    return out


def fetch():
    FRESH.mkdir(exist_ok=True)
    # 1. Credit-to-GDP ratio (A), HP trend (B), gap (C) -- private non-financial sector
    g = wide(get('WS_CREDIT_GAP', '1.0', 'Q.NL.P.A.A+B+C'), 'CG_DTYPE', index_name=None)
    g = g.rename(columns={'A': 'ratio', 'B': 'trend_bis', 'C': 'gap_bis'})[['ratio', 'trend_bis', 'gap_bis']]
    g.to_csv(FRESH / 'nl_bis.csv')

    # 2. Debt-to-GDP by sector (H households, N NFCs, P private non-fin), % of GDP
    wide(get('WS_TC', '2.0', 'Q.NL.H+N+P.A.M.770.A', '2005-Q1'), 'TC_BORROWERS').to_csv(FRESH / 'nl_tc.csv')

    # 3. Household debt in EUR bn
    h = get('WS_TC', '2.0', 'Q.NL.H.A.M.XDC.A', '2015-Q1')[['TIME_PERIOD', 'OBS_VALUE']]
    h.columns = ['quarter', 'hh_debt_eur_bn']
    h.sort_values('quarter').to_csv(FRESH / 'nl_household_debt_eur.csv', index=False)

    # 4. Debt service ratios
    wide(get('WS_DSR', '1.0', 'Q.NL.P+H+N', '2005-Q1'), 'DSR_BORROWERS').to_csv(FRESH / 'nl_dsr.csv')

    # 5. Residential property prices: N/R = nominal/real; 628 = index 2010=100, 771 = yoy %
    p = get('WS_SPP', '1.0', 'Q.NL.N+R.628+771', '2005-Q1')
    p['s'] = p['VALUE'] + p['UNIT_MEASURE'].astype(str)
    wide(p, 's').to_csv(FRESH / 'nl_spp.csv')

    # 6. Bank credit to private non-fin sector, national currency, NL vs peers (XM = euro area)
    wide(get('WS_TC', '2.0', 'Q.NL+DE+FR+BE+AT+XM.P.B.M.XDC.A', '2019-Q1'), 'BORROWERS_CTY').to_csv(FRESH / 'bank_credit_ea.csv')

    # 7. Household debt/GDP international comparison
    i = get('WS_TC', '2.0', 'Q.NL+XM+DE+FR+US+CH+DK+SE+NO+AU+GB+CA.H.A.M.770.A', '2022-Q1')
    i = i[i.TIME_PERIOD == '2022-Q1'][['BORROWERS_CTY', 'OBS_VALUE']]
    i.columns = ['country', 'hh_debt_pct_gdp_2022Q1']
    i.sort_values('hh_debt_pct_gdp_2022Q1', ascending=False).to_csv(FRESH / 'hh_debt_gdp_intl_2022Q1.csv', index=False)


FILES = ['nl_bis.csv', 'nl_tc.csv', 'nl_household_debt_eur.csv', 'nl_dsr.csv', 'nl_spp.csv',
         'bank_credit_ea.csv', 'hh_debt_gdp_intl_2022Q1.csv']


def compare(tol=1e-6):
    """Print new periods, dropped periods and revised values (abs diff > tol) per file."""
    for f in FILES:
        old = pd.read_csv(DATA / f, index_col=0)
        new = pd.read_csv(FRESH / f, index_col=0)
        added = new.index.difference(old.index)
        dropped = old.index.difference(new.index)
        common_i = old.index.intersection(new.index)
        common_c = old.columns.intersection(new.columns)
        o, n = old.loc[common_i, common_c], new.loc[common_i, common_c]
        d = (n - o).abs()
        d = d.where(o.isna() == n.isna(), float('inf'))  # value appeared or disappeared
        rev = d.stack()
        rev = rev[rev > tol]
        print(f'\n{f}: +{len(added)} new periods {list(added)[:6]}, -{len(dropped)} dropped, '
              f'{len(rev)} revised values (max abs diff {d.max().max():.4g})')
        if len(rev):
            print(rev.sort_values(ascending=False).head(10).to_string())


if __name__ == '__main__':
    fetch()
    compare()
    if '--replace' in sys.argv:
        for f in FILES:
            (DATA / f).write_bytes((FRESH / f).read_bytes())
        print('\nSnapshot replaced. Re-run: python code/gap.py && python code/fig1.py && python code/other.py')
