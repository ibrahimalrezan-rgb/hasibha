#!/usr/bin/env python3
"""
تحديث الصفحات الإنجليزية من العربية باستخدام AI
يستخرج المقال + الحقول + JavaScript
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

# قائمة الصفحات
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


def clean_ai_response(text):
    """ينظف رد AI من code blocks"""
    if not text:
        return ""
    text = text.strip()
    if text.startswith("```"):
        parts = text.split("```")
        if len(parts) >= 2:
            text = parts[1]
            if text.startswith("html") or text.startswith("json") or text.startswith("javascript"):
                text = text.split("\n", 1)[1] if "\n" in text else ""
    return text.strip()


def read_ar_content(slug):
    """يقرأ كل المحتوى من الصفحة العربية"""
    path = os.path.join(ROOT_DIR, f"{slug}.html")
    if not os.path.exists(path):
        return None
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    result = {
        'article': '',
        'fields': [],
        'script': '',
        'title': '',
        'description': ''
    }
    
    # استخراج article-box (كل المحتوى حتى main end)
    match = re.search(r'<div class="article-box">(.*?)</div>\s*</div>\s*</main>', content, re.DOTALL)
    if match:
        result['article'] = match.group(1).strip()
    
    # استخراج الحقول
    label_pattern = re.compile(r'<label for="([^"]+)">([^<]+)</label>', re.UNICODE)
    for m in label_pattern.finditer(content):
        field_id = m.group(1)
        label_ar = m.group(2).strip()
        if field_id and label_ar:
            result['fields'].append({
                'id': field_id,
                'label_ar': label_ar
            })
    
    # استخراج السكربت الأخير
    scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
    for s in reversed(scripts):
        if 'function calculate' in s:
            result['script'] = s.strip()
            break
    
    # استخراج العنوان
    title_match = re.search(r'<title>([^<]+)</title>', content)
    if title_match:
        result['title'] = title_match.group(1).strip()
    
    # استخراج الوصف
    desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)
    if desc_match:
        result['description'] = desc_match.group(1).strip()
    
    return result


def translate_article(ai, article_ar):
    """يترجم المقال من العربية للإنجليزية"""
    if not article_ar:
        return ""
    
    prompt = f"""Translate the following Arabic HTML content to English.

CRITICAL RULES:
1. Keep ALL HTML tags exactly as they are: <h3>, <p>, <ul>, <li>, <div class="tip">
2. Translate ONLY the text content inside the tags
3. Keep numbers as-is
4. Keep "ريال" → "SAR", "السعودية" → "Saudi Arabia", "حاسبها" → "Hasibha"
5. Keep class names and attributes unchanged
6. Do NOT add explanations or code blocks
7. Output ONLY the translated HTML

Arabic HTML:
{article_ar}

English HTML:"""
    
    result = ai.generate(prompt, max_tokens=4000)
    return clean_ai_response(result)


def translate_labels(ai, labels_ar):
    """يترجم قائمة labels من العربية للإنجليزية"""
    if not labels_ar:
        return []
    
    prompt = f"""Translate these Arabic labels to English.

Rules:
- Return ONLY a JSON array of translated strings
- Same order as input
- No explanations
- No code blocks

Input: {json.dumps(labels_ar, ensure_ascii=False)}

Output (JSON array only):"""
    
    result = ai.generate(prompt, max_tokens=500)
    result = clean_ai_response(result)
    
    try:
        # تنظيف إضافي
        if result.startswith('['):
            return json.loads(result)
    except:
        pass
    
    # fallback: ترجمة بسيطة
    return [f"Field {i+1}" for i in range(len(labels_ar))]


def build_fields_html(fields_ar, labels_en):
    """يبني HTML الحقول بالإنجليزية"""
    html = ""
    for i, field in enumerate(fields_ar):
        label_en = labels_en[i] if i < len(labels_en) else field['label_ar']
        fid = field['id']
        html += f'    <label for="{fid}">{label_en}</label>\n'
        html += f'    <div class="input-row">\n'
        html += f'      <input type="number" id="{fid}" placeholder="{label_en}" oninput="calculate()">\n'
        html += f'    </div>\n\n'
    return html


def generate_en_page(ai, page):
    """يولّد صفحة إنجليزية كاملة"""
    slug = page['slug']
    print(f"  📖 قراءة {slug}.html...")
    
    content = read_ar_content(slug)
    if not content:
        print(f"  ⚠️ لم أجد {slug}.html")
        return None
    
    if not content['article']:
        print(f"  ⚠️ لا يوجد article-box")
        return None
    
    print(f"  📊 {len(content['fields'])} حقل، {len(content['article'])} حرف مقال")
    
    # ترجمة المقال
    print(f"  🤖 ترجمة المقال...")
    article_en = translate_article(ai, content['article'])
    
    if not article_en or len(article_en) < 100:
        print(f"  ⚠️ الترجمة فشلت")
        return None
    
    print(f"  ✅ مقال ({len(article_en)} حرف)")
    
    # ترجمة الحقول
    labels_ar = [f['label_ar'] for f in content['fields']]
    if labels_ar:
        print(f"  🤖 ترجمة {len(labels_ar)} حقل...")
        labels_en = translate_labels(ai, labels_ar)
        print(f"  ✅ تمت الترجمة")
    else:
        labels_en = []
    
    fields_html = build_fields_html(content['fields'], labels_en)
    
    # الوصف الإنجليزي
    desc_prompt = f"Write a short SEO description (140-160 chars) in English for: {page['title_en']}. Just the description, no quotes."
    desc_en = clean_ai_response(ai.generate(desc_prompt, max_tokens=200))
    
    if not desc_en or len(desc_en) < 20:
        desc_en = f"Free online {page['title_en']}. Get instant, accurate results - no registration required."
    
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
    
    # استخدام القالب
    template = load_template()
    
    # السكربت
    script = content['script'] or ""
    full_script = f"function formatNumber(n){{return n.toLocaleString('en-US',{{minimumFractionDigits:2,maximumFractionDigits:2}});}}\n\n{script}"
    
    # استبدالات
    replacements = {
        "{{LANG}}": "en",
        "{{DIR}}": "ltr",
        "{{TITLE}}": page['title_en'],
        "{{DESCRIPTION}}": desc_en,
        "{{KEYWORDS}}": page['title_en'],
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
        "{{H1}}": page['icon'] + ' ' + page['title_en'],
        "{{SUBTITLE}}": desc_en,
        "{{FIELDS_HTML}}": fields_html,
        "{{CALC_BUTTON}}": "Calculate",
        "{{RESULT_HTML}}": '<div class="result-row"><span class="result-label">Result</span><span class="result-value big" id="finalResult">0</span></div>',
        "{{BACK_LINK}}": "↩ Back to Home",
        "{{ARTICLE_HTML}}": article_en,
        "{{FOOTER_PRIVACY}}": "Privacy Policy",
        "{{FOOTER_CONTACT}}": "Contact Us",
        "{{FOOTER_ABOUT}}": "About Us",
        "{{FOOTER_COPYRIGHT}}": f'Hasibha © {datetime.now().year} — All Rights Reserved',
        "{{CALC_SCRIPT}}": full_script
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
    
    # تحديد الصفحات
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
