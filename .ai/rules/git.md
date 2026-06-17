# Git & Branching

- Branch naming: `feat/*`, `fix/*`, `hotfix/*`, `experiment/*`. One branch per task.
- Branch levels: `feature/* → develop/staging → main`. Move up only via PR + Product Owner approval.
- Small, focused commits; imperative messages.
- Never force-push shared branches. Never rewrite history on `main`.
- Every PR states: goal, changed files, tests run + result, risks.
- On merge conflict: resolve carefully by hand, then re-run the full relevant pipeline.
