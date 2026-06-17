---
name: llmops
description: Use when versioning prompts/models/RAG, setting up eval gates, traces, or cost/latency tracking for AI behaviour.
---
# LLMOps
## Rules in practice
- Prompts live in `llmops/prompts/<task>/vX.Y.Z.yaml` with metadata (id, version, owner, status, input/output schema, eval dataset, rollback version).
- Any prompt/model/RAG change → run evals → staging → canary → production only if metrics improve.
- Every AI request is traced with prompt/model/RAG versions, retrieved chunks, latency, cost.
- Raw user feedback never updates AI behaviour directly (see ../rules/llmops.md).
