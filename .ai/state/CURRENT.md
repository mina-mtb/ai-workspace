# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
PROJECT-LINKS is merged to `main` and available at `.ai/integrations/PROJECT-LINKS.md`.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
Completed git housekeeping and Confluence Pass 2 batch 3 (2026-06-24).
Added `scratch/` to `.gitignore`, committed and pushed checkpoint `01be7b9`
(`chore: ignore scratch/ and checkpoint CURRENT state`). From now on, commit pending
`CURRENT.md`/state changes before starting new work so state history stays in git.

Filled WSAI pages 09, 10, 11, and 12 in both EN and FA from the real repo files using
native Atlassian MCP only, sequential calls, and `cloudId="minatahmasebib.atlassian.net"`.
Each page has a top cross-link to its language twin and the standard repo-wins mirror note.
Readback verified page `2359377` (`12 - LLMOps EN`) includes the Persian cross-link and
the LLMOps rules table.

Updated page IDs:
- 09 EN `2588673`, 09 FA `2162711`
- 10 EN `2490389`, 10 FA `2359357`
- 11 EN `2293800`, 11 FA `2228226`
- 12 EN `2359377`, 12 FA `2359397`

Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`. Site: `minatahmasebib.atlassian.net`.

## Where we are now
Working branch: `main`, synced with `origin/main` before Pass 2 batch 1.
Atlassian: Confluence spaces accessible include Personal, PROGRAMVAR, SD, SD1, and WSAI.
Jira projects AIW, FJ, and SCRUM accessible from Codex via MCP.
WorkspaceAI Confluence skeleton exists; Pass 2 batches 1, 2, and 3 are filled.
`scratch/` is ignored and should not appear as an untracked commit candidate.

## Next step
- Human checks page `12 - LLMOps (EN)` in browser and confirms it matches `.ai/rules/llmops.md`
  and `.ai/skills/ai-engineer/llmops.md`.
- Continue Confluence Pass 2 next: batch 4 = pages 13, 14, and 15 in EN+FA.
- Do NOT start FindJob coding until human says so.

## Blockers / open questions
- Direct REST API Basic-auth retest needs the actual Atlassian email/API-token pair or
  precomputed Basic header in the current session. MCP server auth works through OAuth.
- FindJob Confluence space remains TBD and must be separate from WSAI.
- Old remote branches still need later triage: `feat/product-owner-setup`,
  `feat/tool-model-selection`.
