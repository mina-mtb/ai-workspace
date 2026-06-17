# Communication Protocol

How agents report and hand off. Work passes as a structured packet, not free-form chat.
Agents also keep the GitHub Issue updated (the control plane) and ../state/CURRENT.md (the live snapshot).

## Result report (end of every task)
```
## Summary        — what you did and why (1-2 sentences)
## Changed files  — path — what changed
## Decisions      — non-obvious choices and why
## Tests          — command run; result PASS/FAIL with key numbers (evidence)
## Risks/follow-ups
## Open questions
## State updated?  — CURRENT.md updated + Issue commented? (yes/no)
```

## Handoff
Same report PLUS: which role you hand to, and exactly what you need from them. See ../handoffs/.

## Escalate to the human when
- An architectural decision is needed (record an ADR).
- The action is irreversible (delete data, drop tables, prod deploy).
- A hard rule would have to be broken.
- Loop safety triggered: 3 failed attempts or repeated identical error (../rules/03-loop-safety.md).
