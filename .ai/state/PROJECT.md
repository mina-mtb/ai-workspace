# PROJECT — Mission & Guardrails (the north star)

Every agent reads this first. If a task does not serve this mission, stop and flag the Product Owner.

## Operating mode
MERGE_MODE: human-approval
<!-- human-approval = the human plays Product Owner; nothing merges until the human says "approved".
     product-owner-auto = a trusted Product Owner agent approves on its own. Switch later, when trust is earned.
     Change behaviour by editing this one line. See ../rules/04-merge-authority.md. -->

## Current project
Name: ai-workspace (the reusable agentic system)
Goal: Build a tool-agnostic, multi-layer agent system that any AI tool can read from, so software
      can be built consistently and safely across rotating agents.
Next planned project: FindJob — phase 1 (CV matching + CV generation).

## How work flows right now (semi-automatic)
The human acts as the "interface" — carrying a task from one role to the next via the repo and GitHub
Issues. Agents do NOT call each other automatically yet. The shared memory (this folder + Issues) is
what lets a fresh agent continue where another stopped. Full auto handoff is a future build, not a setting.

## Hard guardrails (never violate — see ../rules/)
- One branch per task; no direct pushes to main.
- No direct DB schema edits; migrations only.
- A task is done only when its tests pass (verified by Test/QA, not the builder).
- Stop after 3 failed attempts; hand off to the human.
- No agent merges its own work; the Product Owner is the final merge gate (per MERGE_MODE above).
- Stay inside your module; cross-module only through contracts (../rules/06-module-boundaries.md).
- No uncontrolled AI self-learning; AI changes are versioned and eval-gated.

## Who decides what
- The human (you) sets the mission and, in human-approval mode, gives the final go-ahead.
- Product Owner agent guards the mission and (in product-owner-auto mode) authorizes merges.
- Orchestrator routes work; family agents execute; Test/QA + Reviewer verify.
