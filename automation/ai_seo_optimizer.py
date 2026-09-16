#!/usr/bin/env python3
"""
تحسين السيو بالذكاء الاصطناعي - النسخة النهائية
"""

import os
import re
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
        {"slug": "mortgage", "title_ar": "حاسبة التمويل العقاري", "title_en": "Mortgage Calculator", "desc_ar": "قسطك الشهري وقدرتك على الشراء لأي عقار سكني.", "desc_en": "Monthly payment and purchasing power for any residential property."},
        {"slug": "personal-loan", "title_ar": "حاسبة التمويل الشخصي", "title_en": "Personal Loan Calculator", "desc_ar": "القسط الشهري والفائدة لأي مبلغ ومدة تمويل.", "desc_en": "Monthly installment and interest for any amount and term."},
        {"slug": "eos", "title_ar": "حاسبة نهاية الخدمة", "title_en": "End of Service Calculator", "desc_ar": "مكافأتك وفق نظام العمل السعودي — استقالة أو فصل.", "desc_en": "Your benefit according to Saudi Labor Law."},
        {"slug": "vat", "title_ar": "حاسبة ضريبة القيمة المضافة", "title_en": "VAT Calculator", "desc_ar": "إضافة أو استبعاد 15% من أي مبلغ في ثانية.", "desc_en": "Add or exclude 15% from any amount."},
        {"slug": "salary", "title_ar": "الراتب بعد التأمينات", "title_en": "Salary After Insurance", "desc_ar": "صافي راتبك بعد خصم التأمينات الاجتماعية (GOSI).", "desc_en": "Your net salary after GOSI deduction."},
        {"slug": "zakat", "title_ar": "حاسبة الزكاة", "title_en": "Zakat Calculator", "desc_ar": "احسب زكاة أموالك بدقة وفق الأحكام الشرعية", "desc_en": "Calculate your Zakat accurately."},
        {"slug": "gold-value", "title_ar": "حاسبة قيمة الذهب", "title_en": "Gold Value Calculator", "desc_ar": "احسب قيمة الذهب حسب الوزن والعيار والسعر الحالي", "desc_en": "Calculate gold value by weight and karat."},
        {"slug": "currency", "title_ar": "تحويل العملات", "title_en": "Currency Converter", "desc_ar": "ريال سعودي، دولار، يورو وأكثر — بأسعار محدثة.", "desc_en": "SAR, USD, EUR and more with updated rates."},
        {"slug": "length", "title_ar": "تحويل الطول", "title_en": "Length Converter", "desc_ar": "أمتار، أقدام، إنشات وبوصات بضغطة واحدة.", "desc_en": "Meters, feet, inches in one click."},
        {"slug": "weight", "title_ar": "تحويل الوزن", "title_en": "Weight Converter", "desc_ar": "كيلوغرام، رطل، أونصة وجرام بدقة كاملة.", "desc_en": "Kilograms, pounds, ounces and grams."},
        {"slug": "area", "title_ar": "تحويل المساحة", "title_en": "Area Converter", "desc_ar": "متر مربع، فدان، هكتار وكيلومتر مربع.", "desc_en": "Square meters, acres, hectares."},
        {"slug": "bmi", "title_ar": "مؤشر كتلة الجسم", "title_en": "BMI Calculator", "desc_ar": "وزنك المثالي وتصنيفك الصحي بالتفصيل.", "desc_en": "Your ideal weight and health classification."},
        {"slug": "calorie", "title_ar": "حاسبة السعرات الحرارية", "title_en": "Calorie Calculator", "desc_ar": "احتياجك اليومي من الطاقة حسب نشاطك وهدفك.", "desc_en": "Daily energy needs based on activity."},
        {"slug": "water", "title_ar": "حاسبة احتياج الماء", "title_en": "Water Intake Calculator", "desc_ar": "كم لتر يحتاج جسمك يوميًا بناءً على وزنك.", "desc_en": "How many liters your body needs daily."},
        {"slug": "age", "title_ar": "حاسبة العمر", "title_en": "Age Calculator", "desc_ar": "عمرك بالسنوات والأشهر والأيام بدقة كاملة.", "desc_en": "Your exact age in years, months and days."},
        {"slug": "discount", "title_ar": "حاسبة نسبة الخصم", "title_en": "Discount Calculator", "desc_ar": "كم وفّرت فعلًا من السعر الأصلي في التخفيضات.", "desc_en": "How much you saved from the original price."},
        {"slug": "date-diff", "title_ar": "الوقت بين تاريخين", "title_en": "Date Difference", "desc_ar": "الفارق بين أي تاريخين بالأيام والشهور والسنوات.", "desc_en": "The gap between any two dates."},
    ]

def call_gemini(prompt, max_tokens=1000):
    """استدعاء Gemini بالطريقة المؤكدة: Header + gemini-flash-latest"""
    if not GEMINI_API_KEY:
        return None
    
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"
    
    try:
        data = json.dumps({
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature": 0.3,
                "maxOutputTokens": max_tokens,
                "responseMimeType": "application/json"
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
        
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode('utf-8'))
            if 'candidates' in result and result['candidates']:
                return result['candidates'][0]['content']['parts'][0]['text']
                
    except urllib.error.HTTPError as e:
        if e.code == 503:
            print(f"    ⏳ السيرفر مزدحم، انتظار 10 ثواني...")
            time.sleep(10)
            try:
                with urllib.request.urlopen(req, timeout=60) as response:
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

def generate_seo_metadata(page):
    prompt = f"""You are an SEO expert for the Saudi Arabian market.
Generate optimized SEO metadata for this calculator:

Arabic Name: {page['title_ar']}
Arabic Description: {page['desc_ar']}
English Name: {page['title_en']}
English Description: {page['desc_en']}

Return valid JSON with these exact fields:
{{
  "title_ar": "Arabic title 50-60 chars, include 2026 and main keyword",
  "description_ar": "Arabic description 150-160 chars with call to action",
  "title_en": "English title 50-60 chars, include 2026 and main keyword",
  "description_en": "English description 150-160 chars with call to action",
  "keywords": "5 keywords separated by comma"
}}

Rules:
- Include year 2026 in titles
- Main keyword at the beginning
- Add compelling call-to-action
- Target Saudi users specifically"""
    
    result = call_gemini(prompt)
    if result:
        # تنظيف الرد من أي علامات
        result = result.strip()
        if result.startswith('```json'):
            result = result[7:]
        if result.startswith('```'):
            result = result[3:]
        if result.endswith('```'):
            result = result[:-3]
        result = result.strip()
        
        # البحث عن JSON
        json_match = re.search(r'\{[\s\S]*\}', result)
        if json_match:
            try:
                return json.loads(json_match.group())
            except:
                pass
        # محاولة مباشرة
        try:
            return json.loads(result)
        except:
            pass
    
    return None

def update_meta_tag(html, tag_name, new_value):
    pattern = rf'<meta name="{tag_name}" content="[^"]*"'
    replacement = f'<meta name="{tag_name}" content="{new_value}"'
    return re.sub(pattern, replacement, html)

def optimize_page(page, lang='ar'):
    slug = page['slug'] if lang == 'ar' else f"{page['slug']}-en"
    path = os.path.join(ROOT_DIR, f"{slug}.html")
    
    if not os.path.exists(path):
        return None
    
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    seo_data = generate_seo_metadata(page)
    if not seo_data:
        print(f"    ⚠️ فشل التوليد")
        return None
    
    title = seo_data.get('title_ar' if lang == 'ar' else 'title_en', '')
    desc = seo_data.get('description_ar' if lang == 'ar' else 'description_en', '')
    keywords = seo_data.get('keywords', '')
    
    changes = 0
    
    if title:
        html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html)
        changes += 1
    
    if desc:
        new_html = update_meta_tag(html, 'description', desc)
        if new_html != html:
            html = new_html
            changes += 1
    
    if keywords:
        new_html = update_meta_tag(html, 'keywords', keywords)
        if new_html != html:
            html = new_html
            changes += 1
    
    if changes > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"    ✅ تم ({changes} تغييرات): {title[:50]}")
        return seo_data
    
    return None

def main():
    print("🤖 بدء تحسين السيو (النسخة النهائية)...")
    print(f"📊 عدد الحاسبات: {len(PAGES)}")
    print(f"🎯 الموديل: gemini-flash-latest")
    
    if not GEMINI_API_KEY:
        print("❌ خطأ: GEMINI_API_KEY غير موجود")
        return
    
    success = 0
    fail = 0
    
    for i, page in enumerate(PAGES, 1):
        print(f"\n[{i}/{len(PAGES)}] 🔨 {page['title_ar']}")
        
        # العربية
        print(f"  📄 الصفحة العربية...")
        if optimize_page(page, 'ar'):
            success += 1
        else:
            fail += 1
        
        time.sleep(2)
        
        # الإنجليزية
        print(f"  📄 الصفحة الإنجليزية...")
        if optimize_page(page, 'en'):
            success += 1
        else:
            fail += 1
        
        time.sleep(2)
    
    print(f"\n{'='*60}")
    print(f"📊 النتيجة النهائية:")
    print(f"  ✅ نجح: {success}")
    print(f"  ❌ فشل: {fail}")
    print(f"🎉 اكتمل!")

if __name__ == "__main__":
    main()
