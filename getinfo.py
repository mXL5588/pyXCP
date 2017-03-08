import json
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:14000/api/"
headers = {'content-type': 'application/json'}
auth = HTTPBasicAuth('rpc', 'sweng')

payload = {
  "method": "get_running_info",
  "params": {},
  "jsonrpc": "2.0",
  "id": 0
}
response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
print("Response: ", response.text)