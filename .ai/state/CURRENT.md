# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
PROJECT-LINKS is merged to `main` and available at `.ai/integrations/PROJECT-LINKS.md`.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
Created high-level AIW Stories under Epic `AIW-3` (Integration & Connection Knowledge)
on 2026-06-25. First verified one AIW-2 Story (`AIW-7`) still had the expected pattern:
bilingual EN/FA description, parent=`AIW-2`, and Jira-side GitHub mirror comment. Then
created 3 Stories under `AIW-3`; each has a bilingual EN/FA description, is parent-linked
to `AIW-3`, and is mirrored to a GitHub Issue with label `story`. Each GitHub Issue body
links to the Jira Story and parent Epic; each Jira Story has a comment linking back to
the GitHub Issue. Readback verified parent=`AIW-3`, bilingual descriptions, and Jira-side
GitHub mirror comments.

Created Story mirrors:
- `AIW-10` / GitHub #11 - Write Atlassian MCP integration doc.
- `AIW-11` / GitHub #12 - Capture Atlassian technical lessons as a skill.
- `AIW-12` / GitHub #13 - Fill ROLES mapping for ai-workspace.

Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`. Site: `minatahmasebib.atlassian.net`.

## Where we are now
Working branch: `main`, synced with `origin/main` before Pass 2 batch 1.
Atlassian: Confluence spaces accessible include Personal, PROGRAMVAR, SD, SD1, and WSAI.
Jira projects AIW, FJ, and SCRUM accessible from Codex via MCP.
WorkspaceAI Confluence skeleton exists; Pass 2 is complete; all 16 EN/FA page-pairs are
filled with repo-mirrored content; both Home pages now act as portal pages.
AIW Jira backlog now has 6 top-level Epics mirrored to GitHub Issues, plus 6 high-level
Stories mirrored to GitHub Issues: 3 under `AIW-2` and 3 under `AIW-3`.
`scratch/` is ignored and should not appear as an untracked commit candidate.

## Next step
- WSAI Confluence is done: content pages are filled and Home pages link to all topics.
- Continue adding high-level Stories, next = Epic `AIW-5` (Safety & Hygiene Rules),
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
