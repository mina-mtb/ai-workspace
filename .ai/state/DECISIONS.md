# DECISIONS - running log (lightweight ADR index)

Append-only. Newest at top. One line per decision; link to a full ADR in docs/adr/ if it's big.

- 2026-06-25 - The three core governance rules for commit discipline, mirroring/dual-write, and prioritization are now active as rules 12, 13, and 14; future agents must checkpoint state, keep mirrored systems aligned, and separate Epic organization from execution order.
- 2026-06-24 - Every project gets an "Idea Inbox" (a Confluence page) for capturing raw ideas/hypotheses/dreams freely, separate from the real backlog. Ideas are periodically reviewed: promote to a real Story, keep reviewing, or archive. Raw ideas must NOT clutter the real Jira backlog until promoted.
- 2026-06-24 - AIW (ai-workspace) is a permanent, never-closed board: setup Epics get completed, but an always-open "Continuous Improvement" Epic keeps receiving new Stories whenever rule 11 fires in any project. AIW is a living project, not a finite one.
- 2026-06-18 - Use Atlassian's official Rovo MCP endpoint `https://mcp.atlassian.com/v1/mcp/authv2` via `mcp-remote@latest` for Jira/Confluence access; do not use the deprecated `/v1/sse` endpoint.
- 2026-06-17 - Use a two-level agent design: 10 family agents (active) + specialist skills under each
  family (promoted to full agents only when they grow large enough). Reason: specialization without
  unmanageable agent sprawl.
- 2026-06-17 - Control plane = GitHub Issues (chosen for traceability and to support rotating agents).
- 2026-06-17 - State/memory lives in `.ai/state/` so rotating agents share context via the repo.
