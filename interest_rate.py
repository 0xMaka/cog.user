# @note: returns value shown under `Borrow interest rate`
from web3 import Web3, HTTPProvider; w3 = Web3(HTTPProvider('https://rpc.scroll.io'))

ONE_PERCENT = 317097920 # cog_factory.vy#L241

def accrue_info(pair: str) -> tuple:
  sig = w3.solidity_keccak(['string'],['accrue_info()']).hex()
  from eth_abi import decode
  return decode(['uint256','uint256','uint256'], w3.eth.call({ 'to' : pair, 'data' : sig }))

def get_rate(pair: str) -> int:
  return accrue_info(pair)[0] / ONE_PERCENT

if __name__ == '__main__':
  print(get_rate('0xb31d07F716b5cd5C47e5d46E6955D7185F04Fd24'))
