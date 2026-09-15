#!/usr/bin/env python3
"""
توليد المحتوى الفريد بالذكاء الاصطناعي
"""

import os
import json
import time
import urllib.request

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY', '')

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

def call_deepseek(prompt):
    if not DEEPSEEK_API_KEY:
        print("  ⚠️ لا يوجد API Key")
        return None
    try:
        data = json.dumps({
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "أنت كاتب محتوى محترف. تجيب فقط بمحتوى HTML صالح."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.5,
            "max_tokens": 2500
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
        print(f"  ⚠️ خطأ: {e}")
        return None

def generate_content(page):
    prompt = f"""اكتب مقالاً عن {page['title_ar']} للسوق السعودي:
- عنوان رئيسي (H2)
- مقدمة (100 كلمة)
- شرح الحاسبة (200 كلمة)
- مثال عملي (100 كلمة)
- 3 أسئلة شائعة مع إجابات

أجب بصيغة HTML فقط (h2, h3, p, ul, li)."""
    return call_deepseek(prompt)

def main():
    print("📝 توليد المحتوى الفريد...")
    if not DEEPSEEK_API_KEY:
        print("❌ DEEPSEEK_API_KEY غير موجود")
        return
    
    for i, page in enumerate(PAGES, 1):
        print(f"\n[{i}/{len(PAGES)}] {page['title_ar']}")
        ar_path = os.path.join(ROOT_DIR, f"{page['slug']}.html")
        if not os.path.exists(ar_path):
            print(f"    ⚠️ الملف غير موجود")
            continue
        
        with open(ar_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        if 'ai-content' in html:
            print(f"    ℹ️ المحتوى موجود")
            continue
        
        content = generate_content(page)
        if content:
            insert_point = html.find('</main>')
            if insert_point != -1:
                new_block = f'\n<div class="ai-content" style="margin-top:32px">{content}</div>\n'
                html = html[:insert_point] + new_block + html[insert_point:]
                with open(ar_path, 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"    ✅ تم ({len(content)} حرف)")
        
        time.sleep(2)
    
    print("\n🎉 اكتمل!")

if __name__ == "__main__":
    main()
