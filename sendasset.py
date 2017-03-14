#send asset
import json
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:14000/api/"
headers = {'content-type': 'application/json'}
auth = HTTPBasicAuth('rpc', 'sweng')



payload = {
           "method": "create_send",
           "params": {
                      {
                      	'source': 'mh4w5JnU662ddHywJU3X1wYL6mufjd6Egz', 
						'destination': 'mqKfr6S5SJgzWcd1kqjdKRzWvUwS8XoR8t',
						'regular_dust_size': 5429, 
						'encoding': 'auto', 
						'pubkey': '02ac768d1624b533fd6b9b5f6c2c7944efa474az043131b63953f1d1e4bff44b43', 
						'allow_unconfirmed_inputs': False, 
						'op_return_value': 0, 
						'fee': None, 
						'quantity': 1, 
						'asset': 'SWENGDMO', 
						'fee_per_kb': 10000 }
						#'multisig_dust_size': 7799}
                     },
           "jsonrpc": "2.0",
           "id": 0
          }


response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
print("Response: ", response.text)