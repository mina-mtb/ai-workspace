# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner (Antigravity, Claude model) has completed onboarding. All governance files read and confirmed.
Two feature branches (`feat/role-boundaries`, `feat/product-owner-setup`) are pending review/merge on GitHub.
Jira/Atlassian MCP is NOT connected in this session — no Jira tools available yet.

## Last action
PO read onboarding doc, all rules (00–11), all state files, all agent definitions, skills INDEX,
git-merge-flow skill, and entry files (AGENTS.md, CLAUDE.md, START-HERE.md). Confirmed understanding.

## Where we are now
Working branch: `chore/po-onboarding-confirm`. On `main`: governance system is solid (11 rules, 10 agents,
skills index, merge flow, handoff signals, branch flow with two human gates). No application code yet.
Pending unmerged branches on origin: `feat/product-owner-setup`, `feat/tool-model-selection`.

## Next step
- Human merges `feat/role-boundaries` and `feat/product-owner-setup` into main (if approved).
- Fix Atlassian MCP connection so PO can access Jira boards AIW and FJ.
- Fill in ROLES.template.md for ai-workspace project (tool→role mapping).
- Design PROJECT-LINKS.md for ai-workspace (AIW) and FindJob (FJ).
- Do NOT start FindJob coding until human says so.

## Blockers / open questions
- Atlassian/Jira MCP is not connected in this Antigravity session. No Jira tools available. Human needs to fix the connection.
- `.ai/integrations/` directory does not exist yet on main.
