---
name: builder-skill
description: A comprehensive Web3 builder skill for learning Solidity, Stylus, and Midnight.
---

# Web3 Builder Skill

 This skill assists you in becoming a proficient Web3 builder by providing expert knowledge and guidance on three key areas:
 1.  **Solidity Development** (Ethereum Standard)
 2.  **Arbitrum Stylus** (Rust Smart Contracts)
 3.  **Midnight Network** (Privacy-First Blockchain)
 4.  **Advanced Agent Workflows** (Pro Hacks)

 ## When to use

 Use this skill when the user asks about:
 - Learning or writing Solidity smart contracts.
 - Getting started with Arbitrum Stylus (Rust contracts).
 - Understanding or developing for the Midnight Network.
 - Best practices, common pitfalls, or setup guides for these technologies.
 - Building Hybrid Privacy dApps (e.g., Private Poker using Midnight + Stylus).

 ## Instructions

 ### 1. Identify the User's Goal

 Determine which technology the user is interested in:

 -   **Solidity/Ethereum**: refer to [Solidity Resources](resources/solidity.md).
 -   **Arbitrum Stylus**: refer to [Stylus Resources](resources/stylus.md).
 -   **Midnight Network**: refer to [Midnight Resources](resources/midnight.md).
 -   **Advanced Workflow/Hacks**: refer to [Advanced Workflows](resources/advanced_agent_workflows.md).

 ### 2. Apply the Knowledge

 #### For Solidity Requests:
 -   **Teach**: Explain concepts using the "Teaching Mode" in `solidity.md`.
 -   **Review**: Audit code using the "Code Review Mode" checklist.
 -   **Build**: Use the "Build Mode" to suggest scaffoldings or patterns.
 -   **Warn**: ALWAYS check for "Critical Gotchas" (e.g., token decimals, reentrancy).

 #### For Stylus Requests:
 -   **Mindset Shift**: emphasize "No Constructors", "Composition Over Inheritance", and "WASM Constraints".
 -   **Setup**: Use `scripts/scaffold.py` to initialize projects with optimized configurations.
 -   **Check**: Use `scripts/check_size.py` to verify binary size constraints (< 24KB).
 -   **Deploy**: Explain the deployment process (cargo stylus deploy).
 -   **Private Poker**: See "Chip Manager" prototype in `stylus.md` for high-freq betting state.

 #### For Midnight Requests:
 -   **Architecture**: Explain the roles of Node, Indexer, and Proof Server.
 -   **Compact**: Reference Compact language features (Privacy patterns, Types).
 -   **SDK**: Guide on TypeScript integration.
 -   **Private Poker**: See "Card Guardian" prototype in `midnight.md` for ZK hand verification.

 #### For Advanced Workflow Requests:
 -   **Plan Mode**: ENFORCE planning for complex tasks (Hack #2).
 -   **Parallelize**: Suggest Git Worktrees for multi-feature work (Hack #1).
 -   **Self-Correct**: Remind user to update `CLAUDE.md` on recurring errors (Hack #3).
 -   **Visualize**: Use ASCII diagrams for structural changes (Hack #10).

 ### 3. General Principles
 -   **SOLID**: Ensure generated code or advice follows clean architecture.
 -   **Simple**: Do not overcomplicate; provide the essential files/steps first.
 -   **No Repetition**: Avoid common mistakes listed in the resources.
