# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
PROJECT-LINKS is merged to `main` and available at `.ai/integrations/PROJECT-LINKS.md`.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
WSAI Confluence is fully done (2026-06-24). After Pass 2 filled all 16 EN/FA page-pairs,
polished the two Home pages into language-specific portals using native Atlassian MCP only,
sequential calls, and `cloudId="minatahmasebib.atlassian.net"`. Kept each existing Home
cross-link and intro, then appended a Contents section with direct links to all 15 topic
pages in the same language. Readback verified the EN Home contains the Contents list and
the first link resolves to `01 - Vision & Goals (EN)` page `2359297`.

Updated page IDs:
- 00 EN Home `2162690` now links to all EN topic pages 01-15.
- 00 FA Home `2293780` now links to all FA topic pages 01-15.

Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`. Site: `minatahmasebib.atlassian.net`.

## Where we are now
Working branch: `main`, synced with `origin/main` before Pass 2 batch 1.
Atlassian: Confluence spaces accessible include Personal, PROGRAMVAR, SD, SD1, and WSAI.
Jira projects AIW, FJ, and SCRUM accessible from Codex via MCP.
WorkspaceAI Confluence skeleton exists; Pass 2 is complete; all 16 EN/FA page-pairs are
filled with repo-mirrored content; both Home pages now act as portal pages.
`scratch/` is ignored and should not appear as an untracked commit candidate.

## Next step
- WSAI Confluence is done: content pages are filled and Home pages link to all topics.
- Build the AIW Jira backlog.
- Set up branch structure when ready: develop / integration / staging.
- Triage old remote branches: `feat/product-owner-setup`, `feat/tool-model-selection`.
- Do NOT start FindJob coding until human says so.

## Blockers / open questions
- Direct REST API Basic-auth retest needs the actual Atlassian email/API-token pair or
  precomputed Basic header in the current session. MCP server auth works through OAuth.
- FindJob Confluence space remains TBD and must be separate from WSAI.
- Old remote branches still need later triage: `feat/product-owner-setup`,
  `feat/tool-model-selection`.
