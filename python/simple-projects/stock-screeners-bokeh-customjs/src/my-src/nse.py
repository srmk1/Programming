from typing import Union, Optional, List, Dict, Tuple, TextIO, Any
import requests
import bs4

#
# References:
# https://github.com/VarunS2002/Python-NSE-Option-Chain-Analyzer/blob/master/NSE_Option_Chain_Analyzer.py
#
class nse:
    indices: List[str] = []
    stocks: List[str] = []
    headers: Dict[str, str] = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'accept-language': 'en,gu;q=0.9,hi;q=0.8',
        'accept-encoding': 'gzip, deflate, br'
    }
    url_symbols: str = "https://www.nseindia.com/products-services/" \
                       "equity-derivatives-list-underlyings-information"
    url_index_option_chain: str = "https://www.nseindia.com/api/option-chain-indices?symbol="
    url_option_chain: str = "https://www.nseindia.com/option-chain"

    def get_index_stock_derivatives_from_nse_website(self):
        try:
            symbols_information: requests.Response = requests.get(self.url_symbols, headers=self.headers)
            symbols_information_soup: bs4.BeautifulSoup = bs4.BeautifulSoup(symbols_information.content, "html.parser")
        except Exception as err:
            print("Error")

        try:
            symbols_table: bs4.element.Tag = symbols_information_soup.findChildren('table')[0]
        except IndexError as err:
            print("Error1")

        symbols_table_rows: List[bs4.element.Tag] = list(symbols_table.findChildren(['th', 'tr']))
        symbols_table_rows_str: List[str] = ['' for _ in range(len(symbols_table_rows) - 1)]
        for column in range(len(symbols_table_rows) - 1):
            symbols_table_rows_str[column] = str(symbols_table_rows[column])
            divider_row: str = '<tr>\n' \
                           '<td colspan="3"><strong>Derivatives on Individual Securities</strong></td>\n' \
                           '</tr>'
        for column in range(4, symbols_table_rows_str.index(divider_row) + 1):
            cells: bs4.element.ResultSet = symbols_table_rows[column].findChildren('td')
            column: int = 0
            for cell in cells:
                if column == 2:
                    self.indices.append(cell.string)
                column += 1
        for column in reversed(range(symbols_table_rows_str.index(divider_row) + 1)):
            symbols_table_rows.pop(column)

        for row in symbols_table_rows:
            cells: bs4.element.ResultSet = row.findChildren('td')
            column: int = 0
            for cell in cells:
                if column == 2:
                    self.stocks.append(cell.string)
                column += 1

        return self.indices, self.stocks

    # Returns dictionary of the
    # https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY
    # dict['records']['data'] contains all the records
    def get_index_option_chain(self, symbol):
        session: requests.Session = requests.Session()

        url = self.url_index_option_chain + symbol
        try:
            request = session.get(self.url_option_chain, headers=self.headers, timeout=5)
            cookies = dict(request.cookies)
            response = session.get(url, headers=self.headers, timeout=5, cookies=cookies)
        except Exception as err:
            print(request)
            print(response)

        if response is not None:
            try:
                json_data = response.json()
            except Exception as err:
                print(response)
                json_data = {}

        return json_data

