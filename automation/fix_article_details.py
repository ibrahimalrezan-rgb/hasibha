#!/usr/bin/env python3
"""
إصلاح تفاصيل المقالات والصفحات الثابتة بناءً على تقرير SEO الأخير
"""
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============================================
# 1) إصلاح وصف صفحة اتصل بنا (قصير جداً)
# ============================================
contact_path = os.path.join(ROOT_DIR, 'contact.html')
if os.path.exists(contact_path):
    with open(contact_path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    new_desc = "تواصل مع فريق حاسبها للاستفسارات والاقتراحات حول الحاسبات المالية والصحية. نحن هنا لمساعدتك والرد على جميع استفساراتك خلال 24 ساعة."
    
    # استبدال الوصف القديم
    c = re.sub(r'<meta\s+name="description"\s+content="[^"]*"', 
               f'<meta name="description" content="{new_desc}"', c)
    
    with open(contact_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("✅ تم إصلاح وصف صفحة contact.html")

# ============================================
# 2) إصلاح تفاصيل المقالات (أبعاد الصور + hreflang + معرفات العناوين)
# ============================================
articles_dir = os.path.join(ROOT_DIR, 'articles')
fixed_count = 0

if os.path.exists(articles_dir):
    for name in os.listdir(articles_dir):
        if not name.endswith('.html') or name.startswith('index'):
            continue
        
        path = os.path.join(articles_dir, name)
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        orig = c
        
        is_en = name.endswith('-en.html')
        base_name = name[:-8] if is_en else name[:-5]
        other_lang = f"{base_name}-en.html" if not is_en else f"{base_name}.html"
        
        # أ) إضافة أبعاد للصورة (يمنع اهتزاز التخطيط CLS)
        # نستهدف فقط صور اللوقو التي ليس لها أبعاد
        c = re.sub(
            r'<img\s+src="/images/logo\.png"(?!\s+width)(?!\s+height)([^>]*)>',
            r'<img src="/images/logo.png" width="54" height="36"\1>',
            c
        )
        
        # ب) إضافة hreflang للنسخة الأخرى
        if f'hreflang="{"en" if is_en else "ar"}"' not in c:
            other_url = f"https://hasibha.com/articles/{other_lang[:-5]}"
            hreflang_tag = f'<link rel="alternate" hreflang="{"en" if is_en else "ar"}" href="{other_url}">'
            # نضيفه بعد الـ canonical
            c = re.sub(
                r'(<link\s+rel="canonical"[^>]+>)',
                r'\1\n' + hreflang_tag,
                c
            )
        
        # ج) إضافة id للعناوين الشائعة لتعمل روابط المراسي (Anchors)
        replacements = [
            (r'<h2>(الأسئلة الشائعة.*?)</h2>', r'<h2 id="faq">\1</h2>'),
            (r'<h2>(FAQ.*?)</h2>', r'<h2 id="faq">\1</h2>'),
            (r'<h2>(نصائح.*?)</h2>', r'<h2 id="tips">\1</h2>'),
            (r'<h2>(Golden Tips.*?)</h2>', r'<h2 id="tips">\1</h2>'),
            (r'<h2>(الخات.*?)</h2>', r'<h2 id="conclusion">\1</h2>'),
            (r'<h2>(Conclusion.*?)</h2>', r'<h2 id="conclusion">\1</h2>'),
            (r'<h2>(جرّب.*?)</h2>', r'<h2 id="calculator">\1</h2>'),
            (r'<h2>(Try the.*?)</h2>', r'<h2 id="calculator">\1</h2>'),
        ]
        for pattern, repl in replacements:
            c = re.sub(pattern, repl, c)

        if c != orig:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(c)
            fixed_count += 1

print(f"✅ تم إصلاح تفاصيل {fixed_count} مقال (أبعاد صور + hreflang + معرفات عناوين)")

# ============================================
# 3) ملاحظة بخصوص canonical و sitemap
# ============================================
print("\n💡 ملاحظة:")
print("- تحذير canonical في articles/index.html: الرابط /articles/ هو الصحيح سيوياً (أفضل من /articles/index). يمكنك تجاهل هذا التحذير بأمان.")
print("- تحذير sitemap: تأكد من تشغيل generate_sitemap.py بعد هذا السكربت لالتقاط أي تحديثات.")
print("🎉 اكتمل الإصلاح!")
