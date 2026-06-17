---
name: scoring
description: Use when computing job↔CV suitability scores and ranking candidates/CVs for a job.
---
# Suitability Scoring (FindJob)
## Idea
Given a job description's requirements and a person's CVs/experiences, rank which CV best matches.
Combine semantic similarity (vectors) with structured signals (required skills present, seniority).
## Steps
1. Extract the job's required skills/role.
2. Retrieve candidate CVs/experience vectors (pgvector).
3. Score: similarity + weighted structured matches → ranked list with reasons.
4. Validate output schema; expose the reasoning ("why this CV").
## Gotchas
- No invented experience. The score must be explainable and eval-tested against a golden dataset.
