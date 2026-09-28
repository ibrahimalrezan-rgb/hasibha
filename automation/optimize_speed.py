#!/usr/bin/env python3
"""
السرعة v2:
1) دمج CSS داخل كل صفحة (إلغاء حظر العرض)
2) نقل AdSense + GTM لنهاية body (بعد المحتوى)
3) preload للوقو
"""
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS_PATH = os.path.join(ROOT_DIR, 'css', 'style.css')

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    CSS = f.read().strip()

LINK_TAG = '<link rel="stylesheet" href="/css/style.css">'
INLINE_TAG = '<style>\n' + CSS + '\n</style>'

ADSENSE_RE = re.compile(
    r'[ \t]*<script async src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=ca-pub-4842993238012462"[^>]*></script>\s*'
)

GTM_RE = re.compile(
    r'[ \t]*<script async src="https://www\.googletagmanager\.com/gtag/js\?id=G-NZLXJFVCDW"></script>\s*'
    r'(?:<script>window\.dataLayer[\s\S]*?</script>\s*)?'
)

PRELOAD = '<link rel="preload" as="image" href="/images/logo.png">'

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
        
        # 1) دمج CSS داخل الصفحة
        if LINK_TAG in content:
            content = content.replace(LINK_TAG, INLINE_TAG, 1)
        
        # 2) نقل AdSense + GTM لنهاية body
        moved = []
        def collect(m):
            moved.append(m.group(0).strip())
            return ''
        content = ADSENSE_RE.sub(collect, content)
        content = GTM_RE.sub(collect, content)
        if moved and '</body>' in content:
            block = '\n' + '\n'.join(moved) + '\n'
            content = content.replace('</body>', block + '</body>', 1)
        
        # 3) preload للوقو
        if PRELOAD not in content and '/images/logo.png' in content:
            content = content.replace(
                '<meta charset="UTF-8">',
                '<meta charset="UTF-8">\n' + PRELOAD,
                1
            )
        
        if content != orig:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {os.path.relpath(path, ROOT_DIR)}")
            fixed += 1

print(f"\n✅ صفحات معدّلة: {fixed}")
print("🎉 اكتمل!")
