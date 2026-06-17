---
name: mlops
description: Use when training, evaluating, or serving a custom ML model (not just calling an LLM API).
---
# MLOps
## Steps
1. Version the dataset and the training run (params, metrics).
2. Evaluate against a held-out set; record metrics.
3. Register the model with a version; serve behind a contract/interface.
4. Gate promotion (staging → canary → prod) on metric improvement; keep rollback.
## Gotchas
- Treat model artifacts and datasets as versioned assets, like prompts. No silent swaps.
