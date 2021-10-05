"""
Poc for BT interactions
"""
from web3 import Web3, HTTPProvider
import json

class BTInteractor():

    def __init__(self, contract_address, private_key):
        self._contract_address = contract_address
        self._private_key = private_key
        self.init()
        self.populate_contract()

    def init(self):
        self._w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
        # print(w3.isConnected())
        # print(w3.eth.accounts[0])
        self._addr = self._w3.eth.accounts[0]

    def populate_contract(self):
        f = open('/Users/Surbhi.Anand/hack21/hashValidator/build/contracts'
                 '/BackupHashStorage.json')
        backup_contract_json = json.load(f)
        self._contract = self._w3.eth.contract(self._contract_address, abi=backup_contract_json['abi'])

    def addHashToBlockchain(self, hash, path):
        transaction = self._contract.functions.addHashToBlochain(
            hash, path).buildTransaction({
            'from': self._addr,
            'nonce': self._w3.eth.get_transaction_count(self._addr)
        })
        signed_txn = self._w3.eth.account.signTransaction(transaction, private_key=self._private_key)
        self._w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(self._contract.functions.backupsCount().call())

# def web3setup():
#     w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
#     print(w3.isConnected())
#     print(w3.eth.accounts[0])
#     addr = w3.eth.accounts[0]
#
#     f = open('/Users/animesh.kumar/hackathon/eth-todo-list/build/contracts/BackupHashStorage.json')
#     backup_contract_json = json.load(f)
#     contract_address = '0x9484BBf583941e78Af3b361682e2B99909aB648c'
#     contract = w3.eth.contract(contract_address, abi=backup_contract_json['abi'])
    # print(contract.functions.backupsCount().call())


# if __name__ == '__main__':
#     interactor = BTInteractor('0x9484BBf583941e78Af3b361682e2B99909aB648c', 'd94b93442e0b2ef1a71b84e633637f923357dc9966065abc8ea5a67027850aad')

