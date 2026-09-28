#!/usr/bin/env python3
"""
السرعة v3:
1) حذف @import للخطوط من style.css (السبب الرئيسي لحظر العرض)
2) إعادة دمج CSS النظيف داخل كل الصفحات (حتى القديمة المدمجة سابقاً)
3) إضافة width/height للوقو
"""
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS_PATH = os.path.join(ROOT_DIR, 'css', 'style.css')

# ============================================
# 1) تنظيف style.css من @import
# ============================================
with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css = f.read()

css_clean = re.sub(r"@import\s+url\([^)]*\);?\s*", "", css)
css_clean = re.sub(r"@import\s+['\"][^'\"]*['\"];?\s*", "", css_clean)

if css_clean != css:
    with open(CSS_PATH, 'w', encoding='utf-8') as f:
        f.write(css_clean)
    print("✅ تم حذف @import من style.css")

CSS = css_clean.strip()
INLINE_TAG = '<style>\n' + CSS + '\n</style>'
LINK_TAG = '<link rel="stylesheet" href="/css/style.css">'

# نمط الـ style القديم المدمج (يبدأ بـ @import)
OLD_INLINE_RE = re.compile(r'<style>\s*@import[\s\S]*?</style>')

fixed = 0

for root, dirs, files in os.walk(ROOT_DIR):
    dirs[:] = [d for d in dirs if d not in ('.git',)]
    for name in files:
        if not name.endswith('.html'):
            continue
        
        path = os.path.join(root, name)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        orig = content
        
        # 2) إعادة دمج CSS النظيف
        if LINK_TAG in content:
            content = content.replace(LINK_TAG, INLINE_TAG, 1)
        elif OLD_INLINE_RE.search(content):
            content = OLD_INLINE_RE.sub(INLINE_TAG, content, count=1)
        
        # 3) إضافة أبعاد اللوقو (يمنع CLS)
        if 'width="54"' not in content:
            content = content.replace(
                'style="height:36px;vertical-align:middle"',
                'width="54" height="36" style="height:36px;vertical-align:middle"'
            )
        if 'width="42"' not in content:
            content = content.replace(
                'style="height:28px;vertical-align:middle"',
                'width="42" height="28" style="height:28px;vertical-align:middle"'
            )
        
        if content != orig:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {os.path.relpath(path, ROOT_DIR)}")
            fixed += 1

print(f"\n✅ صفحات معدّلة: {fixed}")
print("🎉 اكتمل!")
