# Core rule bridge (set activation to: Always On)

Connects Antigravity's native rules to the shared knowledge base in `.ai/`.
Before any task, read and obey the single source of truth:
@.ai/state/PROJECT.md
@.ai/state/CURRENT.md
@.ai/rules/00-core.md
@.ai/rules/02-testing-gate.md
@.ai/rules/03-loop-safety.md
@.ai/rules/04-merge-authority.md

## Never violate
- DB schema changes via migrations only.
- No direct commits/pushes to main — one branch per task, open a PR.
- No secrets in the repo.
- Not done until Test/QA confirms passing tests; the builder cannot self-verify.
- Stop after 3 failed attempts; hand off to the human.
- No agent merges its own work — Product Owner is the final gate.
If a request conflicts with these, follow the rule and say so.
