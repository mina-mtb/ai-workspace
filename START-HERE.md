# START HERE (v2)

This is the upgraded reusable agent system: 10 family agents, specialist skills, hard governance
rules (testing gate, loop safety, merge authority), and a shared state/memory system for rotating agents.

## Why the state/ folder matters most for you
You rotate between Codex, Antigravity, Gemini, Claude — they share no memory. The repo is the only
shared memory. `.ai/state/CURRENT.md` lets any fresh agent read "where we are + next step" and continue
without you re-explaining. Every agent updates it on leaving.

## How tools connect
- Codex / Cursor / Copilot / Windsurf / Gemini CLI → read `AGENTS.md` automatically.
- Claude Code → `CLAUDE.md`. Antigravity → `GEMINI.md` (+ `.agents/rules/` set to Always On).
- Web chat (ChatGPT/Gemini/Claude) → paste `.ai/rules/00-core.md` + `.ai/state/PROJECT.md` into a Project/Gem once.

## The growth habit
When an agent repeats a mistake, add the rule/skill that would have prevented it.
When a skill gets big and is used constantly, promote it to its own agent.
