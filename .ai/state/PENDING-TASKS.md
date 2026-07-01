# کارهای معلق (Pending Tasks)

این فایل حاوی کارهایی است که در طول فازهای مختلف به دلایل وابستگی‌های خارجی یا تصمیمات استراتژیک معلق شده‌اند و نیاز به اقدام در آینده دارند.

## PENDING-001: تستِ زنده‌ی سرور Jira fallback
- وضعیت: معلق (Pending)
- دلیل: provider اصلی (OAuth/Rovo MCP) سالم کار می‌کند، پس عجله‌ای نیست.
- برای انجامش لازم است:
  1. ساخت یک Atlassian API token جدید (نام پیشنهادی: jira-rest-fallback، scopeها: read:jira-work و write:jira-work).
  2. ساخت فایل .env لوکالِ gitignore‌شده در ai-workspace-config با سه متغیر:
     JIRA_REST_URL, JIRA_REST_USER, JIRA_REST_API_TOKEN.
  3. اجرای سرور و گرفتنِ تستِ READ زنده (مثلاً list_projects) به‌عنوان PASS.
- ارجاع: REPORT-FINAL.md، چک‌لیست بخش ۷ (موارد تستِ زنده).