#!/usr/bin/env python3
"""توليد sitemap.xml شامل: حاسبات + مقالات (ar + en) + صفحات ثابتة"""
import os
import re
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(ROOT_DIR, 'articles')
SITE_URL = "https://hasibha.com"
TODAY = datetime.now().strftime("%Y-%m-%d")

urls = []

def add_url(loc, priority, changefreq="weekly", lastmod=None):
    urls.append({"loc": loc, "priority": priority, "changefreq": changefreq, "lastmod": lastmod or TODAY})

# الرئيسية
add_url(f"{SITE_URL}/", "1.0", "daily")
add_url(f"{SITE_URL}/index-en", "0.9", "daily")

# الثابتة
for slug, pr in [("privacy","0.5"),("privacy-en","0.4"),("contact","0.5"),("contact-en","0.4"),("about","0.5"),("about-en","0.4")]:
    add_url(f"{SITE_URL}/{slug}", pr, "monthly")

# الحاسبات
try:
    from config import PAGES
except ImportError:
    PAGES = []
for page in PAGES:
    add_url(f"{SITE_URL}/{page['slug']}", "0.9", "weekly")
    add_url(f"{SITE_URL}/{page['slug']}-en", "0.8", "weekly")

# المقالات (ar + en)
ar_count = en_count = 0
if os.path.exists(ARTICLES_DIR):
    add_url(f"{SITE_URL}/articles/", "0.8", "weekly")
    add_url(f"{SITE_URL}/articles/index-en", "0.7", "weekly")
    for name in os.listdir(ARTICLES_DIR):
        if not name.endswith('.html') or name.startswith('index'):
            continue
        slug = name[:-5]
        lastmod = TODAY
        try:
            with open(os.path.join(ARTICLES_DIR, name), 'r', encoding='utf-8') as f:
                dm = re.search(r'"datePublished":"([^"]*)"', f.read())
            if dm:
                lastmod = dm.group(1)
        except Exception:
            pass
        pr = "0.8" if not slug.endswith('-en') else "0.7"
        add_url(f"{SITE_URL}/articles/{slug}", pr, "weekly", lastmod)
        if slug.endswith('-en'):
            en_count += 1
        else:
            ar_count += 1

lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    lines.append('  <url>')
    lines.append(f'    <loc>{u["loc"]}</loc>')
    lines.append(f'    <lastmod>{u["lastmod"]}</lastmod>')
    lines.append(f'    <changefreq>{u["changefreq"]}</changefreq>')
    lines.append(f'    <priority>{u["priority"]}</priority>')
    lines.append('  </url>')
lines.append('</urlset>')

with open(os.path.join(ROOT_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"✅ sitemap.xml: {len(urls)} رابط (مقالات ar: {ar_count} | en: {en_count})")
