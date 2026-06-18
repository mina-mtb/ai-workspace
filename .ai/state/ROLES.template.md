# ROLES — tool-to-role mapping for THIS project

> Copy this into each project and fill it in at kickoff. Every agent reads this to confirm its role
> before acting (see ../rules/10-role-boundaries.md). One tool may hold one role per piece of work.

## Project
Name: <repo name>
Date set: <date>

## Mapping (the human decides this per project)
- Product Owner : <tool, e.g. Claude Code>
- Coder         : <tool, e.g. Codex in VS Code>
- Tester (QA)   : <tool, e.g. Antigravity>
- Reviewer      : <tool, or "same as Tester for now", or "Product Owner reviews lightly">
- Human gates   : the human (you)

## Rules reminder
- No tool verifies or merges its own work.
- The tool that coded a task may not test, review, or merge that same task.
- Only Product Owner merges feature -> integration. Only the human moves through the two human gates.
- Each agent states its role at the start of a turn and refuses out-of-role work.
