#!/usr/bin/env python3
"""
تحسين السيو بالذكاء الاصطناعي - Gemini (مجاني) - مع تشخيص الأخطاء
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

def test_api_key():
    """اختبار المفتاح أولاً"""
    print("🔍 اختبار API Key...")
    
    if not GEMINI_API_KEY:
        print("❌ المفتاح فارغ")
        return False
    
    print(f"📌 طول المفتاح: {len(GEMINI_API_KEY)}")
    print(f"📌 أول 10 أحرف: {GEMINI_API_KEY[:10]}...")
    
    if not GEMINI_API_KEY.startswith('AIza'):
        print("⚠️ المفتاح لا يبدأ بـ AIza (شكل مفتاح Gemini)")
        print("   تأكد أنك نسخت مفتاح Gemini من: aistudio.google.com/apikey")
        return False
    
    # جرب قائمة الموديلات المتاحة
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={GEMINI_API_KEY}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))
            if 'models' in data:
                print(f"✅ المفتاح يعمل! عدد الموديلات المتاحة: {len(data['models'])}")
                print("📋 الموديلات المتاحة:")
                for m in data['models'][:10]:
                    print(f"   - {m['name']}")
                return True
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8', errors='ignore')
        print(f"❌ خطأ {e.code}: {error_body[:500]}")
        return False
    except Exception as e:
        print(f"❌ خطأ: {e}")
        return False

def call_gemini(prompt):
    """استدعاء Gemini API مع طباعة الأخطاء الحقيقية"""
    if not GEMINI_API_KEY:
        return None
    
    # قائمة الموديلات (نجرب كل واحد)
    models = [
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-1.5-flash",
        "gemini-1.5-flash-latest",
        "gemini-pro",
    ]
    
    for model in models:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_API_KEY}"
            
            data = json.dumps({
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"temperature": 0.3, "maxOutputTokens": 1000}
            }).encode('utf-8')
            
            req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
            
            with urllib.request.urlopen(req, timeout=60) as response:
                result = json.loads(response.read().decode('utf-8'))
                if 'candidates' in result and result['candidates']:
                    print(f"    ✓ نجح باستخدام {model}")
                    return result['candidates'][0]['content']['parts'][0]['text']
                    
        except urllib.error.HTTPError as e:
            # طباعة الخطأ الحقيقي
            try:
                error_body = e.read().decode('utf-8', errors='ignore')
                # نطبع الخطأ فقط لأول موديل (لتجنب التكرار)
                if model == models[0]:
                    print(f"    ⚠️ {model}: HTTP {e.code}")
                    print(f"       {error_body[:300]}")
            except:
                pass
            continue
            
        except urllib.error.URLError as e:
            if model == models[0]:
                print(f"    ⚠️ خطأ شبكة: {e.reason}")
            continue
            
        except Exception as e:
            if model == models[0]:
                print(f"    ⚠️ خطأ غير متوقع: {e}")
            continue
    
    return None

def generate_seo_metadata(page):
    """توليد عنوان ووصف محسّن"""
    prompt = f"""أنت خبير سيو متخصص في السوق السعودي.
لدي حاسبة اسمها: {page['title_ar']}
وصفها الحالي: {page['desc
