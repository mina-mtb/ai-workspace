# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
PROJECT-LINKS is merged to `main` and available at `.ai/integrations/PROJECT-LINKS.md`.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
Created the first real AIW backlog Epics (2026-06-24). Recorded the decision that AIW is
a permanent living board in `.ai/state/DECISIONS.md` and pushed commit `0a7b627`
(`docs: record AIW-is-a-living-project decision`). Created 6 Jira Epics in project `AIW`
and mirrored each as a GitHub Issue in `mina-mtb/ai-workspace` with label `epic`.
Each GitHub Issue body links to its Jira Epic, and each Jira Epic has a comment linking
back to its GitHub Issue. `AIW-1` / GitHub #2 was marked Done/completed; the rest remain open.

Created Epic mirrors:
- `AIW-1` / GitHub #2 - Confluence Documentation Foundation - Done/completed.
- `AIW-2` / GitHub #3 - Git & Branch Infrastructure - To Do/open.
- `AIW-3` / GitHub #4 - Integration & Connection Knowledge - To Do/open.
- `AIW-4` / GitHub #5 - Mirroring & Sync Governance - To Do/open.
- `AIW-5` / GitHub #6 - Safety & Hygiene Rules - To Do/open.
- `AIW-6` / GitHub #7 - Continuous Improvement (Ongoing - never closed) - To Do/open permanently.

Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`. Site: `minatahmasebib.atlassian.net`.

## Where we are now
Working branch: `main`, synced with `origin/main` before Pass 2 batch 1.
Atlassian: Confluence spaces accessible include Personal, PROGRAMVAR, SD, SD1, and WSAI.
Jira projects AIW, FJ, and SCRUM accessible from Codex via MCP.
WorkspaceAI Confluence skeleton exists; Pass 2 is complete; all 16 EN/FA page-pairs are
filled with repo-mirrored content; both Home pages now act as portal pages.
AIW Jira backlog now has 6 top-level Epics mirrored to GitHub Issues.
`scratch/` is ignored and should not appear as an untracked commit candidate.

## Next step
- WSAI Confluence is done: content pages are filled and Home pages link to all topics.
- Add Stories under each AIW Epic, mirrored Jira<->GitHub in the same pattern.
- Set up branch structure when ready: develop / integration / staging.
- Triage old remote branches: `feat/product-owner-setup`, `feat/tool-model-selection`.
- Do NOT start FindJob coding until human says so.

## Blockers / open questions
- Direct REST API Basic-auth retest needs the actual Atlassian email/API-token pair or
  precomputed Basic header in the current session. MCP server auth works through OAuth.
- FindJob Confluence space remains TBD and must be separate from WSAI.
- Old remote branches still need later triage: `feat/product-owner-setup`,
  `feat/tool-model-selection`.
