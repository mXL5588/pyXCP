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
                      "filters": [{"field": "address", "op": "==", "value": "mh4w5JnU662ddHywJU3X1wYL6mufjd6Egz"},
                                  {"field": "address", "op": "==", "value": "mqKfr6S5SJgzWcd1kqjdKRzWvUwS8XoR8t"}],
                      "filterop": "or"
                     },
           "jsonrpc": "2.0",
           "id": 0
          }

response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
print("Response: ", response.text)