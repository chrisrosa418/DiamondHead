import os
import numpy as np
import pandas as pd
import pickle
import quandl
from datetime import datetime

import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
#py.init_notebook_mode(connected=True)

QUANDL_API_KEY = 'YZy_BB7WF_ByoCLdKJDR'

quandl.ApiConfig.api_key = os.environ['YZy_BB7WF_ByoCLdKJDR']

btc_usd_price_kraken = get_quandl_data('BCHARTS/KRAKENUSD')
btc_usd_price_kraken.head()





def get_quandl_data(quandl_id):
    '''Download and cache Quandl dataseries'''
    cache_path = '{}.pkl'.format(quandl_id).replace('/','-')
    try:
        f = open(cache_path, 'rb')
        df = pickle.load(f)
        print('Loaded {} from cache'.format(quandl_id))
    except (OSError, IOError) as e:
        print('Downloading {} from Quandl'.format(quandl_id))
        df = quandl.get(quandl_id, returns="pandas")
        df.to_pickle(cache_path)
        print('Cached {} at {}'.format(quandl_id, cache_path))
    return df