import json
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:14000/api/"
headers = {'content-type': 'application/json'}
auth = HTTPBasicAuth('counterparty-rpc', 'sweng')

# Send 1 XCP (specified in satoshis) from one address to another.
payload = {
           "method": "create_send",
           "params": {
                      "source": "my4fJWPYaWRsNuKXqj9bsNsDYWzsRR6PMp",
                      "destination": "miCf5Wbi9vkJfa5HC2gkzuPwRHdvu5X9iy",
                      "asset": "SWENGTEST",
                      "quantity": 100000000
                     },
           "jsonrpc": "2.0",
           "id": 0
          }

response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
print("Response: ", response.text)