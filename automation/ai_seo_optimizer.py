#!/usr/bin/env python3
"""
تحسين السيو بالذكاء الاصطناعي - Gemini (مُحسّن 2026)
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

def call_gemini(prompt, max_tokens=1000, max_retries=3):
    """استدعاء Gemini API مع retry للـ 503 وأسماء موديلات حديثة"""
    if not GEMINI_API_KEY:
        print("  ⚠️ لا يوجد GEMINI_API_KEY")
        return None
    
    # 🆕 أسماء الموديلات الحديثة (2026)
    models = [
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-1.5-flash",  # كـ fallback
    ]
    
    for model in models:
        for attempt in range(max_retries):
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
                
                data = json.dumps({
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {
                        "temperature": 0.3,
                        "maxOutputTokens": max_tokens,
                        "responseMimeType": "application/json"  # 🆕 إجبار JSON
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
                        text = result['candidates'][0]['content']['parts'][0]['text']
                        print(f"    ✓ نجح باستخدام {model}")
                        return text
                        
            except urllib.error.HTTPError as e:
                error_body = e.read().decode('utf-8', errors='ignore')
                
                if e.code == 503:
                    # High demand - ننتظر ونعيد المحاولة
                    wait_time = 5 * (attempt + 1)
                    print(f"    ⏳ {model} مزدحم، انتظار {wait_time}ث...")
                    time.sleep(wait_time)
                    continue
                elif e.code == 429:
                    # Rate limit
                    print(f"    ⏳ Rate limit، انتظار 10ث...")
                    time.sleep(10)
                    continue
                elif e.code == 404:
                    # الموديل غير موجود - جرب التالي
                    break
                else:
                    print(f"    ⚠️ {model}: {e.code}")
                    if attempt == 0:
                        print(f"       {error_body[:200]}")
                    break
                    
            except Exception as e:
                print(f"    ⚠️ خطأ: {e}")
                break
    
    return None

def extract_json(text):
    """استخراج JSON من رد AI حتى لو كان markdown"""
    if not text:
        return None
    
    # 1. إزالة markdown code blocks
    text = text.strip()
    if text.startswith('```json'):
        text = text[7:]
    if text.startswith('```'):
        text = text[3:]
    if text.endswith('```'):
        text = text[:-3]
    text = text.strip()
    
    # 2. محاولة تحليل مباشر
    try:
        return json.loads(text)
    except:
        pass
    
    # 3. البحث عن JSON داخل النص
    json_match = re.search(r'\{[\s\S]*\}', text)
    if json_match:
        try:
            return json.loads(json_match.group())
        except:
            pass
    
    return None

def generate_seo_metadata(page):
    """توليد SEO metadata محسّن"""
    prompt = f"""You are an SEO expert for the Saudi market.
Generate optimized metadata for this calculator:

Name (Arabic): {page['title_ar']}
Current Description (Arabic): {page['desc_ar']}
Name (English): {page['title_en']}
Current Description (English): {page['desc_en']}

Return ONLY valid JSON with these exact fields:
{{
  "title_ar": "Arabic SEO title 50-60 chars with 2026",
  "description_ar": "Arabic meta description 150-160 chars with CTA",
  "title_en": "English SEO title 50-60 chars with 2026",
  "description_en": "English meta description 150-160 chars with CTA",
  "keywords": "keyword1, keyword2, keyword3, keyword4, keyword5"
}}

Requirements:
- Include year 2026
- Include main keyword at start
- Add call-to-action in descriptions
- Make it compelling for Saudi users"""
    
    result = call_gemini(prompt)
    if result:
        data = extract_json(result)
        if data:
            return data
        else:
            print(f"    ⚠️ فشل استخراج JSON من الرد")
            print(f"    📄 الرد: {result[:200]}...")
    return None

def update_meta_tag(html, tag_name, new_value, attr='name'):
    pattern = rf'<meta {attr}="{tag_name}" content="[^"]*"'
    replacement = f'<meta {attr}="{tag_name}" content="{new_value}"'
    return re.sub(pattern, replacement, html)

def optimize_page(page, lang='ar'):
    """تحسين صفحة واحدة"""
    slug = page['slug'] if lang == 'ar' else f"{page['slug']}-en"
    path = os.path.join(ROOT_DIR, f"{slug}.html")
    
    if not os.path.exists(path):
        return None
    
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    lang_label = "العربية" if lang == 'ar' else "الإنجليزية"
    print(f"  🤖 تحسين الصفحة {lang_label}...")
    
    seo_data = generate_seo_metadata(page)
    if not seo_data:
        print(f"    ⚠️ فشل التوليد")
        return None
    
    title = seo_data.get('title_ar' if lang == 'ar' else 'title_en', '')
    desc = seo_data.get('description_ar' if lang == 'ar' else 'description_en', '')
    keywords = seo_data.get('keywords', '')
    
    changes = 0
    
    if title:
        title_match = re.search(r'<title>.*?</title>', html)
        if title_match:
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
        print(f"    ✅ تم التحديث ({changes} تغييرات)")
        print(f"       العنوان: {title[:60]}")
        return seo_data
    else:
        print(f"    ⚠️ لم يتم تطبيق أي تغيير")
        return None

def main():
    print("🤖 بدء تحسين السيو بالذكاء الاصطناعي...")
    print(f"📊 عدد الحاسبات: {len(PAGES)}")
    
    if not GEMINI_API_KEY:
        print("❌ خطأ: GEMINI_API_KEY غير موجود")
        return
    
    success_count = 0
    fail_count = 0
    
    for i, page in enumerate(PAGES, 1):
        print(f"\n[{i}/{len(PAGES)}] 🔨 {page['title_ar']}")
        
        # تحسين العربية
        result_ar = optimize_page(page, 'ar')
        if result_ar:
            success_count += 1
        else:
            fail_count += 1
        
        time.sleep(2)
        
        # تحسين الإنجليزية
        result_en = optimize_page(page, 'en')
        if result_en:
            success_count += 1
        else:
            fail_count += 1
        
        time.sleep(2)
    
    print(f"\n{'='*60}")
    print(f"📊 النتائج النهائية:")
    print(f"  ✅ نجح: {success_count}")
    print(f"  ❌ فشل: {fail_count}")
    print(f"🎉 اكتمل!")

if __name__ == "__main__":
    main()
