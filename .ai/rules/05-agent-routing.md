# Rule: Agent Routing (how the Orchestrator assigns work)

The Orchestrator reads a task and routes it to the right family agent. Routing is explicit, not magic.

| If the task is about... | Route to | Then verified by |
|---|---|---|
| Module boundaries, tech decisions, ADRs | Architect | Reviewer |
| API / domain / application logic (.NET) | Backend | Test/QA → Reviewer |
| RAG, embeddings, scoring, prompts, model/eval | AI Engineer | Test/QA → Reviewer |
| Schema, migrations, SQL, pgvector | Database | Test/QA → Reviewer |
| UI, components, API wiring | Frontend | Test/QA → Reviewer |
| Docker, CI/CD, environments, deploy, external APIs | DevOps | Reviewer |
| Defining/running tests, acceptance | Test/QA | (produces the signal) |
| Whether work fits the mission + merge approval | Product Owner | (final gate) |

## Notes
- Every implementation task ends at Test/QA → Reviewer → Product Owner. That chain is not optional.
- A family agent loads the specialist skill it needs from `../skills/<family>/` (e.g. Database loads
  `skills/database/pgvector.md`). Specialists are skills, not separate agents — until one grows big
  enough to be promoted to its own agent.
- If a task spans multiple families, the Orchestrator sequences them (default: one at a time to avoid
  merge conflicts) and defines the handoffs.
