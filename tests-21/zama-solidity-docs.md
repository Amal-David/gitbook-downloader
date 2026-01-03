# Table of Contents

- [Overview](#overview)
**Getting Started**
  - [What is FHEVM Solidity](#what-is-fhevm-solidity)
  - [Quick start tutorial](#quick-start-tutorial)
**Smart Contract**
  - [Configuration](#configuration)
  - [Supported types](#supported-types)
  - [Operations on encrypted types](#operations-on-encrypted-types)
  - [Encrypted inputs](#encrypted-inputs)
  - [Access Control List](#access-control-list)
  - [Logics](#logics)
  - [Decryption](#decryption)
**Development Guide**
  - [Hardhat plugin](#hardhat-plugin)
  - [Foundry](#foundry)
  - [HCU](#hcu)
  - [Migrate to v0.9](#migrate-to-v0-9)
  - [How to Transform Your Smart Contract into a FHEVM Smart Contract?](#how-to-transform-your-smart-contract-into-a-fhevm-smart-contract)

---


# Overview

Source: https://docs.zama.org/protocol/solidity-guides/

**Welcome to Solidity Guides!**

This section will guide you through writing confidential smart contracts in Solidity using the FHEVM library. With Fully Homomorphic Encryption(FHE), your contracts can operate directly on encrypted data without ever decrypting it onchain.

## Where to go next

If you’re new to the Zama Protocol, start with the [Litepaper](https://docs.zama.ai/protocol/zama-protocol-litepaper) or the [Protocol Overview](https://docs.zama.ai/protocol) to understand the foundations.

Otherwise:

🟨 Go to [**What is FHEVM**](/protocol/solidity-guides/getting-started/overview) to learn about the core concepts and features.

🟨 Go to [**Quick Start Tutorial**](/protocol/solidity-guides/getting-started/quick-start-tutorial) to build and test your first confidential smart contract.

🟨 Go to [**Smart Contract Guides**](/protocol/solidity-guides/smart-contract/configure) for details on encrypted types, supported operations, inputs, ACL, and decryption flows.

🟨 Go to [**Development Guides**](/protocol/solidity-guides/development-guide/hardhat) to set up your local environment with Hardhat or Foundry and deploy FHEVM contracts.

🟨 Go to [**Migration Guide**](/protocol/solidity-guides/development-guide/migration) if you're upgrading from a previous version to the latest.

## Help center

Ask technical questions and discuss with the community.

* [Community forum](https://community.zama.ai/c/fhevm/15)
* [Discord channel](https://discord.com/invite/zama)

[NextWhat is FHEVM Solidity](/protocol/solidity-guides/getting-started/overview)

Last updated 17 days ago

---


# What is FHEVM Solidity

Source: https://docs.zama.org/protocol/solidity-guides/getting-started/overview

This document provides an overview of key features of the FHEVM smart contract library.

## Configuration and initialization

Smart contracts using FHEVM require proper configuration and initialization:

* **Environment setup**: Import and inherit from environment-specific configuration contracts
* **Relayer configuration**: Configure secure relayer access for cryptographic operations
* **Initialization checks**: Validate encrypted variables are properly initialized before use

For more information see [Configuration](/protocol/solidity-guides/smart-contract/configure).

## Encrypted data types

FHEVM introduces encrypted data types compatible with Solidity:

* **Booleans**: `ebool`
* **Unsigned Integers**: `euint8`, `euint16`, `euint32`, `euint64`, `euint128`, `euint256`
* **Addresses**: `eaddress`
* **Input**: `externalEbool`, `externalEaddress`, `externalEuintXX` for handling encrypted input data

Encrypted data is represented as ciphertext handles, ensuring secure computation and interaction.

For more information see [use of encrypted types](/protocol/solidity-guides/smart-contract/types).

## Casting types

fhevm provides functions to cast between encrypted types:

* **Casting between encrypted types**: `FHE.asEbool` converts encrypted integers to encrypted booleans
* **Casting to encrypted types**: `FHE.asEuintX` converts plaintext values to encrypted types
* **Casting to encrypted addresses**: `FHE.asEaddress` converts plaintext addresses to encrypted addresses

For more information see [use of encrypted types](/protocol/solidity-guides/smart-contract/types).

## Confidential computation

fhevm enables symbolic execution of encrypted operations, supporting:

* **Arithmetic:** `FHE.add`, `FHE.sub`, `FHE.mul`, `FHE.min`, `FHE.max`, `FHE.neg`, `FHE.div`, `FHE.rem`

  + Note: `div` and `rem` operations are supported only with plaintext divisors
* **Bitwise:** `FHE.and`, `FHE.or`, `FHE.xor`, `FHE.not`, `FHE.shl`, `FHE.shr`, `FHE.rotl`, `FHE.rotr`
* **Comparison:** `FHE.eq`, `FHE.ne`, `FHE.lt`, `FHE.le`, `FHE.gt`, `FHE.ge`
* **Advanced:** `FHE.select` for branching on encrypted conditions, `FHE.randEuintX` for on-chain randomness.

For more information on operations, see [Operations on encrypted types](/protocol/solidity-guides/smart-contract/operations).

For more information on conditional branching, see [Conditional logic in FHE](/protocol/solidity-guides/smart-contract/logics/conditions).

For more information on random number generation, see [Generate Random Encrypted Numbers](/protocol/solidity-guides/smart-contract/operations/random).

## Access control mechanism

fhevm enforces access control with a blockchain-based Access Control List (ACL):

* **Persistent access**: `FHE.allow`, `FHE.allowThis` grants permanent permissions for ciphertexts.
* **Transient access**: `FHE.allowTransient` provides temporary access for specific transactions.
* **Validation**: `FHE.isSenderAllowed` ensures that only authorized entities can interact with ciphertexts.
* **Persistent public decryption**: `FHE.makePubliclyDecryptable`, `FHE.isPubliclyDecryptable` makes a given ciphertext permanently publicly decryptable.

For more information see [ACL](/protocol/solidity-guides/smart-contract/acl).


Last updated 1 month ago

---


# Quick start tutorial

Source: https://docs.zama.org/protocol/solidity-guides/getting-started/quick-start-tutorial

This tutorial guides you to start quickly with Zama’s **Fully Homomorphic Encryption (FHE)** technology for building confidential smart contracts.

## What You’ll Learn

In **about 30 minutes**, you'll go from a basic Solidity contract to a fully confidential one using **FHEVM**. Here's what you'll do:

1. Set up your development environment
2. Write a simple Solidity smart contract
3. Convert it into an FHEVM-compatible confidential contract
4. Test your FHEVM-compatible confidential contract

## Prerequisite

* A basic understanding of **Solidity** library and **Ethereum**.
* Some familiarity with **Hardhat.**

**About Hardhat**

[**Hardhat**](https://hardhat.org/) is a development environment for compiling, deploying, testing, and debugging Ethereum smart contracts. It’s widely used in the Ethereum ecosystem.

In this tutorial, we'll introduce the FHEVM hardhat template that provides an easy way to use FHEVM.


Last updated 2 months ago

---


# Configuration

Source: https://docs.zama.org/protocol/solidity-guides/smart-contract/configure

This document explains how to enable encrypted computations in your smart contract by setting up the `fhevm` environment. Learn how to integrate essential libraries, configure encryption, and add secure computation logic to your contracts.

## Core configuration setup

To utilize encrypted computations in Solidity contracts, you must configure the **FHE library** and **Oracle addresses**. The `fhevm` package simplifies this process with prebuilt configuration contracts, allowing you to focus on developing your contract’s logic without handling the underlying cryptographic setup.

This library and its associated contracts provide a standardized way to configure and interact with Zama's FHEVM (Fully Homomorphic Encryption Virtual Machine) infrastructure on different Ethereum networks. It supplies the necessary contract addresses for Zama's FHEVM components (`ACL`, `FHEVMExecutor`, `KMSVerifier`, `InputVerifier`) and the decryption oracle, enabling seamless integration for Solidity contracts that require FHEVM support.

## Key components configured automatically

1. **FHE library**: Sets up encryption parameters and cryptographic keys.
2. **Oracle**: Manages secure cryptographic operations such as public decryption.
3. **Network-specific settings**: Adapts to local testing, testnets (Sepolia for example), or mainnet deployment.

By inheriting these configuration contracts, you ensure seamless initialization and functionality across environments.

## ZamaConfig.sol

The `ZamaConfig` library exposes functions to retrieve FHEVM configuration structs and oracle addresses for supported networks (currently only the Sepolia testnet).

Under the hood, this library encapsulates the network-specific addresses of Zama's FHEVM infrastructure into a single struct (`FHEVMConfigStruct`).

## ZamaEthereumConfig

The `ZamaEthereumConfig` contract is designed to be inherited by a user contract. The constructor automatically sets up the FHEVM coprocessor and decryption oracle using the configuration provided by the library for the respective network. When a contract inherits from `ZamaEthereumConfig`, the constructor calls `FHE.setCoprocessor` with the appropriate addresses. This ensures that the inheriting contract is automatically wired to the correct FHEVM contracts and oracle for the target network, abstracting away manual address management and reducing the risk of misconfiguration.

**Example**

## Using `isInitialized`

The `isInitialized` utility function checks whether an encrypted variable has been properly initialized, preventing unexpected behavior due to uninitialized values.

**Function signature**

**Purpose**

* Ensures encrypted variables are initialized before use.
* Prevents potential logic errors in contract execution.

**Example: Initialization Check for Encrypted Counter**

## Summary

By leveraging prebuilt a configuration contract like `ZamaEthereumConfig` in `ZamaConfig.sol`, you can efficiently set up your smart contract for encrypted computations. These tools abstract the complexity of cryptographic initialization, allowing you to focus on building secure, confidential smart contracts.


Last updated 1 month ago

---


# Supported types

Source: https://docs.zama.org/protocol/solidity-guides/smart-contract/types

This document introduces the encrypted integer types provided by the `FHE` library in FHEVM and explains their usage, including casting, state variable declarations, and type-specific considerations.

## Introduction

The `FHE` library offers a robust type system with encrypted integer types, enabling secure computations on confidential data in smart contracts. These encrypted types are validated both at compile time and runtime to ensure correctness and security.

## Key features of encrypted types

* Encrypted integers function similarly to Solidity’s native integer types, but they operate on **Fully Homomorphic Encryption (FHE)** ciphertexts.
* Arithmetic operations on `e(u)int` types are **unchecked**, meaning they wrap around on overflow. This design choice ensures confidentiality by avoiding the leakage of information through error detection.
* Future versions of the `FHE` library will support encrypted integers with overflow checking, but with the trade-off of exposing limited information about the operands.

Encrypted integers with overflow checking will soon be available in the `FHE` library. These will allow reversible arithmetic operations but may reveal some information about the input values.

Encrypted integers in FHEVM are represented as FHE ciphertexts, abstracted using ciphertext handles. These types, prefixed with `e` (for example, `euint64`) act as secure wrappers over the ciphertext handles.

## List of encrypted types

The `FHE` library currently supports the following encrypted types:

Type

Bit Length

Supported Operators

Aliases (with supported operators)

Ebool

2

and, or, xor, eq, ne, not, select, rand

Euint8

8

add, sub, mul, div, rem, and, or, xor, shl, shr, rotl, rotr, eq, ne, ge, gt, le, lt, min, max, neg, not, select, rand, randBounded

Euint16

16

add, sub, mul, div, rem, and, or, xor, shl, shr, rotl, rotr, eq, ne, ge, gt, le, lt, min, max, neg, not, select, rand, randBounded

Euint32

32

add, sub, mul, div, rem, and, or, xor, shl, shr, rotl, rotr, eq, ne, ge, gt, le, lt, min, max, neg, not, select, rand, randBounded

Euint64

64

add, sub, mul, div, rem, and, or, xor, shl, shr, rotl, rotr, eq, ne, ge, gt, le, lt, min, max, neg, not, select, rand, randBounded

Euint128

128

add, sub, mul, div, rem, and, or, xor, shl, shr, rotl, rotr, eq, ne, ge, gt, le, lt, min, max, neg, not, select, rand, randBounded

Euint160

160

Eaddress (eq, ne, select)

Euint256

256

and, or, xor, shl, shr, rotl, rotr, eq, ne, neg, not, select, rand, randBounded

Division (`div`) and remainder (`rem`) operations are only supported when the right-hand side (`rhs`) operand is a plaintext (non-encrypted) value. Attempting to use an encrypted value as `rhs` will result in a panic. This restriction ensures correct and secure computation within the current framework.

Higher-precision integer types are available in the `TFHE-rs` library and can be added to `fhevm` as needed.


Last updated 2 months ago

---


# Operations on encrypted types

Source: https://docs.zama.org/protocol/solidity-guides/smart-contract/operations

This document outlines the operations supported on encrypted types in the `FHE` library, enabling arithmetic, bitwise, comparison, and more on Fully Homomorphic Encryption (FHE) ciphertexts.

## Arithmetic operations

The following arithmetic operations are supported for encrypted integers (`euintX`):

Name

Function name

Symbol

Type

Add

`FHE.add`

`+`

Binary

Subtract

`FHE.sub`

`-`

Binary

Multiply

`FHE.mul`

`*`

Binary

Divide (plaintext divisor)

`FHE.div`

Binary

Reminder (plaintext divisor)

`FHE.rem`

Binary

Negation

`FHE.neg`

`-`

Unary

Min

`FHE.min`

Binary

Max

`FHE.max`

Binary

Division (FHE.div) and remainder (FHE.rem) operations are currently supported only with plaintext divisors.

## Bitwise operations

The FHE library also supports bitwise operations, including shifts and rotations:

Name

Function name

Symbol

Type

Bitwise AND

`FHE.and`

`&`

Binary

Bitwise OR

`FHE.or`

`|`

Binary

Bitwise XOR

`FHE.xor`

`^`

Binary

Bitwise NOT

`FHE.not`

`~`

Unary

Shift Right

`FHE.shr`

Binary

Shift Left

`FHE.shl`

Binary

Rotate Right

`FHE.rotr`

Binary

Rotate Left

`FHE.rotl`

Binary

The shift operators `FHE.shr` and `FHE.shl` can take any encrypted type `euintX` as a first operand and either a `uint8`or a `euint8` as a second operand, however the second operand will always be computed modulo the number of bits of the first operand. For example, `FHE.shr(euint64 x, 70)` is equivalent to `FHE.shr(euint64 x, 6)` because `70 % 64 = 6`. This differs from the classical shift operators in Solidity, where there is no intermediate modulo operation, so for instance any `uint64` shifted right via `>>` would give a null result.

## Comparison operations

Encrypted integers can be compared using the following functions:

Name

Function name

Symbol

Type

Equal

`FHE.eq`

Binary

Not equal

`FHE.ne`

Binary

Greater than or equal

`FHE.ge`

Binary

Greater than

`FHE.gt`

Binary

Less than or equal

`FHE.le`

Binary

Less than

`FHE.lt`

Binary

## Ternary operation

The `FHE.select` function is a ternary operation that selects one of two encrypted values based on an encrypted condition:

Name

Function name

Symbol

Type

Select

`FHE.select`

Ternary

## Random operations

You can generate cryptographically secure random numbers fully on-chain:

**Name**

**Function Name**

**Symbol**

**Type**

Random Unsigned Integer

`FHE.randEuintX()`

Random

For more details, refer to the [Random Encrypted Numbers](/protocol/solidity-guides/smart-contract/operations/random) document.

## Best Practices

Here are some best practices to follow when using encrypted operations in your smart contracts:

## Use the appropriate encrypted type size

Choose the smallest encrypted type that can accommodate your data to optimize gas costs. For example, use `euint8` for small numbers (0-255) rather than `euint256`.

❌ Avoid using oversized types:

✅ Instead, use the smallest appropriate type:

## Use scalar operands when possible to save gas

Some FHE operators exist in two versions: one where all operands are ciphertexts handles, and another where one of the operands is an unencrypted scalar. Whenever possible, use the scalar operand version, as this will save a lot of gas.

❌ For example, this snippet cost way more in gas:

✅ Than this one:

Despite both leading to the same encrypted result!

## Beware of overflows of FHE arithmetic operators

FHE arithmetic operators can overflow. Do not forget to take into account such a possibility when implementing FHEVM smart contracts.

❌ For example, if you wanted to create a mint function for an encrypted ERC20 token with an encrypted `totalSupply` state variable, this code is vulnerable to overflows:

✅ But you can fix this issue by using `FHE.select` to cancel the mint in case of an overflow:

Notice that we did not check separately the overflow on `balances[msg.sender]` but only on `totalSupply` variable, because `totalSupply` is the sum of the balances of all the users, so `balances[msg.sender]` could never overflow if `totalSupply` did not.


Last updated 2 months ago

---


# Encrypted inputs

Source: https://docs.zama.org/protocol/solidity-guides/smart-contract/inputs

This document introduces the concept of encrypted inputs in the FHEVM, explaining their role, structure, validation process, and how developers can integrate them into smart contracts and applications.

Encrypted inputs are a core feature of FHEVM, enabling users to push encrypted data onto the blockchain while ensuring data confidentiality and integrity.

## What are encrypted inputs?

Encrypted inputs are data values submitted by users in ciphertext form. These inputs allow sensitive information to remain confidential while still being processed by smart contracts. They are accompanied by **Zero-Knowledge Proofs of Knowledge (ZKPoKs)** to ensure the validity of the encrypted data without revealing the plaintext.

## Key characteristics of encrypted inputs:

1. **Confidentiality**: Data is encrypted using the public FHE key, ensuring that only authorized parties can decrypt or process the values.
2. **Validation via ZKPoKs**: Each encrypted input is accompanied by a proof verifying that the user knows the plaintext value of the ciphertext, preventing replay attacks or misuse.
3. **Efficient packing**: All inputs for a transaction are packed into a single ciphertext in a user-defined order, optimizing the size and generation of the zero-knowledge proof.

## Parameters in encrypted functions

When a function in a smart contract is called, it may accept two types of parameters for encrypted inputs:

1. `externalEbool`**,** `externalEaddress`**,**`externalEuintXX`: Refers to the index of the encrypted parameter within the proof, representing a specific encrypted input handle.
2. `bytes`: Contains the ciphertext and the associated zero-knowledge proof used for validation.

Here’s an example of a Solidity function accepting multiple encrypted parameters:

Copy

```
function exampleFunction(
  externalEbool param1,
  externalEuint64 param2,
  externalEuint8 param3,
  bytes calldata inputProof
) public {
  // Function logic here
}
```

In this example, `param1`, `param2`, and `param3` are encrypted inputs for `ebool`, `euint64`, and `euint8` while `inputProof` contains the corresponding ZKPoK to validate their authenticity.

## Input Generation using Hardhat

In the below example, we use Alice's address to create the encrypted inputs and submits the transaction.

## Input Order

Developers are free to design the function parameters in any order. There is no required correspondence between the order in which encrypted inputs are constructed in TypeScript and the order of arguments in the Solidity function.

## Validating encrypted inputs

Smart contracts process encrypted inputs by verifying them against the associated zero-knowledge proof. This is done using the `FHE.asEuintXX`, `FHE.asEbool`, or `FHE.asEaddress` functions, which validate the input and convert it into the appropriate encrypted type.

## Example validation

This example demonstrates a function that performs multiple encrypted operations, such as updating a user's encrypted balance and toggling an encrypted boolean flag:

## Example validation in the `ConfidentialERC20.sol` smart contract

Here’s an example of a smart contract function that verifies an encrypted input before proceeding:

## How validation works

1. **Input verification**:
   The `FHE.fromExternal` function ensures that the input is a valid ciphertext with a corresponding ZKPoK.
2. **Type conversion**:
   The function transforms `externalEbool`, `externalEaddress`, `externalEuintXX` into the appropriate encrypted type (`ebool`, `eaddress`, `euintXX`) for further operations within the contract.

## Best Practices

* **Input packing**: Minimize the size and complexity of zero-knowledge proofs by packing all encrypted inputs into a single ciphertext.
* **Frontend encryption**: Always encrypt inputs using the FHE public key on the client side to ensure data confidentiality.
* **Proof management**: Ensure that the correct zero-knowledge proof is associated with each encrypted input to avoid validation errors.

Encrypted inputs and their validation form the backbone of secure and private interactions in the FHEVM. By leveraging these tools, developers can create robust, privacy-preserving smart contracts without compromising functionality or scalability.


Last updated 2 months ago

---


# Access Control List

Source: https://docs.zama.org/protocol/solidity-guides/smart-contract/acl

This document describes the Access Control List (ACL) system in FHEVM, a core feature that governs access to encrypted data. The ACL ensures that only authorized accounts or contracts can interact with specific ciphertexts, preserving confidentiality while enabling composable smart contracts. This overview provides a high-level understanding of what the ACL is, why it's essential, and how it works.

## What is the ACL?

The ACL is a permission management system designed to control who can access, compute on, or decrypt encrypted values in fhevm. By defining and enforcing these permissions, the ACL ensures that encrypted data remains secure while still being usable within authorized contexts.

## Why is the ACL important?

Encrypted data in FHEVM is entirely confidential, meaning that without proper access control, even the contract holding the ciphertext cannot interact with it. The ACL enables:

* **Granular permissions**: Define specific access rules for individual accounts or contracts.
* **Secure computations**: Ensure that only authorized entities can manipulate or decrypt encrypted data.
* **Gas efficiency**: Optimize permissions using transient access for temporary needs, reducing storage and gas costs.

## How does the ACL work?

## Types of access

* **Permanent allowance**:

  + Configured using `FHE.allow(ciphertext, address)`.
  + Grants long-term access to the ciphertext for a specific address.
  + Stored in a dedicated contract for persistent storage.
* **Transient allowance**:

  + Configured using `FHE.allowTransient(ciphertext, address)`.
  + Grants access to the ciphertext only for the duration of the current transaction.
  + Stored in transient storage, reducing gas costs.
  + Ideal for temporary operations like passing ciphertexts to external functions.
* **Permanent public allowance**:

  + Configured using `FHE.makePubliclyDecryptable(ciphertext)`.
  + Grants long-term access to the ciphertext for any user.
  + Stored in a dedicated contract for persistent storage.

**Syntactic sugar**:

* `FHE.allowThis(ciphertext)` is shorthand for `FHE.allow(ciphertext, address(this))`. It authorizes the current contract to reuse a ciphertext handle in future transactions.

## Transient vs. permanent allowance

Allowance type

Purpose

Storage type

Use case

**Transient**

Temporary access during a transaction.

[Transient storage](https://eips.ethereum.org/EIPS/eip-1153) (EIP-1153)

Calling external functions or computations with ciphertexts. Use when wanting to save on gas costs.

**Permanent**

Long-term access across multiple transactions.

Dedicated contract storage

Persistent ciphertexts for contracts or users requiring ongoing access.

## Granting and verifying access

## Granting access

Developers can use functions like `allow`, `allowThis`, and `allowTransient` to grant permissions:

* `allow`: Grants permanent access to an address.
* `allowThis`: Grants the current contract access to manipulate the ciphertext.
* `allowTransient`: Grants temporary access to an address for the current transaction.
* `makePubliclyDecryptable`: Grants permanent, global permission for any entity to decrypt the cleartext value associated with the given ciphertext (handle) off-chain.

## Verifying access

To check if an entity has permission to access a ciphertext, use functions like `isAllowed` or `isSenderAllowed`:

* `isAllowed`: Verifies if a specific address has permission.
* `isSenderAllowed`: Simplifies checks for the current transaction sender.
* `isPubliclyDecryptable`: Verifies whether any entity is permitted to retrieve the ciphertext's cleartext value off-chain.
* `checkSignatures`: Verifies the authenticity of a cleartext value by checking cryptographic signatures. This ensures that the value submitted back to the chain originated from a legitimate public decryption operation on the associated ciphertext handle.

## Practical uses of the ACL

* **Confidential parameters**: Pass encrypted values securely between contracts, ensuring only authorized entities can access them.
* **Secure state management**: Store encrypted state variables while controlling who can modify or read them.
* **Privacy-preserving computations**: Enable computations on encrypted data with confidence that permissions are enforced.
* **Publicly Verifiable Result Reveal**: Enable the public reveal of a confidential operation's final result. For example, enabling the public to verify the final price in a sealed-bid confidential auction.

---

For a detailed explanation of the ACL's functionality, including code examples and advanced configurations, see [ACL examples](/protocol/solidity-guides/smart-contract/acl/acl_examples).


Last updated 1 month ago

---


# Logics

Source: https://docs.zama.org/protocol/solidity-guides/smart-contract/logics

[Branching](/protocol/solidity-guides/smart-contract/logics/conditions)

---


# Decryption

Source: https://docs.zama.org/protocol/solidity-guides/smart-contract/oracle

## Public Decryption

This section explains how to handle public decryption in FHEVM. Public decryption allows plaintext data to be accessed when required for contract logic or user presentation, ensuring confidentiality is maintained throughout the process.

Public decryption is essential in two primary cases:

1. **Smart contract logic**: A contract requires plaintext values for computations or decision-making.
2. **User interaction**: Plaintext data needs to be revealed to all users, such as revealing the decision of the vote.

## Overview

Public decryption of a confidential on-chain result is designed as an asynchronous three-steps process that splits the work between the blockchain (on-chain) and off-chain execution environments.

**Step 1: On-Chain Setup - Enabling Permanent Public Access**

This step is executed by the smart contract using the FHE Solidity library to signal that a specific confidential result is ready to be revealed.

* **FHE Solidity Library Function:** `FHE.makePubliclyDecryptable`
* **Action:** The contract sets the ciphertext handle's status as publicly decryptable, **globally and permanently** authorizing any entity to request its off-chain cleartext value.
* **Result:** The ciphertext is now accessible to any entity, which can request its decryption from the Zama off-chain Relayer.

**Step 2: Off-chain Decryption - Decryption and Proof Generation**

This step can be executed by any off-chain client using the Relayer SDK.

* **Relayer SDK Function:** `FhevmInstance.publicDecrypt`
* **Action:** The off-chain client submits the ciphertext handle to the Zama Relayer's Key Management System (KMS).
* **Result:** The Zama Relayer returns three items:

  1. The cleartext (the decrypted value).
  2. The ABI-encoding of that cleartext.
  3. A Decryption Proof (a byte array of signatures and metadata) that serves as a cryptographic guarantee that the cleartext is the authentic, unmodified result of the decryption performed by the KMS.

**Step 3: On-Chain Verification - Submit and Guarantee Authenticity**

This final step is executed on-chain by the contrat using the FHE Solidity library with the proof generated off-chain to ensure the cleartext submitted to the contract is trustworthy.

* **FHE Solidity Library Function:** `FHE.checkSignatures`
* **Action:** The caller submits the cleartext and decryption proof back to a contract function. The contract calls `FHE.checkSignatures`, which reverts the transaction if the proof is invalid or does not match the cleartext/ciphertext pair.
* **Result:** The receiving contract gains a cryptographic guarantee that the submitted cleartext is the authentic decrypted value of the original ciphertext. The contract can then securely execute its business logic (e.g., reveal a vote, transfer funds, update state).

## Tutorial

This tutorial provides a deep dive into the three-step asynchronous public decryption process required to finalize a confidential on-chain computation by publicly revealing its result.

The Solidity contract provided below, `FooBarContract`, is used to model this entire workflow. The contract's main function `runFooBarConfidentialLogic` simulates the execution of a complex confidential computation (e.g., calculating a winner or a final price) that results in 2 encrypted final values (ciphertexts) `_encryptedFoo` and `_encryptedBar`.

Then, in order to finalize the workflow, the `FooBarContract` needs the decrypted clear values of both `_encryptedFoo` and `_encryptedBar` to decide whether to trigger some finalization logic (e.g. reveal a vote, transfer funds). The `FooBarContract`'s function `_runFooBarClearBusinessLogicFinalization` simulates this step. Since the FHEVM prevents direct on-chain decryption, the process must shift to an off-chain decryption phase, which presents a challenge: ***How can the*** `FooBarContract` ***trust that the cleartext submitted back to the chain is the authentic, unmodified result of the decryption of both*** `_encryptedFoo` ***and*** `_encryptedBar`***?***

This is where the off-chain `publicDecrypt` function and the on-chain `checkSignatures` function come into play.

## The Solidity Contract

1

## Run On-Chain Confidential Logic

We first execute the on-chain confidential logic using a TypeScript client. This simulates the initial phase of the confidential computation.

2

## Run On-Chain Request Clear Values

With the confidential logic complete, the next step is to execute the on-chain function that requests and enables public decryption of the computed encrypted values `_encryptedFoo` and `_encryptedBar`. In a production scenario, we might use a Solidity event to notify the off-chain client that the necessary encrypted values are ready for off-chain public decryption.

3

## Run Off-Chain Public Decryption

Now that the ciphertexts are marked as publicly decryptable, we call the off-chain function `publicDecrypt` using the `relayer-sdk`. This fetches the clear values along with the Zama KMS decryption proof required for the final on-chain verification.

**Crucial Ordering Constraint:** The decryption proof is cryptographically bound to the specific order of handles passed in the input array. The proof computed for `[efoo, ebar]` is different from the proof computed for `[ebar, efoo]`.

4

## Run On-Chain

On the client side, we have computed all the clear values and, crucially, obtained the associated decryption proof. We can now securely move on to the final step: sending this data on-chain to trigger verification and final business logic simulated in the `_runFooBarClearBusinessLogicFinalization` contract function. If verification succeeds, the contract securely executes the `_runFooBarClearBusinessLogicFinalization` (e.g., transfers funds, publishes the vote result, etc.), completing the full confidential workflow.

## Public Decryption On-Chain & Off-Chain API

## On-chain `FHE.makePubliclyDecryptable` function

The contract sets the ciphertext handle's status as publicly decryptable, globally and permanently authorizing any entity to request its off-chain cleartext value. Note the calling contract must have ACL permission to access the handle in the first place.

**Function arguments**

**Function return**

This function has no return value

## Off-chain relayer-sdk `publicDecrypt` function

The relayer-sdk `publicDecrypt` function is defined as follow:

**Function arguments**

Argument

Description

Constraints

`handles`

The list of ciphertext handles (represented as bytes32 values) to decrypt.

These handles must correspond to ciphertexts that have been marked as publicly decryptable on-chain.

**Function return type** `PublicDecryptResults`

The function returns an object containing the three essential components required for the final on-chain verification in Step 3 of the public decryption workflow:

Property

Type

Description

On-Chain usage

`clearValues`

`Record<`0x${string}`, bigint | boolean |` 0x${string}`>`

An object mapping each input ciphertext handle to its raw decrypted cleartext value.

N/A

`abiEncodedClearValues`

`0x${string}`

The ABI-encoded byte string of all decrypted cleartext values, preserving the exact order of the input handles list.

`abiEncodedCleartexts` argument when calling the on-chain `FHE.checkSignatures`

`decryptionProof`

`0x${string}`

A byte array containing the KMS cryptographic signatures and necessary metadata that proves the decryption was legitimately performed.

`decryptionProof` argument when calling the on-chain `FHE.checkSignatures`

## On-chain `FHE.checkSignatures` function

**Function arguments**

Argument

Description

Constraint

`handlesList`

The list of ciphertext handles (represented as bytes32 values) whose decryption is being verified.

Must contain the exact same number of elements as the cleartext values in abiEncodedCleartexts.

`abiEncodedCleartexts`

The ABI encoding of the decrypted cleartext values associated with the handles. (Use abi.encode to prepare this argument.)

Order is critical: The i-th value in this encoding must be the cleartext that corresponds to the i-th handle in handlesList. Types must match.

`decryptionProof`

A byte array containing the KMS cryptographic signatures and necessary metadata that prove the off-chain decryption was performed by the authorized Zama Key Management System.

This proof is generated by the Zama KMS and is obtained via the `relayer-sdk.publicDecrypt` function.

**Function return**

This function has no return value and simply reverts if the proof verification failed.

Notice that the callback should always verify the signatures and implement a replay protection mechanism (see below).


Last updated 1 month ago

---


# Hardhat plugin

Source: https://docs.zama.org/protocol/solidity-guides/development-guide/hardhat

This section will guide you through writing and testing FHEVM smart contracts in Solidity using [Hardhat](https://hardhat.org).

## The FHEVM Hardhat Plugin

To write FHEVM smart contracts using Hardhat, you need to install the [FHEVM Hardhat Plugin](https://www.npmjs.com/package/@fhevm/hardhat-plugin) in your Hardhat project.

This plugin enables you to develop, test, and interact with FHEVM contracts right out of the box.

It extends Hardhat’s functionality with a complete FHEVM API that allows you:

* Encrypt data
* Decrypt data
* Run tests using various FHEVM execution modes
* Write FHEVM-enabled Hardhat Tasks

## Where to go next

🟨 Go to [**Setup Hardhat**](https://docs.zama.ai/protocol/solidity-guides/getting-started/setup) to initialize your FHEVM Hardhat project.

🟨 Go to [**Write FHEVM Tests in Hardhat**](/protocol/solidity-guides/development-guide/hardhat/write_test) for details on writing tests of FHEVM smart contracts using Hardhat.

🟨 Go to [**Run FHEVM Tests in Hardhat**](/protocol/solidity-guides/development-guide/hardhat/run_test) to learn how to execute those tests in different FHEVM environments.

🟨 Go to [**Write FHEVM Hardhat Task**](/protocol/solidity-guides/development-guide/hardhat/write_task) to learn how to write your own custom FHEVM Hardhat task.


Last updated 2 months ago

---


# Foundry

Source: https://docs.zama.org/protocol/solidity-guides/development-guide/foundry

This guide explains how to use Foundry with FHEVM for developing smart contracts.

While a Foundry template is currently in development, we strongly recommend using the [Hardhat template](/protocol/solidity-guides/getting-started/setup)) for now, as it provides a fully tested and supported development environment for FHEVM smart contracts.

However, you could still use Foundry with the mocked version of the FHEVM, but please be aware that this approach is **NOT** recommended, since the mocked version is not fully equivalent to the real FHEVM node's implementation (see warning in hardhat). In order to do this, you will need to rename your `FHE.sol` imports from `@fhevm/solidity/lib/FHE.sol` to `fhevm/mocks/FHE.sol` in your solidity source files.


Last updated 2 months ago

---


# HCU

Source: https://docs.zama.org/protocol/solidity-guides/development-guide/hcu

This guide explains how to use Fully Homomorphic Encryption (FHE) operations in your smart contracts on FHEVM. Understanding HCU is critical for designing efficient confidential smart contracts.

## Overview

FHE operations in FHEVM are computationally intensive compared to standard Ethereum operations, as they require complex mathematical computations to maintain privacy and security. To manage computational load and prevent potential denial-of-service attacks, FHEVM implements a metering system called **Homomorphic Complexity Units ("HCU")**.

To represent this complexity, we introduced the **Homomorphic Complexity Unit ("HCU")**. In Solidity, each FHE operation consumes a set amount of HCU based on the operational computational complexity for hardware computation. Since FHE transactions are symbolic, this helps preventing resource exhaustion outside of the blockchain.

To do so, there is a contract named `HCULimit`, which monitors HCU consumption for each transaction and enforces two key limits:

* **Sequential homomorphic operations depth limit per transaction**: Controls HCU usage for operations that must be processed in order.
* **Global homomorphic operations complexity per transaction**: Controls HCU usage for operations that can be processed in parallel.

If either limit is exceeded, the transaction will revert.

## HCU limit

The current devnet has an HCU limit of **20,000,000** per transaction and an HCU depth limit of **5,000,000** per transaction. If either HCU limit is exceeded, the transaction will revert.

To resolve this, you must do one of the following:

* Refactor your code to reduce the number of FHE operations in your transaction.
* Split your FHE operations across multiple independent transactions.

## HCU costs for common operations

## Boolean operations (`ebool`)

Function name

HCU (scalar)

HCU (non-scalar)

`and`

22,000

25,000

`or`

22,000

24,000

`xor`

2,000

22,000

`not`

-

2

`select`

-

55,000

`randEbool`

-

19,000

---

## Unsigned integer operations

HCU increase with the bit-width of the encrypted integer type. Below are the detailed costs for various operations on encrypted types.

## **8-bit Encrypted integers (**`euint8`**)**

Function name

HCU (scalar)

HCU (non-scalar)

`add`

84,000

88,000

`sub`

84,000

91,000

`mul`

122,000

150,000

`div`

210,000

-

`rem`

440,000

-

`and`

31,000

31,000

`or`

30,000

30,000

`xor`

31,000

31,000

`shr`

32,000

91,000

`shl`

32,000

92,000

`rotr`

31,000

93,000

`rotl`

31,000

91,000

`eq`

55,000

55,000

`ne`

55,000

55,000

`ge`

52,000

63,000

`gt`

52,000

59,000

`le`

58,000

58,000

`lt`

52,000

59,000

`min`

84,000

119,000

`max`

89,000

121,000

`neg`

-

79,000

`not`

-

9

`select`

-

55,000

`randEuint8`

-

23,000

## **16-bit Encrypted integers (**`euint16`**)**

Function name

HCU (scalar)

HCU (non-scalar)

`add`

93,000

93,000

`sub`

93,000

93,000

`mul`

193,000

222,000

`div`

302,000

-

`rem`

580,000

-

`and`

31,000

31,000

`or`

30,000

31,000

`xor`

31,000

31,000

`shr`

32,000

123,000

`shl`

32,000

125,000

`rotr`

31,000

125,000

`rotl`

31,000

125,000

`eq`

55,000

83,000

`ne`

55,000

83,000

`ge`

55,000

84,000

`gt`

55,000

84,000

`le`

58,000

83,000

`lt`

58,000

84,000

`min`

88,000

146,000

`max`

89,000

145,000

`neg`

-

93,000

`not`

-

16

`select`

-

55,000

`randEuint16`

-

23,000

## **32-bit Encrypted Integers (**`euint32`**)**

Function name

HCU (scalar)

HCU (non-scalar)

`add`

95,000

125,000

`sub`

95,000

125,000

`mul`

265,000

328,000

`div`

438,000

-

`rem`

792,000

-

`and`

32,000

32,000

`or`

32,000

32,000

`xor`

32,000

32,000

`shr`

32,000

163,000

`shl`

32,000

162,000

`rotr`

32,000

160,000

`rotl`

32,000

163,000

`eq`

82,000

86,000

`ne`

83,000

85,000

`ge`

84,000

118,000

`gt`

84,000

118,000

`le`

84,000

117,000

`lt`

83,000

117,000

`min`

117,000

182,000

`max`

117,000

180,000

`neg`

-

131,000

`not`

-

32

`select`

-

55,000

`randEuint32`

-

24,000

## **64-bit Encrypted integers (**`euint64`**)**

Function name

HCU (scalar)

HCU (non-scalar)

`add`

133,000

162,000

`sub`

133,000

162,000

`mul`

365,000

596,000

`div`

715,000

-

`rem`

1,153,000

-

`and`

34,000

34,000

`or`

34,000

34,000

`xor`

34,000

34,000

`shr`

34,000

209,000

`shl`

34,000

208,000

`rotr`

34,000

209,000

`rotl`

34,000

209,000

`eq`

83,000

120,000

`ne`

84,000

118,000

`ge`

116,000

152,000

`gt`

117,000

152,000

`le`

119,000

149,000

`lt`

118,000

146,000

`min`

150,000

219,000

`max`

149,000

218,000

`neg`

-

131,000

`not`

-

63

`select`

-

55,000

`randEuint64`

-

24,000

## **128-bit Encrypted integers (**`euint128`**)**

Function name

HCU (scalar)

HCU (non-scalar)

`add`

172,000

259,000

`sub`

172,000

260,000

`mul`

696,000

1,686,000

`div`

1,225,000

-

`rem`

1,943,000

-

`and`

37,000

37,000

`or`

37,000

37,000

`xor`

37,000

37,000

`shr`

37,000

272,000

`shl`

37,000

272,000

`rotr`

37,000

283,000

`rotl`

37,000

278,000

`eq`

117,000

122,000

`ne`

117,000

122,000

`ge`

149,000

210,000

`gt`

150,000

218,000

`le`

150,000

218,000

`lt`

149,000

215,000

`min`

186,000

289,000

`max`

180,000

290,000

`neg`

-

168,000

`not`

-

130

`select`

-

57,000

`randEuint128`

-

25,000

## **256-bit Encrypted integers (**`euint256`**)**

Function name

HCU (scalar)

HCU (non-scalar)

`and`

38,000

38,000

`or`

38,000

38,000

`xor`

39,000

39,000

`shr`

38,000

369,000

`shl`

39,000

378,000

`rotr`

40,000

375,000

`rotl`

38,000

378,000

`eq`

118,000

152,000

`ne`

117,000

150,000

`neg`

-

269,000

`not`

-

130

`select`

-

108,000

`randEuint256`

-

30,000

## **Encrypted addresses (**`euint160`**)**

When using `eaddress` (internally represented as `euint160`), the HCU costs for equality and inequality checks and select are as follows:

Function name

HCU (scalar)

HCU (non-scalar)

`eq`

115,000

125,000

`ne`

115,000

124,000

`select`

-

83,000

## Additional Operations

Function name

HCU

`cast`

32

`trivialEncrypt`

32

`randBounded`

23,000-30,000


Last updated 2 months ago

---


# Migrate to v0.9

Source: https://docs.zama.org/protocol/solidity-guides/development-guide/migration

FHEVM v0.9 introduces major architectural changes, including:

* Removal of the Zama Oracle
* Introduction of a self-relaying public decryption workflow
* Unified `ZamaEthereumConfig` replacing `SepoliaConfig`

This guide explains what changed and how to migrate your project smoothly.

## What Changed in FHEVM v0.9?

Before diving into migration steps, it’s important to understand the main breaking change: public decryption is no longer handled by a Zama Oracle, but by your dApp’s off-chain logic.

## FHEVM v0.8 Oracle-Based Decryption

In FHEVM v0.8, the decryption process relies on a trusted **Oracle** to relay the decryption request and proof between the dApp and the Zama Key Management System (KMS). This approach abstracts the complexity but introduces an external dependency.

**Decryption Steps:**

Step

Component

Action

**1.**

**dApp (Solidity)**

Calls `FHE.requestDecryption()` to signal a need for clear data.

**2.**

**Oracle**

Listens for the on-chain decryption request event.

**3.**

**Oracle (Off-chain)**

Performs the `publicDecryption` with the Zama KMS, retrieving the **clear values** and the **decryption proof**.

**4.**

**Oracle**

Calls the user-specified dApp **callback Solidity function** with the clear values and the associated proof.

**5.**

**dApp (Solidity Callback)**

Calls `FHE.verifySignatures()` to verify the authenticity of the clear values using the provided proof.

> **Key takeaway for v0.8:** The Oracle is the trusted intermediary responsible for performing the off-chain decryption and submitting the result back to the dApp contract.

## FHEVM v0.9 Self-Relaying Decryption & dApp Responsibility

The FHEVM v0.9 architecture shifts to a **self-relaying model**, empowering the dApp client (the user) to execute the off-chain decryption and re-submission. This decentralizes the process and removes the dependency on a general-purpose Oracle.

**Example Scenario: Checking a Player's Encrypted Score**

Consider a **Game contract** where Alice's final score is stored encrypted on-chain. Alice needs to prove her clear score to claim a reward.

Step

Component

Action

**1.**

**Game Contract (Solidity)**

An on-chain function is called to make Alice's encrypted score **publicly decryptable**.

**2.**

**Alice (Client/Off-chain)**

Alice fetches the publicly decryptable encrypted score from the Game contract.

**3.**

**Alice (Client/Off-chain)**

Alice or any third-party service uses the `@zama-fhe/relayer-sdk` to call the off-chain `publicDecrypt` function. This returns the clear score value and a **proof of decryption**.

**4.**

**Alice (Client/On-chain)**

Alice calls a function on the **Game contract** with the decrypted clear score and the proof.

**5.**

**Game Contract (Solidity)**

The contract calls `FHE.verifySignatures()` to **verify the score's validity** using the provided proof.

**6.**

**Game Contract (Solidity)**

If the score is valid, the contract executes the game logic (e.g., distributing Alice's prize).

> **Key takeaway for FHEVM v0.9:** Decryption is a **user-driven, off-chain process**. The dApp client is responsible for off-chain decryption, fetching the proof, and relaying the result back on-chain for verification.

**Why this matters:** If your dApp previously relied on the Oracle, you must rewrite your decryption flow. The migration steps below guide you through this change.

## Migration Checklist

Here is a brief, ordered list of the steps required to successfully migrate your project to FHEVM v0.9:

1. **Update Dependencies:** Upgrade all key Zama FHE packages to their **FHEVM v0.9 versions**.
2. **Update Solidity Config:** Replace the removed `SepoliaConfig` with the unified `ZamaEthereumConfig`.
3. **Update Solidity Code:** Remove all calls to the discontinued Oracle-based FHE library functions.
4. **Re-compile & Re-deploy:** Due to new FHEVM addresses, all affected contracts must be re-compiled and re-deployed on Sepolia.
5. **Rewrite Public Decryption Logic:** Eliminate reliance on the discontinued Zama Oracle and implement the **self-relaying** workflow using the `@zama-fhe/relayer-sdk` and `FHE.verifySignatures()`.

Follow these steps for a smooth transition to FHEVM v0.9:

## Step 1: Update Core Dependencies

Ensure your project uses the latest versions of the FHEVM development tools.

Dependency

Minimum Required Version

Notes

`@fhevm/solidity`

`v0.9.1`

Contains the updated FHE library contracts.

`@zama-fhe/relayer-sdk`

`v0.3.0-5`

**Crucial for v0.9:** Enables the new self-relaying decryption model.

`@fhevm/hardhat-plugin`

`v0.3.0-1`

Latest tooling support for development and deployment.

## Step 2: Update Network Configuration in Solidity

The Solidity contracts now use a unified configuration contract defined in `@fhevm/solidity/config/ZamaConfig.sol`.

* **⚠️ Removal:** The `SepoliaConfig` contract is now **removed**.
* **✅ New Standard:** Update your imports and usages to use the new standard `ZamaEthereumConfig` contract. This change simplifies future cross-chain compatibility.

The new `ZamaEthereumConfig` abstract contract now dynamically resolves the FHEVM host addresses according to the `block.chainid`.

Replace:

With:

You can read more about [Configuration on the dedicated page](/protocol/solidity-guides/smart-contract/configure).

## Step 3: Update Solidity Code

The Zama public decryption Oracle is discontinued. The following functions are no more available in the FHE Solidity library:

* `FHE.loadRequestedHandles`
* `FHE.requestDecryptionWithoutSavingHandles`
* `FHE.requestDecryption`

## Step 4: Re-compile and Re-deploy Smart Contracts

Due to fundamental changes in the FHEVM implementation and underlying infrastructure:

* **New FHEVM Addresses:** The contract addresses for core FHE components have changed.
* **Action:** You **must** re-compile your entire Solidity codebase and re-deploy all affected contracts to the **Sepolia** network.

## Step 5: Adjust Public Decryption Logic (Crucial Architectural Change)

The most significant change is the discontinuation of the Zama Oracle. This requires substantial adjustments to how your dApp handles decryption on-chain.

Aspect

FHEVM v0.8 (Old Logic)

FHEVM v0.9 (New Logic)

**Decryption Handler**

**Zama Oracle** actively listens for requests and submits the result.

**dApp Client/User** performs the off-chain decryption (self-relaying).

**Solidity Function**

Used `FHE.requestDecryption()`.

You will now create custom functions that accept the decrypted value and the proof.

**Client-Side Tool**

N/A

**Use** `@zama-fhe/relayer-sdk` to perform the `publicDecrypt` and obtain the proof.

> **Action:** Thoroughly review your Solidity code, dApp logic, and backend services. Any code relying on the external Oracle must be rewritten to implement the self-relaying workflow using the `@zama-fhe/relayer-sdk`.

## FHEVM v0.9 Code Examples: Public Decryption Logic

The following code examples illustrate the **new public decryption logic** introduced in v0.9. This new workflow uses the combination of:

* **On-chain public decyption permission** via `FHE.makePubliclyDecryptable`
* **Off-chain decryption** via `publicDecrypt` using the `@zama-fhe/relayer-sdk` or the FHEVM Hardhat Plugin
* **On-chain signature verification** via `FHE.checkSignatures`

## Code Examples

* [HeadsOrTails](https://github.com/zama-ai/fhevm/blob/release/0.9.x/docs/examples/heads-or-tails.md): Demonstrates the complete public decryption workflow where a cipher text is first marked as decryptable on-chain via `FHE.makePubliclyDecryptable`, and its cleartext value is subsequently verified on-chain using `FHE.checkSignatures` after being fetched off-chain via `publicDecrypt`.
* [HighestDieRoll](https://github.com/zama-ai/fhevm/blob/release/0.9.x/docs/examples/highest-die-roll.md): Extends the public decryption workflow to a multi-input scenario, demonstrating how the on-chain `FHE.checkSignatures` function ensures the authenticity of multiple cleartext values derived from multiple encrypted on-chain cypher texts.


Last updated 1 month ago

---


# How to Transform Your Smart Contract into a FHEVM Smart Contract?

Source: https://docs.zama.org/protocol/solidity-guides/development-guide/transform_smart_contract_with_fhevm

This short guide will walk you through converting a standard Solidity contract into one that leverages Fully Homomorphic Encryption (FHE) using FHEVM. This approach lets you develop your contract logic as usual, then adapt it to support encrypted computation for privacy.

For this guide, we will focus on a voting contract example.

---

## 1. Start with a Standard Solidity Contract

Begin by writing your voting contract in Solidity as you normally would. Focus on implementing the core logic and functionality.

Copy

```
// Standard Solidity voting contract example
pragma solidity ^0.8.0;

contract SimpleVoting {
    mapping(address => bool) public hasVoted;
    uint64 public yesVotes;
    uint64 public noVotes;
    uint256 public voteDeadline;

    function vote(bool support) public {
        require(block.timestamp <= voteDeadline, "Too late to vote");
        require(!hasVoted[msg.sender], "Already voted");
        hasVoted[msg.sender] = true;

        if (support) {
            yesVotes += 1;
        } else {
            noVotes += 1;
        }
    }

    function getResults() public view returns (uint64, uint64) {
        return (yesVotes, noVotes);
    }
}
```

---

## 2. Identify Sensitive Data and Operations

Review your contract and determine which variables, functions, or computations require privacy. In this example, the vote counts (`yesVotes`, `noVotes`) and individual votes should be encrypted.

---

## 3. Integrate FHEVM and update your business logic accordingly.

Replace standard data types and operations with their FHEVM equivalents for the identified sensitive parts. Use encrypted types and FHEVM library functions to perform computations on encrypted data.

Adjust your contract’s code to accept and return encrypted data where necessary. This may involve changing function parameters and return types to work with ciphertexts instead of plaintext values, as shown above.

* The `vote` function now has two parameters: `support` and `inputProof`.
* The `getResults` can only be called after the decryption occurred. Otherwise, the decrypted results are not visible to anyone.

However, it is far from being the main change. As this example illustrates, working with FHEVM often requires re-architecting the original logic to support privacy.

In the updated code, the logic becomes async; results are hidden until a request (to the oracle) explicitely has to be made to decrypt publically the vote results.

## Conclusion

As this short guide showed, integrating with FHEVM not only requires integration with the FHEVM stack, it also requires refactoring your business logic to support mechanism to swift between encrypted and non-encrypted components of the logic.

[PreviousMigrate to v0.9](/protocol/solidity-guides/development-guide/migration)

Last updated 1 month ago

---
