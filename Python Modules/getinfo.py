import json
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:14000/api/"
headers = {'content-type': 'application/json'}
auth = HTTPBasicAuth('rpc', 'sweng')



def main():
	parseResponse(accessAPI(),"last_block") 

def accessAPI():
	payload = {
	  "method": "get_running_info",
	  "params": {},
	  "jsonrpc": "2.0",
	  "id": 0
	}
	response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
	#print("Response: ", response.text)
	responseObj = json.loads(response.text)
	keys =  responseObj.keys()
	print(keys)
	#print(parsableResponse["result"].bitcoin_block_count)
	#if 'result' in responseObj:
	#        print(responseObj['result'].get('last_block').get('block_index'))
	#else:
	#        print ('This does not have a key')  
	return responseObj

def parseResponse(jsonObj, dataField):
#checks to see if valid counterparty or bitcoin api call with result key
	if 'result' in jsonObj:
	    print(jsonObj['result'].get(dataField))
	    return jsonObj['result'].get(dataField)
	else:
	    print ('This does not have a key')   


main()