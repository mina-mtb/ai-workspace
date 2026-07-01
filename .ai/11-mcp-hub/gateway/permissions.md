# Permissions

مدیریت دسترسی‌ها (RBAC / Least Privilege) برای استفاده از سرورهای MCP.

## قوانین پایه‌ای
- **پیش‌فرض:** دسترسی مسدود است (Deny by default).
- **اعطای دسترسی:** فقط پروژه‌ها و ایجنت‌هایی که به صراحت در فایل `.project-ai/selected-mcp-servers.md` لیست شده باشند، مجاز به استفاده از ابزارهای مشخص‌شده هستند.

## نگاشت مجوزها (نمونه)
```yaml
permissions:
  roles:
    - name: orchestrator
      allowed_capabilities:
        - issue-tracking
        - filesystem-read
    - name: architect
      allowed_capabilities:
        - filesystem-read
        - github-search
```
