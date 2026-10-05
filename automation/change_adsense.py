#!/usr/bin/env python3
"""
تغيير حساب AdSense + إضافة Meta Tag للتحقق
في كل ملفات الموقع تلقائياً
"""
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OLD_PUB = "ca-pub-4842993238012462"
NEW_PUB = "ca-pub-1508132460803414"

META_TAG = f'<meta name="google-adsense-account" content="{NEW_PUB}">'

changed = 0
meta_added = 0

targets = []
for root, dirs, files in os.walk(ROOT_DIR):
    dirs[:] = [d for d in dirs if d not in ('.git',)]
    for name in files:
        if name.endswith(('.html', '.py')):
            targets.append(os.path.join(root, name))

for path in targets:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        continue
    
    orig = content
    
    # 1) استبدال الرقم القديم بالجديد
    if OLD_PUB in content:
        content = content.replace(OLD_PUB, NEW_PUB)
    
    # 2) إضافة Meta Tag للتحقق (ملفات HTML فقط، مرة واحدة)
    if path.endswith('.html') and 'google-adsense-account' not in content:
        if '</head>' in content:
            content = content.replace('</head>', f'\n{META_TAG}\n</head>', 1)
            meta_added += 1
    
    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ {os.path.relpath(path, ROOT_DIR)}")
        changed += 1

print(f"\n{'='*50}")
print(f"🔄 ملفات تم تحديث الرقم فيها: {changed}")
print(f"🔐 ملفات أُضيف لها Meta Tag: {meta_added}")
print(f"📊 الحساب الجديد: {NEW_PUB}")
print(f"🎉 اكتمل!")
