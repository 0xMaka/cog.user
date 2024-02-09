## cog.user ⚙️.👩‍🔧👨‍🔧

Assortment of examples and personal files that hope to be useful, includes some programatic interactions, ABI and address compilations.<br>
There is also a support focused [FAQ](support_faq.md), providing work arounds for a variety of situations users may experience.

<table class="fixed-align">
  <tbody>
    <tr>
  <td>  
      
| Item                                 | Description                                               |
|--------------------------------------|-----------------------------------------------------------|
| [get_pairs.py](get_pairs.py)   (v1)  | Generates a csv of all pairs from factory contract events | 
| [interest_rate.py](interest_rate.py) | Returns value shown on UI under `Borrow interest rate`    | 
| [sim_remove.py](sim_remove.py)       | Performs an `eth_call` for `remove_collateral` on a pair  | 
| [sim_repay.py](sim_repay.py)         | Performs an `eth_call` for `repay` on a pair              |
| [cog_pair.py](cog_pair.py)  (v1)     | Low level static caller, that makes no checks on inputs   |
|           <img width=150/>           |                  <img width=430/>                         |
 
  </td>

  <td valign="top", valign="right">

| Compilation                               | 
|-------------------------------------------|
|  [pairs.csv](data/pairs.csv) (v1)         | 
|  [tokens.csv](data/tokens.csv)            |
|  [incentivized.md](data/incentivized.md)  | 
|  [support_faq.md](support_faq.md)         |
|           <img width=100/>                |

  </td>
    </tr>
  </tbody>
</table>

<table class="fixed-align">
  <tbody>
   <tr>
  <th>
    Spotlight
  </th>
    </tr>  
    <tr>
  <td valign="top", valign="center">
 
  ```python
  >>> #----------------------------------------------------------------------------------
  >>> # cog_pair.py can be useful for making static requests without a contract instance. 
  >>> #----------------------------------------------------------------------------------
  >>> import cog_pair as cp
  >>> pair = '0x677dde488050F00Cc7412b910da25575a72FadD6'
  >>> cp.accrue_info(pair)
  (317097920, 1707389800, 188738642170121)
  >>> # ---------------------------------------------------------------------------------
  >>> # also exposes some values via direct storage access and parsing of the constructor
  >>> #----------------------------------------------------------------------------------
  >>> cp.interest_per_second(pair)
  317097920
  >>> cp.constructor(pair)
  Constructor(
    asset='0x5300000000000000000000000000000000000004', 
    collateral='0xf610a9dfb7c89644979b4a0f27063e9e7d7cda32', 
    oracle='0xbabd55549c266c6755b99173fe7604238d04117d', 
    min_target_utilization=300000000000000000, 
    max_target_utilization=700000000000000000, 
    starting_interest_per_second=951293760, 
    min_interest=317097920, 
    max_interest=3170979200, 
    elasticity=28800000000000000000000000000000000000000
  )
>>>
>>> # ---------------------------------------------------------------------------------
>>> # a list of all methods and values can be found below (Global values are hardcoded)
>>> #----------------------------------------------------------------------------------
>>> cp.
cp.BORROW_OPENING_FEE(                      cp.decimals(
cp.DEFAULT_PROTOCOL_FEE(                    cp.exchange_rate(
cp.GLOBAL_BORROW_OPENING_FEE_PRECISION      cp.factory(
cp.GLOBAL_COLLATERIZATION_RATE              cp.fees_earned_fraction(
cp.GLOBAL_COLLATERIZATION_RATE_PRECISION    cp.interest_per_second(
cp.GLOBAL_EXCHANGE_RATE_PRECISION           cp.last_accrued(
cp.GLOBAL_FACTOR_PRECISION                  cp.last_elapsed_time(
cp.GLOBAL_INTEREST_PER_SECOND_PRECISION     cp.last_interest_per_second(
cp.GLOBAL_LIQUIDATION_MULTIPLIER            cp.max_deposit(
cp.GLOBAL_LIQUIDATION_MULTIPLIER_PRECISION  cp.max_mint(
cp.GLOBAL_PROTOCOL_FEE_PRECISION            cp.max_redeem(
cp.GLOBAL_PROTOCOL_SURGE_THRESHOLD          cp.max_withdraw(
cp.GLOBAL_SURGE_DURATION                    cp.name(
cp.GLOBAL_UTILIZATION_PRECISION             cp.oracle(
cp.INTEREST_ELASTICITY(                     cp.paused(
cp.MAXIMUM_INTEREST_PER_SECOND(             cp.preview_deposit(
cp.MAXIMUM_TARGET_UTILIZATION(              cp.preview_mint(
cp.MINIMUM_INTEREST_PER_SECOND(             cp.preview_redeem(
cp.MINIMUM_TARGET_UTILIZATION(              cp.preview_withdraw(
cp.STARTING_INTEREST_PER_SECOND(            cp.protocol_fee(
cp.accrue_info(                             cp.surge_info(
cp.allowance(                               cp.symbol(
cp.asset(                                   cp.total_asset(
cp.balance(                                 cp.total_assets(
cp.borrow_approvals(                        cp.total_borrow(
cp.collateral(                              cp.total_supply(
cp.constructor(                             cp.user_borrow_part(
cp.convert_to_assets(                       cp.user_collateral_share(
cp.convert_to_shares(
>>>
```
    
</td>
  </tr>
 
  <tr>
<td>
  <img width=800/>
</td>
  </tr>
</table>

<div style="text-align: right">

| ABI                                      | Description                                                                                  | Source                                                                                            |
|------------------------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [cog_factory.json](abi/cog_factory.json) | A priviledged factory for creating Cog Pairs and managing their protocol-owned liquidity     | [cog_factory.vy](https://github.com/CogFinance/Cog-Isolated-Lending/blob/main/src/cog_factory.vy) |
| [cog_pair.json](abi/cog_pair.json)       | Implementation of an isolated lending pool with PoL in Vyper                                 | [cog_pair.vy](https://github.com/CogFinance/Cog-Isolated-Lending/blob/main/src/cog_pair.vy)       |
| [fuse_box.json](abi/fuse_box.json)       | A robust Oracle Implementation with secure upgradability in mind, and simplicity at its core | [fuse_box](https://github.com/CogFinance/Cog-Isolated-Lending/blob/main/src/fuse_box.vy])      |
| [loan_router.json](abi/loan_router.json) | A very smol helper contract for routing multiple borrows                                     | [loan_router.vy](https://github.com/CogFinance/Cog-Isolated-Lending/blob/main/src/loan_router.vy) |

</div>
<img src="https://github.com/0xMaka/cog/assets/12489182/e396e82b-7fa6-4687-9dd9-ebc7f853fc93" alt="cogs" align="right" width="200"/>

---
> **_NOTE:_** As always it is suggested to consider personal circumstance, to do your own research and take the appropriate action for you.<br>
Information provided here is an attempt to contribute to that research but in no way constitutes financial advise of any kind.
