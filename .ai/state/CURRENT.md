# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
PROJECT-LINKS is merged to `main` and available at `.ai/integrations/PROJECT-LINKS.md`.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
Created the WorkspaceAI Idea Inbox (2026-06-25). Recorded the Idea Inbox decision in
`.ai/state/DECISIONS.md` and pushed commit `138ab80` (`docs: add Idea Inbox concept`).
Created WSAI Confluence page `16 - Idea Inbox / دفتر ایده‌ها` under homepage `2195585`
with page ID `3473409`. Seeded the first raw idea: bilingual auto-translation for manual
Jira/Confluence entries. Added the Idea Inbox link as item 16 at the bottom of both Home
page Contents sections (`00 EN` and `00 FA`). Readback verified the new page body and
the Home EN link to page `3473409`.

Created page:
- `16 - Idea Inbox / دفتر ایده‌ها` / Confluence page `3473409`.

Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`. Site: `minatahmasebib.atlassian.net`.

## Where we are now
Working branch: `main`, synced with `origin/main` before Pass 2 batch 1.
Atlassian: Confluence spaces accessible include Personal, PROGRAMVAR, SD, SD1, and WSAI.
Jira projects AIW, FJ, and SCRUM accessible from Codex via MCP.
WorkspaceAI Confluence skeleton exists; Pass 2 is complete; all 16 EN/FA page-pairs are
filled with repo-mirrored content; both Home pages now act as portal pages.
AIW Jira backlog now has 6 top-level Epics mirrored to GitHub Issues, plus 6 high-level
Stories mirrored to GitHub Issues: 3 under `AIW-2` and 3 under `AIW-3`.
WSAI also has an Idea Inbox page for raw ideas before promotion into the real backlog.
`scratch/` is ignored and should not appear as an untracked commit candidate.

## Next step
- WSAI Confluence is done: content pages are filled and Home pages link to all topics.
- Continue adding high-level Stories, next = Epic `AIW-5` (Safety & Hygiene Rules),
  mirrored Jira<->GitHub in the same bilingual pattern.
- Later: promote the raw bilingual auto-translation idea into an Epic `AIW-4` Story when ready.
- Set up branch structure when ready: develop / integration / staging.
- Triage old remote branches: `feat/product-owner-setup`, `feat/tool-model-selection`.
- Do NOT start FindJob coding until human says so.

## Blockers / open questions
- Direct REST API Basic-auth retest needs the actual Atlassian email/API-token pair or
  precomputed Basic header in the current session. MCP server auth works through OAuth.
- FindJob Confluence space remains TBD and must be separate from WSAI.
- Old remote branches still need later triage: `feat/product-owner-setup`,
  `feat/tool-model-selection`.
