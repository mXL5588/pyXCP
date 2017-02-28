import json
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:14000/api/"
headers = {'content-type': 'application/json'}
auth = HTTPBasicAuth('counterparty-rpc', 'sweng')


# Issuance (indivisible)
payload = {
           "method": "create_issuance",
           "params": {
                      "source": "my4fJWPYaWRsNuKXqj9bsNsDYWzsRR6PMp",
                      "asset": "TESTASSET",
                      "quantity": 100000000,
                      "description": "This is a test asset",
                      "divisible": False
                     },
           "jsonrpc": "2.0",
           "id": 0
          }


response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
print("Response: ", response.text)