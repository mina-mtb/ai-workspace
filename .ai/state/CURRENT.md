# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
PROJECT-LINKS is merged to `main` and available at `.ai/integrations/PROJECT-LINKS.md`.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
Completed Confluence Pass 2 batch 2 (2026-06-24) using native Atlassian MCP only,
sequential calls, and `cloudId="minatahmasebib.atlassian.net"`. Filled WSAI pages
04, 06, 07, and 08 in both EN and FA from the real repo files, each with a top
cross-link to its language twin and the standard repo-wins mirror note. Readback
verified page `2424873` (`04 - Agents EN`) includes the Persian cross-link and all
10 agent roles from `.ai/agents/`.

Updated page IDs:
- 04 EN `2424873`, 04 FA `2424893`
- 06 EN `2457601`, 06 FA `2195631`
- 07 EN `2424933`, 07 FA `2490369`
- 08 EN `2523137`, 08 FA `2555905`

Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`. Site: `minatahmasebib.atlassian.net`.

## Where we are now
Working branch: `main`, synced with `origin/main` before Pass 2 batch 1.
Atlassian: Confluence spaces accessible include Personal, PROGRAMVAR, SD, SD1, and WSAI.
Jira projects AIW, FJ, and SCRUM accessible from Codex via MCP.
WorkspaceAI Confluence skeleton exists; Pass 2 batches 1 and 2 are filled.

## Next step
- Human checks page `04 - Agents (EN)` in browser and confirms all 10 agents match `.ai/agents/`.
- Continue Confluence Pass 2 next: batch 3 = pages 09, 10, 11, and 12 in EN+FA.
- Add `scratch/` to `.gitignore` in a separate repo-file task so temporary audit artifacts
  do not keep appearing in Source Control.
- Do NOT start FindJob coding until human says so.

## Blockers / open questions
- Direct REST API Basic-auth retest needs the actual Atlassian email/API-token pair or
  precomputed Basic header in the current session. MCP server auth works through OAuth.
- FindJob Confluence space remains TBD and must be separate from WSAI.
- Old remote branches still need later triage: `feat/product-owner-setup`,
  `feat/tool-model-selection`.
