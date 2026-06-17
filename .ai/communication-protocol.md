# Communication Protocol

How agents report work and hand it to the next agent. Every agent uses this format.
Agents do not pass work through long free-form chat — they pass a structured packet.

## Result report (every agent, end of every task)

```
## Summary
<one or two sentences: what you did and why>

## Changed files
- path/to/file — what changed

## Decisions
- <any non-obvious choice you made, and why>

## Tests
- command run:
- result: PASS / FAIL (with key numbers)

## Risks & follow-ups
- <anything the next person should watch out for, or work left undone>

## Open questions
- <anything you were not sure about and decided / need a human to decide>
```

## Handoff (when passing to another agent)

Use the same report PLUS state clearly:
- **To which role** you are handing off (e.g. "→ Reviewer Agent").
- **What you need from them** (e.g. "verify migration safety + security review").

See `handoffs/_TEMPLATE.md` for the full handoff packet.

## Escalate to a human when

- The task needs an architectural decision (record an ADR).
- The action is irreversible (deleting data, dropping tables, production deploy).
- A hard rule in `rules/` would have to be broken to proceed.
- You have looped 3 times on the same failure without progress. Stop and ask.
