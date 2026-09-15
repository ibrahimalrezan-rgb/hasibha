#!/usr/bin/env python3
"""
تحسين السيو بالذكاء الاصطناعي
يستخدم DeepSeek API لتحسين العناوين والأوصاف والمحتوى
"""

import os
import sys
import re
import json
import requests
import time
from config import PAGES, SITE_URL

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY', '')

def call_deepseek(prompt, max_tokens=2000):
    """استدعاء DeepSeek API"""
    if not DEEPSEEK_API_KEY:
        print("  ⚠️ DeepSeek API Key غير موجود")
        return None
    
    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": "أنت خبير سيو متخصص في السوق السعودي. تجيب فقط بالـ JSON بدون أي شرح إضافي."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3,
                "max_tokens": max_tokens
            },
            timeout=60
        )
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            print(f"  ⚠️ DeepSeek error: {response.status_code}")
            return None
    except Exception as e:
        print(f"  ⚠️ DeepSeek exception: {e}")
        return None

def generate_seo_metadata(page):
    """توليد عنوان ووصف محسّن بالذكاء الاصطناعي"""
    
    prompt = f"""أنت خبير سيو متخصص في السوق السعودي.
لدي حاسبة اسمها: {page['title_ar']}
الوصف الحالي: {page['desc_ar']}

أريدك تولد لي:
1. عنوان SEO محسّن (50-60 حرف) يتضمن الكلمة المفتاحية الرئيسية والسنة 2026
2. وصف Meta محسّن (150-160 حرف) يتضمن الكلمة المفتاحية ودعوة للفعل
3. كلمات مفتاحية (5 كلمات)

أجب فقط بهذا الشكل:
{{
  "title": "العنوان المحسّن",
  "description": "الوصف المحسّن",
  "keywords": "كلمة1, كلمة2, كلمة3, كلمة4, كلمة5"
}}
"""
    
    result = call_deepseek(prompt)
    if result:
        # استخراج JSON من الرد
        json_match = re.search(r'\{.*\}', result, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group())
            except:
                pass
    return None

def optimize_page_seo(page, html_content):
    """تحسين صفحة واحدة"""
    
    print(f"  🤖 توليد سيو محسّن لـ {page['title_ar']}...")
    
    seo_data = generate_seo_metadata(page)
    if not seo_data:
        print(f"    ⚠️ فشل توليد السيو")
        return html_content
    
    # تحديث العنوان
    old_title = re.search(r'<title>(.*?)</title>', html_content)
    if old_title:
        html_content = html_content.replace(
            f'<title>{old_title.group(1)}</title>',
            f'<title>{seo_data["title"]}</title>'
        )
    
    # تحديث الوصف
    old_desc = re.search(r'<meta name="description" content="(.*?)"', html_content)
    if old_desc:
        html_content = html_content.replace(
            f'<meta name="description" content="{old_desc.group(1)}"',
            f'<meta name="description" content="{seo_data["description"]}"'
        )
    
    # تحديث الكلمات المفتاحية
    old_keywords = re.search(r'<meta name="keywords" content="(.*?)"', html_content)
    if old_keywords:
        html_content = html_content.replace(
            f'<meta name="keywords" content="{old_keywords.group(1)}"',
            f'<meta name="keywords" content="{seo_data["keywords"]}"'
        )
    
    print(f"    ✅ تم التحديث")
    return html_content

def main():
    print("🤖 بدء تحسين السيو بالذكاء الاصطناعي...")
    
    if not DEEPSEEK_API_KEY:
        print("❌ خطأ: يجب تعيين DEEPSEEK_API_KEY")
        print("   أضف الـ Secret في: Settings → Secrets → Actions")
        return
    
    for page in PAGES:
        # تحسين الصفحة العربية
        ar_path = os.path.join(ROOT_DIR, f"{page['slug']}.html")
        if os.path.exists(ar_path):
            with open(ar_path, 'r', encoding='utf-8') as f:
                html = f.read()
            
            optimized_html = optimize_page_seo(page, html)
            
            with open(ar_path, 'w', encoding='utf-8') as f:
                f.write(optimized_html)
        
        time.sleep(1)  # تجنب الـ rate limit
    
    print("\n🎉 اكتمل تحسين السيو!")

if __name__ == "__main__":
    main()
