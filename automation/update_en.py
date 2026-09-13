#!/usr/bin/env python3
"""
تحديث الصفحات الإنجليزية من العربية باستخدام AI
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

# قائمة الصفحات اللي سنحدّثها
PAGES = [
    {"slug": "mortgage", "title_ar": "حاسبة التمويل العقاري", "title_en": "Mortgage Calculator", "category": "finance", "icon": "🏠"},
    {"slug": "personal-loan", "title_ar": "حاسبة التمويل الشخصي", "title_en": "Personal Loan Calculator", "category": "finance", "icon": "💵"},
    {"slug": "eos", "title_ar": "حاسبة نهاية الخدمة", "title_en": "End of Service Calculator", "category": "finance", "icon": "📋"},
    {"slug": "vat", "title_ar": "حاسبة ضريبة القيمة المضافة", "title_en": "VAT Calculator", "category": "finance", "icon": "🧾"},
    {"slug": "salary", "title_ar": "حاسبة الراتب بعد التأمينات", "title_en": "Salary After Insurance", "category": "finance", "icon": "💼"},
    {"slug": "currency", "title_ar": "تحويل العملات", "title_en": "Currency Converter", "category": "conversion", "icon": "💱"},
    {"slug": "length", "title_ar": "تحويل الطول", "title_en": "Length Converter", "category": "conversion", "icon": "📏"},
    {"slug": "weight", "title_ar": "تحويل الوزن", "title_en": "Weight Converter", "category": "conversion", "icon": "⚖️"},
    {"slug": "area", "title_ar": "تحويل المساحة", "title_en": "Area Converter", "category": "conversion", "icon": "📐"},
    {"slug": "bmi", "title_ar": "مؤشر كتلة الجسم BMI", "title_en": "BMI Calculator", "category": "health", "icon": "🧍"},
    {"slug": "calorie", "title_ar": "حاسبة السعرات الحرارية", "title_en": "Calorie Calculator", "category": "health", "icon": "🍎"},
    {"slug": "water", "title_ar": "حاسبة احتياج الماء", "title_en": "Water Intake Calculator", "category": "health", "icon": "💧"},
    {"slug": "age", "title_ar": "حاسبة العمر", "title_en": "Age Calculator", "category": "general", "icon": "🎂"},
    {"slug": "discount", "title_ar": "حاسبة نسبة الخصم", "title_en": "Discount Calculator", "category": "general", "icon": "🏷️"},
    {"slug": "date-diff", "title_ar": "الوقت بين تاريخين", "title_en": "Date Difference Calculator", "category": "general", "icon": "📅"},
]

# الصفحات الثابتة
STATIC_PAGES = [
    {"slug": "privacy", "title_en": "Privacy Policy"},
    {"slug": "about", "title_en": "About Us"},
    {"slug": "contact", "title_en": "Contact Us"},
]


def load_config():
    with open(os.path.join(AUTOMATION_DIR, 'config.json'), 'r', encoding='utf-8') as f:
        return json.load(f)


def load_template():
    with open(os.path.join(AUTOMATION_DIR, 'template.html'), 'r', encoding='utf-8') as f:
        return f.read()


def get_api_key(provider_name):
    if provider_name == "gemini":
        return os.environ.get("GEMINI_API_KEY")
    elif provider_name == "claude":
        return os.environ.get("ANTHROPIC_API_KEY")
    elif provider_name == "openai":
        return os.environ.get("OPENAI_API_KEY")
    return None


def read_ar_article(slug):
    """يقرأ المقال العربي من الصفحة الحالية"""
    path = os.path.join(ROOT_DIR, f"{slug}.html")
    if not os.path.exists(path):
        return None
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # استخراج article-box
    match = re.search(r'<div class="article-box">(.*?)</div>\s*</div>\s*</main>', content, re.DOTALL)
    if not match:
        return None
    
    return match.group(1).strip()


def read_ar_script(slug):
    """يقرأ JavaScript من الصفحة العربية"""
    path = os.path.join(ROOT_DIR, f"{slug}.html")
    if not os.path.exists(path):
        return None
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # استخراج السكربت الأخير
    scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
    if scripts:
        # نأخذ الأخير (يحتوي calculate)
        for s in reversed(scripts):
            if 'function calculate' in s or 'function formatNumber' in s:
                return s.strip()
    return None


def translate_text(ai, text, lang_from="ar", lang_to="en"):
    """يترجم نص باستخدام AI"""
    if not text:
        return ""
    
    prompt = f"""Translate the following text from Arabic to English.

Keep the HTML structure exactly the same:
- Keep all <h3>, <p>, <ul>, <li>, <div class="tip"> tags
- Translate only the text content
- Keep numbers, URLs, technical terms in English
- Keep "ريال" as "SAR"
- Keep "السعودية" as "Saudi Arabia"

Text to translate:
{text}

Output ONLY the translated HTML. No explanations. No code blocks.
"""
    
    result = ai.generate(prompt, max_tokens=4000)
    return result.strip()


def extract_faq_from_article(article_html):
    """يستخرج الأسئلة من المقال العربي"""
    if 'الأسئلة الشائعة' not in article_html:
        return ""
    
    parts = article_html.split('الأسئلة الشائعة')
    if len(parts) > 1:
        return parts[1].strip()
    return ""


def generate_en_page(ai, page):
    """يولّد صفحة إنجليزية من العربية"""
    slug = page['slug']
    
    # قراءة المحتوى العربي
    print(f"  📖 قراءة {slug}.html...")
    article_ar = read_ar_article(slug)
    if not article_ar:
        print(f"  ⚠️ لم أجد article-box في {slug}.html")
        return None
    
    script = read_ar_script(slug)
    
    # ترجمة المقال
    print(f"  🤖 ترجمة المقال...")
    article_en = translate_text(ai, article_ar)
    
    if not article_en or len(article_en) < 100:
        print(f"  ⚠️ الترجمة فشلت")
        return None
    
    print(f"  ✅ تمت الترجمة ({len(article_en)} حرف)")
    
    # استخدام القالب
    template = load_template()
    
    # تقسيم article_en إلى مقال + أسئلة
    faq_html = ""
    if 'FAQ' in article_en or 'Frequently Asked' in article_en:
        # الأسئلة موجودة داخل الترجمة
        pass
    
    # بناء الصفحة
    title = page['title_en']
    desc_prompt = f"Write a one-sentence SEO description (150-160 chars) in English for: {page['title_ar']}"
    desc = ai.generate(desc_prompt, max_tokens=200).strip()
    
    if not desc or len(desc) < 20:
        desc = f"Free online {title.lower()} - Calculate instantly and accurately."
    
    # بناء Schema
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/index-en"},
                    {"@type": "ListItem", "position": 2, "name": title, "item": f"{SITE_URL}/{slug}-en"}
                ]
            },
            {
                "@type": "WebApplication",
                "name": title,
                "description": desc,
                "url": f"{SITE_URL}/{slug}-en",
                "applicationCategory": "UtilityApplication",
                "operatingSystem": "Any",
                "inLanguage": "en-US",
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "SAR"}
            }
        ]
    }
    
    # استبدال القيم
    replacements = {
        "{{LANG}}": "en",
        "{{DIR}}": "ltr",
        "{{TITLE}}": title,
        "{{DESCRIPTION}}": desc,
        "{{KEYWORDS}}": title,
        "{{SLUG}}": slug,
        "{{SITE_NAME}}": "Hasibha",
        "{{OG_LOCALE}}": "en_US",
        "{{SCHEMA}}": json.dumps(schema, ensure_ascii=False, indent=2),
        "{{NAV_CALC}}": "Calculators",
        "{{NAV_FEATURES}}": "Features",
        "{{NAV_FAQ}}": "FAQ",
        "{{LANG_SWITCH_URL}}": f"/{slug}",
        "{{LANG_SWITCH_CODE}}": "ar",
        "{{LANG_SWITCH_TEXT}}": "عربي",
        "{{BREADCRUMB_HOME}}": "🏠 Home",
        "{{H1}}": page['icon'] + ' ' + title,
        "{{SUBTITLE}}": desc,
        "{{CALC_BUTTON}}": "Calculate",
        "{{BACK_LINK}}": "↩ Back to Home",
        "{{ARTICLE_HTML}}": article_en,
        "{{FOOTER_PRIVACY}}": "Privacy Policy",
        "{{FOOTER_CONTACT}}": "Contact Us",
        "{{FOOTER_ABOUT}}": "About Us",
        "{{FOOTER_COPYRIGHT}}": f'Hasibha © {datetime.now().year} — All Rights Reserved',
        "{{FIELDS_HTML}}": "",  # سنحتفظ بالحقول الإنجليزية لاحقاً
        "{{RESULT_HTML}}": "",
        "{{CALC_SCRIPT}}": script or "",
    }
    
    for key, value in replacements.items():
        template = template.replace(key, value)
    
    # حفظ
    output = f"{slug}-en.html"
    output_path = os.path.join(ROOT_DIR, output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"  ✅ تم إنشاء {output}")
    return output


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
        
        if not ai:
            print("⚠️ AI غير متاح")
            return
    else:
        print("⚠️ AI معطل")
        return
    
    # تحديث الصفحات
    pages_to_update = PAGES
    if len(sys.argv) > 1:
        # تحديث صفحة واحدة فقط
        target = sys.argv[1]
        pages_to_update = [p for p in PAGES if p['slug'] == target]
    
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
