const fs = require('fs');
const path = require('path');

const ROOT_DIR = 'C:\\Users\\ibrah\\.gemini\\antigravity\\scratch\\hasibha';
const SITE_URL = 'https://hasibha.com';
const TODAY = new Date().toISOString().split('T')[0];
const YEAR = new Date().getFullYear();

// Read config from python file or define the pages structure
const CATEGORIES = {
    "finance":    {"ar": "مالية",    "en": "Finance",    "icon": "💰"},
    "conversion": {"ar": "تحويلات",  "en": "Conversion", "icon": "🔄"},
    "health":     {"ar": "صحية",     "en": "Health",     "icon": "❤️"},
    "general":    {"ar": "عامة",     "en": "General",    "icon": "📦"},
};

const PAGES = [
    {"slug": "citizen-account", "title_ar": "حاسبة حساب المواطن",       "title_en": "Citizen Account Calculator",    "desc_ar": "احسب الدعم الشهري التقديري للأسرة والفرد المستقل.",        "desc_en": "Estimated monthly support for family and individuals.", "category": "finance",    "icon": "🇸🇦"},
    {"slug": "social-security", "title_ar": "حاسبة الضمان المطور",      "title_en": "Social Security Calculator",   "desc_ar": "احسب المعاش الشهري ودعم الغذاء والكهرباء.",                 "desc_en": "Monthly pension, food and electricity support.",       "category": "finance",    "icon": "🛡️"},
    {"slug": "mortgage",        "title_ar": "حاسبة التمويل العقاري",     "title_en": "Mortgage Calculator",          "desc_ar": "قسطك الشهري وقدرتك على الشراء لأي عقار سكني.",            "desc_en": "Monthly payment and purchasing power for any home.",   "category": "finance",    "icon": "🏠"},
    {"slug": "personal-loan",   "title_ar": "حاسبة التمويل الشخصي",      "title_en": "Personal Loan Calculator",     "desc_ar": "القسط الشهري والفائدة لأي مبلغ ومدة تمويل.",              "desc_en": "Monthly installment and interest for any amount.",     "category": "finance",    "icon": "💵"},
    {"slug": "eos",             "title_ar": "حاسبة نهاية الخدمة",        "title_en": "End of Service Calculator",    "desc_ar": "مكافأتك وفق نظام العمل السعودي — استقالة أو فصل.",        "desc_en": "Your benefit per Saudi Labor Law — resignation or termination.", "category": "finance", "icon": "📋"},
    {"slug": "vat",             "title_ar": "حاسبة ضريبة القيمة المضافة","title_en": "VAT Calculator",               "desc_ar": "إضافة أو استبعاد 15% من أي مبلغ في ثانية.",               "desc_en": "Add or remove 15% VAT from any amount instantly.",     "category": "finance",    "icon": "🧾"},
    {"slug": "salary",          "title_ar": "الراتب بعد التأمينات",      "title_en": "Salary After Insurance",       "desc_ar": "صافي راتبك بعد خصم التأمينات الاجتماعية (GOSI).",         "desc_en": "Your net salary after GOSI deduction.",                "category": "finance",    "icon": "💼"},
    {"slug": "zakat",           "title_ar": "حاسبة الزكاة",              "title_en": "Zakat Calculator",             "desc_ar": "احسب زكاة أموالك بدقة وفق الأحكام الشرعية.",              "desc_en": "Calculate your Zakat accurately per Sharia rules.",    "category": "finance",    "icon": "🕌"},
    {"slug": "gold-value",      "title_ar": "حاسبة قيمة الذهب",          "title_en": "Gold Value Calculator",        "desc_ar": "احسب قيمة الذهب حسب الوزن والعيار والسعر الحالي.",        "desc_en": "Gold value by weight, karat and current price.",       "category": "finance",    "icon": "🥇"},
    {"slug": "hijri-date",      "title_ar": "تحويل التاريخ",             "title_en": "Hijri Date Converter",         "desc_ar": "تحويل بين التاريخ الهجري والميلادي وفق تقويم أم القرى.", "desc_en": "Convert between Hijri and Gregorian dates accurately.", "category": "conversion", "icon": "🗓️"},
    {"slug": "currency",        "title_ar": "تحويل العملات",             "title_en": "Currency Converter",           "desc_ar": "ريال سعودي، دولار، يورو وأكثر — بأسعار محدثة.",           "desc_en": "SAR, USD, EUR and more with live rates.",              "category": "conversion", "icon": "💱"},
    {"slug": "length",          "title_ar": "تحويل الطول",               "title_en": "Length Converter",             "desc_ar": "أمتار، أقدام، إنشات وبوصات بضغطة واحدة.",                 "desc_en": "Meters, feet, inches in one click.",                   "category": "conversion", "icon": "📏"},
    {"slug": "weight",          "title_ar": "تحويل الوزن",               "title_en": "Weight Converter",             "desc_ar": "كيلوغرام، رطل، أونصة وجرام بدقة كاملة.",                  "desc_en": "Kilograms, pounds, ounces and grams.",                 "category": "conversion", "icon": "⚖️"},
    {"slug": "area",            "title_ar": "تحويل المساحة",             "title_en": "Area Converter",               "desc_ar": "متر مربع، فدان، هكتار وكيلومتر مربع.",                    "desc_en": "Square meters, acres, hectares and km².",              "category": "conversion", "icon": "📐"},
    {"slug": "pregnancy",       "title_ar": "حاسبة الحمل والولادة",      "title_en": "Pregnancy Calculator",          "desc_ar": "موعد الولادة المتوقع وأسبوع الحمل بدقة طبية.",            "desc_en": "Estimated due date and pregnancy week.",               "category": "health",     "icon": "🤰"},
    {"slug": "bmi",             "title_ar": "مؤشر كتلة الجسم",           "title_en": "BMI Calculator",               "desc_ar": "وزنك المثالي وتصنيفك الصحي بالتفصيل.",                    "desc_en": "Your ideal weight and health category.",               "category": "health",     "icon": "🧍"},
    {"slug": "calorie",         "title_ar": "حاسبة السعرات الحرارية",    "title_en": "Calorie Calculator",           "desc_ar": "احتياجك اليومي من الطاقة حسب نشاطك وهدفك.",               "desc_en": "Daily energy needs based on activity and goal.",       "category": "health",     "icon": "🍎"},
    {"slug": "water",           "title_ar": "حاسبة احتياج الماء",        "title_en": "Water Intake Calculator",      "desc_ar": "كم لتر يحتاج جسمك يوميًا بناءً على وزنك.",                "desc_en": "How many liters your body needs daily.",               "category": "health",     "icon": "💧"},
    {"slug": "age",             "title_ar": "حاسبة العمر",               "title_en": "Age Calculator",               "desc_ar": "عمرك بالسنوات والأشهر والأيام بدقة كاملة.",               "desc_en": "Your exact age in years, months and days.",            "category": "general",    "icon": "🎂"},
    {"slug": "discount",        "title_ar": "حاسبة نسبة الخصم",          "title_en": "Discount Calculator",          "desc_ar": "كم وفّرت فعلًا من السعر الأصلي في التخفيضات.",             "desc_en": "How much you really saved from the original price.",   "category": "general",    "icon": "🏷️"},
    {"slug": "date-diff",       "title_ar": "الوقت بين تاريخين",         "title_en": "Date Difference Calculator",   "desc_ar": "الفارق بين أي تاريخين بالأيام والشهور والسنوات.",          "desc_en": "Gap between any two dates in days and months.",        "category": "general",    "icon": "📅"},
];

function getLatestArticles(limit = 4, lang = "ar") {
    const articles = [];
    const articlesDir = path.join(ROOT_DIR, 'articles');
    if (!fs.existsSync(articlesDir)) return articles;

    const files = fs.readdirSync(articlesDir);
    for (const name of files) {
        if (!name.endsWith('.html') || name.startsWith('index')) continue;
        const slug = name.slice(0, -5);
        const isEn = slug.endsWith('-en');
        if ((lang === 'en') !== isEn) continue;

        try {
            const content = fs.readFileSync(path.join(articlesDir, name), 'utf8');
            const titleMatch = content.match(/<title>(.*?)<\/title>/);
            const descMatch = content.match(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/);
            const dateMatch = content.match(/"datePublished"\s*:\s*"([^"]*)"/);

            if (titleMatch) {
                articles.push({
                    slug: slug,
                    title: titleMatch[1].replace(' | حاسبها', '').replace(' | Hasibha', '').trim(),
                    desc: descMatch ? (descMatch[1].slice(0, 110) + '...') : '',
                    date: dateMatch ? dateMatch[1] : TODAY
                });
            }
        } catch (e) {}
    }
    articles.sort((a, b) => (b.date > a.date ? 1 : -1));
    return articles.slice(0, limit);
}

function buildTabs(lang) {
    const allLabel = lang === 'ar' ? 'الكل' : 'All';
    let tabs = `<button class="tab on" data-cat="all">${allLabel} (${PAGES.length})</button>\n`;
    for (const [key, meta] of Object.entries(CATEGORIES)) {
        const count = PAGES.filter(p => p.category === key).length;
        if (count === 0) continue;
        const label = lang === 'ar' ? meta.ar : meta.en;
        tabs += `<button class="tab" data-cat="${key}">${meta.icon} ${label} (${count})</button>\n`;
    }
    return tabs;
}

function buildCards(lang) {
    let html = '';
    for (const p of PAGES) {
        const title = lang === 'ar' ? p.title_ar : p.title_en;
        const desc = lang === 'ar' ? p.desc_ar : p.desc_en;
        // Check if file exists for en
        const enFileExists = fs.existsSync(path.join(ROOT_DIR, `${p.slug}-en.html`));
        const href = lang === 'ar' ? `/${p.slug}` : (enFileExists ? `/${p.slug}-en` : `/${p.slug}`);
        const cta = lang === 'ar' ? 'استخدم الحاسبة ←' : 'Use Calculator →';
        html += `<a class="card ${p.category}" data-cat="${p.category}" href="${href}">
<span class="card-icon">${p.icon}</span>
<div><h3>${title}</h3><p>${desc}</p></div>
<span class="card-cta">${cta}</span>
</a>\n`;
    }
    return html;
}

function buildArticlesSection(lang, articles) {
    if (!articles || articles.length === 0) return '';
    const ar = lang === 'ar';
    const secTitle = ar ? 'أحدث الأدلة والمقالات' : 'Latest Guides & Articles';
    const viewAll = ar ? 'عرض جميع المقالات ←' : 'View All Articles →';
    const readCta = ar ? 'اقرأ الدليل الكامل ←' : 'Read Full Guide →';

    let cards = '';
    for (const a of articles) {
        cards += `<a class="card gen" href="/articles/${a.slug}">
<span class="card-icon">📖</span>
<div><h3>${a.title}</h3><p>${a.desc}</p></div>
<span class="card-cta">${readCta}</span>
</a>\n`;
    }

    return `<section class="wrap" id="articles">
<div class="section-head" style="display:flex;justify-content:space-between;align-items:center;margin-top:50px">
  <h2>${secTitle}</h2>
  <a href="/articles" style="color:var(--accent);font-size:14px;font-weight:700;text-decoration:none">${viewAll}</a>
</div>
<div class="grid">
${cards}
</div>
</section>\n`;
}

function buildIndex(lang) {
    const ar = lang === 'ar';
    const title = ar ? "حاسبها 2026 — أفضل منصة حاسبات مالية وصحية مجانية في السعودية" : "Hasibha 2026 — Best Free Financial & Health Calculators in Saudi Arabia";
    const desc = ar ? `${PAGES.length} حاسبة مجانية معتمدة في السعودية: حساب المواطن، الضمان المطور، التمويل العقاري، التأمينات والراتب، الزكاة، الحمل، الذهب. نتائج فورية بدون تسجيل.` : `${PAGES.length} free calculators: Citizen Account, Social Security, mortgage, net salary, zakat, pregnancy, gold and more. Instant accurate results.`;
    const other = ar ? "index-en" : "";
    const otherLabel = ar ? "EN" : "عربي";
    const homeHref = ar ? "/" : "/index-en";
    const brand = ar ? "حاسبها" : "Hasibha";

    const navHtml = ar ?
      '<a href="#calculators">الحاسبات</a>\n<a href="/articles">المقالات والأدلة</a>\n<a href="#features">المميزات</a>\n<a href="#faq">الأسئلة الشائعة</a>' :
      '<a href="#calculators">Calculators</a>\n<a href="/articles">Articles & Guides</a>\n<a href="#features">Features</a>\n<a href="#faq">FAQ</a>';

    const stats = [
        [`${PAGES.length}+`, ar ? "حاسبة ذكية مجانية" : "Free Smart Calculators"],
        ["2", ar ? "لغة" : "Languages"],
        ["4", ar ? "تصنيفات رئيسية" : "Categories"],
        ["100%", ar ? "مجاني وبدون تسجيل" : "Free & Instant"],
    ];
    const statsHtml = stats.map(([v, s]) => `<div class="stat"><b>${v}</b><span>${s}</span></div>`).join('\n');

    const features = ar ? [
        ["⚡", "سرعة فائقة ونتائج فورية", "احسب أي عملية بضغطة زر وبدون انتظار أو تحميل خوادم."],
        ["🔒", "خصوصية وأمان 100%", "لا نطلب أي تسجيل أو بيانات شخصية، الحسابات تجري في جهازك فقط."],
        ["📱", "مشاركة سهلة عبر واتساب", "أزرار لمشاركة النتائج مع عائلتك أو زملائك أو نسخها للحافظة."],
        ["🇸🇦", "محدث وفق الأنظمة السعودية", "مبني بدقة على لوائح ساما، التأمينات الاجتماعية، وحساب المواطن."],
    ] : [
        ["⚡", "Instant Real-Time Results", "Run any calculation with zero delay or server roundtrips."],
        ["🔒", "100% Private & Anonymous", "No registration required. Everything computes locally in your browser."],
        ["📱", "One-Click WhatsApp Sharing", "Easily share results and calculations with friends and family."],
        ["🇸🇦", "Saudi Regulated & Verified", "Built exactly per SAMA, GOSI, and official ministry guidelines."],
    ];
    const featHtml = features.map(([i, t, s]) => `<div class="feature"><b>${i} ${t}</b><span>${s}</span></div>`).join('\n');

    const faqs = ar ? [
        ["هل جميع حاسبات موقع حاسبها مجانية؟", "نعم، كافة الأدوات والحاسبات مجانية بالكامل ومتاحة للجميع دون أي رسوم أو اشتراكات أو تسجيل دخول."],
        ["كيف تضمنون دقة العمليات الحسابية؟", "معادلاتنا الحسابية مبنية استناداً إلى أحدث اللوائح والأنظمة الحكومية الرسمية في المملكة العربية السعودية (البنك المركزي السعودي ساما، التأمينات الاجتماعية، وزارة الموارد البشرية، وهيئة الزكاة والضريبة والجمارك)."],
        ["هل تُحفظ البيانات أو المبالغ التي أدخلها؟", "لا على الإطلاق. موقع حاسبها مصمم ليعمل بتقنية المعالجة المحلية داخل متصفحك (Client-side)، فلا يتم تخزين أي أرقام أو بيانات مالية."],
    ] : [
        ["Are all calculators completely free?", "Yes, 100% free with no hidden fees, subscriptions, or login required."],
        ["How accurate are the financial calculations?", "Calculations strictly adhere to official Saudi government regulations (SAMA, GOSI, ZATCA, HRSD)."],
        ["Is any personal data stored?", "No. All calculations run strictly in your local browser sandbox."],
    ];
    const faqHtml = faqs.map(([q, a]) => `<details><summary>${q}</summary><div class="faq-a">${a}</div></details>`).join('\n');

    const footLinks = ar ?
      '<a href="/privacy">سياسة الخصوصية</a>\n<a href="/contact">اتصل بنا</a>\n<a href="/about">من نحن</a>\n<a href="/articles">المقالات والأدلة</a>' :
      '<a href="/privacy-en">Privacy Policy</a>\n<a href="/contact-en">Contact</a>\n<a href="/about-en">About</a>\n<a href="/articles">Articles</a>';

    const schema = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": brand,
        "url": SITE_URL + (ar ? "/" : "/index-en"),
        "inLanguage": ar ? "ar-SA" : "en-US",
        "description": desc,
        "potentialAction": {
            "@type": "SearchAction",
            "target": `${SITE_URL}/#calculators`,
            "query-input": "required name=search_term_string"
        }
    };

    const articlesSection = buildArticlesSection(lang, getLatestArticles(4, lang));

    return `<!DOCTYPE html>
<html lang="${ar ? 'ar' : 'en'}" dir="${ar ? 'rtl' : 'ltr'}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${title}</title>
<meta name="description" content="${desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="${SITE_URL}/${ar ? '' : 'index-en'}">
<link rel="alternate" hreflang="ar" href="${SITE_URL}/">
<link rel="alternate" hreflang="en" href="${SITE_URL}/index-en">
<link rel="alternate" hreflang="x-default" href="${SITE_URL}/">
<link rel="icon" type="image/png" href="${SITE_URL}/images/logo.png">
<link rel="apple-touch-icon" href="${SITE_URL}/images/logo.png">
<link rel="preload" as="image" href="${SITE_URL}/images/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<link rel="preconnect" href="https://www.googletagmanager.com">
<link rel="preconnect" href="https://www.google-analytics.com">
<meta property="og:title" content="${title}">
<meta property="og:description" content="${desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="${brand}">
<meta property="og:image" content="${SITE_URL}/images/logo.png">
<meta property="og:image:width" content="512">
<meta property="og:image:height" content="512">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${title}">
<meta name="twitter:description" content="${desc}">
<meta name="twitter:image" content="${SITE_URL}/images/logo.png">
<meta name="theme-color" content="#0b0d10">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NZLXJFVCDW"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag('js',new Date());gtag('config','G-NZLXJFVCDW');</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1508132460803414" crossorigin="anonymous"></script>
<script type="application/ld+json">
${JSON.stringify(schema, null, 2)}
</script>
<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<header class="site-header">
<div class="wrap header-in">
<a class="logo" href="${homeHref}">
<img src="${SITE_URL}/images/logo.png" alt="${brand}" width="54" height="36" style="height:36px;vertical-align:middle">
${brand}
</a>
<nav class="main-nav">${navHtml}</nav>
<div class="header-actions">
<button class="theme-btn" id="themeBtn" aria-label="تبديل الوضع الليلي">🌓</button>
<a class="lang-btn" href="/${other}">${otherLabel}</a>
</div>
</div>
</header>
<section class="hero">
<div class="badge"><span class="dot"></span>${ar ? 'المنصة السعودية الأولى للحاسبات الذكية' : 'Saudi Leading Smart Calculators'}</div>
<h1>${ar ? 'كل حاسباتك المالية والصحية في مكان واحد' : 'All Your Financial & Health Calculators in One Place'}</h1>
<p class="lead">${ar ? 'مصممة خصيصاً للسوق السعودي — دقيقة، سريعة، ومجانية بالكامل مع نتائج فورية.' : 'Built for the Saudi market — accurate, fast and completely free with instant results.'}</p>
<div class="stats">${statsHtml}</div>
</section>
<section class="wrap" id="calculators">
<div class="section-head"><h2>${ar ? 'اختر حاسبتك' : 'Choose Your Calculator'}</h2></div>
<div class="tabs">
${buildTabs(lang)}
</div>
<div class="grid">
${buildCards(lang)}
</div>
</section>
${articlesSection}
<section class="wrap" id="features">
<div class="section-head"><h2>${ar ? 'لماذا يفضل الآلاف حاسبها؟' : 'Why Choose Hasibha?'}</h2></div>
<div class="features-grid">
${featHtml}
</div>
</section>
<section class="wrap faq" id="faq">
<div class="section-head"><h2>${ar ? 'الأسئلة الشائعة' : 'FAQ'}</h2></div>
${faqHtml}
</section>
<footer class="site-footer">
<div class="wrap footer-in">
<a class="logo" href="${homeHref}">
<img src="${SITE_URL}/images/logo.png" alt="${brand}" width="42" height="28" style="height:28px;vertical-align:middle">
${brand}
</a>
<nav>${footLinks}</nav>
<p>${ar ? `حاسبها © ${YEAR} — جميع الحقوق محفوظة` : `Hasibha © ${YEAR} — All Rights Reserved`}</p>
</div>
</footer>
<script>
(function(){
var root=document.documentElement, btn=document.getElementById('themeBtn');
function apply(t){ if(t==='dark'){root.setAttribute('data-theme','dark');}else{root.removeAttribute('data-theme');} }
var saved=null; try{saved=localStorage.getItem('hs-theme');}catch(e){}
if(!saved){saved=(window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'light';}
apply(saved);
btn.addEventListener('click',function(){
var next=root.getAttribute('data-theme')==='dark'?'light':'dark';
apply(next); try{localStorage.setItem('hs-theme',next);}catch(e){}
});
})();
(function(){
var tabs=document.querySelectorAll('.tab');
var cards=document.querySelectorAll('.card[data-cat]');
tabs.forEach(function(btn){
btn.addEventListener('click',function(){
tabs.forEach(function(b){b.classList.remove('on');});
btn.classList.add('on');
var cat=btn.getAttribute('data-cat');
cards.forEach(function(card){
var show=(cat==='all')||(card.getAttribute('data-cat')===cat);
if(show){card.classList.remove('hide');card.style.display='';}
else{card.classList.add('hide');card.style.display='none';}
});
});
});
})();
</script>
</body>
</html>
`;
}

// 1. Generate index.html and index-en.html
console.log('Writing index.html...');
fs.writeFileSync(path.join(ROOT_DIR, 'index.html'), buildIndex('ar'), 'utf8');

console.log('Writing index-en.html...');
fs.writeFileSync(path.join(ROOT_DIR, 'index-en.html'), buildIndex('en'), 'utf8');

// 2. Generate sitemap.xml
console.log('Generating sitemap.xml...');
const sitemapUrls = [
    { loc: `${SITE_URL}/`, priority: '1.0', changefreq: 'daily' },
    { loc: `${SITE_URL}/index-en`, priority: '0.9', changefreq: 'daily' },
    { loc: `${SITE_URL}/privacy`, priority: '0.5', changefreq: 'monthly' },
    { loc: `${SITE_URL}/privacy-en`, priority: '0.4', changefreq: 'monthly' },
    { loc: `${SITE_URL}/contact`, priority: '0.5', changefreq: 'monthly' },
    { loc: `${SITE_URL}/contact-en`, priority: '0.4', changefreq: 'monthly' },
    { loc: `${SITE_URL}/about`, priority: '0.5', changefreq: 'monthly' },
    { loc: `${SITE_URL}/about-en`, priority: '0.4', changefreq: 'monthly' },
];

for (const p of PAGES) {
    sitemapUrls.push({ loc: `${SITE_URL}/${p.slug}`, priority: '0.9', changefreq: 'weekly' });
    if (fs.existsSync(path.join(ROOT_DIR, `${p.slug}-en.html`))) {
        sitemapUrls.push({ loc: `${SITE_URL}/${p.slug}-en`, priority: '0.8', changefreq: 'weekly' });
    }
}

// Articles
const articlesDir = path.join(ROOT_DIR, 'articles');
if (fs.existsSync(articlesDir)) {
    sitemapUrls.push({ loc: `${SITE_URL}/articles/`, priority: '0.8', changefreq: 'weekly' });
    sitemapUrls.push({ loc: `${SITE_URL}/articles/index-en`, priority: '0.7', changefreq: 'weekly' });
    const articleFiles = fs.readdirSync(articlesDir);
    for (const f of articleFiles) {
        if (!f.endsWith('.html') || f.startsWith('index')) continue;
        const slug = f.slice(0, -5);
        const pr = slug.endsWith('-en') ? '0.7' : '0.8';
        sitemapUrls.push({ loc: `${SITE_URL}/articles/${slug}`, priority: pr, changefreq: 'weekly' });
    }
}

const sitemapXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${sitemapUrls.map(u => `  <url>
    <loc>${u.loc}</loc>
    <lastmod>${TODAY}</lastmod>
    <changefreq>${u.changefreq}</changefreq>
    <priority>${u.priority}</priority>
  </url>`).join('\n')}
</urlset>`;

fs.writeFileSync(path.join(ROOT_DIR, 'sitemap.xml'), sitemapXml, 'utf8');
console.log(`✅ sitemap.xml generated with ${sitemapUrls.length} URLs!`);
console.log('🎉 Index and Sitemap built successfully!');
