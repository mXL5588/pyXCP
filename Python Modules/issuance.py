import json
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:14000/api/"
headers = {'content-type': 'application/json'}
auth = HTTPBasicAuth('rpc', 'sweng')


# Issuance (indivisible)
payload = {
           "method": "create_issuance",
           "params": {
                      "source": "mh4w5JnU662ddHywJU3X1wYL6mufjd6Egz",
                      "asset": "SWENGBALLOT",
                      "quantity": 10000000,
                      "description": "This is a test asset for the demo",
                      "divisible": False
                     },
           "jsonrpc": "2.0",
           "id": 0
          }


response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
print("Response: ", response.text)