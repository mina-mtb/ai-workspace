# .ai — Shared Agent Knowledge Base

The reusable brain for all AI agents across all projects in this workspace.
Written once, read by every tool (via the root `AGENTS.md`).

## Folders

| Folder | What it holds | Rule of thumb |
|---|---|---|
| `rules/` | **Mandatory constraints.** What agents must / must never do. | A rule is non-negotiable. Short. |
| `skills/` | **How-to guides** for specific tasks. Loaded on demand. | One task per file. YAML frontmatter so tools can match it. |
| `agents/` | **Role definitions.** Mission, what each role may change, required output. | Narrow authority per role. |
| `workflows/` | **Step-by-step processes** for repeatable jobs. | Triggered as a checklist or `/slash` command. |
| `handoffs/` | **Standard packet** an agent passes to the next agent. | Prevents rework and lost context. |
| `communication-protocol.md` | How agents report results and hand off. | The shared "contract". |

## Rule vs Skill (the distinction that matters)

- **Rule** = *what is mandatory.* "Schema changes must go through migrations."
- **Skill** = *how to do it.* "Here are the exact steps to create and apply a migration."

## Keep it lean

Human-written, minimal files beat long auto-generated ones. Only write down what an agent
can't discover by itself: exact commands, hard constraints, and your non-standard patterns.
Prune ruthlessly. An inaccurate rule is worse than no rule.
