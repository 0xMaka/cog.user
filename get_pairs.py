# @note: retreving all pools
from web3 import Web3, HTTPProvider; w3 = Web3(HTTPProvider('https://rpc.scroll.io'))

FACTORY_ADD = '0xbAbD55549c266c6755b99173fE7604238D04117d'
FACTORY_ABI = open('abi/cog_factory.json').read()
BLOCK_DEPLOYED = 85518
factory = w3.eth.contract(address=FACTORY_ADD, abi=FACTORY_ABI)

stable = factory.events.StablePairCreated().get_logs(fromBlock=BLOCK_DEPLOYED)
low    = factory.events.LowPairCreated().get_logs(fromBlock=BLOCK_DEPLOYED)
medium = factory.events.MediumPairCreated().get_logs(fromBlock=BLOCK_DEPLOYED)
high   = factory.events.HighPairCreated().get_logs(fromBlock=BLOCK_DEPLOYED)
custom = factory.events.CustomPairCreated().get_logs(fromBlock=BLOCK_DEPLOYED)

all_logs = stable + low + medium + high + custom

from collections import namedtuple
Pair = namedtuple('Pair',['risk_tier','pair','asset','collateral'])

def logs_to_pairs(logs: list[dict]) -> list[Pair]:
  return list(map(lambda x: Pair(
    x['event'][:-len('PairCreated')],
    x['args']['pair'],
    x['args']['asset'],
    x['args']['collateral'],
  ), logs))

def save(logs: list[dict]) -> int:
  fields = ['risk_tier','pair','asset','collateral']
  rows = list(map(lambda x : x._asdict(), logs_to_pairs(logs)))
  with open('data/pairs.csv', 'w') as f: 
    from csv import DictWriter
    csv = DictWriter(f,fieldnames=fields); csv.writeheader(); csv.writerows(rows)
  return 1

if __name__ == '__main__':
  save(all_logs)

