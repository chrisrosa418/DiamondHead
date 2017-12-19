#!/bin/env python
import requests
from requests.auth import AuthBase
import base64, hashlib, hmac, time
import json

class GDAXRequestAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message.encode('utf-8'), hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest())
        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request

def products():
    response = requests.get(api_base + '/products')
    # check for invalid api response
    if response.status_code is not 200:
        raise Exception('Invalid GDAX Status Code: %d' % response.status_code)
    return response.json()

api_base = 'https://api-public.sandbox.gdax.com'
api_key = 'd08ea2ca6f3664eb7942735b9af771a0'
api_secret = 'dQuh6C650UGhbZK733CiW2EiQJ4KCsysLWcnMBCz2vtBRDQ/boQhwf0FhYDjfyDV5Ax8AcdP2nO2BmcjiOse3w=='
passphrase = 'tdf5xoiwpv'

auth = GDAXRequestAuth(api_key, api_secret, passphrase)

order_url = api_base + '/orders'
order_data = {
    'type': 'market',
    'side': 'buy',
    'product_id': 'BTC-USD',
    'size': '0.01'
}



response = requests.post(order_url, data=json.dumps(order_data), auth=auth)



#requests.post(order_url, data=data, headers=headers)

print(response.json())


909  fso package list | grep fireeye.hx
  910  fso package list | grep fireeye.hx | gawk '{print "fso package uninstall $2"}'
  911  fso package list | grep fireeye.hx | grep -v 112 | gawk '{print "fso package uninstall "$2}'
  912  fso package list | grep fireeye.hx | grep -v 112 | gawk '{print "fso package uninstall "$2}' | > do.sh
  915  fso package list | grep fireeye.hx | grep -v 112 | gawk '{print "fso package uninstall "$2}' > do.sh
  923  fso package install fireeye.hx.2.2.2.tar
  924  fso package list


