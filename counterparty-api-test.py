import json
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:14000/api/"
headers = {'content-type': 'application/json'}
auth = HTTPBasicAuth('counterparty-rpc', 'sweng')

payload = {
  "method": "get_running_info",
  "params": {},
  "jsonrpc": "2.0",
  "id": 0
}



# Fetch all balances for all assets for both of two addresses, using keyword-based arguments
payload = {
           "method": "get_balances",
           "params": {
                      "filters": [{"field": "address", "op": "==", "value": "14qqz8xpzzEtj6zLs3M1iASP7T4mj687yq"},
                                  {"field": "address", "op": "==", "value": "1bLockjTFXuSENM8fGdfNUaWqiM4GPe7V"}],
                      "filterop": "or"
                     },
           "jsonrpc": "2.0",
           "id": 0
          }
# Get all burns between blocks 280537 and 280539 where greater than .2 BTC was burned, sorting by tx_hash (ascending order)
payload = {
           "method": "get_burns",
           "params": {
                      "filters": {"field": "burned", "op": ">", "value": 20000000},
                      "filterop": "AND",
                      "order_by": "tx_hash",
                      "order_dir": "asc",
                      "start_block": 1080000,
                      "end_block": 1090023
                     },
           "jsonrpc": "2.0",
           "id": 0
          }

response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
print("Response: ", response.text)