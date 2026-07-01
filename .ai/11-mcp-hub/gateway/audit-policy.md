# Audit Policy

سیاست‌های مربوط به ثبت و ممیزی لاگ‌های سیستم Gateway.

## استانداردهای لاگ
هر فراخوانی ابزار باید اطلاعات زیر را ثبت کند:
- **Timestamp:** زمان دقیق اجرا
- **Caller Identity:** ایجنت یا پروسه فراخوانی‌کننده
- **Target Capability/Provider:** قابلیت هدف و پروایدری که انتخاب شده (Primary یا Fallback)
- **Action:** نام ابزار (مثلاً `get_issue`)
- **Outcome:** موفقیت، شکست یا سوئیچ به Fallback
- **Duration:** مدت زمان اجرا

## Rate Limiting & Circuit Breaker
- محدودیت‌های فراخوانی برای جلوگیری از Overload سرورهای خارجی.
- در صورت دریافت خطاهای متوالی (مثل 5xx)، Circuit Breaker فعال شده و مسیر دسترسی قطع می‌گردد، یا بر اساس پیکربندی fallback به سرویس پشتیبان سوییچ می‌شود.
