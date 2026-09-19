#!/usr/bin/env python3
"""
تحسين سرعة الموقع:
1) تأجيل Google Tag Manager ليحمل بعد اكتمال الصفحة
2) إضافة preconnect للمصادر الخارجية
يشمل كل صفحات HTML + سكربتات التوليد للمستقبل
"""
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OLD_GTM_HTML = '''<script async src="https://www.googletagmanager.com/gtag/js?id=G-NZLXJFVCDW"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag('js',new Date());gtag('config','G-NZLXJFVCDW');</script>'''

NEW_GTM_HTML = '''<script>
window.addEventListener('load',function(){
var s=document.createElement('script');
s.src='https://www.googletagmanager.com/gtag/js?id=G-NZLXJFVCDW';
s.async=true;
document.head.appendChild(s);
s.onload=function(){
window.dataLayer=window.dataLayer||[];
function gtag(){dataLayer.push(arguments)}
window.gtag=gtag;
gtag('js',new Date());
gtag('config','G-NZLXJFVCDW');
};
});
</script>'''

OLD_GTM_PY = '''<script async src="https://www.googletagmanager.com/gtag/js?id=G-NZLXJFVCDW"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-NZLXJFVCDW');</script>'''

NEW_GTM_PY = '''<script>
window.addEventListener('load',function(){{
var s=document.createElement('script');
s.src='https://www.googletagmanager.com/gtag/js?id=G-NZLXJFVCDW';
s.async=true;
document.head.appendChild(s);
s.onload=function(){{
window.dataLayer=window.dataLayer||[];
function gtag(){{dataLayer.push(arguments)}}
window.gtag=gtag;
gtag('js',new Date());
gtag('config','G-NZLXJFVCDW');
}};
}});
</script>'''

VIEWPORT = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
PRECONNECT = '''<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://www.googletagmanager.com">
<link rel="preconnect" href="https://www.google-analytics.com">
<link rel="dns-prefetch" href="https://pagead2.googlesyndication.com">'''

fixed = 0
skipped = 0

targets = []
for root, dirs, files in os.walk(ROOT_DIR):
    dirs[:] = [d for d in dirs if d not in ('.git',)]
    for name in files:
        if name.endswith('.html'):
            targets.append(os.path.join(root, name))

# سكربتات التوليد أيضًا (للمستقبل)
for py in ('update_en.py', 'generate_index.py'):
    p = os.path.join(ROOT_DIR, 'automation', py)
    if os.path.exists(p):
        targets.append(p)

for path in targets:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    if OLD_GTM_HTML in content:
        content = content.replace(OLD_GTM_HTML, NEW_GTM_HTML)
    if OLD_GTM_PY in content:
        content = content.replace(OLD_GTM_PY, NEW_GTM_PY)

    if 'rel="preconnect"' not in content and VIEWPORT in content:
        content = content.replace(VIEWPORT, PRECONNECT, 1)

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ {os.path.relpath(path, ROOT_DIR)}")
        fixed += 1
    else:
        skipped += 1

print(f"\n✅ معدّل: {fixed} | ℹ️ بدون تغيير: {skipped}")
print("🎉 اكتمل!")
