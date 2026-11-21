#!/usr/bin/env python3
"""
إصلاح مشاكل SEO المكتشفة تلقائياً
- العناوين المكررة والقصيرة والطويلة
- H1 المفقود/المتعدد
- Descriptions الناقصة
- canonical الخاطئ
"""
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============================================
# 1) إصلاح العناوين المكررة والقصيرة
# ============================================
TITLE_FIXES = {
    'about.html': ('من نحن — حاسبها | منصة الحاسبات السعودية',
                   'تعرف على فريق حاسبها ورؤيتنا لتقديم أفضل الحاسبات المالية والصحية للسوق السعودي.'),
    'privacy.html': ('سياسة الخصوصية — حاسبها | بياناتك آمنة معنا',
                      'اكتشف كيف نحمي خصوصيتك في حاسبها — لا نحفظ أي بيانات، كل الحسابات في متصفحك.'),
    'contact.html': ('اتصل بنا — حاسبها | تواصل معنا بسهولة',
                     'تواصل مع فريق حاسبها للاستفسارات والاقتراحات — نرد خلال 24 ساعة.'),
    'about-en.html': ('About Us — Hasibha | Saudi Calculators Platform',
                      'Learn about Hasibha team and our vision to deliver the best financial & health calculators for Saudi Arabia.'),
    'privacy-en.html': ('Privacy Policy — Hasibha | Your Data is Safe',
                        'Discover how we protect your privacy at Hasibha — no data stored, all calculations run in your browser.'),
    'contact-en.html': ('Contact Us — Hasibha | Get in Touch',
                        'Reach out to Hasibha team for inquiries and suggestions — we reply within 24 hours.'),
}

# ============================================
# 2) إصلاح العناوين الإنجليزية القصيرة للحاسبات
# ============================================
EN_CALC_TITLES = {
    'bmi-en.html': 'BMI Calculator 2026 | Ideal Weight & Health Classification',
    'calorie-en.html': 'Calorie Calculator 2026 | Daily Energy Needs for Saudis',
    'currency-en.html': 'Currency Converter 2026 | Live SAR Exchange Rates',
    'discount-en.html': 'Discount Calculator 2026 | Save Money on Saudi Sales',
    'length-en.html': 'Length Converter 2026 | Meters, Feet & Inches Instantly',
    'mortgage-en.html': 'Saudi Mortgage Calculator 2026 | Monthly Payment & Rates',
    'vat-en.html': 'VAT Calculator 2026 | Add or Remove 15% Saudi Tax',
    'weight-en.html': 'Weight Converter 2026 | KG, Pounds & Ounces',
    'zakat-en.html': 'Zakat Calculator 2026 | Accurate Islamic Zakat Guide',
    'age-en.html': 'Age Calculator 2026 | Exact Age in Years, Months & Days',
    'area-en.html': 'Area Converter 2026 | sqm, Acres & Hectares',
    'personal-loan-en.html': 'Saudi Personal Loan Calculator 2026 | Best Rates',
    'eos-en.html': 'Saudi End of Service Calculator 2026 | ESB Benefits',
    'salary-en.html': 'Salary After GOSI Calculator 2026 | Net Pay Saudi',
    'gold-value-en.html': 'Gold Value Calculator 2026 | 24K, 22K, 21K, 18K',
    'water-en.html': 'Water Intake Calculator 2026 | Daily Liters Needed',
    'date-diff-en.html': 'Date Difference Calculator 2026 | Days Between Dates',
}

fixed = 0

# ============================================
# تطبيق إصلاحات الصفحات الثابتة
# ============================================
for fname, (new_title, new_desc) in TITLE_FIXES.items():
    path = os.path.join(ROOT_DIR, fname)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c

    # العنوان
    c = re.sub(r'<title[^>]*>.*?</title>', f'<title>{new_title}</title>', c, flags=re.S)

    # Description (أضف أو استبدل)
    if '<meta name="description"' in c:
        c = re.sub(r'<meta\s+name="description"[^>]*>',
                   f'<meta name="description" content="{new_desc}">', c)
    elif '</head>' in c:
        c = c.replace('</head>', f'<meta name="description" content="{new_desc}">\n</head>', 1)

    # H1 مفقود → استخرج من العنوان
    if '<h1' not in c and '</main>' in c:
        h1_text = new_title.split('—')[0].split('|')[0].strip()
        c = c.replace('<main>', f'<main>\n<div class="wrap"><h1>{h1_text}</h1></div>', 1)

    # canonical صحيح
    expected_canonical = f'https://hasibha.com/{fname[:-5]}'
    if 'rel="canonical"' in c:
        c = re.sub(r'<link\s+rel="canonical"\s+href="[^"]*">',
                   f'<link rel="canonical" href="{expected_canonical}">', c)

    if c != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✅ {fname}")
        fixed += 1

# ============================================
# 3) إصلاح عناوين الحاسبات الإنجليزية القصيرة
# ============================================
for fname, new_title in EN_CALC_TITLES.items():
    path = os.path.join(ROOT_DIR, fname)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c

    c = re.sub(r'<title[^>]*>.*?</title>', f'<title>{new_title}</title>', c, flags=re.S)

    if c != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✅ {fname} (title)")
        fixed += 1

# ============================================
# 4) إصلاح المقالات: H1 مزدوج + عناوين طويلة
# ============================================
articles_dir = os.path.join(ROOT_DIR, 'articles')
SHORT_ARTICLE_TITLES = {
    'bmi-guide-2026-en.html': 'BMI Guide 2026 | Saudi Health Calculator',
    'eos-guide-2026-en.html': 'End of Service 2026 | Saudi ESB Guide',
    'mortgage-guide-2026-en.html': 'Saudi Mortgage Guide 2026 | Full Calculator',
    'zakat-guide-2026-en.html': 'Zakat Guide 2026 | Islamic Calculator Saudi',
    'mortgage-guide-2026.html': 'دليل التمويل العقاري 2026 | الحاسبة السعودية',
}

if os.path.exists(articles_dir):
    for fname in os.listdir(articles_dir):
        if not fname.endswith('.html') or fname.startswith('index'):
            continue
        path = os.path.join(articles_dir, fname)
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        orig = c

        # إصلاح H1 مزدوج: احذف الثاني
        h1_matches = list(re.finditer(r'<h1[^>]*>.*?</h1>', c, re.S))
        if len(h1_matches) > 1:
            for m in reversed(h1_matches[1:]):
                c = c[:m.start()] + c[m.end():]

        # اختصار العناوين الطويلة
        if fname in SHORT_ARTICLE_TITLES:
            c = re.sub(r'<title[^>]*>.*?</title>',
                       f'<title>{SHORT_ARTICLE_TITLES[fname]}</title>', c, flags=re.S)

        # إصلاح المراسي غير الموجودة في المقالات الإنجليزية
        if fname.endswith('-en.html'):
            c = c.replace('href="#when-doctor"', 'href="#faq"')
            c = c.replace('href="#golden-tips"', 'href="#tips"')
            c = c.replace('href="#summary"', 'href="#faq"')

        if c != orig:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"✅ articles/{fname}")
            fixed += 1

# ============================================
# 5) إضافة description لفهرسي المقالات
# ============================================
for fname, desc in [
    ('articles/index.html', 'مكتبة حاسبها — أدلة شاملة عن الزكاة، التمويل العقاري، ضريبة القيمة المضافة، مكافأة نهاية الخدمة والمزيد.'),
    ('articles/index-en.html', 'Hasibha Library — Complete guides on Zakat, Saudi Mortgage, VAT 15%, End of Service Benefits and more.'),
]:
    path = os.path.join(ROOT_DIR, fname)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c

    if '<meta name="description"' not in c and '</head>' in c:
        c = c.replace('</head>', f'<meta name="description" content="{desc}">\n</head>', 1)

    # إصلاح canonical
    canonical = 'https://hasibha.com/articles/' if fname == 'articles/index.html' else 'https://hasibha.com/articles/index-en'
    if 'rel="canonical"' not in c and '</head>' in c:
        c = c.replace('</head>', f'<link rel="canonical" href="{canonical}">\n</head>', 1)

    if c != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✅ {fname} (description + canonical)")
        fixed += 1

# ============================================
# 6) إصلاح sitemap.xml (إزالة /articles/ المكرر)
# ============================================
sitemap_path = os.path.join(ROOT_DIR, 'sitemap.xml')
if os.path.exists(sitemap_path):
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        s = f.read()
    orig = s

    # إزالة /articles/ المكرر (نترك فقط /articles/index-en إذا وجد)
    # أو ببساطة: احذف url الذي loc = https://hasibha.com/articles/
    s = re.sub(
        r'\s*<url>\s*<loc>https://hasibha\.com/articles/</loc>[\s\S]*?</url>',
        '', s)

    if s != orig:
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(s)
        print("✅ sitemap.xml (إزالة المسار المكرر)")
        fixed += 1

print(f"\n🎉 تم إصلاح {fixed} مشكلة تلقائياً!")
