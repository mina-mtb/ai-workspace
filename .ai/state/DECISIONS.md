# DECISIONS - running log (lightweight ADR index)

Append-only. Newest at top. One line per decision; link to a full ADR in docs/adr/ if it's big.

- 2026-06-18 - Use Atlassian's official Rovo MCP endpoint `https://mcp.atlassian.com/v1/mcp/authv2` via `mcp-remote@latest` for Jira/Confluence access; do not use the deprecated `/v1/sse` endpoint.
- 2026-06-17 - Use a two-level agent design: 10 family agents (active) + specialist skills under each
  family (promoted to full agents only when they grow large enough). Reason: specialization without
  unmanageable agent sprawl.
- 2026-06-17 - Control plane = GitHub Issues (chosen for traceability and to support rotating agents).
- 2026-06-17 - State/memory lives in `.ai/state/` so rotating agents share context via the repo.
