#!/usr/bin/env python3
"""استبدال رابط اللوقو الخارجي بمسار محلي في كل الملفات"""
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD_URL = "https://i.ibb.co/MyCPJW6y/B8947-E27-073-B-4-DE2-8-E7-F-EB2023-A17-E70.png"
NEW_URL = "/images/logo.png"

changed = 0
for root, dirs, files in os.walk(ROOT_DIR):
    dirs[:] = [d for d in dirs if d not in ('.git',)]
    for name in files:
        if name.endswith(('.html', '.py')):
            path = os.path.join(root, name)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            if OLD_URL in content:
                content = content.replace(OLD_URL, NEW_URL)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                changed += 1
                print(f"✅ تم التحديث: {os.path.relpath(path, ROOT_DIR)}")

print(f"\n🎉 عدد الملفات المحدثة: {changed}")
