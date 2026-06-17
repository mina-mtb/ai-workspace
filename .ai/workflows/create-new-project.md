# Workflow: Create a New Project

Use when starting a brand-new application on top of this shared system.

1. Write the goal in a `project-brief.md` (what it does, who it's for, constraints).
2. Orchestrator reads the brief, identifies project type, selects relevant rules + skills.
3. Architect designs initial module boundaries; records ADR-0001 (initial architecture).
4. Create the project's own thin `AGENTS.md` (commands + stack + pointer to shared `.ai/`).
5. Set up git, branch protection, and a test command from day one.
6. Backend / Frontend / Database / DevOps agents scaffold only their parts.
7. Reviewer verifies the skeleton against the rules before real feature work begins.
