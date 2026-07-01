# گزارش نهایی: ساخت بانک مرکزی MCP

این گزارش آخرین مرحله از پروسه ۳ مرحله‌ای ساخت MCP Hub است.

## خلاصه‌ی گروه‌ها
- **گروه A:** ساختار پایه پوشه‌ها در `‎.ai/11-mcp-hub`، قانون تفکیک Config/Secret (`Rule 15`)، راه‌اندازی پوشه جداگانه‌ی `ai-workspace-config`، تنظیمات Gateway (مسیریابی، مجوزها و ممیزی) و رجیستری (Capabilities و Catalog) ساخته شد.
- **گروه B:** مستندسازی اتصال اصلی جیرا (Rovo) و پیاده‌سازی کامل سرور پشتیبان با FastMCP (`jira-rest-fallback`) با رعایت قوانین Fallback، Idempotency، و اضافه شدن وابستگی‌ها و اصلاحات امنیتی/خطایابی.
- **گروه C:** گردش‌کار ساخت ابزارهای جدید MCP (`create-new-mcp-server.md`) همراه با تأکید بر تأیید انسانی تدوین شد. تمامی تصمیمات به عنوان ADR ثبت شدند و فایل‌های State و Lessons متبلور و آپدیت گردیدند.

## درخت نهایی ساخته شده

### .ai/11-mcp-hub/
```text
C:\USERS\MINA_\AI-WORKSPACE\.AI\11-MCP-HUB
├── README.md
├── config/
│   └── README.md
├── gateway/
│   ├── audit-policy.md
│   ├── broker-config.md
│   ├── permissions.md
│   └── README.md
├── registry/
│   ├── capabilities.md
│   ├── catalog.md
│   └── README.md
├── servers/
│   ├── README.md
│   ├── cloud/
│   │   ├── github/
│   │   └── jira/
│   │       ├── connection.md
│   │       ├── fallback.md
│   │       ├── manifest.md
│   │       └── server/
│   │           ├── requirements.txt
│   │           └── server.py
│   ├── custom/
│   └── system/
│       ├── db-sqlite-postgres/
│       └── filesystem/
├── templates/
│   ├── README.md
│   └── mcp-server-python-template/
│       ├── requirements.txt
│       └── server.py
└── workflows/
    ├── create-new-mcp-server.md
    └── README.md
```

### ai-workspace-config/
```text
C:\USERS\MINA_\AI-WORKSPACE-CONFIG
├── .env.example
├── README.md
├── connections/
│   └── jira.md
└── environments/
```

## وضعیت تست‌ها
- **تستِ خشک کد سرور:** سرور پایتون `server.py` با موفقیت Compile شد و هیچ خطای Import و Syntax وجود ندارد. منطق READ auto-fallback و WRITE no-switch در کدهای فایل و همچنین در `capabilities.md` و `fallback.md` به صورت کامل پیاده‌سازی و تشریح شد.
- **تست اتصال زنده:** ⏳ **معلق تا زمان توکن** (تا زمان تامین `Atlassian API Token` در `.env`).

## چک‌لیست بخش ۷ سند اصلی

**ساختار و قانون**
- [x] `‎.ai/11-mcp-hub/` با ساختار کامل ساخته شد.
- [x] `‎.ai/rules/15-config-and-secrets-separation.md` نوشته شد و اصل «secret در هیچ repo ای نباشد» در آن صریح است.
- [x] repo جداگانه‌ی `ai-workspace-config` ساخته شد و **هیچ secret ای در آن نیست** (فقط `.env.example` با نام متغیرها).

**Gateway و Registry**
- [x] مسیر Gateway (permission → validation → execution → audit) تعریف شد.
- [x] `capabilities.md` قابلیت `issue-tracking` را با primary=rovo و fallback=rest دارد.

**Jira**
- [x] `connection.md` بدونِ secret نوشته شد و توضیح‌گرِ اتصال در repo config است.
- [x] `mcp-remote` به نسخه‌ی مشخص pin شد.
- [x] سرور `jira-rest-fallback` با Python/FastMCP ساخته و در catalog ثبت شد.
- [x] provider رسمی Atlassian دست‌نخورده و به‌عنوان primary فعال است.

**ایمنی و تست**
- [x] fallback خواندنی خودکار کار می‌کند (منطق پیاده‌سازی شده، تست زنده ⏳ معلق).
- [x] fallback نوشتنی بدون تأیید انسان سوییچ نمی‌کند و idempotency دارد (منطق پیاده‌سازی شده، تست زنده ⏳ معلق).
- [x] `delete_issue` پیاده نشده؛ `set_backlog_rank` پاسخِ «Unsupported» می‌دهد.

**خودیادگیری و ثبت**
- [x] `create-new-mcp-server.md` با قید تأیید انسان نوشته شد.
- [x] `DECISIONS.md` (D1–D8) و `CURRENT.md` به‌روز شدند.
- [x] یک درس‌آموخته در `10-memory-and-lessons/` درباره‌ی این فاز ثبت شد.
