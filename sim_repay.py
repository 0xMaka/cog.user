# @note: example `repay(address,uint256)` eth_call
from web3 import Web3, HTTPProvider; w3 = Web3(HTTPProvider('https://rpc.scroll.io'))

# configuration
PAIR_ADD = '...'
ACCOUNT  = '...'
AMOUNT   =  ... 
#--

# initialisation
PAIR_ABI = open('abi/cog_pair.json').read()
pair = w3.eth.contract(address=PAIR_ADD, abi=PAIR_ABI)

# driver
if __name__ == '__main__':
  call = w3.eth.call(pair.functions.repay(ACCOUNT, AMOUNT).build_transaction(
    {'from': ACCOUNT, 'gasPrice': w3.eth.gas_price * 2, 'type': 0x0}
  ))
  print(call.hex()) # should return 0x or revert
