#!/usr/bin/env python3
"""إصلاح المقالات الموجودة: الشريط الأبيض بالداكن + روابط تبديل اللغة"""
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(ROOT_DIR, 'articles')

DARK_FIX = '''
[data-theme="dark"] .breadcrumb{background:#161a21 !important;border-bottom-color:#262c36 !important;color:#6b7480 !important}
[data-theme="dark"] .breadcrumb a{color:#10b981 !important}
[data-theme="dark"] .breadcrumb span{color:#f3f4f6 !important}
[data-theme="dark"] .theme-btn,[data-theme="dark"] .lang-btn{background:#161a21 !important;border-color:#262c36 !important;color:#f3f4f6 !important}
[data-theme="dark"] .article-meta{color:#6b7480 !important}
'''

fixed = 0
if os.path.exists(ARTICLES_DIR):
    for name in sorted(os.listdir(ARTICLES_DIR)):
        if not name.endswith('.html'):
            continue
        path = os.path.join(ARTICLES_DIR, name)
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        orig = c
        is_en = name[:-5].endswith('-en')

        if '[data-theme="dark"] .breadcrumb' not in c:
            c = c.replace('</style>', DARK_FIX + '</style>', 1)

        if is_en:
            ar_slug = name[:-len('-en.html')]
            c = c.replace('<a class="lang-btn" href="/index">عربي</a>', f'<a class="lang-btn" href="/articles/{ar_slug}">عربي</a>')
            c = c.replace('<a class="lang-btn" href="/index-en">عربي</a>', f'<a class="lang-btn" href="/articles/{ar_slug}">عربي</a>')
        else:
            en_slug = name[:-5] + '-en'
            if os.path.exists(os.path.join(ARTICLES_DIR, en_slug + '.html')):
                c = c.replace('<a class="lang-btn" href="/index-en">EN</a>', f'<a class="lang-btn" href="/articles/{en_slug}">EN</a>')

        if c != orig:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"✅ {name}")
            fixed += 1
        else:
            print(f"⏭️ {name}")

print(f"\n✅ مُصلح: {fixed}")
