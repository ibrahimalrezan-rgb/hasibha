#!/usr/bin/env python3
"""توليد النسخة الإنجليزية لكل مقال عربي موجود"""
import os
import re
import json
import time
import urllib.request
import urllib.error
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(ROOT_DIR, 'articles')
DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY', '')

CSS_EN = """
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:"Segoe UI",Tahoma,Arial,sans-serif;background:#f8fafc;color:#1e293b;line-height:1.7;text-align:left}
.wrap{max-width:800px;margin:0 auto;padding:0 20px}
.site-header{position:sticky;top:0;z-index:50;background:rgba(255,255,255,0.86);backdrop-filter:blur(10px);border-bottom:1px solid #e6e8eb}
.header-in{display:flex;align-items:center;gap:20px;height:60px}
.logo{display:flex;align-items:center;gap:8px;font-size:20px;font-weight:700;color:#0b0d10;text-decoration:none}
.logo img{height:35px}
.main-nav{display:flex;gap:4px;margin-inline-start:8px}
.main-nav a{padding:6px 12px;border-radius:8px;font-size:14px;color:#4b5563;text-decoration:none}
.main-nav a:hover{background:#f6f7f8}
.header-actions{margin-inline-start:auto;display:flex;gap:8px}
.lang-btn,.theme-btn{border:1px solid #e6e8eb;border-radius:8px;padding:6px 12px;font-size:13px;color:#0b0d10;background:#fff;text-decoration:none;cursor:pointer}
.breadcrumb{background:#fff;padding:12px 0;font-size:13px;color:#8b95a1;border-bottom:1px solid #e6e8eb}
.breadcrumb a{color:#059669;text-decoration:none}
.breadcrumb span{margin:0 4px}
.article{background:#fff;border:1px solid #e6e8eb;border-radius:16px;padding:40px 32px;margin:30px auto;line-height:1.9;text-align:left}
.article h1{font-size:28px;color:#064e3b;margin-bottom:16px;border-bottom:3px solid #059669;padding-bottom:16px}
.article-meta{color:#8b95a1;font-size:13px;margin-bottom:32px;display:flex;gap:16px;flex-wrap:wrap}
.article h2{font-size:22px;color:#064e3b;margin:32px 0 16px;padding-bottom:8px;border-bottom:2px solid #059669}
.article h3{font-size:18px;color:#1e293b;margin:24px 0 12px}
.article p{color:#4b5563;font-size:16px;margin-bottom:16px}
.article ul,.article ol{color:#4b5563;padding-left:24px;margin-bottom:16px}
.article li{margin-bottom:8px}
.article strong{color:#0b0d10}
.article em{color:#059669;font-style:normal}
.article table{width:100%;border-collapse:collapse;margin:16px 0}
.article th,.article td{border:1px solid #e6e8eb;padding:12px;text-align:left}
.article th{background:#f0fdf4;color:#064e3b;font-weight:700}
.cta-box{background:#f0fdf4;border:2px solid #059669;border-radius:16px;padding:24px;margin:32px 0;text-align:center}
.cta-box h3{color:#064e3b;margin-bottom:12px}
.cta-box p{color:#4b5563;margin-bottom:16px}
.cta-btn{display:inline-block;background:#059669;color:#fff;padding:14px 32px;border-radius:12px;text-decoration:none;font-weight:700;font-size:16px}
.site-footer{border-top:1px solid #e6e8eb;padding:32px 0;margin-top:24px;background:#fff;text-align:center;color:#8b95a1;font-size:13px}
.footer-in{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}
.footer-in nav{display:flex;gap:18px}
.footer-in a{color:#8b95a1;text-decoration:none}
[data-theme="dark"] body{background:#0e1116;color:#f3f4f6}
[data-theme="dark"] .site-header{background:rgba(14,17,22,0.86);border-bottom-color:#262c36}
[data-theme="dark"] .logo,[data-theme="dark"] .article h1,[data-theme="dark"] .article h2,[data-theme="dark"] .article h3,[data-theme="dark"] .article strong{color:#f3f4f6}
[data-theme="dark"] .main-nav a,[data-theme="dark"] .article p,[data-theme="dark"] .article ul,[data-theme="dark"] .article ol,[data-theme="dark"] .article li{color:#aab3bf}
[data-theme="dark"] .article,[data-theme="dark"] .site-footer,[data-theme="dark"] .breadcrumb{background:#161a21;border-color:#262c36;color:#6b7480}
[data-theme="dark"] .breadcrumb a{color:#10b981}
[data-theme="dark"] .breadcrumb span{color:#f3f4f6}
[data-theme="dark"] .article th{background:rgba(5,150,105,0.16);color:#f3f4f6}
[data-theme="dark"] .article td{border-color:#262c36}
[data-theme="dark"] .cta-box{background:rgba(5,150,105,0.1);border-color:#10b981}
[data-theme="dark"] .cta-box h3,[data-theme="dark"] .cta-box p{color:#f3f4f6}
[data-theme="dark"] .theme-btn,[data-theme="dark"] .lang-btn{background:#161a21;border-color:#262c36;color:#f3f4f6}
@media(max-width:720px){.main-nav{display:none}.article{padding:24px 16px}.article h1{font-size:22px}.article h2{font-size:18px}}
"""

def call_deepseek(prompt, max_tokens=8000, max_retries=3):
    if not DEEPSEEK_API_KEY:
        return None
    url = "https://api.deepseek.com/chat/completions"
    for attempt in range(max_retries):
        try:
            data = json.dumps({
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": "You are a professional translator specialized in Saudi finance and health content."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.4,
                "max_tokens": max_tokens
            }).encode('utf-8')
            req = urllib.request.Request(url, data=data, headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
            })
            with urllib.request.urlopen(req, timeout=180) as response:
                result = json.loads(response.read().decode('utf-8'))
                if 'choices' in result and result['choices']:
                    return result['choices'][0]['message']['content']
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(30 * (attempt + 1))
                continue
            print(f"    ⚠️ خطأ {e.code}")
            break
        except Exception as e:
            print(f"    ⚠️ {e}")
            if attempt < max_retries - 1:
                time.sleep(10)
    return None

def translate(text, max_tokens=8000):
    if not text:
        return None
    prompt = f"""Translate the following Arabic content to English.
- If it contains HTML tags, keep ALL tags exactly as they are and translate only the visible text between them.
- Use professional, natural English suitable for a Saudi audience.
- Return ONLY the translated result, no explanations.

{text}"""
    r = call_deepseek(prompt, max_tokens)
    if r:
        r = r.strip()
        if r.startswith('```html'): r = r[7:]
        if r.startswith('```'): r = r[3:]
        if r.endswith('```'): r = r[:-3]
        return r.strip()
    return None

def build_en_article(ar_slug, en_slug, title_en, desc_en, content_en, calc_slug, calc_title_en, date_pub):
    year = datetime.now().year
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title_en,
        "description": desc_en,
        "author": {"@type": "Organization", "name": "Hasibha"},
        "datePublished": date_pub,
        "inLanguage": "en-US",
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"https://hasibha.com/articles/{en_slug}"}
    }
    return f'''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_en} | Hasibha</title>
<meta name="description" content="{desc_en}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://hasibha.com/articles/{en_slug}">
<link rel="alternate" hreflang="ar" href="https://hasibha.com/articles/{ar_slug}">
<link rel="alternate" hreflang="en" href="https://hasibha.com/articles/{en_slug}">
<link rel="icon" type="image/png" href="/images/logo.png">
<link rel="preload" as="image" href="/images/logo.png">
<meta property="og:title" content="{title_en}">
<meta property="og:description" content="{desc_en}">
<meta property="og:type" content="article">
<meta property="og:url" content="https://hasibha.com/articles/{en_slug}">
<meta property="og:image" content="https://hasibha.com/images/logo.png">
<meta name="theme-color" content="#0b0d10">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4842993238012462" crossorigin="anonymous"></script>
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=2)}
</script>
<style>
{CSS_EN}
</style>
</head>
<body>
<header class="site-header">
<div class="wrap header-in">
<a class="logo" href="/index-en">
<img src="/images/logo.png" alt="Hasibha">
Hasibha
</a>
<nav class="main-nav">
<a href="/index-en#calculators">Calculators</a>
<a href="/articles/index-en">Articles</a>
<a href="/index-en#faq">FAQ</a>
</nav>
<div class="header-actions">
<button class="theme-btn" onclick="toggleTheme()" aria-label="Theme">🌓</button>
<a class="lang-btn" href="/articles/{ar_slug}">عربي</a>
</div>
</div>
</header>
<nav class="breadcrumb">
<div class="wrap">
<a href="/index-en">🏠 Home</a>
<span>←</span>
<a href="/articles/index-en">Articles</a>
<span>←</span>
<span style="color:#0b0d10;font-weight:600">{title_en[:45]}</span>
</div>
</nav>
<main>
<div class="wrap">
<article class="article">
<h1>{title_en}</h1>
<div class="article-meta">
<span>📅 {date_pub}</span>
<span>✍️ Hasibha Team</span>
<span>⏱️ 10 min read</span>
</div>
{content_en}
<div class="cta-box">
<h3>🎯 Try the {calc_title_en}</h3>
<p>Calculate everything accurately in seconds — free, no registration</p>
<a href="/{calc_slug}" class="cta-btn">Open Calculator ←</a>
</div>
</article>
</div>
</main>
<footer class="site-footer">
<div class="wrap footer-in">
<a class="logo" href="/index-en" style="font-size:16px">
<img src="/images/logo.png" alt="Hasibha" style="height:28px">
🧮 Hasibha
</a>
<nav>
<a href="/privacy-en">Privacy</a>
<a href="/contact-en">Contact</a>
<a href="/about-en">About</a>
</nav>
<p>Hasibha © {year} — All Rights Reserved</p>
</div>
</footer>
<script>
function toggleTheme(){{var r=document.documentElement,t=r.getAttribute('data-theme')==='dark'?'light':'dark';if(t==='dark')r.setAttribute('data-theme','dark');else r.removeAttribute('data-theme');try{{localStorage.setItem('hs-theme',t);}}catch(e){{}}}}
(function(){{var t=null;try{{t=localStorage.getItem('hs-theme');}}catch(e){{}}if(!t)t=(matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'light';if(t==='dark')document.documentElement.setAttribute('data-theme','dark');}})();
</script>
</body>
</html>
'''

def main():
    if not DEEPSEEK_API_KEY:
        print("❌ DEEPSEEK_API_KEY غير موجود")
        return
    os.makedirs(ARTICLES_DIR, exist_ok=True)
    
    for name in sorted(os.listdir(ARTICLES_DIR)):
        if not name.endswith('.html') or name.startswith('index') or name[:-5].endswith('-en'):
            continue
        ar_slug = name[:-5]
        en_slug = ar_slug + '-en'
        en_path = os.path.join(ARTICLES_DIR, en_slug + '.html')
        if os.path.exists(en_path):
            print(f"⏭️ {en_slug} موجود مسبقاً")
            continue
        
        with open(os.path.join(ARTICLES_DIR, name), 'r', encoding='utf-8') as f:
            c = f.read()
        
        h1 = re.search(r'<h1>(.*?)</h1>', c)
        desc_m = re.search(r'<meta name="description" content="([^"]*)"', c)
        date_m = re.search(r'"datePublished":"([^"]*)"', c)
        body_m = re.search(r'<div class="article-meta">.*?</div>\s*(.*?)\s*<div class="cta-box">', c, re.DOTALL)
        calc_m = re.search(r'<a href="/([a-z0-9-]+)" class="cta-btn">', c)
        calc_title_m = re.search(r'<h3>🎯 جرّب (.*?)</h3>', c)
        
        if not (h1 and body_m):
            print(f"⚠️ {name}: تعذر استخراج المحتوى")
            continue
        
        print(f"\n🌐 ترجمة: {ar_slug}")
        title_en = translate(h1.group(1), 300)
        desc_en = translate(desc_m.group(1) if desc_m else h1.group(1), 400)
        content_en = translate(body_m.group(1), 8000)
        calc_title_en = translate(calc_title_m.group(1) if calc_title_m else 'Calculator', 200)
        
        if not content_en:
            print("    ❌ فشل الترجمة")
            continue
        
        html = build_en_article(
            ar_slug, en_slug,
            title_en or h1.group(1),
            desc_en or desc_m.group(1) if desc_m else '',
            content_en,
            calc_m.group(1) if calc_m else '',
            calc_title_en or 'Calculator',
            date_m.group(1) if date_m else datetime.now().strftime("%Y-%m-%d")
        )
        
        with open(en_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"    ✅ تم إنشاء {en_slug}.html")
        time.sleep(3)
    
    print("\n🎉 اكتملت الترجمة!")

if __name__ == "__main__":
    main()
