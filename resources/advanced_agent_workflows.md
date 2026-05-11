# Advanced Agent Workflows & Hacks

This document outlines 10 advanced "hacks" to maximize agent efficiency, based on methods from Boris Chernny (creator of Claude Code). Use these workflows to handle complex tasks, parallel processing, and error recovery.

## 1. Parallelization with Git Worktrees
**Goal**: Run multiple agent instances simultaneously on different features without conflict.

**Instructions**:
-   **Setup**: instead of switching branches in one folder, create worktrees.
    ```bash
    git worktree add ../feature-name feature-branch
    ```
-   **Execution**: Open a new terminal tab/pane for each worktree (`../feature-name`).
-   **Agent Task**: Assign one agent to each folder to work on isolated features (e.g., Agent A on `frontend`, Agent B on `backend`).
-   **Merge**: Once sub-agents finish, return to the main repo and merge logic.

## 2. Plan Mode (The 1-Minute Investment)
**Goal**: Prevent hours of debugging by planning for 1 minute.

**Trigger**: If a request > 1 file change or involves complex logic.
**Protocol**:
1.  **Stop**: Do not write code immediately.
2.  **Think**: Create a high-level plan (or use `/plan` if available).
3.  **Refine**: Ask the user to review the plan. "Is this approach correct?"
4.  **Execute**: Only proceed after approval.
    *   *Metric*: Planning takes ~1 min but saves ~1 hour of "fixing bad code".

## 3. Self-Correction (Optimize System Prompt)
**Goal**: Prevent repeating the same mistake twice.

**Trigger**: When the agent makes a mistake that matters (e.g., wrong lint command, ignored project rule).
**Instruction**:
-   **Don't just fix the code.**
-   **Fix the Brain**: explicitly update `CLAUDE.md` (or equivalent system prompt file).
-   **Prompt**: "Update `CLAUDE.md` so you never make this mistake again."

## 4. Skills Repository (SOPs)
**Goal**: Standardize complex workflows.

**Concept**: Treat "Skills" as importable packages.
-   Maintain a `skills/` directory or separate repo.
-   **Pull Skill**: When faced with a known task type (e.g., "Deploy to AWS"), read the specific `skills/deploy_aws.md` file first.
-   **Create Skill**: If a workflow works well, save it as a markdown file for future use.

## 5. One-Shot Bug Fix (Error Context)
**Goal**: Fix bugs in a single attempt.

**Protocol**:
-   **Capture**: User must provide the **exact** error code/stack trace.
-   **Context**: Paste the error directly into the tool/terminal.
-   **Instruction**: "Fix this error. Here is the stack trace: [PASTE_ERROR]."
-   **Confidence**: The agent usually has enough info to fix it without "exploratory" edits if the full error is provided.

## 6. "Scrap This" (The Reset Button)
**Goal**: Escape bad local minima (messy/spaghetti code).

**Trigger**: If the code is becoming convoluted, hacky, or breaking many tests.
**Prompt**:
> "Knowing everything you know now, scrap this and implement the more elegant solution."
**Reasoning**: Takes the "learned context" but discards the "bad code," leading to a clean V2 implementation immediately.

## 7. Ghost TTY & Terminal Management
**Goal**: Run many heavy tasks without UI lag.

**Instruction**:
-   Use lightweight terminal environments (like Ghost TTY) to manage multiple split-panes.
-   This allows running 10+ Git Worktrees simultaneously (see Hack #1).

## 8. Sub-Agents (Squad Mode)
**Goal**: Delegation and fresh eyes.

**Trigger**: Verification or distinct sub-tasks.
**Protocol**:
-   **Create**: Generate a `sub_agent_instructions.md` file.
-   **Role**: Define a specific role (e.g., "Code Reviewer", "QA Tester").
-   **Fresh Context**: A new agent session reads ONLY that instruction file and the necessary code. It has no "memory bias" from the implementation phase.
-   **Example**: "Act as a Senior Reviewer. Read `src/main.ts` and critique it against SOLID principles."

## 9. No Manual SQL (Data Analytics)
**Goal**: Zero manual database querying.

**Instruction**:
-   Never write manual SQL queries to "check data" if an agent is available.
-   **Task**: "Analyze the users table and tell me how many signed up last week."
-   The agent formulates the query, runs it (via tool), and reports usage.

## 10. Explanatory & Diagram Mode
**Goal**: Visualization and understanding.

**Trigger**: When changes are structural or complex.
**Instruction**:
-   **Diagram**: "Create an ASCII architecture diagram of the changes."
-   **Explain**: "Explain *why* you chose this pattern over [Alternative]."
-   Use `output_styles` to force the agent to "teach" rather than just "do", ensuring the user maintains mental mastery of the codebase.
