import json
import requests
from requests.auth import HTTPBasicAuth

serverURL = "http://localhost:14000/api/"
auth = HTTPBasicAuth('rpc', 'sweng')

class cRPCHost(object):
    def __init__(self, url):
        self._session = requests.Session()
        self._url = url
        self._headers = {'content-type': 'application/json'}
    def call(self, rpcMethod, params):
        print(self)
        print(rpcMethod)
        print(params)
        payload = json.dumps({"method": rpcMethod, "params": params, "jsonrpc": "2.0", "id": 0})
        print (payload)
        tries = 10
        hadConnectionFailures = False
        while True:
            try:
                response = self._session.post(self._url, headers=self._headers, data=payload, auth=auth)
            except requests.exceptions.ConnectionError:
                tries -= 1
                if tries == 0:
                    raise Exception('Failed to connect for remote procedure call.')
                hadFailedConnections = True
                print("Couldn't connect for remote procedure call, will sleep for ten seconds and then try again ({} more tries)".format(tries))
                time.sleep(10)
            else:
                if hadConnectionFailures:
                    print('Connected for remote procedure call after retry.')
                break
        if not response.status_code in (200, 500):
            raise Exception('RPC connection failure: ' + str(response.status_code) + ' ' + response.reason)
        responseJSON = response.json()
        if 'error' in responseJSON and responseJSON['error'] != None:
            raise Exception('Error in RPC call: ' + str(responseJSON['error']))
        return responseJSON['result']




host = cRPCHost(serverURL)
objParams = {"source": "mh4w5JnU662ddHywJU3X1wYL6mufjd6Egz",
                      "asset": "TESTBALL",
                      "quantity": 100,
                      "description": "This is a test asset for the demo",
                      "divisible": False}

unsignedTransaction = host.call('create_issuance', objParams)
print(unsignedTransaction)
#block = host.call('last_block', runningInfo)
## lookup details in the results
#coinBase = block['tx'][0]
## more than one RPC parameter
#l = host.call('listreceivedbyaddress', 0, True)
#print(dataCall.text)

