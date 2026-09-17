#!/usr/bin/env python3
"""
توليد المحتوى الفريد بالذكاء الاصطناعي - DeepSeek
يدعم الاستئناف الذكي + أنماط متوافقة مع الموقع
"""

import os
import re
import json
import time
import urllib.request
import urllib.error

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

def call_deepseek(prompt, max_tokens=2500, max_retries=3):
    """استدعاء DeepSeek API مع إعادة المحاولة"""
    if not DEEPSEEK_API_KEY:
        print("  ⚠️ DEEPSEEK_API_KEY غير موجود")
        return None
    
    url = "https://api.deepseek.com/chat/completions"
    
    for attempt in range(max_retries):
        try:
            data = json.dumps({
                "model": "deepseek-chat",
                "messages": [
                    {
                        "role": "system",
                        "content": "أنت كاتب محتوى محترف متخصص في السوق السعودي والحاسبات المالية والصحية. تكتب محتوى فريد ومفيد باللغة العربية الفصحى بأسلوب احترافي."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.7,
                "max_tokens": max_tokens
            }).encode('utf-8')
            
            req = urllib.request.Request(
                url,
                data=data,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
                }
            )
            
            with urllib.request.urlopen(req, timeout=120) as response:
                result = json.loads(response.read().decode('utf-8'))
                if 'choices' in result and result['choices']:
                    return result['choices'][0]['message']['content']
                    
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8', errors='ignore')
            
            if e.code == 429:
                wait = 30 * (attempt + 1)
                print(f"    ⏳ تجاوز الحد، انتظار {wait} ثانية...")
                time.sleep(wait)
                continue
            elif e.code == 500 or e.code == 503:
                wait = 15 * (attempt + 1)
                print(f"    ⏳ خطأ في السيرفر، انتظار {wait} ثانية...")
                time.sleep(wait)
                continue
            else:
                print(f"    ⚠️ خطأ {e.code}: {error_body[:200]}")
                break
        except Exception as e:
            print(f"    ⚠️ خطأ: {e}")
            if attempt < max_retries - 1:
                time.sleep(10)
                continue
            break
    
    return None

def clean_html_content(content):
    """تنظيف المحتوى من علامات markdown وأي نص خارج HTML"""
    if not content:
        return ""
    
    content = content.strip()
    
    # إزالة ``` من البداية والنهاية
    if content.startswith('```html'):
        content = content[7:]
    if content.startswith('```'):
        content = content[3:]
    if content.endswith('```'):
        content = content[:-3]
    
    content = content.strip()
    
    # إزالة أي أنماط مضمنة قديمة (لأن الأنماط الآن في CSS)
    content = re.sub(r'\s*style="[^"]*"', '', content)
    
    # إزالة أي class قديمة
    content = re.sub(r'\s*class="[^"]*"', '', content)
    
    return content

def generate_content(page):
    """توليد محتوى فريد للحاسبة"""
    
    category_info = {
        "finance": "مالية",
        "conversion": "تحويلات",
        "health": "صحية",
        "general": "عامة"
    }
    
    category_ar = category_info.get(page.get('category', 'general'), 'عامة')
    
    prompt = f"""اكتب مقالاً شاملاً وفريداً باللغة العربية الفصحى عن "{page['title_ar']}" للسوق السعودي.

المتطلبات:
1. عنوان رئيسي جذاب (H2) يتضمن الكلمة المفتاحية والسنة 2026
2. مقدمة جذابة (100 كلمة) تشرح أهمية الحاسبة للمستخدم السعودي
3. شرح مفصل لكيفية عمل الحاسبة (200 كلمة) مع خطوات واضحة
4. مثال عملي بأرقام حقيقية من السوق السعودي (100 كلمة)
5. ثلاث نصائح مهمة للمستخدم السعودي (100 كلمة)
6. ثلاثة أسئلة شائعة مع إجابات مختصرة ودقيقة

القواعد:
- اذكر الأنظمة السعودية ذات الصلة (نظام العمل، التأمينات الاجتماعية، هيئة الزكاة والضريبة والجمارك، مؤسسة النقد السعودي)
- استخدم أرقام ونسب واقعية من السوق السعودي 2026
- اجعل المحتوى فريداً ومفيداً ومختلفاً عن المنافسين
- اكتب بأسلوب احترافي وسهل الفهم
- استخدم صيغة الجمع للمخاطبة (مثال: "احسب، تعرف، اكتشف")
- هذه حاسبة {category_ar}، فاجعل المحتوى مناسباً لهذا التصنيف

أجب فقط بمحتوى HTML صالح باستخدام هذه الوسوم فقط:
h2, h3, p, ul, ol, li, strong, em

ممنوع:
- أي تعليقات
- أي شرح خارج الوسوم
- أي أنماط مضمنة (style="...")
- أي classes"""
    
    result = call_deepseek(prompt)
    if result:
        return clean_html_content(result)
    return None

def add_related_links(page, all_pages):
    """توليد روابط داخلية ذات صلة (بدون أنماط مضمنة)"""
    
    # البحث عن حاسبات من نفس التصنيف
    related = [p for p in all_pages if p.get('category') == page.get('category') and p['slug'] != page['slug']][:3]
    
    if not related:
        related = [p for p in all_pages if p['slug'] != page['slug']][:3]
    
    if not related:
        return ""
    
    links_html = '\n<div class="related-calculators">\n'
    links_html += '<h3>🔗 حاسبات ذات صلة</h3>\n'
    links_html += '<ul>\n'
    for rel in related:
        links_html += f'<li><a href="/{rel["slug"]}">← {rel["title_ar"]}</a></li>\n'
    links_html += '</ul>\n</div>\n'
    
    return links_html

def main():
    print("📝 توليد المحتوى الفريد (DeepSeek)...")
    print(f"📊 عدد الحاسبات: {len(PAGES)}")
    
    if not DEEPSEEK_API_KEY:
        print("❌ خطأ: DEEPSEEK_API_KEY غير موجود")
        print("   أضفه في: Settings → Secrets and variables → Actions")
        return
    
    success = 0
    skipped = 0
    fail = 0
    
    for i, page in enumerate(PAGES, 1):
        print(f"\n[{i}/{len(PAGES)}] 🔨 {page['title_ar']}")
        
        ar_path = os.path.join(ROOT_DIR, f"{page['slug']}.html")
        if not os.path.exists(ar_path):
            print(f"    ⚠️ الملف غير موجود: {page['slug']}.html")
            fail += 1
            continue
        
        with open(ar_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # التحقق من وجود المحتوى مسبقاً (الاستئناف الذكي)
        if 'ai-content' in html:
            print(f"    ℹ️ المحتوى موجود مسبقاً - تم التخطي")
            skipped += 1
            continue
        
        print(f"    🤖 جاري توليد المحتوى...")
        content = generate_content(page)
        
        if content:
            # البحث عن مكان الإضافة (قبل </main> أو قبل نهاية article-box)
            insert_point = html.find('</div>\n</div>\n</main>')
            if insert_point == -1:
                insert_point = html.find('</div>\n</main>')
            if insert_point == -1:
                insert_point = html.find('</main>')
            
            if insert_point != -1:
                related_links = add_related_links(page, PAGES)
                new_block = f'\n<div class="ai-content">\n{content}\n</div>\n{related_links}'
                html = html[:insert_point] + new_block + html[insert_point:]
                
                with open(ar_path, 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"    ✅ تم إضافة المحتوى ({len(content)} حرف)")
                success += 1
            else:
                print(f"    ⚠️ لم أجد مكاناً للإضافة في الملف")
                fail += 1
        else:
            print(f"    ❌ فشل التوليد")
            fail += 1
        
        time.sleep(2)
    
    print(f"\n{'='*60}")
    print(f"📊 النتيجة النهائية:")
    print(f"  ✅ تم التوليد: {success}")
    print(f"  ℹ️ تم التخطي: {skipped}")
    print(f"  ❌ فشل: {fail}")
    print(f"🎉 اكتمل!")

if __name__ == "__main__":
    main()
