# PROJECT — Mission & Guardrails (the north star)

> Every agent reads this first. If a task does not serve this mission, stop and flag the Product Owner.

## Current project
<!-- Fill in when you start a real project. For now this workspace itself is the project:
     building and hardening the reusable agent system. -->
Name: ai-workspace (the reusable agentic system)
Goal: Build a tool-agnostic, multi-layer agent system that any AI tool can read from, so software
      can be built consistently and safely across rotating agents.

## Hard guardrails (never violate — see ../rules/)
- One branch per task; no direct pushes to main.
- No direct DB schema edits; migrations only.
- A task is done only when its tests pass (verified by Test/QA, not the builder).
- Stop after 3 failed attempts; hand off to the human.
- No agent merges its own work; the Product Owner is the final merge gate.
- No uncontrolled AI self-learning; AI changes are versioned and eval-gated.

## Who decides what
- The human (you) sets the mission and approves direction.
- Product Owner agent guards the mission and authorizes merges.
- Orchestrator routes work; family agents execute; Test/QA + Reviewer verify.
