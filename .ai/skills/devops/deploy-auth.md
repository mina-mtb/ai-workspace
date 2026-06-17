---
name: deploy-auth
description: Use for deployment authorization and promoting a build between environments (staging → production).
---
# Deployment Authorization
## Rule
Environment promotion is gated. Production deploy requires: green pipeline, staging smoke tests passed,
migration rehearsed with backup, and Product Owner approval recorded.
## Environments
Local/Dev · Test/CI · Staging · Production · AI Sandbox — fully separated secrets/DBs. Dev never touches prod.
