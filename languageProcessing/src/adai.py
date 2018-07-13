import sys
import json
import requests

API_URL = "https://www.censys.io/api/v1"
UID = "f678b0fc-1307-4099-b2ee-a08655d3aa55"
SECRET = "wyjMu4gTfLdLIh8C9VnzCZpfGKyR7vxh"

low = 1
high = 2

params = {'query': "alexa_rank:["+str(low)  +" TO " + str(high)+"]"}
res = requests.post(API_URL + "/search/websites",json = params, auth=(UID, SECRET))
if res.status_code != 200:
        print "error occurred: %s" % res.json()["error"]
        sys.exit(1)

obj = json.loads(res.content)
print obj