# Solidity Learning Resources
Derived from [Ethereum Wingman](https://github.com/austintgriffith/ethereum-wingman)

## 🚨 The Most Important Concept
**NOTHING IS AUTOMATIC ON ETHEREUM.**
Smart contracts cannot execute themselves. For any function that "needs to happen":
1. Make it callable by **ANYONE** (not just admin)
2. Give callers a **REASON** (profit, reward, their own interest)
3. Make the incentive **SUFFICIENT** to cover gas + profit

## Critical Gotchas
1. **Token Decimals Vary**: USDC = 6, WBTC = 8, most = 18
2. **Approve Pattern Required**: Contracts need approval before `transferFrom`
3. **Reentrancy Attacks**: Always use Checks-Effects-Interactions pattern + `ReentrancyGuard`
4. **Oracle Manipulation**: Never use DEX spot prices directly
5. **No Floating Point**: Use basis points (e.g., 500/10000 = 5%)
6. **Vault Inflation Attack**: Protect first depositors

## Usage Modes
When acting as an Ethereum Wingman, adopt these personas:

### Teaching Mode
- Explain concepts like "How does the ERC-20 approve pattern work?"
- Clarify "Constant product formula in AMMs"

### Code Review Mode
- Look for vulnerabilities: "Review this withdrawal function for reentrancy"
- Check for common pitfalls: "Audit this oracle integration"

### Build Mode
- Assist in constructing: "Help me build a token with buy/sell functionality"
- Scaffolding: "Set up a staking contract with rewards"

## SpeedRun Ethereum Challenges references
- **Simple NFT**: ERC-721, minting, metadata
- **Decentralized Staking**: Coordination, deadlines, escrow
- **Token Vendor**: ERC-20 approve pattern
- **DEX**: AMM, constant product formula

## SOLID Code Sample: Simple Staking

This contract demonstrates **Single Responsibility**, **Open/Closed** (via virtual functions), and **Security** (ReentrancyGuard).

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title StakingContract
/// @notice Handles staking logic securely and simply
contract StakingContract is ReentrancyGuard, Ownable {
    IERC20 public immutable stakingToken;
    mapping(address => uint256) public balances;
    
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    constructor(address _token) Ownable(msg.sender) {
        require(_token != address(0), "Invalid token");
        stakingToken = IERC20(_token);
    }

    /// @notice Stakes tokens into the contract
    /// @param amount Amount to stake
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        
        // Checks-Effects-Interactions pattern handled by ReentrancyGuard + Logic order
        balances[msg.sender] += amount;
        
        // Interaction
        bool success = stakingToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer failed"); // Always check return values
        
        emit Staked(msg.sender, amount);
    }

    /// @notice Withdraws staked tokens
    /// @param amount Amount to withdraw
    function withdraw(uint256 amount) external nonReentrant {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        balances[msg.sender] -= amount;
        
        bool success = stakingToken.transfer(msg.sender, amount);
        require(success, "Transfer failed");
        
        emit Withdrawn(msg.sender, amount);
    }
}
```

