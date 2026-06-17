# Workflow: Add a Feature

1. Read the project brief + architecture notes.
2. Confirm with Architect whether the feature fits existing modules (new module → ADR).
3. Orchestrator makes a task plan: which agents, in what order.
4. Each agent implements ONLY its part, on its own branch.
5. Each agent writes tests for its part.
6. Run the full test suite locally.
7. Hand off to Reviewer: architecture, tests, security, docs, (LLMOps if AI is involved).
8. If it passes, open a PR with the standard summary.
9. After merge, if something reusable emerged, add a rule/skill to `.ai/`.
