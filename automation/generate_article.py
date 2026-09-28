#!/usr/bin/env python3
"""
توليد مقالات SEO بالذكاء الاصطناعي (DeepSeek)
كل مقال: 2000-2500 كلمة + Schema + روابط داخلية
"""

import os
import json
import time
import re
import urllib.request
import urllib.error
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(ROOT_DIR, 'articles')
DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY', '')

# قائمة المقالات المخططة
ARTICLES = [
    {
        "slug": "zakat-guide-2026",
        "title": "دليل حساب الزكاة في السعودية 2026: كل ما تحتاج معرفته",
        "keyword": "حساب الزكاة",
        "category": "finance",
        "related_calc": "zakat",
        "related_calc_title": "حاسبة الزكاة",
        "topics": [
            "ما هي الزكاة في الإسلام؟",
            "نصاب الزكاة في الذهب والفضة 2026",
            "زكاة الرواتب والأجور",
            "زكاة الأسهم والاستثمارات",
            "زكاة العقارات التجارية",
            "كيفية حساب الزكاة خطوة بخطوة",
            "أخطاء شائعة في حساب الزكاة",
            "موعد إخراج الزكاة",
            "الجهات الرسمية لإخراج الزكاة في السعودية"
        ]
    },
    {
        "slug": "eos-guide-2026",
        "title": "مكافأة نهاية الخدمة في السعودية 2026: الدليل الشامل",
        "keyword": "مكافأة نهاية الخدمة",
        "category": "finance",
        "related_calc": "eos",
        "related_calc_title": "حاسبة نهاية الخدمة",
        "topics": [
            "ما هي مكافأة نهاية الخدمة؟",
            "متى يستحق العامل المكافأة؟",
            "حساب المكافأة في الاستقالة",
            "حساب المكافأة في الفصل",
            "نظام العمل السعودي الجديد",
            "أمثلة عملية بأرقام حقيقية",
            "حقوق العامل عند انتهاء العقد",
            "المكافأة للعاملين في القطاع الحكومي",
            "كيف تحسب مكافأتك بخطوات بسيطة"
        ]
    },
    {
        "slug": "mortgage-guide-2026",
        "title": "التمويل العقاري في السعودية 2026: الدليل الكامل للمقترضين",
        "keyword": "التمويل العقاري",
        "category": "finance",
        "related_calc": "mortgage",
        "related_calc_title": "حاسبة التمويل العقاري",
        "topics": [
            "ما هو التمويل العقاري؟",
            "أنواع التمويل العقاري في السعودية",
            "شروط الحصول على التمويل",
            "حساب القسط الشهري",
            "أفضل البنوك للتمويل العقاري 2026",
            "رسوم التمويل العقاري المخفية",
            "نسبة الفائدة الحقيقية",
            "مؤسسة التمويل العقاري",
            "نصائح قبل التوقيع على العقد"
        ]
    },
    {
        "slug": "vat-guide-2026",
        "title": "ضريبة القيمة المضافة 15% في السعودية: الدليل الشامل 2026",
        "keyword": "ضريبة القيمة المضافة",
        "category": "finance",
        "related_calc": "vat",
        "related_calc_title": "حاسبة ضريبة القيمة المضافة",
        "topics": [
            "ما هي ضريبة القيمة المضافة؟",
            "تاريخ تطبيق الضريبة في السعودية",
            "السلع المعفاة من الضريبة",
            "حساب الضريبة على الفواتير",
            "التسجيل في هيئة الزكاة والضريبة",
            "الإقرارات الضريبية الشهرية",
            "عقوبات التأخير",
            "الفرق بين 5% و 15%",
            "نصائح لأصحاب المشاريع الصغيرة"
        ]
    },
    {
        "slug": "bmi-guide-2026",
        "title": "مؤشر كتلة الجسم BMI: الدليل الشامل للوزن الصحي 2026",
        "keyword": "مؤشر كتلة الجسم",
        "category": "health",
        "related_calc": "bmi",
        "related_calc_title": "حاسبة مؤشر كتلة الجسم",
        "topics": [
            "ما هو مؤشر كتلة الجسم؟",
            "معادلة حساب BMI",
            "تصنيفات مؤشر كتلة الجسم",
            "الوزن المثالي حسب الطول",
            "علاقة BMI بالصحة",
            "BMI عند الأطفال والمراهقين",
            "BMI للرياضيين (الاستثناءات)",
            "كيف تخسر الوزن بشكل صحي",
            "متى تراجع طبيب التغذية"
        ]
    },
]

def call_deepseek(prompt, max_tokens=4000, max_retries=3):
    if not DEEPSEEK_API_KEY:
        return None
    
    url = "https://api.deepseek.com/chat/completions"
    
    for attempt in range(max_retries):
        try:
            data = json.dumps({
                "model": "deepseek-chat",
                "messages": [
                    {
                        "role": "system",
                        "content": "أنت كاتب محتوى خبير في السوق السعودي. تكتب مقالات شاملة مفيدة باللغة العربية الفصحى بأسلوب احترافي."
                    },
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": max_tokens
            }).encode('utf-8')
            
            req = urllib.request.Request(url, data=data, headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
            })
            
            with urllib.request.urlopen(req, timeout=180) as response:
                result = json.loads(response.read().decode('utf-8'))
                if 'choices' in result and result['choices']:
                    return result['choices'][0]['message']['content']
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(30 * (attempt + 1))
                continue
            error = e.read().decode('utf-8', errors='ignore')
            print(f"    ⚠️ خطأ {e.code}: {error[:200]}")
            break
        except Exception as e:
            print(f"    ⚠️ {e}")
            if attempt < max_retries - 1:
                time.sleep(10)
    return None

def clean_html(content):
    if not content:
        return ""
    content = content.strip()
    if content.startswith('```html'): content = content[7:]
    if content.startswith('```'): content = content[3:]
    if content.endswith('```'): content = content[:-3]
    return content.strip()

def generate_article(article):
    topics_list = "\n".join(f"- {t}" for t in article['topics'])
    
    prompt = f"""اكتب مقالاً شاملاً باللغة العربية الفصحى بعنوان:
"{article['title']}"

الكلمة المفتاحية الرئيسية: "{article['keyword']}"
الفئة: {article['category']}
مرتبط بـ: {article['related_calc_title']}

المواضيع المطلوبة (اكتب 150-200 كلمة لكل موضوع):
{topics_list}

متطلبات المقال:
1. مقدمة جذابة (200 كلمة) تحتوي الكلمة المفتاحية
2. جدول محتويات قابل للنقر (HTML anchors)
3. فصول مفصلة بوسوم h2 لكل موضوع
4. أمثلة عملية من الواقع السعودي (أرقام ونسب حقيقية 2026)
5. ذكر الأنظمة السعودية (نظام العمل، التأمينات، هيئة الزكاة، ساما)
6. 3 نصائح ذهبية في نهاية المقال
7. خاتمة قوية تشجع القارئ على استخدام {article['related_calc_title']}
8. 5 أسئلة شائعة مع إجابات (FAQ)

القواعد:
- اكتب 2000-2500 كلمة على الأقل
- استخدم اللغة العربية الفصحى السهلة
- اذكر مصادر موثوقة (SAMA, GOSI, ZATCA)
- اجعل المحتوى فريداً ومفيداً
- استخدم أرقام ونسب سعودية واقعية 2026

أجب فقط بمحتوى HTML صالح باستخدام: h2, h3, p, ul, ol, li, strong, em, a, table, tr, td, th
لا تستخدم: style, class, iframe, script, أو أي وسوم خارج هذه القائمة."""
    
    return clean_html(call_deepseek(prompt))

def build_article_html(article, content):
    title = article['title']
    keyword = article['keyword']
    related_calc = article['related_calc']
    related_calc_title = article['related_calc_title']
    year = datetime.now().year
    
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": f"دليل شامل عن {keyword} في السعودية 2026",
        "author": {
            "@type": "Organization",
            "name": "حاسبها"
        },
        "publisher": {
            "@type": "Organization",
            "name": "حاسبها",
            "logo": {
                "@type": "ImageObject",
                "url": "https://hasibha.com/images/logo.png"
            }
        },
        "datePublished": datetime.now().strftime("%Y-%m-%d"),
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"https://hasibha.com/articles/{article['slug']}"
        },
        "inLanguage": "ar-SA"
    }
    
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | حاسبها</title>
<meta name="description" content="دليل شامل ومفصل عن {keyword} في السعودية 2026. أمثلة عملية، قوانين، ونصائح الخبراء.">
<meta name="keywords" content="{keyword}, {article['category']}, السعودية, 2026">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://hasibha.com/articles/{article['slug']}">
<link rel="icon" type="image/png" href="/images/logo.png">
<link rel="apple-touch-icon" href="/images/logo.png">
<link rel="preload" as="image" href="/images/logo.png">
<link rel="preconnect" href="https://www.googletagmanager.com">
<link rel="preconnect" href="https://www.google-analytics.com">
<meta property="og:title" content="{title}">
<meta property="og:description" content="دليل شامل ومفصل عن {keyword} في السعودية 2026">
<meta property="og:type" content="article">
<meta property="og:url" content="https://hasibha.com/articles/{article['slug']}">
<meta property="og:image" content="https://hasibha.com/images/logo.png">
<meta name="theme-color" content="#0b0d10">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4842993238012462" crossorigin="anonymous"></script>
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=2)}
</script>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:"Segoe UI",Tahoma,"Noto Kufi Arabic",sans-serif;background:#f8fafc;color:#1e293b;line-height:1.7}}
.wrap{{max-width:800px;margin:0 auto;padding:0 20px}}
.site-header{{position:sticky;top:0;z-index:50;background:rgba(255,255,255,0.86);backdrop-filter:blur(10px);border-bottom:1px solid #e6e8eb}}
.header-in{{display:flex;align-items:center;gap:20px;height:60px}}
.logo{{display:flex;align-items:center;gap:8px;font-size:20px;font-weight:700;color:#0b0d10;text-decoration:none}}
.logo img{{height:35px;vertical-align:middle}}
.main-nav{{display:flex;gap:4px;margin-inline-start:8px}}
.main-nav a{{padding:6px 12px;border-radius:8px;font-size:14px;color:#4b5563;text-decoration:none}}
.main-nav a:hover{{background:#f6f7f8;color:#0b0d10}}
.header-actions{{margin-inline-start:auto;display:flex;align-items:center;gap:8px}}
.lang-btn,.theme-btn{{border:1px solid #e6e8eb;border-radius:8px;padding:6px 12px;font-size:13px;color:#0b0d10;background:#fff;text-decoration:none;cursor:pointer}}
.breadcrumb{{background:#fff;padding:12px 0;font-size:13px;color:#8b95a1;border-bottom:1px solid #e6e8eb}}
.breadcrumb a{{color:#059669;text-decoration:none}}
.breadcrumb span{{margin:0 4px}}
.article{{background:#fff;border:1px solid #e6e8eb;border-radius:16px;padding:40px 32px;margin:30px auto;line-height:2}}
.article h1{{font-size:28px;color:#064e3b;margin-bottom:16px;border-bottom:3px solid #059669;padding-bottom:16px}}
.article-meta{{color:#8b95a1;font-size:13px;margin-bottom:32px;display:flex;gap:16px;flex-wrap:wrap}}
.article h2{{font-size:22px;color:#064e3b;margin:32px 0 16px;padding-bottom:8px;border-bottom:2px solid #059669}}
.article h3{{font-size:18px;color:#1e293b;margin:24px 0 12px}}
.article p{{color:#4b5563;font-size:16px;margin-bottom:16px}}
.article ul,.article ol{{color:#4b5563;padding-right:24px;margin-bottom:16px}}
.article li{{margin-bottom:8px}}
.article strong{{color:#0b0d10}}
.article em{{color:#059669;font-style:normal}}
.article table{{width:100%;border-collapse:collapse;margin:16px 0;background:#fff;border-radius:8px;overflow:hidden}}
.article th,.article td{{border:1px solid #e6e8eb;padding:12px;text-align:right}}
.article th{{background:#f0fdf4;color:#064e3b;font-weight:700}}
.cta-box{{background:#f0fdf4;border:2px solid #059669;border-radius:16px;padding:24px;margin:32px 0;text-align:center}}
.cta-box h3{{color:#064e3b;margin-bottom:12px}}
.cta-box p{{color:#4b5563;margin-bottom:16px}}
.cta-btn{{display:inline-block;background:#059669;color:#fff;padding:14px 32px;border-radius:12px;text-decoration:none;font-weight:700;font-size:16px}}
.cta-btn:hover{{background:#047857}}
.site-footer{{border-top:1px solid #e6e8eb;padding:32px 0;margin-top:24px;background:#fff;text-align:center;color:#8b95a1;font-size:13px}}
.footer-in{{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}}
.footer-in nav{{display:flex;gap:18px;flex-wrap:wrap}}
.footer-in a{{color:#8b95a1;text-decoration:none}}
[data-theme="dark"] body{{background:#0e1116;color:#f3f4f6}}
[data-theme="dark"] .site-header{{background:rgba(14,17,22,0.86);border-bottom-color:#262c36}}
[data-theme="dark"] .logo,[data-theme="dark"] .article h1,[data-theme="dark"] .article h2,[data-theme="dark"] .article h3,[data-theme="dark"] .article strong{{color:#f3f4f6}}
[data-theme="dark"] .main-nav a,[data-theme="dark"] .article p,[data-theme="dark"] .article ul,[data-theme="dark"] .article ol,[data-theme="dark"] .article li{{color:#aab3bf}}
[data-theme="dark"] .article,[data-theme="dark"] .site-footer,[data-theme="dark"] .article th,[data-theme="dark"] .article td{{background:#161a21;border-color:#262c36;color:#aab3bf}}
[data-theme="dark"] .article th{{background:rgba(5,150,105,0.16);color:#f3f4f6}}
[data-theme="dark"] .cta-box{{background:rgba(5,150,105,0.1);border-color:#10b981}}
[data-theme="dark"] .cta-box h3,[data-theme="dark"] .cta-box p{{color:#f3f4f6}}
@media(max-width:720px){{.main-nav{{display:none}}.article{{padding:24px 16px}}.article h1{{font-size:22px}}.article h2{{font-size:18px}}}}
</style>
</head>
<body>
<header class="site-header">
<div class="wrap header-in">
<a class="logo" href="/">
<img src="/images/logo.png" alt="حاسبها">
حاسبها
</a>
<nav class="main-nav">
<a href="/#calculators">الحاسبات</a>
<a href="/articles">المقالات</a>
<a href="/#faq">الأسئلة</a>
</nav>
<div class="header-actions">
<button class="theme-btn" onclick="toggleTheme()" aria-label="Theme">🌓</button>
<a class="lang-btn" href="/index-en">EN</a>
</div>
</div>
</header>
<nav class="breadcrumb">
<div class="wrap">
<a href="/">🏠 الرئيسية</a>
<span>←</span>
<a href="/articles">المقالات</a>
<span>←</span>
<span style="color:#0b0d10;font-weight:600">{title[:40]}...</span>
</div>
</nav>
<main>
<div class="wrap">
<article class="article">
<h1>{title}</h1>
<div class="article-meta">
<span>📅 {datetime.now().strftime("%d %B %Y")}</span>
<span>✍️ فريق حاسبها</span>
<span>⏱️ 10 دقائق قراءة</span>
</div>
{content}
<div class="cta-box">
<h3>🎯 جرّب {related_calc_title}</h3>
<p>احسب كل شيء بدقة في ثوانٍ — مجاني وبدون تسجيل</p>
<a href="/{related_calc}" class="cta-btn">افتح الحاسبة ←</a>
</div>
</article>
</div>
</main>
<footer class="site-footer">
<div class="wrap footer-in">
<a class="logo" href="/" style="font-size:16px">
<img src="/images/logo.png" alt="حاسبها" style="height:28px">
🧮 حاسبها
</a>
<nav>
<a href="/privacy">سياسة الخصوصية</a>
<a href="/contact">اتصل بنا</a>
<a href="/about">من نحن</a>
</nav>
<p>حاسبها © {year} — جميع الحقوق محفوظة</p>
</div>
</footer>
<script>
function toggleTheme(){{
var r=document.documentElement,t=r.getAttribute('data-theme')==='dark'?'light':'dark';
if(t==='dark')r.setAttribute('data-theme','dark');else r.removeAttribute('data-theme');
try{{localStorage.setItem('hs-theme',t);}}catch(e){{}}
}}
(function(){{
var t=null;try{{t=localStorage.getItem('hs-theme');}}catch(e){{}}
if(!t)t=(matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'light';
if(t==='dark')document.documentElement.setAttribute('data-theme','dark');
}})();
</script>
</body>
</html>
'''

def main():
    if not DEEPSEEK_API_KEY:
        print("❌ DEEPSEEK_API_KEY غير موجود")
        return
    
    os.makedirs(ARTICLES_DIR, exist_ok=True)
    
    for i, article in enumerate(ARTICLES, 1):
        path = os.path.join(ARTICLES_DIR, f"{article['slug']}.html")
        
        if os.path.exists(path):
            print(f"[{i}/{len(ARTICLES)}] ⏭️ {article['slug']} موجود مسبقاً")
            continue
        
        print(f"\n[{i}/{len(ARTICLES)}] 📝 {article['title'][:50]}...")
        print(f"    🤖 جاري التوليد (قد يستغرق دقيقتين)...")
        
        content = generate_article(article)
        if not content:
            print(f"    ❌ فشل التوليد")
            continue
        
        html = build_article_html(article, content)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"    ✅ تم إنشاء {article['slug']}.html ({len(content)} حرف)")
        time.sleep(3)
    
    print(f"\n🎉 اكتمل توليد المقالات!")

if __name__ == "__main__":
    main()
