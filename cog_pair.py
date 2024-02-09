# @title   : cog_pair.py
# @notice  : helper - efficient for making static requests without a contract instance
#            exposes some values via direct storage access and parsing of the constructor
# @author  : maka

#--------------------------------------------------------------------------------------#

from eth_abi import encode as __encode, decode as __decode
from web3 import Web3 as _w, HTTPProvider as _hp; _w3 = _w(_hp('https://rpc.scroll.io'))

_keccak = lambda x   : _w3.solidity_keccak(['string'],[x])[:4].hex()
_call   = lambda x,y : _w3.eth.call({ 'to' : x, 'data' : y })
_decode = lambda x,y : __decode(x,y)[0]
_encode = lambda x,y : __encode(x,y).hex()
 
#--------------------

def user_collateral_share(pair: str, user: str) -> int:
  sig = _keccak('user_collateral_share(address)')
  data = sig + _encode(['address'],[user])
  return _decode(['uint256'], _call(pair,data))

def user_borrow_part(pair: str, user: str) -> int:
  sig = _keccak('user_borrow_part(address)')
  data = sig + _encode(['address'],[user])
  return _decode(['uint256'], _call(pair,data))

def max_deposit(pair: str, user: str) -> int:
  sig = _keccak('maxDeposit(address)')
  data = sig + _encode(['address'],[user])
  return _decode(['uint256'], _call(pair,data))

def preview_deposit(pair: str, value: int) -> int:
  sig = _keccak('previewDeposit(uint256)')
  data = sig + _encode(['uint256'],[value])
  return _decode(['uint256'], _call(pair,data))

def max_mint(pair: str, user: str) -> int:
  sig = _keccak('maxMint(address)')
  data = sig + _encode(['address'],[user])
  return _decode(['uint256'], _call(pair,data))

def preview_mint(pair: str, value: int) -> int:
  sig = _keccak('previewMint(uint256)')
  data = sig + _encode(['uint256'],[value])
  return _decode(['uint256'], _call(pair,data))

def max_withdraw(pair: str, user: str) -> int:
  sig = _keccak('maxWithdraw(address)')
  data = sig + _encode(['address'],[user])
  return _decode(['uint256'], _call(pair,data))

def preview_withdraw(pair: str, value: int) -> int:
  sig = _keccak('previewWithdraw(uint256)')
  data = sig + _encode(['uint256'],[value])
  return _decode(['uint256'], _call(pair,data))

def max_redeem(pair: str, user: str) -> int:
  sig = _keccak('maxRedeem(address)')
  data = sig + _encode(['address'],[user])
  return _decode(['uint256'], _call(pair,data))

def preview_redeem(pair: str, value: int) -> int:
  sig = _keccak('previewRedeem(uint256)')
  data = sig + _encode(['uint256'],[value])
  return _decode(['uint256'], _call(pair,data))

def balance(pair: str, user: str) -> int:
  sig = _keccak('balance(address)')
  data = sig + _encode(['address'],[user])
  return _decode(['uint256'], _call(pair,data))

def allowance(pair: str, spendee: str, spender: str) -> int:
  sig = _keccak('allowance(address,address)')
  data = sig + _encode(['address','address'],[spendee,spender])
  return _decode(['uint256'], _call(pair,data))

def borrow_approvals(pair: str, spendee: str, spender: str) -> int:
  sig = _keccak('borrow_approvals(address,address)')
  data = sig + _encode(['address','address'],[spendee,spender])
  return _decode(['uint256'], _call(pair,data))

#--------------------

def convert_to_shares(pair: str, value: int) -> int:
  sig = _keccak('convertToShares(uint256)')
  data = sig + _encode(['uint256'],[value])
  return _decode(['uint256'], _call(pair,data))

def convert_to_assets(pair: str, value: int) -> int:
  sig = _keccak('convertToAssets(uint256)')
  data = sig + _encode(['uint256'],[value])
  return _decode(['uint256'], _call(pair,data))

#--------------------

def total_supply(pair: str) -> int:
  data = _keccak('totalSupply()')
  return _decode(['uint256'], _call(pair,data))

def name(pair: str) -> str:
  data = _keccak('name()')
  return _decode(['string'], _call(pair,data))

def symbol(pair: str) -> str:
  data = _keccak('symbol()')
  return _decode(['string'], _call(pair,data))

def decimals(pair: str) -> int:
  data = _keccak('decimals()')
  return _decode(['uint256'], _call(pair,data))

def total_assets(pair: str) -> int:
  data = _keccak('totalAssets()')
  return _decode(['uint256'], _call(pair,data))

def total_asset(pair: str) -> tuple:
  data = _keccak('total_asset()')
  return _decode(['(uint256,uint256)'], _call(pair,data))

def total_borrow(pair: str) -> int:
  data = _keccak('total_borrow()')
  return _decode(['(uint256,uint256)'], _call(pair,data))

def exchange_rate(pair: str) -> int:
  data = _keccak('exchange_rate()')
  return _decode(['uint256'], _call(pair,data))

def accrue_info(pair: str) -> int:
  data = _keccak('accrue_info()')
  return _decode(['(uint256,uint256,uint256)'], _call(pair,data))

def surge_info(pair: str) -> int:
  data = _keccak('surge_info()')
  return _decode(['(uint256,uint256)'], _call(pair,data))

def paused(pair: str) -> bool:
  data = _keccak('paused()')
  return _decode(['bool'], _call(pair,data))

def protocol_fee(pair: str) -> int:
  data = _keccak('protocol_fee()')
  return _decode(['uint256'], _call(pair,data))

def BORROW_OPENING_FEE(pair: str) -> int:
  data = _keccak('BORROW_OPENING_FEE()')
  return _decode(['uint256'], _call(pair,data))

def DEFAULT_PROTOCOL_FEE(pair: str) -> int:
  data = _keccak('DEFAULT_PROTOCOL_FEE()')
  return _decode(['uint256'], _call(pair,data))

#-------------------------

def factory(pair: str) -> str:
  data = _keccak('factory()')
  return _decode(['address'], _call(pair,data))

def asset(pair: str) -> str:
  data = _keccak('asset()')
  return _decode(['address'], _call(pair,data))

def collateral(pair: str) -> str:
  data = _keccak('collateral()')
  return _decode(['address'], _call(pair,data))

def oracle(pair: str) -> str:
  data = _keccak('oracle()')
  return _decode(['address'], _call(pair,data))

#--------------------------------------------------------------------------------------#

# storage slots
# slot 0     : total_colleral_share
# slot 1-2   : total_collateral_asset
# slot 3-4   : total_borrow
# slot 5     : user_collateral_share mapping
# slot 6     : user_borrow_part mapping
# slot 7     : exchange_rate
# slot 8-10  : accrue_info
# slot 11-12 : surge_info
# slot 13    : ?paused (bool)
# slot 14    : BORROW_OPENING_FEE
# slot 15    : protocol_fee
# slot 16    : DEFAULT_OPENING_FEE

_int = lambda x,y : _decode(['uint256'], _w3.eth.get_storage_at(x,y))

def interest_per_second(pair: str)      -> int : return _int(pair,  8)
def last_accrued(pair: str)             -> int : return _int(pair,  9)
def fees_earned_fraction(pair: str)     -> int : return _int(pair, 10)
def last_interest_per_second(pair: str) -> int : return _int(pair, 11)
def last_elapsed_time(pair: str)        -> int : return _int(pair, 12)

#-------------------------

from collections import namedtuple as _tuple
_Constructor = _tuple(
  'Constructor',[
  'asset',
  'collateral',
  'oracle',
  'min_target_utilization',
  'max_target_utilization',
  'starting_interest_per_second',
  'min_interest',
  'max_interest',
  'elasticity'
])

def constructor(pair: str) -> _tuple:
  word = 32; page = word * 9
  args = _w3.eth.get_code(pair)[-page:]
  argx = list(map(lambda x : args[x:x+word], range(0,page,word)))
  return _Constructor(
    _decode(['address'], argx[0]),
    _decode(['address'], argx[1]),
    _decode(['address'], argx[2]),
    _decode(['uint256'], argx[3]),
    _decode(['uint256'], argx[4]),
    _decode(['uint256'], argx[5]),
    _decode(['uint256'], argx[6]),
    _decode(['uint256'], argx[7]),
    _decode(['uint256'], argx[8])
  )

#-------------------------

_x  = lambda x : x * -32; _p  = lambda x : x +  32; _xp = lambda x : _p(_x(x))
_slice = lambda x, y : _decode(['uint256'], _w3.eth.get_code(x)[_x(y):_xp(y)])

def MINIMUM_TARGET_UTILIZATION(pair: str)   -> int : return _slice(pair,6)
def MAXIMUM_TARGET_UTILIZATION(pair: str)   -> int : return _slice(pair,5)
def STARTING_INTEREST_PER_SECOND(pair: str) -> int : return _slice(pair,4)
def MINIMUM_INTEREST_PER_SECOND(pair: str)  -> int : return _slice(pair,3)
def MAXIMUM_INTEREST_PER_SECOND(pair: str)  -> int : return _slice(pair,2)
def INTEREST_ELASTICITY(pair: str) -> int:
  return _decode(['uint256'], _w3.eth.get_code(pair)[-32:])

#-------------------------

GLOBAL_EXCHANGE_RATE_PRECISION = 1000000000000000000         # 1e18
GLOBAL_COLLATERIZATION_RATE_PRECISION = 100000               # 1e5
GLOBAL_COLLATERIZATION_RATE = 75000                          # 75%
GLOBAL_BORROW_OPENING_FEE_PRECISION = 100000
GLOBAL_PROTOCOL_FEE_PRECISION = 1000000
GLOBAL_PROTOCOL_SURGE_THRESHOLD = 1635979200
GLOBAL_SURGE_DURATION = 86400 * 3                            # 3 Days
GLOBAL_UTILIZATION_PRECISION = 1000000000000000000           # 1e18
GLOBAL_FACTOR_PRECISION = 1000000000000000000                # 1e18
GLOBAL_LIQUIDATION_MULTIPLIER = 112000                       # 12
GLOBAL_LIQUIDATION_MULTIPLIER_PRECISION = 100000             # 1e5
GLOBAL_INTEREST_PER_SECOND_PRECISION = 1000000000000000000   # 1e18

#--------------------------------------------------------------------------------------#

# 1love
