# AGENTS.md

Universal instructions for ANY AI agent working in this repository
(Codex, Claude Code, Cursor, Gemini, Antigravity, Copilot, Windsurf, etc.).

This file is the single entry point. Read it first, every session, before any other action.

> Keep this file short and true. Only put here what an agent could NOT figure out on its own:
> exact commands, hard constraints, and non-standard patterns. Delete anything that is not true
> for this project. A long or inaccurate file makes agents worse, not better.

---

## 1. Read before you act

The shared knowledge base lives in `.ai/`. At the start of a task, read:

1. `.ai/rules/00-core.md` — the non-negotiable rules. Always apply them.
2. `.ai/communication-protocol.md` — how you report results and hand work to another agent.
3. The role file in `.ai/agents/` that matches what you are doing (e.g. `backend.md`, `reviewer.md`).
4. Any file in `.ai/skills/` whose description matches the current task.

If a rule in `.ai/rules/` conflicts with a user request, follow the rule and say so.

---

## 2. Hard constraints (full text in `.ai/rules/`)

- **Secrets:** never commit secrets, credentials, tokens, or `.env` files. Never print them.
- **Branches:** never commit or push directly to `main`. One branch per task.
- **Database:** never modify the database schema directly. Schema changes go through migrations only.
- **Tests:** a task is not done until the relevant tests pass. "It looks right" is not done.
- **Architecture:** do not change an architectural decision without recording an ADR.
- **Destructive actions:** never delete data, drop tables, force-push, or wipe environments
  without explicit human approval in the same conversation.

---

## 3. Commands (FILL THIS IN PER PROJECT)

Agents reference these constantly. Replace the placeholders with the real commands.

```
Install:   <e.g. dotnet restore  |  npm install  |  pip install -r requirements.txt>
Build:     <e.g. dotnet build    |  npm run build>
Test:      <e.g. dotnet test     |  npm test>
Lint:      <e.g. dotnet format    |  npm run lint>
Run (dev): <e.g. dotnet run       |  npm run dev>
```

---

## 4. Definition of done

A task is complete only when ALL of these are true:

- Code compiles / builds.
- Relevant tests are written and passing.
- No secrets or debug junk left behind.
- A short summary exists: what changed, why, which files, which tests, and any risks.
  (Use the format in `.ai/communication-protocol.md`.)

---

## 5. Project-specific overrides

Anything specific to THIS project (not the shared library) goes in `.project-ai/`
or below this section. Project-specific rules override the shared `.ai/` rules.
