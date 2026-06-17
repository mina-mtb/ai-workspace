---
name: pgvector
description: Use for vector storage and semantic similarity search inside PostgreSQL — e.g. matching a job description to the most relevant CV (FindJob phase 1).
---
# pgvector (vector search in PostgreSQL)
## When to use
Semantic search / similarity (FindJob: find the best-matching CV for a job). Chosen over a separate
vector DB (Qdrant) for the start: one fewer database, simpler backup/deploy.
## Steps
1. Enable the extension via a migration: `CREATE EXTENSION IF NOT EXISTS vector;`
2. Store embeddings in a `vector(N)` column (N = embedding dimension).
3. Add an index (e.g. HNSW / IVFFlat) for fast similarity search.
4. Query nearest neighbours by cosine/inner-product distance to the job's embedding.
## Gotchas
- The embedding model + dimension is part of the RAG version — coordinate with ai-engineer/embedding.md.
- The vector-store choice must be versioned and RAG eval run before any production change.
- Migrate to Qdrant only when workload/latency truly demands it.
