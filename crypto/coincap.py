from coinmarketcap import Market
import json
from datetime import datetime
import time


def _getPrice(queryCurrency):
    coinmarketcap = Market()
    response = coinmarketcap.ticker(queryCurrency, limit=3, convert='USD')

    return response


def _displayCurrency(currency):
    # Get current Currency Price
    currencyTicker = _getPrice(currency)

    responseDict = {}

    responseDict[''] =
    last_updated = currencyTicker[0]['last_updated']
    last_updated = time.strftime("%D %H:%M:%S", time.localtime(int(last_updated)))

    currencyName = currencyTicker[0]['name']
    responseDict[''] =
    currencyPrice = currencyTicker[0]['price_usd']
    responseDict[''] =
    percent_change_1h = currencyTicker[0]['percent_change_1h']
    responseDict[''] =
    percent_change_24h = currencyTicker[0]['percent_change_24h']
    responseDict[''] =
    percent_change_7d = currencyTicker[0]['percent_change_7d']
    responseDict[''] =

    return currencyPrice

print _displayCurrency("Bitcoin")
print _displayCurrency("Ripple")
