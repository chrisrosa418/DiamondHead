import requests
import json
from pprint import pprint
import time
import urllib2
from urllib2 import Request
from urllib import urlencode
import pandas as pd
import hashlib
import hmac





def _getResult(url_short):
    try:
        url_build = 'https://bittrex.com/api/v1.1/public/{}'.format(url_short)
        response = requests.get(url_build)
        obj = json.loads(response.content)
        response_dict = {k: v for k, v in obj.iteritems()}

    except Exception as e:
        result.error(602, "API connection failed: %s" % e.message)
        return result

    if (response.status_code == 200) and (response_dict['success'] == True):
        pass
    else:
        print 'DEBUG - Response Status Code == {} -- Response Success Message == {}'.format(response.status_code, response_dict['success'])


    return response_dict


def getMarkets():
    response_dict = _getResult('getmarkets')

    currency_dict = {}

    for x in response_dict['result']:
        currency_dict[x['MarketCurrency']] = x['MarketName']

    return currency_dict

def getTicker(currency_pair):
    url = 'getticker?market={}'.format(currency_pair)

    response_dict = _getResult(url)

    return response_dict

def getCurrencies():
    response_dict = _getResult('getcurrencies')


    currency_list = []

    for x in response_dict['result']:
        currency_list.append(x['Currency'])

    return currency_list


def getMarketSummary(currency):
    url = 'getmarketsummary?market={}'.format(currency)
    response_dict = _getResult(url)

    return response_dict

def getMarketSummaries():
    url = 'getmarketsummaries'

    response_dict = _getResult(url)

    return response_dict

def getMarketHistory(currency):
    url = 'getmarkethistory?market={}'.format(currency)

    response_dict = _getResult(url)

    return response_dict

def getOrderHistory():
    key = '4c5880475bdc47eeb48066e4f6fa9f32'
    secret = '75e5e906a1454abfb2fb81b16c5e9298'

    values = {'count': '10'}
    method = 'getorderhistory'

    url = 'https://bittrex.com/api/v1.1/account/'
    url += method + '?' + urlencode(values)
    url += '&apikey=' + key
    url += '&nonce=' + str(int(time.time()))

    signature = hmac.new(secret, url, hashlib.sha512).hexdigest()
    headers = {'apisign': signature}

    req = urllib2.Request(url, headers=headers)

    r = urllib2.urlopen(req)
    return r



#response_dict = getMarketSummaries()

#for k,v in response_dict.iteritems():
#    if k == 'result':
#        result = v

#for i in result:
    #print 'Currency Pair  -- {}    --  Volume  -- {}'.format(i['MarketName'], i['Volume'])

#currency='btc-xrp'
#coin = getMakretSummary(currency)

#print 'Coin -- {}     Volume -- {}'.format(currency, coin[0]['Volume'])
#print getCurrencies()

def parseRecentOrders():
    r = getOrderHistory()
    for i in r:
        app = i

    dict = json.loads(app)
    mm = pd.DataFrame(dict['result'])

    return mm




dict = getMarkets()
#pprint(dict)










