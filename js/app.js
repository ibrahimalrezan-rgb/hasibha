/* Hasibha — shared site script (theme, year, share/copy for every calculator) */
(function () {
  'use strict';
  var doc = document, root = doc.documentElement;
  var isAr = (root.getAttribute('lang') || 'ar').indexOf('ar') === 0;
  var T = isAr
    ? { wa: 'مشاركة عبر واتساب', copy: 'نسخ النتيجة', copied: 'تم نسخ النتيجة ✅', via: 'احسبها مجاناً عبر حاسبها:', fail: 'تعذّر النسخ' }
    : { wa: 'Share on WhatsApp', copy: 'Copy result', copied: 'Result copied ✅', via: 'Calculate it free on Hasibha:', fail: 'Copy failed' };

  /* ---------- theme ---------- */
  function applyTheme(t) { if (t === 'dark') root.setAttribute('data-theme', 'dark'); else root.removeAttribute('data-theme'); }
  var btn = doc.getElementById('themeBtn');
  if (btn) btn.addEventListener('click', function () {
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    applyTheme(next);
    try { localStorage.setItem('hs-theme', next); } catch (e) {}
  });

  /* ---------- footer year ---------- */
  var y = doc.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  /* ---------- toast ---------- */
  function toast(msg) {
    var t = doc.getElementById('toast');
    if (!t) { t = doc.createElement('div'); t.id = 'toast'; t.className = 'toast'; t.setAttribute('role', 'status'); doc.body.appendChild(t); }
    t.textContent = msg; t.classList.add('show');
    clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove('show'); }, 2400);
  }

  /* ---------- number formatting ---------- */
  function fmt(n, d) {
    if (n === null || n === undefined || isNaN(n)) return '0';
    d = (d === undefined) ? 2 : d;
    return Number(n).toLocaleString('en-US', { minimumFractionDigits: 0, maximumFractionDigits: d });
  }
  function fmtFixed(n, d) {
    d = (d === undefined) ? 2 : d;
    return Number(n || 0).toLocaleString('en-US', { minimumFractionDigits: d, maximumFractionDigits: d });
  }

  /* ---------- build share text from a result card ---------- */
  function clean(s) { return (s || '').replace(/\s+/g, ' ').trim(); }
  function isVisible(el) { return !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length); }
  function resultText(card) {
    if (card.getAttribute('data-share-text')) return card.getAttribute('data-share-text');
    if (typeof window.getShareText === 'function') { var c = window.getShareText(card); if (c) return c; }
    var lines = [];
    var hero = card.querySelector('.result-hero');
    if (hero) {
      var lab = hero.querySelector('.result-label'), val = hero.querySelector('.result-val'), unit = hero.querySelector('.result-unit'), sub = hero.querySelector('.result-sub');
      var line = (lab ? clean(lab.textContent) + ': ' : '') + (val ? clean(val.textContent) : '') + (unit ? ' ' + clean(unit.textContent) : '');
      if (clean(line)) lines.push(line);
      if (sub && clean(sub.textContent)) lines.push(clean(sub.textContent));
    }
    var pairs = card.querySelectorAll('.result-item, .breakdown-item, .result-row');
    for (var i = 0; i < pairs.length; i++) {
      var p = pairs[i]; if (!isVisible(p)) continue;
      var a = p.querySelector('span, .result-label'), b = p.querySelector('b, strong, .result-value');
      if (a && b && clean(b.textContent) && clean(b.textContent) !== '—') lines.push('• ' + clean(a.textContent) + ': ' + clean(b.textContent));
    }
    if (!lines.length) {
      var clone = card.cloneNode(true);
      var sa = clone.querySelector('.share-actions'); if (sa) sa.parentNode.removeChild(sa);
      lines.push(clean(clone.textContent).slice(0, 600));
    }
    return lines.join('\n');
  }
  function pageTitle() {
    var h1 = doc.querySelector('h1');
    return clean(h1 ? h1.textContent : doc.title).replace(/^[^\w\u0600-\u06FF]+/, '');
  }
  function pageUrl() { return location.origin + location.pathname.replace(/\.html$/, ''); }
  function fullText(card) {
    return '📊 ' + pageTitle() + '\n' + resultText(card) + '\n\n' + T.via + '\n' + pageUrl();
  }

  function share(card) {
    card = card || doc.querySelector('.result-card');
    var text = card ? fullText(card) : pageTitle() + '\n' + pageUrl();
    window.open('https://wa.me/?text=' + encodeURIComponent(text), '_blank', 'noopener');
    if (window.gtag) try { gtag('event', 'share', { method: 'whatsapp', item_id: location.pathname }); } catch (e) {}
  }
  function copy(card) {
    card = card || doc.querySelector('.result-card');
    var text = card ? fullText(card) : pageUrl();
    function fallback() {
      var ta = doc.createElement('textarea'); ta.value = text; ta.setAttribute('readonly', '');
      ta.style.position = 'fixed'; ta.style.opacity = '0'; doc.body.appendChild(ta); ta.select();
      try { doc.execCommand('copy'); toast(T.copied); } catch (e) { toast(T.fail); }
      doc.body.removeChild(ta);
    }
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(function () { toast(T.copied); }, fallback);
    else fallback();
  }

  var WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4c-1-1.6-1.5-3.4-1.5-5.2C2.2 6.6 6.6 2.2 12 2.2c2.6 0 5.1 1 6.9 2.9 1.8 1.8 2.9 4.3 2.9 6.9 0 5.4-4.4 9.8-9.8 9.8zM20.5 3.5C18.2 1.2 15.2 0 12 0 5.4 0 0 5.4 0 12c0 2.1.6 4.2 1.6 6L0 24l6.2-1.6c1.8 1 3.8 1.5 5.8 1.5 6.6 0 12-5.4 12-12 0-3.2-1.2-6.2-3.5-8.4z"/></svg>';
  var CP_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>';

  function attachShare(card) {
    if (card.getAttribute('data-no-share') !== null || card.querySelector('.share-actions')) return;
    var box = doc.createElement('div'); box.className = 'share-actions';
    var wa = doc.createElement('button'); wa.type = 'button'; wa.className = 'share-btn whatsapp-btn'; wa.innerHTML = WA_SVG + '<span>' + T.wa + '</span>';
    var cp = doc.createElement('button'); cp.type = 'button'; cp.className = 'share-btn copy-btn'; cp.innerHTML = CP_SVG + '<span>' + T.copy + '</span>';
    wa.addEventListener('click', function () { share(card); });
    cp.addEventListener('click', function () { copy(card); });
    box.appendChild(wa); box.appendChild(cp); card.appendChild(box);
  }
  function initShare() {
    var cards = doc.querySelectorAll('.result-card');
    for (var i = 0; i < cards.length; i++) attachShare(cards[i]);
  }
  if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', initShare); else initShare();

  /* ---------- helpers for calculators ---------- */
  function show(el) { if (typeof el === 'string') el = doc.getElementById(el); if (el) { el.hidden = false; el.style.display = ''; attachShare(el); } }
  function hide(el) { if (typeof el === 'string') el = doc.getElementById(el); if (el) el.hidden = true; }
  function num(id) { var el = doc.getElementById(id); if (!el) return 0; var v = parseFloat(String(el.value).replace(/,/g, '')); return isNaN(v) ? 0 : v; }
  function setText(id, v) { var el = doc.getElementById(id); if (el) el.textContent = v; }

  window.Hasibha = { isAr: isAr, fmt: fmt, fmtFixed: fmtFixed, toast: toast, share: share, copy: copy, show: show, hide: hide, num: num, setText: setText, attachShare: attachShare };
  /* backwards compatibility for inline handlers */
  window.shareWhatsApp = function () { share(); };
  window.copyResult = function () { copy(); };
})();
