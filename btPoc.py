"""
Poc for BT interactions
"""
from web3 import Web3, HTTPProvider
import json

if __name__ == '__main__':
 w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
 print(w3.isConnected())
 print(w3.eth.accounts[0])
 addr = w3.eth.accounts[0]

 f = open('/Users/animesh.kumar/hackathon/eth-todo-list/build/contracts/BackupHashStorage.json')
 backup_contract_json = json.load(f)
 contract_address = '0x9484BBf583941e78Af3b361682e2B99909aB648c'
 contract = w3.eth.contract(contract_address,abi=backup_contract_json['abi'])
 print(contract.functions.backupsCount().call())


#  adding new transaction
# periodic creation of backups
#

transaction = contract.functions.addHashToBlochain(
    'string3','string4' ).buildTransaction({
    'from': addr,
    'nonce': w3.eth.get_transaction_count(addr)
    })
private_key = "d94b93442e0b2ef1a71b84e633637f923357dc9966065abc8ea5a67027850aad"
signed_txn = w3.eth.account.signTransaction(transaction, private_key=private_key)
w3.eth.sendRawTransaction(signed_txn.rawTransaction)
