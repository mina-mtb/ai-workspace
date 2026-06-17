# START HERE

This folder is a starter for a **reusable, tool-agnostic agent system**.
The goal: write your rules, skills, and agent roles **once**, and have every AI tool you use
(ChatGPT, Gemini, Codex, Antigravity, Claude Code, Cursor…) read from the same source —
so they all behave consistently and get smarter project after project.

## The big idea

```
.ai/         = the shared brain (rules, skills, agent roles, workflows, handoffs).
               Written once. Reused everywhere. Version-controlled = permanent capital.

AGENTS.md    = the universal "door". Every modern AI coding tool reads this file and
               from it is pointed into .ai/. This is what connects your separate tools.

CLAUDE.md /  = thin one-line files that just say "follow AGENTS.md", for tools that
GEMINI.md      look for their own filename first.
```

## How each tool plugs in

| Tool | How it reads the system |
|---|---|
| **Codex, Cursor, Windsurf, Continue, Aider, Copilot, Gemini CLI** | Read `AGENTS.md` at repo root automatically. Nothing extra to do. |
| **Claude Code** | Reads `CLAUDE.md` (and `AGENTS.md`). Already pointed in. |
| **Antigravity** | Reads `AGENTS.md`, and also its own `.agents/rules` + `.agents/skills`. For heavy Antigravity use, you can mirror `.ai/skills/*` into `.agents/skills/` (they use the same YAML frontmatter format). |
| **ChatGPT / Gemini (web chat)** | No auto-read. Two options: (1) create a Project / Gem and paste the contents of `.ai/rules/00-core.md` + the relevant agent role into its instructions once; (2) upload the specific `.ai/` files you need at the start of a chat. |

## Two levels: workspace vs project

- Put `.ai/` at your **workspace root** (next to all your projects), like your friend's screenshot.
  This is the shared library every project inherits.
- Each **project** gets its own thin `AGENTS.md` (and optional `.project-ai/` folder) that points
  to the shared `.ai/` and adds only what is specific to that project (its commands, its stack, its ADRs).

## First steps (do these today)

1. Copy `.ai/`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` to your real workspace root.
2. Open `AGENTS.md` and fill in the **Commands** section for your real project. Delete any hard
   constraint that doesn't apply to you. Keep it short and TRUE.
3. Open `.ai/rules/` and keep only the rules you actually want enforced. Edit the database rule
   to match your stack (it currently uses the EF Core / migrations example).
4. Open `.ai/agents/` and adjust the roles to match how you actually want to split work.
5. Commit everything to git. From now on, every agent reads from here.
6. Pick ONE small real task and run it through one tool, following the workflow in
   `.ai/workflows/add-feature.md`. See what the agent gets wrong, then fix the rule/skill that
   would have prevented it. That feedback loop is how this system gets stronger over time.

## The one rule that keeps this healthy

When an agent does something wrong, don't just correct it in the chat.
**Ask: "which rule or skill, if it had existed, would have prevented this?"** — then write that
rule/skill into `.ai/`. That is the entire secret of why these systems compound.
