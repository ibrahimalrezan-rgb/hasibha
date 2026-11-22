// Unifies head assets, header, footer and shared scripts across every page.
// Idempotent: safe to run many times.  Usage: node automation/unify.js
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const VER = '3';

function list() {
  const out = [];
  for (const f of fs.readdirSync(ROOT)) if (f.endsWith('.html') && !f.startsWith('google')) out.push(f);
  for (const f of fs.readdirSync(path.join(ROOT, 'articles'))) if (f.endsWith('.html')) out.push('articles/' + f);
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

const ICONS = '<svg class="i-moon" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg><svg class="i-sun" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';

function header(isAr, langHref) {
  if (isAr) return `<header class="site-header">
  <div class="wrap header-in">
    <a class="logo" href="/" aria-label="حاسبها — الصفحة الرئيسية"><img src="/images/logo.png" alt="حاسبها" width="54" height="36">حاسبها</a>
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
  return `<header class="site-header">
  <div class="wrap header-in">
    <a class="logo" href="/index-en" aria-label="Hasibha — Home"><img src="/images/logo.png" alt="Hasibha" width="54" height="36">Hasibha</a>
    <nav class="main-nav" aria-label="Main navigation">
      <a href="/index-en#calculators">Calculators</a>
      <a href="/articles/index-en">Articles</a>
      <a href="/about-en">About</a>
      <a href="/contact-en">Contact</a>
    </nav>
    <div class="header-actions">
      <button class="theme-btn" id="themeBtn" type="button" aria-label="Toggle dark mode">${ICONS}</button>
      <a class="lang-btn" href="${langHref}" hreflang="ar" lang="ar">عربي</a>
    </div>
  </div>
</header>`;
}

function footer(isAr) {
  if (isAr) return `<footer class="site-footer">
  <div class="wrap footer-in">
    <a class="logo" href="/"><img src="/images/logo.png" alt="حاسبها" width="42" height="28" loading="lazy">حاسبها</a>
    <nav aria-label="روابط الفوتر">
      <a href="/#calculators">جميع الحاسبات</a>
      <a href="/articles/">المقالات</a>
      <a href="/about">من نحن</a>
      <a href="/contact">تواصل معنا</a>
      <a href="/privacy">سياسة الخصوصية</a>
    </nav>
    <p>حاسبها © <span id="year">2026</span> — جميع الحقوق محفوظة</p>
  </div>
</footer>`;
  return `<footer class="site-footer">
  <div class="wrap footer-in">
    <a class="logo" href="/index-en"><img src="/images/logo.png" alt="Hasibha" width="42" height="28" loading="lazy">Hasibha</a>
    <nav aria-label="Footer links">
      <a href="/index-en#calculators">All Calculators</a>
      <a href="/articles/index-en">Articles</a>
      <a href="/about-en">About</a>
      <a href="/contact-en">Contact</a>
      <a href="/privacy-en">Privacy Policy</a>
    </nav>
    <p>Hasibha © <span id="year">2026</span> — All rights reserved</p>
  </div>
</footer>`;
}

const ASSETS = `<!--hs:assets-->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;800;900&display=swap">
<link rel="stylesheet" href="/css/style.css?v=${VER}">
<link rel="dns-prefetch" href="https://pagead2.googlesyndication.com">
<link rel="dns-prefetch" href="https://www.googletagmanager.com">
<script>try{var t=localStorage.getItem('hs-theme');if(t==='dark'||(!t&&window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches))document.documentElement.setAttribute('data-theme','dark')}catch(e){}</script>
<!--/hs:assets-->`;

const TOAST = '<div class="toast" id="toast"></div>';
const APPJS = `<div class="toast" id="toast"></div>\n<script src="/js/app.js?v=${VER}"></script>`;

let changed = 0;
for (const rel of list()) {
  const file = path.join(ROOT, rel);
  let c = fs.readFileSync(file, 'utf8');
  const orig = c;
  const isAr = /<html[^>]*lang="ar"/i.test(c);

  // ---- head assets
  c = c.replace(/<!--hs:assets-->[\s\S]*?<!--\/hs:assets-->\s*/g, '');
  c = c.replace(/[ \t]*<link[^>]*(fonts\.googleapis\.com|fonts\.gstatic\.com)[^>]*>\s*\n?/gi, '');
  c = c.replace(/[ \t]*<link[^>]*href="\/css\/style\.css[^"]*"[^>]*>\s*\n?/gi, '');
  c = c.replace(/[ \t]*<link rel="preload" as="image" href="\/images\/logo\.png">\s*\n?/gi, '');
  c = c.replace(/[ \t]*<link rel="(preconnect|dns-prefetch)" href="https:\/\/(www\.googletagmanager\.com|www\.google-analytics\.com|pagead2\.googlesyndication\.com)"[^>]*>\s*\n?/gi, '');
  c = c.replace(/<style(?![^>]*data-keep)[^>]*>[\s\S]*?<\/style>\s*/gi, '');
  c = c.replace(/<meta name="theme-color"[^>]*>/i, '<meta name="theme-color" content="#059669">');
  // insert assets after viewport meta (or after charset)
  if (/<meta name="viewport"[^>]*>/i.test(c)) c = c.replace(/(<meta name="viewport"[^>]*>)/i, '$1\n' + ASSETS);
  else c = c.replace(/(<meta charset[^>]*>)/i, '$1\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n' + ASSETS);

  // ---- header / footer
  const langHref = counterpart(rel, isAr);
  c = c.replace(/<header[\s\S]*?<\/header>/i, header(isAr, langHref));
  c = c.replace(/<footer[\s\S]*?<\/footer>/i, footer(isAr));

  // ---- old theme / year / toast code
  c = c.replace(/\(function\(\)\{\s*var root\s*=\s*document\.documentElement[\s\S]*?\}\)\(\);\s*/g, '');
  c = c.replace(/var y=document\.getElementById\('year'\);if\(y\)y\.textContent=new Date\(\)\.getFullYear\(\);\s*/g, '');
  c = c.replace(/document\.getElementById\(['"]year['"]\)\.textContent\s*=\s*new Date\(\)\.getFullYear\(\);\s*/g, '');
  c = c.replace(/[ \t]*<div class="toast" id="toast"[^>]*>[^<]*<\/div>\s*\n?/g, '');
  // drop now-empty inline scripts
  c = c.replace(/<script>\s*<\/script>\s*/g, '');

  // ---- shared app.js directly after footer
  c = c.replace(/[ \t]*<script src="\/js\/app\.js[^"]*"><\/script>\s*\n?/g, '');
  c = c.replace(/<\/footer>\s*/i, '</footer>\n' + APPJS + '\n');

  if (c !== orig) { fs.writeFileSync(file, c, 'utf8'); changed++; }
}
console.log('unify: updated ' + changed + ' files');
