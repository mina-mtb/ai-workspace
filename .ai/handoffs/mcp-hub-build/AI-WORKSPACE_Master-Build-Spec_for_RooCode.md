# سند ساخت جامع (Master Build Spec) برای Roo Code
### رهبرِ ارکستر: همه‌ی تصمیم‌ها + قانون جدید Config/Secrets + ترتیب ساخت + چک‌لیست بازبینی

> این سند «چهارمین و اصلی‌ترین» سند اجراست. سه سند دیگر پیوستِ آن‌اند. Roo Code باید **این سند را به‌عنوان ترتیبِ ساخت** دنبال کند و برای جزئیات به سه سند دیگر رجوع کند:
> 1. `AI-WORKSPACE_Master-Reference_and_Backup` (چرایی و بک‌آپ دستاوردها)
> 2. `AI-WORKSPACE_MCP-Hub_Handoff_for_RooCode` (ساختِ بانک MCP)
> 3. `Addendum_JiraProvider-Contract_and_Language` (قرارداد Jira + زبان)
> 4. **این سند** (ترتیب ساخت + قانون جدید + معیار پذیرش)

---

## بخش ۰ — قوانین بنیادی (که کل ساخت باید رعایت کند)
- main همیشه پایدار؛ push مستقیم ممنوع؛ هر تغییر از مسیر Pull Request؛ هر PR باید checkها را پاس کند.
- تغییر معماری فقط با ثبت ADR در `‎.ai/state/DECISIONS.md`.
- هیچ سرور MCP بدون عبور از Gateway/Broker فراخوانی نمی‌شود (permission → validation → execution → audit).
- **هیچ Secret در هیچ repo ای نباید commit شود** (قانون کامل در بخش ۲).
- Self-learning مستقیم ممنوع؛ ساختِ خودکارِ ابزار در نقاط حساس نیازمند تأیید انسان.

---

## بخش ۱ — دفترچه‌ی تصمیم‌های قطعی (Decision Ledger)
این‌ها را در `‎.ai/state/DECISIONS.md` به‌صورت ADR ثبت کن:

| # | تصمیم | وضعیت |
|---|---|---|
| D1 | بانک MCP یک لایه‌ی مرکزی مشترک است: `‎.ai/11-mcp-hub/` (نه پروژه‌ی جدا). | قطعی |
| D2 | هر سرور MCP پشت Gateway/Broker با permission، validation، audit، rate limit. | قطعی |
| D3 | سرورهای MCP دست‌سازِ ما با **Python (FastMCP)**؛ بانک چندزبانه است (سرورهای آماده‌ی بیرونی به هر زبانی مجازند). | قطعی |
| D4 | Jira: سرور رسمی **Atlassian Rovo MCP = primary**؛ سرور دست‌سازِ Python/REST = **fallback**. | قطعی |
| D5 | Fallback خواندنی خودکار؛ fallback نوشتنی فقط با idempotency + تأیید انسان + circuit breaker. | قطعی |
| D6 | نسخه‌ی `mcp-remote` باید pin شود (نه `@latest`). | قطعی |
| D7 | **قانون تفکیک Config/Secrets:** هر پروژه (و خودِ workspace) یک repo کد + یک repo config جدا؛ secret فقط در secret manager/`.env` لوکالِ gitignore‌شده. | قطعی (جدید) |
| D8 | لایه‌های آینده: سرور MCP برای Obsidian، و Telegram Gateway — فعلاً ساخته نمی‌شوند (بخش ۸). | برنامه‌ریزی‌شده |

---

## بخش ۲ — قانون جدید: تفکیک Config و Secrets (کامل)
**این قانون را به‌صورت فایل `‎.ai/rules/15-config-and-secrets-separation.md` بساز.** این قانون هم برای خودِ workspace و هم برای **هر پروژه‌ای که بعداً زیر آن ساخته می‌شود** اجباری است.

### ۲.۱. اصل امنیتی درست
جدا کردن config امنیت را از سه راه بالا می‌برد: کنترل دسترسیِ جدا (blast radius کوچک)، سخت‌تر شدنِ نشتِ تصادفیِ secret، و audit تمیزتر. اما **secret واقعی نباید در هیچ repo ای (حتی repo جدا) commit شود**؛ در تاریخِ git می‌ماند.

### ۲.۲. سه‌لایه‌ی طبقه‌بندی
- **Tier A — config حساس‌نبودهٔ کوپله با کد** (ساختار، defaultها، فلگ‌ها): می‌تواند کنار کد بماند.
- **Tier B — config محیط/دیپلوی/اتصال بدونِ secret** (تنظیمات هر محیط، توضیح‌گر اتصال، IaC): در **repo جداگانه‌ی config** با دسترسیِ محدودتر.
- **Tier C — secretها** (token، password، OAuth): فقط در **secret manager** یا `.env` لوکالِ **gitignore‌شده**. تنها فایل env که commit می‌شود `.env.example` است (فقط نام متغیرها، بدون مقدار).

### ۲.۳. ساختار repoها
- workspace مرکزی: یک repo کد (همین `ai-workspace`) + یک repo config جدا با نام `ai-workspace-config`.
- هر پروژه: `‎<project>` (کد) + `‎<project>-config` (config محیط/دیپلوی، بدون secret).
- قرارداد نام‌گذاری: پسوند `-config` برای repo تنظیمات.

### ۲.۴. کنترل و پایداری
- RBAC: repo config دسترسیِ محدودتر از repo کد دارد (least privilege).
- همه‌ی تغییرات config از مسیر PR و audit.
- **Secret scanning** در CI برای هر دو repo فعال باشد + `.gitignore` سخت‌گیرانه برای `.env`.
- **Reproduگزاری:** توضیح‌گرِ اتصال (endpoint، Cloud ID، scopeها، **نامِ** env variableها بدون مقدار، دستور دقیق اجرا) در repo config مستند شود تا انتقال به ماشین/agent دیگر بدون افشای secret ممکن باشد.

### ۲.۵. مدیریت secret (تصمیم عملی)
- **فاز فعلی (تک‌کاربر، لوکال):** `.env` لوکالِ gitignore‌شده کافی است.
- **هنگام رفتن روی VPS/چنددستگاهی:** به یک secret manager مهاجرت شود (گزینه‌ی سبک و git-friendly: **SOPS + age** برای secretهای رمزنگاری‌شده؛ یا یک secret manager میزبانی‌شده). این ارتقا بعداً انجام می‌شود، اما قانون از الان طوری نوشته می‌شود که مسیرش باز باشد.

### ۲.۶. اثر فوری روی Jira
- توضیح‌گرِ اتصال Rovo MCP (endpoint، Cloud ID، سایت، scopeها، نامِ env variableها، دستور pin‌شده) → به `ai-workspace-config` منتقل/مستند شود.
- توکن REST مربوط به provider fallback → در secret manager/`.env` لوکال؛ هرگز در repo.

---

## بخش ۳ — ساختار نهایی که باید ساخته شود

```text
ai-workspace/                         # repo کد (موجود)
├── .ai/
│   ├── 00-universal/ ... 10-memory-and-lessons/   # لایه‌های موجود
│   ├── 11-mcp-hub/                   # ★ بانک MCP (طبق سند Handoff)
│   │   ├── README.md
│   │   ├── registry/{catalog.md, capabilities.md}
│   │   ├── gateway/{broker-config.md, permissions.md, audit-policy.md}
│   │   ├── servers/
│   │   │   ├── system/{filesystem/, db-sqlite-postgres/}
│   │   │   ├── cloud/
│   │   │   │   ├── github/
│   │   │   │   └── jira/
│   │   │   │       ├── manifest.md
│   │   │   │       ├── connection.md        # توضیح‌گر بدون secret (اشاره به repo config)
│   │   │   │       ├── fallback.md
│   │   │   │       └── server/              # کد سرور fallback (Python/FastMCP)
│   │   │   └── custom/
│   │   ├── templates/mcp-server-python-template/   # مبنای همه‌ی سرورهای دست‌ساز
│   │   ├── workflows/create-new-mcp-server.md      # خودیادگیریِ gated (بخش ۵)
│   │   └── config/mcp_settings.reference.json
│   ├── rules/15-config-and-secrets-separation.md   # ★ قانون جدید
│   └── state/{DECISIONS.md (به‌روز), CURRENT.md (به‌روز)}
│
└── (کد)

ai-workspace-config/                  # ★ repo جدید config (بدون secret)
├── environments/{local.md, staging.md, prod.md}
├── connections/jira.md               # توضیح‌گر کامل اتصال Jira (بدون مقدار secret)
├── .env.example                      # فقط نام متغیرها
└── README.md
```

برای پروژه‌های آینده، template پوشه‌ی `.project-ai/` باید این‌ها را هم داشته باشد:
- `selected-mcp-servers.md` (کدام سرورهای بانک در این پروژه مجازند — least privilege).
- اشاره به repo config جداگانه‌ی همان پروژه (`‎<project>-config`).

---

## بخش ۴ — Jira (خلاصه‌ی اجرایی؛ جزئیات در Addendum)
- قابلیت `issue-tracking` در `registry/capabilities.md` با دو provider ثبت شود:
  - `jira-rovo-mcp` (primary، رسمی Atlassian، OAuth).
  - `jira-rest-fallback` (fallback، Python/FastMCP روی REST v3).
- interface ثابت (get/search/create/edit/transition/comment/worklog/...) طبق Addendum بخش ۳.۳.
- سیاست READ خودکار / WRITE محافظت‌شده طبق Addendum بخش ۴.
- `connection.md` بدونِ secret + pin کردن `mcp-remote`.
- `delete_issue` عمداً پیاده نشود؛ `set_backlog_rank` با پرچمِ «Unsupported» پاسخ دهد.

---

## بخش ۵ — خودیادگیری (workflow `create-new-mcp-server`) — gated
`‎.ai/11-mcp-hub/workflows/create-new-mcp-server.md` بساز با این منطق:
1. Orchestrator تشخیص می‌دهد ابزارِ لازم در `catalog.md` نیست.
2. از روی `templates/mcp-server-python-template/` یک سرور scaffold می‌شود.
3. سرور پشت Gateway ثبت و `manifest.md` + permission نوشته می‌شود.
4. **در نقاط حساس (شبکه، دیتابیس production، secret، عملیات مخرب) تأیید انسان اجباری است.**
5. بعد از تست، به `catalog.md` اضافه می‌شود.
6. اگر تکرارشونده بود، «crystallize» و درس‌آموخته در `10-memory-and-lessons/` ثبت شود.
7. Curator وضعیت سرورها را بین Active/Stale/Archive می‌چرخاند تا از تورمِ ابزار جلوگیری شود.

---

## بخش ۶ — ترتیب ساخت (Build Order)
1. **پایه:** اسکلت `‎.ai/11-mcp-hub/` با تمام زیرپوشه‌ها + README کوتاه در هرکدام.
2. **قانون جدید:** فایل `‎.ai/rules/15-config-and-secrets-separation.md` (بخش ۲).
3. **repo config:** ساختِ `ai-workspace-config` با ساختار بخش ۳ (بدون هیچ secret).
4. **Gateway:** `gateway/broker-config.md`، `permissions.md`، `audit-policy.md`.
5. **Registry:** `capabilities.md` (قابلیت `issue-tracking` با دو provider) + `catalog.md`.
6. **Template:** `templates/mcp-server-python-template/` (FastMCP، حداقلی و قابل‌اجرا).
7. **Jira — توضیح‌گر و pin:** `connection.md`، `manifest.md`، `fallback.md` + pin کردن `mcp-remote` + انتقال توضیح‌گر اتصال به repo config.
8. **Jira — سرور fallback:** ساخت `jira-rest-fallback` با Python/FastMCP از روی template.
9. **workflow خودیادگیری:** `create-new-mcp-server.md` (بخش ۵).
10. **ثبت وضعیت:** به‌روزرسانی `DECISIONS.md` (D1–D8) و `CURRENT.md`.
11. **تست‌ها:** health_check هر دو provider؛ تست سوییچِ READ (primary خاموش → fallback)؛ تست عدم‌سوییچِ WRITE.

هر گام در یک Branch جدا و از مسیر PR.

---

## بخش ۷ — Definition of Done + چک‌لیست بازبینی
> این چک‌لیست معیارِ من برای بررسیِ نتیجه‌ی نهایی است. لطفاً هر مورد را که انجام شد، در گزارشِ بازگشتی علامت بزن.

**ساختار و قانون**
- [ ] `‎.ai/11-mcp-hub/` با ساختار کامل ساخته شد.
- [ ] `‎.ai/rules/15-config-and-secrets-separation.md` نوشته شد و اصل «secret در هیچ repo ای نباشد» در آن صریح است.
- [ ] repo جداگانه‌ی `ai-workspace-config` ساخته شد و **هیچ secret ای در آن نیست** (فقط `.env.example` با نام متغیرها).

**Gateway و Registry**
- [ ] مسیر Gateway (permission → validation → execution → audit) تعریف شد.
- [ ] `capabilities.md` قابلیت `issue-tracking` را با primary=rovo و fallback=rest دارد.

**Jira**
- [ ] `connection.md` بدونِ secret نوشته شد و توضیح‌گرِ اتصال در repo config است.
- [ ] `mcp-remote` به نسخه‌ی مشخص pin شد.
- [ ] سرور `jira-rest-fallback` با Python/FastMCP ساخته و در catalog ثبت شد.
- [ ] provider رسمی Atlassian دست‌نخورده و به‌عنوان primary فعال است.

**ایمنی و تست**
- [ ] fallback خواندنی خودکار کار می‌کند (تست شد).
- [ ] fallback نوشتنی بدون تأیید انسان سوییچ نمی‌کند (تست شد) و idempotency/circuit-breaker دارد.
- [ ] `delete_issue` پیاده نشده؛ `set_backlog_rank` پاسخِ «Unsupported» می‌دهد.

**خودیادگیری و ثبت**
- [ ] `create-new-mcp-server.md` با قید تأیید انسان نوشته شد.
- [ ] `DECISIONS.md` (D1–D8) و `CURRENT.md` به‌روز شدند.
- [ ] یک درس‌آموخته در `10-memory-and-lessons/` درباره‌ی این فاز ثبت شد.

**گزارش بازگشتی برای بازبینی من شامل:** درختِ نهاییِ ساخته‌شده، محتوای `capabilities.md` و `15-config-and-secrets-separation.md`، و نتیجه‌ی سه تست (READ fallback، WRITE no-switch، health_check).

---

## بخش ۸ — چیزهایی که فعلاً **نساز** (تا scope منفجر نشود)
- سرور MCP برای Obsidian (فاز آینده).
- Telegram Gateway (فاز آینده).
- سرورهای system/cloud اضافی (filesystem, github, db) — فقط پوشه‌ی خالی با README؛ ساختشان فاز بعدی است.
- مهاجرت به secret manager (فعلاً `.env` لوکال؛ قانون مسیرش را باز گذاشته).

> اصل نهایی: ساده و کم‌دامنه شروع کن، اما همه‌چیز versioned، tested، secure، auditable و rollbackable.
