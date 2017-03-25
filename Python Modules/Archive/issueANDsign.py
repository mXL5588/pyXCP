    #! /usr/bin/env python3

from counterpartylib.lib import util
from counterpartylib.lib import config
from counterpartylib.lib.backend import addrindex

#config.TESTNET = 1
#config.RPC =
#config.BACKEND_URL =
#config.BACKEND_SSL_NO_VERIFY =
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
                      "asset": "TESTBALLOT",
                      "quantity": 1000,
                      "description": "This is a test asset for the demo",
                      "divisible": False
                     },
           "jsonrpc": "2.0",
           "id": 0
          }


response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
print("Response: ", response.text)
def main():
    do_send("mh4w5JnU662ddHywJU3X1wYL6mufjd6Egz", "mh4w5JnU662ddHywJU3X1wYL6mufjd6Egz", "TESTBALLOT",  1000)
    print("Done")
def counterparty_api(method, params):
    return util.api(method, params)

def bitcoin_api(method, params):
    return addrindex.rpc(method, params)

def do_send(source, destination, asset, quantity):
    validateaddress = bitcoin_api('validateaddress', [source])
    assert validateaddress['ismine']
    pubkey = validateaddress['pubkey']
    unsigned_tx = counterparty_api('create_send', {'source': source, 'destination': destination, 'asset': asset, 'quantity': quantity, 'pubkey': pubkey, 'allow_unconfirmed_inputs': True})
    signed_tx = bitcoin_api('signrawtransaction', response.text)['hex']
    tx_hash = bitcoin_api('sendrawtransaction', [signed_tx])
    return tx_hash