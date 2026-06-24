# Rule: Prioritization

Execution order is a decision, not an accident. Epics organize work by theme; priority and rank decide
what happens next.

## Priority order
1. **Foundation or blocking work first.** If other work depends on it, it moves up.
2. **Safety rules from real incidents next.** A repeated or high-risk failure becomes priority work when
   it can prevent future damage.
3. **High-value / low-effort work next.** Small improvements with broad leverage should not wait behind
   large speculative work.
4. **Everything else follows.** Nice-to-have, future automation, and exploratory work stays lower until
   it becomes blocking or time-sensitive.

## Rules
1. **Use Jira Priority and backlog rank to express execution order.** Priority communicates importance;
   rank communicates sequence when the board supports it.
2. **Human has final priority in `human-approval` mode.** The architect proposes; the human/Product
   Owner sets the final priority.
3. **Epic is not execution order.** A Story's parent Epic is for organization. A Story under a later Epic
   may run before one under an earlier Epic if it is foundational, safety-critical, or blocking.
4. **Record priority exceptions.** If work is pulled forward or pushed back for a reason that is not
   obvious, note it in Jira/GitHub and, when durable, in `.ai/state/DECISIONS.md`.
5. **Known limitation:** if MCP cannot set exact backlog rank, set Jira Priority, create or update the
   work in the intended order where possible, and tell the human when manual board ordering is needed.

## Done means
The report states the intended next work, its priority rationale, and whether manual board ranking is
needed.
