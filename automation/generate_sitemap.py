 #!/usr/bin/env python3
"""
توليد sitemap.xml شامل:
- كل صفحات الحاسبات (عربي + إنجليزي)
- كل المقالات
- الصفحات الثابتة
"""

import os
import re
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(ROOT_DIR, 'articles')
SITE_URL = "https://hasibha.com"
TODAY = datetime.now().strftime("%Y-%m-%d")

urls = []

def add_url(loc, priority, changefreq="weekly", lastmod=None):
    urls.append({
        "loc": loc,
        "priority": priority,
        "changefreq": changefreq,
        "lastmod": lastmod or TODAY
    })

# ============================================
# 1) الصفحات الرئيسية
# ============================================
add_url(f"{SITE_URL}/", "1.0", "daily")
add_url(f"{SITE_URL}/index-en", "0.9", "daily")

# ============================================
# 2) الصفحات الثابتة
# ============================================
static_pages = [
    ("privacy", "0.5"), ("privacy-en", "0.4"),
    ("contact", "0.5"), ("contact-en", "0.4"),
    ("about", "0.5"), ("about-en", "0.4"),
]
for slug, priority in static_pages:
    add_url(f"{SITE_URL}/{slug}", priority, "monthly")

# ============================================
# 3) صفحات الحاسبات (عربي + إنجليزي)
# ============================================
try:
    from config import PAGES
except ImportError:
    PAGES = []
    # fallback: قراءة من الملفات الموجودة
    for name in os.listdir(ROOT_DIR):
        if name.endswith('.html') and not name.startswith('index'):
            slug = name.replace('.html', '')
            if slug.endswith('-en'):
                continue
            PAGES.append({"slug": slug})

for page in PAGES:
    slug = page['slug']
    add_url(f"{SITE_URL}/{slug}", "0.9", "weekly")
    add_url(f"{SITE_URL}/{slug}-en", "0.8", "weekly")

# ============================================
# 4) المقالات (جديد!)
# ============================================
articles_count = 0
if os.path.exists(ARTICLES_DIR):
    add_url(f"{SITE_URL}/articles/", "0.8", "weekly")
    
    for name in os.listdir(ARTICLES_DIR):
        if name.endswith('.html') and name != 'index.html':
            slug = name.replace('.html', '')
            path = os.path.join(ARTICLES_DIR, name)
            
            # استخراج تاريخ النشر
            lastmod = TODAY
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                date_match = re.search(r'"datePublished":"([^"]*)"', content)
                if date_match:
                    lastmod = date_match.group(1)
            except:
                pass
            
            add_url(f"{SITE_URL}/articles/{slug}", "0.8", "weekly", lastmod)
            articles_count += 1

# ============================================
# 5) بناء ملف XML
# ============================================
xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
xml_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for u in urls:
    xml_lines.append('  <url>')
    xml_lines.append(f'    <loc>{u["loc"]}</loc>')
    xml_lines.append(f'    <lastmod>{u["lastmod"]}</lastmod>')
    xml_lines.append(f'    <changefreq>{u["changefreq"]}</changefreq>')
    xml_lines.append(f'    <priority>{u["priority"]}</priority>')
    xml_lines.append('  </url>')

xml_lines.append('</urlset>')

sitemap_path = os.path.join(ROOT_DIR, 'sitemap.xml')
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(xml_lines))

print(f"✅ تم توليد sitemap.xml")
print(f"   📊 إجمالي الروابط: {len(urls)}")
print(f"   📝 منها مقالات: {articles_count}")
print(f"   🧮 صفحات الحاسبات: {len(PAGES) * 2}")
print(f"   📄 صفحات ثابتة: {len(static_pages) + 2}")
