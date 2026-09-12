#!/usr/bin/env python3
"""
نظام أتمتة حاسبها - مع دعم AI + محتوى افتراضي + تحديث الرئيسية
"""

import json
import os
import re
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ai_providers import get_provider

SITE_URL = "https://hasibha.com"
SITE_NAME = "حاسبها"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTOMATION_DIR = os.path.dirname(os.path.abspath(__file__))


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


def default_article(calc, lang):
    title = calc['title_ar'] if lang == "ar" else calc['title_en']
    desc = calc['description_ar'] if lang == "ar" else calc['description_en']
    
    if lang == "ar":
        return f"""<h3>عن {title}</h3>
<p>{desc}. تستخدم هذه الحاسبة معادلات دقيقة لمساعدتك في الحصول على نتائج فورية وموثوقة.</p>

<h3>كيفية الاستخدام</h3>
<ul>
<li>أدخل القيم المطلوبة في الحقول أعلاه.</li>
<li>ستظهر النتيجة تلقائياً أثناء الكتابة.</li>
<li>يمكنك تعديل القيم للحصول على نتائج مختلفة.</li>
</ul>

<h3>ملاحظات مهمة</h3>
<p>جميع الحسابات تتم داخل متصفحك مباشرة ولا يتم إرسالها لأي خادم. النتائج تقديرية ويُنصح بمراجعة جهة مختصة للحالات الخاصة.</p>

<div class="tip">💡 <strong>نصيحة:</strong> احتفظ بنتيجة الحساب للرجوع إليها لاحقاً.</div>"""
    else:
        return f"""<h3>About {title}</h3>
<p>{desc}. This calculator uses accurate formulas to give you instant, reliable results.</p>

<h3>How to Use</h3>
<ul>
<li>Enter the required values in the fields above.</li>
<li>The result appears automatically as you type.</li>
<li>Modify values to get different results.</li>
</ul>

<h3>Important Notes</h3>
<p>All calculations run inside your browser and are never sent to any server. Results are estimates; consult a specialist for specific cases.</p>

<div class="tip">💡 <strong>Tip:</strong> Save your result for future reference.</div>"""


def default_faq(calc, lang):
    title = calc['title_ar'] if lang == "ar" else calc['title_en']
    
    if lang == "ar":
        return [
            {"q": f"هل {title} مجانية؟", "a": "نعم، جميع الحاسبات في حاسبها مجانية بالكامل."},
            {"q": "هل النتائج دقيقة؟", "a": "نعم، نستخدم معادلات دقيقة، لكن النتائج تقديرية."},
            {"q": "هل بياناتي محفوظة؟", "a": "لا، جميع الحسابات تتم في متصفحك فقط."},
            {"q": "هل يمكن استخدامها على الجوال؟", "a": "نعم، الموقع متوافق مع جميع الأجهزة."}
        ]
    else:
        return [
            {"q": f"Is {title} free?", "a": "Yes, all calculators on Hasibha are completely free."},
            {"q": "Are results accurate?", "a": "Yes, we use accurate formulas, but results are estimates."},
            {"q": "Is my data saved?", "a": "No, all calculations run in your browser only."},
            {"q": "Does it work on mobile?", "a": "Yes, the site works on all devices."}
        ]


def default_script(calc, lang):
    """يولّد سكربت تلقائي من الحقول"""
    fields = calc['fields']
    reads = []
    sums = []
    for f in fields:
        fid = f['id']
        reads.append(f"  var {fid} = parseFloat(document.getElementById('{fid}').value) || 0;")
        sums.append(fid)
    
    reads_str = "\n".join(reads)
    total_expr = " + ".join(sums)
    currency = 'ريال' if lang == 'ar' else 'SAR'
    
    return f"""function calculate(){{
{reads_str}
  var total = {total_expr};
  var result = total;
  document.getElementById('finalResult').textContent = formatNumber(result) + ' {currency}';
  document.getElementById('resultCard').style.display = 'block';
}}"""


def render_fields(calc, lang):
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
    if not faqs:
        return ""
    title = "الأسئلة الشائعة" if lang == "ar" else "FAQ"
    html = f'<h3>{title}</h3>\n'
    for item in faqs:
        html += f'<div style="margin-bottom:16px"><strong>{item["q"]}</strong><p>{item["a"]}</p></div>\n'
    return html


def render_schema(calc, lang, faqs):
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
    template = load_template()
    
    article = calc.get(f'article_{lang}', '')
    faqs = calc.get(f'faq_{lang}', [])
    script = calc.get('calc_script', '')
    
    if ai_provider and config.get('ai_enabled'):
        if not article:
            print(f"    🤖 توليد مقال ({lang})...")
            try:
                result = ai_provider.generate_article(calc, lang)
                if result and len(result) > 100:
                    article = result
                    print(f"    ✅ مقال ({len(result)} حرف)")
                else:
                    print(f"    ⚠️ رد فاضي - استخدام محتوى افتراضي")
                    article = default_article(calc, lang)
            except Exception as e:
                print(f"    ⚠️ خطأ: {e}")
                article = default_article(calc, lang)
        
        if not faqs:
            print(f"    🤖 توليد أسئلة ({lang})...")
            try:
                result = ai_provider.generate_faq(calc, lang)
                if result and len(result) > 0:
                    faqs = result
                    print(f"    ✅ {len(result)} أسئلة")
                else:
                    print(f"    ⚠️ رد فاضي - استخدام أسئلة افتراضية")
                    faqs = default_faq(calc, lang)
            except Exception as e:
                print(f"    ⚠️ خطأ: {e}")
                faqs = default_faq(calc, lang)
    
    if not article:
        article = default_article(calc, lang)
    if not faqs:
        faqs = default_faq(calc, lang)
    if not script:
        print(f"    ⚙️ استخدام قالب سكربت تلقائي...")
        script = default_script(calc, lang)
    
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


def update_index_page(calculators):
    """يحدّث الصفحة الرئيسية بالبطاقات الجديدة"""
    index_path = os.path.join(ROOT_DIR, 'index.html')
    
    if not os.path.exists(index_path):
        print("⚠️ index.html غير موجود")
        return
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # البحث عن نهاية cardsGrid
    if '<!-- AUTO-GENERATED-START -->' in content:
        pattern = r'\s*<!-- AUTO-GENERATED-START -->.*?<!-- AUTO-GENERATED-END -->'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # بناء البطاقات
    cards_html = '\n      <!-- AUTO-GENERATED-START -->\n'
    for calc in calculators:
        cat = calc.get('category', 'fin')
        slug = calc['slug']
        title = calc['title_ar']
        desc = calc['description_ar']
        icon = calc.get('icon', '🧮')
        
        # تحديد فئة CSS
        cat_class = 'fin'
        if cat in ['conversion', 'conv']:
            cat_class = 'conv'
        elif cat in ['health']:
            cat_class = 'health'
        elif cat in ['general', 'gen']:
            cat_class = 'gen'
        
        cards_html += f'      <a class="card {cat_class}" href="/{slug}" data-cat="{cat_class}" data-title="{title}">\n'
        cards_html += f'        <span class="card-icon">{icon}</span>\n'
        cards_html += f'        <div><h3>{title}</h3><p>{desc}</p></div>\n'
        cards_html += f'        <span class="card-cta">احسب الآن ←</span>\n'
        cards_html += f'      </a>\n'
    cards_html += '      <!-- AUTO-GENERATED-END -->\n    '
    
    # نضيف قبل closing div of cardsGrid
    # نبحث عن النمط
    target = '    </div>\n    <p class="empty-msg"'
    if target in content:
        content = content.replace(target, cards_html + '</div>\n    <p class="empty-msg"', 1)
    else:
        # بديل
        target2 = '</div>\n    <p class="empty-msg"'
        if target2 in content:
            content = content.replace(target2, cards_html + '</div>\n    <p class="empty-msg"', 1)
        else:
            print("⚠️ لم يتم العثور على نهاية cardsGrid")
            return
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ تم تحديث index.html بـ {len(calculators)} بطاقة")


def main():
    config = load_config()
    
    ai_provider = None
    if config.get('ai_enabled'):
        provider_name = config.get('ai_provider', 'gemini')
        api_key = get_api_key(provider_name)
        
        if api_key:
            try:
                ai_provider = get_provider(provider_name, api_key, config.get('ai_model'))
                print(f"🤖 AI: {provider_name} ({config.get('ai_model', 'default')})")
            except Exception as e:
                print(f"⚠️ خطأ في تحميل AI: {e}")
        else:
            print(f"⚠️ لا يوجد مفتاح API")
    
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
    
    print(f"\n📝 تحديث الصفحة الرئيسية...")
    update_index_page(calculators)
    
    print("\n🎉 اكتمل!")


if __name__ == "__main__":
    main()
