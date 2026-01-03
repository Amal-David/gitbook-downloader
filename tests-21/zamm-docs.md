# Table of Contents

- [ZAMM Protocol](#zamm-protocol)
  - [1 Design Fundamentals](#1-design-fundamentals)
    - [1.1 Constant‑Product Pools](#1-1-constant-product-pools)
    - [1.2 ERC‑6909 LP Tokens](#1-2-erc-6909-lp-tokens)
    - [1.3 Transient Storage Credit](#1-3-transient-storage-credit)
    - [1.4 TWAP Oracle](#1-4-twap-oracle)
    - [1.5 Hook System](#1-5-hook-system)
      - [Hook Interface](#hook-interface)
  - [2 Contract Addresses & Deployment](#2-contract-addresses-deployment)
    - [CREATE3 Deployment Strategy](#create3-deployment-strategy)
  - [3 Integration Guide](#3-integration-guide)
    - [3.1 Router Patterns](#3-1-router-patterns)
      - [Efficient Multi-hop Routing](#efficient-multi-hop-routing)
    - [3.2 ERC-7702 Batching](#3-2-erc-7702-batching)
      - [ERC-7702 Benefits](#erc-7702-benefits)
    - [3.3 Gas Optimization Tips](#3-3-gas-optimization-tips)
      - [Best Practices for Gas Efficiency](#best-practices-for-gas-efficiency)
  - [4 Pool Lifecycle](#4-pool-lifecycle)
    - [4.1 `addLiquidity()`](#4-1-addliquidity)
    - [4.2 `removeLiquidity()`](#4-2-removeliquidity)
  - [5 Swapping](#5-swapping)
    - [5.1 `swapExactIn()`](#5-1-swapexactin)
    - [5.2 `swapExactOut()`](#5-2-swapexactout)
    - [5.3 `swap()` (low‑level)](#5-3-swap-low-level)
    - [5.4 Price Calculations](#5-4-price-calculations)
  - [6 Orderbook System](#6-orderbook-system)
    - [Orderbook vs AMM Trade-offs](#orderbook-vs-amm-trade-offs)
    - [6.1 `makeOrder()`](#6-1-makeorder)
      - [Order Structure](#order-structure)
    - [6.2 `fillOrder()`](#6-2-fillorder)
    - [6.3 `cancelOrder()`](#6-3-cancelorder)
    - [6.4 `redemptions`](#6-4-redemptions)
  - [7 Timelock System](#7-timelock-system)
    - [Timelock Use Cases](#timelock-use-cases)
    - [7.1 `lockup()`](#7-1-lockup)
    - [7.2 `unlock()`](#7-2-unlock)
      - [Timelock Storage](#timelock-storage)
  - [8 Token Factory](#8-token-factory)
    - [Token Creation Patterns](#token-creation-patterns)
  - [9 Transient Balance API](#9-transient-balance-api)
  - [10 Fee Control](#10-fee-control)
    - [Protocol Fee Mechanism](#protocol-fee-mechanism)
  - [11 Error Handling](#11-error-handling)
  - [12 Security Notes & Best Practices](#12-security-notes-best-practices)
    - [Pool Key Considerations](#pool-key-considerations)
    - [Common Integration Pitfalls](#common-integration-pitfalls)
  - [13 Example Workflows](#13-example-workflows)
    - [13.1 Single‑hop ETH → DAI](#13-1-single-hop-eth-dai)
    - [13.2 Two‑hop WBTC → ETH → USDC with Transient Credit](#13-2-two-hop-wbtc-eth-usdc-with-transient-credit)
    - [13.3 Create and Fill Limit Order](#13-3-create-and-fill-limit-order)
    - [13.4 Timelock ETH for Vesting](#13-4-timelock-eth-for-vesting)
    - [13.5 Hook-Enabled Pool](#13-5-hook-enabled-pool)
    - [13.6 Advanced: Arbitrage with Orderbook + AMM](#13-6-advanced-arbitrage-with-orderbook-amm)
  - [14 Quick ABI Reference](#14-quick-abi-reference)
  - [15 License](#15-license)

---


# ZAMM Protocol

Source: https://docs.zamm.eth.limo/

# ZAMM Overview

**ZAMM** is a *singleton* smart‑contract
implementing a gas‑minimized Uniswap V2–style constant‑product
market. It wraps liquidity shares and custom tokens in the ERC‑6909
multi‑token standard, introduces
**transient storage credit** for efficient routing, and
includes native **orderbook**,
**timelock**, and **hook** systems for
comprehensive DeFi infrastructure.

## 1 Design Fundamentals

## 1.1 Constant‑Product Pools

Each pool obeys `x·y = k`. Pools are identified by
`poolId = keccak256(PoolKey)` where
`PoolKey` includes:

```
{
  id0, id1       // ERC‑6909 token IDs (0 = ERC‑20 / native ETH)
  token0, token1 // contract addresses (address(0) = native ETH)
  feeOrHook      // basis‑points fee ≤ 10000 OR hook address with flags
}
```

Ordering rules guarantee a single canonical ID for any unordered pair.

## 1.2 ERC‑6909 LP Tokens

Add‑/remove‑liquidity mints/burns a fungible ERC‑6909 token whose
`tokenContract == address(this)` and
`id == poolId`. The pool's `supply` field tracks
total liquidity and supports `transfer()`/`approve()`
natively through the ERC-6909 standard.

## 1.3 Transient Storage Credit

During a transaction ZAMM can *credit* balances to the caller in transient storage (EIP‑1153
style). This creates a zero-transfer accounting system inside the
contract, eliminating costly external token movements.

* `deposit(token,id,amount)` credits manually.
* Any `_safeTransfer(...,to)` where
  `to == address(this)` credits automatically.
* `_useTransientBalance()` spends credit inside
  swaps/liquidity adds.
* Unused credit can be reclaimed via
  `recoverTransientBalance()`.

This mechanism lets routers build multihop paths with just a single
external transfer at entry and exit — reducing gas costs by orders of
magnitude compared to traditional approaches.

## 1.4 TWAP Oracle

ZAMM maintains price accumulators for each pool, enabling
time-weighted average price (TWAP) calculations. Each time a pool is
updated, the price accumulator is updated if any time has passed since
the last update:

```
pool.price0CumulativeLast += uint256(uqdiv(encode(reserve1), reserve0)) * timeElapsed;
pool.price1CumulativeLast += uint256(uqdiv(encode(reserve0), reserve1)) * timeElapsed;
```

These accumulators can be used by external contracts to calculate
price averages over any time period, providing a
manipulation-resistant price oracle similar to Uniswap V2's approach.

## 1.5 Hook System

ZAMM supports extensible hooks that can be triggered before and/or
after key operations. Hooks are specified in the pool's
`feeOrHook` field using flag bits:

```
// Hook flags from contract
uint256 constant FLAG_BEFORE = 1 << 255;  // Execute before action
uint256 constant FLAG_AFTER  = 1 << 254;  // Execute after action
uint256 constant ADDR_MASK   = (1 << 160) - 1;  // Address portion


// If no flags are set, defaults to FLAG_AFTER only
```

## Hook Interface

Hook contracts must implement the `IZAMMHook` interface:

```
interface IZAMMHook {
    function beforeAction(
        bytes4 sig, 
        uint256 poolId,
        address sender,
        bytes calldata data
    ) external returns (uint256 feeBps);


    function afterAction(
        bytes4 sig,
        uint256 poolId,
        address sender,
        int256 d0,     // token0 delta
        int256 d1,     // token1 delta  
        int256 dLiq,   // liquidity delta
        bytes calldata data
    ) external;
}
```

The `beforeAction` hook can override the fee for that
specific transaction by returning a non-zero value. The
`afterAction` hook receives deltas for all state changes.

## 2 Contract Addresses & Deployment

**Address:**

0x000000000000040470635EB91b7CE4D132D616eD

## CREATE3 Deployment Strategy

ZAMM utilizes CREATE3 for deterministic deployment, allowing
identical contract addresses across all EVM blockchains. This
approach ensures that the protocol maintains a consistent identity
while supporting chain-specific customizations.

Key benefits:

* Single recognizable address across all networks, simplifying
  integration
* Per-chain parameter customization without changing contract
  identity
* Seamless extensibility with existing DeFi ecosystems on each chain
* Network effect amplification through unified liquidity addressing

## 3 Integration Guide

This section provides practical guidance for developers integrating
ZAMM into wallets, routers, and other DeFi applications.

## 3.1 Router Patterns

## Efficient Multi-hop Routing

ZAMM's transient storage system enables extremely gas-efficient
multi-hop swaps. The key insight is to deposit tokens once, perform
all intermediate swaps with `to=address(this)` to
accumulate transient credit, then perform the final swap to the
destination address.

```
// Efficient 3-hop: USDC → WETH → WBTC → DAI
contract MyRouter {
    function multiHopSwap(
        uint256 amountIn,
        uint256 amountOutMin,
        PoolKey[] calldata pools,
        address to
    ) external {
        IERC20(USDC).transferFrom(msg.sender, address(this), amountIn);
        IERC20(USDC).approve(address(zamm), amountIn);
        
        // 1. Deposit USDC once
        zamm.deposit(USDC, 0, amountIn);
        
        // 2. USDC→WETH (output to transient storage)
        zamm.swap(pools[0], 0, wethOut, address(zamm), "");
        
        // 3. WETH→WBTC (output to transient storage)  
        zamm.swap(pools[1], 0, wbtcOut, address(zamm), "");
        
        // 4. WBTC→DAI (final output to user)
        zamm.swapExactIn(pools[2], wbtcOut, amountOutMin, true, to, deadline);
    }
}
```

## 3.2 ERC-7702 Batching

ZAMM leverages ERC-7702 for wallet-level transaction batching rather
than contract-level multicall. This approach provides better gas
efficiency and user experience by batching at the account abstraction
layer.

```
// ERC-7702 compatible wallet batching
// Atomic liquidity add + limit order + timelock
const batchedTxs = [
    // 1. Add liquidity to WETH/USDC pool
    {
        to: zamm,
        value: ethers.parseEther("1"),
        data: zamm.interface.encodeFunctionData("addLiquidity", [
            wethUsdcPool, 
            ethers.parseEther("1"), 
            ethers.parseUnits("3000", 6),
            ethers.parseEther("0.95"), 
            ethers.parseUnits("2850", 6),
            userAddress, 
            deadline
        ])
    },
    
    // 2. Create limit order with excess WETH
    {
        to: zamm,
        value: ethers.parseEther("0.05"),
        data: zamm.interface.encodeFunctionData("makeOrder", [
            ethers.ZeroAddress, 0, ethers.parseEther("0.05"),  // sell 0.05 ETH
            USDC, 0, ethers.parseUnits("150", 6),              // for 150 USDC  
            deadline, true                                      // allow partial fills
        ])
    },
    
    // 3. Lock remaining tokens for 6 months
    {
        to: zamm,
        value: 0,
        data: zamm.interface.encodeFunctionData("lockup", [
            USDC, userAddress, 0, 
            ethers.parseUnits("500", 6), 
            Math.floor(Date.now() / 1000) + (180 * 24 * 3600)
        ])
    }
];


// Execute as batched transaction via ERC-7702 wallet
await wallet.executeBatch(batchedTxs);
```

## ERC-7702 Benefits

* **Native batching:** Transactions are batched at the
  wallet level, not requiring contract support
* **Better UX:** Users see a single transaction rather
  than multiple contract calls
* **Gas efficiency:** Eliminates delegatecall overhead
  from contract-level batching
* **Atomic execution:** All operations succeed or fail
  together
* **Flexible composition:** Can batch ZAMM calls with
  other protocol interactions

## 3.3 Gas Optimization Tips

## Best Practices for Gas Efficiency

* **Batch operations:** Use ERC-7702 wallet batching to
  combine multiple ZAMM operations in a single transaction
* **Minimize external transfers:** Leverage transient
  storage to avoid redundant token transfers between hops
* **Use exact calculations:** Pre-calculate swap
  amounts off-chain when possible to avoid reverts
* **Efficient data packing:** Use compact structs and
  avoid unnecessary storage reads
* **Hook optimization:** Keep hook contracts minimal -
  they execute on every swap/liquidity operation

**Gas Comparison (approximate):**

```
// Traditional 3-hop (3 separate transactions)
USDC→WETH: ~80k gas + external transfers
WETH→WBTC: ~80k gas + external transfers  
WBTC→DAI: ~80k gas + external transfers
Total: ~240k gas + 6 external transfers


// ZAMM transient storage (single batched transaction)
3-hop batch: ~120k gas + 1 initial transfer + 1 final transfer
Savings: ~50% gas + 67% fewer external transfers
```

## 4 Pool Lifecycle

## 4.1 `addLiquidity()`

```
function addLiquidity(
    PoolKey calldata poolKey,
    uint256 amount0Desired,
    uint256 amount1Desired,
    uint256 amount0Min,
    uint256 amount1Min,
    address to,
    uint256 deadline
) public payable lock returns (uint256 amount0, uint256 amount1, uint256 liquidity)
```

Add assets to a pool, receiving LP tokens. Supports transient credit
and native ETH. For new pools, the ratio sets the initial price. For
existing pools, amounts are adjusted to match the current pool ratio.
Excess ETH is automatically refunded when more is provided than
needed.

**Pool Creation:** The first
`addLiquidity` call to a new pool will create it and
enforce token ordering rules. ETH pools require
`token0 == address(0)` and `id0 == 0`.

## 4.2 `removeLiquidity()`

```
function removeLiquidity(
    PoolKey calldata poolKey,
    uint256 liquidity,
    uint256 amount0Min,
    uint256 amount1Min,
    address to,
    uint256 deadline
) public lock returns (uint256 amount0, uint256 amount1)
```

Burn LP tokens for underlying reserves. The function calculates
amounts proportionally:
`amount0 = liquidity * reserve0 / totalSupply`.
`amount0Min/amount1Min` guard against slippage.

## 5 Swapping

## 5.1 `swapExactIn()`

```
function swapExactIn(
    PoolKey calldata poolKey,
    uint256 amountIn,
    uint256 amountOutMin,
    bool zeroForOne,
    address to,
    uint256 deadline
) public payable lock returns (uint256 amountOut)
```

* `zeroForOne=true` sells token0 for token1.
* Accepts transient credit or pulls tokens / `msg.value`.
* Reverts on `amountOut < amountOutMin`.
* Supports hooks that can modify the effective fee rate.

## 5.2 `swapExactOut()`

```
function swapExactOut(
    PoolKey calldata poolKey,
    uint256 amountOut,
    uint256 amountInMax,
    bool zeroForOne,
    address to,
    uint256 deadline
) public payable lock returns (uint256 amountIn)
```

Specify exact output amount, calculates required input. Refunds excess
ETH when provided. Uses the same fee and hook logic as
`swapExactIn`.

## 5.3 `swap()` (low‑level)

```
function swap(
    PoolKey calldata poolKey,
    uint256 amount0Out,
    uint256 amount1Out,
    address to,
    bytes calldata data
) public lock
```

Flash‑style primitive patterned after Uniswap V2. When
`to == address(this)` the output is credited to transient
storage, enabling efficient **multihop** sequences inside
a router. If `data` is non‑empty,
`IZAMMCallee(to).zammCall` will be invoked.

**Important:** This function expects input tokens to
already be present via transient balance or previous transfers. It
checks the `x*y=k` invariant after fees are applied.

## 5.4 Price Calculations

ZAMM includes helper functions for calculating swap amounts based on
the constant product formula with fees:

```
// Calculate output amount given an exact input amount
function _getAmountOut(uint256 amountIn, uint256 reserveIn, uint256 reserveOut, uint256 swapFee)
    internal pure returns (uint256 amountOut) {
    uint256 amountInWithFee = amountIn * (10000 - swapFee);
    uint256 numerator = amountInWithFee * reserveOut;
    uint256 denominator = (reserveIn * 10000) + amountInWithFee;
    return numerator / denominator;
}


// Calculate input amount needed for an exact output amount
function _getAmountIn(uint256 amountOut, uint256 reserveIn, uint256 reserveOut, uint256 swapFee)
    internal pure returns (uint256 amountIn) {
    uint256 numerator = reserveIn * amountOut * 10000;
    uint256 denominator = (reserveOut - amountOut) * (10000 - swapFee);
    return (numerator / denominator) + 1;
}
```

## 6 Orderbook System

ZAMM includes a native orderbook system that allows users to place
limit orders that can be filled by other traders. Orders support both
full-fill and partial-fill modes, with automatic ETH escrow for sell
orders.

## Orderbook vs AMM Trade-offs

The integrated orderbook complements the AMM by providing:

* **Price improvement:** Execute at exact limit prices
  rather than AMM slippage
* **Capital efficiency:** No impermanent loss for limit
  orders
* **MEV protection:** Orders execute at predetermined
  prices
* **Time preference:** Set orders to execute when
  market conditions are favorable

Use AMM for immediate execution and liquidity, orderbook for
price-sensitive trades and advanced strategies.

## 6.1 `makeOrder()`

```
function makeOrder(
    address tokenIn,    // token being sold
    uint256 idIn,       // token ID (0 for ERC-20)
    uint96 amtIn,       // amount being sold
    address tokenOut,   // token being bought
    uint256 idOut,      // token ID (0 for ERC-20)
    uint96 amtOut,      // amount desired
    uint56 deadline,    // order expiration
    bool partialFill    // allow partial fills
) payable returns (bytes32 orderHash)
```

Creates a new limit order. Key features:

* ETH orders are automatically escrowed when
  `tokenIn == address(0)`
* Orders are identified by a hash of all parameters including the
  maker address
* Supports both full-fill-only and partial-fill modes
* Orders expire at the specified deadline

## Order Structure

```
struct Order {
    bool partialFill;    // whether partial fills are allowed
    uint56 deadline;     // expiration timestamp
    uint96 inDone;       // amount of tokenIn already filled
    uint96 outDone;      // amount of tokenOut already paid
}
```

## 6.2 `fillOrder()`

```
function fillOrder(
    address maker,       // original order creator
    address tokenIn,     // must match order
    uint256 idIn,
    uint96 amtIn,        // full order amount
    address tokenOut,
    uint256 idOut,
    uint96 amtOut,       // full order amount
    uint56 deadline,
    bool partialFill,
    uint96 fillPart      // 0 = "take remainder", or specific amount
) payable
```

Fills an existing order. Key behaviors:

* For partial fills: `fillPart` specifies amount, or 0 to
  fill remaining
* For full fills: `fillPart` must be 0 or equal to
  `amtOut`
* Proportional calculation ensures fair pricing across partial fills
* Orders are automatically deleted when fully filled

## 6.3 `cancelOrder()`

```
function cancelOrder(
    address tokenIn,
    uint256 idIn,
    uint96 amtIn,
    address tokenOut,
    uint256 idOut,
    uint96 amtOut,
    uint56 deadline,
    bool partialFill
) public
```

Cancels an existing order. For partial-fill orders, any escrowed ETH
minus already-filled amounts is returned to the maker.

**Gas Optimization:** The orderbook uses tight packing
and efficient storage patterns. Orders are stored as structs with
uint96 amounts to fit multiple values in single storage slots, and
order hashes are computed from all parameters to avoid collisions.

## 6.4 `redemptions`

ZAMM provides a burn/redemption mechanism through its orderbook. Users may create an order that pays out a new token in exchange for users programmatically burning it by making a transient deposit that gets spent on their "fill". This is an advanced pattern that should be used in conjunction with secure helper contracts.

## 7 Timelock System

ZAMM includes a native timelock system for secure, delayed transfers
of any supported token type. This enables trustless escrow, vesting
schedules, and delayed governance actions.

## Timelock Use Cases

* **Vesting schedules:** Lock team tokens with staged
  releases
* **Trustless escrow:** Lock funds until conditions are
  met
* **Self-imposed restrictions:** Prevent impulsive
  trading decisions
* **Governance delays:** Lock proposals until voting
  periods end
* **Savings accounts:** Lock funds for forced savings
  with penalties

## 7.1 `lockup()`

```
function lockup(
    address token,       // token contract (address(0) for ETH)
    address to,          // beneficiary
    uint256 id,          // token ID (0 for ERC-20)
    uint256 amount,      // amount to lock
    uint256 unlockTime   // when funds can be claimed
) payable returns (bytes32 lockHash)
```

Creates a timelock for tokens. Features:

* Supports ETH, ERC-20, and ERC-6909 tokens
* ETH is automatically escrowed via `msg.value`
* Lock hash is computed from all parameters for unique identification
* Emits `Lock` event for tracking
* Reverts if `unlockTime ≤ block.timestamp`

## 7.2 `unlock()`

```
function unlock(
    address token,
    address to,
    uint256 id,
    uint256 amount,
    uint256 unlockTime
) public
```

Claims locked tokens after the unlock time. Requirements:

* Must provide exact same parameters used in `lockup()`
* Current time must be ≥ `unlockTime`
* Lock must exist (not already claimed)
* Anyone can call this function - not restricted to the beneficiary

## Timelock Storage

```
mapping(bytes32 lockHash => uint256 unlockTime) public lockups;


// Lock hash computation
lockHash = keccak256(abi.encode(token, to, id, amount, unlockTime));
```

The timelock system uses minimal storage by only tracking unlock
times. The lock parameters are embedded in the hash, ensuring that
tokens can only be unlocked with the exact original parameters.

## 8 Token Factory

ZAMM includes a streamlined token factory for creating new ERC-6909
tokens with optional metadata.

```
function coin(address creator, uint256 supply, string calldata uri)
    public returns (uint256 coinId)
```

Features:

* Sequential coin IDs starting from 1 (auto-incremented)
* Mints entire supply to creator address
* Emits URI event for metadata tracking
* Gas-optimized for high-frequency token creation
* Uses `_initMint` internally to avoid approval checks

## Token Creation Patterns

```
// Simple token creation
uint256 coinId = zamm.coin(msg.sender, 1_000_000e18, "ipfs://metadata");


// Create token + immediate pool liquidity
uint256 coinId = zamm.coin(address(this), 1_000_000e18, "ipfs://metadata");
ZERC6909(address(zamm)).approve(msg.sender, coinId, 500_000e18);


// Add liquidity with newly created token
zamm.addLiquidity{value: 10 ether}(
    PoolKey(coinId, 0, address(zamm), address(0), 30), // 0.3% fee
    500_000e18, 10 ether, // 50% of supply paired with 10 ETH
    490_000e18, 9.5 ether, // 2% slippage tolerance
    msg.sender, block.timestamp + 300
);
```

## 9 Transient Balance API

| Function | Purpose |
| --- | --- |
| `deposit(token,id,amount)` | Pre‑credit balance. Use before calling swaps in the same tx. |
| `recoverTransientBalance(token,id,to)` | Withdraw leftover credit at end of tx. |
| `receive()` | Automatically credits ETH sent directly to contract. |

**Tip:** If you build a router, structure calls as:

1. `deposit()` for input tokens once
2. series of `swap()` (or `swapExactIn`) with
   `to=this`
3. final `swapX` with external `to`
4. optional `recoverTransientBalance`

For wallet-level batching, use ERC-7702 to execute multiple ZAMM
calls atomically.

## 10 Fee Control

`setFeeTo(address)` sets the protocol‑fee recipient.
`setFeeToSetter(address)` transfers admin rights. Only the
current `feeToSetter` (initialized to deployer) may call
either function.

## Protocol Fee Mechanism

When enabled (by setting a non-zero `feeTo` address), the
protocol collects a fee calculated as 1/6th of the growth in sqrt(k)
each time liquidity is added or removed. The fee is stored in the
pool's `kLast` field:

```
// in _mintFee function  
uint256 rootK = sqrt(uint256(reserve0) * reserve1);
uint256 rootKLast = sqrt(pool.kLast);
if (rootK > rootKLast) {
    uint256 numerator = pool.supply * (rootK - rootKLast);
    uint256 denominator = rootK * 5 + rootKLast;
    uint256 liquidity = numerator / denominator;
    if (liquidity > 0) {
        _mint(feeTo, poolId, liquidity);
    }
    pool.supply += liquidity;
}
```

This mechanism captures trading fees proportional to liquidity
growth, distributing them as LP tokens to the protocol fee
recipient.

## 11 Error Handling

ZAMM uses custom errors for gas efficiency. Key errors include:

| Error | Meaning |
| --- | --- |
| `Reentrancy()` | Reentrancy attempt detected |
| `Expired()` | Transaction deadline has passed |
| `InvalidMsgVal()` | Incorrect ETH amount sent |
| `InsufficientLiquidity()` | Not enough liquidity in pool |
| `InsufficientInputAmount()` | Input amount too low |
| `InsufficientOutputAmount()` | Output amount too low |
| `K()` | Invariant x\*y=k broken |
| `InvalidFeeOrHook()` | Fee above maximum or invalid hook address |
| `InvalidPoolTokens()` | Token ordering violated |
| `InsufficientLiquidityMinted()` | LP tokens amount too small |
| `Unauthorized()` | Caller not authorized |
| `Overflow()` | Arithmetic overflow |
| `Pending()` | Order/lock already exists or timelock not ready |
| `BadSize()` | Invalid fill amount for orderbook operation |

## 12 Security Notes & Best Practices

## Pool Key Considerations

When implementing ZAMM integrations, pay special attention to the
`feeOrHook` field in `PoolKey`:

```
// Fee-only pool (traditional)
PoolKey memory feePool = PoolKey({
    id0: 0, id1: 0,
    token0: WETH, token1: USDC,
    feeOrHook: 30  // 0.3% fee
});


// Hook-enabled pool  
PoolKey memory hookPool = PoolKey({
    id0: 0, id1: 0,
    token0: WETH, token1: USDC,
    feeOrHook: uint256(uint160(hookContract)) | FLAG_BEFORE | FLAG_AFTER
});
```

**Important:** Hook-enabled pools may have dynamic fees
determined by the hook contract's `beforeAction` return
value.

## Common Integration Pitfalls

* **ETH handling:** Always check if
  `token == address(0)` and handle
  `msg.value` correctly
* **Token ordering:** Ensure tokens follow ZAMM's
  ordering rules to avoid `InvalidPoolTokens` errors
* **Transient storage cleanup:** Always call
  `recoverTransientBalance` to avoid leaving dust
* **Deadline usage:** Set realistic deadlines to
  prevent transaction failures in high congestion
* **Hook awareness:** Check if pools use hooks which
  may affect gas costs and behavior
* **Order hash calculation:** Include all parameters in
  correct order when reconstructing order hashes
* **ERC-7702 compatibility:** Ensure wallet supports
  ERC-7702 batching for optimal gas efficiency

* Re‑entrancy is blocked via a transient guard (`lock`
  modifier) using EIP-1153 transient storage.
* Pools with identical tokens must follow ordering rules or calls
  revert.
* Transient credit is *cleared* the moment it is consumed —
  unused credit is recoverable but never leaks.
* Hook contracts should be carefully audited as they have execution
  control during swaps and liquidity operations.
* Orderbook ETH escrow is automatic but partial fills require careful
  accounting of filled amounts.
* Timelock parameters are immutable once created - double-check unlock
  times before calling `lockup()`.
* Always pass explicit `deadline` to mitigate price racing.
* All arithmetic is `unchecked` where overflow is
  impossible by design; review upstream math if extending.

## 13 Example Workflows

## 13.1 Single‑hop ETH → DAI

```
// Direct swap call
zamm.swapExactIn{value: 1 ether}(
  PoolKey({
    id0: 0, id1: 0,
    token0: address(0),  // ETH
    token1: DAI,         // DAI contract
    feeOrHook: 30        // 0.30% fee
  }),
  1 ether,
  1800e18,       // minimum DAI out
  true,          // zeroForOne (ETH → DAI)
  user,
  block.timestamp + 300
);
```

## 13.2 Two‑hop WBTC → ETH → USDC with Transient Credit

```
// Using ERC-7702 wallet batching
const batchedSwaps = [
    // 1. Deposit WBTC once
    {
        to: zamm,
        value: 0,
        data: zamm.interface.encodeFunctionData("deposit", [WBTC, 0, ethers.parseUnits("1", 8)])
    },
    
    // 2. WBTC→ETH, output kept as credit
    {
        to: zamm,
        value: 0,
        data: zamm.interface.encodeFunctionData("swap", [
            keyWBTC_ETH, 0, ethOut, zamm.target, "0x"
        ])
    },
    
    // 3. ETH→USDC to user
    {
        to: zamm,
        value: 0,
        data: zamm.interface.encodeFunctionData("swapExactIn", [
            keyETH_USDC, ethOut, minUsdc, true, user, deadline
        ])
    }
];


await wallet.executeBatch(batchedSwaps);
```

## 13.3 Create and Fill Limit Order

```
// Maker: Sell 100 DAI for 0.05 ETH
bytes32 orderHash = zamm.makeOrder(
    DAI, 0, 100e18,           // selling 100 DAI
    address(0), 0, 0.05 ether, // buying 0.05 ETH
    block.timestamp + 1 days,  // 24 hour expiry
    true                       // allow partial fills
);


// Taker: Fill 50% of the order
zamm.fillOrder{value: 0.025 ether}(
    maker, DAI, 0, 100e18,
    address(0), 0, 0.05 ether,
    block.timestamp + 1 days, true,
    0.025 ether                // fill 50%
);
```

## 13.4 Timelock ETH for Vesting

```
// Lock 10 ETH for 6 months
bytes32 lockHash = zamm.lockup{value: 10 ether}(
    address(0),                    // ETH
    beneficiary,                   // recipient
    0,                            // ETH id = 0
    10 ether,                     // amount
    block.timestamp + 180 days    // 6 months
);


// Anyone can unlock after 6 months
zamm.unlock(
    address(0), beneficiary, 0, 
    10 ether, block.timestamp + 180 days
);
```

## 13.5 Hook-Enabled Pool

```
// Create pool with custom hook
PoolKey memory poolKey = PoolKey({
    id0: 0, id1: 0,
    token0: address(0), token1: USDC,
    feeOrHook: uint256(uint160(myHook)) | FLAG_BEFORE | FLAG_AFTER
});


// The hook will be called before and after all swaps/liquidity operations
// Hook can override fees by returning non-zero from beforeAction
```

## 13.6 Advanced: Arbitrage with Orderbook + AMM

```
// Arbitrage between ZAMM orderbook and external DEX
contract ZAMMArbitrageur {
    function executeArbitrage(
        bytes32 orderHash,
        uint96 fillAmount,
        address externalDex,
        bytes calldata externalSwapData
    ) external {
        // 1. Fill profitable order on ZAMM
        zamm.fillOrder{value: msg.value}(
            maker, tokenIn, idIn, amtIn,
            tokenOut, idOut, amtOut, deadline, true, fillAmount
        );
        
        // 2. Immediately swap on external DEX for profit
        (bool success,) = externalDex.call(externalSwapData);
        require(success, "External swap failed");
        
        // 3. Profit is the difference between order price and market price
    }
}
```

## 14 Quick ABI Reference

| Function (public) | Key Args | Returns |
| --- | --- | --- |
| `coin` | `creator,supply,uri` | `coinId` |
| `addLiquidity` | `PoolKey,amount0Desired,amount1Desired,…` | `amount0,amount1,liquidity` |
| `removeLiquidity` | `PoolKey,liquidity,…` | `amount0,amount1` |
| `swapExactIn` | `PoolKey,amountIn,…` | `amountOut` |
| `swapExactOut` | `PoolKey,amountOut,…` | `amountIn` |
| `swap` | `PoolKey,amount0Out,amount1Out,to,data` | — |
| `makeOrder` | `tokenIn,idIn,amtIn,tokenOut,idOut,amtOut,deadline,partialFill` | `orderHash` |
| `fillOrder` | `maker,tokenIn,idIn,amtIn,tokenOut,idOut,amtOut,deadline,partialFill,fillPart` | — |
| `cancelOrder` | `tokenIn,idIn,amtIn,tokenOut,idOut,amtOut,deadline,partialFill` | — |
| `lockup` | `token,to,id,amount,unlockTime` | `lockHash` |
| `unlock` | `token,to,id,amount,unlockTime` | — |
| `deposit` | `token,id,amount` | — |
| `recoverTransientBalance` | `token,id,to` | `amount` |
| `setFeeTo / setFeeToSetter` | `address` | — |

## 15 License

Code released under **MIT**. Documentation © 2025
*z0r0z*. No warranty.

---
