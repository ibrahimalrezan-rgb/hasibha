#!/usr/bin/env python3
"""
تحديث فهرس المقالات + استدعاء توليد الـ sitemap
ينشئ المجلد تلقائياً إذا لم يكن موجوداً
"""

import os
import re
import subprocess
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(ROOT_DIR, 'articles')

# إنشاء المجلد إذا لم يكن موجوداً
os.makedirs(ARTICLES_DIR, exist_ok=True)

# ============================================
# جمع كل المقالات
# ============================================
articles = []
for name in os.listdir(ARTICLES_DIR):
    if name.endswith('.html') and name != 'index.html':
        path = os.path.join(ARTICLES_DIR, name)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        title = re.search(r'<title>(.*?)</title>', content)
        desc = re.search(r'<meta name="description" content="([^"]*)"', content)
        date = re.search(r'"datePublished":"([^"]*)"', content)
        category = re.search(r'<span style="font-size:12px;color:var\(--text-3\)">([^<]*)</span>', content)
        
        if title:
            articles.append({
                "slug": name.replace('.html', ''),
                "title": title.group(1).replace(' | حاسبها', ''),
                "desc": desc.group(1)[:120] + '...' if desc else '',
                "date": date.group(1) if date else '',
                "category": category.group(1) if category else '📄 عام'
            })

articles.sort(key=lambda x: x['date'], reverse=True)

# ============================================
# بناء بطاقات المقالات
# ============================================
cards = ""
for a in articles:
    cards += f'''<a class="article-card" href="/articles/{a['slug']}">
<span class="date">{a['category']} • {a['date']}</span>
<h3>{a['title']}</h3>
<p>{a['desc']}</p>
<span class="read-more">اقرأ المقال ←</span>
</a>
'''

# ============================================
# بناء صفحة الفهرس
# ============================================
html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>المقالات | حاسبها — دليلك المالي والصحي الشامل</title>
<meta name="description" content="مقالات شاملة عن الزكاة، التمويل العقاري، مكافأة نهاية الخدمة، ضريبة القيمة المضافة والمزيد.">
<link rel="icon" type="image/png" href="/images/logo.png">
<link rel="preload" as="image" href="/images/logo.png">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:"Segoe UI",Tahoma,"Noto Kufi Arabic",sans-serif;background:#f8fafc;color:#1e293b;line-height:1.7}}
.wrap{{max-width:1060px;margin:0 auto;padding:0 20px}}
.site-header{{position:sticky;top:0;z-index:50;background:rgba(255,255,255,0.86);backdrop-filter:blur(10px);border-bottom:1px solid #e6e8eb}}
.header-in{{display:flex;align-items:center;gap:20px;height:60px}}
.logo{{display:flex;align-items:center;gap:8px;font-size:20px;font-weight:700;color:#0b0d10;text-decoration:none}}
.logo img{{height:35px}}
.main-nav{{display:flex;gap:4px;margin-inline-start:8px}}
.main-nav a{{padding:6px 12px;border-radius:8px;font-size:14px;color:#4b5563;text-decoration:none}}
.main-nav a:hover{{background:#f6f7f8}}
.header-actions{{margin-inline-start:auto;display:flex;gap:8px}}
.theme-btn,.lang-btn{{border:1px solid #e6e8eb;border-radius:8px;padding:6px 12px;font-size:13px;cursor:pointer;background:#fff;text-decoration:none;color:#0b0d10}}
.hero{{padding:60px 0 40px;text-align:center;background:linear-gradient(135deg,#ecfdf5,#f0fdf4)}}
.hero h1{{font-size:38px;font-weight:800;color:#064e3b;margin-bottom:12px}}
.hero p{{color:#4b5563;font-size:18px;max-width:600px;margin:0 auto}}
.articles-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;padding:40px 0}}
.article-card{{background:#fff;border:1px solid #e6e8eb;border-radius:16px;padding:24px;text-decoration:none;color:#1e293b;transition:.25s;display:flex;flex-direction:column;gap:12px}}
.article-card:hover{{border-color:#059669;transform:translateY(-3px);box-shadow:0 8px 24px rgba(5,150,105,0.12)}}
.article-card .date{{font-size:12px;color:#8b95a1}}
.article-card h3{{font-size:18px;font-weight:700;color:#064e3b;line-height:1.4}}
.article-card p{{font-size:14px;color:#4b5563;line-height:1.6}}
.article-card .read-more{{margin-top:auto;color:#059669;font-weight:600;font-size:14px}}
.site-footer{{border-top:1px solid #e6e8eb;padding:32px 0;margin-top:24px;background:#fff;text-align:center;color:#8b95a1;font-size:13px}}
[data-theme="dark"] body{{background:#0e1116;color:#f3f4f6}}
[data-theme="dark"] .site-header{{background:rgba(14,17,22,0.86);border-color:#262c36}}
[data-theme="dark"] .hero{{background:linear-gradient(135deg,#0e1116,#12151b)}}
[data-theme="dark"] .article-card,.site-footer{{background:#161a21;border-color:#262c36}}
[data-theme="dark"] .article-card h3{{color:#10b981}}
[data-theme="dark"] .article-card p{{color:#aab3bf}}
@media(max-width:600px){{.hero h1{{font-size:28px}}.articles-grid{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<header class="site-header">
<div class="wrap header-in">
<a class="logo" href="/">
<img src="/images/logo.png" alt="حاسبها">
حاسبها
</a>
<nav class="main-nav">
<a href="/#calculators">الحاسبات</a>
<a href="/articles" style="color:#059669;font-weight:600">المقالات</a>
<a href="/#faq">الأسئلة</a>
</nav>
<div class="header-actions">
<button class="theme-btn" onclick="toggleTheme()">🌓</button>
<a class="lang-btn" href="/index-en">EN</a>
</div>
</div>
</header>
<section class="hero">
<h1>📚 مكتبة حاسبها</h1>
<p>دليلك الشامل للحاسبات المالية والصحية في السعودية</p>
</section>
<main class="wrap">
<div class="articles-grid">
{cards if cards else '<p style="grid-column:1/-1;text-align:center;padding:40px;color:#8b95a1">لا توجد مقالات بعد — قريباً!</p>'}
</div>
</main>
<footer class="site-footer">
<p>حاسبها © {datetime.now().year} — جميع الحقوق محفوظة</p>
</footer>
<script>
function toggleTheme(){{var r=document.documentElement,t=r.getAttribute('data-theme')==='dark'?'light':'dark';if(t==='dark')r.setAttribute('data-theme','dark');else r.removeAttribute('data-theme');try{{localStorage.setItem('hs-theme',t);}}catch(e){{}}}}
(function(){{var t=null;try{{t=localStorage.getItem('hs-theme');}}catch(e){{}}if(!t)t=(matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'light';if(t==='dark')document.documentElement.setAttribute('data-theme','dark');}})();
</script>
</body>
</html>
'''

with open(os.path.join(ARTICLES_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ تم تحديث فهرس المقالات ({len(articles)} مقال)")

# ============================================
# استدعاء توليد الـ sitemap تلقائياً
# ============================================
sitemap_script = os.path.join(ROOT_DIR, 'automation', 'generate_sitemap.py')
if os.path.exists(sitemap_script):
    print("🔄 تحديث sitemap.xml تلقائياً...")
    subprocess.run(['python', sitemap_script], check=True)
