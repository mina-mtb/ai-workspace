# Rule: Merge Authority (the Product Owner is the final gate)

No agent merges its own work. Integration to a higher branch is a separate, external decision.

## The approval chain (a branch cannot move up a level until each step passes)
1. **Builder** (Backend / AI / Database / Frontend / DevOps) finishes work on its own branch and opens a PR.
2. **Test/QA** runs the tests and posts pass/fail evidence.
3. **Reviewer** checks code quality, architecture boundaries, and security.
4. **Product Owner** confirms the change serves the project goal and does not drift from mission,
   then — and only then — authorizes the merge to the higher branch.

## Hard constraints
- A builder agent is PROHIBITED from merging its own PR.
- Merge to `main` (or any protected/higher branch) requires Product Owner authorization recorded in the PR.
- If Test/QA fails or Reviewer flags a blocking issue, the PR goes back to the builder. No override.
- The Product Owner may BLOCK a merge purely on mission-drift grounds even if tests pass.
