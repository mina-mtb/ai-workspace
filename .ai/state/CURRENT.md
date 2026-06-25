# CURRENT - Live snapshot

> Update this at the end of EVERY session. Keep it short and true. This is the first thing the
> next agent reads. Overwrite the stale parts; this is a snapshot, not a history (history goes to git + Issues).

## Status
Product Owner onboarding was completed in Antigravity/Claude; verified Atlassian execution connection is Codex MCP.
PROJECT-LINKS is merged to `main` and available at `.ai/integrations/PROJECT-LINKS.md`.
**Atlassian MCP is CONNECTED and WORKING in Codex** - Jira and Confluence read/write page tools are verified functional.

## Last action
Started AIW-9 branch protection setup (2026-06-25), but protection could not be configured
from the current Codex environment. `gh` is not installed/in PATH, and the available GitHub
connector exposes repo/issue/PR/branch tools but no branch protection or ruleset mutation
tool. Raw token/API fallback was not used.

Moved Jira Story `AIW-9` to In Progress and added matching starting/manual-instruction
comments to GitHub Issue #10. Added a pending-manual branch protection note to WSAI
Confluence page `11 - DevOps & Environments (EN)` (`2293800`) and FA twin (`2228226`).
Readback verified `AIW-9` remains In Progress and the Confluence EN page includes the
Branch protection section.

both sides updated? pending manual step. Human must configure GitHub branch protection for
`main` in the UI, then AIW-9 can be closed.

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
triage remains open; `AIW-9` branch protection is In Progress pending manual GitHub UI setup.
Epic `AIW-5` is partially done: governance rules 12/14 are Done; other safety/hygiene work
may be added later via incidents or continuous improvement.
WSAI also has an Idea Inbox page for raw ideas before promotion into the real backlog.
`scratch/` is ignored and should not appear as an untracked commit candidate.

## Next step
- Human applies branch protection manually for `main` in GitHub UI: Settings -> Branches
  -> Add branch protection rule/ruleset -> pattern `main` -> require PR before merge,
  require branch up to date if shown, do not require multiple reviewers, do not require
  status checks yet, disallow force pushes, disallow deletions.
- After manual protection is applied, close out `AIW-9`: verify protection, move Jira to
  Done, close GitHub Issue #10, and update Confluence from pending to protected.
- Decide the state-update flow after `main` protection, because direct `CURRENT.md` pushes
  should move to PR-based checkpointing unless a deliberate exception is chosen.
- Remaining open foundational work after AIW-9: `AIW-8` stale branch triage.
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
