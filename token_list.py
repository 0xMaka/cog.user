def data() -> list:
  from csv import reader
  with open('data/pairs.csv', newline='') as f: 
    return list(map(lambda x : x, reader(f, delimiter=',')))

def assets(data: list) -> list:
  return list(map(lambda x : x[2], data))[1:]

def collaterals(data: list) -> list:
  return list(map(lambda x : x[3], data))[1:]

def tokens(data: list) -> list:
  tokens = set().union(assets(data), collaterals(data))
  return list(tokens)

def pretty(tokens: list) -> list:
  from collections import namedtuple
  Token = namedtuple ('Token',['name', 'symbol', 'decimals', 'address'])
  import cog_pair as cp                # can reuse erc20 methods
  return list(map(lambda x : Token(cp.name(x), cp.symbol(x), cp.decimals(x), x), tokens))

token_list = pretty(tokens(data()))

def save(lst: list) -> int:
  fields = ['name','symbol','decimals','address']
  rows = list(map(lambda x : x._asdict(), lst))
  with open('data/tokens.csv', 'w') as f: 
    from csv import DictWriter
    csv = DictWriter(f,fieldnames=fields); csv.writeheader(); csv.writerows(rows)
  return 1

if __name__ == '__main__':
  save(token_list)
