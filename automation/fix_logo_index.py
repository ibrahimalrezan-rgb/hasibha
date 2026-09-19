#!/usr/bin/env python3
"""
إضافة اللوقو للصفحات الرئيسية (index.html و index-en.html)
والصفحات الثابتة (privacy, contact, about) ونسخها الإنجليزية
"""
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO_TAG = '<img src="/images/logo.png" alt="حاسبها" style="height:36px;vertical-align:middle">\n      '
LOGO_TAG_FOOTER = '<img src="/images/logo.png" alt="حاسبها" style="height:28px;vertical-align:middle">\n      '

# الصفحات التي تحتاج إصلاح
pages_to_fix = [
    'index.html',
    'index-en.html',
    'privacy.html',
    'privacy-en.html',
    'contact.html',
    'contact-en.html',
    'about.html',
    'about-en.html',
]

fixed_count = 0

for page in pages_to_fix:
    path = os.path.join(ROOT_DIR, page)
    if not os.path.exists(path):
        print(f"⚠️ {page} غير موجود")
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # فحص: هل يحتوي على class="logo" لكن بدون img داخله؟
    # نبحث عن <a class="logo"...>  ثم نص مباشر (بدون <img)
    # Header: <a class="logo" href="...">نص</a>
    # Footer: <a class="logo" href="...">🧮 نص</a>
    
    # نمط الهيدر: <a class="logo" href="..."> نص بدون img </a>
    # نتحقق من أن ما بين > و </a> لا يحتوي على <img
    
    def fix_logo_links(html, logo_tag):
        # البحث عن كل روابط اللوقو
        pattern = r'(<a\s+class="logo"\s+href="[^"]*">)(.*?)(</a>)'
        
        def replacer(match):
            open_tag = match.group(1)
            inner = match.group(2)
            close_tag = match.group(3)
            
            # إذا كان هناك img مسبقاً، اتركه
            if '<img' in inner:
                return match.group(0)
            
            # إذا ما فيه img، أضف اللوقو قبل النص
            return open_tag + '\n      ' + logo_tag + inner.strip() + '\n    ' + close_tag
        
        return re.sub(pattern, replacer, html, flags=re.DOTALL)
    
    # إصلاح روابط اللوقو في الهيدر (height: 36px)
    content = fix_logo_links(content, LOGO_TAG)
    
    # إضافة favicon في head إذا غير موجود
    if '/images/logo.png' not in content and '<link rel="icon"' not in content:
        # إضافة بعد <head> مباشرة
        content = content.replace(
            '<head>',
            '<head>\n<link rel="icon" type="image/png" href="/images/logo.png">\n<link rel="apple-touch-icon" href="/images/logo.png">',
            1
        )
    
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ تم إصلاح: {page}")
        fixed_count += 1
    else:
        print(f"ℹ️ {page}: ما يحتاج تعديل")

print(f"\n🎉 عدد الملفات المُصلحة: {fixed_count}")
