#!/usr/bin/env python3
"""
توليد المحتوى الفريد بالذكاء الاصطناعي - Gemini (مجاني)
"""

import os
import json
import time
import urllib.request
import urllib.error

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')

try:
    from config import PAGES
except ImportError:
    PAGES = [
        {"slug": "mortgage", "title_ar": "حاسبة التمويل العقاري", "category": "finance"},
        {"slug": "personal-loan", "title_ar": "حاسبة التمويل الشخصي", "category": "finance"},
        {"slug": "eos", "title_ar": "حاسبة نهاية الخدمة", "category": "finance"},
        {"slug": "vat", "title_ar": "حاسبة ضريبة القيمة المضافة", "category": "finance"},
        {"slug": "salary", "title_ar": "الراتب بعد التأمينات", "category": "finance"},
        {"slug": "zakat", "title_ar": "حاسبة الزكاة", "category": "finance"},
        {"slug": "gold-value", "title_ar": "حاسبة قيمة الذهب", "category": "finance"},
        {"slug": "currency", "title_ar": "تحويل العملات", "category": "conversion"},
        {"slug": "length", "title_ar": "تحويل الطول", "category": "conversion"},
        {"slug": "weight", "title_ar": "تحويل الوزن", "category": "conversion"},
        {"slug": "area", "title_ar": "تحويل المساحة", "category": "conversion"},
        {"slug": "bmi", "title_ar": "مؤشر كتلة الجسم", "category": "health"},
        {"slug": "calorie", "title_ar": "حاسبة السعرات الحرارية", "category": "health"},
        {"slug": "water", "title_ar": "حاسبة احتياج الماء", "category": "health"},
        {"slug": "age", "title_ar": "حاسبة العمر", "category": "general"},
        {"slug": "discount", "title_ar": "حاسبة نسبة الخصم", "category": "general"},
        {"slug": "date-diff", "title_ar": "الوقت بين تاريخين", "category": "general"},
    ]

def call_gemini(prompt):
    """استدعاء Gemini API مع عدة موديلات"""
    if not GEMINI_API_KEY:
        print("  ⚠️ لا يوجد GEMINI_API_KEY")
        return None
    
    # قائمة الموديلات المتاحة (نجرب كل واحد حتى ينجح)
    models = [
        "gemini-2.5-flash",
        "gemini-2.5-flash-lite",
        "gemini-2.0-flash",
        "gemini-1.5-flash",
        "gemini-1.5-pro",
    ]
    
    for model in models:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_API_KEY}"
            
            data = json.dumps({
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"temperature": 0.7, "maxOutputTokens": 2500}
            }).encode('utf-8')
            
            req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
            
            with urllib.request.urlopen(req, timeout=120) as response:
                result = json.loads(response.read().decode('utf-8'))
                if 'candidates' in result and result['candidates']:
                    print(f"    ✓ باستخدام {model}")
                    return result['candidates'][0]['content']['parts'][0]['text']
        except urllib.error.HTTPError as e:
            # جرب الموديل التالي
            continue
        except Exception as e:
            continue
    
    print("  ⚠️ فشلت جميع الموديلات")
    return None

def generate_content(page):
    """توليد محتوى فريد للحاسبة"""
    prompt = f"""أنت كاتب محتوى محترف متخصص في السوق السعودي.
اكتب مقالاً شاملاً عن "{page['title_ar']}" باللغة العربية.

المتطلبات:
1. عنوان رئيسي جذاب (H2) يتضمن الكلمة المفتاحية والسنة 2026
2. مقدمة جذابة (100 كلمة) تشرح أهمية الحاسبة
3. شرح مفصل لكيفية عمل الحاسبة (200 كلمة)
4. مثال عملي بالأرقام الحقيقية من السوق السعودي (100 كلمة)
5. 3 نصائح مهمة للمستخدم السعودي (100 كلمة)
6. 3 أسئلة شائعة مع إجابات مختصرة

القواعد:
- استخدم لغة عربية فصحى واضحة
- اذكر الأرقام والنسب السعودية الحقيقية
- اذكر الأنظمة السعودية ذات الصلة (نظام العمل، التأمينات، إلخ)
- اجعل المحتوى مفيد ومختلف عن المنافسين

أجب فقط بمحتوى HTML صالح باستخدام الوسوم: h2, h3, p, ul, li, strong, em
لا تستخدم أي تعليقات أو شرح إضافي.
لا تضع أي نص خارج الوسوم HTML.
"""
    return call_gemini(prompt)

def add_related_links(page, all_pages):
    """توليد روابط داخلية ذات صلة"""
    related = [p for p in all_pages if p.get('category') == page.get('category') and p['slug'] != page['slug']][:3]
    
    if not related:
        related = [p for p in all_pages if p['slug'] != page['slug']][:3]
    
    if not related:
        return ""
    
    links_html = '\n<div class="related-calculators" style="margin-top:32px;padding:24px;background:var(--card, #fff);border-radius:16px;border:1px solid var(--border, #e2e8f0)">\n'
    links_html += '<h3 style="margin-bottom:16px;font-size:18px">حاسبات ذات صلة</h3>\n'
    links_html += '<ul style="list-style:none;padding:0;margin:0">\n'
    for rel in related:
        links_html += f'<li style="margin-bottom:8px"><a href="/{rel["slug"]}" style="color:var(--accent, #059669);text-decoration:none">← {rel["title_ar"]}</a></li>\n'
    links_html += '</ul>\n</div>\n'
    
    return links_html

def main():
    print("📝 توليد المحتوى الفريد (Gemini - مجاني)...")
    print(f"📊 عدد الحاسبات: {len(PAGES)}")
    
    if not GEMINI_API_KEY:
        print("❌ خطأ: GEMINI_API_KEY غير موجود")
        print("   أضفه في: Settings → Secrets and variables → Actions")
        return
    
    for i, page in enumerate(PAGES, 1):
        print(f"\n[{i}/{len(PAGES)}] 🔨 {page['title_ar']}")
        
        ar_path = os.path.join(ROOT_DIR, f"{page['slug']}.html")
        if not os.path.exists(ar_path):
            print(f"    ⚠️ الملف غير موجود: {page['slug']}.html")
            continue
        
        with open(ar_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        if 'ai-content' in html:
            print(f"    ℹ️ المحتوى موجود مسبقاً - تم التخطي")
            continue
        
        print(f"    🤖 جاري توليد المحتوى...")
        content = generate_content(page)
        
        if content:
            # تنظيف المحتوى من أي markdown أو نص خارج HTML
            content = content.strip()
            if content.startswith('```html'):
                content = content[7:]
            if content.startswith('```'):
                content = content[3:]
            if content.endswith('```'):
                content = content[:-3]
            content = content.strip()
            
            # البحث عن مكان الإضافة
            insert_point = html.find('</div>\n</div>\n</main>')
            if insert_point == -1:
                insert_point = html.find('</main>')
            
            if insert_point != -1:
                related_links = add_related_links(page, PAGES)
                new_block = f'\n<div class="ai-content" style="margin-top:32px;padding:24px;background:var(--card, #fff);border-radius:16px;border:1px solid var(--border, #e2e8f0)">\n{content}\n</div>\n{related_links}'
                html = html[:insert_point] + new_block + html[insert_point:]
                
                with open(ar_path, 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"    ✅ تم ({len(content)} حرف)")
            else:
                print(f"    ⚠️ لم أجد مكان للإضافة")
        else:
            print(f"    ❌ فشل التوليد")
        
        time.sleep(3)  # تجنب rate limit
    
    print("\n🎉 اكتمل!")

if __name__ == "__main__":
    main()
