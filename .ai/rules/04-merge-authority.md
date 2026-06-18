# Rule: Merge Authority (the Product Owner is the final gate)

No agent merges its own work. Integration to a higher branch is a separate, external decision.

## The approval chain (a branch cannot move up a level until each step passes)
1. **Builder** (Backend / AI / Database / Frontend / DevOps) finishes on its own branch, opens a PR.
2. **Test/QA** runs the tests and posts pass/fail evidence.
3. **Reviewer** checks code quality, architecture boundaries, and security.
4. **Product Owner** confirms the change serves the project goal and does not drift from mission,
   then authorizes the merge.

## What "no agent merges its own work" actually means
The rule exists to prevent **self-approval** — an agent verifying and merging its OWN output with no
independent check. It does NOT forbid an agent from *executing* a merge that an independent authority
has already approved.

Therefore the test for whether a merge may be executed is:
- **The one executing the merge must NOT be the one who built the branch, AND**
- **An independent approval exists** (from the Product Owner — which, in the current phase, is the human).

If both are true, executing the git merge is allowed (see ../skills/git/git-merge-flow.md).
If the same agent built the branch and would also approve/merge it → that is self-approval → FORBIDDEN.

## Merge mode (controls who gives the final go-ahead)
The active mode is set in ../state/PROJECT.md as `MERGE_MODE`:
- `human-approval` (default, current phase): the human plays Product Owner. Nothing merges until the
  human explicitly says "approved". An agent may then execute the merge, as long as it did not build the branch.
- `product-owner-auto` (later phase): a trusted Product Owner agent gives the go-ahead itself, without
  asking the human each time. The human only observes. Switch to this only when trust is established.

To change phase, the human edits the single `MERGE_MODE` line in PROJECT.md.

## Hard constraints
- A builder agent is PROHIBITED from approving or merging its own PR.
- Merge to `main`/protected branches requires Product Owner authorization recorded in the PR.
- If Test/QA fails or Reviewer flags a blocking issue, the PR goes back to the builder. No override.
- The Product Owner may BLOCK a merge on mission-drift grounds even if tests pass.
