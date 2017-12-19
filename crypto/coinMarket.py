import requests
import json
from pprint import pprint
from datetime import time
import datetime
from BeautifulSoup import BeautifulSoup



def _getResult(url_short):
    try:

        currency = 'cardano'
        dateNow = datetime.datetime.now().strftime("%Y%m%d")
        url_build = 'https://coinmarketcap.com/currencies/{}/historical-data/?start=20130428&end={}'.format(currency, dateNow)
        #url_build = 'https://bittrex.com/api/v1.1/public/{}'.format(url_short)
        response = requests.get(url_build)

        soup = BeautifulSoup(response.content)
        table = soup.findAll('table')

        headers = []
        for x in table:
            rows = ''
            rows = x.findAll('th')
            for row in rows:
                headers.append(row.text)

        body = []
        for x in table:
            rows = ''
            rows = x.findAll('td')
            for row in rows:
                body.append(row.text)



        hLen = int(len(headers))

        bLen = int(len(body))

        for i in range(bLen):
            if bLen % hLen == 0:
                print body[i]


        '''
        for x in 100:
            #what to do every time.
            if x % 5 == 0:
                #what to do every 5th time.
        '''



    except Exception as e:
        result.error(602, "API connection failed: %s" % e.message)
        return result

    if (response.status_code == 200) and (response_dict['success'] == True):
        pass
    else:
        print 'DEBUG - Response Status Code == {} -- Response Success Message == {}'.format(response.status_code, response_dict['success'])


    return response_dict

_getResult('')

