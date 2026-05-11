# Arbitrum Stylus Master Guide

Derived from [Stylus Quickstart](https://docs.arbitrum.io/stylus/quickstart) and Expert Practices.

## 🧠 Phase 1: Mindset Shift (Solidity -> Rust Stylus)

The Agent must understand that Stylus is not "Solidity in Rust." It requires a low-level understanding of WASM and Rust's safety guarantees.

### 1. No Constructors
- **Fact**: WASM does not execute constructor logic during deployment.
- **Rule**: Use an `init` function protected by an `Initialized` storage flag.

### 2. Composition Over Inheritance
- **Fact**: Stylus macros for inheritance are limited and prone to storage duplication.
- **Rule**: Embed parent structs (e.g., Erc20) inside the child contract struct and use wrappers.

### 3. WASM Constraints
- **Fact**: Contracts must be under 24KB when compiled to WASM.
- **Rule**: Optimize using `opt-level = 'z'` and avoid heavy external crates.

## 🛠️ Phase 2: Actionable Resource Catalog

Use these specific libraries and repositories to build faster. Do not reinvent the wheel.

### 📜 Smart Contract Libraries
- **OpenZeppelin Stylus**: The gold standard for ERC-20, ERC-721, and Access Control in Rust.
- **Awesome Stylus**: A curated list of proof-of-concepts, including Uniswap V2 in WASM and specialized NFT implementations.
- **Stylus SDK**: The core framework for writing Stylus contracts.

### 🧪 Testing & Tooling
- **Motsu**: A fast, Rust-native, in-memory testing environment. Essential for parallelized unit tests.
- **Cargo Stylus**: The CLI tool for checking contract validity and managing gas/size.
- **Moo**: Mocking utilities for simulating on-chain storage during testing.

### 🌐 Frontend & App Integration
- **Alloy-sol-types**: For encoding/decoding Solidity types in Rust to ensure compatibility with existing Ethereum tools.
- **Vite + React + Tailwind**: The recommended frontend stack for building agent-facing dashboards (similar to the "Wingman" pattern).

## 📋 Phase 3: AI Workflow (The "Skill" Loop)

1. **Analyze**: Read requirements -> Consult `resources/stylus.md`.
2. **Initialize**: Run `scripts/scaffold.py` to set up optimized Cargo.toml.
3. **Code**: Write Rust code using the Composition Pattern.
4. **Audit**: Run `scripts/check_size.py` to verify WASM size is < 24KB.
5. **Validate**: Generate and run Motsu tests.

## 💬 Phase 4: Detailed Prompts to Trigger Skills

### 1. The "Architect" Prompt (Project Initialization)
> "Act as a Stylus Expert. I need to build a [Project Name]. Use the scaffold.py script to initialize a new Stylus project. Ensure you include the OpenZeppelin Stylus libraries for [ERC-20/AccessControl] and configure the workspace for Motsu testing."

### 2. The "Converter" Prompt (Solidity to Rust)
> "Analyze this Solidity contract: [Paste Code]. Convert it to Arbitrum Stylus Rust. Constraint: Do not use deep inheritance. Use the Composition pattern as described in rust_patterns.md. Implement an init function instead of a constructor."

### 3. The "Optimizer" Prompt (Binary Size Control)
> "My Stylus contract logic is finished. Run scripts/check_size.py to measure the WASM binary. If it exceeds 24KB, analyze the imports and suggest code-stripping or opt-level configurations in Cargo.toml to reduce the size."

### 4. The "Tester" Prompt (High-Speed Validation)
> "Write a comprehensive unit test suite for this Stylus contract using the Motsu framework. Ensure the tests use DashMap for thread-safe storage simulation so they can run in parallel. Focus on edge cases like [Unprivileged Access / Zero Balance Transfers]."

## 🔗 Reference Links
- [Research: Vector Search for Decentralized Systems](https://research.arbitrum.io)
- [Tutorial: Testing Stylus with Motsu](https://github.com/OpenZeppelin/motsu)
- [Community: Arbiverse Bangkok Intro to Stylus](https://arbitrum.io/community)

## ⚡ Skill Set B: Arbitrum Stylus Rust Engineer

This skill requires high-performance Rust coding for **High-Frequency Betting** and **EVM Compatibility**.

### Key Concepts
1.  **sol_storage!**: The macro for mapping Solidity storage slots to Rust structs.
2.  **#[external]**: Attribute to expose Rust functions to the EVM (callable by other contracts/users).
3.  **WASM Optimization**: Critical for gas costs. Use `opt-level = 'z'` and avoid `std` where possible.

### Tooling
-   **cargo stylus**: CLI for building, checking, and deploying.
-   **motsu**: Unit testing framework for Stylus.

### 🏗️ Prototype: The "Chip Manager" (Stylus/Rust)

**Goal**: Handle bets efficiently using Rust's memory safety and low gas costs.

```rust
/*
  Prototype: Chip Manager
  File: lib.rs
*/

use stylus_sdk::{prelude::*, alloy_primitives::U256};

sol_storage! {
    #[entrypoint]
    pub struct PokerTable {
        mapping(address => uint256) balances;
        uint256 pot;
    }
}

#[external]
impl PokerTable {
    // High-performance betting function
    pub fn place_bet(&mut self, amount: U256) -> Result<bool, Vec<u8>> {
        let player = self.vm.msg_sender();
        
        // 1. Storage access is cheaper in Stylus
        let current_balance = self.balances.get(player);
        
        if current_balance < amount {
            return Ok(false); // Fail gracefully
        }

        // 2. Update state in-memory before writing to storage
        self.balances.setter(player).set(current_balance - amount);
        self.pot.set(self.pot.get() + amount);

        Ok(true)
    }
}
```
