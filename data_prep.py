import numpy as np
import pandas as pd
import logging
import yfinance as yf
from src import CONFIG

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def get_data(start_date, end_date, tickers=['AAPL', 'GOOG', 'BTC-USD']):
    '''
    get data from yf for tickers AAPL, GOOG, BTC-USD
    :return: dataframe
    '''
    # get stock data
    stock_data = {}
    for ticker in tickers:
        stock_data[ticker] = get_stock_data(ticker, start_date, end_date)

        # calculate daily percentage change
        stock_data[ticker]['daily_pct_change'] = (stock_data[ticker]['Adj Close'] - stock_data[ticker]['Adj Close'].shift(-1)) / \
                                           stock_data[ticker]['Adj Close'].shift(-1) * 100

    return stock_data


def data_getter_test():
    start_date = '2020-01-01'
    end_date = '2021-01-01'
    tickers = ['AAPL', 'GOOG', 'BTC-USD', '^GSPC', 'GC=F']
    data = get_data(start_date, end_date, tickers=tickers)
    for ticker in tickers:
        assert isinstance(data[ticker], pd.DataFrame)
        assert isinstance(data[ticker]['daily_pct_change'], pd.Series)
    logging.info('Data getter test passed.')


if __name__ == '__main__':
    data_getter_test()
