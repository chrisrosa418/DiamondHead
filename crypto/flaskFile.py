from flask import Flask
from coinmarketcap import Market
import time
from datetime import datetime

app = Flask(__name__)

@app.route('/')

def index():
    apples = 'app'
    bitcoin = _displayCurrency("Bitcoin")
    return bitcoin

def _getPrice(queryCurrency):
    coinmarketcap = Market()
    response = coinmarketcap.ticker(queryCurrency, limit=3, convert='USD')

    return response
def _displayCurrency(currency):
    #Get current Currency Price
    currencyTicker = _getPrice(currency)

    last_updated = currencyTicker[0]['last_updated']
    last_updated = time.strftime("%D %H:%M:%S", time.localtime(int(last_updated)))

    currencyName = currencyTicker[0]['name']
    currencyPrice = currencyTicker[0]['price_usd']
    percent_change_1h = currencyTicker[0]['percent_change_1h']
    percent_change_24h = currencyTicker[0]['percent_change_24h']
    percent_change_7d = currencyTicker[0]['percent_change_7d']

    return currencyPrice

if __name__ == "__main__":
    app.run(debug=True)
