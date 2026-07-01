# Jira Server Connection

این فایل تنها یک ارجاع به پیکربندی‌های ذخیره‌شده در ریپازیتوری جداگانه‌ی تنظیمات است و هیچ Secretی را در خود نگه نمی‌دارد.

## ارجاع به پیکربندی
تمامی اطلاعات اتصال (شامل endpointها، متغیرهای محیطی موردنیاز، و شناسه کلود) در فایل زیر مستند شده‌اند:
`../../../ai-workspace-config/connections/jira.md`

## دستور اجرای Primary Provider (Rovo MCP)
دستور پین‌شده و ایمن برای اجرای سرور رسمی:
```bash
npx -y mcp-remote@0.1.38 https://mcp.atlassian.com/v1/mcp/authv2
```
