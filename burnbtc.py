#burn btc for xrp
import json
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:14000/api/"
headers = {'content-type': 'application/json'}
auth = HTTPBasicAuth('rpc', 'sweng')

# Send 1 XCP (specified in satoshis) from one address to another.
payload = {
           "method": "create_burn",
           "params": {
                      "source": "mh4w5JnU662ddHywJU3X1wYL6mufjd6Egz",
                      "quantity": 1000000
                     },
           "jsonrpc": "2.0",
           "id": 0
          }

response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
print("Response: ", response.text)