# LLMOps Rules (for any AI behaviour change)

AI behaviour is not "just code". Every change to how the AI behaves is governed.

- **No uncontrolled self-learning.** Raw user feedback NEVER updates a prompt, RAG index, or model directly.
  Path: raw feedback → review/approval → offline eval → staging → canary → production-only-if-metrics-improve.
- **Version everything.** Prompts, model choices, and RAG index config are versioned and live under `llmops/`,
  not scattered in code. Each prompt carries metadata (id, version, owner, status, schemas, eval dataset, rollback version).
- **Eval gates.** If a prompt / model / RAG index changes, the relevant evals must run and pass before release.
- **Output validation.** Every AI output is validated (schema, required fields, no invented facts, no PII leakage) before it is shown or saved.
- **Traceability.** Every AI request is traceable with its prompt/model/RAG versions, retrieved chunks, latency, and cost.
