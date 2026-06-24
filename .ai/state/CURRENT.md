# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
All governance files read and confirmed.
Two feature branches (`feat/role-boundaries`, `feat/product-owner-setup`) are pending review/merge on GitHub.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
Created repo branch `feat/project-links` for the PROJECT-LINKS registry task (2026-06-24).
Added `.ai/integrations/PROJECT-LINKS.md`, the canonical registry separating WorkspaceAI
from FindJob and recording verified tool connections. This is a repo-file task only; no
Atlassian/Jira/Confluence write was performed during this step.

Previous Atlassian milestone: Pass 1 completed for WSAI. Manual `WSAI` space exists
(space ID `2195461`, homepage ID `2195585`), and 32 WorkspaceAI Confluence skeleton pages
were created under homepage `2195585` using native Codex Atlassian MCP.
Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`. Site: `minatahmasebib.atlassian.net`.

## Where we are now
Working branch: `feat/project-links`. On `main`: governance system is solid (11 rules, 10 agents,
skills index, merge flow, handoff signals, branch flow with two human gates). No application code yet.
Pending unmerged branches on origin: `feat/product-owner-setup`, `feat/tool-model-selection`.
Atlassian: Confluence spaces accessible include Personal, PROGRAMVAR, SD, SD1, and WSAI.
Jira projects AIW, FJ, and SCRUM accessible from Codex via MCP.

## Next step
- Human reviews/approves the `feat/project-links` PR; do not merge without human approval.
- After PROJECT-LINKS is accepted, continue Confluence Pass 2: fill bodies + EN<->FA cross-links
  using the real WSAI page IDs from Pass 1.
- Fill in ROLES.template.md for ai-workspace project (tool->role mapping).
- Create first Jira issues in AIW board for initial sprint planning.
- Do NOT start FindJob coding until human says so.

## Blockers / open questions
- Direct REST API Basic-auth retest needs the actual Atlassian email/API-token pair or
  precomputed Basic header in the current session. MCP server auth works through OAuth.
- FindJob Confluence space remains TBD and must be separate from WSAI.
