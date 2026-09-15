#!/usr/bin/env python3
"""
توليد المحتوى الفريد بالذكاء الاصطناعي
يضيف محتوى 500+ كلمة لكل حاسبة
"""

import os
import re
import json
import time
import urllib.request
import urllib.parse

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY', '')

# استيراد الحاسبات من ملف الإعدادات أو تعريفها هنا
try:
    from config import PAGES
except ImportError:
    PAGES = [
        {"slug": "mortgage", "title_ar": "حاسبة التمويل العقاري", "desc_ar": "قسطك الشهري وقدرتك على الشراء لأي عقار سكني.", "category": "finance"},
        {"slug": "personal-loan", "title_ar": "حاسبة التمويل الشخصي", "desc_ar": "القسط الشهري والفائدة لأي مبلغ ومدة تمويل.", "category": "finance"},
        {"slug": "eos", "title_ar": "حاسبة نهاية الخدمة", "desc_ar": "مكافأتك وفق نظام العمل السعودي — استقالة أو فصل.", "category": "finance"},
        {"slug": "vat", "title_ar": "حاسبة ضريبة القيمة المضافة", "desc_ar": "إضافة أو استبعاد 15% من أي مبلغ في ثانية.", "category": "finance"},
        {"slug": "salary", "title_ar": "الراتب بعد التأمينات", "desc_ar": "صافي راتبك بعد خصم التأمينات الاجتماعية (GOSI).", "category": "finance"},
        {"slug": "zakat", "title_ar": "حاسبة الزكاة", "desc_ar": "احسب زكاة أموالك بدقة وفق الأحكام الشرعية", "category": "finance"},
        {"slug": "gold-value", "title_ar": "حاسبة قيمة الذهب", "desc_ar": "احسب قيمة الذهب حسب الوزن والعيار والسعر الحالي", "category": "finance"},
        {"slug": "currency", "title_ar": "تحويل العملات", "desc_ar": "ريال سعودي، دولار، يورو وأكثر — بأسعار محدثة.", "category": "conversion"},
        {"slug": "length", "title_ar": "تحويل الطول", "desc_ar": "أمتار، أقدام، إنشات وبوصات بضغطة واحدة.", "category": "conversion"},
        {"slug": "weight", "title_ar": "تحويل الوزن", "desc_ar": "كيلوغرام، رطل، أونصة وجرام بدقة كاملة.", "category": "conversion"},
        {"slug": "area", "title_ar": "تحويل المساحة", "desc_ar": "متر مربع، فدان، هكتار وكيلومتر مربع.", "category": "conversion"},
        {"slug": "bmi", "title_ar": "مؤشر كتلة الجسم BMI", "desc_ar": "وزنك المثالي وتصنيفك الصحي بالتفصيل.", "category": "health"},
        {"slug": "calorie", "title_ar": "حاسبة السعرات الحرارية", "desc_ar": "احتياجك اليومي من الطاقة حسب نشاطك وهدفك.", "category": "health"},
        {"slug": "water", "title_ar": "حاسبة احتياج الماء", "desc_ar": "كم لتر يحتاج جسمك يوميًا بناءً على وزنك.", "category": "health"},
        {"slug": "age", "title_ar": "حاسبة العمر", "desc_ar": "عمرك بالسنوات والأشهر والأيام بدقة كاملة.", "category": "general"},
        {"slug": "discount", "title_ar": "حاسبة نسبة الخصم", "desc_ar": "كم وفّرت فعلًا من السعر الأصلي في التخفيضات.", "category": "general"},
        {"slug": "date-diff", "title_ar": "الوقت بين تاريخين", "desc_ar": "الفارق بين أي تاريخين بالأيام والشهور والسنوات.", "category": "general"},
    ]

def call_deepseek(prompt, max_tokens=3000):
    """استدعاء DeepSeek API"""
    if not DEEPSEEK_API_KEY:
        print("  ⚠️ DeepSeek API Key غير موجود")
        return None
    
    try:
        data = json.dumps({
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "أنت كاتب محتوى محترف متخصص في الحاسبات المالية والصحية للسوق السعودي. تجيب فقط بمحتوى HTML صالح بدون أي شرح إضافي."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.5,
            "max_tokens": max_tokens
        }).encode('utf-8')
        
        req = urllib.request.Request(
            "https://api.deepseek.com/v1/chat/completions",
            data=data,
            headers={
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                "Content-Type": "application/json"
            }
        )
        
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result['choices'][0]['message']['content']
    except Exception as e:
        print(f"  ⚠️ DeepSeek error: {e}")
        return None

def generate_unique_content(page):
    """توليد محتوى فريد للحاسبة"""
    
    prompt = f"""أكتب مقالاً شاملاً عن {page['title_ar']} للسوق السعودي.

المتطلبات:
1. عنوان رئيسي (H2) جذاب يتضمن الكلمة المفتاحية
2. مقدمة جذابة (100 كلمة) تشرح أهمية الحاسبة
3. شرح مفصل لكيفية عمل الحاسبة (200 كلمة)
4. مثال عملي بالأرقام (100 كلمة)
5. نصائح مهمة للمستخدم السعودي (100 كلمة)
6. 3 أسئلة شائعة مع إجابات مختصرة

أكتب بصيغة HTML صالحة بدون <html> و <body> و <head>.
استخدم فقط: <h2>, <h3>, <p>, <ul>, <li>, <strong>, <em>
لا تستخدم أي تعليقات أو شرح إضافي.
"""
    
    content = call_deepseek(prompt)
    return content

def add_related_links(page, all_pages):
    """توليد روابط داخلية ذات صلة"""
    
    # ابحث عن حاسبات من نفس التصنيف
    related = [p for p in all_pages if p.get('category') == page.get('category') and p['slug'] != page['slug']][:3]
    
    if not related:
        # لو ما فيه نفس التصنيف، خذ أول 3 حاسبات
        related = [p for p in all_pages if p['slug'] != page['slug']][:3]
    
    if not related:
        return ""
    
    links_html = '\n<div class="related-calculators" style="margin-top:32px;padding:24px;background:var(--card);border-radius:16px;border:1px solid var(--border)">\n'
    links_html += '<h3 style="margin-bottom:16px;font-size:18px">حاسبات ذات صلة</h3>\n'
    links_html += '<ul style="list-style:none;padding:0;margin:0">\n'
    for rel in related:
        links_html += f'<li style="margin-bottom:8px"><a href="/{rel["slug"]}" style="color:var(--accent);text-decoration:none">← {rel["title_ar"]}</a></li>\n'
    links_html += '</ul>\n</div>\n'
    
    return links_html

def add_content_to_page(page, html_content):
    """إضافة المحتوى الفريد للصفحة"""
    
    # التحقق من وجود المحتوى مسبقاً
    if 'ai-content' in html_content:
        print(f"    ℹ️ المحتوى موجود مسبقاً")
        return html_content
    
    print(f"  📝 توليد محتوى فريد...")
    content = generate_unique_content(page)
    
    if not content:
        print(f"    ⚠️ فشل توليد المحتوى")
        return html_content
    
    # إضافة الروابط الداخلية
    related_links = add_related_links(page, PAGES)
    
    # البحث عن نهاية الـ article-box لإضافة المحتوى
    article_end = html_content.find('</div>\n</div>\n</main>')
    if article_end == -1:
        # جرب نمط آخر
        article_end = html_content.find('</article-box>')
        if article_end == -1:
            article_end = html_content.find('</main>')
    
    if article_end != -1:
        new_content = f'\n<div class="ai-content" style="margin-top:32px">\n{content}\n</div>\n{related_links}'
        html_content = html_content[:article_end] + new_content + html_content[article_end:]
        print(f"    ✅ تم إضافة المحتوى ({len(content)} حرف)")
    else:
        print(f"    ⚠️ لم أجد مكان لإضافة المحتوى")
    
    return html_content

def main():
    print("📝 بدء توليد المحتوى الفريد...")
    print(f"📊 عدد الحاسبات: {len(PAGES)}")
    
    if not DEEPSEEK_API_KEY:
        print("❌ خطأ: يجب تعيين DEEPSEEK_API_KEY")
        print("   أضف الـ Secret في: Settings → Secrets and variables → Actions")
        return
    
    for i, page in enumerate(PAGES, 1):
        print(f"\n[{i}/{len(PAGES)}] 🔨 {page['title_ar']}")
        
        ar_path = os.path.join(ROOT_DIR, f"{page['slug']}.html")
        if os.path.exists(ar_path):
            with open(ar_path, 'r', encoding='utf-8') as f:
                html = f.read()
            
            updated_html = add_content_to_page(page, html)
            
            with open(ar_path, 'w', encoding='utf-8') as f:
                f.write(updated_html)
        else:
            print(f"    ⚠️ الملف غير موجود: {page['slug']}.html")
        
        time.sleep(2)  # تجنب الـ rate limit
    
    print("\n🎉 اكتمل توليد المحتوى!")

if __name__ == "__main__":
    main()
