# پیوست فنی برای Roo Code — قرارداد JiraProvider + تصمیم زبان
### الحاق به سند «Handoff for Roo Code» (بعد از اجرای گزارش بازرسی Codex)

> این پیوست بر پایه‌ی گزارش بازرسیِ Codex نوشته شده و پیش‌نیازِ ساختِ سرور MCP جدید Jira است. طبق تحویلِ Codex: **اول قرارداد JiraProvider تعریف می‌شود، بعد سرور جدید ساخته می‌شود.**

---

## ۱. واقعیت‌های کشف‌شده‌ی اتصال فعلی Jira (بدون هیچ Secret)

- **روش فعلی = سرور MCP رسمی Atlassian (Rovo)، remote، از طریق `mcp-remote`.**
- Endpoint فعلی MCP: `https://mcp.atlassian.com/v1/mcp/authv2`
- سایت Jira: `https://minatahmasebib.atlassian.net`
- Cloud ID: `122f52d1-9fca-43d7-885e-8d7b387c257d`
- احراز هویت: **OAuth مدیریت‌شده توسط Atlassian**؛ scopeها: `read:jira-work`, `write:jira-work`.
- هیچ secret/token در repo نیست؛ config بیرونِ repo است (`~/.codex/config.toml`) و به محیط Conda `gemini_env` وابسته است.
- Project keyها: `AIW`, `FJ`.
- عملیاتِ در‌دسترس: خواندن/ساخت/ویرایش issue، گرفتن و اجرای transition، کامنت، جستجوی JQL و Rovo Search، فهرست پروژه‌ها/issue type/متادیتای فیلد، lookup کاربر، remote link و issue link، worklog، خواندن/ساخت relationship در Teamwork Graph.
- محدودیت‌ها: **delete issue در دسترس نیست** (که برای ایمنی خوب است)؛ **تنظیم backlog rank پشتیبانی نمی‌شود**.

---

## ۲. تصمیم نقش‌ها (Primary / Fallback)

> این مهم‌ترین تصمیم این پیوست است.

- **Primary = `jira-rovo-mcp`** (همان سرور رسمی Atlassian که الان کار می‌کند). دلیل: نگه‌داری‌شده توسط Atlassian، پوشش وسیع، OAuth بدون نیاز به مدیریت secret.
- **Fallback = `jira-rest-fallback`** (سرور MCP دست‌سازِ ما با **Python/FastMCP** روی Jira Cloud REST API v3). نقش: پشتیبانِ مقاوم + وسیله‌ی یادگیریِ ساختِ سرور MCP.

اصل: چیزی که کار می‌کند و رایگان نگه‌داری می‌شود را جایگزین نمی‌کنیم؛ رویش یک لایه‌ی مقاومت می‌گذاریم و در کنارش مهارتِ ساختِ سرور را تمرین می‌کنیم.

---

## ۳. قرارداد JiraProvider (چه چیزی ثابت، چه چیزی abstract)

عامل هیچ‌وقت مستقیم با «Rovo» یا «REST» حرف نمی‌زند؛ فقط با قابلیت `issue-tracking` از طریق interface زیر کار می‌کند.

### ۳.۱. ثابت (باید در هر دو provider یکسان بماند)
- هویت سایت/Cloud و project keyها (`AIW`, `FJ`).
- مجموعه‌ی عملیات و معنای آن‌ها (semantics).
- معنای transition و JQL.
- سیاست mirroring، اصل least privilege، عدم ذخیره‌ی secret، و شناسه‌های cross-link.

### ۳.۲. Abstract (می‌تواند بین providerها فرق کند)
- transport و نام ابزارها (tool names).
- endpoint و نسخه‌ی API.
- روش احراز هویت (OAuth در Rovo / API token در REST).
- نگاشت request/response، pagination.
- capability detection، timeout/retry/rate-limit، مدل خطا و logging.

### ۳.۳. متدهای interface (provider-agnostic)
عملیاتِ خواندنی (READ):
- `get_issue(key)`
- `search_issues(jql)`
- `list_projects()`
- `get_issue_types(project)`
- `get_field_metadata(project, issue_type)`
- `lookup_user(query)`
- `get_remote_links(key)`

عملیاتِ نوشتنی (WRITE — با احتیاط ویژه):
- `create_issue(project, issue_type, fields)`
- `edit_issue(key, fields)`
- `transition_issue(key, transition_id)`
- `add_comment(key, body)`
- `add_worklog(key, worklog)`
- `create_issue_link(from_key, to_key, type)`

قابلیت‌های اختیاری/ناپشتیبان:
- `set_backlog_rank(...)` → در provider فعلی پشتیبانی نمی‌شود؛ باید با پرچمِ «Unsupported by active provider» پاسخ روشن بدهد، نه خطای مبهم.
- `delete_issue(...)` → عمداً پیاده‌سازی نمی‌شود (ایمنی).

---

## ۴. سیاست Fallback (قلب ایمنی)

```yaml
capability: issue-tracking
  providers:
    - id: jira-rovo-mcp      # رسمی Atlassian
      role: primary
      transport: mcp-remote (OAuth)
      health_check: یک READ سبک (مثلاً list_projects یا get_issue روی یک key معلوم)
    - id: jira-rest-fallback # ساختِ ما، Python/FastMCP روی REST v3
      role: fallback
      transport: local mcp server (API token)
      health_check: همان READ سبک روی REST

  policy:
    READ:
      auto_fallback: true      # اگر primary در health_check رد شد، خودکار به fallback برو و لاگ بزن
    WRITE:
      auto_fallback: false     # هرگز سوییچِ بی‌سروصدا
      require:
        - idempotency_key                 # هر write یک کلید یکتا دارد
        - verify_previous_operation       # اول چک کن عملیات قبلی واقعاً انجام نشده باشد
        - circuit_breaker                 # بعد از n خطای پیاپی، مسیر را قطع کن
        - human_confirmation              # سوییچِ نوشتنی فقط با تأیید انسان
    on_unsupported_capability:
      behavior: پاسخ صریح «این عملیات در provider فعال پشتیبانی نمی‌شود»
```

قاعده‌ی طلایی write: **بهتر است یک عملیات نوشتنی موقتاً شکست بخورد تا اینکه دوبار (تکراری) اجرا شود.**

همه‌ی این‌ها همچنان از مسیر Gateway/Broker مرکزی رد می‌شوند (permission → validation → execution → audit) که در Handoff تعریف شد.

---

## ۵. تصمیم زبان (ثبت رسمی)

- **سرورهای MCP دست‌سازِ ما با Python نوشته می‌شوند (سبک FastMCP).** دلیل: هم‌خانوادگی با مغز AI و FastAPIِ پروژه، بلوغِ کتابخانه‌های داده/AI/RAG، و هماهنگی با چرخه‌ی Skill Crystallization (تولید فایل `.py`).
- **سیاست چندزبانه:** بانک می‌تواند میزبانِ سرورهای آماده‌ی بیرونی به هر زبانی باشد (مثل همین Rovo MCP که Node/`mcp-remote` است). Gateway زبان را نمی‌بیند و فقط سرور را ثبت می‌کند. یعنی **Python زبانِ «تولیدِ» ماست، ولی بانک چندزبانه است.**
- به‌روزرسانی template: در `‎.ai/11-mcp-hub/templates/` اولویت با `mcp-server-python-template` (FastMCP) است و مبنای همه‌ی سرورهای دست‌ساز می‌شود.

---

## ۶. سخت‌سازی و پایداری (از ریسک‌های گزارش Codex)

1. **Pin کردن نسخه:** به‌جای `mcp-remote@latest` نسخه‌ی مشخص (مثلاً `mcp-remote@0.1.38`) استفاده شود؛ برای reproducibility و کاهش ریسک supply-chain.
2. **مستندسازی اتصال داخل repo:** یک فایل `servers/cloud/jira/connection.md` بساز که شامل باشد: endpoint، Cloud ID، سایت، scopeها، **نامِ** env variableها (بدون مقدار)، و دستور دقیق اجرا. هدف: قابل‌انتقال شدن به دستگاه/agent دیگر (پیش‌نیازِ آینده‌ی تلگرام و چنددستگاهی).
3. **Least privilege برای fallback:** توکنِ REST تا حد ممکن با کمترین دسترسی ساخته شود؛ scope نوشتنی فقط اگر واقعاً لازم بود.
4. **بدون secret در repo:** توکنِ REST از طریق secret manager/env تأمین می‌شود، هرگز داخل repo.
5. **افزودن تست:** یک `health_check` و یک `contract test` سبک برای هر دو provider (چون الان هیچ‌کدام وجود ندارد).

---

## ۷. کارهای بعدی Roo Code (بعد از تأیید نقش‌ها)
1. در `registry/capabilities.md` قابلیت `issue-tracking` را با دو provider و سیاست بخش ۴ ثبت کن.
2. interface بخش ۳.۳ را به‌عنوان قرارداد ثابت پیاده کن.
3. `servers/cloud/jira/connection.md` (بخش ۶.۲) و `manifest.md` را بنویس.
4. نسخه‌ی `mcp-remote` را pin کن.
5. تازه بعد از این، سرور `jira-rest-fallback` را با Python/FastMCP از روی template بساز.
6. تست سوییچِ READ (primary خاموش → fallback) و تستِ عدم‌سوییچِ WRITE را انجام بده.
