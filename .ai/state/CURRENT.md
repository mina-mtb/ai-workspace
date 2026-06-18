# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Setting up the agent system. Atlassian Rovo MCP was added to the local Codex config and needs a Codex restart plus OAuth sign-in before tools are available.

## Last action
Added `mcp_servers.atlassian_rovo` to `C:\Users\mina_\.codex\config.toml` using `mcp-remote@latest` and Atlassian's current `/v1/mcp/authv2` endpoint. No tokens were stored in the repo or config.

## Where we are now
Working branch: `chore/atlassian-mcp-config-note`. GitHub MCP is available in the current Codex session. Atlassian MCP is configured locally but not loaded into this active session yet.

## Next step
- Restart Codex so the new Atlassian MCP server is loaded.
- Complete the Atlassian OAuth flow in the browser when prompted.
- After restart, verify Jira/Confluence tools appear and can search permitted Atlassian Cloud content.
- Decide the first concrete project (planned: FindJob phase 1: CV matching + CV generation).

## Blockers / open questions
- The Atlassian connector/plugin was not available as an installed Codex app in this session, so the setup uses the official remote MCP endpoint through `mcp-remote`.
- A relevant `ai-workspace` GitHub Issue was not visible in the recent GitHub connector results, so no issue comment was added.
