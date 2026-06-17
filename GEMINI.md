# GEMINI.md — Antigravity rules (always-on)

Antigravity reads this file at the start of every session and it has the highest priority.
Treat everything below as always-on and non-negotiable.

## Step 0 — before any action
The single source of truth for all rules is the `.ai/` folder. Read and obey:
- @.ai/rules/00-core.md
- @.ai/rules/database-migrations.md
- @.ai/rules/git.md
- @.ai/rules/testing.md
- @.ai/rules/security.md
- @.ai/communication-protocol.md
Also follow the shared `AGENTS.md` in this directory.
If you cannot resolve a reference, OPEN and read the file at that path before proceeding.

## Hard prohibitions (summary; the full text in .ai/rules/ wins if more detailed)
- NEVER change the database schema directly. Schema changes go through migrations only.
- NEVER commit or push directly to `main`/`master`. One branch per task; open a PR.
- NEVER commit secrets, credentials, tokens, or `.env` files. Never print them.
- NEVER do destructive actions (drop tables, delete data, force-push, wipe environments)
  without explicit human approval in the same conversation.
- A task is NOT done until the relevant tests are written and passing.

## On conflict
If a user request conflicts with any rule above, follow the rule and say so clearly.
Do not silently break a rule to satisfy a request.
