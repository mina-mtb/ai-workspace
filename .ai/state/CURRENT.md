# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
PROJECT-LINKS is merged to `main` and available at `.ai/integrations/PROJECT-LINKS.md`.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
Completed AIW-7 branch structure setup (2026-06-25). Created and pushed long-lived
branches:
- `develop` from `main`
- `staging` from `develop`
- `integration` from `develop`

Confirmed all three exist locally and on origin. `.ai/rules/07-branch-flow-and-gates.md`
already showed the concrete branch flow clearly, so no repo doc PR was needed. Mirrored the
active branch model summary to WSAI Confluence page `11 - DevOps & Environments (EN)`
(`2293800`) and FA twin (`2228226`). Jira Story `AIW-7` was moved to Done; GitHub Issue
#8 received a completion comment and was closed as completed. Readback verified `AIW-7`
is Done and the Confluence EN page includes the Branch model section.

Both sides updated? yes: Git branches, WSAI Confluence, Jira, and GitHub Issue #8 are aligned.

Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`. Site: `minatahmasebib.atlassian.net`.

## Where we are now
Working branch: `main`, synced with `origin/main`. Long-lived branches now exist on origin:
`develop`, `integration`, and `staging`.
Atlassian: Confluence spaces accessible include Personal, PROGRAMVAR, SD, SD1, and WSAI.
Jira projects AIW, FJ, and SCRUM accessible from Codex via MCP.
WorkspaceAI Confluence skeleton exists; Pass 2 is complete; all 16 EN/FA page-pairs are
filled with repo-mirrored content; both Home pages now act as portal pages.
AIW Jira backlog now has 6 top-level Epics mirrored to GitHub Issues, plus 11 high-level
Stories mirrored to GitHub Issues: 3 under `AIW-2`, 3 under `AIW-3`, 2 under `AIW-5`,
and 3 under `AIW-4`.
Epic `AIW-2` is partially done: `AIW-7` branch structure is Done; `AIW-8` stale branch
triage and `AIW-9` branch protection remain open.
Epic `AIW-5` is partially done: governance rules 12/14 are Done; other safety/hygiene work
may be added later via incidents or continuous improvement.
WSAI also has an Idea Inbox page for raw ideas before promotion into the real backlog.
`scratch/` is ignored and should not appear as an untracked commit candidate.

## Next step
- Remaining open foundational work: `AIW-2` Stories `AIW-8` (stale branch triage) and
  `AIW-9` (branch protection). Suggested next execution: `AIW-9`.
- Remaining integration knowledge work: `AIW-3` Stories (Atlassian MCP doc, Atlassian
  lessons skill, ROLES mapping).
- Future/non-blocking AIW-4 work remains open: automated Jira<->GitHub sync and bilingual
  auto-translation.
- Decide how much more WorkspaceAI infrastructure to finish before starting FindJob.
- Do NOT start FindJob coding until human says so.

## Blockers / open questions
- Direct REST API Basic-auth retest needs the actual Atlassian email/API-token pair or
  precomputed Basic header in the current session. MCP server auth works through OAuth.
- FindJob Confluence space remains TBD and must be separate from WSAI.
- Old remote branches still need later triage: `feat/product-owner-setup`,
  `feat/tool-model-selection`.
