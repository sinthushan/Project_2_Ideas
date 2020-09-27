import pandas as pd
import quandl
import os
from dotenv import load_dotenv
from quandl.errors import quandl_error
import yfinance as yf
import datetime
import requests


load_dotenv()
FMP_API_KEY = os.getenv("FMP_API_KEY")
security_basket = ['AAPL', 'MSFT', 'FB']

def createClusters(security_basket):
    fundamental_df = pd.DataFrame()
    for security in security_basket:
        r = requests.get(f'https://financialmodelingprep.com/api/v3/ratios/{security}?limit=1&apikey={FMP_API_KEY}')
        data_json = r.text
        df = pd.read_json(data_json)
        fundamental_df.append(df)
    return df


df = createClusters(security_basket)
