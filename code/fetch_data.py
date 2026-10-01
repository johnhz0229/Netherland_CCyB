"""Re-download all BIS series used in this project (SDMX REST v2, CSV).

Usage:  python code/fetch_data.py        -> writes data/*.csv (overwrites the snapshot)
The snapshot in data/ was downloaded on 2026-10-01; run this to refresh/verify it.
NOTE: written in a sandbox without access to stats.bis.org, so it has not been executed;
check the output shapes against the snapshot files before relying on it.
"""
import io
from pathlib import Path
import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
BASE = 'https://stats.bis.org/api/v2/data/dataflow/BIS/{flow}/{ver}/{key}'


def get(flow, ver, key, start=None):
    params = {'format': 'csv'}
    if start:
        params['startPeriod'] = start
    r = requests.get(BASE.format(flow=flow, ver=ver, key=key), params=params, timeout=60)
    r.raise_for_status()
    return pd.read_csv(io.StringIO(r.text))


def wide(df, col):
    return df.pivot_table(index='TIME_PERIOD', columns=col, values='OBS_VALUE').sort_index()


# 1. Credit-to-GDP ratio (A), HP trend (B), gap (C) -- private non-financial sector
g = wide(get('WS_CREDIT_GAP', '1.0', 'Q.NL.P.A.A+B+C'), 'CG_DTYPE')
g = g.rename(columns={'A': 'ratio', 'B': 'trend_bis', 'C': 'gap_bis'})[['ratio', 'trend_bis', 'gap_bis']]
g.to_csv(DATA / 'nl_bis.csv')

# 2. Debt-to-GDP by sector (H households, N NFCs, P private non-fin), % of GDP
wide(get('WS_TC', '2.0', 'Q.NL.H+N+P.A.M.770.A', '2005-Q1'), 'TC_BORROWERS').to_csv(DATA / 'nl_tc.csv')

# 3. Household debt in EUR bn
h = get('WS_TC', '2.0', 'Q.NL.H.A.M.XDC.A', '2015-Q1')[['TIME_PERIOD', 'OBS_VALUE']]
h.columns = ['quarter', 'hh_debt_eur_bn']
h.to_csv(DATA / 'nl_household_debt_eur.csv', index=False)

# 4. Debt service ratios
wide(get('WS_DSR', '1.0', 'Q.NL.P+H+N', '2005-Q1'), 'DSR_BORROWERS').to_csv(DATA / 'nl_dsr.csv')

# 5. Residential property prices: N/R = nominal/real; 628 = index 2010=100, 771 = yoy %
p = get('WS_SPP', '1.0', 'Q.NL.N+R.628+771', '2005-Q1')
p['s'] = p['VALUE'] + p['UNIT_MEASURE'].astype(str)
wide(p, 's').to_csv(DATA / 'nl_spp.csv')

# 6. Bank credit to private non-fin sector, national currency, NL vs peers (XM = euro area)
wide(get('WS_TC', '2.0', 'Q.NL+DE+FR+BE+AT+XM.P.B.M.XDC.A', '2019-Q1'), 'BORROWERS_CTY').to_csv(DATA / 'bank_credit_ea.csv')

# 7. Household debt/GDP international comparison
i = get('WS_TC', '2.0', 'Q.NL+XM+DE+FR+US+CH+DK+SE+NO+AU+GB+CA.H.A.M.770.A', '2022-Q1')
i = i[i.TIME_PERIOD == '2022-Q1'][['BORROWERS_CTY', 'OBS_VALUE']]
i.columns = ['country', 'hh_debt_pct_gdp_2022Q1']
i.sort_values('hh_debt_pct_gdp_2022Q1', ascending=False).to_csv(DATA / 'hh_debt_gdp_intl_2022Q1.csv', index=False)
print('done')
