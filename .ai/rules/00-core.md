# Core Rules (always on)

These apply to every agent, every task, every project. Non-negotiable.
If a request conflicts with a rule, follow the rule and explain why.

1. **No secrets in the repo.** Never commit credentials, tokens, API keys, or `.env` files.
   Never print secrets in output or logs.
2. **One branch per task.** Never commit or push directly to `main`/`master`.
3. **No direct database edits.** Schema changes go through migrations only. (See `database-migrations.md`.)
4. **Tests gate "done".** Write/keep tests passing for what you changed. No passing tests = not done.
5. **No destructive actions without human approval.** No dropping tables, deleting data,
   force-pushing, or wiping environments unless a human approves it in the same conversation.
6. **Architecture changes need an ADR.** Don't silently change boundaries, frameworks, or
   data flow. Record the decision (Architecture Decision Record).
7. **Stay in your lane.** Only change what your role (see `../agents/`) is allowed to change.
8. **Report in the standard format.** End every task with the result report from
   `../communication-protocol.md`.
9. **When unsure, stop and ask.** Don't guess on irreversible or high-impact actions.
