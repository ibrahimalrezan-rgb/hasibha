#!/usr/bin/env python3
"""
توليد sitemap.xml احترافي مع hreflang tags
"""

import os
from datetime import datetime
from config import PAGES, SITE_URL

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def generate_sitemap():
    """يولد sitemap.xml كامل مع hreflang tags"""
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    # الصفحات الثابتة
    static_pages = [
        {"url": "/", "priority": "1.0", "changefreq": "weekly"},
        {"url": "/index-en", "priority": "1.0", "changefreq": "weekly"},
        {"url": "/privacy", "priority": "0.3", "changefreq": "yearly"},
        {"url": "/privacy-en", "priority": "0.3", "changefreq": "yearly"},
        {"url": "/about", "priority": "0.3", "changefreq": "yearly"},
        {"url": "/about-en", "priority": "0.3", "changefreq": "yearly"},
        {"url": "/contact", "priority": "0.3", "changefreq": "yearly"},
        {"url": "/contact-en", "priority": "0.3", "changefreq": "yearly"},
    ]
    
    urls = []
    
    # الصفحات الثابتة
    for page in static_pages:
        url = f"{SITE_URL}{page['url']}"
        urls.append(f'''  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{page['changefreq']}</changefreq>
    <priority>{page['priority']}</priority>
  </url>''')
    
    # صفحات الحاسبات مع hreflang
    for page in PAGES:
        slug = page['slug']
        url_ar = f"{SITE_URL}/{slug}"
        url_en = f"{SITE_URL}/{slug}-en"
        
        # الصفحة العربية
        urls.append(f'''  <url>
    <loc>{url_ar}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <xhtml:link rel="alternate" hreflang="ar" href="{url_ar}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{url_en}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{url_ar}"/>
  </url>''')
        
        # الصفحة الإنجليزية
        urls.append(f'''  <url>
    <loc>{url_en}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <xhtml:link rel="alternate" hreflang="ar" href="{url_ar}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{url_en}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{url_ar}"/>
  </url>''')
    
    sitemap_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(urls)}
</urlset>'''
    
    return sitemap_xml

def generate_robots_txt():
    """يولد robots.txt"""
    return f'''User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml

# Disallow admin or private areas if any
# Disallow: /admin/
'''

def main():
    print("🗺️ توليد خريطة الموقع...")
    
    # sitemap.xml
    sitemap_xml = generate_sitemap()
    sitemap_path = os.path.join(ROOT_DIR, 'sitemap.xml')
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)
    print(f"  ✅ تم توليد sitemap.xml ({len(PAGES) * 2 + 8} URL)")
    
    # robots.txt
    robots_txt = generate_robots_txt()
    robots_path = os.path.join(ROOT_DIR, 'robots.txt')
    with open(robots_path, 'w', encoding='utf-8') as f:
        f.write(robots_txt)
    print(f"  ✅ تم توليد robots.txt")
    
    print("\n🎉 اكتمل!")

if __name__ == "__main__":
    main()
