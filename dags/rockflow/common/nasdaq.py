from rockflow.common.downloader import Downloader
from rockflow.common.utils import user_agent


class Nasdaq(Downloader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def url(self):
        return "https://api.nasdaq.com/api/screener/stocks"

    @property
    def params(self):
        return {
            'tableonly': 'false',
            'limit': 0,
            'offset': 0,
            'download': 'true',
        }

    @property
    def headers(self):
        return {
            "Accept": "application/json, text/plain, */*",
            "DNT": "1",
            "Origin": "https://www.nasdaq.com",
            "Referer": "www.google.com",
            "Sec-Fetch-Mode": "cors",
            "User-Agent": user_agent,
        }

    # def _to_tickers(self) -> pd.DataFrame:
    #     result = pd.DataFrame()
    #     result['raw'] = self.csv_df()['symbol']
    #     result['symbol'] = result['raw'].astype(str)
    #     result['yahoo'] = result['raw'].apply(
    #         lambda x: x.strip().replace("^", "-P").replace("/", "-").upper()
    #     )
    #     result['futu'] = result['yahoo'].apply(
    #         lambda x: "%s-US" % x
    #     )
    #     result['market'] = pd.Series(["US" for _ in range(len(result.index))])
    #     return result

    # def _to_df(self) -> pd.DataFrame:
    #     response = json.load(self.oss())
    #     return pd.DataFrame(
    #         response.get('data').get(
    #             'table', response.get('data')
    #         ).get('rows')
    #     )