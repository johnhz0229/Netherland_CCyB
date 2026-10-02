"""Download the macro series for the slide-7 chart from the ECB Data Portal -> data/nl_macro.csv.

Series (ECB Data Portal, SDMX API):
  MNA.Q.Y.NL.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.LR.N  Dutch real GDP (chain-linked volumes, s.a.)
  ICP.M.NL.N.000000.4.ANR                       Dutch HICP inflation, % y/y
  FM.D.U2.EUR.4F.KR.DFR.LEV                     ECB deposit facility rate, %
Usage (repo root): python code/fetch_macro.py
"""
import io
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
API = 'https://data-api.ecb.europa.eu/service/data/'
SERIES = {'gdp': 'MNA/Q.Y.NL.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.LR.N',
          'hicp': 'ICP/M.NL.N.000000.4.ANR',
          'dfr': 'FM/D.U2.EUR.4F.KR.DFR.LEV'}


def get(key):
    r = requests.get(API + key, params={'format': 'csvdata', 'startPeriod': '2018-01-01'}, timeout=60)
    r.raise_for_status()
    d = pd.read_csv(io.StringIO(r.text))
    return d.set_index('TIME_PERIOD')['OBS_VALUE']


def main():
    out = []
    for name, key in SERIES.items():
        s = get(key)
        if name == 'gdp':
            s.index = pd.PeriodIndex(s.index.str.replace('-', ''), freq='Q').to_timestamp(how='end').normalize()
            s = s / s[pd.Timestamp('2019-12-31')] * 100      # index, 2019Q4 = 100
            s.index = s.index.to_period('M').to_timestamp()  # quarter -> last month of quarter
        elif name == 'hicp':
            s.index = pd.to_datetime(s.index)
        else:
            s.index = pd.to_datetime(s.index)
            s = s.resample('MS').last()
        out.append(s.rename(name))
    df = pd.concat(out, axis=1).sort_index()
    df.index.name = 'month'
    df.to_csv(ROOT / 'data' / 'nl_macro.csv', float_format='%.3f')
    print(df.dropna(how='all').tail(3))
    print('HICP 2022 average:', round(df.loc['2022', 'hicp'].mean(), 1))


if __name__ == '__main__':
    main()
