---
name: embedding
description: Use when generating or versioning text embeddings (e.g. BERT) for semantic search/matching.
---
# Embeddings
## Steps
1. Pick & pin the embedding model (name + version). The dimension must match the pgvector column.
2. Batch-embed; track which model/version produced each vector.
3. Re-embedding everything is required if you change the model — treat as a RAG version bump.
## Gotchas
- Embedding model is part of RAG versioning. Changing it invalidates existing vectors.
