# .ai — Shared Agent Knowledge Base (v2)

The reusable brain + memory for all AI agents, across all projects, read by every tool via root AGENTS.md.

## Folders
- `rules/` — mandatory constraints (incl. testing gate, loop safety, merge authority, routing, LLMOps).
- `agents/` — the 10 family roles (Product Owner, Orchestrator, Architect, Backend, AI Engineer, Database, Frontend, DevOps, Reviewer, Test/QA).
- `skills/` — specialist how-to files grouped by department; read `skills/INDEX.md` first.
- `workflows/` — step-by-step processes.
- `handoffs/` — the standard packet passed between agents.
- `state/` — shared memory across rotating agents (PROJECT.md, CURRENT.md, DECISIONS.md). **This is what lets a fresh agent continue where another stopped.**
- `communication-protocol.md` — how agents report and escalate.

## The model in one picture
```
Human sets mission ─► Product Owner (guards mission, final merge gate)
                         │
                    Orchestrator (routes work via rules/05-agent-routing.md)
                         │
   Architect · Backend · AI Engineer · Database · Frontend · DevOps  (builders, each loads its skills/)
                         │
                    Test/QA (independent pass/fail)  ─►  Reviewer (quality/security)  ─►  Product Owner (merge)
```
Memory lives in `state/` + GitHub Issues. Knowledge lives in `rules/` + `skills/`.

## Keep it lean
Human-curated, minimal, true. When an agent repeats a mistake, add the rule/skill that prevents it.
When a skill grows large and is used constantly, promote it to its own agent.
