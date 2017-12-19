#!/bin/env python


import hmac
import hashlib
import time
import requests
import base64
import json
from requests.auth import AuthBase
from gdax.public_client import PublicClient
from gdax.gdax_auth import GdaxAuth


def get_auth_headers(timestamp, message, api_key, secret_key, passphrase):
    message = message.encode('ascii')
    hmac_key = base64.b64decode(secret_key)
    signature = hmac.new(hmac_key, message, hashlib.sha256)
    signature_b64 = base64.b64encode(signature.digest()).decode('utf-8')
    return {
        'Content-Type': 'Application/JSON',
        'CB-ACCESS-SIGN': signature_b64,
        'CB-ACCESS-TIMESTAMP': timestamp,
        'CB-ACCESS-KEY': api_key,
        'CB-ACCESS-PASSPHRASE': passphrase
    }



url_build = 'https://api-public.sandbox.gdax.com'

try:
    response = requests.get(url_build, auth=HTTPBasicAuth(apikey, password))
except Exception as e:
    result.error(602, "API connection failed: %s" % e.message)
    return result

if response.status_code == 200:
    obj = json.loads(response.content)
    result.trace('DEBUG OBJ', obj)
    response_dict = {k: v for k, v in obj.iteritems()}
    result.trace('DEBUG OBJ', response_dict)
    response_temp = {'hasResponseObj': True}

    # has an extra value total_rows that will be removed
    if queryType == 'DNSRecordResponse':
        response_dict.pop('total_rows')
    # checks for missing malwareObj to override hasResponseObj
    if queryType == 'ipMalwareResponse':
        if not response_dict['malware']:
            response_temp = {'hasResponseObj': False}

    response_dict.update(response_temp)

elif response.status_code == 400:
    result.trace('Bad Request – Invalid request format')

elif response.status_code == 401:
    result.trace('Unauthorized – Invalid API Key')

elif response.status_code == 403:
    result.trace('Forbidden – You do not have access to the requested resource')

elif response.status_code == 404:
    result.trace('Not Found')

elif response.status_code == 500:
    result.trace('	Internal Server Error – We had a problem with our server')

else:
    continue
