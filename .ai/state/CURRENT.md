# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
PROJECT-LINKS is merged to `main` and available at `.ai/integrations/PROJECT-LINKS.md`.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
Created the first AIW Stories under Epic `AIW-2` (Git & Branch Infrastructure) on 2026-06-25.
Each Story has a bilingual EN/FA description, is parent-linked to `AIW-2`, and is mirrored
to a GitHub Issue with label `story`. Each GitHub Issue body links to the Jira Story and
parent Epic; each Jira Story has a comment linking back to the GitHub Issue. Readback
verified parent=`AIW-2`, bilingual descriptions, and Jira-side GitHub mirror comments.

Created Story mirrors:
- `AIW-7` / GitHub #8 - Create branch structure (develop / integration / staging).
- `AIW-8` / GitHub #9 - Triage stale remote branches.
- `AIW-9` / GitHub #10 - Set up branch protection on main.

Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`. Site: `minatahmasebib.atlassian.net`.

## Where we are now
Working branch: `main`, synced with `origin/main` before Pass 2 batch 1.
Atlassian: Confluence spaces accessible include Personal, PROGRAMVAR, SD, SD1, and WSAI.
Jira projects AIW, FJ, and SCRUM accessible from Codex via MCP.
WorkspaceAI Confluence skeleton exists; Pass 2 is complete; all 16 EN/FA page-pairs are
filled with repo-mirrored content; both Home pages now act as portal pages.
AIW Jira backlog now has 6 top-level Epics mirrored to GitHub Issues, plus the 3 high-level
Stories under Epic `AIW-2` mirrored to GitHub Issues.
`scratch/` is ignored and should not appear as an untracked commit candidate.

## Next step
- WSAI Confluence is done: content pages are filled and Home pages link to all topics.
- Continue adding high-level Stories, next = Epic `AIW-3` (Integration & Connection Knowledge),
  mirrored Jira<->GitHub in the same bilingual pattern.
- Set up branch structure when ready: develop / integration / staging.
- Triage old remote branches: `feat/product-owner-setup`, `feat/tool-model-selection`.
- Do NOT start FindJob coding until human says so.

## Blockers / open questions
- Direct REST API Basic-auth retest needs the actual Atlassian email/API-token pair or
  precomputed Basic header in the current session. MCP server auth works through OAuth.
- FindJob Confluence space remains TBD and must be separate from WSAI.
- Old remote branches still need later triage: `feat/product-owner-setup`,
  `feat/tool-model-selection`.
