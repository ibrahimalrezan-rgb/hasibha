#!/usr/bin/env python3
"""
إضافة رمز AdSense لإثبات الملكية لكل صفحات الموقع
يعمل على كل ملفات HTML الموجودة + يتجنب التكرار
"""
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# رمز AdSense الخاص بك
ADSENSE_CODE = '''<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4842993238012462" crossorigin="anonymous"></script>'''

fixed_count = 0
skipped_count = 0
error_count = 0

# المشي على كل ملفات HTML
for root, dirs, files in os.walk(ROOT_DIR):
    dirs[:] = [d for d in dirs if d not in ('.git', '.github', 'automation', 'node_modules')]
    
    for name in files:
        if not name.endswith('.html'):
            continue
        
        path = os.path.join(root, name)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"⚠️ خطأ في قراءة {name}: {e}")
            error_count += 1
            continue
        
        original = content
        
        # ============================================
        # التحقق من وجود الرمز مسبقاً
        # ============================================
        if 'ca-pub-4842993238012462' in content:
            skipped_count += 1
            continue
        
        # ============================================
        # إضافة الرمز قبل </head> مباشرة
        # ============================================
        if '</head>' in content:
            # أضف قبل </head>
            content = content.replace(
                '</head>',
                f'\n{ADSENSE_CODE}\n</head>',
                1
            )
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ تم إضافة AdSense: {os.path.relpath(path, ROOT_DIR)}")
            fixed_count += 1
        else:
            print(f"⚠️ لم أجد </head> في: {name}")
            error_count += 1

print(f"\n{'='*60}")
print(f"📊 النتيجة النهائية:")
print(f"  ✅ تم الإضافة: {fixed_count}")
print(f"  ℹ️ موجود مسبقاً: {skipped_count}")
print(f"  ⚠️ أخطاء: {error_count}")
print(f"🎉 اكتمل!")
