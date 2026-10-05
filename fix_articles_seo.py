#!/usr/bin/env python3
"""
إصلاح شامل وسحري لجميع ملاحظات الـ SEO (🔵 و 🟡) في المقالات
1) إضافة أبعاد للصور (width/height) لمنع اهتزاز الصفحة.
2) إضافة معرفات (id) للعناوين لتعمل روابط جدول المحتويات.
3) إضافة روابط hreflang للنسخ الإنجليزية.
"""
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(ROOT_DIR, 'articles')

fixed_count = 0

if os.path.exists(ARTICLES_DIR):
    for name in os.listdir(ARTICLES_DIR):
        if not name.endswith('.html') or name.startswith('index'):
            continue
        
        path = os.path.join(ARTICLES_DIR, name)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        is_en = name.endswith('-en.html')
        base_name = name[:-8] if is_en else name[:-5]
        
        # 1) إصلاح أبعاد صورة اللوقو
        content = re.sub(
            r'(<img\s+src="/images/logo\.png")(?!\s+width)',
            r'\1 width="54" height="36"',
            content
        )
        
        # 2) إضافة معرفات (id) للعناوين H2 لتعمل الروابط الداخلية
        # القاموس يربط بين نص العنوان والـ id المطلوب
        id_mappings = [
            (r'(<h2[^>]*>)(.*?الأسئلة الشائعة.*?)(</h2>)', r'\1\2\3'.replace('<h2>', '<h2 id="faq">')),
            (r'(<h2[^>]*>)(.*?FAQ.*?)(</h2>)', r'\1\2\3'.replace('<h2>', '<h2 id="faq">')),
            (r'(<h2[^>]*>)(.*?نصائح.*?)(</h2>)', r'\1\2\3'.replace('<h2>', '<h2 id="tips">')),
            (r'(<h2[^>]*>)(.*?Golden Tips.*?)(</h2>)', r'\1\2\3'.replace('<h2>', '<h2 id="tips">')),
            (r'(<h2[^>]*>)(.*?الخاتمة.*?)(</h2>)', r'\1\2\3'.replace('<h2>', '<h2 id="conclusion">')),
            (r'(<h2[^>]*>)(.*?Conclusion.*?)(</h2>)', r'\1\2\3'.replace('<h2>', '<h2 id="conclusion">')),
            (r'(<h2[^>]*>)(.*?جرّب.*?)(</h2>)', r'\1\2\3'.replace('<h2>', '<h2 id="calculator">')),
            (r'(<h2[^>]*>)(.*?Try the.*?)(</h2>)', r'\1\2\3'.replace('<h2>', '<h2 id="calculator">')),
            (r'(<h2[^>]*>)(.*?موعد إخراج الزكاة.*?)(</h2>)', r'\1\2\3'.replace('<h2>', '<h2 id="zakat-timing">')),
            (r'(<h2[^>]*>)(.*?الجهات الرسمية.*?)(</h2>)', r'\1\2\3'.replace('<h2>', '<h2 id="official-bodies">')),
        ]
        
        for pattern, replacement in id_mappings:
            # نتأكد أننا لا نضيف id إذا كان موجوداً بالفعل
            if 'id=' not in re.search(pattern, content, re.IGNORECASE | re.DOTALL).group(0) if re.search(pattern, content, re.IGNORECASE | re.DOTALL) else True:
                content = re.sub(pattern, replacement, content, flags=re.IGNORECASE | re.DOTALL)

        # 3) إضافة رابط hreflang للنسخة الإنجليزية في المقالات العربية
        if not is_en:
            en_url = f"https://hasibha.com/articles/{base_name}-en"
            if 'hreflang="en"' not in content:
                # نضيفه بعد الـ canonical
                content = re.sub(
                    r'(<link\s+rel="canonical"[^>]+>)',
                    rf'\1\n<link rel="alternate" hreflang="en" href="{en_url}">',
                    content
                )

        if content != original_content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed_count += 1
            print(f"✅ تم إصلاح: {name}")

# 4) إصلاح تحذير الـ sitemap (إضافة /articles/index يدوياً إذا لم يكن موجوداً)
sitemap_path = os.path.join(ROOT_DIR, 'sitemap.xml')
if os.path.exists(sitemap_path):
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        sitemap_content = f.read()
    
    if '<loc>https://hasibha.com/articles/index</loc>' not in sitemap_content:
        # نضيفه قبل إغلاق urlset
        new_entry = """  <url>
    <loc>https://hasibha.com/articles/index</loc>
    <lastmod>2026-10-05</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""
        sitemap_content = sitemap_content.replace('</urlset>', new_entry)
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(sitemap_content)
        print("✅ تم إصلاح ملف sitemap.xml")

print(f"\n🎉 اكتمل الإصلاح! تم تعديل {fixed_count} ملف.")
