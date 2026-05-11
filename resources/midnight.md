# Midnight Network Learning Resources
Derived from [Midnight Agent Skills](https://github.com/UvRoxx/midnight-agent-skills)

## What is Midnight?
Midnight is a data protection blockchain that safeguards sensitive commercial and personal data.

## Key Concepts & Skills

### Compact Smart Contracts (`midnight-compact-guide`)
- **Privacy Patterns**: Selective disclosure, commit-reveal.
- **Data Types**: `Counter`, `Uint`, `Bytes`, `Map`, `Vector`, `Set`.
- **References**: `privacy-selective-disclosure.md`, `tokens-shielded-unshielded.md`.

### SDK Integration (`midnight-sdk-guide`)
- **Focus**: TypeScript SDK for dApps.
- **Features**: Wallet integration (Lace), state management, error handling.

### Infrastructure (`midnight-infra-setup`)
- **Node**: `midnight-node` (ws://127.0.0.1:9944)
- **Indexer**: `midnight-indexer` (http://127.0.0.1:8088)
- **Proof Server**: `midnight-ledger` (http://127.0.0.1:6300)

## Workflow
1. **Develop**: Write properties in Compact.
2. **Test**: Use `midnight-test-runner` for simulation and private state testing.
3. **Deploy**: Use `midnight-deploy` to push to local or testnet.

## Typical Skill Structure
```
skills/midnight-{name}/
├── SKILL.md           # Definition
├── scripts/           # Automation scripts
└── rules/             # detailed docs
```

## Sample: Privacy Pattern (Compact)

A snippet demonstrating a private state transition using the `ledger` keyword.

```compact
import CompactStandardLibrary;

export ledger contract PrivateCounter {
    // Private state variable
    // 'opaque' means the value is hidden on-chain
    private field counter: Uint<64>;

    constructor() {
        // Initialize private state
        counter = 0;
    }

    // Public circuit to increment the counter
    // The actual value of 'counter' remains private
    export circuit increment() {
        counter = counter + 1;
    }
}
```


## 🧠 Skill Set A: Midnight Compact Developer

This skill requires understanding **Zero-Knowledge Circuits (ZK)** and **Private State** management.

### Key Concepts
1.  **witness**: Private inputs known only to the prover (e.g., user's hole cards).
2.  **circuit**: Logic that verifies the private data constraints without revealing the data itself.
3.  **ledger**: The public state, often storing hashes (commitments) of the encrypted private data.
4.  **contract**: The orchestration layer combining circuits and ledger state.

### Tooling
-   **compactc**: The compiler for Compact smart contracts.
-   **zkir**: Zero Knowledge Intermediate Representation.

### 🏗️ Prototype: The "Card Guardian" (Compact)

**Goal**: Prove a player holds a specific card hand strength without revealing the cards.

```javascript
/* 
  Prototype: Card Guardian
  File: card_guardian.compact
*/

export circuit verify_hand_strength(
  private_hand: witness<Vector<Card, 2>>, // Private input: 2 hole cards
  public_commitment: Field              // Public hash on ledger
): void {
  // 1. Verify the hand matches the public commitment hash
  // This proves the user hasn't swapped their cards since the deal
  const calculated_hash = hash(private_hand);
  assert(calculated_hash == public_commitment, "Hand integrity check failed");

  // 2. Output the rank (e.g., Pair, Flush) without revealing exact cards
  // logic to calculate rank...
  // const rank = calculate_poker_rank(private_hand);
  // output(rank);
}
```
