# Skills Index

Agents read THIS first to know which skill file to open — so they don't load everything and burn context.
Each skill has a `description` in its frontmatter; match the task to it, then open only that file.

## database/  (owned by Database agent)
- ef-core-migration.md — change schema in .NET/EF Core via migrations
- raw-sql.md — when and how to use raw SQL safely
- pgvector.md — vector storage & similarity search in PostgreSQL (FindJob CV/job matching)

## ai-engineer/  (owned by AI Engineer agent)
- rag-pipeline.md — chunking, embedding, retrieval, reranking, RAG eval
- embedding.md — building/versioning embeddings (e.g. BERT) for semantic search
- scoring.md — job↔CV suitability scoring & ranking
- llmops.md — prompt/model/RAG versioning, eval gates, traces, cost
- mlops.md — training/evaluating/serving custom ML models

## devops/  (owned by DevOps agent)
- docker.md — Dockerfiles & Docker Compose for local + VPS
- ci-cd.md — GitHub Actions pipeline (build, test, eval, security scan)
- deploy-auth.md — deployment authorization & environment promotion
- external-apis.md — integrating & securing third-party services/APIs

## backend/  (owned by Backend agent)
- clean-architecture-dotnet.md — Domain/Application/Infrastructure/API layering rules

## frontend/  (owned by Frontend agent)
- (add as needed)

## Promotion rule
When a skill grows large and is used constantly, promote it to its own agent in ../agents/.
