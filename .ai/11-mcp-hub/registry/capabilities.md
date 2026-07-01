# Capabilities Registry

این فایل نگاشت قابلیت‌ها به سرورهای ارائه‌دهنده (Providers) را تعریف می‌کند.

```yaml
capabilities:
  - capability: issue-tracking
    policy:
      READ:
        auto_fallback: true
      WRITE:
        auto_fallback: false
        require:
          - idempotency_key
          - verify_previous_operation
          - circuit_breaker
          - human_confirmation
      on_unsupported_capability:
        behavior: "پاسخ صریح: این عملیات در provider فعال پشتیبانی نمی‌شود"
    providers:
      - id: jira-rovo-mcp
        role: primary
        transport: mcp-remote (OAuth)
        health_check: "READ سبک (مانند list_projects)"
      - id: jira-rest-fallback
        role: fallback
        transport: local mcp server (API token)
        health_check: "READ سبک از طریق REST"