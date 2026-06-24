# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
PROJECT-LINKS is merged to `main` and available at `.ai/integrations/PROJECT-LINKS.md`.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
Closed out merged PR #19 for the three new governance rules (2026-06-25):
https://github.com/mina-mtb/ai-workspace/pull/19

Human/Product Owner merged PR #19 into `main` as merge commit `41f95fc` and deleted the
remote branch. Local repo is synced to `main`; local `feat/governance-rules` was deleted.
Rules 12/13/14 are now active on `main`:
- `.ai/rules/12-commit-discipline.md`
- `.ai/rules/13-mirroring.md`
- `.ai/rules/14-prioritization.md`

Mirroring close-out is complete: Jira Stories `AIW-13`, `AIW-14`, and `AIW-15` were moved
to Done. GitHub Issues #14, #15, and #16 received completion comments referencing PR #19
and were closed as completed. Readback verified all three Jira Stories are Done.

Both sides updated? yes: repo `main`, WSAI Confluence, Jira, and GitHub Issues are aligned
for rules 12/13/14.

Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`. Site: `minatahmasebib.atlassian.net`.

## Where we are now
Working branch: `main`, synced with `origin/main` at merge commit `41f95fc`.
Atlassian: Confluence spaces accessible include Personal, PROGRAMVAR, SD, SD1, and WSAI.
Jira projects AIW, FJ, and SCRUM accessible from Codex via MCP.
WorkspaceAI Confluence skeleton exists; Pass 2 is complete; all 16 EN/FA page-pairs are
filled with repo-mirrored content; both Home pages now act as portal pages.
AIW Jira backlog now has 6 top-level Epics mirrored to GitHub Issues, plus 11 high-level
Stories mirrored to GitHub Issues: 3 under `AIW-2`, 3 under `AIW-3`, 2 under `AIW-5`,
and 3 under `AIW-4`.
Epic `AIW-5` is partially done: governance rules 12/14 are Done; other safety/hygiene work
may be added later via incidents or continuous improvement.
WSAI also has an Idea Inbox page for raw ideas before promotion into the real backlog.
`scratch/` is ignored and should not appear as an untracked commit candidate.

## Next step
- Remaining open foundational work: `AIW-2` Stories (branch structure, stale branch triage,
  branch protection).
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
