#!/bin/env python
import requests
from requests.auth import AuthBase
import base64, hashlib, hmac, time
import json

class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').rstrip('\n')

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request


api_url = 'https://api.gdax.com/'
api_key = 'b5ffca6591c1bcf30173f2d20f9bcf3a'
api_secret = 'S27BLPE42IpDB3XnqX1ellrZnuCfJ72hEzftKTBDYqQssWGZEaDxmdiWhwrmp1IYwEd+Rfz9u0XQ+ja/sveKHg=='
passphrase = 'rd207a8uxme'

auth = CoinbaseExchangeAuth(api_key, api_secret, passphrase)

#Get Account
r = requests.get(api_url + 'accounts', auth=auth)

#Get BTC Price
startTime = '2017-12-01T20:00:00.578544Z'
endTime = '2017-12-01T23:00:00.578544Z'
granularity = 600

order_data = {'start': startTime, 'end': endTime, 'granularity': granularity}

r = requests.get(api_url + '/products/BTC-USD/candles', params=order_data, auth=auth)

def _getHistoricalData():
    print 'test'


    currencyId = 'BTC-USD'
    addUrl = '/products/{}/candles'.format(currencyId)

    startTime = '2017-12-01'
    endTime = '2017-12-02'
    granularity = 60

    order_data = {'start': startTime, 'end': endTime, 'granularity': granularity}

    order_url = api_url + '/orders'
    order = {
        'size': 1.0,
        'price': 1.0,
        'side': 'buy',
        'product_id': 'BTC-USD',
    }




#response = requests.post(order_url, data=json.dumps(order_data), auth=auth)



#requests.post(order_url, data=data, headers=headers)

print(response.json())





def products():
    response = requests.get(api_base + '/products')
    # check for invalid api response
    if response.status_code is not 200:
        raise Exception('Invalid GDAX Status Code: %d' % response.status_code)
    return response.json()


