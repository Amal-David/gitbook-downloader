# Table of Contents

- [Welcome to MetaLeX](#welcome-to-metalex)
  - [onchain business entity](#onchain-business-entity)
- [❓ FAQ](#faq)
- [🔑 Key Terms](#key-terms)
- [👋 Introduction](#introduction)
    - [BORGs OS](#borgs-os)
  - [Borg Auth](#borg-auth)
    - [borgCORE](#borgcore)
  - [BORG Modes](#borg-modes)
    - [Blacklist](#blacklist)
    - [Unrestricted](#unrestricted)
    - [Whitelist](#whitelist)
  - [Conditions](#conditions)
  - [Governance Adapters](#governance-adapters)
  - [Helpers](#helpers)
  - [Hooks](#hooks)
  - [Implants](#implants)
    - [DAO Veto Grant](#dao-veto-grant)
    - [DAO Vote Grant](#dao-vote-grant)
    - [Eject](#eject)
    - [FailSafe](#failsafe)
    - [Optimistic Grant](#optimistic-grant)
  - [Legal Approach](#legal-approach)
    - [Cybernetic Organization (CybOrg or ‘BORG’)](#cybernetic-organization-cyborg-or-borg)
**🏢 cyberCORPs**
    - [cyberCORPs OS](#cybercorps-os)
    - [Future Integrations](#future-integrations)
    - [Governance and Officers](#governance-and-officers)
    - [Launching a cyberCORP](#launching-a-cybercorp)
    - [Onchain Capital Structure](#onchain-capital-structure)
    - [Benefits](#benefits)
    - [Core Components](#core-components)
    - [Corporate Actions](#corporate-actions)
    - [Tokenized Stock Certificates](#tokenized-stock-certificates)
    - [Transfer Restrictions](#transfer-restrictions)
    - [Sources](#sources)
    - [What is a cyberCORP?](#what-is-a-cybercorp)
**🤝 cyberDeals**
    - [cyberRaise](#cyberraise)
  - [LeXcheX](#lexchex)
    - [LeXscroW](#lexscrow)
    - [MetaVesT](#metavest)
    - [Round Manager](#round-manager)
**⚖️ Cybernetic Law**
    - [Cybernetic Law introduction](#cybernetic-law-introduction)

---


# Welcome to MetaLeX

Source: https://metalex-docs.vercel.app/

![Logo](/header.png)

MetaLeX builds legal and technical infrastructure for [cyBernetic ORGanizations ("BORGs")](/borg/what-is-a-BORG) and other onchain entities like [cyberCORPs](/cybercorps). Our tools combine blockchain automation with robust legal frameworks to help communities coordinate, govern, and transact with confidence.

We are cypherpunk lawyers, engineers, and anons aiming to solve the currently unsolvable problems in crypto, AI, and finance via cyBernetic ORGanizations.

We strive: (1) in the short-run, to improve efficiency, compliance, trust, and access to justice by integrating autonomous technologies into the legal and governance processes of legal entities; and (2) in the long-run, to empower the legal, governance and dealmaking aspects of new cybernetic societies that enhance human freedom and prosperity.

Explore the areas linked in the sidebar to learn more about what we're building, including the [MetaLeX OS](/metalex-os-intro).

---


# onchain business entity

Source: https://metalex-docs.vercel.app/cybercorps

cyberCORPs fuse traditional corporate structures with programmable smart contracts, bringing the benefits of blockchain automation to familiar legal entities. In MetaLeX’s ecosystem, a [BORG (cybernetic organization)](/borg/what-is-a-BORG) is a legally-wrapped DAO or entity governed by code-infused rules. A cyberCORP differs in that it starts as a traditional corporation (e.g. a Delaware C-Corp or LLC) but operates onchain: its equity is tokenized, and its key agreements and governance processes run via smart contracts. (In essence, cyberCORPs were originally conceived as “bizBORGs,” a business-focused subset of BORGs [MetaLeX Substack](https://metalex.substack.com).) While BORGs emphasize fully automated decentralized governance, cyberCORPs intersect with that framework by using BORG technology (such as onchain role management) for a more centralized yet code-assisted corporation. This broadened focus targets startup founders and mainstream businesses – MetaLeX’s cyberCORPs tech has a distinct roadmap and a broader audience beyond crypto DAOs [X](https://x.com).

## Explore More

* [cyberCORPs OS](/cybercorps/cybercorps-os)
* [What is a cyberCORP?](/cybercorps/what-is-a-cyberCORP)
* [Onchain Capital Structure](/cybercorps/onchain-capital-structure)
* [Governance and Officers](/cybercorps/governance-and-officers)
* [Launching a cyberCORP](/cybercorps/launching-a-cybercorp)
* [Future Integrations](/cybercorps/future-integrations)
* [Sources](/cybercorps/sources)

---


# ❓ FAQ

Source: https://metalex-docs.vercel.app/faq

## What is MetaLeX and what does it aim to achieve?

MetaLeX is a platform that fuses law and code to bring legal contracts, organizational governance, and financial deals onto the blockchain. It provides the infrastructure to turn traditional legal entities into cybernetic organizations where on-chain smart contracts handle decisions and transactions that previously relied on paper or manual processes. By combining autonomous blockchain technology with robust legal frameworks, MetaLeX helps communities coordinate and transact with greater speed, transparency, and trust‑minimization while remaining legally compliant.

MetaLeX’s mission is to bridge the gap between legal agreements ("wet" contracts) and "dry" code. In the short run, the team focuses on improving efficiency, compliance, and access to justice by embedding smart contracts into legal and governance processes. In the long run, MetaLeX envisions empowering new cyber‑societies that enhance human freedom and prosperity by making legal, governance, and deal‑making functions autonomous and blockchain‑based. This means creating an "internet of agreements" where on-chain code executes and enforces agreements seamlessly in tandem with legal intent. In summary, MetaLeX’s goal is to make legal automation a reality – using code to enforce rights and obligations while ensuring those actions are recognized and enforceable under traditional law.

## How is MetaLeX structured? What is MetaLeX OS and its modular architecture?

MetaLeX is built as a modular, composable "operating system" for on-chain organizations, often referred to as MetaLeX OS (also called BORGs OS). This framework is composed of interchangeable smart contract components and legal templates that users can mix and match to fit their needs.

At a high level, MetaLeX OS includes several layers:

* **BORGs** – Cybernetic organizations that combine legal entity structures with on-chain governance via smart contracts. BORGs are the fundamental units, similar to traditional companies or foundations augmented with blockchain automation.
* **cyberCORPs** – On-chain corporate structures that facilitate fundraising and equity/token issuance for startups. These are tech‑augmented corporate entities used for compliant capital raises with tokenized securities.
* **cyberDeals** – A suite of smart contract tools for executing deals and agreements on-chain, such as escrows, vesting schedules, and automated legal contracts.
* **Cybernetic Law Templates** – Legal contract templates designed to work hand‑in‑hand with code, ensuring that every on‑chain action has an associated legal text.

MetaLeX OS is open-source and composable – new modules can plug into the system, and existing ones can be upgraded or configured without starting from scratch. The core contracts use a modular design with pluggable extensions called "implants" (smart contract modules that add specific features). Because of this design, MetaLeX components are often described as "LEGO blocks" for legal engineering.

One key piece of the architecture is the **borgCORE** – essentially the heart of every BORG entity. The BORG Core contract wraps a Gnosis Safe (multisig wallet) with a policy layer and the standard DAO interface (ERC‑4824), enforcing which actions the multisig can take and under what conditions. The core is deployed in a chosen mode (whitelist, blacklist, or unrestricted) and then extended by various modules:

* **BorgAuth** – an access control sub‑module deciding who can update policies or install new modules into the BORG.
* **Condition Manager** – a component for checking custom on-chain conditions (like time locks or oracle feeds) before allowing certain actions.
* **On-chain References** – storage in the core for pointers to legal documents (e.g., IPFS hashes of contracts) or links to an associated DAO’s data.
* **Implants** – pluggable Safe modules that add features (like token vesting, optimistic approvals, emergency recovery, etc.) to a BORG.

Because of this layered design, MetaLeX’s architecture is highly composable. You might deploy a base BORG Core for your organization, then attach a ConditionManager to enforce rules, add an implant for special grant-making logic, integrate a Cybernetic Agreement template for legal backing, and so on. Each piece focuses on a specific aspect (governance permissions, deal execution, compliance, etc.), and together they form a cohesive "operating system" for blockchain‑based legal entities.

## What is a BORG, and how is it different from a DAO?

BORG stands for "cyBernetic ORGanization" – a term MetaLeX uses for entities that combine a legal company structure with autonomous code. A BORG is essentially a traditional legal entity (like an LLC, corporation, foundation, etc.) whose charter includes built‑in rules delegating some decisions to smart contracts or AI. In other words, a BORG is a legal entity augmented by on-chain code.

BORGs typically fall into two categories:

* **Business BORGs (bizBORGs)** – Tech‑augmented companies that operate for profit. For instance, a startup could incorporate as a normal company but use tokenized shares, on-chain voting, and automated compliance.
* **DAO‑Adjacent BORGs** – Entities that work alongside decentralized communities (DAOs) to handle things a purely on-chain DAO might struggle with (like legal agreements or holding real-world assets). These might be foundations or trusts that have some autonomy but ultimately serve a DAO’s interests under strict checks and balances.

Compared to a traditional DAO, a BORG is not fully decentralized or anonymous. DAOs in the purest sense are entirely on-chain and self-governing by token holders, without legal entity status. BORGs, however, have legal incorporation and often a known management structure (directors, guardians). The key idea is that BORGs strike a balance: they maximize the use of trust‑minimized code and open governance where feasible, but plug in legal mechanisms wherever needed to cover edge cases or off‑chain obligations. They allow DAOs to accomplish things like signing contracts, hiring people, or owning assets in a legally recognized way while using smart contracts to automate and control those activities.

## What is the BORG Core contract?

The BORG Core (borg-core) is the primary smart contract that powers every MetaLeX BORG. It’s the on-chain brain or policy engine of the organization. Technically, BORG Core is implemented as a Gnosis Safe guard module combined with a DAO interface (ERC‑4824). This means it sits on top of a multisig wallet and intercepts or governs what that multisig can do, according to the BORG’s rules.

Key aspects of BORG Core include:

* **Modes** – When deploying a BORG Core, you choose an immutable mode: whitelist, blacklist, or unrestricted. In whitelist mode, only explicitly allowed actions can be done by the Safe; in blacklist, all actions are allowed except those forbidden; unrestricted mode applies minimal checks.
* **Policy Checks** – The core enforces policy via various sub-components. The Condition Manager evaluates any conditions set on actions, requiring that specific conditions (time delays, approvals, external data conditions, etc.) are true before a transaction is executed.
* **BorgAuth (ACL)** – An access control layer defining who is allowed to make administrative changes to the BORG, typically giving permission to a DAO governance contract or a council rather than individual Safe signers.
* **Implant Support** – The core supports implant modules, additional contracts that extend Safe functionality, such as token vesting or emergency recovery.
* **Legal & DAO Linkage** – The BORG Core stores references to off-chain legal documents and can store the identifier of an associated DAO, tying legal and technical aspects together.

In practice, BORG Core enforces the “rules of the game” inside a BORG. If the Safe is the vault holding assets, the BORG Core is the guard at the vault’s door, checking every instruction against the rulebook. Once deployed, its mode can’t be changed, providing confidence that the BORG will operate only as authorized.

## What is the ConditionManager and why is it important?

The ConditionManager is a module in the MetaLeX system that allows a BORG to enforce complex, custom rules (conditions) on actions taken by its contracts. It lets you specify that an action can occur only if certain conditions are met, encoding real‑world governance or legal requirements into smart contracts.

How it works:

* The ConditionManager keeps a list of condition contracts and knows how to evaluate them in logical combinations. Each Condition is a separate smart contract that returns true/false under certain circumstances.
* Multiple conditions can be combined with AND or OR logic, allowing sophisticated requirements.
* Conditions can be global (apply to all operations) or function-specific.
* Conditions are modular; authorized roles can add or remove condition contracts over time as needs change.
* When an action is attempted, the ConditionManager checks the relevant conditions and reverts the transaction if any required condition is not met.

This enables on-chain code to reflect real‑world rules and safeguards, such as requiring both a majority approval and a time delay before a payout occurs.

## What is the SignatureRegistry (or Cyber Agreement Registry) and what does it do?

The SignatureRegistry, also referred to as a Cyber Agreement Registry, tracks the signing of legal agreements on-chain. Deals between parties often involve both an on-chain transaction and an associated legal document. The SignatureRegistry keeps a tamper-proof record of who signed an agreement, when they signed, and whether all required parties have signed.

For each legal template, the registry stores a template ID and a reference to the legal text. When a new deal is created, an entry is created linking to the template and recording the participating parties. As each party digitally signs the agreement, the registry logs the signature and timestamp. It can determine if an agreement is fully signed by comparing collected signatures to the number of required parties and can emit an event once all have signed.

This functions as an on-chain notary and ledger for agreements, ensuring no action is taken without proper authorization from each party and providing evidence that can be used off-chain if needed. The registry often works with other modules; for example, a BORG might require a SignatureRegistry entry to be fully signed before executing an action.

## What is LeXscroW and how does it work?

LeXscroW is MetaLeX’s on-chain escrow system – a set of smart contracts that hold funds or assets in trust and only release them when predetermined conditions are met. Once a LeXscroW contract is created, no one can arbitrarily take the funds; the logic automatically executes the agreed outcome or refunds participants if conditions fail.

Key features include:

* **Trust-minimized & Non-custodial** – Assets are held in a smart contract with no owner; only the coded conditions control their release.
* **Immutable Conditions** – Rules for release are set at creation and cannot be changed, giving participants certainty.
* **Automatic Refunds** – If conditions are not met, participants can reclaim their deposits.
* **Flexible Deposits & Participation** – Contracts can allow open participation or restrict deposits to specific addresses.
* **Composable** – LeXscroW can be combined with other MetaLeX tools for complex deals.

Variants include DoubleTokenLeXscroW for token swaps, TokenLeXscroW for one-way deals, and EthLeXscroW for native currency escrows. Typical use cases include trustless token swaps, milestone-based funding, grants with clawback, and conditional payouts.

## What is LeXcheX and what does it do?

LeXcheX is MetaLeX’s on-chain accredited investor verification service. It lets an investor prove they are an accredited investor entirely on the blockchain and receive a tamper-proof NFT certificate as proof, replacing traditional paperwork-heavy processes.

How it works:

1. **Investor Questionnaire** – The user answers questions about how they qualify as accredited.
2. **On-Chain Asset Check** – An off-chain oracle evaluates the investor’s wallet balances to confirm asset thresholds.
3. **On-Chain Legal Agreement & NFT Issuance** – If the check is successful, the investor signs an attestation and pays a fee, and LeXcheX mints a non-transferable NFT certificate to the wallet.

Projects like cyberRaise can require this NFT before allowing participation, ensuring compliance with regulations like U.S. Rule 506(c). The NFT is issued under attorney oversight and can expire or be revoked, providing accountability.

## What is MetaVesT and how is it used?

MetaVesT is an advanced token vesting and lockup protocol. It handles complex token distribution schedules in a trust-minimized way, mirroring terms found in traditional equity grants or token sale lockups.

Capabilities include:

* Dual vesting and unlock curves, tracking when tokens are earned and when they become transferable.
* Optional cliffs on either curve.
* Token options and 83(b) support via exercise prices.
* Group amendments allowing majority-in-value of grantees plus the grantor to amend terms.
* Can’t-be-evil protections preventing arbitrary clawbacks of vested tokens.
* Pass-through voting, allowing locked tokens to participate in governance.
* Milestone-based vesting triggered by external events.

MetaVesT escrows tokens and issues non-transferable receipt tokens to grantees. As time passes or milestones occur, the contract updates vested and unlocked amounts. Grantees can withdraw tokens that are both vested and unlocked. MetaVesT is ideal for team/investor vesting, DAO grants, investor lock-ups, and complex deal structures.

## What is a Ricardian Tripler?

A Ricardian Tripler tightly binds together three elements of an agreement – the code, the legal text, and the parameters – into one package. Parties sign one on-chain transaction that records the parameters, stores the legal text, and deploys or references the smart contract enforcing the deal, linking all three components.

This synchronization ensures the legal document explicitly references the smart contract, and the smart contract is parameterized exactly as described in the legal text. The concept prevents disputes where code and human intent diverge and is a step toward "lex cryptographia," where code and law function as one.

## What is the GAIB Agent and what off-chain computation does it handle?

The GAIB Agent is an off-chain computational agent or oracle service that performs tasks too complex or impossible to do entirely on-chain. It interacts with MetaLeX smart contracts to provide trusted off-chain inputs or computations.

Examples include:

* Evaluating crypto asset holdings for LeXcheX accreditation checks.
* Fetching external data feeds like prices or court decisions.
* Running heavy computations or AI analyses and posting results on-chain.
* Generating zero-knowledge proofs or other verifiable data for on-chain use.

The GAIB Agent extends MetaLeX contracts beyond blockchain limits while minimizing trust by using legal accountability or cryptographic proofs.

## How does MetaLeX integrate legal contracts with smart contracts?

MetaLeX practices "Legal Engineering," deliberately designing legal agreements and software together so they operate as a cohesive system. Integration is achieved through:

* **Cybernetic Law Templates** that reference on-chain elements and have slots for on-chain data.
* **On-chain storage of agreements** via the Cyber Agreement Registry, enabling reconstruction of the full contract from template and parameters.
* **Ricardian Triplers** that align legal text and code.
* **No closed platforms** – agreements and data are open and composable.
* **Automation of execution** through smart contracts, minimizing reliance on human performance.
* **Fallbacks and edge cases** addressed via legal clauses when code cannot handle a scenario.
* **Enforceability** by ensuring courts can reference on-chain records as the agreed source of truth.

This approach merges human language and programming language, making legal automation possible.

## Who are the intended users of MetaLeX, and what are some real use cases?

MetaLeX serves several groups:

* **Web3 Startup Founders & Projects** – Use cyberCORPs, cyberRaise, LeXcheX, and MetaVesT to raise funds and manage governance.
* **DAOs and Decentralized Communities** – Use DAO-adjacent BORGs for grants, security, or IP management while retaining on-chain transparency and control.
* **Investors** – Gain clear, automated records of their rights via NFTs and trust in escrowed funds.
* **Legal Professionals and Advisers** – Leverage MetaLeX templates and modules to build solutions for clients.
* **Community Members & DAO Token Holders** – Benefit from transparent operations and safeguarded funds.

Real examples include the Neutron Grants BORG, cyberRaise fundraising rounds, DAO-to-DAO collaborations using LeXscroW, and compliance/KYC scenarios using credential NFTs.

## How is MetaLeX governed, and what is the plan for decentralization of the platform?

MetaLeX is currently developed by MetaLeX Labs, but the architecture is open and increasingly community-driven. The BORGs OS is open-source, and the community contributes via documentation, templates, and feedback. The cyberCORP initiative is in a controlled beta, with plans to open up as legal frameworks mature.

Future decentralization may involve launching a MetaLeX DAO or foundation to oversee protocol upgrades, curating templates, and possibly introducing a token for governance and incentives. The roadmap likely includes open-sourcing remaining components, completing audits, and establishing community governance once the platform is stable and compliant.

## How does MetaLeX address compliance and regulatory considerations?

Compliance is central to MetaLeX’s design:

* **Legal Entity Wrappers** provide limited liability and clarify tax and reporting duties.
* **Securities Law Compliance** is baked in through modules like cyberRaise and LeXcheX, enabling Reg D and Reg S offerings with automated checks.
* **Embedded Compliance Checks** use conditions to enforce investor caps, jurisdiction limits, and more.
* **KYC/AML Integration** is possible via credential NFTs or third-party oracles.
* **Data Privacy** is respected by only storing necessary data on-chain and exploring privacy-preserving techniques.
* **Jurisdictional Customization** allows templates and modules tailored to different legal regimes.
* **Transparency and Auditability** ensure regulators or auditors can verify operations directly on-chain.
* **Emergency Mechanisms** like FailSafe implants provide lawful intervention paths without undermining decentralization.

This proactive approach lets projects comply with regulations while leveraging blockchain advantages.

## Does MetaLeX have a token? How does the MetaLeX platform sustain itself?

As of now, MetaLeX does not have a public native token. The platform’s economic model revolves around providing services and charging fees, such as the $100 USDC fee for LeXcheX accreditation certificates. MetaLeX Labs may also offer consulting or enterprise services for revenue.

If a MetaLeX token is introduced in the future, it could serve governance, incentivize network participants, or capture value from platform usage. Any such token would likely be designed carefully to remain compliant with securities regulations. Until then, MetaLeX focuses on building a robust platform and user base through service-based sustainability.

## How secure is MetaLeX? What is the security model and audit status?

MetaLeX prioritizes security through:

* **Proven Building Blocks** like Gnosis Safe for asset custody.
* **Least Privilege and Role Separation** via directors, guardians, and DAO oversight.
* **Non-Custodial Design** for modules like LeXscroW and MetaVesT.
* **Extensive Testing and Audits** by firms such as MixBytes and Zellic for major components.
* **Ongoing Security Monitoring** and potential bug bounty initiatives.
* **Upgrade Safety** through multi-party approval and time delays where applicable.
* **Fail-safes** like DeadManSwitchCondition and FailSafe implants for recovery scenarios.

To date, MetaLeX has undergone multiple independent audits with no major security incidents reported, reflecting a strong commitment to safeguarding user assets and legal agreements.

## FAQ – Legal, Regulatory, and Practical Concerns (for Professionals & Skeptics)

This section addresses advanced questions raised by legal professionals, regulators, institutional investors, and experienced users who are scrutinizing MetaLeX’s approach. It provides legally grounded, practical answers to common doubts about MetaLeX’s cybernetic agreements, on-chain legal enforceability, regulatory compliance, and real-world usability.

## Q: Are MetaLeX’s “cybernetic” on-chain agreements actually enforceable in the real world?

A: Yes. MetaLeX contracts are designed to be legally binding dual agreements – every on-chain action is mirrored by a written legal contract. When parties enter a MetaLeX deal, a smart contract executes on-chain and the human-readable legal terms (stored on IPFS) are simultaneously adopted, with the transaction data populating the contract text
GitHub
GitHub
. In effect, signing a MetaLeX transaction from your wallet is also cryptographically signing a conventional agreement. This Ricardian Tripler approach ties code, legal text, and parameters into one package, ensuring the smart contract’s outcomes align exactly with the legal obligations
GitHub
. Because the legal agreements explicitly reference the specific smart contract address and terms, a court or arbitrator can recognize and enforce them if a dispute arises. The records on blockchain (signatures, timestamps, parameters) serve as tamper-proof evidence of the deal’s terms and each party’s commitments. In short, MetaLeX replaces “paper-only” contracts with hybrid code-and-prose contracts – they self-execute on-chain, but remain backed by traditional legal validity (e.g. offer, acceptance, and intent to be bound), giving professionals the assurances of enforceability they expect.

## Q: What if something goes wrong on-chain – say a bug, an exploit, or a disagreement about a MetaLeX contract’s outcome? Do we still have recourse?

A: MetaLeX is built to handle disputes and unforeseen issues by combining automated enforcement with legal fallback mechanisms. First, MetaLeX tries to prevent disputes: the smart contracts are rigorously tested and often audited, and their behavior is transparent to all parties
GitHub
. But if a problem does arise (for example, a counterparty breaches an obligation or a critical bug affects the outcome), the parties are not left helpless. Because there is a parallel legal agreement for every deal, an aggrieved party can pursue remedies through normal legal channels – such as arbitration or court litigation – using the signed contract text and blockchain records as evidence. Importantly, MetaLeX’s chosen legal frameworks support this: for instance, the Cayman Islands (where many MetaLeX “BORG” entities are registered) offers specialized courts and a body of common-law precedent for complex business disputes, providing a knowledgeable forum if on-chain agreements end up in litigation
GitHub
. In practice, many MetaLeX contracts include built-in dispute resolution clauses (e.g. arbitration provisions or choice-of-court agreements) to ensure there’s a clear path to resolve issues off-chain if purely on-chain resolution isn’t possible.

MetaLeX’s philosophy is “trust the code for determinable outcomes, but have law as a safety net.” The system strives for lex cryptographia – where code handles routine execution and only ambiguous or wrongful situations fall back to legal processes
GitHub
. Day-to-day, the smart contracts and DAO governance automate decisions, but if something like a hack or an irreconcilable disagreement occurs, human legal norms re-enter to provide accountability. The bottom line for skeptical professionals: you gain the efficiency and certainty of self-executing code without giving up the ability to sue, obtain injunctions, or otherwise enforce rights through the courts when needed. MetaLeX’s own legal team (which even includes former regulatory attorneys familiar with dispute scenarios
metalex.tech
) has engineered the framework so that no on-chain action is beyond the reach of law.

## Q: MetaLeX uses Cayman foundation companies and other offshore entities as legal wrappers. Is this just regulatory arbitrage? What about jurisdiction mismatches if participants are worldwide?

A: The use of jurisdictions like the Cayman Islands is intentional – not to evade law, but to provide a neutral, crypto-friendly legal home that aligns with DAO principles. Cayman “foundation companies” in particular have features ideally suited for decentralized projects: they have no shareholders or private owners, can be structured with purely charitable or mission-based purposes, and allow bylaws that hardwire DAO governance into the entity
GitHub
GitHub
. This means a BORG (cybernetic organization) based in Cayman is ownerless (much like a DAO) and exists solely to carry out its stated purpose (e.g. supporting a protocol), rather than to maximize shareholder profit
GitHub
. By anchoring the organization in one well-defined jurisdiction, MetaLeX avoids the chaos of every multisig signer’s local laws applying at once
GitHub
. All participants know which law governs the entity – providing certainty and avoiding, say, a scenario where a globally distributed team accidentally creates an “unincorporated partnership” subject to dozens of countries’ regulations
GitHub
.

Far from being a shady haven, the Cayman Islands currently offers a robust but innovation-friendly regulatory environment. It has no hostile DAO-specific rules, and its regulators and service providers are experienced with crypto entities. In fact, Cayman foundations come with accountability measures (like requiring a local Supervisor if there are no members) that MetaLeX leverages to ensure compliance with the entity’s rules
GitHub
. This choice of jurisdiction also preempts certain U.S. regulatory issues – for example, by isolating potentially investment-like activities in a Cayman foundation, a DAO can avoid being viewed by U.S. authorities as an unregistered investment fund
GitHub
. That said, MetaLeX is not about hiding from regulation: if a MetaLeX-structured entity operates in other countries (e.g. hiring a U.S. team or serving U.S. investors), it still must comply with those local laws (securities law, tax law, etc.). The Cayman wrapper simply gives a solid legal base; from there, additional compliance (like U.S. securities exemptions, filings, KYC/AML for investors, etc.) can be layered as needed for activities in other jurisdictions. In summary, MetaLeX’s legal strategy is to choose the right tool for the job – e.g. Cayman for a global DAO foundation, Delaware for a U.S.-based non-profit subsidiary – to ensure the entity is both legally sound and aligned with decentralization, rather than to dodge oversight.

## Q: Could these legal wrappers (BORGs) be abused or have vulnerabilities? For instance, what stops a BORG’s insiders from misusing funds or power?

A: MetaLeX BORGs are specifically designed to minimize the risk of insider abuse through both legal obligations and technical safeguards. Legally, every participant in a BORG (e.g. a multisig signer or board member) must sign a BORG Participation Agreement that binds them to act in the entity’s interest and follow its bylaws
GitHub
. This creates a direct contractual duty – if a signer attempted to misappropriate assets or act outside their authority, the foundation (via its Supervisor) and even the DAO community (as third-party beneficiaries) would have legal grounds to hold that individual accountable in court
GitHub
. In other words, rogue actors face real liability for breaching their duties, which deters bad behavior beyond just the honor system.

On the technical side, MetaLeX hard-codes compliance into the smart contracts. The BORG’s on-chain multi-signature wallet (typically a Gnosis SAFE) is outfitted with MetaLeX’s custom “BorgOS” extensions that act as automated watchdogs
GitHub
. For example, the core BORG smart contract serves as a Guard on the SAFE, whitelisting only the actions that are allowed per the BORG’s legal charter
github.com
. Any transaction that isn’t pre-approved (by type, amount, recipient, etc.) will be blocked by the contract guard
github.com
. This means that even if all human signers colluded to do something unauthorized (like sending funds to a personal address or doing an out-of-scope investment), the on-chain code would prevent it unless the proper DAO approvals or conditions are satisfied. MetaLeX’s Condition Manager can even enforce that certain actions only execute if an oracle or external condition is met (for instance, requiring an on-chain vote outcome or a price feed reading)
github.com
. Additionally, BORG bylaws themselves explicitly state that any asset moved outside the approved on-chain channels isn’t legally recognized – a rogue signer moving funds “off-book” would be violating bylaws and could be sued for breach of fiduciary duty
GitHub
GitHub
.

To summarize, power in a BORG is tightly circumscribed: human actors are constrained by both the threat of legal action and by code that enforces the rules in real time. The MetaLeX approach delivers a “defense in depth”: if someone somehow bypasses a smart contract control, the legal agreements kick in; and if someone tries to shrug off legal duties, the smart contracts are there to stop unauthorized moves. This dual layer of protection greatly mitigates the risk of misuse or malfeasance compared to an unstructured DAO or a traditional company without such integrated controls.

## Q: MetaLeX claims legal compliance and “bridging law and code.” How do we know this isn’t just superficial? Is the compliance truly substantive?

A: It’s absolutely substantive. MetaLeX was founded by seasoned attorneys and engineers specifically to embed real legal rigor into blockchain systems – not as a marketing checkbox, but as the core of the platform
metalex.tech
. Every BORG or cybernetic contract MetaLeX helps create involves real legal work: drafting bespoke charters and bylaws, coordinating with law firms to register entities, and ensuring ongoing compliance. For example, when spinning up a BORG foundation, MetaLeX works with licensed Cayman counsel to formally register the company and draft its Memorandum & Articles and Bylaws in line with the DAO’s needs
GitHub
. They even arrange professional directors or supervisors when required by local law, and strictly limit those roles via legal documents to prevent any loopholes
GitHub
. All of this is far beyond a token “paper filing” – it’s a complete legal architecture backing the on-chain operations.

Moreover, MetaLeX’s smart contracts and legal documents are developed in tandem. The team’s lawyers and developers iterate together so that the bylaws and code reflect each other precisely
GitHub
GitHub
. This includes defining clear processes for things like adding members, transferring tokens, or dissolving the entity, and then implementing those processes both in the legal text and in the solidity code. The goal is that anyone examining a MetaLeX structure can see that the rules aren’t just on paper: they are actively enforced by software. For instance, if the bylaws say “any change to the BORG’s multisig signers requires DAO approval,” the smart contract guard literally will not allow a new signer to be added unless a verified DAO vote has occurred
GitHub
. This kind of cross-verification shows that compliance is built into the system’s operations, not merely its intentions.

Finally, MetaLeX’s commitment to real compliance is evidenced by the projects and communities involved. Major DAO initiatives (such as the Lido community’s “Lido Alliance” foundation and others) have used MetaLeX’s framework, subjecting it to scrutiny by top law firms and DAO contributors. The fact that sophisticated stakeholders are adopting BORG structures indicates trust that these are legally sound, not just empty shells. Even MetaLeX’s experimental features like GAIB (an AI legal agent) have detailed legal safeguards (e.g. a Delaware non-profit wrapper, purpose clauses, etc.) rather than being freewheeling bots
followin.io
followin.io
. In sum, MetaLeX’s value proposition hinges on actual legal enforceability and compliance – something they’ve architected at every level of the stack.

## Q: MetaLeX relies on off-chain data and “GAIB” AI agents in some cases. Doesn’t that reintroduce trust and uncertainty? How is the oracle/agent model handled?

A: MetaLeX minimizes off-chain dependencies, but when they are necessary, it handles them in a transparent and trust-managed way. Oracles (for feeding external data like prices or events) and the GAIB agent (MetaLeX’s AI legal assistant) are integrated with careful checks and balances. Here’s how:

* **Decentralized & Controlled Oracles** – MetaLeX smart contracts can ingest off-chain information via oracle feeds, but these are never a single point of failure. The BORG’s Condition Manager module allows multiple conditions and approvals to be required for any action
  github.com
  . For example, a payment might require both an oracle price and a DAO multisig approval to proceed, ensuring no oracle alone can trigger a critical transaction. Oracles can be chosen from reputable decentralized networks (like Chainlink or similar) or even a consortium of known data providers. The oracle inputs themselves are often anchored in the legal docs – the agreement will specify the data source and what happens if that source fails. This way, everyone knows which off-chain data is authoritative, and there’s a legal basis to disregard data that falls outside defined parameters (e.g. clearly erroneous feeds could be deemed invalid by contract). In short, off-chain data is brought in only with explicit, verifiable mechanisms, and usually requires human or DAO sign-off for anything consequential.
* **GAIB (Governance AI Bot) with BORG Oversight** – The GAIB agent – essentially an AI programmed to assist with legal research or even sign certain low-risk transactions – is not a free-roaming AI without constraints. In fact, the GAIB agent is itself wrapped inside a MetaLeX BORG entity (in this case, a Delaware nonstock non-profit corporation) to impose legal and governance oversight
  followin.io
  . The GAIB BORG’s charter includes a “Qualified Code is Law” provision: most of the time the AI’s on-chain actions (its “code”) are treated as the final word, except in defined edge cases like obvious malfunctions or hacks
  followin.io
  . This means if the GAIB agent operates normally (e.g. reviewing a smart contract and giving a green light within its authority), its decisions can auto-execute on-chain. But if it behaves abnormally – say due to an AI glitch or it signs a clearly unauthorized transaction – the BORG’s rules allow human supervisors (and the DAO governance) to step in and override or unwind those actions
  followin.io
  . Practically, GAIB’s powers are limited: it might be allowed to co-sign routine transactions or provide on-chain legal opinions, but it cannot unilaterally control funds beyond what it’s been permitted. All of its transactions still go through the SAFE multisig (where other human or DAO signers can veto if something looks off). In essence, MetaLeX treats an AI agent like any other fallible actor – it’s given a role with specified permissions, and it’s sandboxed within a legal entity so that there’s always an accountable party if something goes wrong.

By combining on-chain controls with off-chain legal oversight, MetaLeX ensures that oracle feeds and AI agents enhance autonomy without compromising trust. Users and regulators can inspect the logic (open-source code, oracle addresses, AI parameters) and also take comfort that an identifiable legal entity is responsible for the outputs. The trust model thus remains multi-layered: trust the math and code where you can, but also have human governance and legal accountability watching over any automated agents.

## Q: Can MetaLeX-based organizations actually interact with traditional legal systems? For example, can a BORG own assets in the real world, sign contracts off-chain, or be taken to court?

A: Absolutely. A MetaLeX “BORG” is a real legal entity (such as a foundation company or nonprofit corporation) and has all the capacities of any company in that jurisdiction. That means it can own property, intellectual property, and other assets in its own name, enter into contracts with outside parties, hire employees or contractors, and so on
GitHub
GitHub
. For instance, a BORG’s foundation could hold a Web2 domain name or a patent on behalf of the DAO – something a smart contract alone cannot do – providing a crucial bridge between on-chain operations and off-chain property rights
GitHub
. Likewise, the BORG can open bank accounts or fiat on-ramp accounts if needed, because it has legal personhood (banks or vendors can KYC the entity and deal with it just like they would with an LLC or corporation).

Importantly, a MetaLeX entity can also appear in court or arbitration as the vehicle representing the DAO’s interests. If the BORG needs to sue (or be sued), the case can be brought in the courts of its home jurisdiction (e.g. Cayman Islands court for a foundation, Delaware court for a U.S. nonstock corp). Those courts are perfectly capable of adjudicating disputes involving the entity’s bylaws or agreements – Cayman even has specialized business courts ready to handle complex crypto disputes
GitHub
. MetaLeX’s legal design ensures there’s always a designated agent or responsible director who can respond to legal service on the entity’s behalf, so a lawsuit won’t get stuck in a black hole. This interoperability extends to things like regulatory filings or registrations: for example, if a BORG issues tokenized shares or interests, it can maintain an official shareholder (member) register that mirrors the on-chain token holdings, satisfying company law requirements. In summary, MetaLeX entities are fully-fledged legal actors in the traditional sense, giving you the benefits of engaging with courts, registries, and counterparties, while concurrently operating with the efficiency of on-chain code.

## Q: What if regulators (like the SEC in the U.S.) crack down on crypto activities? Are MetaLeX structures prepared for regulatory scrutiny or enforcement?

A: MetaLeX is designed with regulatory compliance in mind, aiming to future-proof projects against exactly that kind of risk. By blending legal entities with on-chain governance, MetaLeX actually makes it easier to demonstrate compliance to regulators. For example, if a DAO purely exists on-chain with no legal wrapper, a regulator like the SEC might view it as an unincorporated association or even attempt to treat token holders as part of a de facto partnership – a nightmare scenario. MetaLeX avoids this by giving the DAO a recognized legal form (like a foundation or nonprofit) which regulators can engage with. The foundation can clarify roles (it’s clear who the directors are, who to contact), and it can implement compliance measures (it might restrict token sales to accredited investors, or file disclosures, etc., if required). Essentially, MetaLeX provides an accountability layer that regulators typically want to see
forum.zknation.io
.

Furthermore, MetaLeX structures are intentionally crafted to steer clear of the most sensitive regulatory red flags. For instance, if a BORG will be handling community funds or investments, MetaLeX will structure it so that the foundation is non-profit and has no equity owners, making it less likely to be deemed a security issuer or an “investment company”
GitHub
GitHub
. Profits are not distributed to individuals; instead, any funds are used for the DAO’s purposes, which helps avoid classifications like securities dividends. In one real example, the GAIB project’s token (GAIB) was explicitly not sold as an investment – the token proceeds go into a decentralized liquidity pool, not to MetaLeX or any company’s coffers
followin.io
. This kind of setup was chosen so that the token functions as a utility/governance token for the AI agent, not as a share of a business
followin.io
. By proactively structuring offerings and entities in compliant ways (with legal guidance from experts, including ex-SEC personnel on the MetaLeX team
metalex.tech
), MetaLeX greatly reduces the risk of running afoul of regulations.

Of course, no structure is immune to regulatory overreach or changing laws. However, if a regulator does raise an issue, a MetaLeX BORG can respond in a formal, cooperative manner – it can hire counsel, negotiate, or implement remedial measures as needed, just like any company. Importantly, having clear bylaws and records means a MetaLeX entity can demonstrate its good-faith compliance (for example, showing a regulator the provisions that ensure token holders had to be verified, or that a DAO vote was required for certain actions, etc.). This transparency and built-in compliance make it far easier to satisfy regulators compared to an unaffiliated DAO. In summary, MetaLeX can’t guarantee that a given project won’t become subject to regulation, but it provides the tools to be compliant from day one and to adapt swiftly if the legal environment shifts.

## Q: In a MetaLeX multi-signature governance setup, who owns the IP or products created? And what about personal liability – are the multisig signers/directors personally on the hook if something goes wrong?

A: Intellectual Property (IP) – MetaLeX ensures IP is owned or controlled by the legal entity (the BORG), not by the individual contributors. For example, if a team of developers within a BORG creates software or a brand, the Cayman foundation or Delaware corporation can hold the copyright or trademark. MetaLeX’s framework explicitly allows the entity to custody legal rights and IP that a smart contract can’t hold
GitHub
. In practice, MetaLeX often arranges for contributors to assign any created IP to the foundation, or grants the foundation a perpetual license to use it. A concrete case was the GAIB AI lawyer project: MetaLeX Labs granted the GAIB BORG a perpetual, royalty-free license to all the \_gai16zbrielShapir0 AI’s intellectual property, to ensure the BORG (and by extension the community) can use the AI without risk of MetaLeX later revoking those rights
followin.io
. This kind of arrangement is essentially “IP escrow” – it prevents any one signer or even the founding team from monopolizing assets that are meant for the DAO’s benefit. All key assets (code, domain names, etc.) end up owned by the BORG or formally licensed to it, so they remain with the community’s vehicle even if individual people leave the project.

Liability: One big advantage of the BORG legal wrapper is that it shields individual participants from personal liability in almost all normal circumstances
GitHub
. The foundation company or corporation is a separate legal person – it bears the brunt of any legal liability, debt, or lawsuit. Directors, officers, and multisig signers are generally not personally responsible for the entity’s obligations, as long as they are acting in good faith and in accordance with their duties
GitHub
. If, say, the BORG is sued or owes money, the plaintiffs can go after the foundation’s assets, not the personal assets of the multisig members. This limited liability is crucial for getting talented people to serve in these roles without fear of ruinous personal risk
GitHub
. Of course, the protection isn’t absolute: if a signer commits egregious wrongdoing – e.g. fraud or willful illegal activity – courts can “pierce the veil” and hold them personally accountable
GitHub
. But for ordinary negligence or business losses, the BORG structure provides a corporate veil just like a normal company.

To further protect individuals and encourage responsible governance, all BORG signers explicitly agree to fiduciary-like duties in the Participation Agreement and bylaws
GitHub
GitHub
. They must act in the best interest of the entity/DAO mission and not for personal gain
GitHub
. If they uphold those duties, they remain shielded by the entity. If they breach them (e.g. siphoning funds), then aside from legal action, they also lose the protection – a rogue signer would not only face potential lawsuit but could also be deemed acting outside their authority (and thus possibly personally liable). In summary, MetaLeX aligns incentives so that IP and value accrue to the entity/DAO, and contributors are protected when doing the right thing, but cannot secretly capture value or harm the project without serious consequences.

## Q: How does MetaLeX handle edge-case failures, like a multisig stalemate (signers not agreeing or disappearing) or a critical smart contract bug locking up funds?

A: MetaLeX anticipated these scenarios and built in safety valves at both the legal and smart-contract level. Here are a few ways edge cases are handled:

* **On-Chain “Eject” and Signer Replacement** – If a multisig signer becomes uncooperative or incapacitated, MetaLeX’s BORG contracts allow for their removal or replacement. There is an Eject Implant module that, when enabled, lets an authorized party (often the DAO or a designated “Authority” address) remove a signer from the Gnosis SAFE, or lets a signer voluntarily resign on-chain
  github.com
  . Typically, the DAO (via a governance vote) would have to approve this action, preventing abuse. This ensures that if, for example, one signer disappears or refuses to sign anything (causing a stalemate), the community isn’t permanently stuck – they can vote to replace that keyholder and restore the BORG’s functionality.
* **FailSafe Mechanisms** – MetaLeX BORGs also feature a FailSafe module to recover funds in emergencies
  github.com
  . The FailSafe can be configured with conditions such as timeouts or specific triggers. For instance, the BORG could stipulate: “If the multisig hasn’t had any activity in 6 months and XYZ conditions are met, then funds auto-transfer to the parent DAO’s treasury.”
  followin.io
  This was implemented in the GAIB BORG: if the AI agent or its multisig fails to act for a defined period, the funds revert to a MetaLeX multisig as a backstop
  followin.io
  . FailSafes can also be triggered by a DAO vote or an oracle signal (like a “dead-man switch” condition) if something is clearly wrong. This means even if a contract upgrade is impossible or signers vanish, there’s a predefined way to claw assets back to safety.
* **Legal Override for Catastrophic Events** – In the bylaws and contracts, MetaLeX often includes clauses covering force majeure or “code failure” scenarios. Essentially, the parties acknowledge that if an extreme unforeseen bug or hack occurs – something that defeats the intended functioning of the code – they will cooperate to fix it under the guidance of the DAO or through legal means. In the GAIB charter, for example, there’s a provision that “code is law” except in cases of obvious hacks or blockchain failures
  followin.io
  . Those exceptions allow the community to treat such events as void/unauthorized and to seek remedies (like deploying a patch contract, or in worst case, going to court to freeze misappropriated funds). Additionally, because the BORG is a legal entity, it could file an insurance claim (if there’s coverage) or take emergency actions like hiring a forensic team without needing a new DAO vote in the heat of the moment – it has enough legal agency to respond quickly when required.

In essence, MetaLeX’s design acknowledges that despite best efforts, things can go wrong. By incorporating redundant controls – the ability to vote out a stuck signer, the ability to recover assets on timeout, and legal clauses for handling the truly unexpected – the system provides a path to recovery or resolution. These measures reassure stakeholders that a MetaLeX-based organization won’t be permanently paralyzed by a single point of failure. Even in edge cases, there are procedures to fall back on, governed by either on-chain consensus or legal processes, so the organization can adapt and continue rather than collapse.

## Q: Could there be a conflict between what DAO token holders decide and what the BORG’s directors or signers are legally obligated to do? What if the DAO’s vote goes against the directors’ fiduciary duties or vice versa?

A: MetaLeX’s entire approach is to align the DAO’s will with the legal entity’s duties as closely as possible, so direct conflicts are rare by design. The foundation documents of a BORG explicitly state that the entity’s purpose is to serve the DAO’s project and community
GitHub
. In legal terms, this means the directors’ primary “fiduciary duty” is effectively to carry out the DAO’s mission as defined in those documents. Thus, when a DAO vote is made in accordance with that mission (e.g. approving a budget or changing a protocol parameter), the BORG’s officers are actually fulfilling their duties by executing that decision. MetaLeX reinforces this alignment by embedding DAO oversight into the legal structure: many BORG bylaws include clauses that any major decisions require DAO approval (for example, adding a new board member or dissolving the entity must be voted on by token holders)
GitHub
. This legal requirement means the directors cannot take certain actions unilaterally even if they wanted to – the DAO’s decision is literally part of the corporate governance process, not just an informal influence. The software enforces the same; if bylaws say “DAO must approve X,” then the smart contracts will block action X until a DAO vote is confirmed on-chain
GitHub
. All of this ensures that in normal operations, there’s no divergence: the DAO’s vote and the directors’ legal obligations point in the same direction.

Now, consider a scenario where a DAO passes a proposal that might be problematic – say, something outside the BORG’s legal purpose or even illegal. Because the directors are real people with legal duties, they cannot blindly follow a DAO instruction that is blatantly unlawful (no one can be forced to perform an illegal act). The BORG structure anticipates this: the foundation’s purpose is usually narrow, and any action beyond that purpose is ultra vires (invalid). Directors are advised (and often explicitly required by the Participation Agreement) to politely refuse or delay implementation of any DAO proposal that would break laws or breach the foundation’s charter. For example, if a token vote somehow directed the BORG to distribute funds in a way that violates sanctions or securities laws, the directors’ fiduciary duty would compel them to not execute that, and instead work with the DAO to find a compliant alternative. Importantly, such clashes are extremely uncommon in practice – DAO communities rarely intentionally push for illegal outcomes, and MetaLeX’s legal architects help define the scope of the DAO’s authority up front to avoid ambiguous gray areas.

In practice, if a conflict did occur, there are safeguards: the foundation’s Supervisor (if one exists) could step in to enforce the bylaws, or the directors might call for a revote after explaining the issue to the community. Because MetaLeX entities are flexible, the DAO could even amend the bylaws (with proper approvals) to adjust the entity’s mandate if needed to resolve a conflict. The key point is that MetaLeX provides a structured process to handle any tension between code-governance and law-governance. Rather than a DAO being at the mercy of individual legal actors, or a director being left unprotected if they follow the DAO, both sides are integrated into one governance system. Hardwired accountability means the directors are bound to respect DAO decisions (so they can’t just ignore the community), but fiduciary duty and legal constraints mean the DAO’s power is exercised within the bounds of law (so the community can’t unknowingly force someone into a legal violation)
GitHub
GitHub
. This balanced design reassures institutional and legal-minded folks that DAO governance under MetaLeX won’t result in reckless or unlawful outcomes – there’s always a legal “circuit-breaker” if truly needed, but otherwise the DAO’s voice drives the bus.

In conclusion, MetaLeX’s approach to cybernetic law is all about marrying the innovative autonomy of blockchain with the practical safeguards of the legal system. By anticipating skeptical questions – from enforceability and jurisdiction to edge-case failures – MetaLeX has built a framework that stands up to professional due diligence. The enforceability of agreements is ensured by parallel legal contracts
GitHub
, the legal entities provide real-world interfaces and liability shields
GitHub
GitHub
, and the entire architecture is created to be as transparent, accountable, and resilient as possible. For legal professionals and regulators, MetaLeX demonstrates that decentralization need not mean lawlessness or chaos. Instead, it offers a model where code empowers organizations, and law fortifies that code – providing confidence that a MetaLeX-based organization can innovate quickly without leaving legal compliance and investor protections behind.

---


# 🔑 Key Terms

Source: https://metalex-docs.vercel.app/key-terms

## BORG

The [Cybernetic Organization (CybOrg or ‘BORG’)](/borg/what-is-a-BORG) is a traditional legal entity that uses autonomous technologies (such as smart contracts and AI) to augment the entity’s governance and activities. Just as sci-fi cyborgs (‘cybernetic organisms’) augment humans (natural persons) with robotic organs and limbs or microchip or optics implants, BORGs augment state-chartered entities (legal persons) with autonomous software such as smart contracts and AI. Crucially, legal entities that are BORGs do not merely use autonomous technologies as an incidental part of their business–instead, much like a human might have a robotic prosthesis surgically attached to his shoulder, BORGs are legally governed by autonomous technologies through tech-specific rules implanted in their charter documents.

Similar to DAOs, BORGs operate mostly in public and seek to utilize cutting-edge technology and economic incentive mechanisms to minimize traditional trust-based reliance on intermediaries, fiduciaries and other agents. Unlike a DAO, however, BORGs are not intended to be fully transparent, fully decentralized or fully autonomous or to rely on technological and economic incentive mechanisms alone; instead, they are incorporated as state-chartered entities and rely on a mix of legal, technological and economic mechanisms. BORGs appear in two broad flavors: tech‑augmented companies (“Business BORGs”) and trust‑mitigated entities that wrap or interface with a DAO (“DAO‑Adjacent BORGs”).

## BORG-CORE

Every BORG on [BORGs OS](/borg/BORGs-OS) has a [BORGcore](/borg/borg-core) smart contract as its heart. A BORGcore is a SAFE Guard combined with a standard ERC 4824 DAO interface.

## BORGs OS

The open-source operating system formerly called MetaLeX OS, serving as a shared framework for building and running BORGs and distinct from the more closed-source cyberCORP initiative. Learn more in the [BORGs OS guide](/borg/BORGs-OS).

## Business BORG

A BORG structured as a tech‑augmented company—e.g., a corporation whose shares are tokenized and programmable.

## cyberCORP

An [onchain business entity](/cybercorps) with tokenized securities; currently in a more closed-source, real-world-asset-focused beta track.

## cyberCert

An NFT-based security certificate that represents full ownership of a defined number of units in a cyberCORP. Each cyberCert corresponds to a legal share or bundle and can include metadata such as the holder’s identity or links to underlying agreements.

## cyberScrip

Fungible ERC-20 tokens that can be minted from or converted into cyberCerts. CyberScrip provides liquid, fractional claims to the underlying security but generally does not convey voting or dividend rights until reconverted into a certificate.

## Cybernetic Legal Agreement (Cybernetic Law Template)

A drafting approach that pairs legal text with code for interoperable, composable agreements, avoiding walled-garden SaaS tools. See the [Cybernetic Law introduction](/cybernetic-law/intro-to-cybernetic-law) for background.

## cyberSAFE

A tech-enhanced SAFE that executes signing and funding atomically, issues NFT-based security certificates, and automates deal logic onchain.

## DAO

There is no clear consensus about what a “DAO” is and how it should be defined, and a wide variety of organizations, communities, groups and entities are referred to as “DAOs”.

BORGs OS can plug-and-play with any of these conceptions, but the MetaLeX team prefers sticking to the literal meaning of the acronym “D.A.O.” — i.e., that DAOs must be fully onchain, decentralized and autonomous organizations, where:

* “Autonomous” means self-governing, trust-minimized and resistant to extrinsic exercises of power.
* “Decentralized” means that any residual human discretion (i.e., intrinsic modalities of power) are systematically dispersed over a large, agile, and potentially anonymous group of incentive-aligned persons.
* "Organization" refers to whatever structures or people are organized through the relevant autonomous decentralized technologies.

Put more simply, we view DAOs as limited-programmability robots whose rules and execution live entirely in code, with the limited programmability power widely dispersed among users who can only adjust the program in accordance with hard-coded meta-programming rules.

The riskiest liability vectors that could be associated with DAOs (clearly commercial and/or regulated offchain activities such as investing in new projects, hiring workers for salaried offchain jobs, etc.) should be treated as adjacent to the DAO rather than part of it, and should be housed in transparent, accountable, cybernetically enhanced DAO-adjacent entities: BORGs.

## DAO-Adjacent BORG

A BORG designed to work alongside a DAO, such as a foundation wrapping a DAO-controlled multisig and granting the DAO specific rights over the entity’s actions.

## Directors

Directors are individuals or entities with supervisory and/or operational authority over a legal entity. The exact scope and mechanisms through which directors manage an entity vary depending on the entity type, jurisdiction, and the entity's specific rules (especially Bylaws). In the context of BORGs, directors are likely to be owners of private-key-signers on one or more SAFEs/multisigs included in the BORG. BORGs OS recognizes a specific 'director role' within multisigs, which is basically a subset of signers a majority of whom *must* approve a given transaction for it to execute.

## Guardians

Guardian is a role with no well-defined corporate precedent, but was created as a hybrid entity/SAFE role specifically for BORGs. Guardians are members of a SAFE/multisig within a BORG that are on the SAFE primarily to provide additional security (through wider distribution of private keys/signing power) or quality control and compliance checks, but do not have authorities/powers as broad as those of directors. Part of the reason for having the guardian role is that the KYC/AML and compliance obligations of a legal entity's directors may be very high, meaning that it is hard to obtain a large number of directors to serve on a BORG, but, meanwhile, for reasons of increasing the security of tokens held by a SAFE, it is desirable to have a greater number of private key holders to lower the risk of 'wrench attacks' and other physical attacks as well as loss of keys or unavailability/downtime of signers in an emergency. A BORG's SAFE/multisig may therefore be required to require the approval of both a majority of the directors and some minimum number of guardians before a transaction will execute from the SAFE/multisig.

## Implants

Implants aka 'cybernetic implants' are SAFE Modules included in BORGs OS and designed to make SAFEs function as parts of BORGs.

## Legal Entity

A legal entity is an organization that is given independent personhood through the statutes of a nation or state. Legal entities are generally formed through 'incorporation' or a similar process--filing the entity's charter documents with the relevant nation or state and following specific rules and formalities in doing so. Legal entities generally confer 'limited liability' on their owners and operators--i.e., if the legal entity violates a law or breaches a contract, it is the entity that is liable (out of the assets owned by the entity) and not the individuals who own or operate the entity. Legal entities also allow for continuity of operations over time (for example, enabling long-term legal agreements, banking relationships, etc.) even as individual humans who operate the legal entity change over time.

## LeXscroW

[LeXscroW](/cyberdeals/lexscrow) is a suite of ownerless, condition-driven escrow contracts. Escrows enforce immutable release rules and automatically refund deposits when conditions are not met. Variants support bilateral token swaps, one-sided token sales or native-token escrows.

## MetaVesT

[MetaVesT](/cyberdeals/metavest) is an advanced vesting and token lockup protocol. It enables dual vesting and unlocking curves, option-style grants, group amendments and milestone-based releases while ensuring vested tokens cannot be rugged without consent.

## Multisig aka SAFE

See [SAFE aka Multisig below](/key-terms#safe-aka-multisig).

## Ricardian Tripler

A hybrid code/law primitive combining smart-contract code, legal text and parameters to deploy and enforce agreements entirely onchain. Explore its role in [Cybernetic Law](/cybernetic-law/intro-to-cybernetic-law#ricardian-triplers).

## SAFE aka Multisig

SAFEs, aka multisigs or 'smart accounts' are smart contracts implementing [the Gnosis SAFE source code](https://github.com/safe-global/safe-smart-account). These are smart contract multi-sig 'wallets' running on Ethereum that require a minimum number of private key signatures (corresponding to public addresses on Ethereum) to approve a transaction before it can be executed by the smart contract. Typically in the BORG context, each public/private key address is owned/controlled by a different human individual.

## SAFE Guard

SAFE Guards are smart contracts that constrain the functioning of an otherwise standard Gnosis SAFE, providing controlled access to specific recipients and contracts. This is accomplished by imposing pre-transaction-checks and post-transaction-checks on the SAFE. Guards ‘safeguard the SAFE,’ as it were. If the checks are not satisfied by a given transaction, the transaction will not execute (aka ‘reversion’).

A Guard is added to a SAFE by calling the setGuard() function of the SAFE with the requisite majority or plurality of signatures, parametrized to the smart contract address of the Guard. A SAFE can manage multiple Guards through an intermediary GuardManager contract. A typical use-case would be only allowing ‘owners’ of the SAFE (denominated by address) to execute a transaction (useful for MEV protection) or to only allow the SAFE to interact with certain whitelisted smart contracts via certain whitelisted functions on those smart contracts (useful to prevent accidental transactions or to limit the use of funds).

## SAFE Module

SAFE Modules (sometimes just referred to as 'modules') are smart contracts that extend or modify the functioning of an otherwise standard Gnosis SAFE. They can execute transactions on the SAFE that have not been individually approved by the requisite majority or plurality of signatures.

A Module is added to a SAFE by calling the enableModule() function of the SAFE with the requisite majority or plurality of signatures, parameterized to the smart contract address of the Module. A SAFE can manage multiple Modules through a ModuleManager contract. Typical use-cases would be giving another account a per-month ‘allowance’ it can spend out of the SAFE’s assets, timelocking an upgrade authority that may be exercised by the SAFE over a DeFi protocol, or facilitating Moloch-style ‘ragequit’ functionality where a signer can quit the multisig with a proportional share of its assets.

---


# 👋 Introduction

Source: https://metalex-docs.vercel.app/metalex-os-intro

MetaLeX OS is an open framework that brings legal entities and their operations — governance, agreements, transactions, and even equity — onto the blockchain.

In plain terms: **it turns traditional organizations into cybernetic organizations**. These entities have built-in smart contracts that handle many of the decisions, rules, and transactions that used to require manual or paper processes. The result is a legal entity that is faster, more transparent, and more autonomous.

By merging **code and law**, MetaLeX OS enables DAOs, companies, and funds to:

* Automate governance and compliance rules.
* Execute agreements and transactions directly onchain.
* Operate with the efficiency of DeFi while remaining legally compliant.

> **Key takeaway:** MetaLeX OS is like an *operating system* for legally compliant, blockchain-based organizations. It replaces “wet contracts” (traditional paper/legal agreements) with “dry code” (smart contracts) where possible, without losing enforceability.

---

## What's Inside

The documentation is organized into the major building blocks of MetaLeX OS:

* 🤖 **BORGs** — Cybernetic organizations (legal wrappers + smart contracts).
* 🏢 **cyberCORPs** — Onchain corporate structures for fundraising and equity.
* 💼 **cyberDeals** — Smart, enforceable funding agreements.
* ⚖️ **Cybernetic Law** — The principles and legal designs underpinning the system.

---


# BORGs OS

Source: https://metalex-docs.vercel.app/borg/BORGs-OS

BORGs OS is the 'operating system' for cyBernetic ORGanizations, also as known as 'BORGs'--legal entities that are tightly coupled with blockchain technology to achieve governance-accountable, trust-minimized, transaction-automated and legally optimized governance structures.

BORGs OS consists of a system of BORG-optimized smart contracts, legal documents, offchain legal entity structures, and a web application for monitoring, operating and transacting with BORGs.

Version 1 of BORG OS combines SAFE-compatible smart contracts and legal tooling to manufacture custom BORGs that separate powers between offchain entities and onchain automation. Built on the battle-tested Gnosis SAFE framework, it uses Guards to enforce pre- and post-transaction checks and Modules to automate actions like allowances, timelocks or ragequits. Together these components aim to create governance-accountable, trust-minimized and legally optimized multisig systems.

## Documentation Overview

* [Key Terms](/key-terms) — definitions of BORG and DAO vocabulary.
* BORGs — BORGs and BORGs OS.
  + [What is a BORG?](/borg/what-is-a-BORG) — background on BORG concepts.
  + [BORG Core](/borg/borg-core) — policy engine architecture.
  + [Borg Auth & BorgAuthACL](/borg/borg-auth) — central access control system.
  + [BORG Modes](/borg/borg-modes): [Whitelist](/borg/borg-modes/whitelist), [Blacklist](/borg/borg-modes/blacklist), [Unrestricted](/borg/borg-modes/unrestricted).
  + [Implants](/borg/implants): [Optimistic Grant](/borg/implants/optimistic-grant), [DAO Vote Grant](/borg/implants/dao-vote-grant), [DAO Veto Grant](/borg/implants/dao-veto-grant), [Eject](/borg/implants/eject), [Fail Safe](/borg/implants/fail-safe).
  + [Conditions](/borg/conditions) — rules that gate transactions.
  + [BORG Types](/borg/borg-types): [grantsBORG](/borg/borg-types/grantsborg), [securityBORG](/borg/borg-types/securityborg), [ipBORG](/borg/borg-types/ipborg), [finBORG](/borg/borg-types/finborg), [allianceBORG](/borg/borg-types/allianceborg), [genBORG](/borg/borg-types/genborg), [bizBORG](/borg/borg-types/bizborg), [devBORG](/borg/borg-types/devborg).
  + [BORG Command Center](/borg/borg-landing) — hub for operating a BORG.
    - [How-to BORG](/borg/how-to) — step-by-step interface guide.
    - [DAO Member Guide](/borg/dao-landing) — how token holders participate.
* [LeXscroW](/cyberdeals/lexscrow) — ownerless condition-based escrow, compatible with BORGs.
* [MetaVesT](/cyberdeals/metavest) — vesting and token lockup toolkit, compatible with BORGs.

---


# Borg Auth

Source: https://metalex-docs.vercel.app/borg/borg-auth

**BorgAuth** is the central access control contract in the BORG system, providing multi-level permission management for all BORG modules. In simple terms, it acts as a security hierarchy: *Owner*, *Admin*, and *Privileged* roles (represented by numeric levels 99, 98, 97 respectively) are assigned to addresses, defining what they can do. This ensures that BORG members operate under oversight – typically the DAO or a designated “Authority BORG” holds the Owner role (level 99), staying one level above regular BORG members (often Admin at 98). By structuring control in tiers, BorgAuth makes sure no single actor can exceed their authority, and that a higher authority can always intervene if needed. It’s an adaptable system as well: BorgAuth allows plugging in external **auth adapters** so that other contracts or DAO logic can grant permissions dynamically (for example, letting a DAO’s vote outcomes authorize certain actions). Every BORG contract (the core and each implant) inherits these rules by linking to a BorgAuth instance, creating a unified permissions framework across the entire BORG.

## Role Hierarchy and Purpose

BorgAuth defines three built-in roles with a clear hierarchy: **Owner (99)** as the highest level, **Admin (98)** as the next, and **Privileged (97)** as a base level. Higher numeric value means higher authority – an address with Owner role can do anything an Admin can (and more), and an Admin likewise outranks Privileged users. In practice, you might assign BORG safe owners as Admins, while the DAO’s multi-sig or an oversight contract is the sole Owner. This way, BORG members can perform day-to-day admin operations, but truly critical actions require the top-level role. The contract’s design enforces this by checking that a caller’s role is **greater than or equal** to the required level for an action. For a non-technical analogy, imagine a company: Privileged users are staff, Admins are managers, and the Owner is the executive – each level can do its job, but some decisions are reserved for higher-ups.

## Key Functions in `BorgAuth` (Access Control Logic)

BorgAuth’s functions manage roles and enforce permissions. Each function contributes to the security and flexibility of the BORG system’s access control:

* **`updateRole(address user, uint256 role)`** – Assign or change a user’s role. Only an address with Owner privileges can call this. It’s commonly used to add new BORG members or elevate/demote their permissions. For example, after deploying a BORG, the deployer (initial Owner) might call `updateRole` to make certain addresses Admins (role 98). Notably, the contract forbids an Owner from demoting *their own* role through this function (to prevent accidentally removing the only Owner). A new Owner must be appointed first before the original can relinquish control.
* **`initTransferOwnership(address newOwner)`** – Begins a two-step process to transfer the Owner role to a new address. Only the current Owner can initiate this. Calling this sets a `pendingOwner`. This function by itself doesn’t change any roles; it simply declares an intended new Owner. The requirement that `newOwner` cannot be the caller or the zero address ensures a valid handoff is being set up.
* **`acceptOwnership()`** – Finalizes the ownership transfer. The `pendingOwner` (and only that address) should call this to officially become the new Owner. Upon a correct call, the contract assigns role 99 (Owner) to the pending address and clears the pending slot. This two-step handshake (initiate then accept) protects against accidentally losing ownership: the transfer only completes if the designated new owner confirms it. Under the hood, `acceptOwnership` uses `_updateRole` to grant Owner status and emits a `RoleUpdated` event for transparency.
* **`zeroOwner()`** – Revokes the caller’s Owner status, **irreversibly** dropping them to no role (0). Only an Owner can call this, and doing so when they are the sole Owner will leave the contract with **no address holding Owner privileges**. This function is like a deliberate self-destruct of admin privileges and is used to renounce direct control. In practice, this might be done once a BORG is fully configured and handed off to autonomous governance – for example, the Owner could call `zeroOwner` after setting up all roles and thereby prevent any future manual tampering. **Warning:** After `zeroOwner`, no one can call `updateRole` anymore, so it effectively locks the role assignments permanently (which may be the desired security in a production phase).
* **`setRoleAdapter(uint256 role, address adapter)`** – Links an external authorization contract (adapter) to a specific role level. Only the Owner can configure this. This is a powerful extension point: when an adapter is set, BorgAuth will defer to that adapter’s logic to decide if a user is authorized for that role. The adapter must implement the `IAuthAdapter` interface (specifically, an `isAuthorized(address user) returns (uint256)`). During permission checks, if a user’s direct role is insufficient, BorgAuth calls `adapter.isAuthorized(user)` – if that returns a role >= the required level, the check will pass. In essence, role adapters allow *dynamic or external criteria* to grant roles on the fly. For example, you could attach a DAO governance contract as an adapter for the Owner role: instead of a single hardcoded Owner address, the DAO’s decisions (via the adapter contract logic) could determine who is treated as an Owner or when certain owner-level actions are allowed. This makes the ACL system modular and able to integrate with offchain or cross-contract permissions. The `AdapterUpdated` event logs any changes to adapters for transparency.
* **`onlyRole(uint256 role, address user)`** – The internal **authorization check** used throughout the system. This function (marked `view`) verifies that `user` has at least the given `role`, otherwise it throws an error. Here’s how it works: it looks up the user’s assigned role in the `userRoles` mapping. If the user’s role number is lower than the required level, it then checks if an adapter is defined for that role. If a `roleAdapter` exists, BorgAuth queries the adapter’s `isAuthorized(user)` result. Should the adapter report a role >= the required level, `onlyRole` considers the user authorized and returns without error. If neither the direct role nor the adapter’s authorization meet the criteria, it reverts with `BorgAuth_NotAuthorized`, stopping the calling operation. This function is the backbone of all the **modifiers** like `onlyOwner`/`onlyAdmin`; it centralizes the logic for role enforcement.
* **`_updateRole(address user, uint256 role)`** *(internal)* – A private helper that actually writes the role into the `userRoles` mapping and emits the `RoleUpdated` event. Both `updateRole` and the ownership transfer functions use `_updateRole` under the hood. Whenever someone’s role changes (be it granting Owner to a new address or revoking an Admin’s access), a `RoleUpdated(user, newRole)` event is emitted for offchain monitoring.

All these functions work together to maintain a robust permission structure. **Events** `RoleUpdated` and `AdapterUpdated` are emitted on changes, which helps with auditing and UI feedback (for example, front-ends could listen to know when a new admin is added or an adapter is set).

## Using BorgAuth: Typical Scenarios and Patterns

When a new BORG is deployed, the **BorgAuth contract is one of the first things created**, and the deploying account is automatically given the Owner role (99). This initial Owner can then configure the rest of the system: for instance, they might call `updateRole` to assign Admin role (98) to the addresses that will serve as the BORG’s multisig members. They could also set up a higher authority: for example, if a DAO’s address should oversee the BORG, the Owner might use `updateRole(daoAddress, 99)` to add a DAO-controlled account as an Owner too. Once setup is complete, ownership can be handed off securely – either using the safe two-step `initTransferOwnership/acceptOwnership` process, or by directly assigning a new Owner and then removing oneself. In one deployment script example, the deployer adds an `executor` address as a new Owner (`auth.updateRole(executor, 99)`) and then calls `auth.zeroOwner()` to renounce their own role. This effectively transfers full control to the `executor` address in a single sequence.

Another scenario is integrating a DAO voting contract via **role adapters**. Suppose you want the community (via a governance contract) to approve certain admin actions without hard-coding individual Admin addresses. You could write a custom `IAuthAdapter` that checks if a user’s address is whitelisted by the DAO or if a proposal passed, and have BorgAuth use it. By calling `auth.setRoleAdapter(auth.ADMIN_ROLE(), address(myAdapter))`, the BorgAuth will consult `myAdapter.isAuthorized(user)` whenever an Admin-level action is attempted by `user`. If, say, the adapter returns 98 for users holding a certain governance token, then those users would effectively have Admin rights in the BORG system without being explicitly added in `userRoles`. This pattern is powerful for linking onchain governance with BORG permissions.

## BorgAuthACL – Inherited Access Control in Every Module

While **BorgAuth** is the standalone ACL contract, **BorgAuthACL** is an abstract contract (also defined in `auth.sol`) that BORG modules inherit to easily use these permissions. BorgAuthACL stores an immutable reference `AUTH` to the BorgAuth instance and provides common **modifiers**: `onlyOwner`, `onlyAdmin`, `onlyPriv`, and a generic `onlyRole(_role)`. These modifiers are convenience wrappers that internally call `AUTH.onlyRole(requiredRole, msg.sender)` before executing the rest of a function. This means any function in a BORG contract tagged with `onlyOwner` will automatically enforce that the caller has role 99 in the shared BorgAuth, or the call will be rejected. For example, in the `borgCore` guard contract, critical configuration methods like adding a whitelisted recipient are defined as `function addRecipient(address _recipient, uint256 _limit) external onlyOwner` – only a caller with Owner role can execute that. By contrast, some routine updates in `borgCore` (such as setting the BORG’s human-readable identifier or adding a legal agreement URI) are marked `onlyAdmin`, so any Admin-level user can perform them. Similarly, implants inherit **BorgAuthACL** via a base class, so their functions can require appropriate roles. Most implants restrict dangerous operations (like changing limits or toggling settings) to the Owner, whereas actions meant for regular BORG members might allow Admin or Privileged access depending on the design. All these checks route back to the single **BorgAuth** source of truth, ensuring consistency.

Because each BORG module references the same BorgAuth contract for roles, updating someone’s role immediately affects permissions across the board. This central design avoids having to configure roles in multiple places – you manage roles in one contract and all guards, modules, and adapters respect those settings. It also enhances security by reducing complexity: the logic for authorization is centralized and auditable in BorgAuth, rather than spread throughout the code. In terms of modularity, if MetaLex introduces new implants or adapters, they can all hook into the existing BorgAuth system without modification. And if a particular BORG needs a custom role logic, the `setRoleAdapter` mechanism allows extending or overriding the basic role-checks in a clean way.

## Summary

In summary, `auth.sol` (BorgAuth and BorgAuthACL) is the linchpin of BORG contract security and governance. It establishes a clear chain of command (Owner > Admin > Privileged) and provides the tools to manage that chain – assigning roles, transferring ownership, removing superuser access, and delegating authority to external logic. BORGs and their associated components constantly interact with these functions: every restricted action in the BORG goes through a BorgAuth check to ensure the caller is allowed. For developers, BorgAuth offers an extendable, event-rich ACL pattern that can be tailored to complex governance setups. For general users or organizations, it means the BORG operates with checks and balances: the core can automate operations, yet always under the watchful eye of the roles defined in BorgAuth. This design keeps the BORG’s cybernetic autonomy aligned with the governance rules of its community or parent DAO, balancing **flexibility** with **security** in the MetaLex ecosystem.

## Code Example: Using BorgAuth in a BORG setup

```
Copy

// 1. Deploy the BorgAuth contract – the deployer becomes the initial Owner (role 99).
BorgAuth auth = new BorgAuth();
address deployer = msg.sender;
// auth.userRoles(deployer) == 99 (Owner by constructor)
 
// 2. Assign roles to BORG members and possibly a DAO oversight:
auth.updateRole(borgMember1, auth.ADMIN_ROLE());   // Make borgMember1 an Admin (98)
auth.updateRole(borgMember2, auth.ADMIN_ROLE());   // borgMember2 is also Admin.
auth.updateRole(daoMultisig, auth.OWNER_ROLE());   // Give the DAO’s multisig full Owner rights (99)
 
// (At this point, deployer, as Owner, has set up two Admins and added the DAO as co-Owner.)
 
// 3. Use the two-step ownership transfer if handing off control:
auth.initTransferOwnership(newOwner);    // Propose newOwner as the next Owner
// ... later, from newOwner’s account:
auth.acceptOwnership();                  // newOwner officially becomes Owner
 
// (Alternatively, the deployer could transfer by adding newOwner as Owner and then removing itself:)
auth.updateRole(newOwner, auth.OWNER_ROLE());  // grant Owner to newOwner
auth.zeroOwner();                              // deployer renounces its own Owner role
 
// 4. (Optional) Set up an auth adapter, e.g., to integrate DAO voting for Admin role:
auth.setRoleAdapter(auth.ADMIN_ROLE(), address(daoAdapterContract));
// Now, even if someone isn’t in userRoles with 98, the daoAdapterContract’s logic can authorize them.
```

---


# borgCORE

Source: https://metalex-docs.vercel.app/borg/borg-core

[`borg-core`](https://github.com/MetaLex-Tech/borg-core) is the onchain policy engine that powers MetaLeX BORGs. It combines a SAFE Guard with the standard ERC‑4824 DAO interface, making it the "heart" of every BORG on MetaLeX OS. By wrapping a SAFE with conditional, policy‑driven checks, it enforces which actions multisig members may execute and how outside authorities interact with the BORG.

## Architecture

* **Immutable modes** – each core is deployed in whitelist, blacklist or unrestricted mode. The mode cannot be changed after deployment.
* **BorgAuth** – access control layer that governs who may update policy or install implants.
* **Condition Manager** – modular AND/OR checks for per‑function or per‑contract conditions (e.g., timelocks, balances, oracle data).
* **Onchain references** – stores URIs for legal documents and the adjacent DAO's EIP‑4824 interface.
* **Implants** – SAFE Modules that plug into the core to add features such as optimistic grants, timelocks or signer ejections.

## Getting Started

Clone the repository and install dependencies:

```
Copy

git clone https://github.com/MetaLex-Tech/borg-core
cd borg-core
foundryup           # Update Foundry tools
forge install       # Install project dependencies
forge build --optimize --optimizer-runs 200 --use solc:0.8.20 --via-ir
```

The contracts can then be deployed with your preferred tooling.

## Next Steps

Learn about [Borg Auth & BorgAuthACL](/borg/borg-auth), [BORG modes](/borg/borg-modes), [conditions](/borg/conditions), [governance adapters](/borg/governance-adapters), [helpers](/borg/helpers), [hooks](/borg/hooks), and [implants](/borg/implants) to customize how your organization operates.

---


# BORG Modes

Source: https://metalex-docs.vercel.app/borg/borg-modes

The borgCore is the central hub for onchain BORGs. Its main purpose is to define the policy that governs which actions BORG members may take on chain. It extends the Gnosis Safe guard functionality.

**There are 3 types of BORG modes:**[## Whitelist

Only pre-approved addresses or calldata may execute transactions.](/borg/borg-modes/whitelist)
## Whitelist

* All transactions are blocked unless explicitly pre‑approved.
* Native token transfers must target whitelisted recipients and may include per‑tx limits.
* Calls are limited to whitelisted contracts and methods, with parameter constraints such as type, ranges or exact values.
* Best for highly conservative BORGs holding significant value, like finBORGs or tightly controlled grants programs.

## Blacklist

* Transactions are permitted by default except those explicitly denied.
* Addresses on the blacklist cannot receive transfers.
* Contract calls or specific methods may be blocked unless parameters satisfy defined constraints.
* Useful for trusted teams needing broad discretion while avoiding a short list of risky actions.

## Unrestricted

* No allow or deny lists are enforced.
* Signers have full discretion over transactions but can still use implants or other MetaLeX tooling for optional safeguards.
* Suitable for experimentation or situations where members are highly trusted.

Both whitelist and blacklist modes can enforce cooldown periods on certain calls to prevent spammy proposals or denial‑of‑service patterns.

---


# Blacklist

Source: https://metalex-docs.vercel.app/borg/borg-modes/blacklist

* Transactions are permitted by default except those explicitly denied.
* Addresses on the blacklist cannot receive transfers.
* Contract calls or specific methods may be blocked unless parameters satisfy defined constraints.
* Useful for trusted teams needing broad discretion while avoiding a short list of risky actions.

---


# Unrestricted

Source: https://metalex-docs.vercel.app/borg/borg-modes/unrestricted

* No allow or deny lists are enforced.
* Signers have full discretion over transactions but can still use implants or other MetaLeX tooling for optional safeguards.
* Suitable for experimentation or situations where members are highly trusted.

---


# Whitelist

Source: https://metalex-docs.vercel.app/borg/borg-modes/whitelist

* All transactions are blocked unless explicitly pre‑approved.
* Native token transfers must target whitelisted recipients and may include per‑tx limits.
* Calls are limited to whitelisted contracts and methods, with parameter constraints such as type, ranges or exact values.
* Best for highly conservative BORGs holding significant value, like finBORGs or tightly controlled grants programs.

---


# Conditions

Source: https://metalex-docs.vercel.app/borg/conditions

## Overview

A **BORG** can enforce complex rules on what actions its Gnosis Safe is allowed to execute. **Conditions** are the mechanism by which these rules are implemented onchain. The BORG’s **Condition Manager** (`conditionManager.sol`) is a modular component that allows multiple custom conditions to be defined and combined with logical operators. In practice, this means you can require certain criteria (time delays, token balances, approvals, etc.) to be met before specific Safe transactions or module functions are permitted. Conditions can apply globally to all actions or only to specific functions, giving fine-grained control over the BORG’s behavior.

**Key features of BORG conditions include:**

* **Multiple Condition Support:** You can attach any number of custom condition contracts to a BORG. Each condition is a separate smart contract implementing the `ICondition` interface (with a `checkCondition` function). This modular design means new conditions can be added or removed as needed, even after deployment (by authorized owners).
* **AND/OR Logic:** Each condition is labeled with a logical operator specifying how it combines with others – either **AND** (all specified conditions must be true) or **OR** (at least one must be true). This enables complex logic. For example, you could require **both** a time delay **and** a token balance threshold (AND logic), or allow an action if **any one** of several conditions is satisfied (OR logic).
* **Global vs. Function-Specific:** Conditions can be enforced **globally** (across the entire contract) or tied to a **specific function**. A global condition might apply to all actions (e.g. “the DAO’s token price must be above $X for any spending action”), whereas a function-level condition targets one particular method (e.g. “removing a member requires 5 signatures”). The Condition Manager supports both by maintaining a list of global conditions and a mapping of function signatures to condition lists.

## The Condition Manager Contract

The Condition Manager (`ConditionManager.sol`) is the component that stores and evaluates conditions for a BORG. Every implant module in a BORG inherits the Condition Manager, meaning each module gains the ability to check conditions on its operations. The Condition Manager itself extends the BORG’s access control (it inherits [`BorgAuthACL`](/borg/borg-auth)), so only authorized addresses (usually the DAO or an oversight authority) can add or remove conditions. This ensures that BORG members cannot arbitrarily change the rules; condition management is a privileged action (`onlyOwner`).

**Condition storage:** Internally, the manager keeps:

* An array `conditions[]` for **global conditions**, each with an address of a condition contract and a logic flag. These are evaluated for any check of the contract as a whole.
* A mapping `conditionsByFunction` that maps a function signature (`bytes4`) to an array of condition contracts (with logic flags) specific to that function. These are evaluated only when that particular function is invoked.

Each condition is expected to implement the standard interface `ICondition.checkCondition(address _contract, bytes4 _functionSignature, bytes data)` which returns `true` or `false`. The Condition Manager verifies that any added condition contract supports this interface via ERC-165; otherwise the addition is rejected.

**Adding & removing conditions:** The BORG’s owners (as defined by the ACL) can add a condition by calling `addCondition(op, conditionAddress)` for a global condition or `addConditionToFunction(op, conditionAddress, functionSig)` for a function-specific condition. Here `op` is the logic operator (`Logic.AND` or `Logic.OR`) to associate with that condition. The manager will ensure you don’t add duplicates or invalid contracts. Similarly, conditions can be removed via `removeCondition(index)` or `removeConditionFromFunction(index, functionSig)` by index.

**Condition evaluation:** The Condition Manager provides two mechanisms to enforce conditions at runtime: a function to check all global conditions, and a modifier to check function-specific conditions.

* **Global check (`checkConditions`)** – This view function iterates through every condition in the global `conditions` array and calls its `checkCondition`. The logic is straightforward: for each condition, if it’s labeled **AND**, a `false` result will immediately fail the entire check (returning false). If it’s labeled **OR**, a `true` result will immediately succeed the check (returning true). After looping, if no condition triggered an early return, the outcome is either true (if all AND conditions passed or if the last OR checked was true) or false (if none of the OR conditions were met). In essence: all AND-type conditions must pass, and at least one OR-type condition must pass. If no global conditions are defined, `checkConditions` trivially returns true. This function can be called within contract logic to enforce global constraints before executing an action.
* **Function-level check (`conditionCheck` modifier)** – For more granular control, the Condition Manager offers a `modifier conditionCheck()` that can be applied to individual functions. This modifier looks up any conditions associated with the function being called (`conditionsByFunction[msg.sig]`) and requires they be satisfied. It uses a similar AND/OR evaluation: each condition for that function is checked via `checkCondition`. If an AND-type condition returns false, the modifier triggers a revert (`ConditionNotMet`); if an OR-type condition returns true, it marks the requirement as fulfilled. After checking all, if at least one condition has been met (or if the function had no conditions), execution proceeds. If no condition was met, it reverts. By attaching this modifier to a function, the developer ensures that whenever that function is called, its specific prerequisite conditions are automatically enforced.

**Example:** Suppose a BORG implant wants to require that *either* a time delay has passed **or** a majority of owners have approved before allowing a certain operation. The DAO (as contract owner) could add two conditions – a TimeCondition and a SignatureCondition – both with logic **OR** for that function. The Condition Manager will then permit the function call if **any one** of those conditions is true (enough signatures collected or the time lock expired). If the requirement was that *both* a delay pass **and** approvals are given, the DAO would assign one condition as AND and the other as AND (or simply make them global AND conditions), forcing both to be true. This flexibility in logic composition is what allows BORG conditions to mirror real-world approval workflows and legal requirements.

## Implementing Custom Conditions (ICondition Interface)

Conditions are pluggable because each is a separate smart contract adhering to a simple interface. The `ICondition` interface defines one function, `checkCondition(address _contract, bytes4 _functionSignature, bytes data) external view returns (bool)`, which should return **true** if the condition is satisfied in the given context. The parameters give the condition contract context about what’s happening: `_contract` is typically the address of the contract whose action is being checked (for a BORG implant, this might be the Safe or module address), `_functionSignature` is the function being invoked, and `data` is any extra data (often unused or empty, but available for complex conditions).

To create a new condition type, you can **inherit the `BaseCondition`** abstract contract and implement the `checkCondition` logic. `BaseCondition` already implements the interface and includes an ERC-165 support check for ICondition, so inheriting it simplifies development. For example, a minimal custom condition contract could look like:

```
Copy

import {BaseCondition} from "./BaseCondition.sol";
 
contract MyCustomCondition is BaseCondition {
    // Example state or parameters
    address public immutable target;
    uint256 public immutable threshold;
 
    constructor(address _target, uint256 _threshold) {
        target = _target;
        threshold = _threshold;
    }
 
    function checkCondition(address _contract, bytes4 _func, bytes memory data) 
        public 
        view 
        override 
        returns (bool) 
    {
        // Your custom logic:
        // return true if condition passes, false if not.
        // (For example, ensure _contract holds at least `threshold` of some token, etc.)
        return /* bool expression */;
    }
}
```

Any state needed for the condition (addresses, numeric limits, etc.) can be stored in the condition contract. The Condition Manager treats this contract as a black box that returns a boolean when asked. This design means you can encode almost any rule as a condition contract – whether it’s checking an external contract’s state, aggregating signatures, or even querying an oracle (as long as the oracle value is fed onchain). Because conditions are external contracts, they can maintain their own internal state and update over time (for example, a condition contract might include functions to update thresholds or record approvals). The BORG modules don’t need to know the details; they simply call `checkCondition` on the condition contract when enforcing rules.

When deploying a BORG, MetaLeX provides a suite of **pre-built condition contracts** (detailed below) covering common use cases. These can be added directly to your BORG’s Condition Manager. If those don’t fit your needs, you can develop a custom condition contract using the pattern above, and as long as it implements `ICondition`, it can be integrated seamlessly.

## Built-in Condition Types

MetaLeX’s BORG core comes with several ready-made condition contracts in the `src/libs/conditions` library. These serve as examples and common tools that can be immediately applied. Below is a list of the main condition types and what they enforce:

* **TimeCondition:** This condition checks the current blockchain timestamp against a target time, either ensuring the time is *before* a specified moment or *after* it. It takes an immutable `targetTime` and a comparison mode (BEFORE or AFTER) on construction. The condition passes (returns true) only if the current time is on the correct side of the target time (e.g. AFTER a deadline, or BEFORE an expiration). This is useful for enforcing timelocks or scheduling restrictions (e.g., “action X cannot be performed until after date Y”).
* **BalanceCondition:** Checks an ERC-20 token balance against a threshold. This condition is constructed with a token address, a target account, an amount, and a comparison (GREATER or LESS). At check time, it reads the current token balance of the target address and compares it to the preset amount. It returns true if the balance is `>=` the amount (for GREATER) or `<=` the amount (for LESS). This can enforce that a certain account (such as the BORG’s Safe or a beneficiary) has a required amount of tokens. For example, you might require the Safe to maintain a minimum collateral balance before allowing new loans, etc. (Note: GREATER uses `>=` and LESS uses `<=` by implementation.)
* **ChainLinkOracleCondition:** Integrates an external price feed via Chainlink oracles. This condition is initialized with a reference to a Chainlink Aggregator (price feed), a target price (as an `int256`), and a comparison type (GREATER, EQUAL, or LESS). When checked, it fetches the latest price data from the oracle and compares it to the target price. The condition passes if the price relation matches the specified condition (e.g., price > target for GREATER). Importantly, this contract also ensures the oracle data is fresh: if the latest price update is older than a configured duration, it will revert with an error (treated as condition not met). This prevents actions from proceeding based on stale price information. A ChainLinkOracleCondition could be used to, say, allow a trade only if an asset’s price is below a certain threshold (perhaps for buyback conditions) or above a threshold (for distribution events), with the reliability of Chainlink feeds.
* **API3OracleCondition:** Similar to the Chainlink condition, but designed for API3’s oracle framework (dAPIs and Airnodes). It uses API3’s proxy interface to read a value and timestamp from a data feed. The condition compares the value to a target (GREATER/EQUAL/LESS) and likewise enforces a freshness threshold – if the data is older than a specified duration, it reverts as stale. Functionally, it accomplishes the same goal: gating actions based on an external data feed’s value. You would choose between ChainLinkOracleCondition and API3OracleCondition depending on which oracle network your data source is on.
* **SignatureCondition:** Implements a **multi-signature approval** requirement offchain from the Safe itself. You deploy it with a set of signer addresses and a threshold number of signatures, plus a logic mode (AND vs OR). Each designated signer can call the condition’s `sign()` function to register their approval (and `revokeSignature()` to withdraw it). When `checkCondition` is called, the contract counts how many signers have signed and compares against the threshold: if the condition’s logic is **AND**, it requires *all* specified signers to have signed (signatureCount == total signers). If the logic is **OR**, it requires at least the threshold number to have signed (signatureCount >= threshold). This condition is satisfied independent of the Safe’s own transaction approvals – it’s an additional offchain approval layer. For example, if a BORG Safe has 5 owners, a SignatureCondition could require that 3 out of those 5 call `sign()` before a certain action is allowed. You might use logic=AND for a unanimous consent requirement, or OR with threshold for majority consent. (Note: the `sign()` method in this condition is typically called as a separate transaction by the signers sometime before the guarded action is attempted.)
* **MultiUseSignatureCondition:** This is an extension of the signature condition concept, geared for **per-action approvals**. A MultiUseSignatureCondition (defined in `multiUseSignCondition.sol`) automatically pulls the BORG Safe’s owner list as the set of signers and sets a threshold on how many must approve. What makes it “multi-use” is that it tracks approvals *per specific contract call*. When signers call its `sign(address _contract, bytes _data)` function, they approve a particular target contract and calldata combination. The condition stores who signed what, and maintains a count of signatures for each unique `_contract + _data` combination. The check will return true if either the Safe itself signed (there’s a shortcut allowing the Safe to directly approve, treating a Safe execution as an automatic approval) or if the number of owner signatures for that exact call meets the threshold. This condition is useful for scenarios where each transaction or action needs a fresh set of approvals from owners. For instance, you could require that for any **specific** large transfer, at least N owners have pre-approved that *exact* transfer (by calling `sign` with the recipient and amount data). Since it ties signatures to the exact calldata, owners cannot blanket-approve a broad action – they must approve each instance, providing fine control.
* **DeadManSwitchCondition:** A special fail-safe condition that triggers after a period of inactivity. The idea is to detect if the BORG’s Safe has become dormant or if the members are incapacitated. The DeadManSwitchCondition is set up with a delay interval (e.g. 30 days) and the address of the BORG’s Safe. Authorized callers (like the DAO or designated guardians) can invoke `initiateTimeDelay()` to start the countdown and record the Safe’s current nonce. Once initiated, if the specified delay passes *without the Safe’s nonce changing* (meaning the Safe has not executed any transaction in that period), then `checkCondition` will return true. If at any time a Safe transaction occurs, the Safe’s nonce will increment, causing the condition to reset (or it can be manually reset via `resetTimeDelay()` by an authorized caller). This acts as an automatic trigger for emergency actions: for example, the BORG’s **FailSafeImplant** uses a DeadManSwitchCondition so that if the Safe owners do nothing for the delay period, the DAO is allowed to recover funds from the Safe. In practice, the DeadManSwitchCondition ensures that prolonged inactivity (which might indicate the BORG is defunct or its private keys are lost) can be detected and responded to onchain.

Each of these built-in conditions inherits from BaseCondition and implements the necessary logic in `checkCondition` as summarized above. They are meant to be building blocks – you can mix and match them in the Condition Manager to achieve the desired composite rules for your BORG. For example, a Grants BORG might use a TimeCondition (to enforce a vesting cliff), a BalanceCondition (to ensure a grantee has provided collateral), and a SignatureCondition (to require multi-party approval for releasing funds). All those can be added and configured via the Condition Manager.

## Using Conditions in BORG Modules

In a deployed BORG, **implants** (the modular contracts granting specific powers to the Safe) leverage the Condition Manager to guard their critical functions. As noted, every implant contract already includes the Condition Manager logic, so you can directly call `addCondition` or `addConditionToFunction` on an implant to configure its rules. The BORG’s admin (DAO or an authority BORG) typically sets up conditions during deployment or as part of governance decisions.

**Example – FailSafeImplant:** The FailSafe implant, which allows the DAO to claw back funds from the Safe in emergencies, uses conditions to ensure it only triggers under the right circumstances. In its `recoverSafeFunds()` function (which transfers assets out of the Safe), the implant includes both a function-level and a global condition check: it is declared with the `conditionCheck()` modifier and internally calls `if (!checkConditions(\"\")) revert` before proceeding. In a typical setup, the BORG’s admin might attach a DeadManSwitchCondition globally to this implant (requiring inactivity) and perhaps a SignatureCondition to the `recoverSafeFunds` function (requiring a certain number of DAO signatories to approve the recovery). As a result, the funds recovery will execute only if **both** the Safe has been inactive for the delay period **and** the required approvals have been given – otherwise the Condition Manager will block it, throwing a `ConditionsNotMet` error. This aligns with the idea that a fail-safe should only activate when clearly necessary (time elapsed with no activity) and agreed upon (multi-signature approval), protecting against premature or malicious triggers.

**Example – EjectImplant:** Another module, the Eject implant, allows removal of a BORG member from the Safe (and other membership management). Its functions like `ejectOwner` and `changeThreshold` are likewise protected by conditions. The code shows these functions use the `conditionCheck` modifier and then explicitly call `checkConditions` to enforce any global conditions. An admin could, for instance, add a condition requiring a DAO vote (perhaps through a SignatureCondition representing DAO multisig or an oracle reflecting an offchain vote) before any owner can be ejected. They might also add a TimeCondition to require a notice period before the change. When someone attempts to call `ejectOwner`, the Condition Manager will automatically verify those prerequisites and prevent the call if they aren’t fulfilled, emitting a `ejectImplant_ConditionsNotMet` error. Only when the conditions return true will the Safe’s owner removal actually execute, at which point the implant uses Gnosis Safe’s module mechanism to adjust the Safe’s owners list. This shows how conditions act as a safety net or checkpoint around sensitive governance actions.

**General usage workflow:** To apply conditions in your BORG, follow these steps:

1. **Deploy or identify the needed condition contracts.** For each rule, deploy the corresponding condition (or reuse an existing deployed one). For example, deploy `TimeCondition(targetTime, AFTER)` for a time lock, or `SignatureCondition([listOfSigners], threshold, OR)` for a multi-sig approval condition. Ensure the constructor parameters reflect your policy.
2. **Add conditions via the Condition Manager.** Using the BORG’s admin account (with `onlyOwner` permissions on implants), call the implant’s `addCondition` or `addConditionToFunction`. Specify the logic (AND/OR), the condition’s address, and (if function-specific) the function signature. For convenience, you can usually get a function signature in Solidity by using `MyImplant.contractMethod.selector`.
3. **Verify condition integration.** Once added, the condition is active. Any attempt to execute the guarded actions will now trigger the checks. It’s wise to test scenarios: e.g., try calling the function before the condition is met to ensure it correctly blocks (the transaction should revert with a ConditionNotMet error), then satisfy the condition (e.g., have signers call `sign()`, or wait until the time passes) and call again to confirm it succeeds.
4. **Monitor and update as needed.** Conditions can often be adjusted post-deployment. For instance, the threshold in a SignatureCondition can be increased by redeploying a new condition or, if the contract supports it, calling an update function (the MultiUseSignatureCondition has an `updateThreshold` method, guarded by its owner). If a condition becomes obsolete or an error is found, an authorized user can remove it via `removeCondition` functions, potentially replacing it with a corrected version. Always ensure any changes to conditions align with the BORG’s legal agreements, as these onchain conditions are meant to enforce those offchain rules.

By combining these condition contracts, a MetaLeX BORG can **programmatically ensure that Safe transactions adhere to the agreed governance policies**. The onchain Condition Manager acts as a real-time referee, checking every important action against a list of encoded rules. This structure provides a high degree of assurance that a BORG’s wallet will operate only within the bounds its stakeholders have set. And because the system is modular, it can evolve: new condition types can be introduced as new needs arise (for example, a KYC verification condition or other oracle-based conditions could be added in the future).

In summary, **BORG conditions** are a powerful feature that turn a basic multi-sig into a governed cybernetic entity. They allow encoding time delays, approvals, external data requirements, and more, directly into the Safe’s decision process. Using the Condition Manager and the suite of provided condition contracts (or your own custom ones), you can make your BORG’s smart contracts reflect complex organizational logic and legal constraints, ensuring that “code honors contract” within MetaLeX’s framework.

---


# Governance Adapters

Source: https://metalex-docs.vercel.app/borg/governance-adapters

Governance adapters bridge borgCORE with external DAO governance systems, allowing a BORG to route proposals through specialized voting contracts.

* [`baseGovernanceAdapater.sol`](https://github.com/MetaLex-Tech/borg-core/blob/main/src/libs/governance/baseGovernanceAdapater.sol) – abstract interface that defines common methods for creating, executing, and cancelling proposals and for retrieving vote totals.
* [`flexGovernanceAdapater.sol`](https://github.com/MetaLex-Tech/borg-core/blob/main/src/libs/governance/flexGovernanceAdapater.sol) – implementation that connects to Flexa DAO's FlexGov contract and exposes proposal and vote management tailored to that system.

These adapters let developers plug borgCORE into different governance frameworks without modifying the core contract itself.

---


# Helpers

Source: https://metalex-docs.vercel.app/borg/helpers

Utility contracts used across borgCORE live in the helpers library.

* [`signatureHelper.sol`](https://github.com/MetaLex-Tech/borg-core/blob/main/src/libs/helpers/signatureHelper.sol) – verifies signatures for Gnosis Safe transactions. It reconstructs the Safe's EIP-712 transaction hash, recovers signer addresses, and returns the set of signers up to the Safe's threshold.

---


# Hooks

Source: https://metalex-docs.vercel.app/borg/hooks

Hooks enable BORGs to run custom logic after key lifecycle events such as Safe recovery.

* [`baseRecoveryHook.sol`](https://github.com/MetaLex-Tech/borg-core/blob/main/src/libs/hooks/baseRecoveryHook.sol) – ERC‑165 compliant base contract that defines the `afterRecovery` hook.
* [`exampleRecoveryHook.sol`](https://github.com/MetaLex-Tech/borg-core/blob/main/src/libs/hooks/exampleRecoveryHook.sol) – minimal implementation emitting a `RecoveryHookTriggered` event when invoked.
* [`exampleRecoveryHookRevert.sol`](https://github.com/MetaLex-Tech/borg-core/blob/main/src/libs/hooks/exampleRecoveryHookRevert.sol) – sample hook that deliberately reverts, illustrating how hooks can halt the recovery process.

Developers can extend these contracts to integrate their own post-recovery behavior.

---


# Implants

Source: https://metalex-docs.vercel.app/borg/implants

Implants are plug-in SAFE modules for MetaLeX OS. They pair a `ConditionManager` with a [`BorgAuth`](/borg/borg-auth) contract so outside accounts or smart contracts can influence the BORG core under programmable rules. Implants add extra checks or execute transactions when conditions are satisfied.

Examples include:

* **Optimistic Grant implant** – lets a GrantsBORG issue grants within rate limits and routes larger requests through a DAO timelock and veto process.
* **DAO veto implant** – queues transactions with a timelock that the DAO can cancel.
* **Eject implant** – allows a signer to resign or be removed by the DAO, supporting rapid key rotation.
* **Fail Safe implant** – redirects funds to a predefined address if signer thresholds fall below a safe minimum.

Each implant can evaluate [conditions](/borg/conditions) such as signatures, time delays, token balances or oracle inputs to tailor policy.

---


# DAO Veto Grant

Source: https://metalex-docs.vercel.app/borg/implants/dao-veto-grant

Queues grant transactions and lets the DAO cancel them during a defined veto window before automatic execution by the BORG core.

* When a grant is proposed, the implant places it in a timelock.
* Token holders or guardians may submit a veto while the timelock is active.
* If no veto arrives before the window closes, the grant executes through the BORG core.

The veto window provides a final safeguard without slowing routine approvals.

---


# DAO Vote Grant

Source: https://metalex-docs.vercel.app/borg/implants/dao-vote-grant

Requires a proposal to win a DAO token holder vote before the BORG core releases funds.

* A grant proposal is created in the governance system and connected to the implant.
* After the vote, if quorum and approval thresholds are met, the BORG core disburses funds.
* Proposals that fail or expire are never executed, preserving community control of the treasury.

This ensures grants align with DAO consensus.

---


# Eject

Source: https://metalex-docs.vercel.app/borg/implants/eject

Removes a member or module from the BORG when predefined conditions are satisfied.

* A signer may resign and trigger key rotation.
* The DAO can force-remove compromised or inactive participants.
* Modules that fall out of compliance can be revoked.

The eject implant keeps BORG membership and connected contracts healthy over time.

---


# FailSafe

Source: https://metalex-docs.vercel.app/borg/implants/fail-safe

Provides emergency pause or recovery actions if the BORG core becomes compromised.

Typical configurations include:

* Monitoring signer thresholds and redirecting funds to a designated recovery address if too many keys are lost.
* Pausing outbound transactions while the DAO investigates suspicious activity.
* Offering an escape hatch that a guardian can trigger.

Use the fail‑safe as a last line of defense for safeguarding treasury assets.

---


# Optimistic Grant

Source: https://metalex-docs.vercel.app/borg/implants/optimistic-grant

Automatically approves grants after a waiting period unless vetoed by the DAO.

* Small requests execute quickly while giving token holders time to react.
* Any participant may submit a veto transaction during the cooldown.
* If no veto arrives before the window closes, the grant executes through the BORG core.

Optimistic grants accelerate routine disbursements without sacrificing accountability.

---


# Legal Approach

Source: https://metalex-docs.vercel.app/borg/legal-approach

Decentralized Autonomous Organizations (DAOs) often face challenges when interacting with the “real world” of law and commerce – they lack legal personality, cannot easily sign contracts or own offchain assets, and offer no liability shield to participants. **BORGs** (“Cybernetic Organizations”) are MetaLeX’s answer to this: a hybrid of code and legal entity that wraps a DAO workstream (like a multisig committee or council) in a formal legal structure. By doing so, a BORG provides the **best of both worlds**: the accountability and clarity of traditional entities plus the transparency and autonomy of blockchain-based governance. MetaLeX’s legal approach to BORGs centers on using **memberless, beneficiary-less Cayman Islands foundation companies** as the wrapper for these DAO-adjacent groups, coupled with carefully crafted bylaws that hard-code the DAO’s oversight and the entity’s onchain operations.

## Why Wrap a DAO Workstream in a Legal Entity?

Without any legal entity, a DAO’s multisig or working group exists in a gray area. It may inadvertently be treated as an unincorporated association or partnership, with **uncertain jurisdiction and potentially severe liability for participants**. Members of a multisig could be exposed to **joint-and-several personal liability** for actions taken on behalf of the group, and it’s ambiguous which country’s laws apply if the signers are globally distributed. This uncertainty extends to ownership of assets (Who “owns” a DAO’s treasury held in a multisig?) and the ability to engage offchain – e.g. signing contracts, holding domain names, or hiring contractors. In short, relying purely on code and informal social arrangements can leave real people with real legal risk and no formal recourse.

Wrapping the DAO-affiliated group into a legal entity **solves these problems**. The entity provides **legal personhood** (so it can contract and hold assets) and **limited liability** (so contributors aren’t personally on the hook for the entity’s debts or legal issues). It also anchors the organization to a specific **jurisdiction and legal framework**, avoiding a situation where every signer’s local laws might simultaneously apply. A legal wrapper helps delineate that the group’s activities are on behalf of the entity (and ultimately the DAO’s mission), not a personal venture of the signers. This clarity can be crucial for **regulatory reasons** as well – for example, to ensure a DAO isn’t viewed as an unregistered investment fund simply because it holds diverse assets. Certain assets or operations can be spun out to a BORG entity so that the DAO itself remains a pure protocol governance unit. In the Lido case, the community explicitly wanted to isolate an “alliance” initiative in a separate foundation to avoid Lido DAO appearing like it was managing a venture fund.

Beyond liability and regulatory clarity, having an entity allows the group to handle **offchain assets and services** that a smart contract cannot. For instance, a foundation can own web domains, custody legal rights/IP, employ contributors, and generally interface with traditional institutions on behalf of the DAO’s community. It provides continuity (the entity persists even as individual contributors come and go) and formalizes the **fiduciary-like responsibilities** of the group in a way that is enforceable.

## Why a Cayman Islands Foundation Company?

MetaLeX has experimented with various jurisdictional approaches, but the **Cayman Islands “foundation company”** has emerged as the preferred legal vehicle for DAO-adjacent BORGs. Cayman foundation companies are a relatively new type of legal entity (introduced in 2017) that combine features of trusts, nonprofits, and companies in a highly flexible way. Importantly, they can be structured to have **no shareholders (members)** and even **no beneficiaries**, operating solely for defined purposes. This makes them ideal for community-driven and non-profit-oriented endeavors like DAO support entities.

Key features of a Cayman foundation company that suit BORGs include:

* **No Ownership Shares:** The foundation has **no members or equity shareholders** by design. This means it isn’t “owned” by any individual – much like a DAO has no owners – and can be governed according to its charter rather than shareholder interests. The foundation’s board and officers manage it, but **their powers are constrained by the foundational purpose and bylaws**, rather than driven by shareholder profit motives.
* **Purpose-Driven, No Private Beneficiaries:** The entity can be **“beneficiary-less,”** meaning it isn’t obliged to distribute profits to any owners or beneficiaries. Instead, it exists to pursue a **specific purpose** (which in our case is aligned with supporting a particular protocol/DAO). For example, the Everclear Foundation was set up explicitly “to support the Everclear ecosystem” as its purpose, with no person entitled to the assets – all assets are to be used for that ecosystem’s benefit. Likewise, the proposed Yearn BORG’s foundation is legally barred from operating for the private benefit of the multisig signers; its charter limits it to supporting Yearn and its community goals.
* **Limited Liability & Tax Neutrality:** As an **exempted company** in Cayman, the foundation provides limited liability to its participants (directors, officers, etc.) – they generally won’t be personally liable for the entity’s obligations except in cases of egregious wrongdoing (fraud, gross misconduct). Cayman does not impose corporate income tax, and the entity is regarded as **tax-neutral**, which is beneficial when handling global crypto assets. (Any tax obligations typically fall on the recipients of funds, not the foundation itself.)
* **Governance Flexibility:** Cayman foundation companies allow highly customized governance structures. There is **no legal requirement for a traditional shareholder meeting or equity voting**, so the foundation’s **constitution (Memorandum & Articles) and Bylaws can define bespoke governance processes**. This flexibility lets us incorporate **novel rules tying the foundation to onchain governance**. For instance, the foundation’s bylaws can recognize a particular multisig or DAO vote as part of its decision-making apparatus. Cayman’s legal system is accustomed to creative structures for crypto projects, and local service providers (law firms, corporate services) are experienced in servicing such entities. In practice, we’ve found the Cayman framework amenable to embedding smart contract dependencies and DAO approval mechanisms directly into the legal documents.
* **Crypto-Friendly Jurisdiction:** The Cayman Islands has cultivated a reputation as a **crypto-friendly jurisdiction**, with many DAO-related entities (foundations, treasuries, protocol dev orgs) established there. The regulatory environment is currently favorable (no direct DAO-specific legislation that would constrain innovation), and the jurisdiction offers **specialized courts and common-law precedent** for handling complex business disputes if they arise. Additionally, Cayman permits **foundation companies to be structured with guarantor members or none at all**, and to appoint a **Supervisor** to oversee rule compliance if there are no members – a feature we heavily leverage (more on this below).

In summary, a Cayman foundation company can act almost like a *“corporate smart contract”* – a legal entity with no owners, a defined mission, and internal rules that make it behave in an automated, trust-minimized way. **MetaLeX uses this vehicle for most BORGs** because it aligns philosophically with DAO principles (no owner, mission-focused), while offering the practical benefits of an entity.

## Embedding DAO Oversight in Bylaws (“Hardwired Accountability”)

Forming the foundation company is just the start. The real magic is in the **Bylaws and charter documents** that MetaLeX drafts to bind the entity to the DAO’s will. These Bylaws serve as the “source code” of the legal entity, encoding constraints and governance processes that mirror the DAO’s preferences. We design them to be **as change-resistant and enforceable as possible**, so that all participants (and the DAO community) can trust the arrangement over time.

Some of the common provisions we include in BORG entity Bylaws:

* **Mission Lock-in:** The foundation’s purpose is explicitly defined to align with the DAO’s project. For example, the Lido Alliance BORG Foundation’s constitution restricts it to “furthering the Lido Alliance Program” and related community benefits. It **cannot pursue unrelated business** or stray from this mandate. Similarly, Yearn’s proposed Ychad Foundation must only support the Yearn protocol and community, and *“is not permitted to operate for the personal benefit”* of the multisig signers. This ensures the entity remains a servant to the DAO’s ecosystem, not a for-profit offshoot.
* **Onchain Asset Controls:** The Bylaws typically require that **all onchain assets of the entity are held in specific smart contracts** (usually a Gnosis SAFE multisig) and managed only through those contracts. In other words, the human directors cannot unilaterally move funds by, say, signing a bank wire or using a different wallet – they are legally obligated to use the designated onchain multisig for all crypto assets. The Bylaws often name the exact multisig address or set a process to update it with DAO approval, and declare that any asset outside of it is not considered legally held by the entity. This tie-in means *if a rogue actor tried to divert assets offchain, they’d be violating the Bylaws (and likely face legal action for breach of duty)*, giving an extra layer of assurance beyond the code itself.
* **DAO Approval for Key Decisions:** A hallmark of the BORG design is **formal DAO oversight rights** embedded in the legal docs. Certain critical actions by the foundation cannot happen without the DAO’s consent (usually expressed via an onchain vote or a Snapshot vote, depending on the DAO’s tooling). For instance, BORG Bylaws often require that **any change to the foundation’s directors or multisig signers be approved by both the foundation’s board *and* the DAO’s governance**. In Yearn’s case, this means Ychad multisig signers can only be added or removed if Yearn DAO voters also approve – a co-approval mechanism that is enforced both by software (SAFE modules) and by the legal agreement. Likewise, **dissolving the entity or amending its fundamental purpose** usually requires a DAO vote. The Lido Alliance BORG’s rules stipulate that Lido DAO must sign off on any liquidation of the foundation or any charter changes that would adversely affect the Lido community. These clauses give the DAO a direct veto and control, ensuring the BORG can’t, say, sell off assets or change allegiance without community agreement.
* **“Nuclear Option” Supervisory Powers:** Because the foundation has no shareholders, Cayman law allows the appointment of a **Supervisor** – a party with the power to oversee that the foundation follows its constitution. MetaLeX uses this feature to give the DAO an emergency brake. Typically, MetaLeX (or an affiliated neutral entity) is named as the initial **Supervisor** of the BORG foundation, with the understanding that this role can be transferred to a DAO-trusted entity later. The Supervisor role, as defined in the Bylaws, is usually **passive by default** – it monitors compliance but does not interfere in day-to-day operations. However, if something goes seriously wrong (e.g. the BORG’s management violates the rules or some catastrophic governance failure occurs), the DAO can trigger **Emergency Supervisor Powers** by onchain vote. When activated, these powers allow the Supervisor to take control of the situation: for example, to **remove or replace directors**, freeze certain actions, or initiate legal proceedings in the name of the foundation to protect the community’s interests. This is essentially an on-call backstop to enforce the community’s rights if the normal checks and balances fail. It greatly mitigates trust: the DAO doesn’t have to trust that the BORG directors will behave – if they seriously misbehave, the DAO can legally empower the Supervisor (bound by fiduciary duty) to step in and course-correct.
* **Hard-to-Amend Charter:** We draft the BORG’s governing documents to be **amendment-resistant**. In practice, the Bylaws include “meta-rules” stating that any material changes to these core provisions (purpose, DAO approval rights, asset rules, etc.) require the same dual approval – the board **and the DAO**. In other words, the directors cannot water down their own constraints without going back to the DAO for a vote. This entrenchment of the rules is crucial to maintain long-term trust: even years down the line, new management can’t quietly remove the DAO’s veto or the Supervisor clause unless token holders explicitly agree. The result is a **durable alignment** between the legal entity and the DAO’s governance.

All these provisions are not just on paper – they’re complemented by smart contract systems (the “BORG OS” toolset) that MetaLeX deploys. For example, when the bylaws say “membership changes need DAO approval,” we also install a **SAFE module** (implant) on the multisig that programmatically enforces that by requiring a signed DAO oracle approval before a new signer can be added. The legal and technical safeguards reinforce each other. The **BORG Participation Agreements** that each human signer enters (often by signing onchain) further ensure they acknowledge these rules and will abide by them. This multi-layer approach (law + code) is what makes a BORG truly *cybernetic*: the entity is legally governed by autonomous tech processes, and any attempt to step outside those processes is both automatically blocked onchain *and* illegal under the entity’s charter.

## Implementation: MetaLeX’s Role and Process

Setting up a DAO-adjacent BORG is a multidisciplinary effort – part legal structuring, part smart contract deployment. MetaLeX (comprised of a tech lab and a law firm working in tandem) **handles the end-to-end deployment** of these entities. On the legal side, this means working with Cayman counsel to register the foundation company, acting as or appointing initial directors, and drafting the **Memorandum & Articles of Association** and **Bylaws** in line with the DAO’s requirements. We ensure that a **professional Cayman director** is in place if required for local compliance (often a trusted service provider or individual who has no day-to-day role, but whose presence satisfies Cayman regulatory needs). That director’s powers are strictly limited by the Bylaws (e.g. they might be *required* to co-sign a dissolution or government filing, but they *cannot* initiate major actions unilaterally).

We also typically serve as the initial Supervisor (for practicality and because we authored the rules, we can monitor them). Over time, we can help transition the Supervisor role to a community-designated entity – for instance, Lido DAO has discussed moving the Supervisor duties to a new “Lido OpsBORG” entity controlled by Lido community members. All BORG signers (the individuals on the multisig or board) sign the onchain **BORG Participation Agreement** to formally bind themselves to act in the entity’s interest and follow the Bylaws. This creates privity of contract, so if a signer deviated (e.g. tried to execute an unauthorized transaction), both the foundation (through its Supervisor) and the DAO (as a third-party beneficiary) would have legal grounds to hold them accountable.

On the technical side, MetaLeX deploys the **SAFE multisig** and the suite of **BORG OS smart contracts** (guards, modules, oracles as needed) to implement the onchain side of governance. For example, we might deploy a Snapshot listening oracle and a custom Guard contract on the SAFE: together, these ensure that any transaction above a certain threshold or of a certain type is paused until a corresponding Snapshot vote by the DAO is verified. We rigorously test these implants and often get them audited; notably, we use the well-audited Gnosis SAFE as the core, without modifying its code. The BORG’s contributors then use a MetaLeX-provided web dashboard (or the SAFE interface) to operate, with the implants invisibly enforcing the rules.

From start to finish, MetaLeX’s interdisciplinary team (lawyers and engineers) work closely to **balance decentralization with practicality**. The goal is always to impose the minimum necessary trust assumptions – if something can be enforced by code, we do it; if not, we enforce it by legal means, and often we do both. This ensures the BORG can act efficiently (it has a small group of empowered agents who can sign transactions day-to-day) **without ever escaping the orbit of the DAO’s governance**. It’s a delicate design: too much autonomy and the DAO loses control; too much restriction and the entity can’t operate effectively. Our experience in multiple deployments has honed a model that achieves this balance.

## Real-World Examples of BORG Structuring

MetaLeX has helped design and launch **numerous BORGs** for major Web3 communities, each tailored to their specific needs but following the above principles. Some notable examples:

* **Lido Alliance BORG (2024):** A foundation company was created to wrap Lido DAO’s ecosystem alliance program, which brings outside projects (“Lido Allies”) together. The **Lido Alliance Foundation** is a memberless, non-profit Cayman foundation with bylaws that gave Lido DAO significant oversight. Its Board of Directors (initially two persons, with a handful of additional **Guardians**) can execute the program’s operations, but Lido DAO must approve any new Alliance members and co-approve changes in directors. All assets provided by alliance members are held in onchain multisigs controlled by the foundation, and *any use of those allied tokens requires Lido DAO’s co-signature* (a rule enforced via bylaws and EasyTrack onchain veto modules). The Lido BORG’s bylaws even allow Lido DAO to appoint an emergency supervisor and directly remove directors in case of severe misbehavior. This structure was presented to the Lido community, which signaled strong support, and the legal documents (Memorandum, Articles, Bylaws) were made public for transparency.
* **Yearn’s Ychad BORG (Proposed 2025):** Ychad.eth is a 6-of-9 multisig that has acted as Yearn Finance’s “Guardian” and treasury operator. MetaLeX proposed converting Ychad into a BORG by **registering an ownerless Cayman foundation** to “wrap” the multisig and formalize its relationship with Yearn DAO. Under this plan, the foundation would take ownership of Ychad’s assets and contracts, giving Ychad legal status and its signers legal protection. The foundation’s bylaws (nicknamed the “Ychad Constitution”) institute Yearn DAO approval rights: Yearn token holders must approve any changes to Ychad signers, and Ychad retains a defined veto power over certain DAO proposals (as already exists socially). The bylaws also mandate that Ychad’s powers *only* be exercised via the onchain SAFE and MetaLeX’s BORG modules (called “Mandatory Autonomous Systems” in the legal text). In effect, Ychad becomes a legally accountable extension of Yearn DAO – able to act swiftly on behalf of the DAO, but bound by both law and code to the DAO’s will. This proposal (YIP-XX) was put forth for community discussion in July 2025, highlighting how the BORG would secure Yearn’s multi-sig operations and pave the way for more onchain governance.
* **zkSync Security Council & Guardians (2023-24):** zkSync (a Layer-2 protocol) instituted a decentralized governance system which included a **Security Council** (a 12-member multisig with emergency upgrade powers) and a set of **Guardians** (a group with veto powers). MetaLeX helped structure these as BORG entities. Separate Cayman foundation companies were established to house each of these bodies (often referred to as the ZKSync Security Council Foundation and Guardians Foundation). The legal arrangements mirrored the governance design: Security Council members signed agreements with the foundation and agreed to be bound by the foundation’s bylaws. Those bylaws, in turn, enshrined that the Security Council multisig must act within parameters set by the onchain governance (e.g. only deploying emergency fixes and subject to later ratification). The **Guardians BORG** similarly had a foundation wrapping the veto multisig; its keyholders served as directors constrained by the DAO’s constitution. In zkSync’s docs, one can find references to the **Security Council entity’s bylaws** and the role of its Board in recommending changes, emphasizing that even these tech-savvy roles have a legal backbone. By using BORGs, zkSync ensured that the humans holding critical upgrade keys are part of a legal structure answerable to the community’s rules, not just a loose coalition of individuals. This significantly reduces risk in a high-stakes protocol upgrade context.
* **Everclear Grants BORG (2024):** Everclear, a DeFi project, launched a community grants program and chose to implement it via a BORG. The **Everclear Foundation** (Cayman foundation co.) was set up to receive ~10% of the token supply dedicated to ecosystem grants. This foundation is **“a shareholderless legal entity”** mission-bound to benefit the Everclear ecosystem. Its board (which included community members and an advisor from Connext, since Everclear originated from the Connext ecosystem) evaluates grant proposals. MetaLeX’s bylaws for Everclear Foundation require that any allocation of tokens follows the processes approved by Everclear DAO (via an onchain governance proposal EGP-26) and that unused grant tokens could be clawed back to the DAO treasury if the DAO votes to do so. The Grants BORG structure gave Everclear’s community confidence that the grant funds would be managed transparently and not misused: the foundation cannot, for example, spend those tokens on anything outside the grant mandate. If it attempted to, token holders have legal recourse and, through the bylaws, a say in correcting course. The establishment of the Everclear Grants BORG was documented in Everclear’s governance forum and passed via community vote in 2024, demonstrating the growing adoption of BORG frameworks beyond Ethereum into the broader crypto ecosystem (Everclear is aligned with the Connext network, bridging to Layer-2s).
* **Other Projects:** MetaLeX’s BORG approach has also been applied to various other communities and use-cases. For **Curve Finance (Curve DAO)**, a *“Curve Emergency BORG”* was conceptualized to formalize the emergency multisig that can pause the AMM contracts – again using a foundation so that keyholders are accountable and the DAO can enforce rules on their emergency powers. In the Cosmos realm, **Neutron** (a Cosmos Hub-connected chain) launched the first Cosmos-native Grants BORG, similarly using an entity to manage a community pool with onchain and offchain governance integration. **MetaCartel** and others have explored BORG structures for their own operational subgroups as well. The consistency across these examples is striking: whether the goal is managing grants, safeguarding upgrade keys, or running an alliance or research program, the BORG model brings a **trust-minimized legal wrapper** that reassures stakeholders and allows the DAO to scale its activities into the offchain world.

## Conclusion

MetaLeX’s legal approach to BORGs demonstrates that we can achieve decentralization with accountability – rather than choosing between a nebulous “code is law” collective or a fully traditional corporation, we create a **hybrid**. By leveraging memberless Cayman foundations and anchoring them to onchain governance through unalterable bylaws, **DAO-adjacent BORGs preserve the supremacy of the DAO** while providing the legal clarity and protection of a conventional organization. This approach appeals to both the **technically minded**, who value the onchain enforcement and transparency, and the **legally minded**, who value the clear allocation of duties and remedies. It’s a novel cypherpunk solution: using one of the most flexible entity forms available to ensure that even in the eyes of law, the code and community values will lead. As DAO ecosystems continue to grow and interact with real-world systems, we at MetaLeX believe the BORG framework – continually refined through projects like Lido, Yearn, zkSync, Everclear, and beyond – is a promising path to **organizing the disorganized** and giving DAO contributors the tools to operate safely at the intersection of blockchain and meatspace.

## Sources

* Delphi Labs – **“[Assimilating the BORG: A New Framework for CryptoLaw Entities](https://delphilabs.medium.com/assimilating-the-borg-a-new-framework-for-cryptolaw-entities-7910ec216a7b)”** (Apr 20, 2023)
* Yearn Improvement Proposal (YIP-XX) – **“[Convert Ychad.ETH Into a BORG](https://gov.yearn.fi/t/yip-xx-convert-ychad-eth-into-a-borg/14531)”** (Jul 2025)
* Lido Governance Proposal – **“[Organize the Lido Alliance Program as a Lido-DAO-Adjacent BORG](https://research.lido.fi/t/organize-the-lido-alliance-program-as-a-lido-dao-adjacent-borg/8173)”** (Aug 2024)
* MetaLeX (Gabriel Shapiro) – **[Yearn BORG Proposal, Part 1](https://metalex.substack.com/p/yearn-borg-proposal-part-1)** & **[Part 2](https://metalex.substack.com/p/yearn-borg-proposal-part-2)** Discussions
* Everclear DAO – **[Everclear Foundation Documentation](https://dao-docs.everclear.org/collective/everclear-foundation)** (GitBook, 2023)
* zkSync Governance Docs – **[Security Council and Guardians](https://docs.zknation.io/zksync-governance-procedures/zksync-governance-procedures-overview)** (2024)
* *Additional references:* [Lido Alliance BORG legal docs](https://docs.lido.fi/multisigs/alliance/); [Everclear Governance Lab summary](https://github.com/connext/everclear-gitbook); [Neutron Grants Program Proposal](https://forum.neutron.org/t/approved-proposal-14-launching-the-neutron-grants-program/95); [MetaLeX Newsletter and Whitepaper excerpts](https://metalex.substack.com).

---


# Cybernetic Organization (CybOrg or ‘BORG’)

Source: https://metalex-docs.vercel.app/borg/what-is-a-BORG

‘BORGs’ is short for ‘cyBernetic ORGanizationS’: BORGs are cybernetic entities. They are traditional entities (corporations, limited liability companies, foundations, etc.) whose charters legally embed autonomous software—such as smart contracts and AI—to conduct some or all of their operations and governance. Augmenting entities with autonomous technologies enhances efficiency, trust minimization and ‘social scalability’ while reducing liability and regulatory risks.

For a more detailed description, see this Delphi Labs' seminal [article](https://delphilabs.medium.com/assimilating-the-borg-a-new-cryptolegal-framework-for-dao-adjacent-entities-569e54a43f83) on BORGs from 2023.

BORGs generally fall into two broad categories:

* **Tech-augmented business entities** – independent business entities that embed autonomous software into their operations; at MetaLeX we call these “bizBORGs” or "cyberCORPs," but more often (including in these docs) use the term "cyberCORPs".
* **Trust-mitigated, DAO-adjacent non-business entities** – special-purpose entities funded by and undertaking activities beneficial to larger DAOs/communities under carefully constructed checks and balances and not primarily devoted to for-profit/business use-cases. We typically refer to such entities simply as "BORGs" even though they are a subtype of BORG.

There can be entities 'in between' these two categories--for example, a "public benefit corporation" is like a typical corporate business company, but the management may be required to consider the broader interests of a particular community or society at large.

DAO-adjacent BORGs can take many forms—common examples include **security BORGs** for emergency controls, **grants BORGs** to distribute treasury funds, or **IP BORGs** to steward trademarks and software rights.

Some charters even require all digital assets to sit in a public multisig at a specified address. The DAO can veto changes to that multisig or revoke its powers entirely, ensuring onchain transparency with legal accountability.

From the outside BORGs may operate like DAOs, but their legal entity charters enforce automated decisions for accountability.

Rather than wrapping DAOs in new liabilities, the BORG framework preserves the original vision of DAOs. By re‑characterizing certain “DAOs” as business BORGs and shifting legally sensitive activities to DAO‑adjacent BORGs, true DAOs can stay lean, autonomous, and cypherpunk.

MetaLeX’s mission is to fuse law and code. Our [BORG OS](/metalex-os-intro) provides a customizable suite of SAFE-compatible smart contracts and legal tooling that make it easy to deploy trust-minimized, legally optimized multisig governance for these entities.

BORGs are part of a new design space where hybrid/code law solutions should be guided by the following design principles:

**Principle 1 – Maximize Deference to Autonomous Code**

Maximize the role of trust-minimized smart contracts and other autonomous or decentralized technologies to handle as many deterministic functions as possible. This includes using autonomous technologies such as smart contracts as replacements for traditional legal arrangements that prescribe relatively deterministic rules.

Minimize the role of traditional law (TradLaw) tools such as ‘wet contracts’ and litigation as much as possible in the operations and governance of legal entities and other legal arrangements. When ‘wet contracts’ are required, they should be designed to refer and to defer to the outcomes of autonomous code as much as possible

**Principle 2 – Qualify Autonomous Code Where Necessary**

Identify edge-cases in which Principle #1 may lead to unacceptably unfair, unjust, or unanticipated results and use TradLaw mechanisms to ensure that autonomous code is not outcome-determinative code in these particular circumstances. Instead, offchain legal mechanisms can kick-in to handle these special scenarios in a more fair, just, and legal way.

**Principle 3 - Use TradLaw Mechanisms to Constrain Offchain Agents**

If there are humans in the loop and such humans, despite the use of autonomous technologies, remain in positions of ‘trust’ and thus retain significant potential for acting based on conflicts of interest, abusing their discretion, adversely colluding, cultivating information asymmetries, free-riding, or otherwise abusing their power, we must use traditional ‘wet contracts’ and other legal tools to define their rights and obligations clearly and hold them accountable if such trust is indeed abused. Principle #3 may also be seen as a special sub-case of Principle #2, since in such cases autonomous code by itself is inadequate to achieve trust-minimization or social scaling—however, under Principle #3, law is used more as a supplement to code than as a fallback mechanism for code failures.

---


# cyberCORPs OS

Source: https://metalex-docs.vercel.app/cybercorps/cybercorps-os

cyberCORPs OS is the operating system for programmable corporations. It bundles smart contracts, legal agreements, offchain entity structures and web tooling to help founders run compliant onchain companies.

Version 1 combines fundraising modules, governance features and cap table management to create a code-assisted corporation.

## Documentation Overview

* [Key Terms](/key-terms) — definitions of MetaLeX vocabulary.
* cyberCORPs
  + [What is a cyberCORP?](/cybercorps/what-is-a-cyberCORP)
  + [Onchain Capital Structure](/cybercorps/onchain-capital-structure)
  + [Governance and Officers](/cybercorps/governance-and-officers)
  + [Launching a cyberCORP](/cybercorps/launching-a-cybercorp)
  + [Future Integrations](/cybercorps/future-integrations)
  + [Sources](/cybercorps/sources)
* cyberDeals
  + [cyberRaise](/cyberdeals/cyberraise)
  + [LeXcheX](/cyberdeals/lexchex)
  + [MetaVesT](/cyberdeals/metavest)
  + [LeXscroW](/cyberdeals/lexscrow)

---


# Future Integrations

Source: https://metalex-docs.vercel.app/cybercorps/future-integrations

The cyberCORP framework is under active development, and MetaLeX has a roadmap of integrations and enhancements that will make these onchain corporations even more powerful. Here we outline some expected or potential future features, and discuss how cyberCORPs could fit into the broader MetaLeX vision of cybernetic law.

BORG Implants for Compliance: One intriguing idea is combining cyberCORPs with BORG modules to automate compliance and governance beyond just fundraising. For example, a cyberCORP could “implant” DAO-like components (from the BORGs OS library) into its operations – such as an onchain governance module for shareholders or an AI-driven compliance agent. In practice, this could mean the corp’s bylaws are enforced by smart contracts (a concept already present in BORG charters) or that certain decisions are delegated to decentralized processes. A BORG implant might handle routine compliance tasks (filings, checks) automatically. Since BORGs are “legally-wrapped autonomous organizations,” a cyberCORP could potentially spin up an internal BORG (say, a sub-DAO for community governance of a product, or an AI-run subsidiary) and have it linked to the parent corp’s cap table or contracts. This fusion would ensure human officers and AI/DAO processes work in tandem – e.g. an automated system that monitors transactions for legal compliance and has authority (via [BorgAuth](/borg/borg-auth) roles or multisig) to veto or flag operations that violate preset rules. Such hybrid compliance could reduce the burden on legal teams by catching issues in real-time and providing provable oversight.

DAO and Onchain Community Bridges: MetaLeX recognizes that many companies (especially Web3 projects) straddle the line between traditional corporations and decentralized communities. Future cyberCORP releases may include bridges to DAO governance frameworks. For instance, a cyberCORP could allow a DAO (token-holder community) to control certain votes or even hold an equity stake represented onchain. One could imagine a structure where the corporation issues a class of non-voting stock or a governance token that is held by a DAO treasury – linking the DAO’s decisions to corporate actions. Another scenario is enabling shareholder DAO voting: shareholders could connect their wallet and vote on corporate resolutions onchain, similar to how DAO token voting works, with the results enforceable by the cyberCORP contracts (this is on the roadmap: onchain, DAO-like security-holder voting). This would modernize shareholder meetings and proxy voting, making them continuous and transparent. Additionally, a cyberCORP might integrate with DAO tooling (like Snapshot or onchain voting contracts) so that even non-crypto shareholders can delegate to or participate in decentralized governance processes.

Onchain Accounting and Finance: As more of the company’s lifecycle moves onchain, there’s potential to integrate onchain accounting systems. Revenues in crypto (or even in stablecoins) could automatically feed into accounting smart contracts that classify and report financial data. Think of a future where the corporate treasury is managed by a combination of smart contracts: one that handles payroll (perhaps streaming salaries via something like Sablier), one that handles dividends (distributing stablecoins to tokenized shareholders according to their share classes’ rights), and one that keeps an immutable ledger of all financial transactions for audit purposes. Since cyberCORPs already keep the cap table onchain, extending that to a full “crypto Carta” is natural – MetaLeX explicitly mentions plans for a crypto Carta for cap tables and beyond, implying tools to manage equity plans, model dilution, and track ownership changes with blockchain accuracy. Automated dividend contracts could, for example, check for preferred stock preferences and allocate profits accordingly: if a certain class of preferred stock is entitled to 5% of dividends until a hurdle is met, a smart contract could enforce that split programmatically. Similarly, if the company undergoes an exit or liquidity event, the payouts to each share class can be computed onchain based on token holdings, eliminating manual waterfall spreadsheets.

Regulatory Oracles and Identity: Bridging offchain legal requirements into onchain action is a frontier that cyberCORPs may tackle via oracles. For compliance with securities laws, the identity and accreditation status of investors often matters. We anticipate integration of identity/KYC oracles such as those that can attest “Wallet X is owned by an accredited investor in the US” without revealing the owner’s full identity onchain. A cyberCORP might use such an oracle such that when a share token is about to transfer, a transfer restriction hook (already supported in the CyberCertPrinter contracts) calls an oracle to ensure the new holder meets certain criteria (e.g. not from a sanctioned region, or is within the shareholder limit for an S-Corp, etc.). Regulatory oracles could also feed in real-world events – for example, if a court order is issued affecting the company’s shares, an oracle could inform the smart contract to pause transfers. While these aspects are speculative, they align with MetaLeX’s ethos of fusing offchain legal arrangements with onchain protocols. In fact, achieving reliable real-world data inputs (laws, court decisions, compliance checks) onchain is often called a “holy grail” of legal tech, and cyberCORPs could be a driving use-case to push that forward.

Enhanced Upgrade and Module Ecosystem: As MetaLeX grows, we expect a library of modules that cyberCORPs can opt into. The Upgrade Factory might allow installing new extensions – for instance, a “Board of Directors Module” where board resolutions are tracked onchain and maybe even voting happens onchain with weighted NFT “board seat tokens.” Another could be a Litigation & Dispute Module that, in case of disputes, interfaces with arbitration smart contracts or onchain courts to resolve issues per the specified dispute resolution mechanism. We might also see integrations with insurance protocols (to provide things like directors & officers insurance via smart contract) or with onchain incorporation services (imagine a smart contract that can actually interface with a state’s API to file a certificate of incorporation when a cyberCORP is launched – creating the legal entity in the real world simultaneously with the onchain instantiation).

Community Questions and Ongoing Research: The MetaLeX community and early adopters have posed important questions that are still being researched. For example: How will jurisdictions recognize onchain stock ledgers across borders? Delaware might be friendly, but what about other countries’ corporate laws – will a cyberCORP be valid in, say, Singapore or Germany? Also, what happens if a shareholder loses access to their wallet (private key) – can the cyberCORP implement a “stock reissuance” procedure analogous to affidavit of loss for certificates? (Possibly via an onchain vote of the board to void the lost token and re-mint a new one to a new address.) Another question: How to handle stock splits or mergers onchain? These corporate actions might need coordinated updates to many token IDs and possibly new token contracts. MetaLeX likely will address these with batch operations or new contract patterns. Legal enforceability is of course a constant discussion: each cyberCORP agreement still relies on the legal system to some extent (e.g. an investor might still sue if something went wrong). The question is how much can be done by code to prevent disputes and whether courts will directly accept onchain records as authoritative (early signs are positive, but precedents will be set in coming years).

Tax and regulatory treatment of cyberCORPs will continue to be evaluated. With dividends and assets onchain, how do reporting and taxes get automated? MetaLeX’s team includes tax law expertise, so future versions might incorporate tax optimization logic (for example, handling withholding taxes onchain when paying a dividend to a foreign token-holder, etc.). In conclusion, cyberCORPs represent a bold melding of corporate law with blockchain tech. They fit into the broader MetaLeX ecosystem as the vehicle to put real companies onchain, complementing BORGs (which target decentralized orgs) with something for founders who still need a conventional company structure. As the technology and legal environment mature, we expect cyberCORPs to gain capabilities – from onchain cap table management that rivals traditional services, to automated compliance and cross-chain integrations – pushing the envelope of what a 21st-century corporation can be. MetaLeX envisions a future where entities and agreements are fully cybernetic: self-executing, interoperable, and global by default. cyberCORPs are a major step toward that future, and ongoing community feedback and research will guide their evolution. (If you have a feature request or a question that wasn’t covered, MetaLeX encourages engaging via their community channels – this is a frontier being built collaboratively.)

---


# Governance and Officers

Source: https://metalex-docs.vercel.app/cybercorps/governance-and-officers

Operating a cyberCORP day-to-day involves both onchain code and offchain people. The governance model combines a [BorgAuth](/borg/borg-auth)-based role system with traditional corporate roles (officers, directors, etc.), allowing a company to define who can do what in the smart contracts. When a cyberCORP is created, it comes with a [BorgAuth](/borg/borg-auth) access control contract instance. BorgAuth is MetaLeX’s hierarchical role manager (originally developed for BORGs) that the cyberCORP leverages to manage permissions onchain. The founder or creator of the cyberCORP is typically assigned the highest role (Owner) by the factory at deployment GitHub GitHub. This Owner role (analogous to an ultimate admin) can then add others and assign them roles. In corporate terms, you might give your CFO or general counsel an “Officer” role onchain to let them, say, co-sign certain transactions or update certain records. Using the company officer functions provided, the Owner can call addOfficer(address, role) to add a new officer (e.g. a new executive or director) and removeOfficer(address) to revoke someone’s role GitHub GitHub. Under the hood, this updates the BorgAuth roles: for example, officers might be assigned a specific numeric role code (the contracts often use 200 for officers) which grants them predefined permissions. The cyberCORP smart contracts check these roles on sensitive functions. For instance, only an address with Owner role can change fundamental parameters like the company’s legal details or upgrade the contracts, whereas an address with an Officer role might be allowed to propose deals or manage certain tasks. This system provides fine-grained, onchain control over corporate authority. It’s akin to how a board of directors authorizes officers to act on behalf of a company – but here the authorization is enforced by code. If someone is removed as an officer, their onchain role is revoked immediately, preventing any further authorized actions.
BorgAuth roles also govern the Round Manager, controlling who can approve rounds, toggle transferability, accept or reject EOIs, and change restrictions.

The CyberCorp contract itself stores key corporate metadata which can be updated through governance actions. These include: the official entity name (e.g. Acme, Inc.), the entity type (“Corporation”, “LLC”, etc.), the jurisdiction of incorporation (e.g. Delaware, USA), and contact or identifying details GitHub. It also holds a default dispute resolution mechanism (for example, specifying arbitration or a certain court jurisdiction to handle legal disputes) GitHub. These fields are set at initialization (drawn from the inputs when the cyberCORP is deployed) and can be updated by authorized roles if needed (e.g. if the company reincorporates in a new state or changes its name) GitHub. Having these onchain is important not only for record-keeping but because they can be referenced by other parts of the system – for instance, generating legal documents or ensuring filings are correct.

Another important field is the companyPayable address GitHub. This is essentially the blockchain address representing the company’s treasury or bank account. Funds from deals (and potentially other onchain revenues) will flow into this address. In practice, this could be the address of a multi-signature wallet controlled by the company’s management. The cyberCORP Owner can update the payable address as needed (for example, if the company adopts a new multisig or a finance department wallet) via an onchain call GitHub. By centralizing all incoming payments to a known address, the cyberCORP makes it easier to track revenue onchain and even automate things like dividend payouts or expense management in the future.

It’s worth noting that cyberCORP contracts are upgradeable, reflecting the evolving nature of law and business needs. MetaLeX uses an upgradeability pattern (UUPS proxies or beacon proxies) for the CyberCorp core, IssuanceManager, and DealManager. The cyberCORP has an upgradeFactory address on record GitHub, which is authorized to perform contract logic upgrades. In practical terms, this means the company (with whatever governance process it chooses – perhaps board approval or tokenholder vote) can decide to upgrade the smart contracts to newer versions if bugs are found or features need to be added. For example, if regulations change and a new compliance module is required, MetaLeX Labs could publish an upgraded contract, and the cyberCORP’s Owner (or upgradeFactory) could install that upgrade without disrupting the organization’s operations or data (all shares and deals remain intact). This is crucial for longevity: a corporation might exist for decades, and the tech must be able to adapt over time. Of course, upgrades are permissioned – only the designated governance authority can execute them, preventing unauthorized changes. In the MetaLeX paradigm, this provides a balance between “code is law” and real-world flexibility: the code governs day-to-day, but the humans behind the company aren’t irreversibly locked into one code version if it proves imperfect.

In summary, governance in a cyberCORP is a hybrid of familiar corporate control and onchain rigor. Roles like CEO, CFO, directors, etc., map to onchain roles that gate smart contract functions. Company resolutions (like adding an officer or changing a detail) translate to transactions that update contract state. And because of the BorgAuth ACL, even if a private key is compromised or an officer goes rogue, their powers are limited by the role they hold – and removals are immediate and trustless once executed. It’s a system designed to make corporate governance more transparent and foolproof, while still allowing human judgment at the helm.

---


# Launching a cyberCORP

Source: https://metalex-docs.vercel.app/cybercorps/launching-a-cybercorp

Starting a cyberCORP on MetaLeX is intended to be straightforward for both crypto-native founders and those without blockchain expertise. There are two primary pathways to launch: via the web application interface or by interacting with the smart contracts (for developers and advanced users). Underneath both methods, the same factory contracts are used – ensuring that a cyberCORP created through the UI is functionally the same as one created via code.

Using the Web App: On the cyberCORPs app site, a founder can click “Start a Raise” (or a similarly labeled button) and will be guided through the process. The first step collects basic corporate information – company name, entity type, jurisdiction, etc. – and then asks whether the founder is launching a multi‑investor round or a bespoke single‑investor deal. Choosing **Round** prompts for inputs such as the series type, raise cap, ticket sizes, and round style, and the system wires these details into a Round Manager that will handle issuance for the round. Choosing **Deal** continues directly to the single‑investor flow. Behind the scenes, when the founder submits this form and confirms the transaction in their wallet, the app calls the CyberCorpFactory smart contract to deploy a new cyberCORP instance GitHub GitHub. The factory takes a unique salt (to allow deterministic addresses and prevent duplicates) and the provided inputs, then performs a sequence of actions in one go:
It deploys a fresh [BorgAuth](/borg/borg-auth) contract and immediately assigns the founder’s wallet the Owner role (this ensures the creator will control the new corp’s permissions) GitHub.
It deploys a new CyberCorp contract (the core proxy that represents the company onchain) via a minimal proxy or beacon.
It simultaneously deploys an IssuanceManager and a Round Manager for the corp (each as their own upgradeable proxy) and wires their addresses into the CyberCorp’s state. A Deal Manager can also be deployed for bespoke one‑off deals, but the Round Manager is the default orchestrator for multi‑investor fundraising rounds GitHub GitHub.
It also sets up a CyberCertPrinter implementation reference and URI builder for token metadata, so that the IssuanceManager can spawn actual certificate contracts as needed GitHub GitHub.
All of this is abstracted away from the user; from their perspective, within one transaction their new cyberCORP “organization” is created onchain. The factory emits a CyberCorpDeployed event with the addresses of the new contracts GitHub, which the front-end listens for to confirm deployment. If the founder was creating a raise immediately (which is likely the case when using the UI for a SAFE), the CyberCorpFactory can go a step further via a convenience function: deployCyberCorpAndCreateOffer GitHub GitHub. This performs the steps above and then initializes a deal offer in the same flow. It will call the IssuanceManager to create the necessary CyberCertPrinter(s) for the deal (for example, a SAFE certificate contract, possibly with a particular extension if it’s a hybrid deal) GitHub, and then call the DealManager to proposeAndSignDeal with the founder’s provided terms and signature GitHub. A companion deployCyberCorpAndCreateRound function could likewise form the corp, deploy the certificate printers, and call createRound with the founder’s terms and signature. If such a helper is not yet available, adding one would provide parity with the deal flow. Essentially, using these one-click methods, a founder can both form their onchain company and launch their first fundraising transaction. The UI experience would be: fill in your company info and terms, click Launch, and after confirmation, get a link to share with investors.

Using the Contracts or Scripts: More technical users (or those integrating MetaLeX cyberCORPs into a larger system) can interact directly with the MetaLex-Tech/cybercorps-contracts repository and its deployment scripts. The repository provides Foundry scripts (e.g. deploy.s.sol) and contract APIs that mirror the UI functionality. For instance, a developer could call CyberCorpFactory.deployCyberCorp(...) with their parameters to get a new corp, or use deployCyberCorpAndCreateOffer(...) for a combined operation GitHub. The docs recommend referring to these deployment scripts and templates in the repo GitHub – they contain sample values and illustrate how to format inputs like the officer struct (which includes the officer’s address and initial role) or deal term arrays. By studying or reusing these scripts, one can programmatically launch cyberCORPs as part of a larger deployment pipeline (for example, spinning up multiple test corporations, or integrating cyberCORP formation into a product’s backend).

Once a cyberCORP is launched, the next steps typically involve issuing any initial equity and configuring the organization’s settings. The IssuanceManager that powers the Round Manager can mint founder stock certificates or automatically record SAFE conversions, keeping the cap table in sync. If the corp was created via a fundraising flow, an initial certificate (for the SAFE or equity being issued to the investor) is likely already minted. However, if a corp is created standalone (with no immediate deal), the founder might want to issue founder’s stock onchain to represent their own shares. This can be done by calling the IssuanceManager’s createCertPrinter to set up, say, a Common Stock certificate contract, and then using the IssuanceManager to mint shares to the founder’s address. Similarly, if the company has multiple co-founders or previous investors, one can mint tokens to each of them so that the full cap table is reflected onchain from day one. After launching, founders are encouraged to configure transfer‑restriction hooks such as Whitelist or Toggle to enforce compliance on share transfers. The founder (or whatever governance process they have) should also ensure the [MetaVesT](/cyberdeals/metavest) and [LeXscroW](/cyberdeals/lexscrow) integrations are configured if needed. MetaVesT is MetaLeX’s token vesting/lockup protocol, which is BORG-compatible and can be used for automating token or equity vesting schedules forum.zknation.io mobile.x.com. A cyberCORP can integrate MetaVesT to handle things like employee token vesting or lockups for early investors. For example, if the company wants to issue tokens to an advisor with a 1-year lockup, the MetaVesT contract can be deployed and linked, so that those tokens release gradually without manual oversight mobile.x.com. Meanwhile, LeXscroW (or specifically LexScroWLite as discussed) is likely already embedded for deals, but a corp could also use escrow conditions for other purposes – say, holding funds in escrow until a milestone is reached even outside of the initial SAFE context. Ensuring the companyPayable address is a secure multi-sig controlled by the appropriate people is another post-launch step (this way, when funds flow in from deals or other revenue, multiple officers can manage them securely). In essence, launching a cyberCORP bootstraps a company into the MetaLeX “legal OS”. From that point forward, the company can use various MetaLeX modules: it can execute financing rounds (SAFEs, equity, convertible notes) onchain via deals; it can manage its cap table and equity token transfers via the issuance system; and it can plug in things like MetaVesT for automated vesting or other future modules for compliance. All of this with the assurance that every action is transparent and governed by code where appropriate. The MetaLeX docs and repository will be the go-to reference for developers – for example, to find template IDs for standard agreements or to see how to format a legend (restriction notice) on a stock token. MetaLeX encourages developers to read through the cybercorps-contracts code for deeper understanding, and even to run the tests to see sample workflows of creating a corp and going through a deal (the test suite likely demonstrates a mock SAFE round from start to finish).

---


# Onchain Capital Structure

Source: https://metalex-docs.vercel.app/cybercorps/onchain-capital-structure

A **cyberCORP’s capital structure** – its stock ledger and equity issuance – is managed entirely onchain through a set of smart contracts. This means that a cyberCORP’s shares (and other securities like SAFEs or convertible notes) can exist either as **cyberCerts**, NFT-based certificates representing whole securities, or as **cyberScrip**, ERC-20 fungible tokens derived from those certificates. CyberCerts carry the full bundle of shareholder rights, while cyberScrip breaks those rights into liquid units better suited for trading, vesting, or DeFi use. Holders can convert between the two forms through the IssuanceManager, allowing certificates to be “scripified” for flexibility and later recombined into new cyberCerts. Every issuance, transfer, or conversion is executed by code, bringing unprecedented **transparency, automation, and security** to managing a company’s equity. The core of this system is implemented in MetaLeX’s smart contracts (available in the cyberCORPs contracts repository) and accessible via the user-friendly cyberCORPs web app. Below, we break down how this onchain cap table works and the benefits it provides to founders and investors.

## Explore More

* [Core Components: *IssuanceManager* and *CyberCertPrinter*](/core-components)
* [Tokenized Stock Certificates & Legal Alignment](/tokenized-stock-certificates)
* [Transfer Restrictions & Compliance Controls](/transfer-restrictions)
* [Corporate Actions via Smart Contracts](/corporate-actions)
* [Benefits of an Onchain Cap Table](/benefits)

---


# Benefits

Source: https://metalex-docs.vercel.app/cybercorps/onchain-capital-structure/benefits

Moving a company’s equity and securities onto the blockchain isn’t just a gimmick – it provides tangible advantages over traditional cap table management and stock issuance. Some key benefits of MetaLeX’s cyberCORP onchain capital structure include:

* **Real-Time Transparency:** The cap table is always up-to-date and transparently visible onchain. Founders, investors, and regulators can verify ownership stakes at any time, in real-time, without waiting for quarterly updates or pulling records from lawyers. This real-time view builds trust and aids due diligence (for example, an investor can see their NFT shares in their wallet immediately upon issuance).
* **Instant Settlement & Reduced Friction:** Equity transactions (issuances or transfers) settle nearly instantly with finality. There’s no weeks-long waiting period for paperwork, signatures, and manual entry. A fundraising event that might have taken days of coordination can be executed with a single click (or link share) via the smart contracts. This **reduces operational friction** dramatically – closing an investment round becomes as easy as a blockchain transfer.
* **Automated Compliance:** Built-in rules and automated checks mean that compliance is continuous and trust-minimized. The system won’t allow unauthorized share transfers or over-issuance of stock because the smart contracts enforce the rules. This reduces the risk of human error (no issuing the wrong number of shares, no forgetting to enforce a lock-up) and ensures corporate governance policies are followed by default.
* **Reduced Administrative Overhead:** By leveraging smart contracts, companies can eliminate or simplify many tedious cap table management tasks. No more manually updating spreadsheets, sending certificates, or coordinating between law firms and transfer agents for simple actions. Routine tasks like recording a SAFE conversion or updating a stockholder’s address are handled by contract calls, saving legal hours and administrative costs.
* **Programmable Equity & Investor Rights:** Because shares are represented as code, you can program them to do more. For instance, a cyberCORP could automatically calculate and distribute dividends or other distributions to all shareholders by reading token holdings (no need for a separate payout process). Voting rights can be tallied onchain with tokens, enabling hybrid onchain/offchain governance meetings. Smart extensions (like MetaLeX’s **MetaVesT** for vesting or **LeXcheX** for accredited investor verification) can plug into the cap table to provide advanced features like automated vesting schedules or compliance oracles. This **“code-as-law”** approach means the company’s bylaws or shareholder agreements can be at least partly enforced by smart contracts, reducing ambiguity and the need for after-the-fact enforcement.
* **Global Accessibility for Fundraising:** Using onchain equity makes it easier to involve participants from around the world in a company’s financing. Instead of dealing with international wire transfers and wet signatures, a founder can share a link to a **cyberCORPs fundraising deal** and investors can participate using their web3 wallet, receiving equity tokens in return. This opens up more possibilities for pooling capital (e.g. onchain SAFE investments from a group of angel DAO members) and potentially for future secondary liquidity (trading tokens peer-to-peer, if allowed). While still complying with securities laws, the *technical* barriers to entry are lowered – all you need is an internet connection and a wallet to become a shareholder, which is particularly powerful for global talent and investor communities.
* **Security and Immutability:** Records on Ethereum (or other chains MetaLeX might deploy on) are tamper-evident and secure. It’s extremely difficult for any malicious actor to alter the cap table or forge a stock certificate once issued, compared to the risk of someone manipulating paper records or centralized databases. Every change is recorded in an immutable ledger, creating a robust audit trail. This can improve accountability and prevent common problems like duplicate or inconsistent cap table records.

In summary, a cyberCORP’s onchain capital structure **modernizes the way companies handle equity**. It blends the **legal rigor of traditional corporate finance** (every share is accounted for and compliant) with the **efficiency of blockchain technology** (automation, speed, and transparency). Founders can focus more on building their business and less on cap table spreadsheets, knowing that their company’s ownership is consistently and correctly tracked by code. Investors benefit from immediate clarity on what they own and potentially new ways to interact with their equity (like using tokens in smart contracts for lending or collateral, subject to legal restrictions). MetaLeX’s cyberCORPs turn the cap table into a living, breathing part of the software stack of a company, paving the way for more **dynamic fundraising, governance, and growth** in the onchain era.

**Next Steps:** To delve deeper, you can explore the actual smart contract code in the MetaLeX cybercorps-contracts GitHub repository, which provides implementation details and examples. If you’re a founder or investor interested in using these tools, visit the cyberCORPs platform to see how onchain fundraising and cap table management works in practice, and check out related documentation on **[cyberRaise](/cyberdeals/cyberraise)**, **[Governance and Officers](/cybercorps/governance-and-officers)**, and other cyberCORP features. The onchain future of corporate capital management is here – and MetaLeX’s cyberCORP framework is your guide to leveraging it.

---


# Core Components

Source: https://metalex-docs.vercel.app/cybercorps/onchain-capital-structure/core-components

**IssuanceManager Contract:** When a new cyberCORP is launched, it deploys a dedicated **IssuanceManager** smart contract for that company. Think of the IssuanceManager as an onchain **registrar** or **cap table manager** – it maintains the authoritative record of all the company’s outstanding shares and securities. The IssuanceManager can create and track multiple classes/series of stock or other instruments. It acts as the central controller for equity operations: deploying new token contracts for each security class, minting new shares to investors, recording conversions (e.g. SAFEs converting to equity), and updating the cap table state. In essence, the IssuanceManager is the brain of the onchain cap table, coordinating all equity-related activities for the cyberCORP.

**CyberCertPrinter Contracts:** For each **class or series of equity** that the company has (for example, *Class A Common Stock*, *Series Seed Preferred Stock*, *Series A Preferred*, etc.), the IssuanceManager deploys a separate **CyberCertPrinter** contract. A CyberCertPrinter is essentially a **digital stock certificate printer**. It’s an ERC-721 NFT contract specialized for a particular type of security (e.g. “Common Stock” or “Preferred Stock”) and, if applicable, a series designation (e.g. “Series A”). When the cyberCORP needs to issue shares of that class, the IssuanceManager calls functions on the corresponding CyberCertPrinter to **mint new NFT-based stock certificates** to the appropriate owner. Each token minted by a CyberCertPrinter represents a **unique stock certificate (share)** in that class/series, complete with metadata and legal details. The cyberCORP may have just one CyberCertPrinter (if it only has one class of stock) or many (one for each class and series of shares or convertible instruments it issues).

*Example:* Upon cyberCORP initialization, the founder might use the IssuanceManager to create a *Common Stock* certificate contract and a *Series A Preferred* contract. These would be two CyberCertPrinter instances, one for each class. Later, if the company authorizes a new series of Preferred Stock (say Series B), the IssuanceManager can deploy another CyberCertPrinter for *Series B Preferred*. This modular design keeps different equities separated but under the common control of the IssuanceManager.

**Under the Hood:** CyberCertPrinter contracts are standard ERC-721 tokens with added logic for corporate compliance. Each CyberCertPrinter is deployed via a minimal proxy pattern (allowing upgradeability behind the scenes), and it’s initialized with parameters like the security’s name, ticker symbol, security class (from a predefined enum such as CommonStock or PreferredStock), and series (Series A, B, Seed, etc.). This configuration ensures that each token contract knows what type of equity it represents. The IssuanceManager keeps a registry of all its CyberCertPrinters, enabling the cyberCORP to query or iterate over all share classes in its cap table.

**CyberScrip Tokens and Conversion:** For any certificate contract, the IssuanceManager can also deploy a corresponding `CyberScrip` ERC-20. These fungible tokens mirror the units of a certificate and provide a more liquid representation of the security. Calling `scripifyCert` voids a certificate and mints an equivalent amount of cyberScrip to the holder. When enough scrip is assembled, `convertScripToCert` burns it and restores a matching voided certificate or mints a fresh one. Each direction of conversion can be gated by customizable conditions, allowing issuers to enforce processes like KYC checks or minimum denominations.

---


# Corporate Actions

Source: https://metalex-docs.vercel.app/cybercorps/onchain-capital-structure/corporate-actions

Because equity and investor agreements live onchain, many **corporate actions** can be automated or executed with a single transaction. The IssuanceManager and CyberCertPrinters work in tandem to handle typical events in a company’s life cycle:

* **Issuing New Shares:** When the company needs to issue more stock (for example, issuing founder shares, or closing a new investment round), the IssuanceManager mints new tokens via the relevant CyberCertPrinter. This could be a new Common Stock certificate to a founder, or a batch of Preferred Stock certificates to investors in a financing round. The details of the issuance (who the investor is, how much they paid, valuation, etc.) are captured in the token’s metadata or in event logs. There’s no need to manually update a spreadsheet or stock ledger book – the blockchain **transaction itself is the update**. When fundraising is performed through MetaLeX’s **Round Manager**, the IssuanceManager deploys any required CyberCertPrinter contracts at round creation and mints certificates to investors as allocations are confirmed. For example, EOI submissions in a Series Seed round lead to Series Seed Preferred Stock certificates being minted to multiple investors as the round closes.
* **Hybrid Security Issuance and Conversions:** When a company completes a round through the Round Manager, the IssuanceManager automatically mints certificates for SAFEs, SAFTs, SAFTEs, and equity shares. Conversions are triggered by a subsequent priced equity round for SAFEs and SAFTEs or by a token generation event for SAFTs. The IssuanceManager calculates the correct share or token allocation and mints new certificates accordingly, keeping the onchain cap table current without manual intervention.
* **Stock Splits and Mergers:** If the company ever needs to **split** its stock (e.g., a 2-for-1 split of common shares) or perform other cap table reorganizations, the onchain approach simplifies this. Rather than issuing new certificates and canceling old ones manually, a smart contract function can automate the process – minting additional tokens to each holder in a split, or adjusting token metadata to reflect changes. Similarly, if two classes are merged or a class is reclassified, the contracts could support retiring one CyberCertPrinter’s tokens and reissuing under another, all with a verified record of what happened.
* **Cancellations and Buybacks:** In cases of certificate cancellations (like voiding a lost certificate, or share buybacks/redemptions by the company), an admin can call the IssuanceManager to **void** a specific token ID. The system might either burn the NFT or mark it as canceled in metadata. This is analogous to tearing up a paper certificate, but with an immutable onchain record that certificate #X was voided at a certain block/time by the company. If the company repurchases shares from a shareholder, it can similarly have the shareholder transfer the token back and then burn or hold it as treasury stock (depending on the desired outcome), all traceable onchain.

All of these actions emit events and leave a permanent record. At any point, the company or investors can query the blockchain to get a **real-time cap table**: which addresses hold which shares, and how many. There’s no need to reconcile multiple sources of truth – the chain *is* the source of truth. Moreover, these actions can be executed in a single atomic sequence if needed. For instance, MetaLeX’s CyberCorpFactory contract (used when creating a new cyberCORP) can deploy a new company **and immediately perform a fundraising issuance** in one go. The factory can deploy the corp’s contracts, then call IssuanceManager to create a stock class and issue a SAFE or shares to an investor, then even set up a deal escrow – all in one blockchain transaction (the web app orchestrates this when a founder clicks “Launch and Fund”). This demonstrates the power of onchain integration: **complex multi-step legal processes can be automated**, reducing turnaround time from weeks to seconds.

solidity

```
Copy

// Example: Creating a new share class (Series A Preferred Stock) and issuing shares to an investor
 
address seriesAContract = issuanceManager.createCertPrinter(
    ["Restricted: Unregistered Security"],   // default legend for this stock class
    "Series A Preferred Stock",              // name of the security
    "SERIESA",                               // ticker symbol
    "ipfs://Qm...certificateMetadata.json",  // URI to offchain certificate details
    SecurityClass.PreferredStock,            // type of security (from enum)
    SecuritySeries.SeriesA,                  // series designation (from enum)
    address(0)                               // no special extension logic
);
 
uint256 newCertId = issuanceManager.createCertAndAssign(
    seriesAContract, 
    investorAddress, 
    certificateDetailsStruct                // details like investment amount, shares, etc.
);
// The above call mints a new NFT stock certificate (ID = newCertId) to the investorAddress.
```

*In the code snippet:* The `createCertPrinter` call deploys a new NFT contract for **Series A Preferred Stock** with a transfer restriction legend. The `createCertAndAssign` then mints a new share certificate token from that contract and assigns it to an investor in one step. These functions are part of the cyberCORP’s IssuanceManager contract (see the cybercorps-contracts code for implementation details).

---


# Tokenized Stock Certificates

Source: https://metalex-docs.vercel.app/cybercorps/onchain-capital-structure/tokenized-stock-certificates

When a CyberCertPrinter mints a new token, that token is effectively a **stock certificate issued as an NFT**. Each certificate NFT can include important **metadata**, such as the shareholder’s name, the number of shares it represents, and even a link to a PDF of the signed certificate or relevant legal agreements. MetaLeX’s design explicitly aims to imbue these tokens with the **same legal status and function as traditional paper stock certificates**. In fact, this approach aligns with recent Delaware state law amendments, which *authorize corporations to maintain their stock ledger on a blockchain*. By mapping each share (or each certificate representing a bundle of shares) to a unique token ID, a cyberCORP’s onchain ledger is a legally recognized source of truth for ownership.

**Share Classes and Series in Code:** The smart contracts enforce distinctions between different share classes and series. For example, a token from the *Preferred Stock, Series A* contract is programmatically recognized as “Series A Preferred” and can carry whatever rights or restrictions are unique to that series. This ties into MetaLeX’s broader legal-tech research (see **Tokenizing Corporate Capital Stock** in MetaLeX publications) which ensures that onchain representations correspond to real-world definitions (e.g. what “Series A Preferred” means in a charter or term sheet). Because each share class has its own contract address and metadata, the system can, if needed, treat them differently for voting, dividends, liquidation preferences, etc., just as a traditional corporation would differentiate share classes in its charter.

**Instant, Immutable Ledger:** Whenever shares are issued, transferred, or retired, those changes are recorded by the contracts **immutably onchain**. Instead of updating a spreadsheet or calling a transfer agent, the company uses its IssuanceManager (via a transaction) to record the change. The blockchain becomes the company’s **cap table ledger** – tamper-proof and time-stamped. Ownership of the company’s stock is represented by wallet addresses holding the NFTs, and transfers of ownership occur by transferring these tokens (subject to the restrictions below). Settlement is near-instant, secured by the blockchain’s consensus, meaning no waiting for paperwork to process. At any moment, the IssuanceManager can provide a canonical list of all outstanding shares and their holders by querying the tokens in each CyberCertPrinter it manages.

**cyberScrip: Fungible Claims:** For greater liquidity, a certificate can be broken into ERC-20 units known as cyberScrip. These tokens represent the same number of underlying units as the original cyberCert but are easier to trade, vest, or use as collateral. Scrip holders typically do not exercise shareholder rights until they recombine their tokens into a certificate.

**Converting Between Forms:** The IssuanceManager supports two-way conversion between certificates and scrip. Calling `scripifyCert` transfers a certificate to the contract, voids it, and mints an equivalent amount of cyberScrip to the holder. Later, `convertScripToCert` burns scrip and either revives a matching voided certificate or creates a new one. Issuers can attach custom conditions—such as KYC checks or minimum conversion sizes—to either direction of this process, giving them granular control over how investors move between cyberCerts and cyberScrip.

---


# Transfer Restrictions

Source: https://metalex-docs.vercel.app/cybercorps/onchain-capital-structure/transfer-restrictions

One of the key benefits of an onchain equity system is that compliance rules can be **built into the contracts themselves**. In traditional corporate law, transferring stock often requires certain conditions to be met: for example, board approval, a right of first refusal process, or legends on certificates indicating restrictions (such as *“This security is not registered under the Securities Act and may not be transferred without appropriate authorization”*). CyberCORP smart contracts mirror these requirements in code:

* **Restricted Transfers:** By default, a cyberCORP’s share tokens are **not freely transferable** without the company’s approval. If a shareholder wants to transfer a stock NFT to a new owner, the CyberCertPrinter contract can be configured to **require an endorsement** (permission) before the transfer is finalized onchain. This works analogous to having an officer sign the back of a paper certificate to approve the transfer. The endorsement itself can be represented by an onchain signature or a specific function call by an authorized party. Until an endorsement is recorded, the token cannot be transferred to a new address, preserving the integrity of the cap table and ensuring compliance with any shareholder agreements or securities laws.
* **Legends and Whitelists:** Each CyberCertPrinter can enforce **legends** – essentially notes or flags on the token that indicate transfer restrictions or required qualifications. For instance, a legend might indicate that the holder must be an accredited investor, or that the token cannot be transferred until a certain date. The contracts support global or per-token restrictions and can include whitelist mechanisms (addresses approved for transfer) or require certain conditions to be met (via hook contracts) before a transfer. These legends appear in the token’s metadata and are taken into account whenever a transfer is attempted. If a transfer violates a legend (say, trying to send a Restricted stock token to an unapproved buyer), the contract will **reject the transfer** automatically with an error explaining the restriction.
* **WhitelistTransferHook:** MetaLeX’s contract library includes a hook that checks both the sender and recipient against a board-managed whitelist. If either address is not approved, the transfer reverts. This makes it easy to enforce investor qualification or KYC requirements entirely onchain.
* **ToggleTransferHook:** Another module lets the company flip transferability on or off globally or for specific certificate IDs. When transferability is disabled, the token is non-transferable until the flag is re-enabled, supporting temporary lockups or per-investor restrictions.
* **Onchain Approvals:** Company officers or admins (as defined in the cyberCORP’s governance settings) have special privileges in the IssuanceManager and CyberCertPrinter contracts to manage these restrictions. They can endorse transfers, update legends, or globally toggle whether a particular class of shares is transferable. All such actions are logged via events, creating a clear audit trail. This onchain oversight replaces the need for offchain coordination for tasks like updating a cap table or issuing new certificates – the smart contracts ensure that only authorized actions occur, and nothing “slips through the cracks” without proper sign-off.

These hooks are attached to certificate contracts via the IssuanceManager, and company officers can toggle them as needed, providing an onchain analogue to paper legends and transfer restrictions.

In practice, these compliance features mean a cyberCORP can **satisfy legal requirements by design**. The cap table isn’t just onchain for transparency; it’s also enforcing the rules that real-world lawyers care about. For example, if a share class requires board consent to transfer, the smart contract requires an onchain signature from a board-designated account. If securities laws demand a legend on certain shares, the NFT metadata includes that legend and the contract blocks disallowed trades. This gives regulators, auditors, and the company’s lawyers confidence that the onchain records are not only accurate but also being managed in accordance with the law.

---


# Sources

Source: https://metalex-docs.vercel.app/cybercorps/sources

1. **MetaleX’s cyberSAFE: Fund Your Company in a Few Clicks, Onchain**
   Gabriel Shapiro, *MetaLeX Newsletter*, April 25 2025.  
   <https://metalex.substack.com/p/metalexs-cybersafe-fund-your-company>
2. **Tokenizing Corporate Capital Stock**
   Gabriel Shapiro, *MetaLeX Newsletter*, December 16 2024.  
   <https://open.substack.com/pub/metalex/p/tokenizing-corporate-capital-stock>
3. **MetaLeX cyberCORPs Web App**
   *cyberCORPs* application, MetaLeX.  
   <https://cybercorps.metalex.tech/>
4. **MetaLex-Tech/cybercorps-contracts**
   GitHub repository for cyberCORPs smart contracts.  
   <https://github.com/MetaLex-Tech/cybercorps-contracts>

---


# What is a cyberCORP?

Source: https://metalex-docs.vercel.app/cybercorps/what-is-a-cyberCORP

## What are cyberCORPs (bizBORGs)?

**cyberCORPs** (sometimes called **bizBORGs**) are onchain corporations – legal companies whose key operations (financing, cap table, governance, etc.) run on blockchain-based smart contracts. They merge traditional legal structures (e.g. an LLC or C-corp) with programmable code. This creates a **governance-accountable, trust-minimized organization** that can operate and fund itself directly on the blockchain. In other words, a cyberCORP uses code to enforce corporate actions and policies, while retaining the familiar roles of real-world businesses (shareholders, directors, etc.). Unlike DAOs with open token governance, or DAO-adjacent BORGs that operate like nonprofit SPVs, cyberCORPs are traditional for-profit business entities at their core, just augmented with blockchain automation for efficiency and transparency. Real-world control and ownership are preserved, but execution is handled digitally onchain.

## Why Put Corporate Equity and Agreements Onchain?

Tokenizing a company’s shares and contracts unlocks several powerful benefits:

* **Streamlined Fundraising & Lower Costs:** Raising capital becomes faster and far cheaper. For example, a seed round using Simple Agreements for Future Equity (SAFEs), Token Warrants, Simple Agreements for Future Tokens (SAFTs), or similar agreements, might ordinarily incur upwards of $25k in legal fees, but with MetaLeX can be automated onchain for a fraction of the cost. By replacing lengthy email chains, bespoke negotiations, and DocuSigns with a slick web interface, standardized deal templates, clear term-setting parameters, and autonomous deal execution code, the process is simplified and legal overhead is slashed.
* **Trust-Minimized Execution:** Onchain deals remove the need to trust intermediaries or manual processes. Smart contracts act as impartial escrow agents and executors – no more chasing signatures or funds, since the code handles enforcement. There’s **no need for middlemen** to coordinate closing; once conditions are met the contract automatically closes the deal.
* **Programmability & Composability:** Equity and contractual rights become **digital assets** when represented by tokens. This makes them programmable and even composable like DeFi assets. For instance, an onchain SAFE (cyberSAFE) token *embodies* the legal right to future stock in the company, blurring the line between a PDF agreement and a token in your wallet. These tokens could potentially interact with other onchain tools – e.g. integrated into automated vesting contracts or used as collateral in compliant lending markets – something impossible with traditional paperwork. We like to think of this as "CorpFi".
* **Real-Time Transparency:** Every transaction (signing, funding, token issuance, etc.) is recorded on the blockchain, providing an **audit trail** that all parties can monitor in real time. Founders and investors get a live dashboard of the deal’s status (e.g. whether an investment is funded, or a SAFE has converted). This transparency builds trust and helps catch issues (like missed signatures or deadlines) immediately.
* **Enhanced Marketability of Equity:** Tokenized shares or SAFE rights can be made more liquid. Within legal constraints, these security tokens could potentially trade peer-to-peer or be transferred with far less friction than paper shares. While still complying with securities laws (e.g. only trading among authorized investors), this *digitally native equity* is easier to manage and transfer, unlocking new avenues for secondary markets or collateralizing equity.
* **Legal Enforceability Retained:** Critically, putting deals onchain doesn’t mean forsaking the law – each tokenized agreement is still a real legal contract. cyberCORP transactions bring the efficiency and transparency of DeFi to corporate finance **while preserving the legal enforceability of traditional contracts**. Parties have the same legal rights and remedies as with offchain agreements, but benefit from automated execution. In short, you get the best of both worlds: the speed and certainty of code, plus the protection of law.

## Onchain Financing & Dealmaking (CorpFi in Action)

One of the core value propositions of cyberCORPs is **onchain fundraising** – essentially, bringing startup financing into the realm of smart contracts. This is sometimes dubbed **“CorpFi”** (corporate finance via DeFi technology) – and if you enjoy DeFi’s efficiency, **you’ll love CorpFi** for handling compliant financings with minimal friction. MetaLeX’s first cyberCORP module, called **cyberSAFE**, exemplifies this by transforming a standard SAFE raise into a few-click onchain workflow. The result is that **fundraising becomes as easy as using a web app**, with the system automating the heavy lifting. From YC-style SAFEs to more complex hybrid deals, cyberCORPs make fundraising **onchain, programmable, and just a link away**.

**How a cyberSAFE raise works:** (example of an onchain SAFE deal)

1. **Setup:** A founder starts a deal on the cyberCORPs web portal by inputting the key terms – e.g. company name, valuation cap, investment amount, and any special terms. The terms are recorded in a smart contract and used to generate a legally compliant SAFE agreement (the text of the contract is auto-generated for review).
2. **Sign & Tokenize:** The founder signs the SAFE agreement onchain via their wallet. This action “mints” the deal as an onchain asset – effectively turning the contract into a token that represents the investor’s right to future equity. The smart contract also sets up an escrow to hold funds once the investor participates.
3. **Share with Investors:** The platform provides a unique link to the onchain deal. The founder sends this link to prospective investors instead of a PDF. An investor opens the link, connects their Web3 wallet, and can independently review the terms in the embedded agreement.
4. **Investor Participation:** If the investor is satisfied, they sign the SAFE onchain as well and transfer funds (e.g. USDC or ETH) into the deal’s smart contract. **No emails or wire transfers needed** – their wallet signature and payment are all handled in one interface. (MetaLeX’s LeXcheX compliance module can optionally verify the investor’s accreditation onchain to ensure the raise complies with Reg D or other regulations before they’re allowed to fund.)
5. **Automated Closing:** Once the investor has signed and paid, the deal is automatically marked as **accepted**. The smart contract immediately releases the funds to the company’s treasury (or holds them until a specified condition) and issues the SAFE token (or other security token) to the investor, representing their stake. All parties can track this progress on a dashboard in real time. If an investor fails to fund before a deadline, the deal can expire and the tokenized SAFE won’t be issued – all enforced by code without need for manual intervention.
6. **Post-Deal Management:** The cyberCORP platform continues to assist after the closing. The SAFE token can later be converted into equity tokens seamlessly when a triggering event occurs (for example, if the company raises a priced equity round in the future). In fact, deals are tracked through their lifecycle – one can see which rounds are open, which have closed, and which have converted to stock onchain. This end-to-end lifecycle management means less paperwork down the road when updating cap tables or executing future financings.

Through this onchain deal process, raising capital becomes **fast, transparent, and secure**. Founders can focus on building their business instead of coordinating documents and payments, and investors get confidence that their rights are recorded immutably onchain. All of this is achieved with a familiar legal framework (the SAFE) that’s simply been given a tech upgrade – *“a tech-enhanced SAFE that embeds traditional SAFE deal logic into an automated deal process and tokenized security issuance,”* as MetaLeX describes it.

## Onchain Cap Table Management with Tokenized Equity

Moving a company’s equity and obligations onchain not only streamlines the initial fundraising, but also revolutionizes **cap table management**. In a cyberCORP, shares (or future shares promised under instruments like SAFEs) can exist as **tokens** in authorized wallets rather than as entries on a spreadsheet or PDFs in a drawer. This has several implications:

* **Single Source of Truth:** The blockchain effectively *is* the cap table. Ownership of equity is represented by who holds the security tokens. This means no more inconsistent spreadsheets – everyone (founders, investors, regulators) can refer to the onchain record to see the current distribution of shares or SAFE rights.
* **Instant Updates:** When new shares are issued or transferred, the cap table updates in real time as token balances change. Corporate actions like stock splits or option exercises can be executed by minting/burning tokens according to onchain logic, instantly reflecting the new ownership stakes.
* **Easier Transfers (Within Constraints):** Because equity is tokenized, transferring it (subject to legal restrictions) can be as easy as a wallet transaction. For example, if a shareholder in a private company wants to sell some shares to another accredited investor, an onchain transfer can simplify what traditionally involves significant paperwork. The cyberCORP’s smart contracts can enforce any transfer rules – e.g. preventing transfers to unapproved parties or keeping within a certain shareholder limit – so compliance is maintained even as the tokens move. Within those constraints, **shares as tokens can potentially trade peer-to-peer**, improving liquidity for investors.
* **Integration with Financial Tools:** Tokenized equity can plug into other onchain financial primitives. A company could, for instance, use a token-locking module (like MetaLeX’s MetaVesT) to automate vesting schedules for team members, or allow investors to use their equity tokens as collateral in specialized lending platforms. Cap table changes (like new financing rounds) could automatically trigger smart-contract-based notifications or actions (e.g. SAFE tokens converting to stock tokens upon a qualified financing, as noted above).
* **Cap Table Integrity and Auditability:** With every equity transaction onchain, the history of who owned what and when is immutably recorded. This makes due diligence and audits much simpler – one can cryptographically verify the cap table at any point in time. It also reduces the risk of cap table errors or fraudulent share issuances, since all issuances must conform to the code rules and are publicly verifiable on Ethereum.

In summary, onchain cap table management turns what used to be a tedious administrative task into an automated, transparent system. Founders and CFOs get peace of mind that the cap table is always accurate and up-to-date, and investors get clearer insight into their holdings (often viewable in their own wallets or dashboards). The **marketability** of the equity is improved as well – while staying compliant, the tokens give shareholders more flexibility than traditional stock certificates.

## Onchain Corporate Governance & Compliance

Beyond financing, cyberCORPs improve how companies are governed and kept in compliance by encoding certain governance processes in smart contracts. Rather than relying purely on trust and after-the-fact enforcement, a cyberCORP can **enforce corporate policies in real time**. Key aspects of onchain governance in a cyberCORP include:

* **Multi-Sig Executive Control:** At the heart of a cyberCORP is a multi-signature vault (e.g. a Gnosis Safe) that holds the company’s onchain assets and executes transactions. The signers of this multi-sig are the people entrusted with the company’s decisions – for example, the CEO, CFO, and board members (or whatever governance structure the entity chooses). Because the wallet requires a quorum of these signers to authorize actions, it ensures no single actor can run off with funds or make unilateral decisions. This maps closely to traditional governance (board approval for major actions, etc.), but with cryptographic signatures replacing ink signatures.
* **Onchain Policy Guards:** cyberCORPs leverage the MetaLeX **BORGs OS** modules to embed rules (guards) that automatically check transactions against governance policies. For instance, a rule might require that any treasury transfer above $100k obtains at least 3 of 5 director signatures, or that certain “guarded” actions (like issuing new equity tokens) can only execute after an onchain waiting period (giving time for review or even a token-holder veto if a hybrid DAO model is used). These guards and conditions are coded once and then consistently enforce the agreed governance procedures on every transaction – eliminating the risk of someone bypassing an internal control. Essentially, **real-world corporate controls (board approvals, spending limits, etc.) are separated from but enforced by digital execution**.
* **Automated Compliance Checks:** Compliance requirements that would normally be handled manually by lawyers or compliance officers can be partially automated. We already saw an example with investor accreditation (LeXcheX tokens can represent verified accreditation status and *“slot into any onchain workflow that needs to restrict or log”* such compliance data). Similarly, a cyberCORP could implement whitelist/blacklist modules to comply with sanctions or to ensure tokens only reach permitted jurisdictions. If the company’s bylaws or legal structure impose limits (e.g. no more than 100 shareholders for an LLC, or no transfers until a lockup expires), those rules can be encoded in the smart contracts. This proactive enforcement means the company is **always operating within its legal bounds by default**, rather than relying on after-the-fact correction.
* **Transparent Decision Records:** When corporate decisions are made via onchain actions, it creates a tamper-proof record of governance. For example, if the board of a cyberCORP votes to approve a new token issuance, that approval can be done by each director signing an onchain transaction (or a offchain message recorded onchain). Stakeholders can later verify that, yes, the required approvals were obtained. This transparency holds leaders accountable – no more “shadow actions” that weren’t properly authorized. It’s essentially an automated minute book: every significant action is logged by the system itself.

Crucially, none of this means the human element is removed from governance – rather, the **blockchain acts as a support system for human governance**. cyberCORPs are **not decentralized autonomous organizations (DAOs)** where anyone with tokens can vote; instead, they are traditional organizations (with CEOs, boards, investors) that use blockchain tools to execute decisions in a consistent, rule-abiding way. The result is a company that’s far less reliant on trust in any one individual’s discretion. It’s easier to trust the system because checks and balances are literally built into the code. As MetaLeX puts it, this approach yields *“governance-accountable, trust-minimized and legally optimized”* corporate structures – meaning the company’s management is both **accountable** (every action requires the proper approvals) and **efficient** (much of the process is automated), all while staying within the bounds of law and legal agreements.

## Conclusion: The CorpFi Revolution

cyberCORPs represent a new frontier in how businesses can be created and operated, bringing the ethos of decentralized finance to the world of corporate finance. This movement – sometimes playfully called **“CorpFi”** – is about using blockchain networks to upgrade the *plumbing* of traditional corporations. By putting equity, agreements, and governance processes on Ethereum, MetaLeX is aiming to **“network-ify” organizations and agreements**. In practical terms, that means turning the cumbersome, trust-heavy parts of running a company into streamlined, transparent, and code-assisted workflows.

The value of cyberCORPs lies in **bridging two worlds**: the reliability and legitimacy of traditional companies on one side, and the innovation and efficiency of crypto networks on the other. Founders can fund their companies faster and more cheaply, investors get enforceable rights delivered in token form, and everyone gains from the real-time transparency and security of blockchain operations. Yet all of this happens without discarding the legal protections and structures that make businesses work – rather, those structures are given superpowers by being implemented in smart contracts.

In summary, a cyberCORP empowers a business to **raise capital, manage ownership, and conduct its affairs onchain** in a way that is compliant and convenient. It’s about re-imagining corporate finance (**CorpFi**) for the internet age: cap tables that update themselves, deals that close with a click, and corporate decisions that execute autonomously but within agreed rules. By leveraging MetaLeX’s cyberCORP framework, entrepreneurs can turn their companies into **“cybernetic organizations”** that are faster, leaner, and more transparent than ever before. It’s a bold step toward a future where **every startup or fund could be part of a blockchain-connected network**, raising and transacting in a trust-minimized way – fulfilling the vision of making organizations as programmable as the rest of the digital world.
.

---


# cyberRaise

Source: https://metalex-docs.vercel.app/cyberdeals/cyberraise

**cyberRaise** is MetaLeX Labs’ compliant, early‑stage fundraising dApp designed to transform how startups and investors engage in venture financing. Built atop the cyberCORPS operating system and the cyberDeals smart contract stack, cyberRaise makes the fundraising process fully transparent, programmable, and secure by leveraging blockchain technology. It empowers founders and investors to complete investment rounds without reliance on intermediaries or cumbersome paperwork, streamlining compliance with legal and regulatory requirements. Advanced modules like **LeXcheX** for onchain investor accreditation and **LeXscroW** for automated escrow ensure that all deal conditions are met before capital moves, eliminating counterparty risk.

*The cyberRaise interface allows founders to choose from various deal types – classic SAFEs, SAFTs, SAFTEs, and hybrid SAFE + Token Warrant deals – under different regulatory exemptions (Reg D for U.S. offerings and Reg S for international offerings). Each option comes with standardized terms, enabling compliant fundraising in just a few clicks.* (In brief: **SAFE** for future equity, **SAFT** for future tokens, **SAFTE** combining equity and token rights, and **SAFE + Token Warrant** bundling an equity SAFE with a token option side letter, as explained below.)

For a deeper look at round lifecycle and permissions, see the [Round Manager](/cyberdeals/round-manager).

## Key Smart Contracts and Modules

A number of smart contracts and modules underlie cyberRaise’s onchain functionality, each handling a critical piece of the fundraising workflow:
\* **RoundManager:** Coordinates multi-investor fundraising rounds. Founders call `createRound` to set parameters (series type, raise cap, min/max ticket, round type, payment token, price per unit, valuation, terms and template ID). The RoundManager deploys CyberCertPrinter contracts via the IssuanceManager for each security to be issued, stores the round parameters, and emits a `RoundCreated` event. It supports **two round types** – first‑come‑first‑served (FCFS) and founder‑approved – and manages expressions of interest (EOI), allocation, closing, and conversion of certificates when a qualifying event occurs.

* **DealManager:** The onchain deal orchestrator that coordinates each raise from inception to completion. It manages deal proposal creation, tracks signatures from the parties, and triggers finalization in a secure, auditable manner – moving a deal through all stages (proposed → signed → paid → finalized) according to its rules. DealManager remains available for bespoke single-counterparty agreements, while RoundManager handles multi-investor rounds.
* **CyberAgreementRegistry:** A transparent registry of standardized and attorney-vetted legal agreement templates. Each template is identified by a unique `templateId` (e.g. SAFE, SAFT, SAFTE, etc.), and every executed deal instantiates a new agreement instance with its own `agreementId`. This ties each onchain deal to a specific legal document (retrievable via an IPFS URI or hash of the contract text) while maintaining an immutable record of all executed agreements. The registry also keeps track of which parties have signed and whether an agreement is fully signed, voided, or finalized. It includes a built-in **delegation** system (described later) that allows one address to sign on behalf of another under certain conditions.
* **IssuanceManager:** Handles the compliant issuance of tokenized securities. When `createRound` is called, the RoundManager uses the IssuanceManager to deploy **CyberCertPrinter** contracts (ERC-721 NFT contracts) for each security type, and during allocation it mints non-fungible tokens (NFTs) that serve as digital security certificates representing instruments such as SAFEs, SAFTs, token warrants, or SAFTEs. These NFTs carry the key terms of the deal in their metadata and evidence the investor’s rights. They are initially **non-transferable** to comply with securities law, and the IssuanceManager allows the company to later toggle transferability or void the NFT if needed.
* **LeXscroWLite:** A lightweight escrow smart contract that securely holds assets during the deal process. The RoundManager relies on it to escrow investor funds and the company’s securities for each EOI, releasing assets only when predefined conditions (signatures, accreditation checks, deadlines, custom conditions) are satisfied. This guarantees an atomic swap: the startup’s NFT securities move to the investor only if the investor’s payment is received, and vice versa. If a round allocation expires or is voided, LeXscroWLite can refund funds and return certificates to unwind the transaction safely.
* **LeXcheX:** Automates investor compliance by integrating onchain accreditation checks. LeXcheX is an NFT-based accreditation system: an investor completes a one-time KYC/verification process (offchain) and is issued a **soul-bound** NFT certificate attesting to their accredited status. The cyberRaise platform can then verify an investor’s eligibility in a single contract call. For instance, before accepting an investor’s EOI, the RoundManager invokes a `LexChexCondition` that checks the investor’s address against the LeXcheX contract to confirm they hold a valid accreditation NFT. This fulfills requirements like SEC Rule 506(c) (verification of accredited investor status for public fundraising in the U.S.) without traditional paperwork. The accreditation NFT cannot be transferred and can carry an expiration date or metadata about the verification method, providing a robust onchain record of compliance.
* **TokenWarrantExtension:** An extension module enabling hybrid deals that attach future token rights to equity raises. It supports structures like **SAFE + Token Warrant** deals, where an equity agreement (SAFE) is bundled with an option for the investor to receive tokens in the future. During `createRound`, the RoundManager deploys separate certificate printers for the SAFE and the warrant so that allocation mints the corresponding NFTs together. The TokenWarrantExtension handles additional parameters such as token warrant coverage, exercise price, and token release schedule. For example, it can enforce that if an investor wishes to exercise the warrant later to claim tokens, they must pay a predefined **exercise price** (which can be per token or a nominal amount) – whereas in a SAFTE (see below), the token rights come *without* an extra payment.
* **ICondition:** A flexible interface for plugging in bespoke compliance modules. Beyond standard checks (like accreditation and signatures), cyberRaise allows founders to attach custom smart contract conditions to each EOI. These could include additional KYC/AML verifications, time-based vesting or lock-up requirements, minimum or maximum raise thresholds, or essentially any boolean condition that can be codified in a smart contract. The RoundManager supports adding or removing such conditions, and during allocation it calls each condition’s `checkCondition` function to ensure it returns true. This modular approach means cyberRaise can accommodate project-specific covenants and evolving regulatory requirements without altering its core logic.

## Streamlined Onchain Fundraising Process

cyberRaise supports two transaction models. The **DealManager** powers bespoke single-counterparty deals, while the **RoundManager** coordinates multi-investor fundraising rounds.

## DealManager Flow (single-investor deals)

With cyberRaise, the entire fundraising transaction is handled onchain in a few seamless steps. Founders and investors interact through a user-friendly interface (or directly with the smart contracts), and once terms are agreed and all conditions are met, funds and tokens are exchanged atomically. The process can be summarized as follows:

1. **Proposing a Deal:** The founder initiates a bespoke raise via the intuitive cyberRaise dashboard, or by calling the `DealManager` contract directly. They select a standardized agreement template (e.g. choosing between a SAFE, SAFT, SAFTE, etc.) and input the deal parameters specific to that raise. These parameters include things like the valuation cap or discount, the token allocation or network valuation, whether a token warrant is attached, and any conversion terms or special conditions. Once the terms are set, the founder cryptographically signs the proposal using their Web3 wallet (via an EIP‑712 signature) and sends it onchain to the DealManager, which records a new pending deal with a unique deal ID. An investor counterparty may be specified or left open, and the deal includes an expiration time and optional custom condition contracts.
2. **Escrow Setup:** As soon as a deal is proposed, the platform automatically sets up the onchain escrow and initial security issuance for that deal. The DealManager works with `LeXscroWLite` to create an escrow entry tied to the agreement ID, and invokes the `IssuanceManager` to mint the NFT securities representing the investment instrument(s). For example, if the deal is a SAFE or a SAFTE, an NFT certificate for the convertible instrument is created. If a token warrant is part of the deal, a second NFT representing the warrant is also minted. These NFTs are deposited into escrow to “lock in” the company’s promise onchain, awaiting the investor’s response. The legal agreement text is accessible via the `CyberAgreementRegistry` so the investor can review the full contract before signing, and the founder can share a unique deal link or ID with the prospective investor to complete the transaction.
3. **Investor Countersigning & Funding:** The investor reviews the deal terms and, if they accept, calls `signDealAndPay` to countersign and transfer funds in one transaction. DealManager verifies the investor’s signature, checks that any attached conditions (like `LexChexCondition` for accreditation or other `ICondition` modules) return true, and ensures the deal has not expired. Only the designated investor can countersign if an address was specified; otherwise the first investor to sign becomes the counterparty. Upon success, the investor’s funds are escrowed and their signature is logged in the `CyberAgreementRegistry` alongside the founder’s, marking the agreement as fully signed.
4. **Finalizing the Deal:** When all conditions are satisfied, anyone can call the finalization function. DealManager releases funds to the company’s payable address, delivers the NFT certificates to the investor, and marks the agreement finalized. The escrow performs the atomic swap—capital for securities—ensuring neither party can default. If conditions aren’t met or the deadline expires, the escrow unwinds and refunds the investor, voiding the certificates and leaving an onchain record of the voided deal.

## RoundManager Flow (multi-investor rounds)

1. **Round creation:** The founder uses the cyberRaise dashboard to start a raise, selecting the round type, series, and ticket sizes. They set parameters (series type, raise cap, min/max ticket, round type, payment token, price per unit, valuation, terms and template ID) and call `createRound`. The RoundManager deploys one or more `CyberCertPrinter` contracts via the `IssuanceManager` for each security to be issued, stores the parameters in the `Round` struct, and emits a `RoundCreated` event.
2. **Expressions of Interest (EOI):** Investors join the round by calling `submitEOI` with their desired amount. The RoundManager checks the round’s status, uses `CyberAgreementRegistry` to create an agreement instance, sets up escrow via `LeXscroWLite`, and attaches any per‑EOI conditions (e.g. `LexChexCondition`) to enforce compliance.
3. **Allocation & funding:** For `FCFS` rounds, allocation happens automatically when an EOI is submitted. For `FounderApproved` rounds, the founder reviews EOIs and calls `allocate` on those they accept. During allocation the system signs the agreement, computes units, mints certificates through `IssuanceManager`, attaches endorsements, refunds any surplus funds, finalizes the escrow, and updates the amount raised. Allocation mints **non‑transferable NFT certificates** representing securities (e.g., SAFE tokens, SAFT tokens, or hybrid instruments), demonstrating how capital flows and securities issuance are automated in CorpFi.
4. **Closing & conversion:** A round closes when the raise cap is met or the end time passes, preventing new EOIs. For convertible instruments (SAFE, SAFT, SAFTE), the RoundManager provides functions to convert certificates into equity or tokens when a qualifying event such as a priced equity round or token generation event occurs. Conversions call `IssuanceManager` to mint new equity shares to SAFE holders or distribute tokens to SAFT holders, using valuation caps and discounts encoded in the certificates.

RoundManager is the recommended path for multi-investor raises, while DealManager remains available for bespoke single-counterparty agreements.

## Round Types and Compliance Modules

`RoundType` values determine how EOIs are handled:

* **FCFS:** allocations occur automatically on a first‑come basis.
* **FounderApproved:** the company reviews each EOI and explicitly allocates.

`RoundingPolicy` handles the rounding of fractional units when converting amounts into securities.

Compliance modules are attached per EOI. `LeXcheX` accreditation checks, `LexChexCondition`, and other `ICondition` modules can restrict participation based on jurisdictional or project-specific requirements.

## Compliance & Transfer Restrictions

After certificates are minted, their transferability is controlled by onchain hooks:

* **WhitelistTransferHook** requires both sender and receiver to be approved before a certificate can move.
* **ToggleTransferHook** allows the company to toggle transferability globally or for a specific certificate ID.

These hooks, combined with modules like `LeXcheX`, ensure that securities cannot be transferred to non‑qualified buyers even after the raise, keeping CorpFi operations compliant.

## Hybrid Instruments and Conversions

Each instrument in a round corresponds to a distinct certificate printer created during `createRound`, and certificates are minted upon allocation. For example, a **SAFE + Token Warrant** round causes the RoundManager to create two printers so allocation mints two NFTs – one for the SAFE and another for the warrant. SAFT certificates convert to tokens when the network launches, while SAFTEs or token warrants can convert to both equity and tokens via the RoundManager’s conversion function. This demonstrates how capital flows and securities issuance are automated in CorpFi.

**Delegated Signing Authority:** cyberRaise also provides flexibility for real-world corporate workflows through a delegation feature. In many startups, the person who controls the funds (e.g. a multi-signature corporate wallet) may not be the one actually executing documents day-to-day. To accommodate this, cyberRaise allows a founder or authorized company officer to **delegate signing authority** to another EVM address onchain. In practice, one wallet (for example, the founder’s personal wallet) can be authorized to propose and sign deals on behalf of another address (for example, the company’s official treasury wallet or a multi-sig). This means a company can keep its funds and issued securities in a secure custody account, while a delegate (with a separate key) handles the interactions and approvals on cyberRaise. The delegation is established by an onchain setting in the CyberAgreementRegistry – essentially, the company’s address appoints a delegate address and an optional expiry time for that delegation. Once in place, whenever the delegate signs an agreement, the platform recognizes it as if the company itself signed (the signature verification logic checks the delegation mapping to validate this). Only the specific delegate designated (and only within the time window, if an expiry was set) can act for the delegator, ensuring security. This feature streamlines the process for teams using multi-sig treasuries or hardware vaults: the founder can initiate and close deals with their own key, while funds flow in and out of the multi-sig as intended and the NFTs are ultimately held by the multi-sig or corporate entity. In short, founders can confidently conduct raises through their convenient hot wallet or executive account, while still having the final assets (investor funds and security NFTs) end up in the proper company-controlled wallets. The onchain audit trail will show that the company was the party to the agreement, with the delegate’s signature approved via the delegation mechanism, preserving legal clarity about who the actual issuer and counterparty are.

## Benefits of an Onchain Deal Flow

By turning the entire fundraising pipeline into code, cyberRaise delivers significant advantages over traditional methods:

* **Speed and Efficiency:** Deals that might take weeks or months to coordinate can now close in minutes once terms are agreed. Execution is automatic upon conditions being met – no waiting for wire transfers, coordinating schedules for signings, or couriering documents for signatures. This rapid closing means startups can secure funding faster and start deploying capital immediately. Observers note that MetaLeX’s approach *“streamlines startup fundraising by automating the SAFE process onchain, reducing legal fees”* – time saved is money saved.
* **Cost Reduction:** The automation of legal agreements and elimination of third-party intermediaries (like escrow agents or excessive legal oversight) cuts down on transaction friction and expenses. Founders spend far less on attorney hours and administrative costs, since the smart contracts enforce the terms automatically. Standardized onchain templates mean that in many cases, bespoke document drafting is minimized, further reducing legal overhead.
* **Trust Minimization:** All participants can trust the **code** rather than each other. The rules of the deal are enforced by smart contracts, removing the need to rely on a counterparty’s promise. Funds aren’t released until conditions are verified onchain, and signatures are cryptographically secured and validated. Investors gain confidence that their money will only be released if they indeed receive the agreed-upon securities, and founders are assured that investor funds are locked in escrow once the deal is signed. This cryptographic certainty eliminates the risk of either party backing out after the other has performed, effectively neutralizing counterparty risk.
* **Transparency and Immutable Records:** Every action in a cyberRaise deal – proposal creation, each party’s signature with timestamp, fund deposits, and final distributions – is recorded on the blockchain. This provides an immutable audit trail for regulators, auditors, or future investors. Anyone can independently verify what happened, when it happened, and the exact terms of the deal (since the template ID and key parameters are onchain in the CyberAgreementRegistry). The cap table updates in real-time onchain: an investor’s rights are evidenced by an NFT in their wallet, and that record cannot be tampered with or hidden. This level of transparency and certainty is unprecedented in traditional fundraising, where much is done on faith and paper. With cyberRaise, disputes over “who owns what” or whether funds were sent are virtually eliminated by the public ledger.
* **Global Accessibility with Built-In Compliance:** Because deals are conducted via Web3 wallets and smart contracts, cyberRaise opens up participation to global investors (with the necessary compliance checks baked in). Projects can broadly solicit interest (even via Twitter or community forums) and let the platform handle accreditation checks and regional restrictions. Modules like LeXcheX make it possible to publicly advertise a raise under Rule 506(c) and still restrict actual investment to verified accredited investors in the U.S., while also accommodating non-U.S. investors under Reg S. This expands the pool of capital for startups without sacrificing legal compliance, since the smart contracts rigorously enforce the rules on who can invest and automatically include the proper legend and transfer restrictions on the issued securities. A founder in Singapore could raise from investors in the U.S. and Europe seamlessly on the same platform, with each investor’s credentials verified onchain and the appropriate legal framework (Reg D, Reg S, etc.) automatically applied based on template selection.
* **Innovative Deal Possibilities:** The composable nature of cyberRaise’s contracts means new financing structures can be created or combined easily. Founders are not limited to vanilla SAFE terms – they can offer creative deal sweeteners like token warrants, revenue-sharing conditions, tiered conversions, or other novel mechanisms, and trust the platform to handle the complexity. For instance, cyberRaise supports SAFTEs (which give investors equity plus token rights) and other hybrids that align with Web3 projects’ unique needs. Because these features are modular, MetaLeX can introduce new templates or extensions (for example, for convertible notes, revenue loans, or NFT-based crowdfunding agreements) that plug into the same DealManager and escrow framework. All of this is accomplished in one unified workflow that keeps things simple for users despite the sophisticated outcomes. This flexibility to tailor deals, combined with automation, is paving the way for venture financing that is both innovative and compliant by design.

In sum, cyberRaise transforms fundraising into a faster, safer, and more transparent endeavor. Founders benefit from quick, automated deal execution and reduced overhead, while investors gain reassurance through built-in compliance checks and cryptographic security. The days of shuffling PDFs, coordinating endless emails, and relying on trust are replaced by smart contracts and NFTs that **encapsulate the deal**. Ultimately, cyberRaise doesn’t just make fundraising *simpler* — it makes it fundamentally more **programmatic and secure**. It paves the way for a future where startups can raise capital as easily as sending a transaction, with every legal and financial requirement handled by code. This is venture financing reimagined for the blockchain era, turning the vision of fully onchain startups (or **cyberCORPs**) into a reality today.

**Sources:** The details above are grounded in the cyberRaise app and codebase – notably the MetaLeX Tech **cybercorps-contracts** repository (which implements the DealManager, CyberAgreementRegistry, LeXcheX, etc.) and the live cyberRaise interface. The platform’s supported deal types and compliance features are backed by the smart contracts (see **SecurityClass** enums for SAFE, SAFT, SAFTE, etc., and condition checks for accreditation), ensuring that this launch is fully supported by onchain functionality and not just aspirational marketing.

---


# LeXcheX

Source: https://metalex-docs.vercel.app/cyberdeals/lexchex

**LeXcheX** is MetaLeX Labs’ solution for automating and tokenizing the verification of “accredited investor” status entirely onchain. It streamlines U.S. securities law compliance (specifically **Regulation D, Rules 506(b) and 506(c)**) by replacing cumbersome paper processes and invasive KYC with a blockchain-based certification. In essence, LeXcheX enables startups and DAOs to **“raise in public”** (general solicitation under Rule 506(c)) while ensuring that only verified accredited investors can ultimately purchase the securities. It can also be used in private fundraising (Rule 506(b)) to bolster due diligence on investors without traditional paperwork. The service exemplifies MetaLeX’s mission to fuse autonomous software with legal structures, making it possible to raise capital with just a few onchain clicks – with compliance built in.

## How the LeXcheX Process Works

---

LeXcheX combines smart contracts, offchain oracles, and legal agreements to issue a tamper-proof **Accredited Investor Certificate**. The process is simple for the user and consists of three main steps:

1. **Investor Questionnaire:** The user connects their wallet and provides basic info about their investor status (e.g. individual vs. entity). They indicate how they qualify as accredited – for example, by net worth over $1 million (since income can’t be verified onchain). Basic details like name, entity type, and jurisdiction are collected at this stage for inclusion in the legal certification.
2. **Onchain Wealth Evaluation:** LeXcheX then evaluates the investor’s **onchain asset holdings** to test the net worth criterion. It utilizes an oracle service (a dedicated TypeScript server) that queries the wallet’s balances via the Zapper API. If the **automated test** finds that the user’s blockchain portfolio meets the threshold (e.g. >= $1,000,000 in crypto assets), the investor passes this step. Notably, this is done **without invasive KYC** – no uploading bank statements or personal IDs – just a read of onchain balances. (The oracle is designed to check not only asset value but also potentially a 12-month holding period, to satisfy the net-worth test’s requirements.)
3. **Onchain Agreement & NFT Issuance:** If the asset check is successful, the investor then signs a **“cybernetic” legal agreement** entirely onchain, directly from their wallet. This EIP-712 signature serves as a digital representation of the investor’s representations and warranties (essentially, a promise that they are indeed accredited and the information is true). Once the agreement is signed, the smart contract (controlled by a U.S. licensed attorney) mints a **non-transferable NFT certificate** to the investor’s wallet as proof of accredited status. The investor pays a service fee of **$100 (in USDC)** to MetaLeX as part of this minting. The entire process – from asset verification to legal signature and certificate issuance – happens onchain in a few clicks, with **no paper or manual review needed**.

## Soulbound NFT Certificate and Legal Significance

---

The output of LeXcheX is a **soulbound** (non-transferable) **NFT certificate** that serves as an attorney-signed “**accredited investor letter**.” Technically, this certificate is implemented as an ERC-721 token with modifications for soulbound behavior (using the ERC-5484 and ERC-5192 standards). Once issued, it cannot be sold or transferred – it is permanently bound to the investor’s address (unless revoked or burned). The NFT’s metadata contains the investor’s name, entity type, jurisdiction, and a unique agreement ID, along with a stylized **SVG image** of the certificate. The image itself displays key information: it prominently declares **“U.S. Accredited Investor”**, indicates that the holder of the certificate is an accredited investor, states who certified it (e.g. “Certified by Gabriel Shapiro, Esq., of MetaLeX”), and shows an expiration date. This means an actual licensed attorney (MetaLeX’s counsel) is effectively signing off on the NFT – akin to a traditional lawyer’s letter vouching for the investor’s status, but now in smart-contract form. The certificate is **digitally signed and recorded onchain**, so anyone can cryptographically verify its authenticity and validity period.

The **LeXcheX Accredited Investor Certificate** (soulbound NFT) is a tokenized attorney’s letter confirming the holder’s accredited status. The certificate is emblazoned with “U.S. Accredited Investor,” marked as certified by MetaLeX’s attorney, and includes an expiration date and a unique agreement reference. It is explicitly labeled non-transferable and soul-bound, emphasizing its personal, compliance-oriented nature.

Each LeXcheX certificate comes with a **validity period of 90 days** (approximately three months). This aligns with U.S. SEC guidelines, which suggest that accredited investor verifications should be refreshed every 3 months for Rule 506(c) offerings. After the 90-day period, the NFT is considered expired (the smart contract can mark it invalid) and **anyone may trigger a revocation** of the token onchain. Investors can easily **renew** their certificate by re-running the onchain checks and paying the fee again for another 90-day extension, provided they still meet the requirements. The NFT also includes an admin-controlled revocation mechanism: if it turns out an investor misrepresented themselves or an error occurred, the contract owner (attorney) can **revoke** the certificate at any time, which burns the token and blacklists the address. These features ensure that only valid, up-to-date accreditations persist in the system.

From a legal perspective, companies can rely on a LeXcheX NFT the same way they would rely on a traditional lawyer’s accreditation letter. Under SEC Rule 506(c), an issuer is deemed compliant if they take “**reasonable steps to verify**” purchasers’ accredited status – obtaining a third-party **attorney’s certification letter** is one accepted method. **LeXcheX implements the “lawyer letter” method onchain**: by having an attorney oversee the process and effectively sign the NFT, the certificate evidences that “reasonable steps” were taken to verify the holder’s status. The NFT can be presented to fundraising platforms or token sale contracts, which can programmatically check that the wallet holds a valid accredited-investor NFT before letting them invest. This opens the door for **public fundraising** (general advertising of an investment round) without fear of accidentally selling to unverified investors. In private rounds under Rule 506(b), the NFT is not legally required, but it still provides a convenient assurance (for example, a startup could request investors to obtain LeXcheX certificates as an added layer of diligence).

## Integration with Fundraising Platforms

---

## MetaLeX Integration

LeXcheX is fully integrated into MetaLeX’s **cyberCORPS** onchain fundraising dApp. CyberCORPS is an early-stage financing platform that allows startups (organized as onchain “cyber corporations”) to raise capital by selling tokens or shares. With the LeXcheX integration, a startup using cyberCORPS can **toggle a setting to require accredited status** for their round. In the offering setup form, the issuer simply checks the option \*\*“Require LeXcheX Accredited Investor Status”. This ensures that only investors who hold a valid LeXcheX NFT certificate can participate in the sale. The platform’s smart contracts or front-end will verify the investor’s address against the LeXcheX ERC-721 contract. If an investor has not yet obtained their certificate, the interface can direct them to the LeXcheX application (at **lexchex.metalex.tech**) to go through the verification flow before investing. This seamless integration means founders can confidently advertise their raise (506(c) general solicitation) knowing that **all actual investors will be gated by LeXcheX** compliance checks. It effectively bakes compliance into the fundraising smart contract: unverified participants are filtered out, and only wallets with attorney-approved accreditation tokens can send funds or receive securities.

By combining cyberCORPS with LeXcheX, MetaLeX delivers an end-to-end onchain fundraising solution that is both **highly technical and deeply legal**. The technical side provides automation, efficiency, and trustlessness (smart contracts, oracles, NFTs), while the legal side ensures adherence to U.S. securities laws (verification of investor status, record-keeping of investor acknowledgments, attorney oversight). The result is a novel mechanism where **raising capital becomes as straightforward as issuing a token, and compliance is handled in parallel by code and cryptography**. LeXcheX not only simplifies life for founders and investors by skipping the paperwork, but it also stands as a pioneering example of using blockchain tech to solve real regulatory challenges in a provably compliant way. LeXcheX makes conducting an SEC-compliant offering a breeze – founders can focus on building and promotion, while the protocol ensures that only verified accredited investors end up holding the sale tokens. This integration of **law + code** is a cornerstone of MetaLeX’s approach to making organizations *“cyBernetic”*, and it positions cyberCORPS and LeXcheX as critical components of the onchain capital markets infrastructure.

## Third-Party Integrations

LeXcheX is designed to be highly friendly to third-party integration.

## Technical Integration Guide

LeXcheX is deployed across multiple chains to support various blockchain ecosystems. The contract address is the same on all supported networks:

```
Copy

LexCheX: 0x123E895e0e1a4e39b2E0488DB904AD37C7A62EeD;
```

## Checking Accreditation Status

To verify if an address has a valid LeXcheX accreditation, you can use the following function:

```
Copy

function hasValidLexCheX(address owner) public view returns (bool)
```

This function returns:

* `true` if the address has a valid, non-expired LeXcheX accreditation
* `false` if the address either has no LeXcheX token or if their accreditation has expired

Example usage in a smart contract:

```
Copy

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;
 
interface ILexCheX {
    function hasValidLexCheX(address owner) external view returns (bool);
}
 
contract YourContract {
    ILexCheX constant lexchex = ILexCheX(0x123E895e0e1a4e39b2E0488DB904AD37C7A62EeD);
    
    function testFunction(address investor) public view {
        if(!lexchex.hasValidLexCheX(investor)) revert NotAccredited();
        // ... rest of your function
    }
}
```

Here are examples using popular JavaScript/TypeScript libraries:

## Viem

```
Copy

import { createPublicClient, http } from 'viem'
import { mainnet } from 'viem/chains'
 
const LEXCHEX_ADDRESS = '0x123E895e0e1a4e39b2E0488DB904AD37C7A62EeD'
const LEXCHEX_ABI = [{
  name: 'hasValidLexCheX',
  type: 'function',
  stateMutability: 'view',
  inputs: [{ name: 'owner', type: 'address' }],
  outputs: [{ name: '', type: 'bool' }]
}] as const
 
const client = createPublicClient({
  chain: mainnet,
  transport: http()
})
 
// Check if an address has valid accreditation
const checkAccreditation = async (address: string) => {
  const isAccredited = await client.readContract({
    address: LEXCHEX_ADDRESS,
    abi: LEXCHEX_ABI,
    functionName: 'hasValidLexCheX',
    args: [address]
  })
  
  return isAccredited
}
```

## Ethers.js

```
Copy

import { ethers } from 'ethers'
 
const LEXCHEX_ADDRESS = '0x123E895e0e1a4e39b2E0488DB904AD37C7A62EeD'
const LEXCHEX_ABI = [
  'function hasValidLexCheX(address owner) view returns (bool)'
]
 
// Using ethers v6
const provider = new ethers.JsonRpcProvider('YOUR_RPC_URL')
const lexchex = new ethers.Contract(LEXCHEX_ADDRESS, LEXCHEX_ABI, provider)
 
// Check if an address has valid accreditation
const checkAccreditation = async (address: string) => {
  const isAccredited = await lexchex.hasValidLexCheX(address)
  return isAccredited
}
```

**Sources:**

* [LeXcheX Smart Contract Code](https://github.com/MetaLex-Tech/cybercorps-contracts/blob/e2afc8b1fbecff89f97b8b23d6134508ed00437a/src/creds/lexchex.sol)
* [MetaLeX Launches LeXcheX](https://x.com/MetaLeX_Labs/status/1943310043853521392)

---


# LeXscroW

Source: https://metalex-docs.vercel.app/cyberdeals/lexscrow

LeXscroW is an ownerless, condition‑based escrow system used by BORGs to enforce onchain deal logic. Escrows are deployed without an admin, and their release conditions are immutable once set. Contracts are non‑custodial—the funds remain in escrow until predefined rules resolve them.

## LexScroWLite in cyberCORPs

cyberCORPs embed a streamlined implementation called **LexScroWLite** to mediate deals between a corp and a counterparty. The library manages escrow state, enforces conditions from the Cyber Agreement Registry and releases assets only when a deal is paid and finalized.

LexScroWLite supports escrow of ERC20, ERC721 and ERC1155 tokens. It can:

* create a new escrow tied to a specific agreement;
* pull funds from a buyer once a counterparty is set;
* finalize the deal by routing corp assets to the buyer and buyer assets to the corp; and
* void and refund if the agreement is cancelled.

This lite contract is used internally by cyberCORPs for trustless execution while keeping funds non‑custodial.

## Core Features

* **Ownerless deployment** – contracts have no privileged account after creation.
* **Immutable conditions** – execution rules can reference signatures, time windows or oracle data and cannot be changed after deployment.
* **Flexible depositors** – escrows may restrict who can deposit or allow open participation with optional post‑deposit rejection.
* **Automatic refunds** – deposits return to senders if conditions fail or the escrow expires.
* **Composable** – BORGs can pair LeXscroW with implants or MetaVesT for richer deal logic.

## Execution Flow

1. Parties deposit tokens into the escrow contract.
2. Anyone may trigger execution once all conditions are satisfied, releasing funds to their counterparties.
3. If the escrow expires or a depositor is rejected, a refund function returns the assets.

## Contract Types

* **DoubleTokenLeXscroW** – bilateral escrow for two ERC20 tokens; each side deposits the agreed amount and receives the other's tokens when conditions clear.
* **TokenLeXscroW** – unilateral escrow for a single ERC20 token with refund capability; useful for token sales or milestone releases.
* **EthLeXscroW** – native token variant handling ETH or other gas tokens with the same ruleset.

## Example Uses

* Trustless token swaps between BORGs or DAOs.
* Funding milestones where a DAO releases tokens to a GrantsBORG as progress is verified.
* Cross‑DAO collaborations that pool resources and release them only when shared conditions are met.
* M&A escrows that swap governance tokens after both communities approve.
* Social bets, such as KOL wagers resolved by an oracle feed.

[Source code and audits](https://github.com/MetaLex-Tech/LeXscroW) and the [LexScroWLite library used by cyberCORPs](https://github.com/MetaLex-Tech/cybercorps-contracts/blob/develop/src/libs/LexScroWLite.sol) are available for teams that need deeper integration details.

---


# MetaVesT

Source: https://metalex-docs.vercel.app/cyberdeals/metavest

MetaVesT is a BORG‑compatible vesting and token lockup protocol for ERC20 tokens. It supports sophisticated grant structures that mirror real‑world legal agreements while remaining trust‑minimized.

## Key Capabilities

* **Dual curves** – tokens can "vest" and "unlock" on independent schedules with optional cliffs.
* **Options and restricted awards** – record token‑option exercise prices and restricted‑token repurchase prices in stablecoins to support 83(b) elections and capital‑gains treatment.
* **Group amendments** – a majority‑in‑value of grantees plus the grantor can update terms for an entire cohort.
* **Can't‑be‑evil guarantees** – unless an amendment is approved, vested tokens cannot be clawed back and only vesting can be terminated.
* **Pass‑through voting** – unvested or locked tokens may still be staked and voted in a DAO.
* **Milestones** – vesting can depend on discrete events as well as elapsed time.

## How It Works

MetaVesT escrows the grantor's tokens and issues non-transferable receipts to grantees. Each receipt tracks both vesting and unlocking curves along with optional price terms for options or repurchases. As time or milestones progress, the contract continually recalculates how many tokens are vested and unlocked. Grantees may withdraw the amount that satisfies both curves, while any excess remains locked in the vault.

## Grant Lifecycle

1. **Create grant** – the grantor deposits tokens and defines curves, cliffs and price terms.
2. **Track progress** – time or milestone updates move tokens from unvested to vested and from locked to unlocked.
3. **Withdraw tokens** – grantees can claim the lesser of the vested and unlocked amounts; unvested tokens stay escrowed.
4. **Amend or terminate** – cohort‑wide amendments require majority approval plus the grantor. Otherwise, only vesting may be terminated.

## Tax Optimization Mechanics

* **Token‑option exercise price** – grantees can pay a preset stablecoin amount to turn options into tokens early, locking in the grant's fair market value and starting the capital‑gains holding period.
* **Restricted‑token repurchase price** – the grantor may buy back unvested tokens at an agreed stablecoin price, enabling 83(b) elections without surprise ordinary‑income consequences if employment ends.

These mechanics let MetaVesT mirror traditional equity plans and bake tax strategy directly into onchain grants.

## Uses

MetaVesT can manage compensation for BORG personnel or govern how GrantsBORGs release tokens to recipients. It can also be paired with LeXscroW for escrowed token deals or with implants that respond to DAO approvals.

The MetaVesT repository contains the Solidity contracts, deployment scripts and Foundry tests demonstrating linear schedules, cliffs, milestones and group amendments. Developers can explore the repository for examples of integrating the protocol with DAO governance or with modules like LeXscroW.

---


# Round Manager

Source: https://metalex-docs.vercel.app/cyberdeals/round-manager

The `RoundManager` contract drives the lifecycle of fundraising rounds in the cyberDeals stack. It stores round metadata, tracks expressions of interest (EOIs), and exposes functions that move a raise from creation through conversion. For an overview of how these rounds surface in the app, see [cyberRaise](/cyberdeals/cyberraise).

## Round Lifecycle

* **createRound** – founder opens a round with parameters such as allocation size, deal template, and whether the round is first‑come‑first‑served (FCFS) or requires explicit approval.
* **submitEOI** – investors signal interest in the round by submitting an EOI indicating how much they want to commit.
* **allocate** – an authorized role accepts an EOI and reserves allocation for that investor.
* **reject** – an EOI can be rejected, keeping the round open for other participants.
* **closeRound** – ends the round and prevents new EOIs or allocations.
* **convert** – after a successful close, accepted EOIs are converted into on‑chain agreements and the corresponding security NFTs are minted.

## Data Structures

`Round` records the core details of a raise: creator, total allocation, template reference, whether it is FCFS, and if issued securities are currently transferable.

`EOI` (expression of interest) captures an investor’s requested allocation, wallet address, and current status (pending, accepted, or rejected).

## FCFS vs Founder‑Approved Rounds

FCFS rounds automatically allocate to the first valid EOIs until the allocation is exhausted. Founder‑approved rounds queue EOIs and require an authorized BorgAuth role to call `allocate` or `reject` before funds can move. This allows the company to vet investors while still managing the process on‑chain.

BorgAuth roles therefore determine who can advance the round lifecycle, accept or reject EOIs, and toggle transferability or other restrictions.

---


# Cybernetic Law introduction

Source: https://metalex-docs.vercel.app/cybernetic-law/intro-to-cybernetic-law

MetaLeX defines **cybernetic law** as the fusion of legal agreements with autonomous technologies so that code and law operate as a single system. In practice, this means legal contracts are interwoven with smart contracts and onchain data, allowing agreements to self-execute and be verified through code. This approach is part of a broader **cybernetic economy** vision where legal, governance, and operational functions seamlessly integrate with blockchain protocols【49†L6-L13】. By embedding references to onchain data structures and smart contracts directly in legal templates, cybernetic law moves beyond traditional paper-centric contracting. The goal is to create an “internet of agreements” that is modular, composable, and cryptographically verifiable without relying on closed platforms or manual oversight.

## Why conventional legal tech falls short

Mainstream contract automation tools live in centralized walled gardens that are closed-source, non-composable, and optimized for humans reading static PDFs. Template language is often hidden behind rigid questionnaires, and the generated documents sit on proprietary servers. This **black box** approach obscures important choices and stifles the open standardization that produced instruments like the Y-Combinator SAFE or NVCA model documents. Moreover, because these legacy tools don’t plug into public blockchains, they cannot leverage onchain trust-minimization or automated enforcement. In short, conventional legal tech keeps agreements static and platform-bound, falling short of what cryptonative, programmable agreements require.

## The MetaLeX alternative

MetaLeX offers an open approach: public **cybernetic law templates** that explicitly reference onchain artifacts. Parties can select parameters and sign the agreement directly from their crypto wallets, with those selections stored onchain. Anyone can later reconstruct the human-readable text by combining the IPFS-hosted template with the onchain transaction data, eliminating vendor lock-in and enabling any interface to render the agreement in a traditional format. In essence, MetaLeX turns contracts into interoperable “legal lego” components.

This method has already been implemented in agreements like the BORG Participation Agreement and the Cybernetic Token Exchange Agreement (CyTEA). Using MetaLeX’s platform, a deal is **parametrized and executed onchain**: the parties’ choices (e.g. quantities, prices, dates) are recorded to a smart contract and also dynamically populate the legal prose. Looking forward, the team envisions optional privacy layers for sensitive data, tokenized representations of contractual rights and obligations, more natural language output from onchain records, and even fully formalized, machine-generable agreements. All of these enhancements aim to make onchain deals as robust and user-friendly as traditional contracts, while remaining **trust-minimized** and self-enforcing.

## Ricardian Triplers

To tightly bind legal prose with enforcement code, MetaLeX introduced the **Ricardian Tripler**. A tripler bundles three components into a single deal package:

1. **Code** – a specific smart contract deployed at a known address (the “active” part of the agreement).
2. **Legal text** – a standard form agreement that references that smart contract and defines the legal relationship.
3. **Parameters** – the negotiated values that instantiate both the code and the text.

By signing one onchain transaction, parties simultaneously populate the parameters, adopt the legal text, and (if needed) deploy the enforcing contract. Our initial implementation targets double-token swaps under the LeXscroW escrow system, pairing a legal agreement with a non-custodial smart escrow that cannot execute unless both parties sign. Supporting contracts like `AgreementV1Factory`, `DoubleTokenLexscrowRegistry`, and `SignatureValidator` manage proposal creation, counterparty confirmation, and signature verification onchain – yielding an end-to-end onchain deal lifecycle without dependence on any centralized SaaS platform. In short, Ricardian Triplers ensure that **for every onchain action there is a mirrored legal context**, and vice versa, enforcing alignment between what the code does and what the legal text promises.

## Toward *lex cryptographia*

The MetaLeX vision paper argues that autonomous technologies are creating de facto actors and transactions that operate outside traditional state approval. Yet humans remain in the loop, and disputes still require norms of evidence and accountability. Rather than reverting to ad-hoc “rule of men,” MetaLeX advocates a cryptography-native rule of law – **lex cryptographia** – where code handles deterministic functions and legal mechanisms constrain any human discretion【49†L22-L26】. In essence, lex cryptographia is an emerging form of law defined by rules administered through self-executing smart contracts and decentralized organizations【49†L22-L26】.

Crucially, the long-term vision is to **gradually transition to a stateless, cryptonative legal system** that can operate independently of any single nation’s legal apparatus. MetaLeX believes the missing piece is a cryptonative substitute for the rule of law: an autonomous legal framework in which onchain code provides the enforcement backbone instead of courts【41†L0-L2】. Today’s cybernetic organizations (BORGs) still rely on traditional charters and a mix of legal and technical mechanisms (they are often incorporated as normal companies)【52†L79-L87】, but each innovation shifts more trust and functionality from legal institutions into transparent code. The ultimate aim is a legal order where **trust is placed in verifiable code** rather than in fallible jurisdictions – a system “free of the corruption of the previous trust-dependent one,” as the MetaLeX team describes it【50†L226-L234】. This approach draws on emerging digital jurisprudence (sometimes called **digisprudence**) to determine where code may serve as a superior replacement for traditional legal processes, not merely an aid to them【49†L18-L24】.

Cybernetic law templates and Ricardian Triplers are early building blocks toward this cryptonative rule-of-law system. By tightly merging legal agreements with self-executing code, they lay the groundwork for **lex cryptographia** – a future in which agreements, organizations, and even dispute resolutions can be handled onchain with minimal reliance on legacy legal infrastructure【50†L226-L234】. Each step in this direction – from onchain contract signing to automated escrow enforcement – is bringing us closer to a world of **stateless cryptonative law** governed by code, with the assurance that such code operates under enforceable legal principles rather than outside of them.

---
