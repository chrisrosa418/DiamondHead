import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import json
from mailchimp3 import MailChimp




''''
Fetch data
(1) Fetch top 5 news articles
 (1.a) Top 5 editors choice, top 5 hot items
(2) Use coinCap functions to fetch
 (2.a) Top 5 market cap (and movers)
 (2.b) Top movers (price, volume, percentage)
 (2.c) Top 5 ICO's
 (2.d) Top 5 Exchanges
 (2.e) ICO of the day/week

Prepare email
(1) Grab db/variable data from fetch data step and populate html file

Upload email to MailChimp

'''




class Resturant(object):
    backrupt = False
    def open_branch(self):
        if not self.backrupt:
            print "branch opened"



def fetchNews():
    apikey = '312542dcf2df4262beed0a06a9d98796'

    url = ('https://newsapi.org/v2/top-headlines?sources=crypto-coins-news&apiKey={}'.format(apikey))
    response = requests.get(url)
    responseJson = json.loads(response.content)

    return responseJson

#news = fetchNews()



class FinancialData(object):
    def getMarkets(self):
        response_dict = _getResult('getmarkets')

        currency_dict = {}

        for x in response_dict['result']:
            currency_dict[x['MarketCurrency']] = x['MarketName']

        return currency_dict

    def getMarketSummaries(self):
        url = 'getmarketsummaries'

        response_dict = _getResult(url)

        return response_dict

    def _getResult(self, url_short):
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


market = getMarketSummaries()


def mailChimp():
    client = MailChimp(mc_api='7972ada36e993d5c806bbc71884c5f15-us18', mc_user='tokencrunch')
    client.lists.members.all('123456', count=100, offset=0)
    client.templates.update(template_id='18687', data={'name': 'apitest', 'html': '<html>update</html>'})




