#!/usr/bin/env python3
"""
توليد المحتوى الفريد - النسخة النهائية
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

def call_gemini(prompt, max_tokens=2500):
    """استدعاء Gemini بالطريقة المؤكدة"""
    if not GEMINI_API_KEY:
        return None
    
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"
    
    try:
        data = json.dumps({
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature": 0.7,
                "maxOutputTokens": max_tokens
            }
        }).encode('utf-8')
        
        req = urllib.request.Request(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "x-goog-api-key": GEMINI_API_KEY
            }
        )
        
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode('utf-8'))
            if 'candidates' in result and result['candidates']:
                return result['candidates'][0]['content']['parts'][0]['text']
                
    except urllib.error.HTTPError as e:
        if e.code == 503:
            print(f"    ⏳ السيرفر مزدحم، انتظار 15 ثانية...")
            time.sleep(15)
            try:
                with urllib.request.urlopen(req, timeout=120) as response:
                    result = json.loads(response.read().decode('utf-8'))
                    if 'candidates' in result and result['candidates']:
                        return result['candidates'][0]['content']['parts'][0]['text']
            except:
                pass
        else:
            error_body = e.read().decode('utf-8', errors='ignore')
            print(f"    ⚠️ خطأ {e.code}: {error_body[:150]}")
    except Exception as e:
        print(f"    ⚠️ خطأ: {e}")
    
    return None

def generate_content(page):
    prompt = f"""أنت كاتب محتوى محترف متخصص في السوق السعودي.
اكتب مقالاً شاملاً عن "{page['title_ar']}" باللغة العربية الفصحى.

المتطلبات:
1. عنوان رئيسي جذاب (H2) يتضمن الكلمة المفتاحية والسنة 2026
2. مقدمة جذابة (100 كلمة) تشرح أهمية الحاسبة للمستخدم السعودي
3. شرح مفصل لكيفية عمل الحاسبة (200 كلمة) مع خطوات واضحة
4. مثال عملي بأرقام حقيقية من السوق السعودي (100 كلمة)
5. ثلاث نصائح مهمة للمستخدم السعودي (100 كلمة)
6. ثلاثة أسئلة شائعة مع إجابات مختصرة ودقيقة

القواعد:
- اذكر الأنظمة السعودية ذات الصلة (نظام العمل، التأمينات الاجتماعية، هيئة الزكاة والضريبة والجمارك)
- استخدم أرقام ونسب واقعية من السوق السعودي 2026
- اجعل المحتوى فريداً ومفيداً ومختلفاً عن المنافسين
- اكتب بأسلوب احترافي وسهل الفهم

أجب فقط بمحتوى HTML صالح باستخدام: h2, h3, p, ul, ol, li, strong, em
لا تستخدم أي تعليقات أو شرح خارج الوسوم."""
    
    return call_gemini(prompt)

def add_related_links(page, all_pages):
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
    print("📝 توليد المحتوى الفريد (النسخة النهائية)...")
    print(f"📊 عدد الحاسبات: {len(PAGES)}")
    print(f"🎯 الموديل: gemini-flash-latest")
    
    if not GEMINI_API_KEY:
        print("❌ خطأ: GEMINI_API_KEY غير موجود")
        return
    
    success = 0
    skipped = 0
    
    for i, page in enumerate(PAGES, 1):
        print(f"\n[{i}/{len(PAGES)}] 🔨 {page['title_ar']}")
        
        ar_path = os.path.join(ROOT_DIR, f"{page['slug']}.html")
        if not os.path.exists(ar_path):
            print(f"    ⚠️ الملف غير موجود")
            continue
        
        with open(ar_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        if 'ai-content' in html:
            print(f"    ℹ️ المحتوى موجود مسبقاً")
            skipped += 1
            continue
        
        print(f"    🤖 جاري التوليد...")
        content = generate_content(page)
        
        if content:
            # تنظيف المحتوى
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
                success += 1
            else:
                print(f"    ⚠️ لم أجد مكان للإضافة")
        else:
            print(f"    ❌ فشل التوليد")
        
        time.sleep(3)
    
    print(f"\n{'='*60}")
    print(f"📊 النتيجة النهائية:")
    print(f"  ✅ تم التوليد: {success}")
    print(f"  ℹ️ تم التخطي: {skipped}")
    print(f"🎉 اكتمل!")

if __name__ == "__main__":
    main()
