import bittrex

#response_dict = getMarketSummaries()
#print bittrex.getMakretSummary('BTC-XRP')


def getVolume(currency_pair):
    data = bittrex.getMarketSummary(currency_pair)

    volumeDict = {}

    volumeDict['currencyPair'] = currency_pair

    for k, v in data.iteritems():
        if k == 'result':
            result = v

    for i in result:
        volumeDict['Volume'] = i['Volume']
        volumeDict['BaseVolume'] = i['BaseVolume']

    return volumeDict

def getPrice(currency_pair):
    data = bittrex.getMarketSummary(currency_pair)

    priceDict = {}

    priceDict['currencyPair'] = currency_pair

    for k, v in data.iteritems():
        if k == 'result':
            result = v

    for i in result:
        priceDict['Last'] = i['Last']

    return priceDict

def getTopBaseVolume():
    data = bittrex.getMarketSummaries()

    for k, v in data.iteritems():
        if k == 'result':
            result = v

    marketDict = {}

    for i in result:
        marketDict['PrevDay'] = i['PrevDay']
        marketDict['Volume'] = i['Volume']
        marketDict['Last'] = i['Last']
        marketDict['OpenSellOrders'] = i['OpenSellOrders']
        marketDict['TimeStamp'] = i['TimeStamp']
        marketDict['Bid'] = i['Bid']
        marketDict['Created'] = i['Created']
        marketDict['OpenBuyOrders'] = i['OpenBuyOrders']
        marketDict['High'] = i['High']
        marketDict['MarketName'] = i['MarketName']
        marketDict['Low'] = i['Low']
        marketDict['Ask'] = i['Ask']
        marketDict['BaseVolume'] = i['BaseVolume']

    return result

def test():
    base = getTopBaseVolume()

    pa = pd.DataFrame(base)

    sort = pa.sort_values('BaseVolume')

    apples = sort.tail(20)

def getHtml():
    base = getTopBaseVolume()
    pa = pd.DataFrame(base)
    zz = pa.sort_values('Volume').tail(10)
    zz.to_html('f.html')


import pandas as pd
from collections import OrderedDict
from datetime import date
from pandas.io.json import json_normalize


data = bittrex.getMarketSummaries()


for k,v in data.iteritems():
    if k == 'result':
        result = v

#pprint(result)

ada = bittrex.getMarketSummary('BTC-ADA')
