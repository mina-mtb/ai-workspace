# Core Rules (always on)

Apply to every agent, every task, every project. Non-negotiable.
If a request conflicts with a rule, follow the rule and say so.

1. **No secrets in the repo.** Never commit credentials, tokens, API keys, or `.env` files. Never print them.
2. **One branch per task.** Never commit or push directly to `main`. Open a Pull Request.
3. **No direct database edits.** Schema changes go through migrations only.
4. **Tests gate "done".** See `02-testing-gate.md`. No passing tests = not done.
5. **Loop safety.** See `03-loop-safety.md`. Stop after 3 failed attempts and ask a human.
6. **Merge authority.** See `04-merge-authority.md`. No agent merges its own work.
7. **No destructive actions without human approval.** No dropping tables, deleting data, force-pushing, or wiping environments.
8. **Architecture changes need an ADR.** Don't silently change boundaries, frameworks, or data flow.
9. **Stay in your lane.** Only change what your role (see `../agents/`) allows.
10. **Report in the standard format** (`../communication-protocol.md`) and update state (`../state/`) at the end of every task.
11. **Stay on mission.** Before acting, confirm the task serves the project's stated goal in `../state/PROJECT.md`. If it drifts, stop and flag the Product Owner.
12. **Commit discipline.** See `12-commit-discipline.md`. Checkpoint state, keep commits focused, push meaningful work, and never commit temp artifacts.
13. **Mirroring / dual-write.** See `13-mirroring.md`. When one side of a mirrored pair changes, update the paired side and report `both sides updated? yes/no`.
14. **Prioritization is explicit.** See `14-prioritization.md`. Foundation/blocking and safety work come first; Epic organization is separate from execution order.
