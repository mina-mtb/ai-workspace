# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
PROJECT-LINKS is merged to `main` and available at `.ai/integrations/PROJECT-LINKS.md`.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
Pass 2 COMPLETE - all 16 WSAI page-pairs are filled (2026-06-24).
Completed Confluence Pass 2 batch 4 using native Atlassian MCP only, sequential calls,
and `cloudId="minatahmasebib.atlassian.net"`. Filled WSAI pages 13, 14, and 15 in both
EN and FA from the real repo files/system documentation. Each page has a top cross-link
to its language twin and the standard repo-wins mirror note. Readback verified page
`2162731` (`15 - Glossary & Decision Log EN`) includes the Persian cross-link, glossary,
and decision log mirrored from `.ai/state/DECISIONS.md`.

Updated page IDs:
- 13 EN `2457621`, 13 FA `2195651`
- 14 EN `2523157`, 14 FA `2588693`
- 15 EN `2162731`, 15 FA `2424953`

Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`. Site: `minatahmasebib.atlassian.net`.

## Where we are now
Working branch: `main`, synced with `origin/main` before Pass 2 batch 1.
Atlassian: Confluence spaces accessible include Personal, PROGRAMVAR, SD, SD1, and WSAI.
Jira projects AIW, FJ, and SCRUM accessible from Codex via MCP.
WorkspaceAI Confluence skeleton exists; Pass 2 is complete and all 16 EN/FA page-pairs
are filled with repo-mirrored content.
`scratch/` is ignored and should not appear as an untracked commit candidate.

## Next step
- WSAI Confluence content pass is done. Optional polish: update `00 - Home / Overview`
  so it links directly to all 15 topic pages.
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
