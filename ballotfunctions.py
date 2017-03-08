import json
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:14000/api/"
headers = {'content-type': 'application/json'}
auth = HTTPBasicAuth('counterparty-rpc', 'sweng')




def createBallot(sourceAddress.string, assetName.string, ballotQuantity.int, ballotDesc.string, isDivisible.bool)
    # Issuance (indivisible)
    payload = {
               "method": "create_issuance",
               "params": {
                          "source": sourceAddress,
                          "asset": assetName,
                          "quantity": ballotQuantity,
                          "description": ballotDesc,
                          "divisible": isDivisible
                         },
               "jsonrpc": "2.0",
               "id": 0
              }


    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
    print("Response: ", response.text)

def castVote(userSourceAddress.string, candidateAddress.string, assetName.string, voteQuantity.int)
# Send 1 XCP (specified in satoshis) from one address to another.
  payload = {
           "method": "create_send",
           "params": {
                      "source": userSourceAddress,
                      "destination": candidateAddress,
                      "asset": assetName,
                      "quantity": voteQuantity
                     },
           "jsonrpc": "2.0",
           "id": 0
          }
    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
    print("Response: ", response.text)

def convertToSatoshis(ballotQuantity.int)
  return ballotQuantity * 100000000

def convertFromSatoshis(voteQuantity.int)
  return voteQuantity / 100000000

def getBallotCandidateBalance(candidateAddress.string)
# Fetch all balances for all assets for both of two addresses, using keyword-based arguments
  payload = {
           "method": "get_balances",
           "params": {
                      "filters": [{"field": "address", "op": "==", "value": candidateAddress}],
                      "filterop": "or"
                     },
           "jsonrpc": "2.0",
           "id": 0
           }
    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
    print("Response: ", response.text)


def getBallotCandidateAddress(ballotID.int)

