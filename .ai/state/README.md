# State — the shared memory across rotating agents

You switch between Codex, Antigravity, Gemini, Claude. They share NO memory with each other.
The ONLY shared memory is this repository. These files are how any agent, on entering, learns
where the project stands — without you re-explaining anything.

## The three files

- `PROJECT.md` — the mission and the guardrails. Rarely changes. The "north star".
- `CURRENT.md` — the live snapshot: what was just done, where we are now, the next step. Updated every task.
- `DECISIONS.md` — the running log of important decisions (lightweight ADR index). Append-only.

## The protocol (every agent follows this)

**On ENTERING a session (before any work):**
1. Read `PROJECT.md` (mission + guardrails).
2. Read `CURRENT.md` (where we are, what's next).
3. Read the GitHub Issues board (the task list / control plane).
4. Read the rules in `../rules/` and your role in `../agents/`.

**On LEAVING a session (after work, even if interrupted):**
1. Update `CURRENT.md`: what you did, current state, the exact next step, any blocker.
2. Comment the same on the relevant GitHub Issue (with evidence: test output, links).
3. If you made an important decision, append it to `DECISIONS.md`.

This is what lets you say "continue" to a fresh agent and have it pick up exactly where the last one stopped.
