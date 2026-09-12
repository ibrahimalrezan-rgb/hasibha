#!/usr/bin/env python3
"""
نظام أتمتة حاسبها - مع دعم AI
"""

import json
import os
import sys
from datetime import datetime

# إضافة المسار
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ai_providers import get_provider

SITE_URL = "https://hasibha.com"
SITE_NAME = "حاسبها"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTOMATION_DIR = os.path.dirname(os.path.abspath(__file__))


def load_config():
    """يقرأ الإعدادات"""
    with open(os.path.join(AUTOMATION_DIR, 'config.json'), 'r', encoding='utf-8') as f:
        return json.load(f)


def load_template():
    """يقرأ قالب HTML"""
    with open(os.path.join(AUTOMATION_DIR, 'template.html'), 'r', encoding='utf-8') as f:
        return f.read()


def get_api_key(provider_name):
    """يجيب المفتاح من متغيرات البيئة"""
    if provider_name == "gemini":
        return os.environ.get("GEMINI_API_KEY")
    elif provider_name == "claude":
        return os.environ.get("ANTHROPIC_API_KEY")
    elif provider_name == "openai":
        return os.environ.get("OPENAI_API_KEY")
    return None


def render_fields(calc, lang):
    """يولّد HTML للحقول"""
    html = ""
    for field in calc['fields']:
        label = field[f'label_{lang}']
        fid = field['id']
        ftype = field.get('type', 'number')
        html += f'    <label for="{fid}">{label}</label>\n'
        html += f'    <div class="input-row">\n'
        html += f'      <input type="{ftype}" id="{fid}" placeholder="{label}" oninput="calculate()">\n'
        html += f'    </div>\n\n'
    return html


def render_faq(faqs, lang):
    """يولّد HTML للأسئلة الشائعة"""
    if not faqs:
        return ""
    title = "الأسئلة الشائعة" if lang == "ar" else "FAQ"
    html = f'<h3>{title}</h3>\n'
    for item in faqs:
        html += f'<div style="margin-bottom:16px"><strong>{item["q"]}</strong><p>{item["a"]}</p></div>\n'
    return html


def render_schema(calc, lang, faqs):
    """يولّد Schema JSON-LD"""
    title = calc['title_ar'] if lang == "ar" else calc['title_en']
    desc = calc['description_ar'] if lang == "ar" else calc['description_en']
    url = f"{SITE_URL}/{calc['slug']}" + ("-en" if lang == "en" else "")
    in_lang = "ar-SA" if lang == "ar" else "en-US"
    
    graph = [
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "الرئيسية" if lang == "ar" else "Home", "item": SITE_URL + "/"},
                {"@type": "ListItem", "position": 2, "name": title, "item": url}
            ]
        },
        {
            "@type": "WebApplication",
            "name": title,
            "description": desc,
            "url": url,
            "applicationCategory": "UtilityApplication",
            "operatingSystem": "Any",
            "inLanguage": in_lang,
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "SAR"}
        }
    ]
    
    if faqs:
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q["q"], "acceptedAnswer": {"@type": "Answer", "text": q["a"]}}
                for q in faqs
            ]
        })
    
    schema = {"@context": "https://schema.org", "@graph": graph}
    return json.dumps(schema, ensure_ascii=False, indent=2)


def generate_page(calc, lang, ai_provider, config):
    """يولّد صفحة كاملة"""
    template = load_template()
    
    # جلب المحتوى من AI أو من JSON
    article = calc.get(f'article_{lang}', '')
    faqs = calc.get(f'faq_{lang}', [])
    script = calc.get('calc_script', '')
    
    if ai_provider and config.get('ai_enabled'):
        print(f"    🤖 توليد مقال ({lang})...")
        if config.get('generate_articles') and not article:
            article = ai_provider.generate_article(calc, lang)
        
        print(f"    🤖 توليد أسئلة ({lang})...")
        if config.get('generate_faq') and not faqs:
            faqs = ai_provider.generate_faq(calc, lang)
        
        print(f"    🤖 توليد كود ({lang})...")
        if config.get('generate_scripts') and not script:
            script = ai_provider.generate_script(calc, lang)
    
    # القيم حسب اللغة
    if lang == "ar":
        title = calc['title_ar']
        desc = calc['description_ar']
        keywords = calc['keywords_ar']
        h1 = calc.get('icon', '') + ' ' + calc['title_ar']
        dir_attr = "rtl"
        og_locale = "ar_SA"
        calc_button = "احسب"
        back_link = "↩ الرجوع للقائمة الرئيسية"
        nav_calc = "الحاسبات"
        nav_features = "المميزات"
        nav_faq = "الأسئلة الشائعة"
        breadcrumb_home = "🏠 الرئيسية"
        footer_privacy = "سياسة الخصوصية"
        footer_contact = "تواصل معنا"
        footer_about = "من نحن"
        footer_copy = f'حاسبها © {datetime.now().year} — جميع الحقوق محفوظة'
        lang_url = f"/{calc['slug']}-en"
        lang_code = "en"
        lang_text = "EN"
        output = f"{calc['slug']}.html"
        result_label = "النتيجة"
        num_locale = "ar-SA"
    else:
        title = calc['title_en']
        desc = calc['description_en']
        keywords = calc['keywords_en']
        h1 = calc.get('icon', '') + ' ' + calc['title_en']
        dir_attr = "ltr"
        og_locale = "en_US"
        calc_button = "Calculate"
        back_link = "↩ Back to Home"
        nav_calc = "Calculators"
        nav_features = "Features"
        nav_faq = "FAQ"
        breadcrumb_home = "🏠 Home"
        footer_privacy = "Privacy Policy"
        footer_contact = "Contact Us"
        footer_about = "About Us"
        footer_copy = f'Hasibha © {datetime.now().year} — All Rights Reserved'
        lang_url = f"/{calc['slug']}"
        lang_code = "ar"
        lang_text = "عربي"
        output = f"{calc['slug']}-en.html"
        result_label = "Result"
        num_locale = "en-US"
    
    result_html = f'      <div class="result-row"><span class="result-label">{result_label}</span><span class="result-value big" id="finalResult">0</span></div>'
    
    full_article = article + render_faq(faqs, lang)
    
    full_script = f"function formatNumber(n){{return n.toLocaleString('{num_locale}',{{minimumFractionDigits:2,maximumFractionDigits:2}});}}\n\n{script}"
    
    replacements = {
        "{{LANG}}": "ar" if lang == "ar" else "en",
        "{{DIR}}": dir_attr,
        "{{TITLE}}": title,
        "{{DESCRIPTION}}": desc,
        "{{KEYWORDS}}": keywords,
        "{{SLUG}}": calc['slug'],
        "{{SITE_NAME}}": SITE_NAME,
        "{{OG_LOCALE}}": og_locale,
        "{{SCHEMA}}": render_schema(calc, lang, faqs),
        "{{NAV_CALC}}": nav_calc,
        "{{NAV_FEATURES}}": nav_features,
        "{{NAV_FAQ}}": nav_faq,
        "{{LANG_SWITCH_URL}}": lang_url,
        "{{LANG_SWITCH_CODE}}": lang_code,
        "{{LANG_SWITCH_TEXT}}": lang_text,
        "{{BREADCRUMB_HOME}}": breadcrumb_home,
        "{{H1}}": h1,
        "{{SUBTITLE}}": desc,
        "{{FIELDS_HTML}}": render_fields(calc, lang),
        "{{CALC_BUTTON}}": calc_button,
        "{{RESULT_HTML}}": result_html,
        "{{BACK_LINK}}": back_link,
        "{{ARTICLE_HTML}}": full_article,
        "{{FOOTER_PRIVACY}}": footer_privacy,
        "{{FOOTER_CONTACT}}": footer_contact,
        "{{FOOTER_ABOUT}}": footer_about,
        "{{FOOTER_COPYRIGHT}}": footer_copy,
        "{{CALC_SCRIPT}}": full_script
    }
    
    for key, value in replacements.items():
        template = template.replace(key, value)
    
    output_path = os.path.join(ROOT_DIR, output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)
    
    return output


def main():
    config = load_config()
    
    # تحضير AI
    ai_provider = None
    if config.get('ai_enabled'):
        provider_name = config.get('ai_provider', 'gemini')
        api_key = get_api_key(provider_name)
        
        if api_key:
            try:
                ai_provider = get_provider(provider_name, api_key)
                print(f"🤖 AI: {provider_name}")
            except Exception as e:
                print(f"⚠️ خطأ في تحميل AI: {e}")
        else:
            print(f"⚠️ لا يوجد مفتاح API لـ {provider_name}")
    
    # قراءة الحاسبات
    with open(os.path.join(AUTOMATION_DIR, 'calculators.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    calculators = data['calculators']
    print(f"📊 عدد الحاسبات: {len(calculators)}")
    
    for i, calc in enumerate(calculators, 1):
        print(f"\n[{i}/{len(calculators)}] 🔨 {calc['title_ar']}")
        ar = generate_page(calc, 'ar', ai_provider, config)
        print(f"  ✅ {ar}")
        en = generate_page(calc, 'en', ai_provider, config)
        print(f"  ✅ {en}")
    
    print("\n🎉 اكتمل!")


if __name__ == "__main__":
    main()
