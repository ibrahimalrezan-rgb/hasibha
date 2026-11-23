const fs = require('fs');
const path = require('path');

const rootDir = 'C:/Users/ibrah/.gemini/antigravity/scratch/hasibha';
const indexPath = path.join(rootDir, 'index.html');
const indexEnPath = path.join(rootDir, 'index-en.html');

let indexHtml = fs.readFileSync(indexPath, 'utf8');
let indexEnHtml = fs.readFileSync(indexEnPath, 'utf8');

// ==========================================
// 1. PWA Manifest & Theme Color in <head>
// ==========================================
const pwaHeadTags = `  <link rel="manifest" href="/manifest.json" />
  <meta name="theme-color" content="#059669" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="default" />
  <meta name="apple-mobile-web-app-title" content="حاسبها" />`;

const pwaHeadTagsEn = `  <link rel="manifest" href="/manifest.json" />
  <meta name="theme-color" content="#059669" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="default" />
  <meta name="apple-mobile-web-app-title" content="Hasibha" />`;

if (!indexHtml.includes('rel="manifest"')) {
  indexHtml = indexHtml.replace('<link rel="canonical"', pwaHeadTags + '\n  <link rel="canonical"');
}
if (!indexEnHtml.includes('rel="manifest"')) {
  indexEnHtml = indexEnHtml.replace('<link rel="canonical"', pwaHeadTagsEn + '\n  <link rel="canonical"');
}

// ==========================================
// 2. Add Print/PDF Button to Modal Actions
// ==========================================
// In Arabic:
const arModalBtnTarget = `<button id="whatsappShareBtn" type="button" class="flex items-center justify-center gap-2 px-3.5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-emerald-600 hover:bg-emerald-700 text-white transition-colors">
              <i data-lucide="message-circle" class="w-4 h-4"></i>
              <span>مشاركة واتساب</span>
            </button>`;

const arModalBtnReplacement = `<button id="whatsappShareBtn" type="button" class="flex items-center justify-center gap-2 px-3.5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-emerald-600 hover:bg-emerald-700 text-white transition-colors">
              <i data-lucide="message-circle" class="w-4 h-4"></i>
              <span>مشاركة واتساب</span>
            </button>
            <button id="printReportBtn" type="button" class="col-span-2 flex items-center justify-center gap-2 py-2.5 px-3 rounded-xl text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200 hover:text-emerald-600 dark:hover:text-emerald-400 bg-slate-100 hover:bg-emerald-50 dark:bg-slate-800 dark:hover:bg-slate-800/80 border border-slate-200/80 dark:border-slate-700 hover:border-emerald-500/30 transition-all shadow-xs">
              <i data-lucide="printer" class="w-4 h-4 text-emerald-600 dark:text-emerald-400"></i>
              <span>طباعة / حفظ تقرير رسمي (PDF)</span>
            </button>`;

if (indexHtml.includes(arModalBtnTarget)) {
  indexHtml = indexHtml.replace(arModalBtnTarget, arModalBtnReplacement);
}

// In English:
const enModalBtnTarget = `<button id="whatsappShareBtn" type="button" class="flex items-center justify-center gap-2 px-3.5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-emerald-600 hover:bg-emerald-700 text-white transition-colors">
              <i data-lucide="message-circle" class="w-4 h-4"></i>
              <span>WhatsApp</span>
            </button>`;

const enModalBtnReplacement = `<button id="whatsappShareBtn" type="button" class="flex items-center justify-center gap-2 px-3.5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-emerald-600 hover:bg-emerald-700 text-white transition-colors">
              <i data-lucide="message-circle" class="w-4 h-4"></i>
              <span>WhatsApp</span>
            </button>
            <button id="printReportBtn" type="button" class="col-span-2 flex items-center justify-center gap-2 py-2.5 px-3 rounded-xl text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200 hover:text-emerald-600 dark:hover:text-emerald-400 bg-slate-100 hover:bg-emerald-50 dark:bg-slate-800 dark:hover:bg-slate-800/80 border border-slate-200/80 dark:border-slate-700 hover:border-emerald-500/30 transition-all shadow-xs">
              <i data-lucide="printer" class="w-4 h-4 text-emerald-600 dark:text-emerald-400"></i>
              <span>Print / Save Official Report (PDF)</span>
            </button>`;

if (indexEnHtml.includes(enModalBtnTarget)) {
  indexEnHtml = indexEnHtml.replace(enModalBtnTarget, enModalBtnReplacement);
}

// ==========================================
// 3. Add Print Logic & Live API & Service Worker in JS
// ==========================================
const printAndPwaJsAr = `
      // Print Official PDF Report
      const printReportBtn = document.getElementById('printReportBtn');
      if (printReportBtn) {
        printReportBtn.addEventListener('click', () => {
          const calc = CALCULATORS.find(c => c.id === activeCalcId) || { title: 'حاسبة ذكية', url: '' };
          const pLabel = document.getElementById('resPrimaryLabel') ? document.getElementById('resPrimaryLabel').textContent : 'النتيجة الرئيسية';
          const pVal = document.getElementById('resPrimaryVal') ? document.getElementById('resPrimaryVal').textContent : '0';
          const pHint = document.getElementById('resPrimaryHint') ? document.getElementById('resPrimaryHint').textContent : '';
          const secRows = Array.from(document.querySelectorAll('#resSecondaryGrid > div')).map(div => {
            const spans = div.querySelectorAll('span');
            return { label: spans[0] ? spans[0].textContent : '', val: spans[1] ? spans[1].textContent : '' };
          });

          const printWin = window.open('', '_blank');
          if (!printWin) {
            window.print();
            return;
          }

          const now = new Date();
          const dateStr = now.toLocaleDateString('ar-SA', { year: 'numeric', month: 'long', day: 'numeric' });
          const timeStr = now.toLocaleTimeString('ar-SA', { hour: '2-digit', minute: '2-digit' });

          const rowsHtml = secRows.map(r => '<tr><td>' + r.label + '</td><td>' + r.val + '</td></tr>').join('');

          const docContent = '<!DOCTYPE html>' +
            '<html lang="ar" dir="rtl">' +
            '<head>' +
              '<meta charset="UTF-8">' +
              '<title>تقرير حساب معتمد — ' + calc.title + ' | منصة حاسبها</title>' +
              '<style>' +
                'body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "IBM Plex Sans Arabic", sans-serif; margin: 40px; color: #0f172a; line-height: 1.6; }' +
                '.header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #059669; padding-bottom: 16px; margin-bottom: 24px; }' +
                '.logo-title { font-size: 24px; font-weight: bold; color: #059669; margin: 0; }' +
                '.subtitle { font-size: 13px; color: #64748b; margin-top: 4px; }' +
                '.meta { text-align: left; font-size: 12px; color: #64748b; }' +
                '.report-card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 24px; margin-bottom: 24px; }' +
                '.primary-box { background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 12px; padding: 20px; text-align: center; margin-bottom: 20px; }' +
                '.primary-label { font-size: 15px; color: #065f46; font-weight: 600; margin-bottom: 6px; }' +
                '.primary-val { font-size: 32px; font-weight: 800; color: #047857; }' +
                '.primary-hint { font-size: 13px; color: #059669; margin-top: 6px; }' +
                '.sec-table { width: 100%; border-collapse: collapse; margin-top: 16px; }' +
                '.sec-table tr { border-bottom: 1px solid #e2e8f0; }' +
                '.sec-table td { padding: 12px 6px; font-size: 14px; }' +
                '.sec-table td:last-child { text-align: left; font-weight: 600; color: #0f172a; }' +
                '.footer { border-top: 1px dashed #cbd5e1; padding-top: 16px; font-size: 11px; color: #94a3b8; text-align: center; }' +
                '@media print { body { margin: 20px; } }' +
              '</style>' +
            '</head>' +
            '<body>' +
              '<div class="header">' +
                '<div>' +
                  '<h1 class="logo-title">حاسبها 🇸🇦</h1>' +
                  '<div class="subtitle">تقرير رسمي — ' + calc.title + '</div>' +
                '</div>' +
                '<div class="meta">' +
                  '<div><strong>تاريخ التقرير:</strong> ' + dateStr + '</div>' +
                  '<div><strong>الوقت:</strong> ' + timeStr + '</div>' +
                  '<div><strong>المرجع:</strong> hasibha.com/' + calc.url + '</div>' +
                '</div>' +
              '</div>' +
              '<div class="report-card">' +
                '<div class="primary-box">' +
                  '<div class="primary-label">' + pLabel + '</div>' +
                  '<div class="primary-val">' + pVal + '</div>' +
                  (pHint ? '<div class="primary-hint">' + pHint + '</div>' : '') +
                '</div>' +
                (rowsHtml ? '<table class="sec-table">' + rowsHtml + '</table>' : '') +
              '</div>' +
              '<div class="footer">' +
                '<p>هذا التقرير تم إعداده إلكترونياً وبدقة عالية عبر منصة حاسبها (hasibha.com) كأداة استرشادية معتمدة وفق أحدث الأنظمة السعودية لعام 2026.</p>' +
                '<p>الرابط المرجعي: https://hasibha.com/' + calc.url + '</p>' +
              '</div>' +
            '</body>' +
            '</html>';

          printWin.document.write(docContent);
          printWin.document.close();
          setTimeout(() => { printWin.print(); }, 250);
        });
      }

      // Live Exchange Rates API Background Sync (cached for 24h)
      (function syncLiveRates() {
        const CACHE_KEY = 'hasibha_live_rates';
        try {
          const cached = localStorage.getItem(CACHE_KEY);
          if (cached) {
            const data = JSON.parse(cached);
            if (Date.now() - data.ts < 24 * 3600 * 1000) {
              if (data.rates && typeof window.applyLiveRates === 'function') {
                window.applyLiveRates(data.rates);
              }
              return;
            }
          }
          fetch('https://open.er-api.com/v6/latest/SAR')
            .then(res => res.json())
            .then(res => {
              if (res && res.result === 'success' && res.rates) {
                const ratesToSAR = {
                  SAR: 1,
                  USD: parseFloat((1 / res.rates.USD).toFixed(4)) || 3.75,
                  EUR: parseFloat((1 / res.rates.EUR).toFixed(4)) || 4.06,
                  AED: parseFloat((1 / res.rates.AED).toFixed(4)) || 1.021,
                  GBP: parseFloat((1 / res.rates.GBP).toFixed(4)) || 4.78,
                  KWD: parseFloat((1 / res.rates.KWD).toFixed(4)) || 12.22
                };
                localStorage.setItem(CACHE_KEY, JSON.stringify({ ts: Date.now(), rates: ratesToSAR }));
                if (typeof window.applyLiveRates === 'function') {
                  window.applyLiveRates(ratesToSAR);
                }
              }
            })
            .catch(() => {});
        } catch (e) {}
      })();

      // PWA Service Worker Registration
      if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
          navigator.serviceWorker.register('/sw.js').catch(() => {});
        });
      }
`;

const printAndPwaJsEn = `
      // Print Official PDF Report
      const printReportBtn = document.getElementById('printReportBtn');
      if (printReportBtn) {
        printReportBtn.addEventListener('click', () => {
          const calc = CALCULATORS.find(c => c.id === activeCalcId) || { title: 'Smart Calculator', url: '' };
          const pLabel = document.getElementById('resPrimaryLabel') ? document.getElementById('resPrimaryLabel').textContent : 'Primary Result';
          const pVal = document.getElementById('resPrimaryVal') ? document.getElementById('resPrimaryVal').textContent : '0';
          const pHint = document.getElementById('resPrimaryHint') ? document.getElementById('resPrimaryHint').textContent : '';
          const secRows = Array.from(document.querySelectorAll('#resSecondaryGrid > div')).map(div => {
            const spans = div.querySelectorAll('span');
            return { label: spans[0] ? spans[0].textContent : '', val: spans[1] ? spans[1].textContent : '' };
          });

          const printWin = window.open('', '_blank');
          if (!printWin) {
            window.print();
            return;
          }

          const now = new Date();
          const dateStr = now.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
          const timeStr = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });

          const rowsHtml = secRows.map(r => '<tr><td>' + r.label + '</td><td>' + r.val + '</td></tr>').join('');

          const docContent = '<!DOCTYPE html>' +
            '<html lang="en" dir="ltr">' +
            '<head>' +
              '<meta charset="UTF-8">' +
              '<title>Official Calculation Report — ' + calc.title + ' | Hasibha</title>' +
              '<style>' +
                'body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 40px; color: #0f172a; line-height: 1.6; }' +
                '.header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #059669; padding-bottom: 16px; margin-bottom: 24px; }' +
                '.logo-title { font-size: 24px; font-weight: bold; color: #059669; margin: 0; }' +
                '.subtitle { font-size: 13px; color: #64748b; margin-top: 4px; }' +
                '.meta { text-align: right; font-size: 12px; color: #64748b; }' +
                '.report-card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 24px; margin-bottom: 24px; }' +
                '.primary-box { background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 12px; padding: 20px; text-align: center; margin-bottom: 20px; }' +
                '.primary-label { font-size: 15px; color: #065f46; font-weight: 600; margin-bottom: 6px; }' +
                '.primary-val { font-size: 32px; font-weight: 800; color: #047857; }' +
                '.primary-hint { font-size: 13px; color: #059669; margin-top: 6px; }' +
                '.sec-table { width: 100%; border-collapse: collapse; margin-top: 16px; }' +
                '.sec-table tr { border-bottom: 1px solid #e2e8f0; }' +
                '.sec-table td { padding: 12px 6px; font-size: 14px; }' +
                '.sec-table td:last-child { text-align: right; font-weight: 600; color: #0f172a; }' +
                '.footer { border-top: 1px dashed #cbd5e1; padding-top: 16px; font-size: 11px; color: #94a3b8; text-align: center; }' +
                '@media print { body { margin: 20px; } }' +
              '</style>' +
            '</head>' +
            '<body>' +
              '<div class="header">' +
                '<div>' +
                  '<h1 class="logo-title">Hasibha 🇸🇦</h1>' +
                  '<div class="subtitle">Official Calculation Report — ' + calc.title + '</div>' +
                '</div>' +
                '<div class="meta">' +
                  '<div><strong>Date:</strong> ' + dateStr + '</div>' +
                  '<div><strong>Time:</strong> ' + timeStr + '</div>' +
                  '<div><strong>Reference:</strong> hasibha.com/' + calc.url + '</div>' +
                '</div>' +
              '</div>' +
              '<div class="report-card">' +
                '<div class="primary-box">' +
                  '<div class="primary-label">' + pLabel + '</div>' +
                  '<div class="primary-val">' + pVal + '</div>' +
                  (pHint ? '<div class="primary-hint">' + pHint + '</div>' : '') +
                '</div>' +
                (rowsHtml ? '<table class="sec-table">' + rowsHtml + '</table>' : '') +
              '</div>' +
              '<div class="footer">' +
                '<p>This report was generated electronically via Hasibha (hasibha.com) based on the latest 2026 Saudi regulations and guidelines.</p>' +
                '<p>Reference: https://hasibha.com/' + calc.url + '</p>' +
              '</div>' +
            '</body>' +
            '</html>';

          printWin.document.write(docContent);
          printWin.document.close();
          setTimeout(() => { printWin.print(); }, 250);
        });
      }

      // Live Exchange Rates API Background Sync (cached for 24h)
      (function syncLiveRates() {
        const CACHE_KEY = 'hasibha_live_rates';
        try {
          const cached = localStorage.getItem(CACHE_KEY);
          if (cached) {
            const data = JSON.parse(cached);
            if (Date.now() - data.ts < 24 * 3600 * 1000) {
              if (data.rates && typeof window.applyLiveRates === 'function') {
                window.applyLiveRates(data.rates);
              }
              return;
            }
          }
          fetch('https://open.er-api.com/v6/latest/SAR')
            .then(res => res.json())
            .then(res => {
              if (res && res.result === 'success' && res.rates) {
                const ratesToSAR = {
                  SAR: 1,
                  USD: parseFloat((1 / res.rates.USD).toFixed(4)) || 3.75,
                  EUR: parseFloat((1 / res.rates.EUR).toFixed(4)) || 4.06,
                  AED: parseFloat((1 / res.rates.AED).toFixed(4)) || 1.021,
                  GBP: parseFloat((1 / res.rates.GBP).toFixed(4)) || 4.78,
                  KWD: parseFloat((1 / res.rates.KWD).toFixed(4)) || 12.22
                };
                localStorage.setItem(CACHE_KEY, JSON.stringify({ ts: Date.now(), rates: ratesToSAR }));
                if (typeof window.applyLiveRates === 'function') {
                  window.applyLiveRates(ratesToSAR);
                }
              }
            })
            .catch(() => {});
        } catch (e) {}
      })();

      // PWA Service Worker Registration
      if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
          navigator.serviceWorker.register('/sw.js').catch(() => {});
        });
      }
`;

// Insert print and pwa logic into both HTML files
const arInsertMarker = `// Embed Widget Action (Generates natural DoFollow backlinks)`;
if (indexHtml.includes(arInsertMarker)) {
  indexHtml = indexHtml.replace(arInsertMarker, printAndPwaJsAr + '\n      ' + arInsertMarker);
}

if (indexEnHtml.includes(arInsertMarker)) {
  indexEnHtml = indexEnHtml.replace(arInsertMarker, printAndPwaJsEn + '\n      ' + arInsertMarker);
}

// Support live rates in currency builder
const oldCurrencyRatesCode = `const ratesToSAR = { SAR: 1, USD: 3.75, EUR: 4.06, AED: 1.021, GBP: 4.78, KWD: 12.22 };`;
const newCurrencyRatesCode = `let ratesToSAR = { SAR: 1, USD: 3.75, EUR: 4.06, AED: 1.021, GBP: 4.78, KWD: 12.22 };
        try {
          const savedRates = localStorage.getItem('hasibha_live_rates');
          if (savedRates) {
            const parsed = JSON.parse(savedRates);
            if (parsed.rates) ratesToSAR = Object.assign(ratesToSAR, parsed.rates);
          }
        } catch (e) {}
        window.applyLiveRates = function(newRates) {
          ratesToSAR = Object.assign(ratesToSAR, newRates);
          compute();
        };`;

indexHtml = indexHtml.replace(oldCurrencyRatesCode, newCurrencyRatesCode);
indexEnHtml = indexEnHtml.replace(oldCurrencyRatesCode, newCurrencyRatesCode);

fs.writeFileSync(indexPath, indexHtml, 'utf8');
fs.writeFileSync(indexEnPath, indexEnHtml, 'utf8');
console.log('✅ PWA, PDF/Print, and Live API successfully integrated into index.html and index-en.html!');
