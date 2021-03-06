from .bitcoinclass import bRPCHost




## default port for bitcoin testnet
## (change to 8332 for 'main net'),
rpcPort = 18332
rpcUser = 'bitcoinrpc'
## not a real password
## but if you use the random password generated by bitcoind
## your password should look something like this
rpcPassword = 'rpc'
serverURL = 'http://' + rpcUser + ':' + rpcPassword + '@localhost:' + str(rpcPort)


host = bRPCHost(serverURL)

hash = host.call('getrawtransaction', "5f437ae647ee975c187251df70c6c2ac5fcf8ec2131cb4f3d3782f143b12d9be")

print(hash)