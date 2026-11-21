#!/usr/bin/env python3
"""
إصلاح المقالات:
1) الشريط الأبيض بالوضع الداكن
2) لون الروابط الأزرق → أخضر مريح للعين
3) إصلاح الروابط المكسورة → تربط بالحاسبة الصحيحة
4) روابط تبديل اللغة
"""
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(ROOT_DIR, 'articles')

try:
    from config import PAGES
except ImportError:
    PAGES = []

DARK_FIX = '''
[data-theme="dark"] .breadcrumb{background:#161a21 !important;border-bottom-color:#262c36 !important;color:#6b7480 !important}
[data-theme="dark"] .breadcrumb a{color:#10b981 !important}
[data-theme="dark"] .breadcrumb span{color:#f3f4f6 !important}
[data-theme="dark"] .theme-btn,[data-theme="dark"] .lang-btn{background:#161a21 !important;border-color:#262c36 !important;color:#f3f4f6 !important}
[data-theme="dark"] .article-meta{color:#6b7480 !important}
.article a{color:#059669;text-decoration:underline;text-underline-offset:3px}
.article a:hover{color:#047857}
[data-theme="dark"] .article a{color:#4ade80 !important}
[data-theme="dark"] .article a:hover{color:#86efac !important}
'''

KNOWN_EXTRA = ['articles', 'index', 'index-en', 'privacy', 'privacy-en',
               'contact', 'contact-en', 'about', 'about-en', '']

def fix_links(html, is_en):
    known = [p['slug'] for p in PAGES]

    def repl(m):
        href = m.group(1).strip()
        text = m.group(2)
        plain = re.sub(r'<[^>]+>', '', text).strip()

        # 1) إذا نص الرابط يحتوي اسم حاسبة → اربطها مباشرة
        for p in PAGES:
            title = p['title_en'] if is_en else p['title_ar']
            if title and title in plain:
                target = f"/{p['slug']}-en" if is_en else f"/{p['slug']}"
                return f'<a href="{target}">{text}</a>'

        # 2) اترك الروابط الخارجية وروابط المقالات والصور
        if href.startswith('http') or href.startswith('/articles') or href.startswith('/images') or href.startswith('mailto'):
            return m.group(0)

        # 3) اترك مراسي جدول المحتويات
        if href.startswith('#'):
            return m.group(0)

        # 4) اترك الروابط الداخلية الصحيحة
        slug = href.strip('/').replace('.html', '')
        if slug in known or slug in KNOWN_EXTRA or (slug.endswith('-en') and slug[:-3] in known):
            return m.group(0)

        # 5) أي رابط مكسور آخر → لقسم الحاسبات
        home = "/index-en" if is_en else ""
        return f'<a href="{home}#calculators">{text}</a>'

    return re.sub(r'<a\s+href="([^"]*)">(.*?)</a>', repl, html, flags=re.DOTALL)

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

        # إضافة إصلاحات CSS مرة واحدة فقط
        if '.article a{' not in c:
            c = c.replace('</style>', DARK_FIX + '</style>', 1)

        # إصلاح الروابط
        c = fix_links(c, is_en)

        # روابط تبديل اللغة
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

print(f"\n✅ مقالات مُصلحة: {fixed}")
