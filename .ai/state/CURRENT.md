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

## Where we are now (2026-07-01)
- بانک MCP (`.ai/11-mcp-hub`) با ساختار Gateway، Registry، Templates و قانون تفکیک Config/Secrets در مخزن مجزا (`ai-workspace-config`) ایجاد شد.
- پروتکل Jira با معماری Fallback پیاده‌سازی شده است (Rovo MCP به عنوان Primary و FastMCP Python به عنوان Fallback).
- تست زنده Fallback به دلیل عدم وجود توکن موقتاً معلق (Pending) است اما ساختار کد به شکل Dry Run تایید گردید.
- گردش کار ساخت سرورهای جدید MCP به صورت کنترل‌شده (با اجبار تایید انسان در مراحل حساس) تنظیم گردید.
- Working branch فعلی: `feature/mcp-hub-group-a`

## Next step
- تامین Atlassian API Token، ثبت در `.env` محلی و اجرای تست زنده روی سرور Fallback جیرا.
- بازبینی و تایید Merge برنچ `feature/mcp-hub-group-a` توسط انسان.
- رفع مشکل مسدود بودن `AIW-12` مربوط به `ROLES.template.md`.

## Blockers / open questions
- Direct REST API Basic-auth retest needs the actual Atlassian email/API-token pair or
  precomputed Basic header in the current session. MCP server auth works through OAuth.
- FindJob Confluence space remains TBD and must be separate from WSAI.
- Old remote branches still need later triage: `feat/product-owner-setup`,
  `feat/tool-model-selection`.
