# AGENTS.md

Universal entry point for ANY AI agent in this repository (Codex, Claude Code, Cursor, Gemini,
Antigravity, Copilot, Windsurf…). Read this first, every session, before anything else.

> Keep this file short and true. Only what an agent can't infer: commands, hard constraints, where to look.

## 1. On entering — read these, in order
1. `.ai/state/PROJECT.md` — the mission and guardrails (your north star).
2. `.ai/state/CURRENT.md` — where the project stands right now and the next step.
3. The GitHub Issues board — the live task list (control plane).
4. `.ai/rules/00-core.md` — the non-negotiable rules.
5. Your role file in `.ai/agents/`, and the matching skill via `.ai/skills/INDEX.md`.

## 2. Hard constraints (full text in .ai/rules/)
- No secrets in the repo. No direct pushes to `main` (one branch per task, open a PR).
- No direct DB schema edits — migrations only.
- A task is done only when its tests PASS, verified by Test/QA (not the builder). [rules/02]
- Stop after 3 failed attempts or a repeated error; hand off to the human. [rules/03]
- No agent merges its own work; the Product Owner is the final merge gate. [rules/04]
- No destructive actions, and no uncontrolled AI self-learning, without approval.
- Keep commits disciplined, mirror paired systems in the same unit of work, and make priority explicit. [rules/12, rules/13, rules/14]

## 3. On leaving — always
- Update `.ai/state/CURRENT.md` (what you did, where we are, next step, blockers).
- Comment progress + evidence on the GitHub Issue. Append notable decisions to `.ai/state/DECISIONS.md`.

## 4. Commands (FILL IN PER PROJECT)
```
Install: 
Build: 
Test: 
Lint: 
```

## 5. The team
Product Owner · Orchestrator · Architect · Backend · AI Engineer · Database · Frontend · DevOps · Reviewer · Test/QA.
Routing: `.ai/rules/05-agent-routing.md`. Specialists are skills under `.ai/skills/<family>/`.
