# Table of Contents

- [Welcome](#welcome)
- [Developer](#developer)
  - [Examples](#examples)
- [Relayer SDK Guides](#relayer-sdk-guides)
- [Solidity Guides](#solidity-guides)
- [Zama Protocol Litepaper](#zama-protocol-litepaper)
**Developer**
  - [Contributing](#contributing)
**Development Guide**
  - [Decryption](#decryption)
      - [User decrypt multiple values](#user-decrypt-multiple-values)
      - [User decrypt single value](#user-decrypt-single-value)
      - [Public Decrypt single value](#public-decrypt-single-value)
      - [Public Decrypt multiple values](#public-decrypt-multiple-values)
  - [FHE Operations](#fhe-operations)
      - [Add](#add)
      - [If then else](#if-then-else)
  - [ERC7984 Standard](#erc7984-standard)
      - [ERC7984 Tutorial](#erc7984-tutorial)
      - [ERC7984 to ERC20 Wrapper](#erc7984-to-erc20-wrapper)
      - [Swap ERC7984 to ERC20](#swap-erc7984-to-erc20)
      - [Swap ERC7984 to ERC7984](#swap-erc7984-to-erc7984)
  - [Library installation and overview](#library-installation-and-overview)
  - [Vesting Wallet](#vesting-wallet)
  - [Integration guide for wallets](#integration-guide-for-wallets)
**Protocol**
  - [FHE on blockchain](#fhe-on-blockchain)
    - [Coprocessor](#coprocessor)
    - [Gateway](#gateway)
    - [Host contracts](#host-contracts)
    - [KMS](#kms)
    - [FHE library](#fhe-library)
    - [Relayer & Oracle](#relayer-oracle)
  - [Roadmap](#roadmap)
  - [CLI](#cli)
    - [Web applications](#web-applications)
  - [Debugging](#debugging)
  - [Decryption](#decryption)
      - [Public decryption](#public-decryption)
      - [User decryption](#user-decryption)
    - [Initialization](#initialization)
    - [Input](#input)
**Smart Contract**
  - [Foundry](#foundry)
  - [Hardhat plugin](#hardhat-plugin)
  - [HCU](#hcu)
  - [Migrate to v0.9](#migrate-to-v0-9)
  - [How to Transform Your Smart Contract into a FHEVM Smart Contract?](#how-to-transform-your-smart-contract-into-a-fhevm-smart-contract)
  - [What is FHEVM Solidity](#what-is-fhevm-solidity)
  - [Quick start tutorial](#quick-start-tutorial)
  - [Set up Hardhat](#set-up-hardhat)
    - [Access Control List](#access-control-list)
  - [Configuration](#configuration)
  - [Encrypted inputs](#encrypted-inputs)
  - [Logics](#logics)
  - [Operations on encrypted types](#operations-on-encrypted-types)
    - [Decryption](#decryption)
    - [Supported types](#supported-types)

---


# Welcome

Source: https://docs.zama.org/protocol/

**Welcome to the Zama Confidential Blockchain Protocol Docs.**
The docs aim to guide you to build confidential dApps on top of any L1 or L2 using Fully Homomorphic Encryption (FHE).

## Where to go next

If you're completely new to FHE or the Zama Protocol, we suggest first checking out the [Litepaper](https://docs.zama.ai/protocol/zama-protocol-litepaper), which offers a thorough overview of the protocol.

Otherwise:

🟨 Go to [**Quick Start**](https://docs.zama.ai/protocol/solidity-guides/getting-started/quick-start-tutorial) to learn how to write your first confidential smart contract using FHEVM.

🟨 Go to [**Solidity Guides**](https://docs.zama.ai/protocol/solidity-guides) to explore how encrypted types, operations, ACLs, and other core features work in practice.

🟨 Go to [**Relayer SDK Guides**](https://docs.zama.ai/protocol/relayer-sdk-guides) to build a frontend that can encrypt, decrypt, and interact securely with the blockchain.

🟨 Go to [**FHE on Blockchain**](/protocol/protocol/overview) to learn the architecture in depth and understand how encrypted computation flows through both on-chain and off-chain components.

🟨 Go to [**Examples**](https://docs.zama.ai/protocol/examples) to find reference and inspiration from smart contract examples and dApp examples.

The Zama Protocol Testnet is not audited and is not intended for production use. **Do not publish any critical or sensitive data**. For production workloads, please wait for the Mainnet release.

## Help center

Ask technical questions and discuss with the community.

* [Community forum](https://community.zama.ai/c/fhevm/15)
* [Discord channel](https://discord.com/invite/zama)

Last updated 3 months ago

---


# Developer

Source: https://docs.zama.org/protocol/developer

There are two ways to contribute to FHEVM:

* [Open issues](https://github.com/zama-ai/fhevm/issues/new/choose) to report bugs and typos, or to suggest new ideas
* Request to become an official contributor by emailing [[email protected]](/cdn-cgi/l/email-protection#0d65686161624d776c606c236c64).

Becoming an approved contributor involves signing our Contributor License Agreement (CLA). Only approved contributors can send pull requests, so please make sure to get in touch before you do!

## Zama Bounty Program

Solve challenges and earn rewards:

* [bounty-program](https://github.com/zama-ai/bounty-program) - Zama's FHE Bounty Program

[PreviousRoadmap](/protocol/protocol/roadmap)

Last updated 6 months ago

---


# Examples

Source: https://docs.zama.org/protocol/examples

This example demonstrates how to build an confidential counter using FHEVM, in comparison to a simple counter.

To run this example correctly, make sure the files are placed in the following directories:

* `.sol` file → `<your-project-root-dir>/contracts/`
* `.ts` file → `<your-project-root-dir>/test/`

This ensures Hardhat can compile and test your contracts as expected.

## A simple counter

counter.sol

counter.ts

Copy

```
// SPDX-License-Identifier: BSD-3-Clause-Clear
pragma solidity ^0.8.24;

/// @title A simple counter contract
contract Counter {
  uint32 private _count;

  /// @notice Returns the current count
  function getCount() external view returns (uint32) {
    return _count;
  }

  /// @notice Increments the counter by a specific value
  function increment(uint32 value) external {
    _count += value;
  }

  /// @notice Decrements the counter by a specific value
  function decrement(uint32 value) external {
    require(_count >= value, "Counter: cannot decrement below zero");
    _count -= value;
  }
}
```

## An FHE counter

FHECounter.sol

FHECounter.ts

[NextFHE Operations](/protocol/examples/basic/fhe-operations)

Last updated 1 month ago

---


# Relayer SDK Guides

Source: https://docs.zama.org/protocol/relayer-sdk-guides

**Welcome to the Relayer SDK Docs.**

This section provides an overview of the key features of Zama’s FHEVM Relayer JavaScript SDK. The SDK lets you interact with FHEVM smart contracts without dealing directly with the [Gateway Chain](https://docs.zama.ai/protocol/protocol/overview/gateway).

With the Relayer, FHEVM clients only need a wallet on the FHEVM host chain. All interactions with the Gateway chain are handled through HTTP calls to Zama's Relayer, which pays for it on the Gateway chain.

## Where to go next

If you’re new to the Zama Protocol, start with the [Litepaper](https://docs.zama.ai/protocol/zama-protocol-litepaper) or the [Protocol Overview](https://docs.zama.ai/protocol) to understand the foundations.

Otherwise:

🟨 Go to [**Setup guide**](/protocol/relayer-sdk-guides/fhevm-relayer/initialization) to learn how to configure the Relayer SDK for your project.

🟨 Go to [**Input registration**](/protocol/relayer-sdk-guides/fhevm-relayer/input) to see how to register new encrypted inputs for your smart contracts.

🟨 Go to [**User decryption**](/protocol/relayer-sdk-guides/fhevm-relayer/decryption/user-decryption) to enable users to decrypt data with their own keys, once permissions have been granted via Access Control List(ACL).

🟨 Go to [**Public decryption**](/protocol/relayer-sdk-guides/fhevm-relayer/decryption/public-decryption) to learn how to decrypt outputs that are publicly accessible via HTTP.

🟨 Go to [**Solidity ACL Guide**](https://docs.zama.ai/protocol/solidity-guides/smart-contract/acl) for more detailed instructions about access control.

## Help center

Ask technical questions and discuss with the community.

* [Community forum](https://community.zama.ai/c/fhevm/15)
* [Discord channel](https://discord.com/invite/zama)

[NextInitialization](/protocol/relayer-sdk-guides/fhevm-relayer/initialization)

Last updated 1 month ago

---


# Solidity Guides

Source: https://docs.zama.org/protocol/solidity-guides

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


# Zama Protocol Litepaper

Source: https://docs.zama.org/protocol/zama-protocol-litepaper

This litepaper describes Zama’s Confidential Blockchain Protocol, which enables confidential smart contracts on existing public blockchains. It includes details about the protocol and token, as well as documentation for node operators.
 **To read Zama's FHEVM technical whitepaper**, please see [on Github](https://github.com/zama-ai/fhevm/blob/main/fhevm-whitepaper.pdf).

## The blockchain confidentiality dilemma

Why do we need blockchain? This question often comes along when discussing building decentralized applications (dapps). After all, most things we use today are not blockchain based and work just fine. However, there are some applications where the cost of blindly trusting a third party and being wrong is too high, such as when dealing with financial assets, identity or governance. In those cases, consumers and companies want strong guarantees that whatever service is being provided is done correctly, while service providers want to ensure their users have the right to use the assets/data they claim.

Blockchains solve this by enabling anyone to publicly verify that a request was executed according to a predetermined logic, and that the resulting state of the overall system is correct. Service providers and their customers no longer have to trust each other, as the integrity of the transaction is guaranteed by the blockchain itself.

One major issue with public verifiability however is that it requires disclosing all the transactions and data to everyone, as keeping them private would prevent verifiability in the first place. This lack of confidentiality has been a major hindrance to global adoption of blockchains, as the very data it is supposed to be used for (money, identity, …) is highly sensitive by nature. Without confidentiality, blockchain cannot reach mass adoption.

## The Zama Confidential Blockchain Protocol

The Zama Confidential Blockchain Protocol (or simply the Zama Protocol) enables issuing, managing and trading assets confidentially on existing public blockchains. It is the most advanced confidentiality protocol to date, offering:

* **End-to-end encryption** of transaction inputs and state: no-one can see the data, not even node operators.
* **Composability** between confidential contracts, as well as with non-confidential ones. Developers can build on top of other contracts, tokens and dapps.
* **Programmable confidentiality**: smart contracts define who can decrypt what, meaning developers have full control over confidentiality rules in their applications.

The Zama Protocol is not a new L1 or L2, but rather a cross-chain confidentiality layer sitting on top of existing chains. As such, users don’t need to bridge to a new chain and can interact with confidential dapps from wherever they choose.

It leverages Zama’s state-of-the-art Fully Homomorphic Encryption (FHE) technology, which enables computing directly on encrypted data. FHE has long been considered the “holy grail” of cryptography, as it allows end-to-end encryption for any application, onchain or offchain. We believe that just like the internet went from zero encryption with HTTP to encrypting data in transit with HTTPS, the next natural step will be to use FHE to enable end-to-end encryption by default in every application, something we call [HTTPZ](https://www.zama.ai/post/people-should-not-care-about-privacy).

Until recently however, FHE was too slow, too limited in terms of applications it could support, and too difficult to use for developers. This is what our team at Zama has spent the last 5 years solving. We now have a highly efficient FHE technology that can support any type of application, using common programming languages such as Solidity and Python, while being over 100x faster than 5 years ago. Importantly, Zama’s FHE technology is already post-quantum, meaning there is no known quantum algorithms that can break it.

While FHE is the core technology used in the Zama Protocol, we also leverage Multi-Party Computation (MPC) and Zero-Knowledge Proofs (ZK) to address the shortcomings of other confidentiality solutions:

* FHE enables confidentiality while being fully publicly verifiable (anyone can recompute the FHE operations and verify them). Using GPUs will soon allow scaling to 100+ transactions/s while dedicated hardware accelerators (FPGAs and ASICs) will enable scaling to thousands of transactions per second.
* MPC enables decentralizing the global network key, ensuring no single party can access it. Using MPC only to generate keys and decrypt data for users minimizes latency and communication, thereby making it far more scalable and decentralized than using it for private computation.
* ZK ensures the encrypted inputs provided by users were actually encrypted correctly. Using ZK only for this specific purpose makes the ZK proofs lightweight and cheap to generate in a browser or mobile app.

The table below summarizes the advantages of the Zama Protocol versus other technologies used in confidential blockchain protocols:

Zama

Other FHE

MPC

ZK

TEE

Private Chains

**Secure**

✅

✅

✅

✅

❌

✅

**Decentralized**

✅

✅

✅

✅

✅

❌

**Verifiable**

✅

✅

❌

✅

❌

❌

**Composable**

✅

✅

✅

❌

✅

✅

**Scalable**

✅

❌

✅

✅

✅

✅

**Easy to use**

✅

❌

❌

❌

✅

✅

## Roadmap

The Zama Protocol leverages years of research and development work done at Zama. The testnet is already live, with the mainnet on Ethereum launching by end of 2025. The timeline is as follows:

* **Public Testnet (already live).** This will allow anyone to deploy and test their confidential dapps, as well as enabling operators to coordinate and get used to the operations.
* **Ethereum Mainnet (Q4 2025)**. This will be the first official mainnet bringing confidentiality to Ethereum.
* **Other EVM chains (H1 2026)**. We will add more EVM chains to the Zama protocol to enable cross-chain confidential assets and applications.
* **Solana support (H2 2026)**. After an initial phase of EVM-only support, we will deploy the Zama Protocol on Solana, enabling confidential SVM applications.

## Use cases

Confidential smart contracts enable a new design space for blockchain applications, in particular when applied to finance, identity and governance. If we look at web2, it is clear that most applications do not share all the data publicly, and thus it is likely that the vast majority of blockchain applications are yet to be built, now that confidentiality is no longer an issue.

Here are some example use cases:

## Finance

* **Confidential payments.** Stablecoins are one the most successful use case for blockchain, with trillions in yearly volume. Everything from credit card payments to salaries, remittances and banking rails is now moving onchain. One of the absolute key requirement however is confidentiality and compliance. Thanks to FHE and the Zama Protocol, this is now possible: balances and transfer amounts are kept encrypted end-to-end, while payment providers can embed compliance features into the token contract directly. You can read more about confidential, compliant payments [here](https://www.zama.ai/post/programmable-privacy-and-onchain-compliance-using-homomorphic-encryption).
* **Tokenization & RWAs**. The tokenization of financial assets is one of the main adoption drivers of blockchain for large institutions. From fund shares to stocks, bonds or derivatives, there is up to $100T of assets that could potentially move onchain. Due to confidentiality and compliance issues however, TradFi institutions have had to rely on private blockchains, making it difficult to ensure interoperability between institutions. With the Zama Protocol, they can now use existing public blockchain such as Ethereum or Solana to tokenize and trade their assets, while keeping their activity and investor identity confidential. They can also ensure KYC/AML checks are done in the smart contracts directly, without revealing sensitive information to others. You can read more about this use case [in the report published by JP Morgan - Kynexis](https://www.jpmorgan.com/kinexys/documents/JPMC-Kinexys-Project-Epic-Whitepaper-2024.pdf), in which they built a proof-of-concept using Zama’s technology.
* **Confidential DeFi.** DeFi has redefined finance by allowing anyone to participate and earn yield, but it suffers from two major issues: people don’t like sharing how much they own, and bots front-running transactions makes it expensive for end users to swap assets onchain. FHE can solve both issues by enabling end-to-end encrypted swaps, where the amount and possibly asset is kept private at all times. Some other use cases includes confidential lending, onchain credit scoring, option pricing and more.

## Tokens

* **Sealed-bid auctions.** Sell assets such as NFTs or tokens in an onchain sealed-bid auction. Each participant places an encrypted bid onchain. When the auction ends, the highest bidder(s) win the item(s), without revealing any of the bids. Not only does this enable better price discovery, it also prevents bots from stealing the auction by monitoring the mempool. This is a particularly effective method for public token sales.
* **Confidential distributions.** Distributing tokens currently requires disclosing publicly how much each address receives. Whether it’s for airdrops, grants, investors or developers, keeping the distributed amounts private is paramount to privacy and security onchain. With FHE, protocols can distribute their token confidentially, run vesting on those encrypted tokens, enable confidential staking and more.

## Identity and Governance

* **Composable onchain identity.** Offchain, we use our identities all the time, from buying products online to booking plane tickets. Doing so onchain however would leak sensitive information such as your name, address, social security number and more. With FHE however, you can have a complete Decentralized ID (DID) + Verifiable Credentials (VC) system onchain, where your identity is encrypted while being fully composable with decentralized applications. Just like you can have account abstraction, you can now have identity abstraction. This is also essential for compliance in onchain payments and tokenization, as it can be used by smart contracts to verify claims in a decentralized, private manner.
* **Confidential governance.** The idea of onchain voting, whether for DAOs, companies or governments, has been explored for as long as blockchains exist. But having the votes cast publicly onchain can lead to biases, blackmailing, or bribing. With FHE, votes (and numbers of tokens staked) can be kept private, ensuring only the final tally is revealed, and not the individual votes.

## Other examples

* **Onchain corporations.** Managing a company onchain would be impossible without the promise of confidentiality. Indeed, information such as the cap table, financials, board votes, customers, and employee registers should not be disclosed publicly. With FHE, all this information could be kept onchain, allowing smart contracts to automate many day-to-day company operations. **‍‍**
* **Prediction markets. ‍‍**Prediction markets are based on the wisdom of the crowd concept: the average prediction of a large number of people tend to be close to the correct outcome. However, this only works if participants are not biased by previous predictions. The Zama Protocol solves this by enabling prediction markets where predictions are encrypted until revealed periodically, leading to better precision in outcomes.
* **Data marketplaces for AI. ‍‍**AI strives on data. With FHE, users can selectively share and sell their data with companies wishing to train AI models. More than this, models can potentially be trained encrypted, with only the result being decrypted, ensuring that users have a constant stream of revenue for their data vs selling it only once and it being used forever.

These are just some examples of what can be done today. We believe that FHE, through Zama’s Protocol, will enable unprecedented liquidity, enabling users and companies to move onchain. With time and scale, it would even become possible to run entire companies, cities or even countries onchain, including their financial and identity infrastructure, elections, currency, taxes, land, car and company registries. Confidential blockchains don’t just enable programmable money: they enable programmable public infrastructure.

## Creating confidential applications

Creating a confidential dapp using existing solutions often requires learning a new (niche) programming language, using dedicated (and often limited) developer tools, and mastering advanced cryptographic concepts.

The Zama Protocol on the other hand enables developers to create confidential dapps directly in Solidity, without any knowledge of cryptography. Developers simply need to import our library (called FHEVM) and write their logic using the provided operators. You can get started today for free by checking out the developer documentation [here](https://docs.zama.ai/protocol).

The following example shows an example confidential token contract, which can be deployed on any supported chain such as Ethereum.

Simply replace the integer operations by their FHE equivalent, then specify who can decrypt the balances. Of course, developers can build much more complicated applications, such as AMMs, lending, and more. On top of the smart contract library, we also provide a Javascript SDK that streamlines the encryption and decryption client-side, making it almost invisible to end-users.

The access control system used by the Zama Protocol is extremely powerful. By allowing contracts to define who can decrypt which value in it, it makes confidentiality (and compliance) fully programmable. There is no assumption at the protocol or user level, everything is encoded in the application logic itself, allowing companies to choose whether they want to offer end-to-end encryption (aka nobody sees anything, not even the companies building the dapp), or onchain encryption (aka the web2 model: only the user and service provider see the data, but nobody else onchain).

The FHEVM library used by the Zama Protocol supports the following encrypted types and operations:

**Type**

**Symbol**

**Logical**

**Arithmetic**

**Comparison**

**Shifts**

**Branching**

**Integer (unsigned)**

euint8…256

and, or, xor, not

add, sub, mul, div, rem, neg, abs, sign

eq, neq, gt, lt, ge, le, min, max

shl, shr, rotl, rotr

select

**Integer (signed)**

eint8…256

and, or, xor, not

add, sub, mul, div, rem, neg, abs, sign

eq, neq, gt, lt, ge, le, min, max

shl, shr, rotl, rotr

select

**Boolean**

ebool

and, or, xor, not

eq, neq

select

**Bytes**

ebytes1…256

and, or, xor, not

eq, neq

shl, shr, rotl, rotr

select

**Address**

eaddress

eq, neq

select

To make deploying dapps easier, we are also building a “Zama Standard Library”: a set of audited, highly optimized smart contracts for common use cases such as:

* confidential tokens and RWAs
* confidential NFTs
* wrappers to bridge between confidential assets and traditional ones
* a confidential identity stack that enables DID/VC onchain
* UniV2-style confidential AMMs
* Confidential vesting
* Confidential airdrops
* Sealed-bid auctions
* Confidential governance

We will continue adding more over time as we see new use cases appearing.

## Technical details

Blockchains typically only support limited computations, making it impossible to run FHE natively on Ethereum and other L1/L2s. To address this issue, we designed the Zama Protocol based on two core ideas: symbolic execution and threshold decryption.

## **‍Symbolic execution**

The idea behind symbolic execution is that whenever a contract calls the Zama FHEVM Solidity library on the host chain (the L1/L2 where the confidential dapp is deployed) to perform an FHE operation, the host chain itself doesn’t do any actual FHE computation; instead, it produces a pointer to the result and emits an event to notify a network of coprocessors, who do the actual FHE computation. This has many advantages:

* The host chain does not need to change anything, run expensive FHE operations or use specific hardware.
* The host chain is not slowed down by FHE, so non-FHE transactions can be executed as fast as they always have been
* FHE operations can be executed in parallel, rather than sequentially, dramatically increasing throughput.

Since all ciphertexts on the host chain are simply pointers (the actual data is stored by coprocessors), FHE operations can be chained just like regular operations, without needing to wait for the previous ones to complete. The only time we need to wait for a ciphertext to be computed is when it has to be decrypted.

From a security perspective, everything the coprocessors do is publicly verifiable, and anyone can just recompute the ciphertexts to verify the result. Initially, we use multiple coprocessors with a majority consensus, but longer term the goal is to enable anyone to compete to execute FHE operations, leveraging ZK-FHE to prove the correctness.

## **Threshold decryption**

To maintain composability onchain, all ciphertexts need to be encrypted under the same public key. This means the private decryption key has to be secured in a way that prevents illegitimate decryption of ciphertexts. The Zama Protocol solves this by splitting the private key amongst multiple parties, using a dedicated threshold MPC protocol as its Key Management Service (KMS).

In order for a user or contract to decrypt a value, they need to first have been explicitly allowed to do so by the contract that produced the value on the host chain. Decrypting the result is then a simple request to the Zama Gateway, which acts as an orchestrator for the protocol and forwards the request to the KMS parties.

This again ensures that all decryption requests are publicly visible, and thus anyone can verify they match the access control logic defined by smart contracts.

## Components

The Zama Protocol is composed of several core components:

* **Host Chains**: the L1s and L2s that are supported by the Zama Protocol, and on which developers deploy their confidential dapps.
* **FHEVM Library**: the library that developers use to create confidential smart contracts.
* **FHEVM Executor**: the contract that is called by dapps to execute FHE operations on the Host Chain. Each time a contract uses an FHE operation, the Executor automatically emits an event to notify Coprocessors to compute it.
* **Access Control List (ACL)**: a smart contract deployed on each Host Chain, which keeps tracks of who can decrypt what. The ACL is central to the operations of the Zama Protocol and is used both to verify a contract is allowed to compute on an encrypted value, and that an address is allowed to decrypt it. Each time a contract allows an address to use a ciphertext, an event is emitted and relayed by Coprocessors to the Gateway, enabling the aggregation of all Host Chain ACLs into a single Gateway ACL used by the KMS to authenticate decryption requests.
* **$ZAMA token**: the native token of the Zama Protocol, used for payment of the fees, staking and governance.
* **Gateway**: a set of smart contracts used to orchestrate the Zama Protocol, and allow users to request verification of their encrypted inputs, decryption of ciphertexts and bridging of encrypted assets between Host Chains. Each of these operations is a transaction to the Gateway contracts, and requires paying a small fee in $ZAMA tokens. While the Gateway contracts could be deployed on any L1 or L2, we opted to run a dedicated Arbitrum rollup for the Zama Protocol, ensuring maximal performance and cost efficiency. Note that our rollup serves only the Zama Protocol and doesn’t allow third party contracts to be deployed on it.
* **Coprocessors**: a set of nodes responsible for 1. verifying encrypted inputs from users, 2. running the actual FHE computations and storing the resulting ciphertexts, 3. relaying ACL events to the Gateway. The Zama Protocol uses multiple coprocessors, which each commit their results to the Gateway, which in turns runs a majority consensus. All tasks performed by the coprocessors are publicly verifiable. Coprocessors can be vertically and horizontally scaled based on throughput requirements of the various confidential dapps.
* **Key Management Service (KMS)**: a set of nodes running various Multi-Party Computation (MPC) protocols for key generation, CRS generation and threshold decryption. The KMS ensures that no single party can ever access the decryption keys. KMS nodes are orchestrated by the Gateway, ensuring all operations are publicly visible. Furthermore, all KMS nodes must run the MPC software inside AWS Nitro Enclaves, making it harder for operators to leak their shares while providing some level of integrity on the MPC computation. Eventually, our goal will be to use ZK-MPC to enable verifiability without hardware assumptions.
* **Operators**: a set of entities that run the Zama Protocol nodes. This includes Coprocessors and KMS nodes.

The following diagram shows the lifecycle of a confidential token transfer across the various components.

![](https://docs.zama.org/protocol/~gitbook/image?url=https%3A%2F%2F1925969531-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUdSYvSNa6t73FdFzbjGT%252Fuploads%252FfIVliW4oxQzPrCCVc9cZ%252F4.%2520Dapp.png%3Falt%3Dmedia%26token%3Dd7b73070-db76-4928-ac2f-ecfc15c321f1&width=768&dpr=4&quality=100&sign=b4f918cc&sv=2)

## Performance

The Zama Protocol is designed to be horizontally scalable, leveraging our cutting-edge [TFHE-rs](https://docs.zama.ai/tfhe-rs) library. Contrary to the sequential behavior of the EVM, the Zama Protocol parallelizes the computation of FHE operations. As long as a specific ciphertext isn’t used in a sequential chain of FHE operations, Coprocessors will be able to increase the throughput simply by adding more servers.

Since we started working on the Zama Protocol, we have been able to increase throughput exponentially from 0.2 transactions per second to over 20 transactions per second on CPU, enough to make all of Ethereum encrypted.

By the end of 2026, we will migrate to GPUs, with an expected 500-1000 TPS per chain, enough to cover all L2s and most Solana use cases.

Finally, we are working on a dedicated hardware accelerator (ASIC) for FHE, which will enable 100,000+ tps / chain on a single server, enough to bring global payments confidentially onchain.

The important point here is that FHE is no longer limited by underlying algorithms, and is now mostly driven by Moore’s law: the better the hardware, the better the throughput of the Zama Protocol.

![](https://docs.zama.org/protocol/~gitbook/image?url=https%3A%2F%2F1925969531-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUdSYvSNa6t73FdFzbjGT%252Fuploads%252FkT3j4akDquDxKi0OdkPA%252FScreenshot%25202025-10-23%2520at%252009.11.59.png%3Falt%3Dmedia%26token%3D79564459-615f-4f65-a906-bf995dba6b2a&width=768&dpr=4&quality=100&sign=7ff3e9b3&sv=2)

## Security

The Zama Protocol uses a defense-in-depth approach, combining multiple techniques to ensure maximum security:

* We use 128 bits of security and a p-fail of 2^-128 for all FHE operations. This is far more than any other FHE scheme used in blockchain currently. Furthermore, our FHE scheme is post-quantum, meaning it is secure even against quantum computers.
* All the FHE operations are publicly verifiable, allowing anyone to recompute the result and identify malicious FHE nodes. This is akin to optimistic rollup security, but for FHE computation. Furthermore, we don’t run a single FHE node, but rather have 3 operators run FHE nodes and sign their outputs, allowing to have both optimistic security and consensus on the result.
* We use 13 nodes with a 2/3 majority rule for all our MPC protocols, while most other projects only use 3 to 5 nodes. Furthermore, our MPC protocol is robust, meaning it will give a correct output with up to 1/3 malicious nodes. As far as we know, this is the first implementation in production of a robust MPC protocol.
* Additionally, our MPC protocol runs inside AWS Nitro Enclaves, adding a layer of defense in depth and preventing access to the underlying share of the FHE private key from outside the protocol. The enclave also offers an attestation of the software version the MPC nodes are running, allowing the protocol to keep track of software updates. The combination of MPC and Nitro enclaves means recovering the shares and using them outside of the protocol would require AWS and multiple MPC nodes to collude.
* Genesis operators are highly reputable organizations with billions at stake through their non-Zama activities, whether as professional validators, infrastructure providers, businesses, or other. As they are all doxxed, anyone can see if they misbehaved. This brings economic security beyond their on-chain stake, as being caught misbehaving in the Zama Protocol will likely impact their other activities.
* Slashing is done via governance, allowing anyone to suggest a recourse if they identify bad behavior in an operator. This offers greater flexibility by allowing to capture edge cases and treat issues on a case per case basis.
* The Zama Protocol is being audited by Trail of Bits and Zenith. This is one of the largest audits of a crypto protocol, with over 34 audit-weeks spent on it so far.

## Compliance

Building confidential applications often requires complying with local regulations. For example, financial institutions need to know who their customers are, verify that they are eligible to access specific financial instruments, that they are not blacklisted etc. Similarly, token issuers could give themselves the right to see the balances and transactions of their users, and comply offchain with existing AML / compliance tools used by traditional finance today.

Contrary to many blockchain confidentiality protocols that puts the burden of compliance on the end-users, the Zama Protocol enables applications to define their own compliance rules directly within their smart contracts.

The ability to have “programmable compliance” is a key advantage offered by FHE, and means that the protocol itself has no say on who can access which encrypted value. Developers decide what is best for their applications, not the Zama Protocol.

## Future Improvements

The Zama Protocol is the most advanced confidentiality protocol to date, and can already scale to address most blockchain use cases. Nonetheless, there are several areas of improvements we are working on to make it even more decentralized, secure and scalable. These typically rely on a combination of better hardware, better algorithms, and ZK-ifying everything:

## Reaching 100k tps

* **New FHE techniques**: we are constantly inventing new FHE techniques that improve performance. We expect the base algorithms to improve by 10-20x over the coming years, similar to the performance gains ZK had in the past few years.
* **FHE ASICs**: we are working with several companies on accelerating FHE with dedicated hardware. The goal is to make FHE 100x-1000x faster using ASICs, in the same way Bitcoin mining or AI has been improved with dedicated hardware. We expect the first accelerators to be available in 2027-2028.
* **ZK-rollup Gateway**: the Gateway currently uses an optimistic rollup. Our goal is to move to a ZK rollup and improve the performance to support tens of thousands of transactions per second with a latency of less than 100ms.

## Making the KMS even more bullet-proof

* **ZK-MPC**: currently, all MPC protocols require a majority assumption on the nodes running the protocol. While this is fine in practice, in theory it enables MPC nodes to collude and provide an incorrect result. Our current design relies of AWS Nitro Enclaves to ensures the MPC nodes run the correct software, but this makes verifiability dependent on hardware security, which is suboptimal. To address this, we are working on adding ZK proofs to the MPC protocols, allowing anyone to verify that the individual contributions of MPC nodes are correct.
* **Large MPC committees**: MPC doesn’t scale well: the more parties are involved, the slower it gets. As a result, most MPC protocols run with less than 10 nodes. While the Zama Protocol already uses more (13 nodes), it would be preferable to increase that number to a hundred, ensuring even more robustness and decentralization.

## Enabling anyone to be an operator

* **Running MPC inside HSMs**: a major issue with MPC protocols is the need to trust the nodes with not leaking their share of the private key. This is typically done by using TEEs and a trusted committee of nodes. However this does not enable permissionless participation, as malicious attackers could try to break the TEE and access the secret in it. As an alternative, we are exploring how to run MPC inside HSMs such as those used by banks and other critical infrastructure.
* **ZK-FHE**: by proving the correctness of the FHE computation, it becomes possible to replace the Coprocessor consensus by a Proof-of-Work style protocol where anyone can compete to execute FHE operations, as long as they provide a proof that the result is correct. Right now, the overhead of ZK on top of the overhead of FHE makes this impractical, but our team is making good progress.

## Making the protocol fully post-quantum

* **Post-quantum ZKPoK**: Zama’s FHE and MPC technologies are already resistant to quantum computers. However, the ZKPoK is not (similar to most ZK-SNARKs). We are working on replacing it with a lattice-based ZK scheme that is post-quantum.
* **Post-quantum signatures**: while we can make the Zama Protocol components post-quantum, signature schemes used by Host Chains are **not** currently post-quantum. We unfortunately do not have control over this, as it is up to the Ethereum, Solana and other L1/L2s communities to migrate to post-quantum signatures.

## Operations and governance

The Zama Protocol uses Delegated Proof-of-Stake, with 18 operators running the protocol: initially 13 KMS nodes and 5 FHE Coprocessors (then more over time). They are chosen according to the following rules:

* genesis operators are selected based on reputation, DevOps experience and offchain value (equity, revenue, market cap, …). This enables bootstrapping security via reputation, as an operator with a large business value will likely lose customers if they get caught misbehaving in the Zama Protocol.
* we will progressively allow anyone to become a KMS or Coprocessor operator. To do so, they will first need to demonstrate they can reliably run a node in testnet, then stake at least 0.5% of the circulating $ZAMA supply. Every epoch (eg 3 months), the top KMS and Coprocessor operators by stake are selected to run the protocol for the next epoch.
* the active operators earn staking rewards in $ZAMA tokens, based on their role and stake.

Token holders with limited infrastructure capabilities that would not qualify to be an operator can still participate in securing the protocol and earning rewards by delegating their $ZAMA tokens to the whitelisted operators. It is up to each operator to decide how to incentivize their delegators, whether through lower commissions or additional non-$ZAMA rewards.

Updates to the Zama Protocol have to be adopted by a majority of operators to be effective. This includes software updates, changes to the fees, adding support for a new Host Chain, etc. The only exception is pausing the protocol in case of an emergency and blacklisting spammers, which any operator can do (however unpausing / de-blacklisting requires multiple coprocessors to be involved). In case of abuse, operators can get slashed. This ensures that the Zama Protocol has a swift mechanism to address critical issues, while incentivizing operators to behave honestly.

## The $ZAMA token

The $ZAMA token is the native token of the Zama Protocol. It is used for protocol fees and staking. It follows a burn and mint model, where 100% of the fees are burnt and tokens are minted to reward operators.

## Fee model

Deploying a confidential app on a supported chain is free and permissionless. Furthermore, the Zama Protocol does not charge for the FHE computation, instead charging for:

* **Verifying ZKPoKs**. Each time a user includes encrypted inputs in a transaction, they need to pay a fee to the Zama Protocol to verify it.
* **Decrypting ciphertexts**. When a user wants to decrypt a ciphertext, they need to pay a fee to the Zama Protocol.
* **Bridging ciphertexts**. When a user wants to bridge an encrypted value from one chain to another, it needs to request it from the Zama Protocol and pay a fee.

The protocol fees can be paid by the end user, the frontend app or a relayer. As such, developers can create applications without their users ever needing to hold $ZAMA tokens directly.

Protocol fees are paid with $ZAMA tokens, but are priced in USD. A price oracle regularly updates the $ZAMA/USD price on the Gateway, which updates the number of $ZAMA tokens paid for each protocol functionality. This has several advantages:

* it ensures protocol fees are proportional to usage and not dependent on speculation
* it creates predictability for users, developers and relayers, which can model their costs in USD rather than potentially volatile tokens.

Additionally, the Zama Protocol uses a volume-based fee model: the more someone uses the protocol, the less fees they pay per operation. The smart contracts on the Gateway keep track of the number of bits each address has verified/decrypted/bridged over the last 30 days, and applies a discount based on volume.

The initial fee structure is as follows. It can be changed via social consensus based on network performance, operating costs or other reasons put forward by token holders:

* **ZKPoK verification**: from $0.5 to $0.005
* **Bridging**: from $1 to $0.01
* **Decryption**: from $0.1 to $0.001

Taking a confidential token transfer as an example:

* amounts and balances are encrypted
* there is typically 3 decryptions per transaction, one for each of the sender and receiver balances, and one for the final amount transferred, which will be set to 0 if the transfer failed.
* as such, the total cost would be, depending on the discount:

  + ZKPoK verification of encrypted amount: [$0.005 - $0.5]
  + Decryption of 2 balances + amount: 3 \* [$0.001 - $0.1] = [$0.003 - $0.3]
  + Total cost: $0.008 to $0.8

This model is designed to be affordable for large users and profitable for operators, regardless of market condition and price volatility. Eg a user interacting just once a month with confidential apps would pay less than 1$ / transaction, while a user interacting with a high-volume app such as a confidential stablecoin payment app or a wallet would pay less than 1 cent / transaction.

With this fee structure, each 3 tps on a host chain generates on average $1m in fees yearly on the Zama Protocol. Considering the growth of stablecoin payments and onchain finance, we can expect over 100k transactions per second globally in the near future. If 10% of those transactions use Zama for confidentiality, it would generate $3b in fees / year for the protocol.

## Staking rewards

Operators need to stake $ZAMA tokens to participate in running the protocol and receive the associated staking rewards. Tokens distributed as staking rewards are minted according to an inflation rate (5% initially), which can be changed via governance.

When rewards are distributed, they are first split by role (sequencer, coprocessors, KMS nodes), then distributed pro-rata of the square root of the stake of each operator within that group. Each operator then decides how they want to split their rewards with their delegators.

Distributing rewards this way ensures that each operator gets rewarded according to the job they did, while avoiding concentration of rewards into a few operators only.

The table below summarizes the percentage of rewards going to each group, and the expected operator infra costs:

Role

% of rewards / operator

Number of operators

Monthly infra cost / operator

Coprocessors

8%

5

$15,000 / 10 tps on host chains

KMS

4.6%

13

$5,000 / 50 tps decryptions

## Distribution

More information coming soon—Follow [Zama on X](https://x.com/zama_fhe) to get latest updates.

## About Zama, the company

The Zama Protocol is a spinout from Zama, an open source cryptography company building state-of-the-art Fully Homomorphic Encryption (FHE) solutions for blockchain and AI.

Zama has raised over $150m at a $1b valuation from some of the most successful blockchain investors, including Multicoin, Pantera, Blockchange and Protocol Labs, as well as founders of major protocols such as Juan Benet (IPFS/Filecoin), Gavin Wood (Ethereum/Polkadot), Anatoly Yakovenko (Solana), Sandeep Nailwal (Polygon), and others.

## Team

Zama is a cryptography company operating across the globe. It was founded in 2020 by Dr Rand Hindi (CEO) and Dr Pascal Paillier (CTO), with other prominent researchers leading the company, such as Prof Nigel Smart (Chief Academic Officer) and Dr Marc Joye (Chief Scientist). There are more than 90 people working at Zama, of which nearly half hold PhDs, making Zama the largest research team in FHE.

About the founders:

* **Rand** is an entrepreneur and deeptech investor. He is the CEO at Zama and a partner at [Unit.vc](http://Unit.vc), where he invested in over 100+ companies across cryptography, AI and biotech. Rand is also a competitive biohacker, and currently ranks in the top 5% of the Rejuvenation Olympics with an aging rate of 0.68. Rand started coding at the age of 10, founded a Social Network at 14 and started his PhD when he was 21. He then created Snips, a confidential AI startup that was acquired by Sonos. He was previously a member of the French Digital Council, advising the government on AI and Privacy issues, a lecturer at Science Po University in Paris, and an advisor to several biotech, AI and defense companies. He holds a BSc in Computer Science and a PhD in Bioinformatics from University College London (UCL).
* **Pascal** is a pioneer in FHE and cryptography, and the CTO at Zama. He invented one of the first additive homomorphic scheme ([the Paillier encryption scheme](https://en.wikipedia.org/wiki/Paillier_cryptosystem)), which is still widely used today. Pascal has published dozens of papers, with major contributions across various cryptography domains, including FHE, smart cards, and more. Prior to Zama, he led the cryptography innovation team at Gemalto, and founded CryptoExperts a leading cryptography consulting firm. Pascal is a 2025 IACR fellow, received several awards for his research, and led multiple ISO standards for cryptography. He holds a PhD in cryptography from Telecom Paris.

## Products & Services

Everything we do is open source under a dual licensing model. It is free for non-commercial use, prototyping, research and personal projects, but commercial use requires either obtaining an enterprise license or building on top of a protocol that already has one.

Developers building on the Zama Protocol don’t need an extra license. However, forking, copying or using Zama’s technology outside of the Zama Protocol does require a license.

We offer several products and services:

* **FHE libraries** for AI and blockchain. This includes [TFHE-rs](https://github.com/zama-ai/tfhe-rs), [FHEVM](https://github.com/zama-ai/fhevm), [Concrete ML](https://github.com/zama-ai/concrete-ml), and [TKMS](https://github.com/zama-ai/threshold-fhe). They are free for non-commercial use, but require an enterprise license for commercial use.
* **Hosted services**, such as an encryption/decryption relayer and a decryption oracle, that make it easy for app developers to use the Zama Confidential Blockchain Protocol and other protocols based on our FHEVM technology.
* **Premium support** for companies and developers who need help building and managing their FHE applications.

There are over 5,000+ developers using our libraries, representing a 70% market share. Our technology has furthermore been licensed to dozens of companies, including L1s, L2s, finance and AI. Nearly all decentralized protocols using FHE are using Zama’s technology behind the scene.

Note that the Zama Protocol is operated as an independent, decentralized protocol. The services we offer on the company side are independent of the protocol itself, and are meant to serve enterprises and developers who want to build confidential applications, regardless of whether they are deployed on the Zama Protocol or not.

## Additional links

* [Zama Protocol docs](https://docs.zama.ai/protocol)
* [FHEVM whitepaper](https://github.com/zama-ai/fhevm/blob/main/fhevm-whitepaper.pdf)
* [TFHE-rs handbook](https://github.com/zama-ai/tfhe-rs-handbook/blob/main/tfhe-rs-handbook.pdf)
* MPC protocol spec (coming soon)
* Audit report (coming soon)
* [Zama GitHub](https://github.com/zama-ai)
* [Discord](https://discord.gg/zama)
* [X](https://x.com/zama)
* [Zama blog](https://www.zama.ai/blog)

## Disclaimer

The present light paper and/or any other accompanying documentation ("**Document**”) only provide educational material about the Zama Protocol and the $ZAMA token. Please note that the Zama Protocol and the $ZAMA token are under active development and are subject to change. Zama may change this Document at any time at its sole discretion without notice.

Any documentation is provided for informational purposes only and does not constitute some kind of prospectus, key information document, or similar document. No prospectus, key information document, or similar document will be provided at any time. There is no guarantee for the completeness of the documentation provided. All numbers and forward-looking statements mentioned within the present document as well as any accompanying documentation reflect mere estimations/indications. They are not guaranteed and may change substantially.

Any and all liability of ZAMA Switzerland AG and/or any affiliated legal entity or private individual for the completeness and accuracy of the documentation provided and any damages arising from reliance on such documentation is limited to the fullest extent permitted by any applicable law.

Any dispute related to or arising out of the information provided within the present Document as well as any accompanying documentation shall be submitted to the exclusive jurisdiction of the competent courts of Zug, Switzerland, with the exclusion of any other jurisdiction or arbitration.

This disclaimer, the Document, as well as any accompanying documentation shall be governed by and construed and interpreted in accordance with the substantive laws of Switzerland, excluding the Swiss conflict of law rules.

Last updated 1 month ago

---


# Contributing

Source: https://docs.zama.org/protocol/developer/contribute

There are two ways to contribute to FHEVM:

* [Open issues](https://github.com/zama-ai/fhevm/issues/new/choose) to report bugs and typos, or to suggest new ideas
* Request to become an official contributor by emailing [[email protected]](/cdn-cgi/l/email-protection#721a171e1e1d3208131f135c131b).

Becoming an approved contributor involves signing our Contributor License Agreement (CLA). Only approved contributors can send pull requests, so please make sure to get in touch before you do!

## Zama Bounty Program

Solve challenges and earn rewards:

* [bounty-program](https://github.com/zama-ai/bounty-program) - Zama's FHE Bounty Program

[PreviousRoadmap](/protocol/protocol/roadmap)

Last updated 6 months ago

---


# Decryption

Source: https://docs.zama.org/protocol/examples/basic/decryption

[User decrypt single value](/protocol/examples/basic/decryption/fhe-user-decrypt-single-value)[User decrypt multiple values](/protocol/examples/basic/decryption/fhe-user-decrypt-multiple-values)

Last updated 6 months ago

---


# User decrypt multiple values

Source: https://docs.zama.org/protocol/examples/basic/decryption/fhe-user-decrypt-multiple-values

This example demonstrates the FHE user decryption mechanism with multiple values.

User decryption is a mechanism that allows specific users to decrypt encrypted values while keeping them hidden from others. Unlike public decryption where decrypted values become visible to everyone, user decryption maintains privacy by only allowing authorized users with the proper permissions to view the data. While permissions are granted onchain through smart contracts, the actual **decryption call occurs off-chain in the frontend application**.

To run this example correctly, make sure the files are placed in the following directories:

* `.sol` file → `<your-project-root-dir>/contracts/`
* `.ts` file → `<your-project-root-dir>/test/`

This ensures Hardhat can compile and test your contracts as expected.

UserDecryptMultipleValues.sol

UserDecryptMultipleValues.ts

Copy

```
// SPDX-License-Identifier: BSD-3-Clause-Clear
pragma solidity ^0.8.24;

import { FHE, ebool, euint32, euint64 } from "@fhevm/solidity/lib/FHE.sol";
import { ZamaEthereumConfig } from "@fhevm/solidity/config/ZamaConfig.sol";

contract UserDecryptMultipleValues is ZamaEthereumConfig {
  ebool private _encryptedBool; // = 0 (uninitizalized)
  euint32 private _encryptedUint32; // = 0 (uninitizalized)
  euint64 private _encryptedUint64; // = 0 (uninitizalized)

  // solhint-disable-next-line no-empty-blocks
  constructor() {}

  function initialize(bool a, uint32 b, uint64 c) external {
    // Compute 3 trivial FHE formulas

    // _encryptedBool = a ^ false
    _encryptedBool = FHE.xor(FHE.asEbool(a), FHE.asEbool(false));

    // _encryptedUint32 = b + 1
    _encryptedUint32 = FHE.add(FHE.asEuint32(b), FHE.asEuint32(1));

    // _encryptedUint64 = c + 1
    _encryptedUint64 = FHE.add(FHE.asEuint64(c), FHE.asEuint64(1));

    // see `DecryptSingleValue.sol` for more detailed explanations
    // about FHE permissions and asynchronous user decryption requests.
    FHE.allowThis(_encryptedBool);
    FHE.allowThis(_encryptedUint32);
    FHE.allowThis(_encryptedUint64);

    FHE.allow(_encryptedBool, msg.sender);
    FHE.allow(_encryptedUint32, msg.sender);
    FHE.allow(_encryptedUint64, msg.sender);
  }

  function encryptedBool() public view returns (ebool) {
    return _encryptedBool;
  }

  function encryptedUint32() public view returns (euint32) {
    return _encryptedUint32;
  }

  function encryptedUint64() public view returns (euint64) {
    return _encryptedUint64;
  }
}
```


Last updated 1 month ago

---


# User decrypt single value

Source: https://docs.zama.org/protocol/examples/basic/decryption/fhe-user-decrypt-single-value

This example demonstrates the FHE user decryption mechanism with a single value.

User decryption is a mechanism that allows specific users to decrypt encrypted values while keeping them hidden from others. Unlike public decryption where decrypted values become visible to everyone, user decryption maintains privacy by only allowing authorized users with the proper permissions to view the data. While permissions are granted onchain through smart contracts, the actual **decryption call occurs off-chain in the frontend application**.

To run this example correctly, make sure the files are placed in the following directories:

* `.sol` file → `<your-project-root-dir>/contracts/`
* `.ts` file → `<your-project-root-dir>/test/`

This ensures Hardhat can compile and test your contracts as expected.

UserDecryptSingleValue.sol

UserDecryptSingleValue.ts

Copy

```
// SPDX-License-Identifier: BSD-3-Clause-Clear
pragma solidity ^0.8.24;

import { FHE, euint32 } from "@fhevm/solidity/lib/FHE.sol";
import { ZamaEthereumConfig } from "@fhevm/solidity/config/ZamaConfig.sol";

/**
 * This trivial example demonstrates the FHE decryption mechanism
 * and highlights common pitfalls developers may encounter.
 */
contract UserDecryptSingleValue is ZamaEthereumConfig {
  euint32 private _trivialEuint32;

  // solhint-disable-next-line no-empty-blocks
  constructor() {}

  function initializeUint32(uint32 value) external {
    // Compute a trivial FHE formula _trivialEuint32 = value + 1
    _trivialEuint32 = FHE.add(FHE.asEuint32(value), FHE.asEuint32(1));

    // Grant FHE permissions to:
    // ✅ The contract caller (`msg.sender`): allows them to decrypt `_trivialEuint32`.
    // ✅ The contract itself (`address(this)`): allows it to operate on `_trivialEuint32` and
    //    also enables the caller to perform user decryption.
    //
    // Note: If you forget to call `FHE.allowThis(_trivialEuint32)`, the user will NOT be able
    //       to user decrypt the value! Both the contract and the caller must have FHE permissions
    //       for user decryption to succeed.
    FHE.allowThis(_trivialEuint32);
    FHE.allow(_trivialEuint32, msg.sender);
  }

  function initializeUint32Wrong(uint32 value) external {
    // Compute a trivial FHE formula _trivialEuint32 = value + 1
    _trivialEuint32 = FHE.add(FHE.asEuint32(value), FHE.asEuint32(1));

    // ❌ Common FHE permission mistake:
    // ================================================================
    // We grant FHE permissions to the contract caller (`msg.sender`),
    // expecting they will be able to user decrypt the encrypted value later.
    //
    // However, this will fail! 💥
    // The contract itself (`address(this)`) also needs FHE permissions to allow user decryption.
    // Without granting the contract access using `FHE.allowThis(...)`,
    // the user decryption attempt by the user will not succeed.
    FHE.allow(_trivialEuint32, msg.sender);
  }

  function encryptedUint32() public view returns (euint32) {
    return _trivialEuint32;
  }
}
```


Last updated 1 month ago

---


# Public Decrypt single value

Source: https://docs.zama.org/protocol/examples/basic/decryption/heads-or-tails

This example showcases the public decryption mechanism and its corresponding on-chain verification in the case of a single value. The core assertion is to guarantee that a single given cleartext is the cryptographically verifiable result of the decryption of a single original on-chain ciphertext.

To run this example correctly, make sure the files are placed in the following directories:

* `.sol` file → `<your-project-root-dir>/contracts/`
* `.ts` file → `<your-project-root-dir>/test/`

This ensures Hardhat can compile and test your contracts as expected.

HeadsOrTails.sol

HeadsOrTails.ts

Copy

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import { FHE, ebool } from "@fhevm/solidity/lib/FHE.sol";
import { ZamaEthereumConfig } from "@fhevm/solidity/config/ZamaConfig.sol";

/**
 * @title HeadsOrTails
 * @notice Implements a simple Heads or Tails game demonstrating public, permissionless decryption
 *         using the FHE.makePubliclyDecryptable feature.
 * @dev Inherits from ZamaEthereumConfig to access FHE functions like FHE.randEbool() and FHE.verifySignatures().
 */
contract HeadsOrTails is ZamaEthereumConfig {
    constructor() {}

    /**
     * @notice Simple counter to assign a unique ID to each new game.
     */
    uint256 private counter = 0;

    /**
     * @notice Defines the entire state for a single Heads or Tails game instance.
     */
    struct Game {
        /// @notice The address of the player who chose Heads.
        address headsPlayer;
        /// @notice The address of the player who chose Tails.
        address tailsPlayer;
        /// @notice The core encrypted result. This is a publicly decryptable ebool handle.
        //          true means Heads won; false means Tails won.
        ebool encryptedHasHeadsWon;
        /// @notice The clear address of the final winner, set after decryption and verification.
        address winner;
    }

    /**
     * @notice Mapping to store all game states, accessible by a unique game ID.
     */
    mapping(uint256 gameId => Game game) public games;

    /**
     * @notice Emitted when a new game is started, providing the encrypted handle required for decryption.
     * @param gameId The unique identifier for the game.
     * @param headsPlayer The address choosing Heads.
     * @param tailsPlayer The address choosing Tails.
     * @param encryptedHasHeadsWon The encrypted handle (ciphertext) storing the result.
     */
    event GameCreated(
        uint256 indexed gameId,
        address indexed headsPlayer,
        address indexed tailsPlayer,
        ebool encryptedHasHeadsWon
    );

    /**
     * @notice Initiates a new Heads or Tails game, generates the result using FHE,
     *         and makes the result publicly available for decryption.
     * @param headsPlayer The player address choosing Heads.
     * @param tailsPlayer The player address choosing Tails.
     */
    function headsOrTails(address headsPlayer, address tailsPlayer) external {
        require(headsPlayer != address(0), "Heads player is address zero");
        require(tailsPlayer != address(0), "Tails player is address zero");
        require(headsPlayer != tailsPlayer, "Heads player and Tails player should be different");

        // true: Heads
        // false: Tails
        ebool headsOrTailsResult = FHE.randEbool();

        counter++;

        // gameId > 0
        uint256 gameId = counter;
        games[gameId] = Game({
            headsPlayer: headsPlayer,
            tailsPlayer: tailsPlayer,
            encryptedHasHeadsWon: headsOrTailsResult,
            winner: address(0)
        });

        // We make the result publicly decryptable.
        FHE.makePubliclyDecryptable(headsOrTailsResult);

        // You can catch the event to get the gameId and the encryptedHasHeadsWon handle
        // for further decryption requests, or create a view function.
        emit GameCreated(gameId, headsPlayer, tailsPlayer, games[gameId].encryptedHasHeadsWon);
    }

    /**
     * @notice Returns the number of games created so far.
     * @return The number of games created.
     */
    function getGamesCount() public view returns (uint256) {
        return counter;
    }

    /**
     * @notice Returns the encrypted ebool handle that stores the game result.
     * @param gameId The ID of the game.
     * @return The encrypted result (ebool handle).
     */
    function hasHeadsWon(uint256 gameId) public view returns (ebool) {
        return games[gameId].encryptedHasHeadsWon;
    }

    /**
     * @notice Returns the address of the game winner.
     * @param gameId The ID of the game.
     * @return The winner's address (address(0) if not yet revealed).
     */
    function getWinner(uint256 gameId) public view returns (address) {
        require(games[gameId].winner != address(0), "Game winner not yet revealed");
        return games[gameId].winner;
    }

    /**
     * @notice Verifies the provided (decryption proof, ABI-encoded clear value) pair against the stored ciphertext,
     *         and then stores the winner of the game.
     * @param gameId The ID of the game to settle.
     * @param abiEncodedClearGameResult The ABI-encoded clear value (bool) associated to the `decryptionProof`.
     * @param decryptionProof The proof that validates the decryption.
     */
    function recordAndVerifyWinner(
        uint256 gameId,
        bytes memory abiEncodedClearGameResult,
        bytes memory decryptionProof
    ) public {
        require(games[gameId].winner == address(0), "Game winner already revealed");

        // 1. FHE Verification: Build the list of ciphertexts (handles) and verify the proof.
        //    The verification checks that 'abiEncodedClearGameResult' is the true decryption
        //    of the 'encryptedHasHeadsWon' handle using the provided 'decryptionProof'.

        // Creating the list of handles in the right order! In this case the order does not matter since the proof
        // only involves 1 single handle.
        bytes32[] memory cts = new bytes32[](1);
        cts[0] = FHE.toBytes32(games[gameId].encryptedHasHeadsWon);

        // This FHE call reverts the transaction if the decryption proof is invalid.
        FHE.checkSignatures(cts, abiEncodedClearGameResult, decryptionProof);

        // 2. Decode the clear result and determine the winner's address.
        //    In this very specific case, the function argument `abiEncodedClearGameResult` could have been a simple
        //    `bool` instead of an abi-encoded bool. In this case, we should have compute abi.encode on-chain
        bool decodedClearGameResult = abi.decode(abiEncodedClearGameResult, (bool));
        address winner = decodedClearGameResult ? games[gameId].headsPlayer : games[gameId].tailsPlayer;

        // 3. Store the winner
        games[gameId].winner = winner;
    }
}
```


Last updated 1 month ago

---


# Public Decrypt multiple values

Source: https://docs.zama.org/protocol/examples/basic/decryption/highest-die-roll

This example showcases the public decryption mechanism and its corresponding on-chain verification in the case of multiple values. The core assertion is to guarantee that multiple given cleartexts are the cryptographically verifiable results of the decryption of multiple original on-chain ciphertexts.

To run this example correctly, make sure the files are placed in the following directories:

* `.sol` file → `<your-project-root-dir>/contracts/`
* `.ts` file → `<your-project-root-dir>/test/`

This ensures Hardhat can compile and test your contracts as expected.

HighestDieRoll.sol

HighestDieRoll.ts

Copy

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import { FHE, euint8 } from "@fhevm/solidity/lib/FHE.sol";
import { ZamaEthereumConfig } from "@fhevm/solidity/config/ZamaConfig.sol";

/**
 * @title HighestDieRoll
 * @notice Implements a simple 8-sided Die Roll game demonstrating public, permissionless decryption
 *         using the FHE.makePubliclyDecryptable feature.
 * @dev Inherits from ZamaEthereumConfig to access FHE functions like FHE.randEbool() and FHE.verifySignatures().
 */
contract HighestDieRoll is ZamaEthereumConfig {
    constructor() {}

    /**
     * @notice Simple counter to assign a unique ID to each new game.
     */
    uint256 private counter = 0;

    /**
     * @notice Defines the entire state for a single Heads or Tails game instance.
     */
    struct Game {
        /// @notice The address of the player who chose Heads.
        address playerA;
        /// @notice The address of the player who chose Tails.
        address playerB;
        /// @notice The core encrypted result. This is a publicly decryptable set of 4 handle.
        euint8 playerAEncryptedDieRoll;
        euint8 playerBEncryptedDieRoll;
        /// @notice The clear address of the final winne, address(0) if draw, set after decryption and verification.
        address winner;
        /// @notice true if the game result is revealed
        bool revealed;
    }

    /**
     * @notice Mapping to store all game states, accessible by a unique game ID.
     */
    mapping(uint256 gameId => Game game) public games;

    /**
     * @notice Emitted when a new game is started, providing the encrypted handle required for decryption.
     * @param gameId The unique identifier for the game.
     * @param playerA The address of playerA.
     * @param playerB The address of playerB.
     * @param playerAEncryptedDieRoll The encrypted die roll result of playerA.
     * @param playerBEncryptedDieRoll The encrypted die roll result of playerB.
     */
    event GameCreated(
        uint256 indexed gameId,
        address indexed playerA,
        address indexed playerB,
        euint8 playerAEncryptedDieRoll,
        euint8 playerBEncryptedDieRoll
    );

    /**
     * @notice Initiates a new highest die roll game, generates the result using FHE,
     *         and makes the result publicly available for decryption.
     * @param playerA The player address choosing Heads.
     * @param playerB The player address choosing Tails.
     */
    function highestDieRoll(address playerA, address playerB) external {
        require(playerA != address(0), "playerA is address zero");
        require(playerB != address(0), "playerB player is address zero");
        require(playerA != playerB, "playerA and playerB should be different");

        euint8 playerAEncryptedDieRoll = FHE.randEuint8();
        euint8 playerBEncryptedDieRoll = FHE.randEuint8();

        counter++;

        // gameId > 0
        uint256 gameId = counter;
        games[gameId] = Game({
            playerA: playerA,
            playerB: playerB,
            playerAEncryptedDieRoll: playerAEncryptedDieRoll,
            playerBEncryptedDieRoll: playerBEncryptedDieRoll,
            winner: address(0),
            revealed: false
        });

        // We make the results publicly decryptable.
        FHE.makePubliclyDecryptable(playerAEncryptedDieRoll);
        FHE.makePubliclyDecryptable(playerBEncryptedDieRoll);

        // You can catch the event to get the gameId and the die rolls handles
        // for further decryption requests, or create a view function.
        emit GameCreated(gameId, playerA, playerB, playerAEncryptedDieRoll, playerBEncryptedDieRoll);
    }

    /**
     * @notice Returns the number of games created so far.
     * @return The number of games created.
     */
    function getGamesCount() public view returns (uint256) {
        return counter;
    }

    /**
     * @notice Returns the encrypted euint8 handle that stores the playerA die roll.
     * @param gameId The ID of the game.
     * @return The encrypted result (euint8 handle).
     */
    function getPlayerADieRoll(uint256 gameId) public view returns (euint8) {
        return games[gameId].playerAEncryptedDieRoll;
    }

    /**
     * @notice Returns the encrypted euint8 handle that stores the playerB die roll.
     * @param gameId The ID of the game.
     * @return The encrypted result (euint8 handle).
     */
    function getPlayerBDieRoll(uint256 gameId) public view returns (euint8) {
        return games[gameId].playerBEncryptedDieRoll;
    }

    /**
     * @notice Returns the address of the game winner. If the game is finalized, the function returns `address(0)`
     *         if the game is a draw.
     * @param gameId The ID of the game.
     * @return The winner's address (address(0) if not yet revealed or draw).
     */
    function getWinner(uint256 gameId) public view returns (address) {
        require(games[gameId].revealed, "Game winner not yet revealed");
        return games[gameId].winner;
    }

    /**
     * @notice Returns `true` if the game result is publicly revealed, `false` otherwise.
     * @param gameId The ID of the game.
     * @return true if the game is publicly revealed.
     */
    function isGameRevealed(uint256 gameId) public view returns (bool) {
        return games[gameId].revealed;
    }

    /**
     * @notice Verifies the provided (decryption proof, ABI-encoded clear values) pair against the stored ciphertext,
     *         and then stores the winner of the game.
     * @param gameId The ID of the game to settle.
     * @param abiEncodedClearGameResult The ABI-encoded clear values (uint8, uint8) associated to the `decryptionProof`.
     * @param decryptionProof The proof that validates the decryption.
     */
    function recordAndVerifyWinner(
        uint256 gameId,
        bytes memory abiEncodedClearGameResult,
        bytes memory decryptionProof
    ) public {
        require(!games[gameId].revealed, "Game already revealed");

        // 1. FHE Verification: Build the list of ciphertexts (handles) and verify the proof.
        //    The verification checks that 'abiEncodedClearGameResult' is the true decryption
        //    of the '(playerAEncryptedDieRoll, playerBEncryptedDieRoll)' handle pair using
        //    the provided 'decryptionProof'.

        // Creating the list of handles in the right order! In this case the order does not matter since the proof
        // only involves 1 single handle.
        bytes32[] memory cts = new bytes32[](2);
        cts[0] = FHE.toBytes32(games[gameId].playerAEncryptedDieRoll);
        cts[1] = FHE.toBytes32(games[gameId].playerBEncryptedDieRoll);

        // This FHE call reverts the transaction if the decryption proof is invalid.
        FHE.checkSignatures(cts, abiEncodedClearGameResult, decryptionProof);

        // 2. Decode the clear result and determine the winner's address.
        //    In this very specific case, the function argument `abiEncodedClearGameResult` could have been replaced by two
        //    `uint8` instead of an abi-encoded uint8 pair. In this case, we should have to compute abi.encode on-chain
        (uint8 decodedClearPlayerADieRoll, uint8 decodedClearPlayerBDieRoll) = abi.decode(
            abiEncodedClearGameResult,
            (uint8, uint8)
        );

        // The die is an 8-sided die (d8) (1..8)
        decodedClearPlayerADieRoll = (decodedClearPlayerADieRoll % 8) + 1;
        decodedClearPlayerBDieRoll = (decodedClearPlayerBDieRoll % 8) + 1;

        address winner = decodedClearPlayerADieRoll > decodedClearPlayerBDieRoll
            ? games[gameId].playerA
            : (decodedClearPlayerADieRoll < decodedClearPlayerBDieRoll ? games[gameId].playerB : address(0));

        // 3. Store the revealed flag
        games[gameId].revealed = true;
        games[gameId].winner = winner;
    }
}
```


Last updated 1 month ago

---


# FHE Operations

Source: https://docs.zama.org/protocol/examples/basic/fhe-operations

Last updated 6 months ago

---


# Add

Source: https://docs.zama.org/protocol/examples/basic/fhe-operations/fheadd

This example demonstrates how to write a simple "a + b" contract using FHEVM.

To run this example correctly, make sure the files are placed in the following directories:

* `.sol` file → `<your-project-root-dir>/contracts/`
* `.ts` file → `<your-project-root-dir>/test/`

This ensures Hardhat can compile and test your contracts as expected.

FHEAdd.sol

FHEAdd.ts

Copy

```
// SPDX-License-Identifier: BSD-3-Clause-Clear
pragma solidity ^0.8.24;

import { FHE, euint8, externalEuint8 } from "@fhevm/solidity/lib/FHE.sol";
import { ZamaEthereumConfig } from "@fhevm/solidity/config/ZamaConfig.sol";

contract FHEAdd is ZamaEthereumConfig {
  euint8 private _a;
  euint8 private _b;
  // solhint-disable-next-line var-name-mixedcase
  euint8 private _a_plus_b;

  // solhint-disable-next-line no-empty-blocks
  constructor() {}

  function setA(externalEuint8 inputA, bytes calldata inputProof) external {
    _a = FHE.fromExternal(inputA, inputProof);
    FHE.allowThis(_a);
  }

  function setB(externalEuint8 inputB, bytes calldata inputProof) external {
    _b = FHE.fromExternal(inputB, inputProof);
    FHE.allowThis(_b);
  }

  function computeAPlusB() external {
    // The sum `a + b` is computed by the contract itself (`address(this)`).
    // Since the contract has FHE permissions over both `a` and `b`,
    // it is authorized to perform the `FHE.add` operation on these values.
    // It does not matter if the contract caller (`msg.sender`) has FHE permission or not.
    _a_plus_b = FHE.add(_a, _b);

    // At this point the contract ifself (`address(this)`) has been granted ephemeral FHE permission
    // over `_a_plus_b`. This FHE permission will be revoked when the function exits.
    //
    // Now, to make sure `_a_plus_b` can be decrypted by the contract caller (`msg.sender`),
    // we need to grant permanent FHE permissions to both the contract ifself (`address(this)`)
    // and the contract caller (`msg.sender`)
    FHE.allowThis(_a_plus_b);
    FHE.allow(_a_plus_b, msg.sender);
  }

  function result() public view returns (euint8) {
    return _a_plus_b;
  }
}
```


Last updated 1 month ago

---


# If then else

Source: https://docs.zama.org/protocol/examples/basic/fhe-operations/fheifthenelse

This example demonstrates how to write a simple contract with conditions using FHEVM, in comparison to a simple counter.

To run this example correctly, make sure the files are placed in the following directories:

* `.sol` file → `<your-project-root-dir>/contracts/`
* `.ts` file → `<your-project-root-dir>/test/`

This ensures Hardhat can compile and test your contracts as expected.

FHEIfThenElse.sol

FHEIfThenElse.ts

Copy

```
// SPDX-License-Identifier: BSD-3-Clause-Clear
pragma solidity ^0.8.24;

import { FHE, ebool, euint8, externalEuint8 } from "@fhevm/solidity/lib/FHE.sol";
import { ZamaEthereumConfig } from "@fhevm/solidity/config/ZamaConfig.sol";

contract FHEIfThenElse is ZamaEthereumConfig {
  euint8 private _a;
  euint8 private _b;
  euint8 private _max;

  // solhint-disable-next-line no-empty-blocks
  constructor() {}

  function setA(externalEuint8 inputA, bytes calldata inputProof) external {
    _a = FHE.fromExternal(inputA, inputProof);
    FHE.allowThis(_a);
  }

  function setB(externalEuint8 inputB, bytes calldata inputProof) external {
    _b = FHE.fromExternal(inputB, inputProof);
    FHE.allowThis(_b);
  }

  function computeMax() external {
    // a >= b
    // solhint-disable-next-line var-name-mixedcase
    ebool _a_ge_b = FHE.ge(_a, _b);

    // a >= b ? a : b
    _max = FHE.select(_a_ge_b, _a, _b);

    // For more information about FHE permissions in this case,
    // read the `computeAPlusB()` commentaries in `FHEAdd.sol`.
    FHE.allowThis(_max);
    FHE.allow(_max, msg.sender);
  }

  function result() public view returns (euint8) {
    return _max;
  }
}
```


Last updated 1 month ago

---


# ERC7984 Standard

Source: https://docs.zama.org/protocol/examples/openzeppelin-confidential-contracts/erc7984

This example demonstrates how to create a confidential token using OpenZeppelin's smart contract library powered by ZAMA's FHEVM.

To run this example correctly, make sure you clone the [fhevm-hardhat-template](https://github.com/zama-ai/fhevm-hardhat-template) and that the files are placed in the following directories:

* `.sol` file → `<your-project-root-dir>/contracts/`
* `.ts` file → `<your-project-root-dir>/test/`

This ensures Hardhat can compile and test your contracts as expected.

ERC7984Example.sol

ERC7984Example.test.ts

ERC7984Example.fixture.ts

Copy

```
// SPDX-License-Identifier: BSD-3-Clause-Clear
pragma solidity ^0.8.24;

import {Ownable2Step, Ownable} from "@openzeppelin/contracts/access/Ownable2Step.sol";
import {FHE, externalEuint64, euint64} from "@fhevm/solidity/lib/FHE.sol";
import {ZamaEthereumConfig} from "@fhevm/solidity/config/ZamaConfig.sol";
import {ERC7984} from "@openzeppelin/confidential-contracts/token/ERC7984.sol";

contract ERC7984Example is ZamaEthereumConfig, ERC7984, Ownable2Step {
    constructor(
        address owner,
        uint64 amount,
        string memory name_,
        string memory symbol_,
        string memory tokenURI_
    ) ERC7984(name_, symbol_, tokenURI_) Ownable(owner) {
        euint64 encryptedAmount = FHE.asEuint64(amount);
        _mint(owner, encryptedAmount);
    }
}
```

Copy

```
import { expect } from 'chai';
import { ethers, fhevm } from 'hardhat';

describe('ERC7984Example', function () {
  let token: any;
  let owner: any;
  let recipient: any;
  let other: any;

  const INITIAL_AMOUNT = 1000;
  const TRANSFER_AMOUNT = 100;

  beforeEach(async function () {
    [owner, recipient, other] = await ethers.getSigners();

    // Deploy ERC7984Example contract
    token = await ethers.deployContract('ERC7984Example', [
      owner.address,
      INITIAL_AMOUNT,
      'Confidential Token',
      'CTKN',
      'https://example.com/token'
    ]);
  });

  describe('Initialization', function () {
    it('should set the correct name', async function () {
      expect(await token.name()).to.equal('Confidential Token');
    });

    it('should set the correct symbol', async function () {
      expect(await token.symbol()).to.equal('CTKN');
    });

    it('should set the correct token URI', async function () {
      expect(await token.tokenURI()).to.equal('https://example.com/token');
    });

    it('should mint initial amount to owner', async function () {
      // Verify that the owner has a balance (without decryption for now)
      const balanceHandle = await token.confidentialBalanceOf(owner.address);
      expect(balanceHandle).to.not.be.undefined;
    });
  });

  describe('Transfer Process', function () {
    it('should transfer tokens from owner to recipient', async function () {
      // Create encrypted input for transfer amount
      const encryptedInput = await fhevm
        .createEncryptedInput(await token.getAddress(), owner.address)
        .add64(TRANSFER_AMOUNT)
        .encrypt();

      // Perform the transfer
      await expect(token
        .connect(owner)
        ['confidentialTransfer(address,bytes32,bytes)'](
          recipient.address,
          encryptedInput.handles[0],
          encryptedInput.inputProof
        )).to.not.be.reverted;

      // Check that both addresses have balance handles (without decryption for now)
      const recipientBalanceHandle = await token.confidentialBalanceOf(recipient.address);
      const ownerBalanceHandle = await token.confidentialBalanceOf(owner.address);
      expect(recipientBalanceHandle).to.not.be.undefined;
      expect(ownerBalanceHandle).to.not.be.undefined;
    });

    it('should allow recipient to transfer received tokens', async function () {
      // First transfer from owner to recipient
      const encryptedInput1 = await fhevm
        .createEncryptedInput(await token.getAddress(), owner.address)
        .add64(TRANSFER_AMOUNT)
        .encrypt();

      await expect(token
        .connect(owner)
        ['confidentialTransfer(address,bytes32,bytes)'](
          recipient.address,
          encryptedInput1.handles[0],
          encryptedInput1.inputProof
        )).to.not.be.reverted;

      // Second transfer from recipient to other
      const encryptedInput2 = await fhevm
        .createEncryptedInput(await token.getAddress(), recipient.address)
        .add64(50) // Transfer half of what recipient received
        .encrypt();

      await expect(token
        .connect(recipient)
        ['confidentialTransfer(address,bytes32,bytes)'](
          other.address,
          encryptedInput2.handles[0],
          encryptedInput2.inputProof
        )).to.not.be.reverted;

      // Check that all addresses have balance handles (without decryption for now)
      const otherBalanceHandle = await token.confidentialBalanceOf(other.address);
      const recipientBalanceHandle = await token.confidentialBalanceOf(recipient.address);
      expect(otherBalanceHandle).to.not.be.undefined;
      expect(recipientBalanceHandle).to.not.be.undefined;
    });

    it('should revert when trying to transfer more than balance', async function () {
      const excessiveAmount = INITIAL_AMOUNT + 100;
      const encryptedInput = await fhevm
        .createEncryptedInput(await token.getAddress(), recipient.address)
        .add64(excessiveAmount)
        .encrypt();

      await expect(
        token
          .connect(recipient)
          ['confidentialTransfer(address,bytes32,bytes)'](
            other.address,
            encryptedInput.handles[0],
            encryptedInput.inputProof
          )
      ).to.be.revertedWithCustomError(token, 'ERC7984ZeroBalance')
        .withArgs(recipient.address);
    });

    it('should revert when transferring to zero address', async function () {
      const encryptedInput = await fhevm
        .createEncryptedInput(await token.getAddress(), owner.address)
        .add64(TRANSFER_AMOUNT)
        .encrypt();

      await expect(
        token
          .connect(owner)
          ['confidentialTransfer(address,bytes32,bytes)'](
            ethers.ZeroAddress,
            encryptedInput.handles[0],
            encryptedInput.inputProof
          )
      ).to.be.revertedWithCustomError(token, 'ERC7984InvalidReceiver')
        .withArgs(ethers.ZeroAddress);
    });
  });
});
```


Last updated 1 month ago

---


# ERC7984 Tutorial

Source: https://docs.zama.org/protocol/examples/openzeppelin-confidential-contracts/erc7984/erc7984-tutorial

This tutorial explains how to create a confidential fungible token using Fully Homomorphic Encryption (FHE) and the OpenZeppelin smart contract library. By following this guide, you will learn how to build a token where balances and transactions remain encrypted while maintaining full functionality.

## Why FHE for confidential tokens?

Confidential tokens make sense in many real-world scenarios:

* **Privacy**: Users can transact without revealing their exact balances or transaction amounts
* **Regulatory Compliance**: Maintains privacy while allowing for selective disclosure when needed
* **Business Intelligence**: Companies can keep their token holdings private from competitors
* **Personal Privacy**: Individuals can participate in DeFi without exposing their financial position
* **Audit Trail**: All transactions are still recorded on-chain, just in encrypted form

FHE enables these benefits by allowing computations on encrypted data without decryption, ensuring privacy while maintaining the security and transparency of blockchain.

## Project Setup

Before starting this tutorial, ensure you have:

1. Installed the FHEVM hardhat template
2. Set up the OpenZeppelin confidential contracts library

For help with these steps, refer to the following tutorial:

* [Setting up OpenZeppelin confidential contracts](https://github.com/zama-ai/fhevm/blob/main/docs/examples/openzeppelin/openzeppelin/README.md)

## Understanding the architecture

Our confidential token will inherit from several key contracts:

1. `ERC7984` - OpenZeppelin's base for confidential tokens
2. `Ownable2Step` - Access control for minting and administrative functions
3. `ZamaEthereumConfig` - FHE configuration for the Ethereum mainnet or Ethereum Sepolia testnet networks

## The base smart contract

Let's create our confidential token contract in `contracts/ERC7984Example.sol`. This contract will demonstrate the core functionality of ERC7984 tokens.

A few key points about this implementation:

* The contract mints an initial supply with a clear (non-encrypted) amount during deployment
* The initial mint is done once during construction, establishing the token's total supply
* All subsequent transfers will be fully encrypted, preserving privacy
* The contract inherits from ERC7984 for confidential token functionality and Ownable2Step for secure access control

While this example uses a clear initial mint for simplicity, in production you may want to consider:

* Using encrypted minting for complete privacy from genesis
* Implementing a more sophisticated minting schedule
* Overriding some privacy assumptions

## Test workflow

Now let's test the token transfer process. We'll create a test that:

1. Encrypts a transfer amount
2. Sends tokens from owner to recipient
3. Verifies the transfer was successful by checking balance handles

Create a new file `test/ERC7984Example.test.ts` with the following test:

To run the tests, use:

## Advanced features and extensions

The basic ERC7984Example contract provides core functionality, but you can extend it with additional features. For example:

## Minting functions

**Visible Mint** - Allows the owner to mint tokens with a clear amount:

* **When to use**: Prefer this for public/tokenomics-driven mints where transparency is desired (e.g., scheduled emissions).
* **Privacy caveat**: The minted amount is visible in calldata and events; use `confidentialMint` for privacy.
* **Access control**: Consider replacing `onlyOwner` with role-based access via `AccessControl` (e.g., `MINTER_ROLE`) for multi-signer workflows.
* **Supply caps**: If you need a hard cap, add a check before `_mint` and enforce it consistently for both visible and confidential flows.

**Confidential Mint** - Allows minting with encrypted amounts for enhanced privacy:

* **Inputs**: `encryptedAmount` and `inputProof` are produced off-chain with the SDK. Always validate and revert on malformed inputs.
* **Gas considerations**: Confidential operations cost more gas; batch mints sparingly and prefer fewer larger mints to reduce overhead.
* **Auditing**: While amounts stay private, you still get a verifiable audit trail of mints (timestamps, sender, recipient).
* **Example (Hardhat SDK)**:

## Burning functions

**Visible Burn** - Allows the owner to burn tokens with a clear amount:

**Confidential Burn** - Allows burning with encrypted amounts:

* **Authorization**: Burning from arbitrary accounts is powerful; consider stronger controls (roles, multisig, timelocks) or user-consented burns.
* **Event strategy**: Decide whether to emit custom events revealing intent (not amounts) for better observability and offchain indexing.
* **Error surfaces**: Expect balance/allowance-like failures if encrypted amount exceeds balance; test both success and revert paths.
* **Example (Hardhat SDK)**:

## Total supply visibility

If you want the owner to be able to view the total supply (useful for administrative purposes):

* **What this does**: Grants the `owner` permission to decrypt the latest total supply handle after every state-changing update.
* **Operational model**: The owner can call `confidentialTotalSupply()` and use their off-chain key material to decrypt the returned handle.
* **Security considerations**:

  + If ownership changes, ensure only the new owner can decrypt going forward. With `Ownable2Step`, this function will automatically allow the current `owner()`.
  + Be mindful of compliance: granting supply visibility may be considered privileged access; document who holds the key and why.
* **Alternatives**: If you want organization-wide access, grant via a dedicated admin contract that holds decryption authority instead of a single EOA.


Last updated 1 month ago

---


# ERC7984 to ERC20 Wrapper

Source: https://docs.zama.org/protocol/examples/openzeppelin-confidential-contracts/erc7984/erc7984erc20wrappermock

This example demonstrates how to wrap between the ERC20 token into a ERC7984 token using OpenZeppelin's smart contract library powered by ZAMA's FHEVM.

To run this example correctly, make sure the files are placed in the following directories:

* `.sol` file → `<your-project-root-dir>/contracts/`
* `.ts` file → `<your-project-root-dir>/test/`

This ensures Hardhat can compile and test your contracts as expected.

ERC7984ERC20WrapperExample.sol

Copy

```
// SPDX-License-Identifier: BSD-3-Clause-Clear
pragma solidity ^0.8.27;

import {ZamaEthereumConfig} from "@fhevm/solidity/config/ZamaConfig.sol";
import {IERC20} from "@openzeppelin/contracts/interfaces/IERC20.sol";
import {ERC7984ERC20Wrapper, ERC7984} from "@openzeppelin/confidential-contracts/token/ERC7984/extensions/ERC7984ERC20Wrapper.sol";

contract ERC7984ERC20WrapperExample is ERC7984ERC20Wrapper, ZamaEthereumConfig {
    constructor(
        IERC20 token,
        string memory name,
        string memory symbol,
        string memory uri
    ) ERC7984ERC20Wrapper(token) ERC7984(name, symbol, uri) {}
}
```


Last updated 23 days ago

---


# Swap ERC7984 to ERC20

Source: https://docs.zama.org/protocol/examples/openzeppelin-confidential-contracts/erc7984/swaperc7984toerc20

This example demonstrates how to swap between a confidential token - the ERC7984 and the ERC20 tokens using OpenZeppelin's smart contract library powered by ZAMA's FHEVM.

To run this example correctly, make sure the files are placed in the following directories:

* `.sol` file → `<your-project-root-dir>/contracts/`
* `.ts` file → `<your-project-root-dir>/test/`

This ensures Hardhat can compile and test your contracts as expected.

SwapERC7984ToERC20.sol

Copy

```
// SPDX-License-Identifier: BSD-3-Clause-Clear
pragma solidity ^0.8.24;

import {FHE, externalEuint64, euint64} from "@fhevm/solidity/lib/FHE.sol";
import {IERC20} from "@openzeppelin/contracts/interfaces/IERC20.sol";
import {SafeERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import {IERC7984} from "@openzeppelin/confidential-contracts/interfaces/IERC7984.sol";

contract SwapERC7984ToERC20 {
    error SwapERC7984ToERC20InvalidGatewayRequest(uint256 requestId);

    mapping(uint256 requestId => address) private _receivers;
    IERC7984 private _fromToken;
    IERC20 private _toToken;

    constructor(IERC7984 fromToken, IERC20 toToken) {
        _fromToken = fromToken;
        _toToken = toToken;
    }

    function SwapERC7984ToERC20(externalEuint64 encryptedInput, bytes memory inputProof) public {
        euint64 amount = FHE.fromExternal(encryptedInput, inputProof);
        FHE.allowTransient(amount, address(_fromToken));
        euint64 amountTransferred = _fromToken.confidentialTransferFrom(msg.sender, address(this), amount);

        bytes32[] memory cts = new bytes32[](1);
        cts[0] = euint64.unwrap(amountTransferred);
        uint256 requestID = FHE.requestDecryption(cts, this.finalizeSwap.selector);

        // register who is getting the tokens
        _receivers[requestID] = msg.sender;
    }

    function finalizeSwap(uint256 requestID, uint64 amount, bytes[] memory signatures) public virtual {
        FHE.checkSignatures(requestID, signatures);
        address to = _receivers[requestID];
        require(to != address(0), SwapERC7984ToERC20InvalidGatewayRequest(requestID));
        delete _receivers[requestID];

        if (amount != 0) {
            SafeERC20.safeTransfer(_toToken, to, amount);
        }
    }
}
```


Last updated 23 days ago

---


# Swap ERC7984 to ERC7984

Source: https://docs.zama.org/protocol/examples/openzeppelin-confidential-contracts/erc7984/swaperc7984toerc7984

This example demonstrates how to swap between a confidential token - the ERC7984 and the ERC20 tokens using OpenZeppelin's smart contract library powered by ZAMA's FHEVM.

To run this example correctly, make sure the files are placed in the following directories:

* `.sol` file → `<your-project-root-dir>/contracts/`
* `.ts` file → `<your-project-root-dir>/test/`

This ensures Hardhat can compile and test your contracts as expected.

SwapERC7984ToERC20.sol

Copy

```
// SPDX-License-Identifier: BSD-3-Clause-Clear
pragma solidity ^0.8.27;

import {FHE, externalEuint64, euint64} from "@fhevm/solidity/lib/FHE.sol";
import {IERC7984} from "@openzeppelin/confidential-contracts/interfaces/IERC7984.sol";

contract SwapERC7984ToERC7984 {
    function swapConfidentialForConfidential(
        IERC7984 fromToken,
        IERC7984 toToken,
        externalEuint64 amountInput,
        bytes calldata inputProof
    ) public virtual {
        require(fromToken.isOperator(msg.sender, address(this)));

        euint64 amount = FHE.fromExternal(amountInput, inputProof);

        FHE.allowTransient(amount, address(fromToken));
        euint64 amountTransferred = fromToken.confidentialTransferFrom(msg.sender, address(this), amount);

        FHE.allowTransient(amountTransferred, address(toToken));
        toToken.confidentialTransfer(msg.sender, amountTransferred);
    }
}
```


Last updated 23 days ago

---


# Library installation and overview

Source: https://docs.zama.org/protocol/examples/openzeppelin-confidential-contracts/openzeppelin

This section contains comprehensive guides and examples for using [OpenZeppelin's confidential smart contracts library](https://github.com/OpenZeppelin/openzeppelin-confidential-contracts) with FHEVM. OpenZeppelin's confidential contracts library provides a secure, audited foundation for building privacy-preserving applications on fully homomorphic encryption (FHE) enabled blockchains.

The library includes implementations of popular standards like ERC20, ERC721, and ERC1155, adapted for confidential computing with FHEVM, ensuring your applications maintain privacy while leveraging battle-tested security patterns.

## Getting Started

This guide will help you set up a development environment for working with OpenZeppelin's confidential contracts and FHEVM.

## Prerequisites

Before you begin, ensure you have the following installed:

* **Node.js** >= 20
* **Hardhat** ^2.24
* **Access to an FHEVM-enabled network** and the Zama gateway/relayer

## Project Setup

1. **Clone the FHEVM Hardhat template repository:**

   Copy

   ```
   git clone https://github.com/zama-ai/fhevm-hardhat-template conf-token
   cd conf-token
   ```
2. **Install project dependencies:**

   Copy

   ```
   npm ci
   ```
3. **Install OpenZeppelin's confidential contracts library:**

   Copy

   ```
   npm i @openzeppelin/confidential-contracts
   ```
4. **Compile the contracts:**

   Copy

   ```
   npm run compile
   ```
5. **Run the test suite:**

   Copy

   ```
   npm test
   ```

## Available Guides

Explore the following guides to learn how to implement confidential contracts using OpenZeppelin's library:

* [**ERC7984 Standard**](/protocol/examples/openzeppelin-confidential-contracts/erc7984) - Learn about the ERC7984 standard for confidential tokens
* [**ERC7984 Tutorial**](/protocol/examples/openzeppelin-confidential-contracts/erc7984/erc7984-tutorial) - Step-by-step tutorial for implementing ERC7984 tokens
* [**ERC7984 to ERC20 Wrapper**](/protocol/examples/openzeppelin-confidential-contracts/erc7984/erc7984erc20wrappermock) - Convert between confidential and public token standards
* [**Swap ERC7984 to ERC20**](/protocol/examples/openzeppelin-confidential-contracts/erc7984/swaperc7984toerc20) - Implement cross-standard token swapping
* [**Swap ERC7984 to ERC7984**](/protocol/examples/openzeppelin-confidential-contracts/erc7984/swaperc7984toerc7984) - Confidential token-to-token swapping
* [**Vesting Wallet**](/protocol/examples/openzeppelin-confidential-contracts/vesting-wallet) - Implement confidential token vesting mechanisms


Last updated 3 months ago

---


# Vesting Wallet

Source: https://docs.zama.org/protocol/examples/openzeppelin-confidential-contracts/vesting-wallet

This example demonstrates how to create a vesting wallet using OpenZeppelin's smart contract library powered by ZAMA's FHEVM.

`VestingWalletConfidential` receives `ERC7984` tokens and releases them to the beneficiary according to a confidential, linear vesting schedule.

To run this example correctly, make sure the files are placed in the following directories:

* `.sol` file → `<your-project-root-dir>/contracts/`
* `.ts` file → `<your-project-root-dir>/test/`

This ensures Hardhat can compile and test your contracts as expected.

VestingWalletExample.sol

VestingWalletExample.test.ts

VestingWalletExample.fixture.ts

Copy

```
// SPDX-License-Identifier: BSD-3-Clause-Clear
pragma solidity ^0.8.24;

import {FHE, ebool, euint64, euint128} from "@fhevm/solidity/lib/FHE.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {ReentrancyGuardTransient} from "@openzeppelin/contracts/utils/ReentrancyGuardTransient.sol";
import {ZamaEthereumConfig} from "@fhevm/solidity/config/ZamaConfig.sol";
import {IERC7984} from "../interfaces/IERC7984.sol";

/**
 * @title VestingWalletExample
 * @dev A simple example demonstrating how to create a vesting wallet for ERC7984 tokens
 * 
 * This contract shows how to create a vesting wallet that receives ERC7984 tokens
 * and releases them to the beneficiary according to a confidential, linear vesting schedule.
 * 
 * This is a non-upgradeable version for demonstration purposes.
 */
contract VestingWalletExample is Ownable, ReentrancyGuardTransient, ZamaEthereumConfig {
    mapping(address token => euint128) private _tokenReleased;
    uint64 private _start;
    uint64 private _duration;

    /// @dev Emitted when releasable vested tokens are released.
    event VestingWalletConfidentialTokenReleased(address indexed token, euint64 amount);

    constructor(
        address beneficiary,
        uint48 startTimestamp,
        uint48 durationSeconds
    ) Ownable(beneficiary) {
        _start = startTimestamp;
        _duration = durationSeconds;
    }

    /// @dev Timestamp at which the vesting starts.
    function start() public view virtual returns (uint64) {
        return _start;
    }

    /// @dev Duration of the vesting in seconds.
    function duration() public view virtual returns (uint64) {
        return _duration;
    }

    /// @dev Timestamp at which the vesting ends.
    function end() public view virtual returns (uint64) {
        return start() + duration();
    }

    /// @dev Amount of token already released
    function released(address token) public view virtual returns (euint128) {
        return _tokenReleased[token];
    }

    /**
     * @dev Getter for the amount of releasable `token` tokens. `token` should be the address of an
     * {IERC7984} contract.
     */
    function releasable(address token) public virtual returns (euint64) {
        euint128 vestedAmount_ = vestedAmount(token, uint48(block.timestamp));
        euint128 releasedAmount = released(token);
        ebool success = FHE.ge(vestedAmount_, releasedAmount);
        return FHE.select(success, FHE.asEuint64(FHE.sub(vestedAmount_, releasedAmount)), FHE.asEuint64(0));
    }

    /**
     * @dev Release the tokens that have already vested.
     *
     * Emits a {VestingWalletConfidentialTokenReleased} event.
     */
    function release(address token) public virtual nonReentrant {
        euint64 amount = releasable(token);
        FHE.allowTransient(amount, token);
        euint64 amountSent = IERC7984(token).confidentialTransfer(owner(), amount);

        // This could overflow if the total supply is resent `type(uint128).max/type(uint64).max` times. This is an accepted risk.
        euint128 newReleasedAmount = FHE.add(released(token), amountSent);
        FHE.allow(newReleasedAmount, owner());
        FHE.allowThis(newReleasedAmount);
        _tokenReleased[token] = newReleasedAmount;
        emit VestingWalletConfidentialTokenReleased(token, amountSent);
    }

    /**
     * @dev Calculates the amount of tokens that have been vested at the given timestamp.
     * Default implementation is a linear vesting curve.
     */
    function vestedAmount(address token, uint48 timestamp) public virtual returns (euint128) {
        return _vestingSchedule(FHE.add(released(token), IERC7984(token).confidentialBalanceOf(address(this))), timestamp);
    }

    /// @dev This returns the amount vested, as a function of time, for an asset given its total historical allocation.
    function _vestingSchedule(euint128 totalAllocation, uint48 timestamp) internal virtual returns (euint128) {
        if (timestamp < start()) {
            return euint128.wrap(0);
        } else if (timestamp >= end()) {
            return totalAllocation;
        } else {
            return FHE.div(FHE.mul(totalAllocation, (timestamp - start())), duration());
        }
    }
}
```


Last updated 1 month ago

---


# Integration guide for wallets

Source: https://docs.zama.org/protocol/examples/openzeppelin-confidential-contracts/wallet-guide

This guide is for wallet and dApp developers who want to support confidential tokens on Zama Protocol. It focuses on ERC-7984 wallet flows: showing balances (user decryption) and sending transfers (encrypted inputs). For deeper SDK details, follow the [Relayer SDK guide](https://docs.zama.org/protocol/relayer-sdk-guides/).

By the end of this guide, you will be able to:

* Understand [Zama Protocol](https://github.com/zama-ai/fhevm/blob/main/docs/protocol/architecture/overview.md) at a high-level.
* Build ERC-7984 confidential token transfers using encrypted inputs.
* Display ERC-7984 confidential token balances.

## **Core concepts in this guide**

While building support for ERC-7984 confidential tokens in your wallet/app, you might come across the following terminology related to [various parts of the Zama Protocol](https://github.com/zama-ai/fhevm/blob/main/docs/protocol/architecture/overview.md). A brief explanation of common terms you might encounter are:

* **FHEVM**: Zama’s [FHEVM library](https://github.com/zama-ai/fhevm/blob/main/docs/protocol/architecture/library.md) that supports computations on encrypted values. Encrypted values are represented on‑chain as **ciphertext handles** (bytes32).
* **Host chain**: The EVM network your users connect to in a wallet with confidential smart contracts. Example: Ethereum / Ethereum Sepolia.
* **Gateway chain**: Zama’s Arbitrum L3 [Gateway chain](https://github.com/zama-ai/fhevm/blob/main/docs/protocol/architecture/gateway.md) that coordinates FHE encryptions/decryptions.
* **Relayer**: Off‑chain [Relayer](https://github.com/zama-ai/fhevm/blob/main/docs/protocol/architecture/relayer_oracle.md) that registers encrypted inputs, coordinate decryptions, and return results to users or contracts. Wallets and dApps talk to the Relayer via the JavaScript SDK.
* **ACL:** Access control for ciphertext handles. Contracts grant per‑address permissions so a user can read data they should have access to.

## Wallet integration at a glance

At a high-level, to integrate Zama Protocol into a wallet, you do **not** need to run FHE infrastructure. You can interact with the Zama Protocol using [Relayer SDK](https://docs.zama.org/protocol/relayer-sdk-guides) in your wallet or app. These are the steps at a high-level:

1. **Relayer SDK initialisation** in web app, browser extension, or mobile app. Follow the [setup guide for Relayer SDK](https://docs.zama.org/protocol/relayer-sdk-guides/development-guide/webapp). In browser contexts, importing the library via the CDN links is easiest. Alternatively, do this by importing the `@zama-fhe/relayer-sdk` NPM package.
2. [Configure and initialise settings](https://docs.zama.org/protocol/relayer-sdk-guides/fhevm-relayer/initialization) for the library.
3. **Confidential token (ERC-7984) basics**:

   * Show encrypted balances using **user decryption**.
   * Build **transfers** using encrypted inputs. Refer to [OpenZeppelin’s ERC-7984 token guide](https://docs.openzeppelin.com/confidential-contracts/token).
   * Manage **operators** for delegated transfers with an expiry, including clear revoke UX.

## **What wallets should support**

* **Transfers**: Support the ERC-7984 transfer variants documented by OpenZeppelin, including forms that use an input proof and optional receiver callbacks.
* **Operators**: Operators can move any amount during an active window. Your UX must capture an expiry, show risk clearly, and make revoke easy.
* **Events and metadata**: Names and symbols behave like conventional tokens, but on-chain amounts remain encrypted. Render user-specific amounts after user decryption.

## Quick start: ERC-7984 example app

To see these concepts in action, check out the [ERC-7984 demo](https://github.com/zama-ai/dapps/tree/main/packages/erc7984example) from the [zama-ai/dapps](https://github.com/zama-ai/dapps) Github repository.

The demo shows how a frontend or wallet app:

1. [**Register encrypted inputs**](https://docs.zama.org/protocol/relayer-sdk-guides/fhevm-relayer/input) for contract calls such as confidential token transfers.
2. Request [**User decryption**](https://docs.zama.org/protocol/relayer-sdk-guides/fhevm-relayer/decryption/user-decryption) so users can view private data like balances.

## Run locally

1. Clone the [zama-ai/dapps](https://github.com/zama-ai/dapps) Github repository
2. Install dependencies and deploy a local Hardhat chain

1. Navigate to the [ERC-7984 demo](https://github.com/zama-ai/dapps/tree/main/packages/erc7984example) folder in the cloned repo

1. Run the demo application on local Hardhat chain

## Steps demonstrated by the ERC-7984 demo app

**Step 1**: On initially logging in and connect a wallet, a user’s confidential token balances are not yet visible/decrypted.

![](https://docs.zama.org/protocol/~gitbook/image?url=https%3A%2F%2F1085519131-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FX08b6UDQsduF6eJZjCJy%252Fuploads%252Fgit-blob-a1b146806145e2ef2c719dfabcbf5fc1703452dc%252Fwallet-guide-1.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=af95e127&sv=2)

Connect wallet to demo app

**Step 2**: User can now sign and fetch their decrypted ERC-7984 confidential token balance. Balances are stored as ciphertext handles. To display a user’s balance, read the balance handle from your token and [perform **user decryption**](https://docs.zama.ai/protocol/relayer-sdk-guides/v0.1/fhevm-relayer/decryption/user-decryption) with an EIP-712-authorised session in the wallet. Ensure the token grants ACL permission to the user before decrypting.

![](https://docs.zama.org/protocol/~gitbook/image?url=https%3A%2F%2F1085519131-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FX08b6UDQsduF6eJZjCJy%252Fuploads%252Fgit-blob-d0ad6390b1c2629a44dfcbbb5b7942a986f669c0%252Fwallet-guide-2.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=38284fe7&sv=2)

Sign user decryption request

![](https://docs.zama.org/protocol/~gitbook/image?url=https%3A%2F%2F1085519131-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FX08b6UDQsduF6eJZjCJy%252Fuploads%252Fgit-blob-214efbb3c7230dbf3fe10c4fb53b52c80fd377e3%252Fwallet-guide-3.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=eeae730e&sv=2)

View confidential token balance

**Step 3**: User chooses ERC-7984 confidential token amount to send, which is encrypted, signed and sent to destination address. Follow [**OpenZeppelin’s ERC-7984 transfer documentation**](https://docs.openzeppelin.com/confidential-contracts/token#transfer) for function variants and receiver callbacks. Amounts are passed as encrypted inputs that your wallet prepares with the Relayer SDK.

![](https://docs.zama.org/protocol/~gitbook/image?url=https%3A%2F%2F1085519131-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FX08b6UDQsduF6eJZjCJy%252Fuploads%252Fgit-blob-77d4ac8ce16742b4c15ed875d59d3d856b57c21a%252Fwallet-guide-4.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=74e45a1&sv=2)

Send confidential tokens

## **UI and UX recommendations**

* **Caching**: Cache decrypted values client‑side for the session lifetime. Offer a refresh action that repeats the flow.
* **Permissions:** treat user decryption as a permission grant with scope and duration. Show which contracts are included and when access expires.
* **Indicators:** use distinct icons or badges for encrypted amounts. Avoid showing zero when a value is simply undisclosed.
* **Operator visibility**: always show current operator approvals with expiry and a one-tap revoke
* **Failure modes:** differentiate between decryption denied, missing ACL grant, and expired decryption session. Offer guided recovery actions.

## **Testing and environments**

* **Testnet configuration:** Start with the SDK’s built‑in Sepolia configuration or a local Hardhat network. Swap to other supported networks by replacing the config object. Keep chain selection in a single source of truth in your app.
* **Mocks:** for unit tests, prefer SDK mocked mode or local fixtures that bypass the Gateway but maintain identical call shapes for your UI logic.

## Further reading

* Detailed [**confidential contracts guide from OpenZeppelin**](https://docs.openzeppelin.com/confidential-contracts) (besides ERC-7984)
* [**ERC-7984 tutorial and examples**](/protocol/examples/openzeppelin-confidential-contracts/openzeppelin)

[PreviousVesting Wallet](/protocol/examples/openzeppelin-confidential-contracts/vesting-wallet)

Last updated 1 month ago

---


# FHE on blockchain

Source: https://docs.zama.org/protocol/protocol/overview

This section explains in depth the Zama Confidential Blockchain Protocol (Zama Protocol) and demonstrates how it can bring encrypted computation to smart contracts using Fully Homomorphic Encryption (FHE).

FHEVM is the core technology that powers the Zama Protocol. It is composed of the following key components.

![](https://docs.zama.org/protocol/~gitbook/image?url=https%3A%2F%2F4279888132-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F06EvE9BR7kBlHwVGcFT8%252Fuploads%252Fgit-blob-64b4536b1a1605b9ccd2d0293a7df06aa358b8d3%252FFHEVM.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=d805f1b6&sv=2)

* [**FHEVM Solidity library**](/protocol/protocol/overview/library): Enables developers to write confidential smart contracts in plain Solidity using encrypted data types and operations.
* [**Host contracts**](/protocol/protocol/overview/hostchain) : Trusted on-chain contracts deployed on EVM-compatible blockchains. They manage access control and trigger off-chain encrypted computation.
* [**Coprocessors**](/protocol/protocol/overview/coprocessor) – Decentralized services that verify encrypted inputs, run FHE computations, and commit results.
* [**Gateway**](/protocol/protocol/overview/gateway) **–** The central orchestrator of the protocol. It validates encrypted inputs, manages access control lists (ACLs), bridges ciphertexts across chains, and coordinates coprocessors and the KMS.
* [**Key Management Service (KMS)**](/protocol/protocol/overview/kms) – A threshold MPC network that generates and rotates FHE keys, and handles secure, verifiable decryption.
* [**Relayer & oracle**](/protocol/protocol/overview/relayer_oracle) – A lightweight off-chain service that helps users interact with the Gateway by forwarding encryption or decryption requests.


Last updated 2 months ago

---


# Coprocessor

Source: https://docs.zama.org/protocol/protocol/overview/coprocessor

This document explains one of the key components of the Zama Protocol - Coprocessor, the Zama Protocol’s off-chain computation engine.

## What is the Coprocessor?

Coprocessor performs the heavy cryptographic operations—specifically, fully homomorphic encryption (FHE) computations—on behalf of smart contracts that operate on encrypted data. Acting as a decentralized compute layer, the coprocessor bridges symbolic on-chain logic with real-world encrypted execution.

Coprocessor works together with the Gateway, verifying encrypted inputs, executing FHE instructions, and maintaining synchronization of access permissions, in particular:

* Listens to events emitted by host chains and the Gateway.
* Executes FHE computations (`add`, `mul`, `div`, `cmp`, etc.) on ciphertexts.
* Validates encrypted inputs and ZK proofs of correctness.
* Maintains and updates a replica of the host chain’s Access Control Lists (ACLs).
* Stores and serves encrypted data for decryption or bridging.

Each coprocessor independently executes tasks and publishes verifiable results, enabling a publicly auditable and horizontally scalable confidential compute infrastructure .

## Responsibilities of the Coprocessor

## Encrypted input verification

When users submit encrypted values to the Gateway, each coprocessor:

* Verifies the associated Zero-Knowledge Proof of Knowledge (ZKPoK).
* Extracts and unpacks individual ciphertexts from a packed submission.
* Stores the ciphertexts under derived handles.
* Signs the verified handles, embedding user and contract metadata.
* Sends the signed data back to the Gateway for consensus.

This ensures only valid, well-formed encrypted values enter the system .

## FHE computation execution

When a smart contract executes a function over encrypted values, the on-chain logic emits symbolic computation events.
Each coprocessor:

* Reads these events from the host chain node it runs.
* Fetches associated ciphertexts from its storage.
* Executes the required FHE operations using the TFHE-rs library (e.g., add, mul, select).
* Stores the resulting ciphertext under a deterministically derived handle.
* Optionally publishes a commitment (digest) of the ciphertext to the Gateway for verifiability.

This offloads expensive computation from the host chain while maintaining full determinism and auditability .

## ACL replication

Coprocessors replicate the Access Control List (ACL) logic from host contracts. They:

* Listen to Allowed and AllowedForDecryption events.
* Push updates to the Gateway.

This ensures decentralized enforcement of access rights, enabling proper handling of decryptions, bridges, and contract interactions .

## Ciphertext commitment

To ensure verifiability and mitigate misbehavior, each coprocessor:

* Commits to ciphertext digests (via hash) when processing Allowed events.
* Publishes these commitments to the Gateway.
* Enables external verification of FHE computations.

This is essential for fraud-proof mechanisms and eventual slashing of malicious or faulty operators .

## Bridging & decryption support

Coprocessors assist in:

* Bridging encrypted values between host chains by generating new handles and signatures.
* Preparing ciphertexts for public and user decryption using operations like Switch-n-Squash to normalize ciphertexts for the KMS.

These roles help maintain cross-chain interoperability and enable privacy-preserving data access for users and smart contracts .

## Security and trust assumptions

Coprocessors are designed to be minimally trusted and publicly verifiable. Every FHE computation or input verification they perform is accompanied by a cryptographic commitment (hash digest) and a signature, allowing anyone to independently verify correctness.

The protocol relies on a majority-honest assumption: as long as more than 50% of coprocessors are honest, results are valid. The Gateway aggregates responses and accepts outputs only when a majority consensus is reached.

To enforce honest behavior, coprocessors must stake $ZAMA tokens and are subject to slashing if caught misbehaving—either through automated checks or governance-based fraud proofs.

This model ensures correctness through transparency, resilience through decentralization, and integrity through economic incentives.

## Architecture & Scalability

The coprocessor architecture includes:

* Event listeners for host chains and the Gateway
* A task queue for FHE and ACL update jobs
* Worker threads that process tasks in parallel
* A public storage layer (e.g., S3) for ciphertext availability

This modular setup supports horizontal scaling: adding more workers or machines increases throughput. Symbolic computation and delayed execution also ensure low gas costs on-chain .


Last updated 2 months ago

---


# Gateway

Source: https://docs.zama.org/protocol/protocol/overview/gateway

This document explains one of the key components of the Zama Protocol - Gateway, the central orchestrator within Zama’s FHEVM protocol, coordinates interactions between users, host chains, coprocessors, and the Key Management Service (KMS), ensuring that encrypted data flows securely and correctly through the system.

## What is the Gateway?

The Gateway is a specialized blockchain component (implemented as an Arbitrum rollup) responsible for managing:

* Validation of encrypted inputs from users and applications.
* Bridging of encrypted ciphertexts across different blockchains.
* Decryption orchestration via KMS nodes.
* Consensus enforcement among decentralized coprocessors.
* Staking and reward distribution to operators participating in FHE computations.

It is designed to be trust-minimized: computations are independently verifiable, and no sensitive data or decryption keys are stored on the Gateway itself.

## Responsibilities of the Gateway

## Encrypted input validation

The Gateway ensures that encrypted values provided by users are well-formed and valid. It does this by:

* Accepting encrypted inputs along with Zero-Knowledge Proofs of Knowledge (ZKPoKs).
* Emitting verification events for coprocessors to validate.
* Aggregating signatures from a majority of coprocessors to generate attestations, which can then be used on-chain as trusted external values.

## Access Control coordination

The Gateway maintains a synchronized copy of Access Control Lists (ACLs) from host chains, enabling it to independently determine if decryption or computation rights should be granted for a ciphertext. This helps enforce:

* Access permissions (allow)
* Public decryption permissions (allowForDecryption)

These ACL updates are replicated by coprocessors and pushed to the Gateway for verification and enforcement.

## Decryption orchestration

When a smart contract or user requests the decryption of an encrypted value:

1. The Gateway verifies ACL permissions.
2. It then triggers the KMS to decrypt (either publicly or privately).
3. Once the KMS returns signed results, the Gateway emits events that can be picked up by an oracle (for smart contract decryption) or returned to the user (for private decryption).

This ensures asynchronous, secure, and auditable decryption without the Gateway itself knowing the plaintext.

## Cross-chain bridging

The Gateway also handles bridging of encrypted handles between host chains. It:

* Verifies access rights on the source chain using its ACL copy.
* Requests the coprocessors to compute new handles for the target chain.
* Collects signatures from coprocessors.

Issues attestations allowing these handles to be used on the destination chain.

## Consensus and slashing enforcement

The Gateway enforces consensus across decentralized coprocessors and KMS nodes. If discrepancies occur:

* Coprocessors must provide commitments to ciphertexts.
* Fraudulent or incorrect behavior can be challenged and slashed.
* Governance mechanisms can be triggered for off-chain verification when necessary.

## Protocol administration

The Gateway runs smart contracts that administer:

* Operator and participant registration (coprocessors, KMS nodes, host chains)
* Key management and rotation
* Bridging logic
* Input validation and decryption workflows

## Security and trust assumptions

The Gateway is designed to operate without requiring trust:

* It does not perform any computation itself—it merely orchestrates and validates.
* All actions are signed, and cryptographic verification is built into every step.

The protocol assumes no trust in the Gateway for security guarantees—it can be fully audited and replaced if necessary.


Last updated 2 months ago

---


# Host contracts

Source: https://docs.zama.org/protocol/protocol/overview/hostchain

This document explains one of the key components of the Zama Protocol - Host contracts.

## What are host contracts?

Host contracts are smart contracts deployed on any supported blockchain (EVM or non-EVM) that act as trusted bridges between on-chain applications and the FHEVM protocol. They serve as the minimal and foundational interface that confidential smart contracts use to:

* Interact with encrypted data (handles)
* Perform access control operations
* Emit events for the off-chain components (coprocessors, Gateway)

These host contracts are used indirectly by developers via the FHEVM Solidity library, abstracting away complexity and integrating smoothly into existing workflows.

## Responsibilities of host contracts

## Trusted interface layer

Host contracts are the only on-chain components that:

* Maintain and enforce Access Control Lists (ACLs) for ciphertexts.
* Emit events that trigger coprocessor execution.
* Validate access permissions (persistent, transient, or decryption-related).

They are effectively the on-chain authority for:

* Who is allowed to access a ciphertext
* When and how they can use it
* These ACLs are mirrored on the Gateway for off-chain enforcement and bridging.

## Access Control API

Host contracts expose access control logic via standardized function calls (wrapped by the FHEVM library):

* `allow(handle, address)`: Grants persistent access.
* `allowTransient(handle, address)`: Grants temporary access for a single transaction.
* `allowForDecryption(handle)`: Marks a handle as publicly decryptable.
* `isAllowed(handle, address)`: Returns whether a given address has access.
* `isSenderAllowed(handle)`: Checks if msg.sender is allowed to use a handle.

They also emit:

* `Allowed(handle, address)`
* `AllowedForDecryption(handle)`

These events are crucial for triggering coprocessor state updates and ensuring proper ACL replication to the Gateway.

→ See the full guide of [ACL](https://docs.zama.ai/protocol/solidity-guides/smart-contract/acl).

## Security role

Although the FHE computation happens off-chain, host contracts play a critical role in protocol security by:

* Enforcing ACL-based gating
* Ensuring only authorized contracts and users can decrypt or use a handle
* Preventing misuse of encrypted data (e.g., computation without access)

Access attempts without proper authorization are rejected at the smart contract level, protecting both the integrity of confidential operations and user privacy.


Last updated 6 months ago

---


# KMS

Source: https://docs.zama.org/protocol/protocol/overview/kms

This document explains one of the key components of the Zama Protocol - The Key Management Service (KMS), responsible for the secure generation, management, and usage of FHE keys needed to enable confidential smart contracts.

## What is the KMS?

The KMS is a decentralized network of several nodes (also called "parties") that run an MPC (Multi-Party Computation) protocol:

* Securely generate global FHE keys
* Decrypt ciphertexts securely for public and user-targeted decryptions
* Support zero-knowledge proof infrastructure
* Manage key lifecycles with NIST compliance

It works entirely off-chain, but is orchestrated through the Gateway, which initiates and tracks all key-related operations. This separation of powers ensures strong decentralization and auditability.

## Key responsibilities

## FHE threshold key generation

* The KMS securely generates a global public/private key pair used across all host chains.
* This key enables composability — encrypted data can be shared between contracts and chains.
* The private FHE key is never directly accessible by a single party; instead, it is secret-shared among the MPC nodes.

The system follows the NIST SP 800-57 key lifecycle model, managing key states such as Active, Suspended, Deactivated,and Destroyed to ensure proper rotation and forward security.

## Threshold Decryption via MPC

The KMS performs decryption using a threshold decryption protocol — at least a minimum number of MPC parties (e.g., 9 out of 13) must participate in the protocol to robustly decrypt a value.

* This protects against compromise: no individual party has access to the full key. And adversary would need to control more than the threshold of KMS nodes to influence the system.
* The protocol supports both:

  + Public decryption (e.g., for smart contracts)
  + User decryption (privately returned, re-encrypted only for the user to access)

All decryption operation outputs are signed by each node and the output can be verified on-chain for full auditability.

## ZK Proof support

The KMS generates Common Reference Strings (CRS) needed to validate Zero-Knowledge Proofs of Knowledge (ZKPoK) when users submit encrypted values.

This ensures encrypted inputs are valid and well-formed, and that a user has knowledge of the plaintext contained in the submitted input ciphertext.

## Security architecture

## MPC-based key sharing

* The KMS currently uses 13 MPC nodes, operated by different reputable organizations.
* Private keys are split using threshold secret sharing.
* Communication between nodes are secured using mTLS with gRPC.

## Honest majority assumption

* The protocol is robust against malicious actors as long as at most 1/3 of the nodes act maliciously.
* It supports guaranteed output delivery even if some nodes are offline or misbehaving.

## Secure execution environments

Each MPC node runs by default inside an AWS Nitro Enclave, a secure execution environment that prevents even node operators from accessing their own key shares. This design mitigates insider risks, such as unauthorized key reconstruction or selling of shares.

## Auditable via gateway

* All operations are broadcast through the Gateway and recorded as blockchain events.
* KMS responses are signed, allowing smart contracts and users to verify results cryptographically.

## Key lifecycle management

The KMS adheres to a formal key lifecycle, as per NIST SP 800-57:

State

Description

Pre-activation

Key is created but not in use.

Active

Key is used for encryption and decryption.

Suspended

Temporarily replaced during rotation. Still usable for decryption.

Deactivated

Archived; only used for decryption.

Compromised

Flagged for misuse; only decryption allowed.

Destroyed

Key material is deleted permanently.

The KMS supports key switching using FHE, allowing ciphertexts to be securely transferred between keys during rotation. This maintains interoperability across key updates.

## Backup & recovery

In addition to robustness through MPC, the KMS also offers a custodial backup system:

* Each MPC node splits its key share into encrypted fragments, distributing them to independent custodians.
* If a share is lost, a quorum of custodians can collaboratively restore it, ensuring recovery even if several MPC nodes are offline.
* This approach guarantees business continuity and resilience against outages.
* All recovery operations require a quorum of operators and are fully auditable on-chain.

## Workflow example: Public decryption

1. A smart contract requests decryption via an oracle.
2. The Gateway verifies permissions (i.e. that the contract is allowed to decrypt the ciphertext) and emits an event.
3. KMS parties retrieve the ciphertext, verify it, and run the MPC decryption protocol to jointly compute the plaintext and sign their result.
4. Once a quorum agrees on the plaintext result, it is published (with signatures).
5. The oracle posts the plaintext back on-chain and contracts can verify the authenticity using the KMS signatures.


Last updated 6 months ago

---


# FHE library

Source: https://docs.zama.org/protocol/protocol/overview/library

This document offers a high-level overview of the **FHEVM library**, helping you understand how it fits into the broader Zama Protocol. To learn how to use it in practice, see the [Solidity Guides](https://docs.zama.ai/protocol/solidity-guides).

## What is FHEVM library?

The FHEVM library enables developers to build smart contracts that operate on encrypted data—without requiring any knowledge of cryptography.

It extends the standard Solidity development flow with:

* Encrypted data types
* Arithmetic, logical, and conditional operations on encrypted values
* Fine-grained access control
* Secure input handling and attestation support

This library serves as an **abstraction layer** over Fully Homomorphic Encryption (FHE) and interacts seamlessly with off-chain components such as the **Coprocessors** and the **Gateway**.

## Key features

## Encrypted data types

The library introduces encrypted variants of common Solidity types, implemented as user-defined value types. Internally, these are represented as `bytes32` handles that point to encrypted values stored off-chain.

Category

Types

Booleans

`ebool`

Unsigned integers

`euint8`, `euint16`, ..., `euint256`

Signed integers

`eint8`, `eint16,` ..., `eint256`

Addresses

`eaddress`

→ See the full guide of [Encrypted data types](https://docs.zama.ai/protocol/solidity-guides/smart-contract/types).

## FHE operations

Each encrypted type supports operations similar to its plaintext counterpart:

* Arithmetic: `add`, `sub`, `mul`, `div`, `rem`, `neg`
* Logic: `and`, `or`, `xor`, `not`
* Comparison: `lt`, `gt`, `le`, `ge`, `eq`, `ne`, `min`, `max`
* Bit manipulation: `shl`, `shr`, `rotl`, `rotr`

These operations are symbolically executed on-chain by generating new handles and emitting events for coprocessors to process the actual FHE computation off-chain.

Example:

→ See the full guide of [Operations on encrypted types](https://docs.zama.ai/protocol/solidity-guides/smart-contract/operations).

## Branching with encrypted Conditions

Direct if or require statements are not compatible with encrypted booleans. Instead, the library provides a `select`operator to emulate conditional logic without revealing which branch was taken:

This preserves confidentiality even in conditional logic.

→ See the full guide of [Branching](https://docs.zama.ai/protocol/solidity-guides/smart-contract/logics/conditions).

## Handling external encrypted inputs

When users want to pass encrypted inputs (e.g., values they’ve encrypted off-chain or bridged from another chain), they provide:

* external values
* A list of coprocessor signatures (attestation)

The function `fromExternal` is used to validate the attestation and extract a usable encrypted handle:

This ensures that only authorized, well-formed ciphertexts are accepted by smart contracts.

→ See the full guide of [Encrypted input](https://docs.zama.ai/protocol/solidity-guides/smart-contract/inputs).

## Access control

The FHE library also exposes methods for managing access to encrypted values using the ACL maintained by host contracts:

* `allow(handle, address)`: Grant persistent access
* `allowTransient(handle, address)`: Grant access for the current transaction only
* `allowForDecryption(handle)`: Make handle publicly decryptable
* `isAllowed(handle, address)`: Check if address has access
* `isSenderAllowed(handle)`: Shortcut for checking msg.sender permissions

These `allow` methods emit events consumed by the coprocessors to replicate the ACL state in the Gateway.

→ See the full guide of [ACL](https://docs.zama.ai/protocol/solidity-guides/smart-contract/acl).

## Pseudo-random encrypted values

The library allows generation of pseudo-random encrypted integers, useful for games, lotteries, or randomized logic:

* `randEuintXX()`
* `randEuintXXBounded`(uint bound)

These are deterministic across coprocessors and indistinguishable to external observers.

→ See the full guide of [Generate random number](https://docs.zama.ai/protocol/solidity-guides/smart-contract/operations/random).


Last updated 6 months ago

---


# Relayer & Oracle

Source: https://docs.zama.org/protocol/protocol/overview/relayer_oracle

This document explains the service interface of the Zama Protocol - Relayer & Oracle.

## What is the Oracle?

The Oracle is an off-chain service that acts on behalf of smart contracts to retrieve decrypted values from the FHEVM protocol.

While the FHEVM protocol’s core components handle encryption, computation, and key management, Oracles and Relayers provide the necessary connectivity between users, smart contracts, and the off-chain infrastructure. They act as lightweight services that interface with the Gateway, enabling smooth interaction with encrypted values—without requiring users or contracts to handle complex integration logic.

These components are not part of the trusted base of the protocol; their actions are fully verifiable, and their misbehavior does not compromise confidentiality or correctness.

## Responsibilities of the Oracle

* Listen for on-chain decryption requests from contracts.
* Forward decryption requests to the Gateway on behalf of the contract.
* Wait for the KMS to produce signed plaintexts via the Gateway.
* Call back the contract on the host chain, passing the decrypted result.

Since the decrypted values are signed by the KMS, the receiving smart contract can verify the result, removing any needto trust the oracle itself.

## Security model of the Oracle

* Oracles are **untrusted**: they can only delay a request, not falsify it.
* All results are signed and verifiable on-chain.

If one oracle fails to respond, another can take over.

Goal: Enable contracts to access decrypted values asynchronously and securely, without embedding decryption logic.

## What is the Relayer?

The Relayer is a user-facing service that simplifies interaction with the Gateway, particularly for encryption and decryption operations that need to happen off-chain.

## Responsibilities of the Relayer

* Send encrypted inputs from the user to the Gateway for registration.
* Initiate user-side decryption requests, including EIP-712 authentication.
* Collect the response from the KMS, re-encrypted under the user’s public key.
* Deliver the ciphertext back to the user, who decrypts it locally in their browser/app.

This allows users to interact with encrypted smart contracts without having to run their own Gateway interface,
validator, or FHE tooling.

## Security model of the Relayer

* Relayers are stateless and **untrusted**.
* All data flows are signed and auditable by the user.
* Users can always run their own relayer or interact with the Gateway directly if needed.

Goal: Make it easy for users to submit encrypted inputs and retrieve private decrypted results without managing infrastructure.

## How they fit in

* Smart contracts use the Oracle to receive plaintext results of encrypted computations via callbacks.
* Users rely on the Relayer to push encrypted values into the system and fetch personal decrypted results, all backed by EIP-712 signatures and FHE key re-encryption.

Together, Oracles and Relayers help bridge the gap between encrypted execution and application usability—without compromising security or decentralization.


Last updated 2 months ago

---


# Roadmap

Source: https://docs.zama.org/protocol/protocol/roadmap

This document gives a preview of the upcoming features of FHEVM. In addition to what's listed here, you can [submit your feature request](https://github.com/zama-ai/fhevm/issues/new) on GitHub.

## Features

Name

Description

ETA

Foundry template

[Forge](https://book.getfoundry.sh/reference/forge/forge)

Q1 '25

## Operations

Name

Function name

Type

ETA

Signed Integers

`eintX`

Coming soon

Add w/ overflow check

`FHE.safeAdd`

Binary, Decryption

Coming soon

Sub w/ overflow check

`FHE.safeSub`

Binary, Decryption

Coming soon

Mul w/ overflow check

`FHE.safeMul`

Binary, Decryption

Coming soon

Random signed int

`FHE.randEintX()`

Random

-

Div

`FHE.div`

Binary

-

Rem

`FHE.rem`

Binary

-

Set inclusion

`FHE.isIn()`

Binary

-

Random encrypted integers that are generated fully on-chain. Currently, implemented as a mockup by using a PRNG in the plain. Not for use in production!


Last updated 2 months ago

---


# CLI

Source: https://docs.zama.org/protocol/relayer-sdk-guides/development-guide/cli

The `fhevm` Command-Line Interface (CLI) tool provides a simple and efficient way to encrypt data for use with the blockchain's Fully Homomorphic Encryption (FHE) system. This guide explains how to install and use the CLI to encrypt integers and booleans for confidential smart contracts.

## Installation

Ensure you have [Node.js](https://nodejs.org/) installed on your system before proceeding. Then, globally install the `@zama-fhe/relayer-sdk` package to enable the CLI tool:

Copy

```
npm install -g @zama-fhe/relayer-sdk
```

Once installed, you can access the CLI using the `relayer` command. Verify the installation and explore available commands using:

Copy

```
relayer help
```

## Encrypting Data

The CLI allows you to encrypt integers and booleans for use in smart contracts. Encryption is performed using the blockchain's FHE public key, ensuring the confidentiality of your data.

## Syntax

Copy

```
relayer encrypt --node <NODE_URL> <CONTRACT_ADDRESS> <USER_ADDRESS> <DATA:TYPE>...
```

* `--node`: Specifies the RPC URL of the blockchain node (e.g., `http://localhost:8545`).
* `<CONTRACT_ADDRESS>`: The address of the contract interacting with the encrypted data.
* `<USER_ADDRESS>`: The address of the user associated with the encrypted data.
* `<DATA:TYPE>`: The data to encrypt, followed by its type:

  + `:64` for 64-bit integers
  + `:1` for booleans

## Example Usage

Encrypt the integer `71721075` (64-bit) and the boolean `1` for the contract at `0x8Fdb26641d14a80FCCBE87BF455338Dd9C539a50` and the user at `0xa5e1defb98EFe38EBb2D958CEe052410247F4c80`:

[PreviousDebugging](/protocol/relayer-sdk-guides/development-guide/webpack)

Last updated 1 month ago

---


# Web applications

Source: https://docs.zama.org/protocol/relayer-sdk-guides/development-guide/webapp

This document guides you through building a web application using the `@zama-fhe/relayer-sdk` library.

## Using directly the library

## Step 1: Setup the library

`@zama-fhe/relayer-sdk` consists of multiple files, including WASM files and WebWorkers, which can make packaging these components correctly in your setup cumbersome. To simplify this process, especially if you're developing a dApp with server-side rendering (SSR), we recommend using our CDN.

## Using UMD CDN

The Zama CDN url format is `https://cdn.zama.org/relayer-sdk-js/<package-version>/relayer-sdk-js.umd.cjs`

Include this line at the top of your project.

Copy

```
<script
  src="https://cdn.zama.org/relayer-sdk-js/0.3.0-8/relayer-sdk-js.umd.cjs"
  type="text/javascript"
></script>
```

In your project, you can use the bundle import if you install `@zama-fhe/relayer-sdk` package:

Copy

```
import {
  initSDK,
  createInstance,
  SepoliaConfig,
} from '@zama-fhe/relayer-sdk/bundle';
```

## Using ESM CDN

If you prefer You can also use the `@zama-fhe/relayer-sdk` as a ES module:

## Using npm package

Install the `@zama-fhe/relayer-sdk` library to your project:

`@zama-fhe/relayer-sdk` uses ESM format. You need to set the [type to "module" in your package.json](https://nodejs.org/api/packages.html#type). If your node project use `"type": "commonjs"` or no type, you can force the loading of the web version by using `import { createInstance } from '@zama-fhe/relayer-sdk/web';`

## Step 2: Initialize your project

To use the library in your project, you need to load the WASM of [TFHE](https://www.npmjs.com/package/tfhe) first with `initSDK`.

## Step 3: Create an instance

Once the WASM is loaded, you can now create an instance.

You can now use your instance to [encrypt parameters](/protocol/relayer-sdk-guides/fhevm-relayer/input), perform [user decryptions](/protocol/relayer-sdk-guides/fhevm-relayer/decryption/user-decryption) or [public decryptions](/protocol/relayer-sdk-guides/fhevm-relayer/decryption/public-decryption).


Last updated 14 days ago

---


# Debugging

Source: https://docs.zama.org/protocol/relayer-sdk-guides/development-guide/webpack

This document provides solutions for common Webpack errors encountered during the development process. Follow the steps below to resolve each issue.

## Can't resolve 'tfhe\_bg.wasm'

**Error message:** `Module not found: Error: Can't resolve 'tfhe_bg.wasm'`

**Cause:** In the codebase, there is a `new URL('tfhe_bg.wasm')` which triggers a resolve by Webpack.

**Possible solutions:** You can add a fallback for this file by adding a resolve configuration in your `webpack.config.js`:

Copy

```
resolve: {
  fallback: {
    'tfhe_bg.wasm': require.resolve('tfhe/tfhe_bg.wasm'),
  },
},
```

## Buffer not defined

**Error message:** `ReferenceError: Buffer is not defined`

**Cause:** This error occurs when the Node.js `Buffer` object is used in a browser environment where it is not natively available.

**Possible solutions:** To resolve this issue, you need to provide browser-compatible fallbacks for Node.js core modules. Install the necessary browserified npm packages and configure Webpack to use these fallbacks.

Copy

```
resolve: {
  fallback: {
    buffer: require.resolve('buffer/'),
    crypto: require.resolve('crypto-browserify'),
    stream: require.resolve('stream-browserify'),
    path: require.resolve('path-browserify'),
  },
},
```

## Issue with importing ESM version

**Error message:** Issues with importing ESM version

**Cause:** With a bundler such as Webpack or Rollup, imports will be replaced with the version mentioned in the `"browser"` field of the `package.json`. This can cause issues with typing.

**Possible solutions:**

* If you encounter issues with typing, you can use the tsconfig.json using TypeScript 5 located in the [fhevm-react-template](https://github.com/zama-ai/fhevm-react-template) repository.
* If you encounter any other issue, you can force import of the browser package.

## Use bundled version

**Error message:** Issues with bundling the library, especially with SSR frameworks.

**Cause:** The library may not bundle correctly with certain frameworks, leading to errors during the build or runtime process.

**Possible solutions:** Use the [prebundled version available](/protocol/relayer-sdk-guides/development-guide/webapp) with `@zama-fhe/relayer-sdk/bundle`. Embed the library with a `<script>` tag and initialize it as shown below:


Last updated 1 month ago

---


# Public decryption

Source: https://docs.zama.org/protocol/relayer-sdk-guides/fhevm-relayer/decryption/public-decryption

This document explains how to perform public decryption of FHEVM ciphertexts. Public decryption is required when you want everyone to see the value in a ciphertext, for example the result of private auction. Public decryption can be done using the Relayer HTTP endpoint.

## HTTP Public Decrypt

Calling the public decryption endpoint of the Relayer can be done easily using the following code snippet.

The total bit length of all ciphertexts being decrypted in a single request must not exceed 2048 bits. Each encrypted type has a specific bit length, for instance `euint8` uses 8 bits and `euint16` uses 16 bits. For the full list of encrypted types and their corresponding bit lengths, refer to the [encrypted types documentation](https://docs.zama.org/protocol/solidity-guides/smart-contract/types#list-of-encrypted-types).

Copy

```
// A list of ciphertexts handles to decrypt
const handles = [
  '0x830a61b343d2f3de67ec59cb18961fd086085c1c73ff0000000000aa36a70000',
  '0x98ee526413903d4613feedb9c8fa44fe3f4ed0dd00ff0000000000aa36a70400',
  '0xb837a645c9672e7588d49c5c43f4759a63447ea581ff0000000000aa36a70700',
];

// The list of decrypted values
// results = {
//    clearValues: {
//      '0x830a61b343d2f3de67ec59cb18961fd086085c1c73ff0000000000aa36a70000': true,
//      '0x98ee526413903d4613feedb9c8fa44fe3f4ed0dd00ff0000000000aa36a70400': 242n,
//      '0xb837a645c9672e7588d49c5c43f4759a63447ea581ff0000000000aa36a70700': '0xfC4382C084fCA3f4fB07c3BCDA906C01797595a8'
//    }
//    abiEncodedClearValues: '0x.....'
//    decryptionProof: '0x.....'
// }
const results: PublicDecryptResults = instance.publicDecrypt(handles);
```

## Onchain Public Decryption Verification

For more details about public decryption and on-chain decryption proof please refer to the on [public decryption page](https://docs.zama.org/protocol/solidity-guides/smart-contract/oracle).


Last updated 16 days ago

---


# User decryption

Source: https://docs.zama.org/protocol/relayer-sdk-guides/fhevm-relayer/decryption/user-decryption

This document explains how to perform user decryption. User decryption is required when you want a user to access their private data without it being exposed to the blockchain.

User decryption in FHEVM enables the secure sharing or reuse of encrypted data under a new public key without exposing the plaintext.

This feature is essential for scenarios where encrypted data must be transferred between contracts, dApps, or users while maintaining its confidentiality.

## When to use user decryption

User decryption is particularly useful for **allowing individual users to securely access and decrypt their private data**, such as balances or counters, while maintaining data confidentiality.

## Overview

The user decryption process involves retrieving ciphertext from the blockchain and performing user-decryption on the client-side. In other words we take the data that has been encrypted by the KMS, decrypt it and encrypt it with the user's private key, so only he can access the information.

This ensures that the data remains encrypted under the blockchain’s FHE key but can be securely shared with a user by re-encrypting it under the user’s NaCl public key.

User decryption is facilitated by the **Relayer** and the **Key Management System (KMS)**. The workflow consists of the following:

1. Retrieving the ciphertext from the blockchain using a contract’s view function.
2. Re-encrypting the ciphertext client-side with the user’s public key, ensuring only the user can decrypt it.

## Step 1: retrieve the ciphertext

To retrieve the ciphertext that needs to be decrypted, you can implement a view function in your smart contract. Below is an example implementation:

Copy

```
import "@fhevm/solidity/lib/FHE.sol";

contract ConfidentialERC20 {
  ...
  function balanceOf(account address) public view returns (euint64) {
    return balances[msg.sender];
  }
  ...
}
```

Here, `balanceOf` allows retrieval of the user’s encrypted balance handle stored on the blockchain. Doing this will return the ciphertext handle, an identifier for the underlying ciphertext.

For the user to be able to user decrypt (also called re-encrypt) the ciphertext value the access control (ACL) needs to be set properly using the `FHE.allow(ciphertext, address)` function in the solidity contract holding the ciphertext.

For more details on the topic please refer to [the ACL documentation](https://docs.zama.org/protocol/solidity-guides/smart-contract/acl). For more details on the topic please refer to [the ACL documentation](https://docs.zama.ai/protocol/solidity-guides/smart-contract/acl).

## Step 2: decrypt the ciphertext

Using those ciphertext handles, user decryption is performed client-side using the `@zama-fhe/relayer-sdk` library. The `userDecrypt` function takes a **list of handles**, allowing you to decrypt multiple ciphertexts in a single request. In this example, provide just one handle. The user needs to have created an instance object prior to that (for more context see [the relayer-sdk setup page](/protocol/relayer-sdk-guides/fhevm-relayer/initialization)).

The total bit length of all ciphertexts being decrypted in a single request must not exceed 2048 bits. Each encrypted type has a specific bit length, for instance `euint8` uses 8 bits and `euint16` uses 16 bits. For the full list of encrypted types and their corresponding bit lengths, refer to the [encrypted types documentation](https://docs.zama.org/protocol/solidity-guides/smart-contract/types#list-of-encrypted-types).


Last updated 16 days ago

---


# Initialization

Source: https://docs.zama.org/protocol/relayer-sdk-guides/fhevm-relayer/initialization

The use of `@zama-fhe/relayer-sdk` requires a setup phase. This consists of the instantiation of the `FhevmInstance`. This object holds all the configuration and methods needed to interact with an FHEVM using a Relayer. It can be created using the following code snippet:

Copy

```
import { createInstance } from '@zama-fhe/relayer-sdk';

const instance = await createInstance({
  // ACL_CONTRACT_ADDRESS (FHEVM Host chain)
  aclContractAddress: '0xf0Ffdc93b7E186bC2f8CB3dAA75D86d1930A433D',
  // KMS_VERIFIER_CONTRACT_ADDRESS (FHEVM Host chain)
  kmsContractAddress: '0xbE0E383937d564D7FF0BC3b46c51f0bF8d5C311A',
  // INPUT_VERIFIER_CONTRACT_ADDRESS (FHEVM Host chain)
  inputVerifierContractAddress: '0xBBC1fFCdc7C316aAAd72E807D9b0272BE8F84DA0',
  // DECRYPTION_ADDRESS (Gateway chain)
  verifyingContractAddressDecryption:
    '0x5D8BD78e2ea6bbE41f26dFe9fdaEAa349e077478',
  // INPUT_VERIFICATION_ADDRESS (Gateway chain)
  verifyingContractAddressInputVerification:
    '0x483b9dE06E4E4C7D35CCf5837A1668487406D955',
  // FHEVM Host chain id
  chainId: 11155111,
  // Gateway chain id
  gatewayChainId: 10901,
  // Optional RPC provider to host chain
  network: 'https://eth-sepolia.public.blastapi.io',
  // Relayer URL
  relayerUrl: 'https://relayer.testnet.zama.org',
});
```

or the even simpler:

The information regarding the configuration of Sepolia's FHEVM and associated Relayer maintained by Zama can be found in the `SepoliaConfig` object or in the [contract addresses page](https://docs.zama.ai/protocol/solidity-guides/smart-contract/configure/contract_addresses). The `gatewayChainId` is `10901`. The `chainId` is the chain-id of the FHEVM chain, so for Sepolia it would be `11155111`.

For more information on the Relayer's part in the overall architecture please refer to [the Relayer's page in the architecture documentation](https://docs.zama.ai/protocol/protocol/overview/relayer_oracle).


Last updated 1 month ago

---


# Input

Source: https://docs.zama.org/protocol/relayer-sdk-guides/fhevm-relayer/input

This document explains how to register ciphertexts to the FHEVM. Registering ciphertexts to the FHEVM allows for future use on-chain using the `FHE.fromExternal` solidity function. All values encrypted for use with the FHEVM are encrypted under a public key of the protocol.

Copy

```
// We first create a buffer for values to encrypt and register to the fhevm
const buffer = instance.createEncryptedInput(
  // The address of the contract allowed to interact with the "fresh" ciphertexts
  contractAddress,
  // The address of the entity allowed to import ciphertexts to the contract at `contractAddress`
  userAddress,
);

// We add the values with associated data-type method
buffer.add64(BigInt(23393893233));
buffer.add64(BigInt(1));
// buffer.addBool(false);
// buffer.add8(BigInt(43));
// buffer.add16(BigInt(87));
// buffer.add32(BigInt(2339389323));
// buffer.add128(BigInt(233938932390));
// buffer.addAddress('0xa5e1defb98EFe38EBb2D958CEe052410247F4c80');
// buffer.add256(BigInt('2339389323922393930'));

// This will encrypt the values, generate a proof of knowledge for it, and then upload the ciphertexts using the relayer.
// This action will return the list of ciphertext handles.
const ciphertexts = await buffer.encrypt();
```

With a contract `MyContract` that implements the following it is possible to add two "fresh" ciphertexts.

With `my_contract` the contract in question using `ethers` it is possible to call the add function as following.


Last updated 1 month ago

---


# Foundry

Source: https://docs.zama.org/protocol/solidity-guides/development-guide/foundry

This guide explains how to use Foundry with FHEVM for developing smart contracts.

While a Foundry template is currently in development, we strongly recommend using the [Hardhat template](/protocol/solidity-guides/getting-started/setup)) for now, as it provides a fully tested and supported development environment for FHEVM smart contracts.

However, you could still use Foundry with the mocked version of the FHEVM, but please be aware that this approach is **NOT** recommended, since the mocked version is not fully equivalent to the real FHEVM node's implementation (see warning in hardhat). In order to do this, you will need to rename your `FHE.sol` imports from `@fhevm/solidity/lib/FHE.sol` to `fhevm/mocks/FHE.sol` in your solidity source files.


Last updated 2 months ago

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


# Set up Hardhat

Source: https://docs.zama.org/protocol/solidity-guides/getting-started/setup

In this section, you’ll learn how to set up a FHEVM Hardhat development environment using the **FHEVM Hardhat template** as a starting point for building and testing fully homomorphic encrypted smart contracts.

## Create a local Hardhat Project

1

## Install a Node.js TLS version

Ensure that Node.js is installed on your machine.

* Download and install the recommended LTS (Long-Term Support) version from the [official website](https://nodejs.org/en).
* Use an **even-numbered** version (e.g., `v18.x`, `v20.x`)

**Hardhat** does not support odd-numbered Node.js versions. If you’re using one (e.g., v21.x, v23.x), Hardhat will display a persistent warning message and may behave unexpectedly.

To verify your installation:

Copy

```
node -v
npm -v
```

2

## Create a new GitHub repository from the FHEVM Hardhat template.

1. On GitHub, navigate to the main page of the [FHEVM Hardhat template](https://github.com/zama-ai/fhevm-hardhat-template) repository.
2. Above the file list, click the green **Use this template** button.
3. Follow the instructions to create a new repository from the FHEVM Hardhat template.

See Github doc: [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template)

3

## Clone your newly created GitHub repository locally

Now that your GitHub repository has been created, you can clone it to your local machine:

Copy

```
cd <your-preferred-location>
git clone <url-to-your-new-repo>

# Navigate to the root of your new FHEVM Hardhat project
cd <your-new-repo-name>
```

Next, let’s install your local Hardhat development environment.

4

## Install your FHEVM Hardhat project dependencies

From the project root directory, run:

Copy

```
npm install
```

This will install all required dependencies defined in your `package.json`, setting up your local FHEVM Hardhat development environment.

5

## Set up the Hardhat configuration variables (optional)

If you do plan to deploy to the Sepolia Ethereum Testnet, you'll need to set up the following [Hardhat Configuration variables](https://hardhat.org/hardhat-runner/docs/guides/configuration-variables).

`MNEMONIC`

A mnemonic is a 12-word seed phrase used to generate your Ethereum wallet keys.

1. Get one by creating a wallet with [MetaMask](https://metamask.io/), or using any trusted mnemonic generator.
2. Set it up in your Hardhat project:

Copy

```
npx hardhat vars set MNEMONIC
```

`INFURA_API_KEY`

The INFURA project key allows you to connect to Ethereum testnets like Sepolia.

1. Obtain one by following the [Infura + MetaMask](https://docs.metamask.io/services/get-started/infura/) setup guide.
2. Configure it in your project:

Copy

```
npx hardhat vars set INFURA_API_KEY
```

**Default Values**

If you skip this step, Hardhat will fall back to these defaults:

* `MNEMONIC` = "test test test test test test test test test test test junk"
* `INFURA_API_KEY` = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"

These defaults are not suitable for real deployments.

## Missing variable error:

If any of the requested Hardhat Configuration Variables is missing, you'll get an error message like this one:`Error HH1201: Cannot find a value for the configuration variable 'MNEMONIC'. Use 'npx hardhat vars set MNEMONIC' to set it or 'npx hardhat var setup' to list all the configuration variables used by this project.`

Congratulations! You're all set to start building your confidential dApp.

## Optional settings

## Install VSCode extensions

If you're using Visual Studio Code, there are some extensions available to improve you your development experience:

* [Prettier - Code formatter by prettier.io](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) — ID:`esbenp.prettier-vscode`,
* [ESLint by Microsoft](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) — ID:`dbaeumer.vscode-eslint`

Solidity support (pick one only):

* [Solidity by Juan Blanco](https://marketplace.visualstudio.com/items?itemName=JuanBlanco.solidity) — ID:`juanblanco.solidity`
* [Solidity by Nomic Foundation](https://marketplace.visualstudio.com/items?itemName=NomicFoundation.hardhat-solidity) — ID:`nomicfoundation.hardhat-solidity`

## Reset the Hardhat project

If you'd like to start from a clean slate, you can reset your FHEVM Hardhat project by removing all example code and generated files.

Then run:


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


# Logics

Source: https://docs.zama.org/protocol/solidity-guides/smart-contract/logics

[Branching](/protocol/solidity-guides/smart-contract/logics/conditions)

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
