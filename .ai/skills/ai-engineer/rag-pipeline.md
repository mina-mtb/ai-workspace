---
name: rag-pipeline
description: Use when building or changing retrieval-augmented generation — chunking, embedding, retrieval, reranking, and RAG evaluation.
---
# RAG Pipeline
## Steps
1. Ingest & chunk documents (record chunking strategy + version).
2. Embed chunks (see embedding.md); store vectors (see ../database/pgvector.md).
3. Retrieve top-K by similarity; optionally rerank.
4. Build the final prompt with retrieved context (prompt is versioned under llmops/).
5. Validate output (schema, no invented facts, no PII leak).
## Gotchas
- Record document version, chunking, embedding model, topK, reranker, vector store — all versioned.
- Run RAG eval before any production change (../rules/llmops.md).
