#!/usr/bin/env python3
"""
توليد صفحات index.html و index-en.html تلقائياً
"""

import os
import sys
from datetime import datetime
from config import PAGES, CATEGORIES, SITE_URL, SITE_NAME, SITE_NAME_EN

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def generate_cards_html(pages, lang='ar'):
    """يولد HTML للبطاقات بلغة معينة"""
    is_ar = lang == 'ar'
    cta_text = "احسب الآن ←" if is_ar else "Calculate Now ←"
    cta_conv = "حوّل الآن ←" if is_ar else "Convert Now ←"
    
    html_parts = []
    for page in pages:
        title = page['title_ar'] if is_ar else page['title_en']
        desc = page['desc_ar'] if is_ar else page['desc_en']
        slug = page['slug'] if is_ar else f"{page['slug']}-en"
        cta = cta_conv if page['category'] == 'conversion' else cta_text
        
        html_parts.append(f'''<a class="card {page['category']}" href="/{slug}" data-cat="{page['category'][:3] if page['category'] != 'finance' else 'fin'}" data-title="{title} {desc}">
<span class="card-icon">{page['icon']}</span>
<div><h3>{title}</h3><p>{desc}</p></div>
<span class="card-cta">{cta}</span>
</a>''')
    
    return '\n'.join(html_parts)

def generate_arabic_index():
    """يولد index.html بالعربية"""
    cards_html = generate_cards_html(PAGES, 'ar')
    year = datetime.now().year
    
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{SITE_NAME} | حاسبات مالية وصحية مجانية للسوق السعودي</title>
<meta name="description" content="{SITE_NAME} — منصة الحاسبات السعودية الأولى: تمويل عقاري، تمويل شخصي، نهاية الخدمة، ضريبة القيمة المضافة، الزكاة، الذهب وأكثر. نتائج فورية ومجانية 100%.">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="hasibha">
<link rel="canonical" href="{SITE_URL}/">
<link rel="alternate" hreflang="ar" href="{SITE_URL}/">
<link rel="alternate" hreflang="en" href="{SITE_URL}/index-en">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}/">
<link rel="icon" type="image/png" href="https://i.ibb.co/MyCPJW6y/B8947-E27-073-B-4-DE2-8-E7-F-EB2023-A17-E70.png">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NZLXJFVCDW"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-NZLXJFVCDW');</script>
<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<header class="site-header">
<div class="wrap header-in">
<a class="logo" href="/" aria-label="{SITE_NAME}">
<img src="https://i.ibb.co/MyCPJW6y/B8947-E27-073-B-4-DE2-8-E7-F-EB2023-A17-E70.png" alt="{SITE_NAME}" style="height:36px;vertical-align:middle">
{SITE_NAME}
</a>
<nav class="main-nav" aria-label="التنقل الرئيسي">
<a href="#calculators">الحاسبات</a>
<a href="#features">المميزات</a>
<a href="#faq">الأسئلة الشائعة</a>
</nav>
<div class="header-actions">
<button class="theme-btn" id="themeBtn" aria-label="تبديل الوضع الليلي">
<svg id="iconMoon" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg>
<svg id="iconSun" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="display:none"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
</button>
<a class="lang-btn" href="/index-en" hreflang="en" lang="en">EN</a>
</div>
</div>
</header>
<main>
<section class="hero wrap">
<span class="badge"><span class="dot"></span> نتائج فورية · بدون تسجيل · خصوصية تامة</span>
<h1>احسبها صحّ… في ثوانٍ</h1>
<p class="lead">كل حاسباتك المالية والصحية واليومية في مكان واحد — مصممة خصيصًا للسوق السعودي وبنظامه.</p>
<div class="stats" aria-label="إحصائيات المنصة">
<div class="stat"><b>{len(PAGES)}+</b><span>حاسبة مجانية</span></div>
<div class="stat"><b>{len(CATEGORIES)}</b><span>تصنيفات رئيسية</span></div>
<div class="stat"><b>عربي / EN</b><span>دعم كامل للغتين</span></div>
<div class="stat"><b>100%</b><span>مجاني للأبد</span></div>
</div>
</section>
<section class="calc-section wrap" id="calculators">
<div class="section-head">
<h2>تصفح الحاسبات</h2>
</div>
<div class="tabs" role="tablist" aria-label="تصنيفات الحاسبات">
<button class="tab on" role="tab" aria-selected="true" data-cat="all">الكل</button>
<button class="tab" role="tab" aria-selected="false" data-cat="fin">مالية</button>
<button class="tab" role="tab" aria-selected="false" data-cat="conv">تحويلات</button>
<button class="tab" role="tab" aria-selected="false" data-cat="health">صحة</button>
<button class="tab" role="tab" aria-selected="false" data-cat="gen">عامة</button>
</div>
<div class="grid" id="cardsGrid">
{cards_html}
</div>
</section>
<section class="features wrap" id="features">
<div class="section-head"><h2>لماذا {SITE_NAME}؟</h2></div>
<div class="features-grid">
<div class="feature"><b>دقة موثوقة</b><span>معادلات محدثة بما يتوافق مع الأنظمة السعودية.</span></div>
<div class="feature"><b>خصوصية تامة</b><span>كل الحسابات تتم داخل متصفحك.</span></div>
<div class="feature"><b>نتائج فورية</b><span>بدون تسجيل أو إعلانات مزعجة.</span></div>
<div class="feature"><b>مصمم للسعودية</b><span>نسب التمويل والتأمينات بنظام المملكة.</span></div>
</div>
</section>
<section class="faq wrap" id="faq">
<div class="section-head"><h2>الأسئلة الشائعة</h2></div>
<details open><summary>هل حاسبات {SITE_NAME} مجانية؟</summary><p class="faq-a">نعم، جميع الحاسبات مجانية 100% وبدون تسجيل.</p></details>
<details><summary>هل يتم حفظ بياناتي؟</summary><p class="faq-a">لا. جميع الحسابات تتم داخل متصفحك بالكامل.</p></details>
<details><summary>هل الحاسبات مخصصة للسوق السعودي؟</summary><p class="faq-a">نعم، صممت وفق الأنظمة السعودية.</p></details>
</section>
</main>
<footer class="site-footer">
<div class="wrap footer-in">
<a class="logo" href="/" style="font-size:16px">
<img src="https://i.ibb.co/MyCPJW6y/B8947-E27-073-B-4-DE2-8-E7-F-EB2023-A17-E70.png" alt="{SITE_NAME}" style="height:28px;vertical-align:middle">
{SITE_NAME}
</a>
<nav aria-label="روابط الفوتر">
<a href="/privacy">سياسة الخصوصية</a>
<a href="/contact">تواصل معنا</a>
<a href="/about">من نحن</a>
</nav>
<p>{SITE_NAME} © {year} — جميع الحقوق محفوظة</p>
</div>
</footer>
<script>
(function(){{var root=document.documentElement,btn=document.getElementById('themeBtn');var moon=document.getElementById('iconMoon'),sun=document.getElementById('iconSun');function apply(t){{if(t==='dark'){{root.setAttribute('data-theme','dark');moon.style.display='none';sun.style.display='block';}}else{{root.removeAttribute('data-theme');moon.style.display='block';sun.style.display='none';}}}}var saved=null;try{{saved=localStorage.getItem('hs-theme');}}catch(e){{}}if(!saved){{saved=(window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'light';}}apply(saved);btn.addEventListener('click',function(){{var next=root.getAttribute('data-theme')==='dark'?'light':'dark';apply(next);try{{localStorage.setItem('hs-theme',next);}}catch(e){{}}}});}})();
(function(){{var tabs=document.querySelectorAll('.tab');var cards=document.querySelectorAll('#cardsGrid .card');var curCat='all';function render(){{cards.forEach(function(c){{var okCat=(curCat==='all'||c.dataset.cat===curCat);c.style.display=okCat?'':'none';}});}}tabs.forEach(function(t){{t.addEventListener('click',function(){{curCat=t.dataset.cat;tabs.forEach(function(x){{x.classList.remove('on');x.setAttribute('aria-selected','false');}});t.classList.add('on');t.setAttribute('aria-selected','true');render();}});}});render();}})();
</script>
</body>
</html>'''

def generate_english_index():
    """يولد index-en.html بالإنجليزية"""
    cards_html = generate_cards_html(PAGES, 'en')
    year = datetime.now().year
    
    return f'''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{SITE_NAME_EN} | Free Financial & Health Calculators</title>
<meta name="description" content="{SITE_NAME_EN} — The #1 Saudi calculators platform: mortgage, personal loan, end of service, VAT, Zakat, gold and more. Instant results, 100% free.">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="hasibha">
<link rel="canonical" href="{SITE_URL}/index-en">
<link rel="alternate" hreflang="ar" href="{SITE_URL}/">
<link rel="alternate" hreflang="en" href="{SITE_URL}/index-en">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}/">
<link rel="icon" type="image/png" href="https://i.ibb.co/MyCPJW6y/B8947-E27-073-B-4-DE2-8-E7-F-EB2023-A17-E70.png">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NZLXJFVCDW"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-NZLXJFVCDW');</script>
<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<header class="site-header">
<div class="wrap header-in">
<a class="logo" href="/index-en" aria-label="{SITE_NAME_EN}">
<img src="https://i.ibb.co/MyCPJW6y/B8947-E27-073-B-4-DE2-8-E7-F-EB2023-A17-E70.png" alt="{SITE_NAME_EN}" style="height:36px;vertical-align:middle">
{SITE_NAME_EN}
</a>
<nav class="main-nav" aria-label="Main navigation">
<a href="#calculators">Calculators</a>
<a href="#features">Features</a>
<a href="#faq">FAQ</a>
</nav>
<div class="header-actions">
<button class="theme-btn" id="themeBtn" aria-label="Toggle dark mode">
<svg id="iconMoon" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg>
<svg id="iconSun" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="display:none"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
</button>
<a class="lang-btn" href="/" hreflang="ar" lang="ar">عربي</a>
</div>
</div>
</header>
<main>
<section class="hero wrap">
<span class="badge"><span class="dot"></span> Instant results · No registration · Complete privacy</span>
<h1>Calculate it right… in seconds</h1>
<p class="lead">All your financial, health, and daily calculators in one place — designed for the Saudi market.</p>
<div class="stats" aria-label="Platform statistics">
<div class="stat"><b>{len(PAGES)}+</b><span>Free calculators</span></div>
<div class="stat"><b>{len(CATEGORIES)}</b><span>Main categories</span></div>
<div class="stat"><b>Arabic / EN</b><span>Full bilingual support</span></div>
<div class="stat"><b>100%</b><span>Free forever</span></div>
</div>
</section>
<section class="calc-section wrap" id="calculators">
<div class="section-head">
<h2>Browse Calculators</h2>
</div>
<div class="tabs" role="tablist" aria-label="Calculator categories">
<button class="tab on" role="tab" aria-selected="true" data-cat="all">All</button>
<button class="tab" role="tab" aria-selected="false" data-cat="fin">Finance</button>
<button class="tab" role="tab" aria-selected="false" data-cat="conv">Converters</button>
<button class="tab" role="tab" aria-selected="false" data-cat="health">Health</button>
<button class="tab" role="tab" aria-selected="false" data-cat="gen">General</button>
</div>
<div class="grid" id="cardsGrid">
{cards_html}
</div>
</section>
<section class="features wrap" id="features">
<div class="section-head"><h2>Why {SITE_NAME_EN}?</h2></div>
<div class="features-grid">
<div class="feature"><b>Trusted Accuracy</b><span>Updated formulas aligned with Saudi regulations.</span></div>
<div class="feature"><b>Complete Privacy</b><span>All calculations happen in your browser.</span></div>
<div class="feature"><b>Instant Results</b><span>No registration, no annoying ads.</span></div>
<div class="feature"><b>Designed for Saudi</b><span>Financing rates and GOSI for the Kingdom.</span></div>
</div>
</section>
<section class="faq wrap" id="faq">
<div class="section-head"><h2>Frequently Asked Questions</h2></div>
<details open><summary>Are {SITE_NAME_EN} calculators free?</summary><p class="faq-a">Yes, all calculators are 100% free with no registration required.</p></details>
<details><summary>Is my data saved?</summary><p class="faq-a">No. All calculations are performed entirely in your browser.</p></details>
<details><summary>Are calculators designed for Saudi market?</summary><p class="faq-a">Yes, according to Saudi regulations and standards.</p></details>
</section>
</main>
<footer class="site-footer">
<div class="wrap footer-in">
<a class="logo" href="/index-en" style="font-size:16px">
<img src="https://i.ibb.co/MyCPJW6y/B8947-E27-073-B-4-DE2-8-E7-F-EB2023-A17-E70.png" alt="{SITE_NAME_EN}" style="height:28px;vertical-align:middle">
{SITE_NAME_EN}
</a>
<nav aria-label="Footer links">
<a href="/privacy-en">Privacy Policy</a>
<a href="/contact-en">Contact Us</a>
<a href="/about-en">About Us</a>
</nav>
<p>{SITE_NAME_EN} © {year} — All Rights Reserved</p>
</div>
</footer>
<script>
(function(){{var root=document.documentElement,btn=document.getElementById('themeBtn');var moon=document.getElementById('iconMoon'),sun=document.getElementById('iconSun');function apply(t){{if(t==='dark'){{root.setAttribute('data-theme','dark');moon.style.display='none';sun.style.display='block';}}else{{root.removeAttribute('data-theme');moon.style.display='block';sun.style.display='none';}}}}var saved=null;try{{saved=localStorage.getItem('hs-theme');}}catch(e){{}}if(!saved){{saved=(window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'light';}}apply(saved);btn.addEventListener('click',function(){{var next=root.getAttribute('data-theme')==='dark'?'light':'dark';apply(next);try{{localStorage.setItem('hs-theme',next);}}catch(e){{}}}});}})();
(function(){{var tabs=document.querySelectorAll('.tab');var cards=document.querySelectorAll('#cardsGrid .card');var curCat='all';function render(){{cards.forEach(function(c){{var okCat=(curCat==='all'||c.dataset.cat===curCat);c.style.display=okCat?'':'none';}});}}tabs.forEach(function(t){{t.addEventListener('click',function(){{curCat=t.dataset.cat;tabs.forEach(function(x){{x.classList.remove('on');x.setAttribute('aria-selected','false');}});t.classList.add('on');t.setAttribute('aria-selected','true');render();}});}});render();}})();
</script>
</body>
</html>'''

def main():
    print("🔥 توليد صفحات الفهرس...")
    
    # توليد index.html
    ar_html = generate_arabic_index()
    ar_path = os.path.join(ROOT_DIR, 'index.html')
    with open(ar_path, 'w', encoding='utf-8') as f:
        f.write(ar_html)
    print(f"  ✅ تم توليد index.html ({len(PAGES)} حاسبة)")
    
    # توليد index-en.html
    en_html = generate_english_index()
    en_path = os.path.join(ROOT_DIR, 'index-en.html')
    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(en_html)
    print(f"  ✅ تم توليد index-en.html ({len(PAGES)} calculators)")
    
    print("\n🎉 اكتمل!")

if __name__ == "__main__":
    main()
