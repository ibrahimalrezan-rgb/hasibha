const fs = require('fs');
const path = require('path');

const rootDir = 'C:/Users/ibrah/.gemini/antigravity/scratch/hasibha';
const indexPath = path.join(rootDir, 'index.html');
const indexEnPath = path.join(rootDir, 'index-en.html');

let indexHtml = fs.readFileSync(indexPath, 'utf8');
let indexEnHtml = fs.readFileSync(indexEnPath, 'utf8');

// =========================================================================
// 1. ARABIC: index.html
// =========================================================================

// Update badge to highlight offline capability
indexHtml = indexHtml.replace('معالجة محلية آمنة', 'يعمل دون إنترنت (Offline)');

// Replace embed button with offline banner in modal
const arOfflineBadgeHtml = `<div class="col-span-2 flex items-center justify-center gap-2 py-2 px-3 rounded-xl text-xs font-semibold text-emerald-800 dark:text-emerald-300 bg-emerald-50 dark:bg-emerald-500/10 border border-emerald-500/20">
              <i data-lucide="wifi-off" class="w-4 h-4 text-emerald-600 dark:text-emerald-400 shrink-0"></i>
              <span>يعمل بالكامل حتى مع انقطاع الإنترنت (Offline Mode) وبخصوصية 100%</span>
            </div>`;

indexHtml = indexHtml.replace(/<button id="embedCalcBtn"[\s\S]*?<\/button>/, arOfflineBadgeHtml);

// Remove embed JS listener
indexHtml = indexHtml.replace(/\/\/ Embed Widget Action[\s\S]*?showToast\('تم نسخ كود التضمين لموقعك مع الرابط بنجاح! 🚀'\);\s*\}\);\s*\}/, '');

// Update PDF Print template in Arabic
indexHtml = indexHtml.replace(
  '<span>طباعة / حفظ تقرير رسمي (PDF)</span>',
  '<span>طباعة / حفظ التقرير (PDF)</span>'
);

indexHtml = indexHtml.replace(
  /تقرير حساب معتمد/g,
  'تقرير حساب تقديري'
);

indexHtml = indexHtml.replace(
  /<div class="subtitle">تقرير رسمي —/g,
  '<div class="subtitle">تقرير تقديري استرشادي (غير معتمد) —'
);

indexHtml = indexHtml.replace(
  /'<div class="footer">'[\s\S]*?<\/div>'/g,
  `'<div style="background:#fffbeb;border:1px solid #fef3c7;border-radius:10px;padding:12px 16px;margin:20px 0 10px;font-size:12px;color:#92400e;line-height:1.6;text-align:right;">' +
    '<strong>⚠️ تنبيه وإخلاء مسؤولية:</strong> هذا التقرير تقديري استرشادي <u>غير معتمد رسمياً</u>، ولا يُعتبر وثيقة قانونية أو مالية ملزمة. النتائج مبنية على الأنظمة واللوائح والتعليمات المعلنة من المصادر الرسمية المعتمدة في المملكة العربية السعودية لعام 2026 (مثل: نظام العمل السعودي، هيئة الزكاة والضريبة والجمارك ZATCA، البنك المركزي السعودي SAMA، والشركة السعودية للكهرباء).' +
  '</div>' +
  '<div class="footer">' +
    '<p><strong>تنويه:</strong> هذا التقرير تم إعداده إلكترونياً عبر منصة حاسبها (hasibha.com) لأغراض التقدير والاسترشاد فقط وهو غير معتمد رسمياً. المعلومات واللوائح مستندة إلى المصادر التنظيمية الرسمية في المملكة العربية السعودية لعام 2026.</p>' +
    '<p>رابط الحاسبة المرجعي: https://hasibha.com/' + calc.url + '</p>' +
  '</div>'`
);

// =========================================================================
// 2. ENGLISH: index-en.html
// =========================================================================

// Update badge in English
indexEnHtml = indexEnHtml.replace('100% Local Processing', 'Works Offline (No Internet)');

// Replace embed button with offline banner in English modal
const enOfflineBadgeHtml = `<div class="col-span-2 flex items-center justify-center gap-2 py-2 px-3 rounded-xl text-xs font-semibold text-emerald-800 dark:text-emerald-300 bg-emerald-50 dark:bg-emerald-500/10 border border-emerald-500/20">
              <i data-lucide="wifi-off" class="w-4 h-4 text-emerald-600 dark:text-emerald-400 shrink-0"></i>
              <span>Works completely offline without internet connection & 100% private</span>
            </div>`;

indexEnHtml = indexEnHtml.replace(/<button id="embedCalcBtn"[\s\S]*?<\/button>/, enOfflineBadgeHtml);

// Remove embed JS listener in English
indexEnHtml = indexEnHtml.replace(/\/\/ Embed Widget Action[\s\S]*?showToast\('Embed code copied to clipboard! 🚀'\);\s*\}\);\s*\}/, '');

// Update PDF Print template in English
indexEnHtml = indexEnHtml.replace(
  '<span>Print / Save Official Report (PDF)</span>',
  '<span>Print / Save Report (PDF)</span>'
);

indexEnHtml = indexEnHtml.replace(
  /Official Calculation Report/g,
  'Calculation Estimate Report'
);

indexEnHtml = indexEnHtml.replace(
  /<div class="subtitle">Official Calculation Report —/g,
  '<div class="subtitle">Advisory Estimate Report (Unofficial) —'
);

indexEnHtml = indexEnHtml.replace(
  /'<div class="footer">'[\s\S]*?<\/div>'/g,
  `'<div style="background:#fffbeb;border:1px solid #fef3c7;border-radius:10px;padding:12px 16px;margin:20px 0 10px;font-size:12px;color:#92400e;line-height:1.6;text-align:left;">' +
    '<strong>⚠️ Disclaimer:</strong> This calculation report is an advisory estimate and is <u>not an officially accredited document</u>. The calculations are based on the latest 2026 regulations and instructions published by official regulatory sources in Saudi Arabia (such as Saudi Labor Law, ZATCA, SAMA, and SEC).' +
  '</div>' +
  '<div class="footer">' +
    '<p><strong>Notice:</strong> This report was generated electronically via Hasibha (hasibha.com) for advisory estimation purposes only and is unofficial. Regulations and data are based on official Saudi Arabian regulatory bodies.</p>' +
    '<p>Reference: https://hasibha.com/' + calc.url + '</p>' +
  '</div>'`
);

fs.writeFileSync(indexPath, indexHtml, 'utf8');
fs.writeFileSync(indexEnPath, indexEnHtml, 'utf8');
console.log('✅ Changes applied successfully with Regex replacement!');
