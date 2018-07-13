from __future__ import print_function
import time

from pprint import pprint
import requests

# create an instance of the API class

authentication_token = 3.4 # float | User athentication uuid (optional)
start = 56 # int | Start query value (optional)
length = 56 # int | Number of rows query (optional)
draw = 56 # int | Number of times table has been reloaded (optional)
q = 'q_example' # str | Values provided in q are tokenized and search on columns: TICKET_ID,SUBJECT,REQUESTOR_UERNAME, REQUESTOR_EMAIL, TICKET_MESSAGES (optional)
sort_by = 'sort_by_example' # str | Column name to order table by (optional)
sort_by_order = 'sort_by_order_example' # str | Sort by ascending or descending (optional)
passed_account_id = 'passed_account_id_example' # str |  (optional)
passed_user_id = 'passed_user_id_example' # str |  (optional)
view_id = 56 # int | View Id (optional)
client_id = '7a564d5a-4fd0-11e8-8b57-ac1ff8470000'
client_secret = 'jv7iuOez2AC0HhFhuLEVXEYpzDe1zUX5'
#var queryUrl = `https://api.ngdesk.com/v2/operations/get_tickets?client_secret=${client_secret}&client_id=${client_id}`
#queryUrl = 'https://api.ngdesk.com/v2/operations/tickets?client_secret={}&client_id={}'.format(client_id, client_secret)
queryUrl = 'https://api.ngdesk.com/v2/operations/tickets?client_secret={}&client_id={}'.format(client_id, client_secret)

try:
    response = requests.post(queryUrl)
    #api_response = api_instance.get_tickets(authentication_token=authentication_token, start=start, length=length, draw=draw, q=q, sort_by=sort_by, sort_by_order=sort_by_order, passed_account_id=passed_account_id, passed_user_id=passed_user_id, view_id=view_id, client_id=client_id, client_secret=client_secret)
    pprint(api_response)
except:
    print("Exception when calling DefaultApi->get_tickets")