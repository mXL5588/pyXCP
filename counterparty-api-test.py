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

# Fetch all debits for > 2 XCP between blocks 280537 and 280539, sorting the results by quantity (descending order)
payload = {
           "method": "get_debits",
           "params": {
                      "filters": [{"field": "asset", "op": "==", "value": "XCP"},
                                  {"field": "quantity", "op": ">", "value": 200000000}],
                      "filterop": "AND",
                      "order_by": "quantity",
                      "order_dir": "desc"
                     },
           "jsonrpc": "2.0",
           "id": 0
          }
# [NEEDED FOR BVS]
# Send 1 XCP (specified in satoshis) from one address to another.
#payload = {
#           "method": "create_send",
#           "params": {
#                      "source": "1CUdFmgK9trTNZHALfqGvd8d6nUZqH2AAf",
#                      "destination": "17rRm52PYGkntcJxD2yQF9jQqRS4S2nZ7E",
#                      "asset": "XCP",
#                      "quantity": 100000000
#                     },
#           "jsonrpc": "2.0",
#           "id": 0
#          }

# [NEEDED FOR BVS]
# Issuance (indivisible)
payload = {
           "method": "create_issuance",
           "params": {
                      "source": "1CUdFmgK9trTNZHALfqGvd8d6nUZqH2AAf",
                      "asset": "MYASSET",
                      "quantity": 1000,
                      "description": "my asset is cool",
                      "divisible": False
                     },
           "jsonrpc": "2.0",
           "id": 0
          }

#Transfer asset ownership
payload = {
           "method": "create_issuance",
           "params": {
                      "source": "1CUdFmgK9trTNZHALfqGvd8d6nUZqH2AAf",
                      "transfer_destination": "17rRm52PYGkntcJxD2yQF9jQqRS4S2nZ7E",
                      "asset": "MYASSET",
                      "quantity": 0
                     },
           "jsonrpc": "2.0",
           "id": 0
          }

#Lock Asset
payload = {
           "method": "create_issuance",
           "params": {
                      "source": "1CUdFmgK9trTNZHALfqGvd8d6nUZqH2AAf",
                      "asset": "MYASSET",
                      "quantity": 0,
                      "description": "LOCK"
                     },
           "jsonrpc": "2.0",
           "id": 0
          }
response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
print("Response: ", response.text)