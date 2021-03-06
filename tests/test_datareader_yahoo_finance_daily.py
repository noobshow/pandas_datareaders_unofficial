#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Run unit tests using
nosetests -s -v
"""

import time
import datetime
from datetime import timedelta

import pandas as pd
from pandas_datareaders_unofficial import DataReader

import pandas.io.data as web

expire_after = timedelta(hours=1) # 0:no cache - None:no cache expiration

def test_yahoo_finance_daily():

    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime(2013, 1, 27)

    symbol = "F"
    symbol = "AAPL"
    #symbol = ["AAPL", 'F']

    print("="*5 + "New DataReader" + "="*5)
    data = DataReader("YahooFinanceDaily", expire_after=expire_after).get(symbol, start, end)
    assert(isinstance(data, pd.DataFrame))
    print(data)
    print(type(data))
    print(data.dtypes)

    print("="*5 + "Pandas original DataReader" + "="*5)

    f = web.DataReader(symbol, 'yahoo', start, end)
    print(f)
    print(type(f))
    print(f.ix['2010-01-04'])
    print(f.dtypes)

    diff = f-data
    
    assert(diff.sum().sum()==0)

    print("="*5 + "New DataReader with multi symbols" + "="*5)
    symbol = ["AAPL", 'F']
    data = DataReader("YahooFinanceDaily", expire_after=expire_after).get(symbol, start, end)
    print(data)
    print(type(data))
    print(data.dtypes)
