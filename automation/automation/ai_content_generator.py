#!/usr/bin/env python3
"""
توليد المحتوى الفريد بالذكاء الاصطناعي
يضيف محتوى 500+ كلمة لكل حاسبة
"""

import os
import re
import json
import requests
import time
from config import PAGES, SITE_URL

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY', '')

def call_deepseek(prompt, max_tokens=3000):
    """استدعاء DeepSeek API"""
    if not DEEPSEEK_API_KEY:
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
                    {"role": "system", "content": "أنت كاتب محتوى محترف متخصص في الحاسبات المالية والصحية للسوق السعودي."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.5,
                "max_tokens": max_tokens
            },
            timeout=120
        )
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        return None
    except Exception as e:
        print(f"  ⚠️ Error: {e}")
        return None

def generate_unique_content(page):
    """توليد محتوى فريد للحاسبة"""
    
    prompt = f"""أكتب مقالاً شاملاً عن {page['title_ar']} للسوق السعودي.

المتطلبات:
1. العنوان الرئيسي (H2)
2. مقدمة جذابة (100 كلمة)
3. شرح مفصل لكيفية عمل الحاسبة (200 كلمة)
4. أمثلة عملية (100 كلمة)
5. نصائح مهمة (100 كلمة)
6. أسئلة شائعة (3 أسئلة مع إجابات)

أكتب بصيغة HTML بدون <html> و <body>:
<h2>العنوان</h2>
<p>المحتوى...</p>
"""
    
    content = call_deepseek(prompt)
    return content

def add_related_links(page, all_pages):
    """توليد روابط داخلية ذات صلة"""
    
    related = [p for p in all_pages if p['category'] == page['category'] and p['slug'] != page['slug']][:3]
    
    if not related:
        return ""
    
    links_html = '<div class="related-calculators">\n<h3>حاسبات ذات صلة</h3>\n<ul>\n'
    for rel in related:
        links_html += f'<li><a href="/{rel["slug"]}">{rel["title_ar"]}</a></li>\n'
    links_html += '</ul>\n</div>\n'
    
    return links_html

def add_content_to_page(page, html_content):
    """إضافة المحتوى الفريد للصفحة"""
    
    # التحقق من وجود المحتوى مسبقاً
    if 'article-box' in html_content and len(html_content) > 15000:
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
    if article_end != -1:
        new_content = f'\n<div class="ai-content">\n{content}\n</div>\n{related_links}'
        html_content = html_content[:article_end] + new_content + html_content[article_end:]
    
    print(f"    ✅ تم إضافة المحتوى ({len(content)} حرف)")
    return html_content

def main():
    print("📝 بدء توليد المحتوى الفريد...")
    
    if not DEEPSEEK_API_KEY:
        print("❌ خطأ: يجب تعيين DEEPSEEK_API_KEY")
        return
    
    for page in PAGES:
        ar_path = os.path.join(ROOT_DIR, f"{page['slug']}.html")
        if os.path.exists(ar_path):
            with open(ar_path, 'r', encoding='utf-8') as f:
                html = f.read()
            
            updated_html = add_content_to_page(page, html)
            
            with open(ar_path, 'w', encoding='utf-8') as f:
                f.write(updated_html)
        
        time.sleep(2)  # تجنب الـ rate limit
    
    print("\n🎉 اكتمل توليد المحتوى!")

if __name__ == "__main__":
    main()
