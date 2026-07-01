# گزارش گروه B: سرور پشتیبان جیرا (Jira Fallback Server)

## خلاصه‌ی کارها
در این مرحله (گام‌های ۷ و ۸)، مستندات و کدهای مربوط به سرور Fallback جیرا توسعه داده شد تا در صورت قطع ارتباط با سرور اصلی (Rovo)، یک مسیر پشتیبان امن و کنترل‌شده در دسترس باشد. همچنین دستور پین‌شده در فایل تنظیمات اصلاح گردید.

## فایل‌های اصلاح/ساخته‌شده

**اصلاح‌شده:**
- `../ai-workspace-config/connections/jira.md`: اصلاح دستور اجرای Primary به `npx -y mcp-remote@0.1.38 https://mcp.atlassian.com/v1/mcp/authv2`.

**ساخته‌شده:**
- `‎.ai/11-mcp-hub/servers/cloud/jira/manifest.md`: تعیین Scopeها و نقش‌های Primary و Fallback.
- `‎.ai/11-mcp-hub/servers/cloud/jira/connection.md`: مستندسازی ارجاع به فایل پیکربندی (بدون Secret) و ثبت دستور پین‌شده.
- `‎.ai/11-mcp-hub/servers/cloud/jira/fallback.md`: شرح پروتکل و قوانین سوییچ (سوییچ خودکار برای READ، سوییچ با تأیید برای WRITE).
- `‎.ai/11-mcp-hub/servers/cloud/jira/server/server.py`: کدهای کامل سرور FastMCP با پایتون شامل تمامی متدهای READ و WRITE درخواستی (با Idempotency key). متد `set_backlog_rank` پیام `Unsupported` برمی‌گرداند و `delete_issue` پیاده‌سازی نشد.
- `‎.ai/11-mcp-hub/servers/cloud/jira/server/requirements.txt`: نیازمندی‌های پایتون (`mcp`, `requests`).

## وضعیت تست‌ها
- **تست ساختار و سینتکس کد پایتون:** تایید شد (کدها با قالب FastMCP منطبق و عاری از مقادیر Hardcode هستند).
- **تستِ زنده‌ی Fallback (اتصال واقعی به جیرا):** ⏳ **معلق (Pending)** - این تست تا زمان آماده‌سازی و قرارگیری Atlassian API Token در فایل `.env` محلی به تعویق افتاده است و پس از تامین Token اجرا خواهد شد.

*(اصلاحات بازبینی اعمال شد: اضافه شدن `requests` به requirements، استفاده از POST برای `search_issues` با JQL، و نمایش متن کامل خطاهای HTTP جیرا).*
