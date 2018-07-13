#import pytrends
from pytrends.request import TrendReq
import requests

requests.packages.urllib3.disable_warnings()

google_username = 'dennisbien.dil@gmail.com'
google_password = 'SouFlo12@'

pytrend = TrendReq(google_username, google_password)

kw_list=['pizza']
pytrend.build_payload(kw_list , geo = 'IN')

pytrend.build_payload()
# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()

# Interest by Region
interest_by_region_df = pytrend.interest_by_region()

# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()

# Get Google Hot Trends data
trending_searches_df = pytrend.trending_searches()

# Get Google Top Charts
top_charts_df = pytrend.top_charts(cid='actors', date=201611)

# Get Google Keyword Suggestions
suggestions_dict = pytrend.suggestions(keyword='pizza')