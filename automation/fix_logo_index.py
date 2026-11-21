#!/usr/bin/env python3
"""
إضافة اللوقو لكل صفحات الموقع تلقائياً
يفحص كل ملفات HTML ويضيف اللوقو لأي صفحة ناقصة
"""
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO_HEADER = '<img src="/images/logo.png" alt="حاسبها" style="height:36px;vertical-align:middle">'
LOGO_FOOTER = '<img src="/images/logo.png" alt="حاسبها" style="height:28px;vertical-align:middle">'

fixed_count = 0
skipped_count = 0

# المشي على كل ملفات HTML في الريبو
for root, dirs, files in os.walk(ROOT_DIR):
    # تجاهل مجلدات معينة
    dirs[:] = [d for d in dirs if d not in ('.git', '.github', 'automation', 'node_modules')]
    
    for name in files:
        if not name.endswith('.html'):
            continue
        
        path = os.path.join(root, name)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # ============================================
        # 1) إصلاح روابط اللوقو في الهيدر والفوتر
        # ============================================
        # نبحث عن <a class="logo"...>...</a>
        # إذا ما فيه <img> داخله، نضيف اللوقو
        
        def fix_logo_link(match):
            open_tag = match.group(1)
            inner = match.group(2)
            close_tag = match.group(3)
            
            # إذا فيه img مسبقاً، اتركه كما هو
            if '<img' in inner:
                return match.group(0)
            
            # حدد إذا هذا هيدر أو فوتر حسب ارتفاع الصورة
            # الفوتر عادة فيه style="font-size:16px" أو emoji 🧮
            if 'font-size:16px' in open_tag or '🧮' in inner:
                logo_tag = LOGO_FOOTER
            else:
                logo_tag = LOGO_HEADER
            
            # أضف اللوقو قبل النص
            inner_clean = inner.strip()
            return f'{open_tag}\n      {logo_tag}\n      {inner_clean}\n    {close_tag}'
        
        content = re.sub(
            r'(<a\s+class="logo"[^>]*>)(.*?)(</a>)',
            fix_logo_link,
            content,
            flags=re.DOTALL
        )
        
        # ============================================
        # 2) إضافة favicon في الـ head إذا غير موجود
        # ============================================
        if '<link rel="icon"' not in content:
            # أضف بعد <meta charset="UTF-8"> أو بعد <head>
            if '<meta charset="UTF-8">' in content:
                content = content.replace(
                    '<meta charset="UTF-8">',
                    '<meta charset="UTF-8">\n<link rel="icon" type="image/png" href="/images/logo.png">\n<link rel="apple-touch-icon" href="/images/logo.png">',
                    1
                )
            elif '<head>' in content:
                content = content.replace(
                    '<head>',
                    '<head>\n<link rel="icon" type="image/png" href="/images/logo.png">\n<link rel="apple-touch-icon" href="/images/logo.png">',
                    1
                )
        
        # ============================================
        # حفظ الملف إذا تغير
        # ============================================
        if content != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ تم الإصلاح: {os.path.relpath(path, ROOT_DIR)}")
            fixed_count += 1
        else:
            skipped_count += 1

print(f"\n{'='*60}")
print(f"📊 النتيجة النهائية:")
print(f"  ✅ تم الإصلاح: {fixed_count}")
print(f"  ℹ️ ما يحتاج تعديل: {skipped_count}")
print(f"🎉 اكتمل!")
