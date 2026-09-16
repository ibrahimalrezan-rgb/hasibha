#!/usr/bin/env python3
"""
تحسين السيو - نسخة تشخيصية
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
        {"slug": "mortgage", "title_ar": "حاسبة التمويل العقاري", "desc_ar": "قسطك الشهري", "title_en": "Mortgage", "desc_en": "Monthly"},
    ]

def diagnose_api():
    """تشخيص حالة API"""
    print("="*60)
    print("🔍 تشخيص Gemini API")
    print("="*60)
    
    if not GEMINI_API_KEY:
        print("❌ GEMINI_API_KEY غير موجود")
        return False
    
    print(f"📌 طول المفتاح: {len(GEMINI_API_KEY)}")
    print(f"📌 أول 10 أحرف: {GEMINI_API_KEY[:10]}...")
    print(f"📌 آخر 5 أحرف: ...{GEMINI_API_KEY[-5:]}")
    
    # محاولة 1: قائمة الموديلات
    print("\n📋 محاولة جلب قائمة الموديلات...")
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models?key={GEMINI_API_KEY}"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))
            if 'models' in data:
                print(f"✅ المفتاح يعمل! عدد الموديلات: {len(data['models'])}")
                print("📋 الموديلات المتاحة (أول 15):")
                for m in data['models'][:15]:
                    name = m['name'].replace('models/', '')
                    print(f"   ✓ {name}")
                return True
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8', errors='ignore')
        print(f"❌ خطأ HTTP {e.code}:")
        print(f"   {error_body[:500]}")
    except Exception as e:
        print(f"❌ خطأ: {e}")
    
    return False

def test_model(model):
    """اختبار موديل معين بطلب بسيط"""
    print(f"\n🧪 اختبار {model}...")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    
    data = json.dumps({
        "contents": [{"parts": [{"text": "Say 'hello' in Arabic"}]}],
        "generationConfig": {"maxOutputTokens": 50}
    }).encode('utf-8')
    
    # الطريقة 1: Header
    try:
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
            if 'candidates' in result:
                text = result['candidates'][0]['content']['parts'][0]['text']
                print(f"   ✅ Header نجح! الرد: {text[:50]}")
                return "header"
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8', errors='ignore')
        print(f"   ❌ Header فشل ({e.code}): {error_body[:200]}")
    except Exception as e:
        print(f"   ❌ Header فشل: {e}")
    
    # الطريقة 2: URL parameter
    try:
        url2 = url + f"?key={GEMINI_API_KEY}"
        req = urllib.request.Request(
            url2,
            data=data,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode('utf-8'))
            if 'candidates' in result:
                text = result['candidates'][0]['content']['parts'][0]['text']
                print(f"   ✅ URL نجح! الرد: {text[:50]}")
                return "url"
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8', errors='ignore')
        print(f"   ❌ URL فشل ({e.code}): {error_body[:200]}")
    except Exception as e:
        print(f"   ❌ URL فشل: {e}")
    
    return None

def main():
    print("🤖 بدء التشخيص الشامل...")
    
    # 1. تشخيص المفتاح
    if not diagnose_api():
        print("\n" + "="*60)
        print("❌ فشل التشخيص - تحقق من:")
        print("   1. المفتاح في GitHub Secrets اسمه: GEMINI_API_KEY")
        print("   2. المفتاح صحيح ومن AI Studio")
        print("   3. Generative Language API مفعّل")
        print("="*60)
        return
    
    # 2. اختبار جميع الموديلات
    print("\n" + "="*60)
    print("🧪 اختبار جميع الموديلات")
    print("="*60)
    
    models_to_test = [
        "gemini-flash-latest",
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-1.5-flash",
        "gemini-1.5-flash-latest",
        "gemini-1.5-pro",
        "gemini-pro",
    ]
    
    working_method = None
    working_model = None
    
    for model in models_to_test:
        result = test_model(model)
        if result:
            working_model = model
            working_method = result
            break
    
    # 3. النتيجة النهائية
    print("\n" + "="*60)
    if working_model:
        print(f"✅ الحل: استخدم {working_model} بطريقة {working_method}")
        print("="*60)
        print("\n📝 الخطوة التالية:")
        print(f"   غيّر قائمة الموديلات في السكربت لتكون:")
        print(f'   models = ["{working_model}"]')
        print(f"\n   واستخدام طريقة الـ {working_method}")
    else:
        print("❌ لم ينجح أي موديل!")
        print("="*60)
        print("\n🔧 الحلول:")
        print("   1. تأكد من تفعيل Generative Language API")
        print("   2. جرب إنشاء مفتاح جديد من AI Studio")
        print("   3. انتظر 5 دقائق (قد يكون ضغط عالي)")

if __name__ == "__main__":
    main()
