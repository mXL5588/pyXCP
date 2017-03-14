import json
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:14000/api/"
headers = {'content-type': 'application/json'}
auth = HTTPBasicAuth('rpc', 'sweng')




# Fetch all balances for all assets for both of two addresses, using keyword-based arguments
payload = {
           "method": "get_balances",
           "params": {
                      "filters": [{"field": "address", "op": "==", "value": "myPy5dWTs43jb4gvirBZdTNeL1QHcwS91f"},
                                  {"field": "address", "op": "==", "value": "mtwNwy1jU3mjW2dBJHmRFH6z2CsKLjQ2dy"}],
                      "filterop": "or"
                     },
           "jsonrpc": "2.0",
           "id": 0
          }

response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
print("Response: ", response.text)