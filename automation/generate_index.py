#!/usr/bin/env python3
"""توليد الفهرس العربي والإنجليزي - التبويبات تُبنى من config تلقائياً"""

import os
import json
from datetime import datetime
from config import PAGES, CATEGORIES, SITE_URL

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YEAR = datetime.now().year

def build_tabs(lang):
    all_label = "الكل" if lang == "ar" else "All"
    tabs = f'<button class="tab on" data-cat="all">{all_label} ({len(PAGES)})</button>\n'
    for key, meta in CATEGORIES.items():
        count = len([p for p in PAGES if p["category"] == key])
        if count == 0:
            continue
        label = meta["ar"] if lang == "ar" else meta["en"]
        tabs += f'<button class="tab" data-cat="{key}">{meta["icon"]} {label} ({count})</button>\n'
    return tabs

def build_cards(lang):
    html = ""
    for p in PAGES:
        title = p["title_ar"] if lang == "ar" else p["title_en"]
        desc = p["desc_ar"] if lang == "ar" else p["desc_en"]
        href = f"/{p['slug']}" if lang == "ar" else f"/{p['slug']}-en"
        cta = "استخدم الحاسبة ←" if lang == "ar" else "← Use Calculator"
        html += f'''<a class="card {p['category']}" data-cat="{p['category']}" href="{href}">
<span class="card-icon">{p['icon']}</span>
<div><h3>{title}</h3><p>{desc}</p></div>
<span class="card-cta">{cta}</span>
</a>
'''
    return html

def build_index(lang):
    ar = lang == "ar"
    title = "حاسبها — كل الحاسبات المالية والصحية في مكان واحد" if ar else "Hasibha — All Financial & Health Calculators in One Place"
    desc = "17 حاسبة مجانية: تمويل، زكاة، ذهب، تأمينات، BMI والمزيد. نتائج فورية بدون تسجيل." if ar else "17 free calculators: mortgage, zakat, gold, GOSI, BMI and more. Instant results."
    other = "index-en" if ar else "index"
    other_label = "EN" if ar else "عربي"
    nav = [("calculators", "الحاسبات" if ar else "Calculators"), ("features", "المميزات" if ar else "Features"), ("faq", "الأسئلة الشائعة" if ar else "FAQ")]
    nav_html = "\n".join(f'<a href="#{i}">{t}</a>' for i, t in nav)
    stats = [
        (str(len(PAGES)) + ("+" if ar else ""), "حاسبة مجانية" if ar else "Free Calculators"),
        ("2", "لغة" if ar else "Languages"),
        ("4", "تصنيفات" if ar else "Categories"),
        ("100%", "مجاني" if ar else "Free"),
    ]
    stats_html = "\n".join(f'<div class="stat"><b>{v}</b><span>{s}</span></div>' for v, s in stats)
    features = [
        ("⚡", "سرعة فورية", "نتائج لحظية بدون انتظار أو تحميل.") if ar else ("⚡", "Instant Speed", "Real-time results with zero waiting."),
        ("🔒", "خصوصية تامة", "لا نحفظ أي بيانات — كل شيء في متصفحك.") if ar else ("🔒", "Full Privacy", "No data stored — everything runs in your browser."),
        ("📱", "يعمل على الجوال", "تصميم متجاوب بالكامل مع كل الشاشات.") if ar else ("📱", "Mobile Ready", "Fully responsive on all screens."),
        ("🌐", "ثنائي اللغة", "عربي وإنجليزي بنفس الدقة والجودة.") if ar else ("🌐", "Bilingual", "Arabic and English with equal quality."),
    ]
    feat_html = "\n".join(f'<div class="feature"><b>{i} {t}</b><span>{s}</span></div>' for i, t, s in features)
    faqs = [
        ("هل الحاسبات مجانية بالفعل؟", "نعم، جميع الحاسبات مجانية 100% بدون تسجيل أو حدود استخدام."),
        ("هل بياناتي محفوظة؟", "لا، كل الحسابات تتم داخل متصفحك ولا تُرسل لأي سيرفر."),
        ("ما مدى دقة النتائج؟", "مبنية على الأنظمة السعودية الرسمية (ساما، التأمينات، هيئة الزكاة)."),
    ] if ar else [
        ("Are the calculators really free?", "Yes, 100% free with no registration or limits."),
        ("Is my data stored?", "No, all calculations run inside your browser."),
        ("How accurate are results?", "Based on official Saudi regulations (SAMA, GOSI, ZATCA)."),
    ]
    faq_html = "\n".join(f'<details><summary>{q}</summary><div class="faq-a">{a}</div></details>' for q, a in faqs)
    home_href = "/index-en" if ar else "/index"
    logo_alt = "حاسبها" if ar else "Hasibha"
    brand = "حاسبها" if ar else "Hasibha"
    hero_badge = "منصة سعودية موثوقة" if ar else "Trusted Saudi Platform"
    hero_h1 = "كل حاسباتك المالية والصحية في مكان واحد" if ar else "All Your Financial & Health Calculators in One Place"
    hero_lead = "مصممة خصيصًا للسوق السعودي — دقيقة، سريعة، ومجانية بالكامل." if ar else "Built for the Saudi market — accurate, fast and completely free."
    sec_calc = "اختر حاسبتك" if ar else "Pick Your Calculator"
    sec_feat = "لماذا حاسبها؟" if ar else "Why Hasibha?"
    sec_faq = "الأسئلة الشائعة" if ar else "FAQ"
    foot_links = f'<a href="/privacy{"-en" if not ar else ""}">{"سياسة الخصوصية" if ar else "Privacy"}</a>\n<a href="/contact{"-en" if not ar else ""}">{"اتصل بنا" if ar else "Contact"}</a>\n<a href="/about{"-en" if not ar else ""}">{"من نحن" if ar else "About"}</a>'
    foot_copy = f"حاسبها © {YEAR} — جميع الحقوق محفوظة" if ar else f"Hasibha © {YEAR} — All Rights Reserved"

    schema = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": brand,
        "url": SITE_URL + "/" + ("" if ar else "index-en"),
        "inLanguage": "ar-SA" if ar else "en-US",
        "description": desc,
    }

    return f'''<!DOCTYPE html>
<html lang="{"ar" if ar else "en"}" dir="{"rtl" if ar else "ltr"}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE_URL}/{"" if ar else "index-en"}">
<link rel="alternate" hreflang="ar" href="{SITE_URL}/">
<link rel="alternate" hreflang="en" href="{SITE_URL}/index-en">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}/">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{brand}">
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
<a class="logo" href="{home_href}"> {brand}</a>
<nav class="main-nav">{nav_html}</nav>
<div class="header-actions">
<button class="theme-btn" id="themeBtn" aria-label="Theme">🌓</button>
<a class="lang-btn" href="/{other}">{other_label}</a>
</div>
</div>
</header>
<section class="hero">
<div class="badge"><span class="dot"></span>{hero_badge}</div>
<h1>{hero_h1}</h1>
<p class="lead">{hero_lead}</p>
<div class="stats">{stats_html}</div>
</section>
<section class="wrap" id="calculators">
<div class="section-head"><h2>{sec_calc}</h2></div>
<div class="tabs">
{build_tabs(lang)}
</div>
<div class="grid">
{build_cards(lang)}
</div>
</section>
<section class="wrap" id="features">
<div class="section-head"><h2>{sec_feat}</h2></div>
<div class="features-grid">
{feat_html}
</div>
</section>
<section class="wrap faq" id="faq">
<div class="section-head"><h2>{sec_faq}</h2></div>
{faq_html}
</section>
<footer class="site-footer">
<div class="wrap footer-in">
<a class="logo" href="{home_href}">🧮 {brand}</a>
<nav>{foot_links}</nav>
<p>{foot_copy}</p>
</div>
</footer>
<script>
(function(){{
var root=document.documentElement, btn=document.getElementById('themeBtn');
function apply(t){{ if(t==='dark'){{root.setAttribute('data-theme','dark');}}else{{root.removeAttribute('data-theme');}} }}
var saved=null; try{{saved=localStorage.getItem('hs-theme');}}catch(e){{}}
if(!saved){{saved=(window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'light';}}
apply(saved);
btn.addEventListener('click',function(){{
var next=root.getAttribute('data-theme')==='dark'?'light':'dark';
apply(next); try{{localStorage.setItem('hs-theme',next);}}catch(e){{}}
}});
}})();
(function(){{
var tabs=document.querySelectorAll('.tab');
var cards=document.querySelectorAll('.card');
tabs.forEach(function(btn){{
btn.addEventListener('click',function(){{
tabs.forEach(function(b){{b.classList.remove('on');}});
btn.classList.add('on');
var cat=btn.getAttribute('data-cat');
cards.forEach(function(card){{
var show=(cat==='all')||(card.getAttribute('data-cat')===cat);
if(show){{card.classList.remove('hide');card.style.display='';}}
else{{card.classList.add('hide');card.style.display='none';}}
}});
}});
}});
}})();
</script>
</body>
</html>
'''

def main():
    print("🏗️ توليد الفهرس...")
    for lang, filename in [("ar", "index.html"), ("en", "index-en.html")]:
        html = build_index(lang)
        path = os.path.join(ROOT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  ✅ {filename} ({len(PAGES)} حاسبة)")
    print("🎉 اكتمل!")

if __name__ == "__main__":
    main()
