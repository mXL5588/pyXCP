#! /usr/bin/env python3

from counterpartylib.lib import util
from counterpartylib.lib import config
from counterpartylib.lib.backend import addrindex

config.TESTNET = 1
config.RPC = bitcion-rpc
config.BACKEND_URL = '127.0.0.1'
# config.BACKEND_SSL_NO_VERIFY =

def counterparty_api(method, params):
    return util.api(method, params)

def bitcoin_api(method, params):
    return addrindex.rpc(method, params)

def do_send(source, destination, asset, quantity, fee, encoding):
    validateaddress = bitcoin_api('validateaddress', [source])
    assert validateaddress['ismine']
    pubkey = validateaddress['pubkey']
    unsigned_tx = counterparty_api('create_send', {'source': source, 'destination': destination, 'asset': asset, 'quantity': quantity, 'pubkey': pubkey, 'allow_unconfirmed_inputs': True})
    signed_tx = bitcoin_api('signrawtransaction', [unsigned_tx])['hex']
    tx_hash = bitcoin_api('sendrawtransaction', [signed_tx])
    return tx_hash