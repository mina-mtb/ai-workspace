# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
PROJECT-LINKS is merged to `main` and available at `.ai/integrations/PROJECT-LINKS.md`.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
Opened PR #19 for the three new governance rules (2026-06-25):
https://github.com/mina-mtb/ai-workspace/pull/19

On branch `feat/governance-rules`, added:
- `.ai/rules/12-commit-discipline.md`
- `.ai/rules/13-mirroring.md`
- `.ai/rules/14-prioritization.md`

Wired the rules into `.ai/rules/00-core.md`, `AGENTS.md`, and `.ai/state/DECISIONS.md`.
Mirrored the rule summaries to WSAI Confluence page `05 - Rules - Non-negotiable (EN)`
(`2359337`) and FA twin (`2424913`). Jira Stories `AIW-13`, `AIW-14`, and `AIW-15`
were moved to In Progress; GitHub Issues #14, #15, and #16 received matching status
comments. Readback verified the Confluence EN page includes the Governance discipline
section and the three Jira Stories are In Progress.

Both sides updated? yes: repo branch + WSAI Confluence are aligned for this rule change.
Canonical repo activation on `main` still waits for human merge of PR #19.

Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`. Site: `minatahmasebib.atlassian.net`.

## Where we are now
Working branch: `feat/governance-rules`, pushed to origin with PR #19 open against `main`.
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
- Human/Product Owner reviews PR #19. Do not merge it automatically.
- If PR #19 is approved and merged, move `AIW-13`, `AIW-14`, and `AIW-15` to Done and
  add matching completion comments to GitHub Issues #14, #15, and #16.
- Set up branch structure when ready: develop / integration / staging.
- Triage old remote branches: `feat/product-owner-setup`, `feat/tool-model-selection`.
- Do NOT start FindJob coding until human says so.

## Blockers / open questions
- Direct REST API Basic-auth retest needs the actual Atlassian email/API-token pair or
  precomputed Basic header in the current session. MCP server auth works through OAuth.
- FindJob Confluence space remains TBD and must be separate from WSAI.
- Old remote branches still need later triage: `feat/product-owner-setup`,
  `feat/tool-model-selection`.
