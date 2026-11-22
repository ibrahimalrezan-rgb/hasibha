// Unifies head assets, header, footer and shared scripts across every page (excluding index homepages).
// Idempotent: safe to run many times. Usage: node automation/unify.js
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const VER = '4';

function list() {
  const out = [];
  for (const f of fs.readdirSync(ROOT)) {
    if (f.endsWith('.html') && !f.startsWith('google') && f !== 'index.html' && f !== 'index-en.html') {
      out.push(f);
    }
  }
  const artDir = path.join(ROOT, 'articles');
  if (fs.existsSync(artDir)) {
    for (const f of fs.readdirSync(artDir)) {
      if (f.endsWith('.html')) out.push('articles/' + f);
    }
  }
  return out;
}

const exists = rel => fs.existsSync(path.join(ROOT, rel));

function urlOf(rel) {
  let u = '/' + rel.replace(/\.html$/, '');
  if (u === '/index') return '/';
  if (u === '/articles/index') return '/articles/';
  return u;
}

function counterpart(rel, isAr) {
  const base = rel.replace(/\.html$/, '');
  let other;
  if (isAr) other = base + '-en';
  else other = base.replace(/-en$/, '');
  if (exists(other + '.html')) return urlOf(other + '.html');
  return isAr ? '/index-en' : '/';
}

const SVG_MARK = `<div class="logo-mark">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <rect x="3" y="3" width="8" height="8" rx="2" fill="white" fill-opacity="0.95"/>
        <rect x="13" y="3" width="8" height="8" rx="2" fill="white" fill-opacity="0.45"/>
        <rect x="3" y="13" width="8" height="8" rx="2" fill="white" fill-opacity="0.45"/>
        <path d="M14 17H20M17 14V20" stroke="white" stroke-width="2.4" stroke-linecap="round"/>
      </svg>
    </div>`;

const ICONS = `<svg class="i-moon" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg><svg class="i-sun" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>`;

function header(isAr, langHref) {
  if (isAr) {
    return `<header class="site-header">
  <div class="wrap header-in">
    <a class="logo" href="/" aria-label="حاسبها — الصفحة الرئيسية">
      ${SVG_MARK}
      <span class="logo-text">حاسبها</span>
      <span class="logo-badge">2026</span>
    </a>
    <nav class="main-nav" aria-label="التنقل الرئيسي">
      <a href="/#calculators">الحاسبات</a>
      <a href="/articles/">المقالات</a>
      <a href="/about">من نحن</a>
      <a href="/contact">تواصل معنا</a>
    </nav>
    <div class="header-actions">
      <button class="theme-btn" id="themeBtn" type="button" aria-label="تبديل الوضع الليلي">${ICONS}</button>
      <a class="lang-btn" href="${langHref}" hreflang="en" lang="en">EN</a>
    </div>
  </div>
</header>`;
  } else {
    return `<header class="site-header">
  <div class="wrap header-in">
    <a class="logo" href="/index-en" aria-label="Hasibha — Home">
      ${SVG_MARK}
      <span class="logo-text">Hasibha</span>
      <span class="logo-badge">2026</span>
    </a>
    <nav class="main-nav" aria-label="Main navigation">
      <a href="/index-en#calculators">Calculators</a>
      <a href="/articles/index-en">Articles</a>
      <a href="/about-en">About</a>
      <a href="/contact-en">Contact</a>
    </nav>
    <div class="header-actions">
      <button class="theme-btn" id="themeBtn" type="button" aria-label="Toggle dark mode">${ICONS}</button>
      <a class="lang-btn" href="${langHref}" hreflang="ar" lang="ar">العربية</a>
    </div>
  </div>
</header>`;
  }
}

function footer(isAr) {
  if (isAr) {
    return `<footer class="site-footer">
  <div class="wrap footer-in">
    <div class="footer-brand">
      <a class="logo" href="/">
        ${SVG_MARK}
        <span class="logo-text">حاسبها</span>
      </a>
      <p>منصتك السعودية الشاملة للحاسبات المالية، التحويلات، والقياسات الصحية بدقة فورية وخصوصية تامة.</p>
    </div>
    <div class="footer-col">
      <h4>حاسبات سريعة</h4>
      <ul>
        <li><a href="/vat">ضريبة القيمة المضافة</a></li>
        <li><a href="/salary">الراتب بعد التأمينات</a></li>
        <li><a href="/mortgage">التمويل العقاري</a></li>
        <li><a href="/eos">نهاية الخدمة</a></li>
        <li><a href="/zakat">حاسبة الزكاة</a></li>
        <li><a href="/bmi">مؤشر كتلة الجسم</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>روابط ومعلومات</h4>
      <p>جميع الحاسبات تعمل محلياً في جهازك بدون تخزين بياناتك. النتائج استرشادية ومحدثة لأنظمة 2026.</p>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <p>حاسبها © <span id="year">2026</span> — جميع الحقوق محفوظة</p>
    <div style="display:flex;gap:14px;">
      <a href="/about">من نحن</a>
      <a href="/contact">تواصل معنا</a>
      <a href="/privacy">الخصوصية</a>
    </div>
  </div>
</footer>`;
  } else {
    return `<footer class="site-footer">
  <div class="wrap footer-in">
    <div class="footer-brand">
      <a class="logo" href="/index-en">
        ${SVG_MARK}
        <span class="logo-text">Hasibha</span>
      </a>
      <p>Your all-in-one Saudi platform for financial, health, and conversion calculations with real-time accuracy and privacy.</p>
    </div>
    <div class="footer-col">
      <h4>Quick Calculators</h4>
      <ul>
        <li><a href="/vat-en">VAT 15%</a></li>
        <li><a href="/salary-en">Salary after GOSI</a></li>
        <li><a href="/mortgage-en">Mortgage Loan</a></li>
        <li><a href="/eos-en">End of Service</a></li>
        <li><a href="/zakat-en">Zakat Calculator</a></li>
        <li><a href="/bmi-en">BMI Calculator</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Privacy & Legal</h4>
      <p>Calculations run locally on your device without storing inputs. Results are for guidance and reflect 2026 Saudi regulations.</p>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <p>Hasibha © <span id="year">2026</span> — All rights reserved</p>
    <div style="display:flex;gap:14px;">
      <a href="/about-en">About</a>
      <a href="/contact-en">Contact</a>
      <a href="/privacy-en">Privacy</a>
    </div>
  </div>
</footer>`;
  }
}

function getAssets(isAr) {
  const fontLink = isAr
    ? '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap">'
    : '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">';

  return `<!--hs:assets-->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
${fontLink}
<link rel="stylesheet" href="/css/style.css?v=${VER}">
<link rel="dns-prefetch" href="https://pagead2.googlesyndication.com">
<link rel="dns-prefetch" href="https://www.googletagmanager.com">
<script>try{var t=localStorage.getItem('hs-theme')||localStorage.getItem('hasibha_theme');if(t==='dark'||(!t&&window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)){document.documentElement.setAttribute('data-theme','dark');document.documentElement.classList.add('dark');}}catch(e){}</script>
<!--/hs:assets-->`;
}

const TOAST = '<div class="toast" id="toast"></div>';
const APPJS = `<div class="toast" id="toast"></div>\n<script src="/js/app.js?v=${VER}"></script>`;

let changed = 0;
for (const rel of list()) {
  const file = path.join(ROOT, rel);
  let c = fs.readFileSync(file, 'utf8');
  const orig = c;
  const isAr = !/-en\.html$/.test(rel) && !rel.endsWith('index-en.html');

  // assets
  c = c.replace(/<!--hs:assets-->[\s\S]*?<!--\/hs:assets-->\s*/g, '');
  c = c.replace(/[ \t]*<link[^>]*(fonts\.googleapis\.com|fonts\.gstatic\.com)[^>]*>\s*\n?/gi, '');
  c = c.replace(/[ \t]*<link[^>]*href="\/css\/style\.css[^"]*"[^>]*>\s*\n?/gi, '');
  c = c.replace(/[ \t]*<link rel="preload" as="image" href="\/images\/logo\.png">\s*\n?/gi, '');
  c = c.replace(/<meta name="theme-color"[^>]*>/i, '<meta name="theme-color" content="#059669">');

  const assets = getAssets(isAr);
  if (/<meta name="viewport"[^>]*>/i.test(c)) {
    c = c.replace(/(<meta name="viewport"[^>]*>)/i, '$1\n' + assets);
  } else if (/<meta charset[^>]*>/i.test(c)) {
    c = c.replace(/(<meta charset[^>]*>)/i, '$1\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n' + assets);
  }

  // header & footer
  const langHref = counterpart(rel, isAr);
  c = c.replace(/<header[\s\S]*?<\/header>/i, header(isAr, langHref));
  c = c.replace(/<footer[\s\S]*?<\/footer>/i, footer(isAr));

  // scripts
  c = c.replace(/[ \t]*<div class="toast" id="toast"[^>]*>[^<]*<\/div>\s*\n?/g, '');
  c = c.replace(/[ \t]*<script src="\/js\/app\.js[^"]*"><\/script>\s*\n?/g, '');
  c = c.replace(/<\/footer>\s*/i, '</footer>\n' + APPJS + '\n');

  if (c !== orig) {
    fs.writeFileSync(file, c, 'utf8');
    changed++;
  }
}
console.log('unify: updated ' + changed + ' files');
