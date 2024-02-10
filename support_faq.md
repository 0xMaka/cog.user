## Support FAQ

This is an faq focused on quick fixes and work arounds for any issues that crop up for the Cog community.

- Information in this guide as with any occumpanying scripts on github are provided under the GNU Affero General Public License v3.0

### Cannot repay my debt though I have enough tokens..
#### Associated error message:

- - Explorer:
```
Fail with error 'ERC20: insufficient allowance'
```
- - Wallet:
```
We were not able to estimate gas. There might be an error in the
contract and this transaction may fail.
```

#### Things to check:
- - The pools allowance to move tokens from the account
- - the amount the pool attempted to move.
- - The balance of the account at the token contract

#### What's goin on:
The tokens contract is reverting at the point the pool contract attempts to perform a `transferFrom`, to move tokens from the repaying account. 
The revertion error indicates the allowance of the caller (pool) is less than the amount attempting to be transferred. 
What can be unusual here, is that it's possible you perform the checks above, the allowance shows as equal to or slightly greater than the amount in the repayment transaction and yet you still receive the same error. In this case you can approve again with a buffer on the amount.

- Quick fix
Approve again, adding a 10% buffer to the approval amount. 
- - If you are repaying 100 usdt approve 110 usdt.

#### Manual approval:
Using a block explorer (https://scrollscan.com/), travel to the address for the token you are trying to repay

<table>
    <tr>
    <th>
      Steps    
    </th>
    <th>
      Explorer: Token address > Contract tab > Write contract
  </th>
  </tr>
  <tr>
    <td>
        1. Obtain the addresses for the pool and token contracts  <br>
        2. Travel to the tokens address using the  explorer.<br>
        3. Click the `Contract` tab, then navigate to the `Write contract` section. <br>
        4. Connect your wallet, enter the pool address under spender, and number of tokens to approve under amount.<br>
        5. Click `Write`.
    </td>
    <td>
      <img src="https://github.com/0xMaka/cog/assets/12489182/07ea6a23-d894-4681-8760-b131858489b0" align="right" width="350"/> 
    </td>
  </tr>
  <tr>
    <td>
      <img width=550/>
    </td>
      <td>
      <img width=350/>
    </td>
  </tr>
</table>

- Obtaining the pool address:
This can be sourced from the wallet pre repay confirmation, from a failed transaction under `interacted with:`, or from the pair lists found on github.<br>

- Obtaining the token address:
This can be sourced from the wallet pre approval confirmation, or via traveling to a token holders address (pool) in a block explorer and clicking on the token in the drop down list, as well as from the token lists found on github.<br>

#### Why isn't the solution more eligant?
- Still looking into the specifics

--- 

### Cannot remove collateral after having repaid:
#### Associated error message:

- - Explorer:
```
Fail
```
- - Wallet:
```
We were not able to estimate gas. There might be an error in the
contract and this transaction may fail.
```

#### Things to check:
- - The value returned by moving the slider to 100%
- - The accounts `collateral share` at the pool contract
- - The value returned by converting the amount to shares, via the pools `amountToShares` function.

#### What's goin on:
The slider can at 100% input more than the accounts total collateral.

In most cases the slider should input the excact amount that can be withdrawn, though in some cases it will overshoot, needing the caller to manually enter the correct value or remove a less than optimal amount.

Using the amount of collateral found under `balance` on the remove collateral tab should work.
However, the UI rounds to the nearest whole number and there is a conversion of amount to shares as well as some rounding that always favors the protocol.
If finding you cannot remove that amount, then grab the exact amount from `user_collateral_share` and input the value returned by that function.

- Quick fix

Manually enter an amount equal to or less than the collateral share.
- - If the slider at 100% shows `100.545684` usdt, when the collateral added was 100 usdt, try to remove `100.000000`, if still experiencing issues grab the exact number from `user_collateral_share`. <br> In the unlikely case that the above doesn't work, use the fractionally smaller number returned by `amountToShares`


#### Obtaining the user collateral share:
- Verified pool contract

If the pool contract is verified at the explorer (in most cases this should happen automatically), then it as simple as navigating to the `Read tab` of the pool contract and calling the `user_collateral_share` method.

<table>
    <tr>
    <th>
      Steps    
    </th>
    <th>
      Explorer: Pair address > Contract tab > Read contract
  </th>
  </tr>
  <tr>
    <td>
        1. Obtain the address for the pool contract.<br>
        2. Travel to the pools address using the explorer.<br>
        3. Click the `Contract` tab, then navigate to the `Read contract` section. <br>
        4. Scroll down to `22. user_collateral_share`, enter the address of the withdrawing account under `arg0`.<br>
        5. Click `Query`.
    </td>
    <td>
      <img src="https://github.com/0xMaka/cog/assets/12489182/f699d0c2-8064-4520-b492-3be876963e0c" align="right" width="350"/> 

    </td>
  </tr>
  <tr>
    <td>
      <img width=550/>
    </td>
      <td>
      <img width=350/>
    </td>
  </tr>
</table>

- Unverified pool contract

In a scenario where the contract is not verified, the method can be called programatically. 
Accompanying the faq is a module called `cog_pair.py`, this can be used to quickly make a static call without any configuration, contract instances or abi.

<table class="fixed-align">
  <tbody>
   <tr>
  <th>
    Helper script
  </th>
    </tr>  
    <tr>
  <td valign="top", valign="center">
 
  ```python
  >>> #-------------------------------------------------------------------
  >>> # cog_pair.py can be used to quickly pull data from a pool contract. 
  >>> #-------------------------------------------------------------------
  >>> import cog_pair as cp
  >>> pair = '0x20b3a538aA525Cf5F8aF25052AE849471d96138B'
  >>> user = '0x4b189EE51829E2628EBA63f024fbE7015f472576'
  >>> cp.user_collateral_share(pair,user)
1998309
```
    
</td>
  </tr>
 
  <tr>
<td>
  <img width=800/>
</td>
  </tr>
</table>

#### Why hasn't a fix been pushed:
 - An inconsitancy in recreating the issue

---
