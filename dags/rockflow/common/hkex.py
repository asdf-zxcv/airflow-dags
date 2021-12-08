from typing import Optional

import pandas as pd
from rockflow.common.downloader import Downloader


class HKEX(Downloader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def url(self):
        return "https://www.hkex.com.hk/chi/services/trading/securities/securitieslists/ListOfSecurities_c.xlsx"

    def to_tickers(self, df: Optional[pd.DataFrame]) -> pd.DataFrame:
        result = pd.DataFrame()
        result['raw'] = df.iloc[:, 0]
        result['symbol'] = result['raw'].astype(str)
        result['yahoo'] = result['raw'].apply(
            lambda x: x.strip().replace("^", "-P").replace("/", "-").upper()
        )
        result['futu'] = result['yahoo'].apply(
            lambda x: "%s-US" % x
        )
        result['market'] = pd.Series(["US" for _ in range(len(result.index))])
        return result

    def to_df(self, fp) -> pd.DataFrame:
        return pd.read_excel(
            fp,
            sheet_name='ListOfSecurities',
            header=[2],
            engine='openpyxl',
        )
