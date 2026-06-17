# GEMINI.md — Antigravity rules (always-on)

Antigravity reads this at the start of every session (highest priority). Treat as always-on, non-negotiable.

## Step 0 — before any action
Single source of truth = the `.ai/` folder. Read and obey:
- @.ai/state/PROJECT.md
- @.ai/state/CURRENT.md
- @.ai/rules/00-core.md
- @.ai/rules/02-testing-gate.md
- @.ai/rules/03-loop-safety.md
- @.ai/rules/04-merge-authority.md
Also read the GitHub Issues board and follow `AGENTS.md`.
If a reference can't be resolved, OPEN and read the file at that path before proceeding.

## Hard prohibitions (full text in .ai/rules/ wins if more detailed)
- NEVER change the database schema directly — migrations only.
- NEVER commit/push directly to `main` — one branch per task; open a PR.
- NEVER commit secrets or `.env` files.
- A task is NOT done until Test/QA confirms passing tests (the builder cannot self-verify).
- Stop after 3 failed attempts / repeated error; hand off to the human.
- NEVER merge your own work — only the Product Owner authorizes merges.
- NEVER let raw user feedback change AI behaviour directly.

## On conflict
Follow the rule and say so. Do not silently break a rule to satisfy a request.

## On leaving
Update @.ai/state/CURRENT.md and comment progress + evidence on the GitHub Issue.
