# Core rule bridge (Always On)

This rule connects Antigravity's native rule system to the shared knowledge base in `.ai/`.
Before any task, read and obey the single source of truth in `.ai/`:
@.ai/rules/00-core.md
@.ai/rules/database-migrations.md
@.ai/rules/git.md
@.ai/rules/testing.md
@.ai/rules/security.md
@.ai/communication-protocol.md

## Hard prohibitions (never violate)
- No direct database schema changes — migrations only.
- No direct commits/pushes to main — one branch per task, open a PR.
- No secrets in the repo.
- No destructive actions without explicit human approval.
- Not done until relevant tests pass.
If a request conflicts with these, follow the rule and say so.
