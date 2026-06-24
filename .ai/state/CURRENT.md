# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
PROJECT-LINKS is merged to `main` and available at `.ai/integrations/PROJECT-LINKS.md`.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
Created 5 governance Stories for the next rules work (2026-06-25). This was paper trail
only: no rule files were written yet. Each Story has a bilingual EN/FA description, is
linked to its parent Epic, and is mirrored to a GitHub Issue with label `story`; each
GitHub Issue links to the Jira Story and parent Epic, and each Jira Story has a comment
linking back to GitHub.

Foundational Stories, created first and set to Priority=Highest:
- `AIW-13` / GitHub #14 - Write commit-discipline rule - parent `AIW-5`.
- `AIW-14` / GitHub #15 - Write prioritization rule - parent `AIW-5`.
- `AIW-15` / GitHub #16 - Write mirroring / dual-write rule - parent `AIW-4`.

Future Stories, set to Priority=Low:
- `AIW-16` / GitHub #17 - Build automated Jira<->GitHub sync - parent `AIW-4`.
- `AIW-17` / GitHub #18 - Build bilingual auto-translation for manual entries - parent
  `AIW-4`; promoted from Idea Inbox page `3473409`.

Readback verified the Jira parent links, priorities, bilingual descriptions, and Jira-side
GitHub mirror comments. The Idea Inbox page was updated: the bilingual auto-translation
idea moved from Raw to Promoted and now points to `AIW-17` / GitHub #18. Direct Jira
backlog-rank mutation was not exposed in the current MCP tool surface, so the three
foundational items were created first and marked Highest; no board-rank API change was made.

Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`. Site: `minatahmasebib.atlassian.net`.

## Where we are now
Working branch: `main`, synced with `origin/main` before Pass 2 batch 1.
Atlassian: Confluence spaces accessible include Personal, PROGRAMVAR, SD, SD1, and WSAI.
Jira projects AIW, FJ, and SCRUM accessible from Codex via MCP.
WorkspaceAI Confluence skeleton exists; Pass 2 is complete; all 16 EN/FA page-pairs are
filled with repo-mirrored content; both Home pages now act as portal pages.
AIW Jira backlog now has 6 top-level Epics mirrored to GitHub Issues, plus 11 high-level
Stories mirrored to GitHub Issues: 3 under `AIW-2`, 3 under `AIW-3`, 2 under `AIW-5`,
and 3 under `AIW-4`.
WSAI also has an Idea Inbox page for raw ideas before promotion into the real backlog.
`scratch/` is ignored and should not appear as an untracked commit candidate.

## Next step
- WSAI Confluence is done: content pages are filled and Home pages link to all topics.
- Write the three rule files next: `.ai/rules/12-commit-discipline.md`,
  `.ai/rules/13-mirroring.md`, and `.ai/rules/14-prioritization.md`.
- Reference the new rules from `.ai/rules/00-core.md` and `AGENTS.md`.
- After rule files exist, mirror their summaries into WSAI Confluence per the mirroring rule.
- Set up branch structure when ready: develop / integration / staging.
- Triage old remote branches: `feat/product-owner-setup`, `feat/tool-model-selection`.
- Do NOT start FindJob coding until human says so.

## Blockers / open questions
- Direct REST API Basic-auth retest needs the actual Atlassian email/API-token pair or
  precomputed Basic header in the current session. MCP server auth works through OAuth.
- FindJob Confluence space remains TBD and must be separate from WSAI.
- Old remote branches still need later triage: `feat/product-owner-setup`,
  `feat/tool-model-selection`.
