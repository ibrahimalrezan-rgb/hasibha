#!/usr/bin/env python3
"""
فاحص SEO تلقائي — فحص فقط بدون تطبيق تعديلات
1) قراءة الصفحات العربية والإنجليزية
2) اكتشاف العناوين المفقودة/المكررة والأوصاف الناقصة
3) فحص الروابط الداخلية والصور والروابط المعطلة
4) مقارنة الصفحات مع sitemap.xml
5) تقرير واضح بالتعديلات المقترحة
6) يُشغل من GitHub Actions دورياً
"""
import os
import re
import html as htmllib
import posixpath
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.parse import urlparse

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_DIR = os.path.join(ROOT_DIR, 'automation', 'reports')
SITE_URL = "https://hasibha.com"
CHECK_EXTERNAL = os.environ.get('CHECK_EXTERNAL', 'false').lower() == 'true'

issues = []          # كل المشاكل المكتشفة
pages_data = {}      # بيانات كل صفحة

def add_issue(page, kind, severity, message, suggestion=""):
    issues.append({
        "page": page, "kind": kind,
        "severity": severity,  # 🔴 خطأ | 🟡 تحذير | 🔵 معلومة
        "message": message, "suggestion": suggestion
    })

def clean(text):
    text = re.sub(r'<[^>]+>', '', text or '')
    return htmllib.unescape(text).strip()

def attr(attrs, name):
    m = re.search(name + r'\s*=\s*["\']([^"\']*)["\']', attrs, re.I)
    return m.group(1) if m else None

def page_url(rel):
    """تحويل مسار الملف إلى رابط الموقع"""
    rel = rel.replace(os.sep, '/')
    if rel == 'index.html':
        return '/'
    if rel.startswith('articles/'):
        return '/articles/' + rel[len('articles/'):-5]
    return '/' + rel[:-5]

def collect_pages():
    pages = []
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in ('.git', '.github', 'automation', 'node_modules', 'reports')]
        for name in files:
            if name.endswith('.html'):
                pages.append(os.path.relpath(os.path.join(root, name), ROOT_DIR))
    return sorted(pages)

def resolve_exists(path):
    """هل المسار الداخلي يشير لملف موجود؟"""
    path = path.split('#')[0].split('?')[0]
    rel = path.lstrip('/')
    if rel == '':
        rel = 'index.html'
    candidates = [rel + '.html', rel + '/index.html', rel]
    return any(os.path.isfile(os.path.join(ROOT_DIR, c)) for c in candidates)

# ============================================
# 1) قراءة الصفحات واستخراج البيانات
# ============================================
pages = collect_pages()
for rel in pages:
    with open(os.path.join(ROOT_DIR, rel), 'r', encoding='utf-8') as f:
        c = f.read()
    url = page_url(rel)

    t = re.search(r'<title[^>]*>(.*?)</title>', c, re.S | re.I)
    title = clean(t.group(1)) if t else ''

    d = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', c, re.S | re.I)
    if not d:
        d = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', c, re.S | re.I)
    desc = htmllib.unescape(d.group(1)).strip() if d else ''

    can = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', c, re.I)
    canonical = can.group(1).strip() if can else ''

    hreflangs = re.findall(r'hreflang=["\'](.*?)["\']', c, re.I)
    h1s = [clean(x) for x in re.findall(r'<h1[^>]*>(.*?)</h1>', c, re.S | re.I)]
    ids = set(re.findall(r'id=["\']([^"\']+)["\']', c))

    imgs, links = [], []
    for m in re.finditer(r'<img\b([^>]*)>', c, re.I):
        a = m.group(1)
        imgs.append({"src": attr(a, 'src') or '', "alt": attr(a, 'alt'),
                     "w": attr(a, 'width'), "h": attr(a, 'height')})
    for m in re.finditer(r'<a\b[^>]*href=["\']([^"\']*)["\']', c, re.I):
        links.append(m.group(1))

    pages_data[rel] = {"url": url, "title": title, "desc": desc,
                       "canonical": canonical, "hreflangs": hreflangs,
                       "h1s": h1s, "ids": ids, "imgs": imgs, "links": links}

# ============================================
# 2) فحوصات العناوين والأوصاف
# ============================================
titles = {}
for rel, p in pages_data.items():
    if not p['title']:
        h1 = p['h1s'][0] if p['h1s'] else p['url']
        suggested = (h1 + ' | حاسبها')[:60]
        add_issue(rel, 'title', '🔴', 'العنوان <title> مفقود أو فارغ',
                  f'أضف: <title>{suggested}</title>')
    else:
        titles.setdefault(p['title'], []).append(rel)
        if len(p['title']) < 30:
            add_issue(rel, 'title', '🟡', f'العنوان قصير ({len(p["title"])} حرف)',
                      'اجعله بين 30-60 حرفاً مع الكلمة المفتاحية')
        elif len(p['title']) > 65:
            add_issue(rel, 'title', '🟡', f'العنوان طويل ({len(p["title"])} حرف) سيُقتطع في قوقل',
                      'اختصره إلى 60 حرفاً كحد أقصى')

    if not p['desc']:
        add_issue(rel, 'description', '🔴', 'وصف الصفحة meta description مفقود',
                  'أضف وصفاً بين 70-160 حرفاً يحتوي الكلمة المفتاحية')
    elif len(p['desc']) < 70:
        add_issue(rel, 'description', '🟡', f'الوصف قصير ({len(p["desc"])} حرف)', 'أطله إلى 120-160 حرفاً')
    elif len(p['desc']) > 165:
        add_issue(rel, 'description', '🟡', f'الوصف طويل ({len(p["desc"])} حرف)', 'اختصره إلى 160 حرفاً')

    if not p['h1s']:
        add_issue(rel, 'h1', '🔴', 'لا يوجد وسم H1 في الصفحة', 'أضف H1 واحداً يحتوي الكلمة المفتاحية')
    elif len(p['h1s']) > 1:
        add_issue(rel, 'h1', '🟡', f'يوجد {len(p["h1s"])} وسوم H1 (المطلوب واحد)', 'اترك H1 واحداً فقط')

    expected = SITE_URL + ('' if p['url'] == '/' else p['url'])
    if not p['canonical']:
        add_issue(rel, 'canonical', '🟡', 'لا يوجد رابط canonical',
                  f'أضف: <link rel="canonical" href="{expected}">')
    elif p['canonical'].rstrip('/') != expected.rstrip('/'):
        add_issue(rel, 'canonical', '🟡', f'canonical لا يطابق الرابط المتوقع ({p["canonical"]})',
                  f'الصحيح: {expected}')

    is_en = p['url'].endswith('-en') or p['url'] == '/index-en' or '/index-en' in p['url']
    if 'en' not in p['hreflangs'] and not is_en:
        add_issue(rel, 'hreflang', '🔵', 'لا توجد نسخة إنجليزية مربوطة بـ hreflang', 'أضف link alternate hreflang="en"')

for title, rels in titles.items():
    if len(rels) > 1:
        for rel in rels:
            add_issue(rel, 'title', '🔴', f'عنوان مكرر مع: {", ".join(r for r in rels if r != rel)}',
                      'اجعل لكل صفحة عنواناً فريداً')

# ============================================
# 3) فحص الصور والروابط
# ============================================
external = set()
for rel, p in pages_data.items():
    for img in p['imgs']:
        src = img['src']
        if not src:
            add_issue(rel, 'image', '🔴', 'صورة بدون خاصية src', 'أضف مسار الصورة أو احذف الوسم')
            continue
        if src.startswith('/'):
            if not resolve_exists(src):
                add_issue(rel, 'image', '🔴', f'صورة معطلة (الملف غير موجود): {src}',
                          'ارفع الملف أو صحح المسار')
        elif src.startswith('http'):
            external.add(src)
        if img['alt'] is None or img['alt'].strip() == '':
            add_issue(rel, 'image', '🟡', f'صورة بدون نص بديل alt: {src[:60]}', 'أضف وصفاً قصيراً للصورة')
        if not img['w'] or not img['h']:
            add_issue(rel, 'image', '🔵', f'صورة بدون أبعاد width/height: {src[:50]}',
                      'أضف الأبعاد لمنع اهتزاز التخطيط CLS')

    for href in p['links']:
        if href.startswith('#'):
            if href != '#' and href[1:] not in p['ids']:
                add_issue(rel, 'anchor', '🔵', f'رابط داخلي لمرساة غير موجودة: {href}',
                          'أضف id مطابقاً أو صحح الرابط')
            continue
        if href.startswith(('mailto:', 'tel:', 'javascript:')):
            continue
        if href.startswith('//') or (href.startswith('http') and not href.startswith(SITE_URL)):
            external.add(href)
            continue
        if href.startswith(SITE_URL):
            path = urlparse(href).path
        elif href.startswith('/'):
            path = href
        else:
            path = posixpath.normpath(posixpath.join(posixpath.dirname(p['url']), href))
        if not resolve_exists(path):
            add_issue(rel, 'link', '🔴', f'رابط داخلي معطل: {href}',
                      'صحح الرابط أو استبدله بصفحة موجودة')

if CHECK_EXTERNAL:
    print(f"🌐 فحص {min(len(external), 40)} رابط خارجي...")
    for url in sorted(external)[:40]:
        try:
            req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as r:
                if r.status >= 400:
                    add_issue('(خارجي)', 'external', '🔴', f'رابط خارجي بحالة {r.status}: {url}', 'حدّث أو احذف الرابط')
        except urllib.error.HTTPError as e:
            add_issue('(خارجي)', 'external', '🔴', f'رابط خارجي بحالة {e.code}: {url}', 'حدّث أو احذف الرابط')
        except Exception:
            add_issue('(خارجي)', 'external', '🔵', f'تعذر التحقق من: {url}', 'تحقق يدوياً')

# ============================================
# 4) المقارنة مع sitemap.xml
# ============================================
sitemap_path = os.path.join(ROOT_DIR, 'sitemap.xml')
sitemap_paths = set()
if os.path.exists(sitemap_path):
    tree = ET.parse(sitemap_path)
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    for loc in tree.findall('.//s:loc', ns):
        if loc.text:
            sitemap_paths.add(urlparse(loc.text.strip()).path or '/')
else:
    add_issue('sitemap.xml', 'sitemap', '🔴', 'ملف sitemap.xml غير موجود!', 'أنشئه عبر generate_sitemap.py')

actual_paths = {p['url'] for p in pages_data.values()}
for path in sorted(actual_paths - sitemap_paths):
    add_issue('sitemap.xml', 'sitemap', '🟡', f'صفحة غير موجودة في الـ sitemap: {path}',
              f'أضف: <url><loc>{SITE_URL}{path}</loc></url>')
for path in sorted(sitemap_paths - actual_paths):
    add_issue('sitemap.xml', 'sitemap', '🔴', f'الـ sitemap يشير لصفحة غير موجودة: {path}',
              'احذف الرابط من الـ sitemap أو أنشئ الصفحة')

# ============================================
# 5) توليد التقرير
# ============================================
os.makedirs(REPORT_DIR, exist_ok=True)
order = {'🔴': 0, '🟡': 1, '🔵': 2}
issues.sort(key=lambda x: (order[x['severity']], x['page'], x['kind']))
counts = {'🔴': 0, '🟡': 0, '🔵': 0}
for i in issues:
    counts[i['severity']] += 1

lines = [
    f"# 🔍 تقرير فحص SEO — {datetime.now().strftime('%Y-%m-%d %H:%M')}",
    "",
    f"- **الصفحات المفحوصة**: {len(pages_data)}",
    f"- **🔴 أخطاء**: {counts['🔴']}",
    f"- **🟡 تحذيرات**: {counts['🟡']}",
    f"- **🔵 معلومات**: {counts['🔵']}",
    "",
    "> ⚠️ هذا تقرير اقتراحات فقط — لم يتم تطبيق أي تعديل تلقائياً.",
    "",
]
if not issues:
    lines.append("✅ **لا توجد مشاكل مكتشفة — الموقع سليم!**")
else:
    current_page = None
    for i in issues:
        if i['page'] != current_page:
            current_page = i['page']
            lines.append(f"## 📄 `{current_page}`")
            lines.append("")
        sug = f" — **الاقتراح**: {i['suggestion']}" if i['suggestion'] else ""
        lines.append(f"- {i['severity']} **[{i['kind']}]** {i['message']}{sug}")
    lines.append("")

report = '\n'.join(lines)
report_file = os.path.join(REPORT_DIR, 'seo-report.md')
with open(report_file, 'w', encoding='utf-8') as f:
    f.write(report)

# ملخص في واجهة GitHub Actions
summary_file = os.environ.get('GITHUB_STEP_SUMMARY')
if summary_file:
    with open(summary_file, 'a', encoding='utf-8') as f:
        f.write(report[:6000])

print(f"📊 الصفحات المفحوصة: {len(pages_data)}")
print(f"🔴 أخطاء: {counts['🔴']} |  تحذيرات: {counts['🟡']} |  معلومات: {counts['']}")
print(f" التقرير: automation/reports/seo-report.md")
for i in issues[:15]:
    print(f"  {i['severity']} [{i['page']}] {i['message']}")
print("🎉 اكتمل الفحص (بدون تطبيق أي تعديل)")
