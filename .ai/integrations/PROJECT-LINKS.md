# PROJECT-LINKS — canonical registry of our separate projects

> Every tool reads this before touching Jira, GitHub, or Confluence, so the two projects
> are never mixed. Two fully separate projects. They only relate in ONE way: building FindJob
> improves the WorkspaceAI system (see rules/11-continuous-improvement.md). Nothing else crosses.

## Project 1 — WorkspaceAI (the reusable agentic system / "the team")
- Role: reusable, tool-agnostic foundation. NOT an application.
- GitHub repo: ai-workspace  (this repo)
- Jira project key: AIW   (name: AI Workspace)
- Confluence space key: WSAI   (name: WorkspaceAI)  — spaceId 2195461, homepage 2195585

## Project 2 — FindJob (the first real product)
- Role: the first application built using WorkspaceAI.
- GitHub repo: Find_Job  (separate repo, its own .git)
- Jira project key: FJ   (name: Find Job)
- Confluence space key: TBD   (not created yet — a separate space, NOT under WSAI)

## The one and only relationship between them
While building FindJob (project 2), any recurring problem is fixed at the WorkspaceAI level
(project 1) as a rule/skill/decision, so future projects never repeat it. This is the ONLY
bridge. Code, boards, spaces, and backlogs stay separate.

## Mirroring policy (within each project, never across)
- WSAI Confluence mirrors the ai-workspace repo; FJ Confluence mirrors the Find_Job repo.
- AIW Jira mirrors ai-workspace GitHub Issues; FJ Jira mirrors Find_Job GitHub Issues.
- Source of truth on conflict: the repo wins for rules/skills/state; cross-linked IDs keep Jira↔GitHub aligned.

## Verified tool connections (update as this changes)
- Atlassian (Jira + Confluence) via MCP: VERIFIED working in **Codex** (2026-06-24).
- Antigravity Atlassian MCP: not registered (config/endpoint issue) — do not rely on it for Atlassian.
