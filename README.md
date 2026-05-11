# Builder Skill: The AI Agent’s Web3 Engineering Force Multiplier

Transform your AI agent into a **production-grade Web3 engineering assistant** with deep expertise in **Solidity**, **Arbitrum Stylus (Rust/WASM)**, **Zero-Knowledge Systems**, and the **Midnight Network privacy stack**.

This skill is designed for developers, DevRel engineers, startup builders, and protocol teams building the next generation of decentralized applications.

---

# 🌐 What This Skill Enables

Your AI agent becomes capable of:

- Architecting scalable smart contract systems
- Writing gas-efficient Solidity contracts
- Building high-performance WASM contracts with Stylus
- Designing privacy-preserving applications on Midnight
- Generating zero-knowledge proof circuits
- Running security reviews & vulnerability analysis
- Optimizing WASM binary size constraints
- Creating production-grade testing pipelines
- Assisting with protocol integrations & cross-chain workflows
- Explaining advanced blockchain concepts like a senior Web3 engineer

---

# 🚀 Quick Start

## 1️⃣ Install the Builder Skill

```bash
npx skills add https://github.com/phamdat721101/builder-skills
```

---

## 2️⃣ Initialize a Web3 Project

```bash
# Create a production-ready Stylus project
python3 scripts/scaffold.py my-stylus-project
```

The scaffold automatically configures:

- Optimized Cargo workspace
- OpenZeppelin Stylus libraries
- WASM optimization flags
- Motsu testing setup
- Foundry compatibility
- Security-first project structure
- CI/CD-ready configurations

---

## 3️⃣ Activate Expert Mode

Prompt your AI agent naturally:

> “Act as a Senior Stylus Protocol Engineer. Architect a scalable ERC-20 protocol with staking, upgradeability, and secure treasury management.”

Or:

> “Act as a Midnight privacy engineer. Design a confidential voting protocol using zero-knowledge proofs and hidden state.”

---

# 🧠 The Recursive Engineering Loop

This skill follows a professional protocol engineering workflow.

---

## 1. Analyze

The agent first studies:

- Requirements
- Protocol constraints
- Tokenomics
- Security assumptions
- Blockchain execution environment
- Resource guides (`resources/`)

Example:

```txt
Analyze resources/stylus.md and explain the WASM memory model before coding.
```

---

## 2. Initialize

Generate robust architecture foundations:

```bash
python3 scripts/scaffold.py protocol-name
```

Includes:

- Modular architecture
- Secure dependency setup
- Workspace optimization
- Testing infrastructure
- Deployment configuration

---

## 3. Build

Generate production-grade code following modern Web3 engineering principles.

### Enforced Design Patterns

- Composition over inheritance
- Explicit initialization
- Minimal trusted surface area
- Deterministic state transitions
- Modular protocol design
- Upgrade-safe architecture
- Storage-safe patterns

---

## 4. Audit

Automated validation layer:

```bash
python3 scripts/check_size.py
```

The AI agent checks:

- WASM binary size
- Gas inefficiencies
- Storage collisions
- Reentrancy risks
- Access control flaws
- Unsafe external calls
- Integer overflows
- Upgradeability risks
- Unsafe Rust patterns

---

## 5. Validate

Generate heavy-duty tests using:

- Foundry
- Motsu
- Fuzz testing
- Property-based testing
- Invariant testing
- Differential testing
- ZK proof verification testing

---

# 🔥 Deep Dive: Arbitrum Stylus Engineering

## Stylus Is NOT “Solidity in Rust”

Stylus introduces an entirely different execution philosophy.

Instead of writing EVM bytecode directly, contracts compile into **WASM (WebAssembly)**, enabling:

- Massive performance improvements
- Lower gas costs
- Safer memory handling
- Advanced Rust abstractions
- Parallelizable execution patterns
- Better cryptographic tooling

---

# ⚡ Core Stylus Mindset

## 1️⃣ No Constructors

Stylus contracts avoid Solidity-style constructors.

### ❌ Avoid

```solidity
constructor() {
    owner = msg.sender;
}
```

### ✅ Use Explicit Initialization

```rust
fn init(&mut self, owner: Address) {
    self.owner.set(owner);
    self.initialized.set(true);
}
```

Why?

- Better upgradeability
- Safer deployment flow
- Deterministic initialization
- Proxy compatibility

---

## 2️⃣ Composition > Inheritance

Rust favors composition over Solidity’s inheritance-heavy design.

### ❌ Deep Inheritance

```solidity
contract Token is ERC20, Ownable, Pausable
```

### ✅ Composition Pattern

```rust
struct MyToken {
    erc20: Erc20,
    ownable: Ownable,
    pausable: Pausable,
}
```

Benefits:

- Explicit state management
- Reduced complexity
- Better modularity
- Safer upgrades
- Easier auditing

---

## 3️⃣ WASM Constraints Matter

Stylus contracts must stay under the **24KB WASM deployment limit**.

### Optimization Strategies

- Strip unused imports
- Use `opt-level = "z"`
- Minimize macro bloat
- Avoid unnecessary generics
- Use static dispatch when possible
- Reduce panic-heavy logic

---

# ⚙️ Advanced Stylus Features

## 🔹 Parallel-Friendly Architecture

Stylus allows future-oriented execution models optimized for concurrency.

Design considerations:

- Minimize shared mutable state
- Use deterministic execution flows
- Isolate storage regions
- Avoid cross-module lock contention

---

## 🔹 Rust Memory Safety

Unlike Solidity:

- No unsafe pointer arithmetic
- Strong compile-time guarantees
- Better cryptographic integrations
- Safer serialization/deserialization

---

## 🔹 WASM Performance Engineering

The AI agent can optimize for:

- CPU instruction count
- Memory allocation patterns
- Serialization overhead
- Storage access minimization
- Hashing efficiency

---

# 🛡️ Solidity Expert Mode

## Security-First Development

The AI agent automatically reviews for:

- Reentrancy
- Flash loan attack vectors
- Signature replay
- Delegatecall abuse
- Oracle manipulation
- Integer overflow/underflow
- Access control misconfiguration
- Unsafe upgradeability

---

## Supported Solidity Patterns

- UUPS Proxies
- Transparent Proxies
- Diamond Standard (EIP-2535)
- ERC-20
- ERC-721
- ERC-1155
- ERC-4626
- Permit (EIP-2612)
- Account Abstraction
- Meta-transactions

---

# 🔐 Midnight Network Expert Mode

## Privacy-Native Smart Contracts

Midnight introduces confidential smart contract execution using:

- Zero-knowledge proofs
- Hidden state transitions
- Opaque data structures
- Selective disclosure
- Confidential computation

---

# 🧩 Midnight Capabilities

## 🔹 Opaque State

Hide:

- User balances
- Voting choices
- Trading strategies
- Identity metadata

Example prompt:

> “Generate a Compact contract using opaque balances and private transfer verification.”

---

## 🔹 Zero-Knowledge Circuits

Generate circuits for:

- Anonymous voting
- Private poker
- Identity verification
- Confidential DAOs
- Hidden bidding systems
- Private stablecoin transfers

---

## 🔹 Witness-Based Execution

Midnight supports witness-driven validation flows.

Use cases:

- Hidden ownership proofs
- Private game logic
- Identity attestations
- Selective disclosure systems

---

# 🧠 The 6 Power Prompts

## 1️⃣ The Architect

> “Act as a Senior Stylus Protocol Architect. Initialize a modular DeFi protocol using Rust composition patterns, OpenZeppelin Stylus libraries, Foundry testing, and secure treasury controls.”

---

## 2️⃣ The Solidity Converter

> “Convert this Solidity contract into optimized Arbitrum Stylus Rust. Eliminate deep inheritance and redesign the architecture using composition patterns.”

---

## 3️⃣ The WASM Optimizer

> “Analyze the generated WASM binary. Reduce deployment size under 24KB while preserving functionality and security guarantees.”

---

## 4️⃣ The Security Auditor

> “Audit this Solidity protocol for reentrancy, unsafe delegatecall usage, access control flaws, storage collision risks, and oracle manipulation vectors.”

---

## 5️⃣ The ZK Engineer

> “Generate a zero-knowledge proof circuit for anonymous voting with hidden voter identities and verifiable tally correctness.”

---

## 6️⃣ The Protocol Tester

> “Write invariant tests, fuzz tests, and edge-case validation for this staking protocol using Foundry and Motsu.”

---

# 🎮 Advanced Use Case: Private Poker Protocol

The “Holy Grail” of decentralized gaming.

A fully decentralized poker system where:

- Cards remain private
- Bets settle instantly
- Hands are provably fair
- Players cannot cheat
- State remains confidential

---

# 🏗️ Multi-Chain Architecture

| Step | Action | Network | Technology |
|------|---------|----------|-------------|
| 1 | Dealer encrypts deck & commits hash | Midnight | Compact Contract |
| 2 | Players prove card ownership | Midnight | ZK Witness |
| 3 | Betting logic executes | Arbitrum Stylus | Rust/WASM |
| 4 | Hand strength verified privately | Midnight | ZK Circuit |
| 5 | Pot distributed trustlessly | Arbitrum | Stylus Verification |

---

## Example Prompt

> “Act as a Web3 Gaming Architect. Generate the Midnight privacy circuit for hidden poker hands and the Stylus betting engine for fast wagering.”

---

# 🛠️ Included Tooling

| Tool | Purpose | Usage |
|------|----------|--------|
| `scripts/scaffold.py` | Generates optimized Web3 project structure | `python3 scripts/scaffold.py app-name` |
| `scripts/check_size.py` | WASM binary size auditing | `python3 scripts/check_size.py` |
| `resources/stylus.md` | Deep Stylus engineering guide | Referenced by AI |
| `resources/midnight.md` | Midnight privacy development | Referenced by AI |
| `resources/security.md` | Smart contract audit checklist | Referenced by AI |
| `resources/zk.md` | ZK architecture patterns | Referenced by AI |

---

# 🔬 Advanced Domains Supported

## DeFi
- AMMs
- Lending protocols
- Liquid staking
- Yield aggregators
- Stablecoins

## Infrastructure
- Cross-chain bridges
- Oracles
- Relayers
- Intent systems

## Privacy
- Anonymous payments
- Hidden governance
- Private DAOs
- Confidential identities

## Gaming
- Provably fair games
- Hidden-state gameplay
- NFT economies
- On-chain tournaments

---

# 🌍 Why This Skill Matters

Modern Web3 development is no longer just writing Solidity.

The next generation of blockchain engineering requires:

- WASM optimization
- Rust protocol architecture
- Zero-knowledge systems
- Privacy-preserving computation
- Cross-chain coordination
- Formal security thinking

This Builder Skill transforms AI from a simple code assistant into a **full-stack protocol engineering co-pilot**.

---

# 🤝 Contributing

PRs are welcome.

Please ensure contributions follow:

- SOLID principles
- Security-first architecture
- Minimal complexity
- Modular protocol design
- Gas/WASM efficiency
- Privacy-preserving patterns

---

# ⚡ Final Vision

This is more than a coding skill.

It is an AI-native Web3 engineering framework capable of helping builders design:

- Scalable protocols
- Privacy-preserving applications
- High-performance WASM contracts
- ZK-powered systems
- Production-ready decentralized infrastructure

The future of Web3 development is:

- AI-assisted
- Privacy-native
- WASM-powered
- ZK-secured
- Multi-chain by default

And this Builder Skill is designed for that future.