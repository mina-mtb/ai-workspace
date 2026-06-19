# Rule: Continuous Improvement (every error becomes a permanent lesson)

When building an application project (e.g. FindJob), we do NOT just fix an error locally and move on.
We ask: "could this class of problem hit us again, in this or another project?" If yes, we also improve
the SHARED system (`ai-workspace/.ai/`) so the whole family of projects never hits it again.

This is what makes the workspace get smarter over time. The two repos evolve in parallel:
the application repo gets the fix; the ai-workspace repo gets the lesson.

## When an error / friction / repeated mistake happens
1. Fix the immediate problem in the application project (its own repo, its own branch).
2. Ask: is this a one-off, or a pattern that could recur?
3. If it's a pattern, capture the lesson in `ai-workspace/.ai/` as the right artifact:
   - a new or updated **rule** (`.ai/rules/`) if it's a "must always / must never",
   - a new or updated **skill** (`.ai/skills/...`) if it's a "how to do X correctly",
   - a note in **DECISIONS.md** if it's a decision/rationale worth remembering.
4. That ai-workspace change follows normal governance: its own branch in the ai-workspace repo,
   reviewed, merged to ai-workspace main. It does NOT go into the application repo.

## How to decide rule vs skill vs decision
- Rule: a hard constraint that must be enforced ("never commit secrets", "migrations only").
- Skill: a repeatable technique ("how to wire pgvector", "how to write an integration test for X").
- Decision (DECISIONS.md): a choice and its reason ("chose Kanban over Scrum because ...").

## Important
- Keep lessons SMALL and human-readable. One clear rule/skill per lesson, not a wall of text.
- Don't over-engineer: only promote a fix to a shared lesson when it's genuinely a recurring pattern.
- The human is told (via a HANDOFF line) whenever a shared-system improvement is proposed, because it
  affects every project and may need the architect's input.
