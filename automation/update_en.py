#!/usr/bin/env python3
"""
تحديث الصفحات الإنجليزية من العربية - بدون AI
يستخدم Google Translate المجاني
"""

import os
import sys
import re
import json
import time
import urllib.parse
import urllib.request
from datetime import datetime

SITE_URL = "https://hasibha.com"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTOMATION_DIR = os.path.dirname(os.path.abspath(__file__))

PAGES = [
    {"slug": "mortgage", "title_en": "Mortgage Calculator", "category": "finance", "icon": "🏠"},
    {"slug": "personal-loan", "title_en": "Personal Loan Calculator", "category": "finance", "icon": "💵"},
    {"slug": "eos", "title_en": "End of Service Calculator", "category": "finance", "icon": "📋"},
    {"slug": "vat", "title_en": "VAT Calculator", "category": "finance", "icon": "🧾"},
    {"slug": "salary", "title_en": "Salary After Insurance", "category": "finance", "icon": "💼"},
    {"slug": "currency", "title_en": "Currency Converter", "category": "conversion", "icon": "💱"},
    {"slug": "length", "title_en": "Length Converter", "category": "conversion", "icon": "📏"},
    {"slug": "weight", "title_en": "Weight Converter", "category": "conversion", "icon": "⚖️"},
    {"slug": "area", "title_en": "Area Converter", "category": "conversion", "icon": "📐"},
    {"slug": "bmi", "title_en": "BMI Calculator", "category": "health", "icon": "🧍"},
    {"slug": "calorie", "title_en": "Calorie Calculator", "category": "health", "icon": "🍎"},
    {"slug": "water", "title_en": "Water Intake Calculator", "category": "health", "icon": "💧"},
    {"slug": "age", "title_en": "Age Calculator", "category": "general", "icon": "🎂"},
    {"slug": "discount", "title_en": "Discount Calculator", "category": "general", "icon": "🏷️"},
    {"slug": "date-diff", "title_en": "Date Difference Calculator", "category": "general", "icon": "📅"},
]


def translate_google(text):
    """يترجم باستخدام Google Translate المجاني"""
    if not text or not text.strip():
        return text
    
    # إذا النص طويل، نقسمه
    if len(text) > 4000:
        parts = []
        current = ""
        for line in text.split("\n"):
            if len(current) + len(line) < 3500:
                current += line + "\n"
            else:
                parts.append(current)
                current = line + "\n"
        if current:
            parts.append(current)
        
        translated_parts = []
        for part in parts:
            translated_parts.append(translate_google(part))
            time.sleep(0.5)
        return "\n".join(translated_parts)
    
    try:
        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=ar&tl=en&dt=t&q=" + urllib.parse.quote(text)
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            if data and data[0]:
                result = ""
                for item in data[0]:
                    if item[0]:
                        result += item[0]
                return result
    except Exception as e:
        print(f"    ⚠️ خطأ ترجمة: {e}")
    
    return text


def translate_html(html):
    """يترجم HTML مع الحفاظ على الوسوم"""
    if not html:
        return ""
    
    def replace_text(match):
        text = match.group(1)
        if not text.strip():
            return '>' + text + '<'
        leading = len(text) - len(text.lstrip())
        trailing = len(text) - len(text.rstrip())
        core = text.strip()
        if core:
            translated = translate_google(core)
            return '>' + ' ' * leading + translated + ' ' * trailing + '<'
        return '>' + text + '<'
    
    html = re.sub(r'>([^<>]+)<', replace_text, html)
    
    return html


def read_ar_page(slug):
    path = os.path.join(ROOT_DIR, f"{slug}.html")
    if not os.path.exists(path):
        return None
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    result = {}
    
    subtitle_match = re.search(r'<p class="subtitle">([^<]+)</p>', content)
    result['subtitle'] = subtitle_match.group(1).strip() if subtitle_match else ''
    
    start_match = re.search(r'</p>', content)
    end_match = re.search(r'<button class="calc-btn"', content)
    
    if start_match and end_match:
        start_pos = start_match.end()
        end_pos = end_match.start()
        result['fields_html'] = content[start_pos:end_pos].strip()
    else:
        result['fields_html'] = ''
    
    article_match = re.search(
        r'<div class="article-box">(.*?)</div>\s*</div>\s*</main>',
        content, re.DOTALL
    )
    result['article'] = article_match.group(1).strip() if article_match else ''
    
    scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
    all_scripts = []
    for s in scripts:
        if 'googletagmanager' in s or 'gtag' in s:
            continue
        if not s.strip():
            continue
        all_scripts.append(s.strip())
    
    result['script'] = '\n\n'.join(all_scripts)
    
    return result


def build_en_page(page, fields_html, article_html, subtitle, desc, script, schema):
    slug = page['slug']
    title = page['title_en']
    icon = page['icon']
    year = datetime.now().year
    
    return f'''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{title} - Hasibha</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{title}, free calculator, online calculator">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="Hasibha">
<link rel="canonical" href="{SITE_URL}/{slug}-en">
<link rel="icon" type="image/png" href="https://i.ibb.co/MyCPJW6y/B8947-E27-073-B-4-DE2-8-E7-F-EB2023-A17-E70.png">
<link rel="apple-touch-icon" href="https://i.ibb.co/MyCPJW6y/B8947-E27-073-B-4-DE2-8-E7-F-EB2023-A17-E70.png">
<link rel="alternate" hreflang="ar" href="{SITE_URL}/{slug}">
<link rel="alternate" hreflang="en" href="{SITE_URL}/{slug}-en">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}/{slug}">

<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE_URL}/{slug}-en">
<meta property="og:type" content="website">
<meta property="og:image" content="https://i.ibb.co/MyCPJW6y/B8947-E27-073-B-4-DE2-8-E7-F-EB2023-A17-E70.png">
<meta property="og:site_name" content="Hasibha">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://i.ibb.co/MyCPJW6y/B8947-E27-073-B-4-DE2-8-E7-F-EB2023-A17-E70.png">
<meta name="theme-color" content="#0b0d10">

<script async src="https://www.googletagmanager.com/gtag/js?id=G-NZLXJFVCDW"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-NZLXJFVCDW');</script>

<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=2)}
</script>

<link rel="stylesheet" href="/css/style.css">
</head>
<body>

<header class="site-header">
  <div class="wrap header-in">
    <a class="logo" href="/index-en" aria-label="Hasibha">
      <img src="https://i.ibb.co/MyCPJW6y/B8947-E27-073-B-4-DE2-8-E7-F-EB2023-A17-E70.png" alt="Hasibha" style="height:36px;vertical-align:middle">
      Hasibha
    </a>
    <nav class="main-nav" aria-label="Main navigation">
      <a href="/index-en#calculators">Calculators</a>
      <a href="/index-en#features">Features</a>
      <a href="/index-en#faq">FAQ</a>
    </nav>
    <div class="header-actions">
      <button class="theme-btn" id="themeBtn" aria-label="Theme">
        <svg id="iconMoon" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg>
        <svg id="iconSun" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="display:none"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
      </button>
      <a class="lang-btn" href="/{slug}" hreflang="ar" lang="ar">عربي</a>
    </div>
  </div>
</header>

<nav class="breadcrumb">
  <div class="wrap">
    <a href="/index-en">🏠 Home</a>
    <span>←</span>
    <span style="color:var(--text);font-weight:600">{title}</span>
  </div>
</nav>

<main>
<div class="wrap">
  <div class="calc-wrapper">
    <h1>{icon} {title}</h1>
    <p class="subtitle">{subtitle}</p>

{fields_html}

    <button class="calc-btn" onclick="calculate()">Calculate</button>

    <div class="result-card" id="resultCard">
    </div>

    <a href="/index-en" class="back-link">↩ Back to Home</a>
  </div>

  <div class="article-box">
{article_html}
  </div>
</div>
</main>

<footer class="site-footer">
  <div class="wrap footer-in">
    <a class="logo" href="/index-en" style="font-size:16px">
      <img src="https://i.ibb.co/MyCPJW6y/B8947-E27-073-B-4-DE2-8-E7-F-EB2023-A17-E70.png" alt="Hasibha" style="height:28px;vertical-align:middle">
      Hasibha
    </a>
    <nav aria-label="Footer">
      <a href="/privacy-en">Privacy Policy</a>
      <a href="/contact-en">Contact Us</a>
      <a href="/about-en">About Us</a>
    </nav>
    <p>Hasibha © {year} — All Rights Reserved</p>
  </div>
</footer>

<script>
(function(){{
  var root=document.documentElement, btn=document.getElementById('themeBtn');
  var moon=document.getElementById('iconMoon'), sun=document.getElementById('iconSun');
  function apply(t){{
    if(t==='dark'){{root.setAttribute('data-theme','dark');moon.style.display='none';sun.style.display='block';}}
    else{{root.removeAttribute('data-theme');moon.style.display='block';sun.style.display='none';}}
  }}
  var saved=null;
  try{{saved=localStorage.getItem('hs-theme');}}catch(e){{}}
  if(!saved){{saved=(window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'light';}}
  apply(saved);
  btn.addEventListener('click',function(){{
    var next=root.getAttribute('data-theme')==='dark'?'light':'dark';
    apply(next);
    try{{localStorage.setItem('hs-theme',next);}}catch(e){{}}
  }});
}})();

{script}
</script>
</body>
</html>
'''


def generate_en_page(page):
    slug = page['slug']
    print(f"  📖 قراءة {slug}.html...")
    
    data = read_ar_page(slug)
    if not data:
        print(f"  ⚠️ لم أجد {slug}.html")
        return None
    
    if not data['fields_html']:
        print(f"  ⚠️ لا توجد حقول")
        return None
    
    if not data['article']:
        print(f"  ⚠️ لا يوجد مقال")
        return None
    
    print(f"  📊 سكربت: {len(data['script'])} حرف، مقال: {len(data['article'])} حرف")
    
    print(f"  🌐 ترجمة العنوان...")
    subtitle_en = translate_google(data['subtitle']) if data['subtitle'] else "Calculate instantly with our free online tool."
    print(f"  ✅ {subtitle_en[:60]}...")
    
    print(f"  🌐 ترجمة المقال...")
    article_en = translate_html(data['article'])
    print(f"  ✅ مقال ({len(article_en)} حرف)")
    
    print(f"  🌐 ترجمة الحقول...")
    fields_en = translate_html(data['fields_html'])
    print(f"  ✅ حقول ({len(fields_en)} حرف)")
    
    script = data['script']
    script = script.replace("'ريال'", "'SAR'")
    script = script.replace('"ريال"', '"SAR"')
    script = script.replace("' سنة'", "' years'")
    script = script.replace("'ar-SA'", "'en-US'")
    script = script.replace('"ar-SA"', '"en-US"')
    script = script.replace("+ ' ريال'", "+ ' SAR'")
    script = script.replace("' ريال'", "' SAR'")
    
    desc = f"Free online {page['title_en']}. Instant, accurate results - no registration required."
    
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/index-en"},
                    {"@type": "ListItem", "position": 2, "name": page['title_en'], "item": f"{SITE_URL}/{slug}-en"}
                ]
            },
            {
                "@type": "WebApplication",
                "name": page['title_en'],
                "description": desc,
                "url": f"{SITE_URL}/{slug}-en",
                "applicationCategory": "UtilityApplication",
                "operatingSystem": "Any",
                "inLanguage": "en-US",
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "SAR"}
            }
        ]
    }
    
    html = build_en_page(page, fields_en, article_en, subtitle_en, desc, script, schema)
    
    output = f"{slug}-en.html"
    output_path = os.path.join(ROOT_DIR, output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"  ✅ تم إنشاء {output}")
    return output


def main():
    pages_to_update = PAGES
    if len(sys.argv) > 1 and sys.argv[1]:
        target = sys.argv[1]
        pages_to_update = [p for p in PAGES if p['slug'] == target]
        if not pages_to_update:
            print(f"⚠️ لم أجد صفحة: {target}")
            return
    
    print(f"📊 عدد الصفحات: {len(pages_to_update)}")
    print("🌐 استخدام Google Translate (بدون AI)")
    
    for i, page in enumerate(pages_to_update, 1):
        print(f"\n[{i}/{len(pages_to_update)}] 🔨 {page['slug']}-en.html")
        try:
            generate_en_page(page)
        except Exception as e:
            print(f"  ❌ خطأ: {e}")
    
    print("\n🎉 اكتمل!")


if __name__ == "__main__":
    main()
