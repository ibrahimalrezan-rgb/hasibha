const fs = require('fs');
const path = require('path');

const rootDir = 'C:/Users/ibrah/.gemini/antigravity/scratch/hasibha';
const indexPath = path.join(rootDir, 'index.html');
const indexEnPath = path.join(rootDir, 'index-en.html');

let indexHtml = fs.readFileSync(indexPath, 'utf8');
let indexEnHtml = fs.readFileSync(indexEnPath, 'utf8');

// Replace duplicate disclaimer in index.html
const dupAr = `<div style="background:#fffbeb;border:1px solid #fef3c7;border-radius:10px;padding:12px 16px;margin:20px 0 10px;font-size:12px;color:#92400e;line-height:1.6;">' +
    '<strong>⚠️ تنبيه وإخلاء مسؤولية:</strong> هذا التقرير تقديري استرشادي <u>غير معتمد رسمياً</u>، ولا يُعتبر وثيقة قانونية أو مالية ملزمة. النتائج مبنية على الأنظمة واللوائح والتعليمات المعلنة من المصادر الرسمية المعتمدة في المملكة العربية السعودية لعام 2026 (مثل: نظام العمل السعودي، هيئة الزكاة والضريبة والجمارك ZATCA، البنك المركزي السعودي SAMA، والشركة السعودية للكهرباء).' +
  '</div>' +
  '<div style="background:#fffbeb;border:1px solid #fef3c7;border-radius:10px;padding:12px 16px;margin:20px 0 10px;font-size:12px;color:#92400e;line-height:1.6;text-align:right;">' +
    '<strong>⚠️ تنبيه وإخلاء مسؤولية:</strong> هذا التقرير تقديري استرشادي <u>غير معتمد رسمياً</u>، ولا يُعتبر وثيقة قانونية أو مالية ملزمة. النتائج مبنية على الأنظمة واللوائح والتعليمات المعلنة من المصادر الرسمية المعتمدة في المملكة العربية السعودية لعام 2026 (مثل: نظام العمل السعودي، هيئة الزكاة والضريبة والجمارك ZATCA، البنك المركزي السعودي SAMA، والشركة السعودية للكهرباء).' +
  '</div>'`;

const singleAr = `<div style="background:#fffbeb;border:1px solid #fef3c7;border-radius:10px;padding:12px 16px;margin:20px 0 10px;font-size:12px;color:#92400e;line-height:1.6;text-align:right;">' +
    '<strong>⚠️ تنبيه وإخلاء مسؤولية:</strong> هذا التقرير تقديري استرشادي <u>غير معتمد رسمياً</u>، ولا يُعتبر وثيقة قانونية أو مالية ملزمة. النتائج مبنية على الأنظمة واللوائح والتعليمات المعلنة من المصادر الرسمية المعتمدة في المملكة العربية السعودية لعام 2026 (مثل: نظام العمل السعودي، هيئة الزكاة والضريبة والجمارك ZATCA، البنك المركزي السعودي SAMA، والشركة السعودية للكهرباء).' +
  '</div>'`;

indexHtml = indexHtml.replace(dupAr, singleAr);

// In index-en.html
const dupEn = `<div style="background:#fffbeb;border:1px solid #fef3c7;border-radius:10px;padding:12px 16px;margin:20px 0 10px;font-size:12px;color:#92400e;line-height:1.6;">' +
    '<strong>⚠️ Disclaimer:</strong> This calculation report is an advisory estimate and is <u>not an officially accredited document</u>. The calculations are based on the latest 2026 regulations and instructions published by official regulatory sources in Saudi Arabia (such as Saudi Labor Law, ZATCA, SAMA, and SEC).' +
  '</div>' +
  '<div style="background:#fffbeb;border:1px solid #fef3c7;border-radius:10px;padding:12px 16px;margin:20px 0 10px;font-size:12px;color:#92400e;line-height:1.6;text-align:left;">' +
    '<strong>⚠️ Disclaimer:</strong> This calculation report is an advisory estimate and is <u>not an officially accredited document</u>. The calculations are based on the latest 2026 regulations and instructions published by official regulatory sources in Saudi Arabia (such as Saudi Labor Law, ZATCA, SAMA, and SEC).' +
  '</div>'`;

const singleEn = `<div style="background:#fffbeb;border:1px solid #fef3c7;border-radius:10px;padding:12px 16px;margin:20px 0 10px;font-size:12px;color:#92400e;line-height:1.6;text-align:left;">' +
    '<strong>⚠️ Disclaimer:</strong> This calculation report is an advisory estimate and is <u>not an officially accredited document</u>. The calculations are based on the latest 2026 regulations and instructions published by official regulatory sources in Saudi Arabia (such as Saudi Labor Law, ZATCA, SAMA, and SEC).' +
  '</div>'`;

indexEnHtml = indexEnHtml.replace(dupEn, singleEn);

fs.writeFileSync(indexPath, indexHtml, 'utf8');
fs.writeFileSync(indexEnPath, indexEnHtml, 'utf8');
console.log('✅ Cleaned duplicate disclaimer boxes');
