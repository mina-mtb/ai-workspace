# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
PROJECT-LINKS is merged to `main` and available at `.ai/integrations/PROJECT-LINKS.md`.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
Synced local `main` after PR #20 was merged (2026-06-25). PR #20 is merged as
`3c9bda8`; local `feat/commit-rule-clarify` was deleted and remote branch was pruned.
Protected-main checkpoint flow is now canonical in `.ai/rules/12-commit-discipline.md`
and `.ai/state/DECISIONS.md`.

Attempted AIW-12 close-out, but `.ai/state/ROLES.template.md` on `main` is still the old
placeholder template, not the filled tool-to-role mapping. No remote `feat/roles-mapping`
branch was found, and git history for the file only shows the old template commit
`f95eca4`. AIW-12 was NOT moved to Done and was NOT mirrored to Confluence. Added blocker
comments to Jira `AIW-12` and GitHub Issue #13.

both sides updated? no for AIW-12 — blocked because the repo source is missing/wrong.

Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`. Site: `minatahmasebib.atlassian.net`.

## Where we are now
Working branch: `chore/checkpoint-roles-blocked`; `main` is synced with `origin/main`.
Long-lived branches exist on origin: `develop`, `integration`, and `staging`.
Atlassian: Confluence spaces accessible include Personal, PROGRAMVAR, SD, SD1, and WSAI.
Jira projects AIW, FJ, and SCRUM accessible from Codex via MCP.
WorkspaceAI Confluence skeleton exists; Pass 2 is complete; all 16 EN/FA page-pairs are
filled with repo-mirrored content; both Home pages now act as portal pages.
AIW Jira backlog now has 6 top-level Epics mirrored to GitHub Issues, plus 11 high-level
Stories mirrored to GitHub Issues: 3 under `AIW-2`, 3 under `AIW-3`, 2 under `AIW-5`,
and 3 under `AIW-4`.
Epic `AIW-2` is partially done: `AIW-7` branch structure is Done, `AIW-9` branch protection
is Done, and `AIW-8` stale branch triage remains open.
Epic `AIW-3` has `AIW-12` blocked/not done because ROLES mapping is still the placeholder
template on `main`; `AIW-10` and `AIW-11` remain open.
Epic `AIW-5` is partially done: governance rules 12/14 are Done; other safety/hygiene work
may be added later via incidents or continuous improvement.
WSAI also has an Idea Inbox page for raw ideas before promotion into the real backlog.
`scratch/` is ignored and should not appear as an untracked commit candidate.

## Next step
- Create/merge the ROLES mapping PR first (`.ai/state/ROLES.template.md` must contain the
  real tool-to-role mapping, not the placeholder template).
- After ROLES is present on `main`, close out `AIW-12`: move Jira to Done, close GitHub
  Issue #13, and mirror the summary to WSAI page `04 - Agents` EN/FA.
- Remaining open foundational work: `AIW-8` stale branch triage.
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
