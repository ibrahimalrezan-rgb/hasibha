#!/usr/bin/env python3
"""
تحديث الصفحات الإنجليزية من العربية
يستخرج الحقول والسكربت كما هي، ويترجم فقط النصوص
"""

import os
import sys
import re
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ai_providers import get_provider

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


def load_config():
    with open(os.path.join(AUTOMATION_DIR, 'config.json'), 'r', encoding='utf-8') as f:
        return json.load(f)


def get_api_key(provider_name):
    if provider_name == "gemini":
        return os.environ.get("GEMINI_API_KEY")
    return None


def clean_ai_response(text):
    if not text:
        return ""
    text = text.strip()
    if text.startswith("```"):
        parts = text.split("```")
        if len(parts) >= 2:
            text = parts[1]
            if text.startswith("html"):
                text = text[4:]
            elif text.startswith("json"):
                text = text[4:]
    return text.strip()


def read_ar_page(slug):
    """يقرأ كل ما نحتاجه من الصفحة العربية"""
    path = os.path.join(ROOT_DIR, f"{slug}.html")
    if not os.path.exists(path):
        return None
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    result = {}
    
    # استخراج fields HTML كامل (كل ما بين subtitle و calc-btn)
    fields_match = re.search(
        r'<p class="subtitle">.*?</p>(.*?)<button class="calc-btn"',
        content, re.DOTALL
    )
    result['fields_html'] = fields_match.group(1).strip() if fields_match else ''
    
    # استخراج article-box
    article_match = re.search(
        r'<div class="article-box">(.*?)</div>\s*</div>\s*</main>',
        content, re.DOTALL
    )
    result['article'] = article_match.group(1).strip() if article_match else ''
    
    # استخراج السكربت الأخير
    scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
    script_found = ''
    for s in reversed(scripts):
        if 'function calculate' in s:
            script_found = s.strip()
            break
    result['script'] = script_found
    
    return result


def translate_article(ai, article_ar):
    if not article_ar:
        return ""
    
    prompt = f"""Translate this Arabic HTML article to English.

CRITICAL RULES:
1. Keep ALL HTML tags exactly: <h3>, <p>, <ul>, <li>, <div class="tip">
2. Translate only text content, NOT tags or class names
3. Keep numbers, URLs as-is
4. "ريال" → "SAR", "السعودية" → "Saudi Arabia", "حاسبها" → "Hasibha"
5. Do NOT add markdown or code blocks
6. Output ONLY the English HTML

Arabic HTML:
{article_ar}

English HTML:"""
    
    result = ai.generate(prompt, max_tokens=4000)
    return clean_ai_response(result)


def translate_fields_html(ai, fields_ar):
    """يترجم النصوص فقط في الحقول، ويحفظ البنية"""
    if not fields_ar:
        return ""
    
    # نترجم الكل دفعة واحدة
    prompt = f"""Translate the Arabic text in this HTML to English.

CRITICAL RULES:
1. Keep ALL HTML tags and attributes EXACTLY as they are
2. Translate ONLY the Arabic text content (in labels, placeholders, .slider-value, .labels)
3. Do NOT change: input types, ids, class names, min, max, value, step
4. "٪" stays "٪" or becomes "%" - keep consistent
5. "ريال" → "SAR", "سنة" → "years"
6. Do NOT add markdown or code blocks
7. Output ONLY the translated HTML

Arabic HTML:
{fields_ar}

English HTML:"""
    
    result = ai.generate(prompt, max_tokens=4000)
    return clean_ai_response(result)


def generate_en_page(ai, page):
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
    
    # ترجمة المقال
    print(f"  🤖 ترجمة المقال...")
    article_en = translate_article(ai, data['article'])
    print(f"  ✅ مقال ({len(article_en)} حرف)")
    
    # ترجمة الحقول
    print(f"  🤖 ترجمة الحقول...")
    fields_en = translate_fields_html(ai, data['fields_html'])
    print(f"  ✅ حقول ({len(fields_en)} حرف)")
    
    # الوصف
    desc_prompt = f"Write a short SEO meta description in English (140-160 chars) for: {page['title_en']}. Return ONLY the description."
    desc_en = clean_ai_response(ai.generate(desc_prompt, max_tokens=200))
    if not desc_en or len(desc_en) < 30:
        desc_en = f"Free online {page['title_en']}. Instant, accurate results - no registration required."
    
    # Schema
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
                "description": desc_en,
                "url": f"{SITE_URL}/{slug}-en",
                "applicationCategory": "UtilityApplication",
                "operatingSystem": "Any",
                "inLanguage": "en-US",
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "SAR"}
            }
        ]
    }
    
    # السكربت - نستخدم اللي في العربي كما هو (يشتغل بالإنجليزية تلقائياً)
    script = data['script']
    
    # نعدل بعض النصوص العربية في السكربت
    script = script.replace("'ريال'", "'SAR'")
    script = script.replace('"ريال"', '"SAR"')
    script = script.replace("' سنة'", "' years'")
    script = script.replace('" سنة"', '" years"')
    
    # نغير locale للأرقام
    script = script.replace("'ar-SA'", "'en-US'")
    script = script.replace('"ar-SA"', '"en-US"')
    
    # بناء الصفحة
    template = build_en_template(page, fields_en, article_en, desc_en, script, schema)
    
    output = f"{slug}-en.html"
    output_path = os.path.join(ROOT_DIR, output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"  ✅ تم إنشاء {output}")
    return output


def build_en_template(page, fields_html, article_html, desc, script, schema):
    """يبني صفحة إنجليزية كاملة"""
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
    <p class="subtitle">{desc}</p>

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


def main():
    config = load_config()
    
    ai = None
    if config.get('ai_enabled'):
        provider_name = config.get('ai_provider', 'gemini')
        api_key = get_api_key(provider_name)
        
        if api_key:
            try:
                ai = get_provider(provider_name, api_key, config.get('ai_model'))
                print(f"🤖 AI: {provider_name}")
            except Exception as e:
                print(f"⚠️ خطأ في AI: {e}")
                return
        else:
            print("⚠️ لا يوجد مفتاح API")
            return
    else:
        print("⚠️ AI معطل")
        return
    
    pages_to_update = PAGES
    if len(sys.argv) > 1 and sys.argv[1]:
        target = sys.argv[1]
        pages_to_update = [p for p in PAGES if p['slug'] == target]
        if not pages_to_update:
            print(f"⚠️ لم أجد صفحة: {target}")
            return
    
    print(f"📊 عدد الصفحات: {len(pages_to_update)}")
    
    for i, page in enumerate(pages_to_update, 1):
        print(f"\n[{i}/{len(pages_to_update)}] 🔨 {page['slug']}-en.html")
        try:
            generate_en_page(ai, page)
        except Exception as e:
            print(f"  ❌ خطأ: {e}")
    
    print("\n🎉 اكتمل!")


if __name__ == "__main__":
    main()
