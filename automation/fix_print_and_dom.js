const fs = require('fs');
const path = require('path');

const rootDir = 'C:/Users/ibrah/.gemini/antigravity/scratch/hasibha';
const indexPath = path.join(rootDir, 'index.html');
const indexEnPath = path.join(rootDir, 'index-en.html');

let indexHtml = fs.readFileSync(indexPath, 'utf8');
let indexEnHtml = fs.readFileSync(indexEnPath, 'utf8');

const arPrintBtn = `<button id="printReportBtn" type="button" class="col-span-2 flex items-center justify-center gap-2 py-2.5 px-3 rounded-xl text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200 hover:text-emerald-600 dark:hover:text-emerald-400 bg-slate-100 hover:bg-emerald-50 dark:bg-slate-800 dark:hover:bg-slate-800/80 border border-slate-200/80 dark:border-slate-700 hover:border-emerald-500/30 transition-all shadow-xs">
              <i data-lucide="printer" class="w-4 h-4 text-emerald-600 dark:text-emerald-400"></i>
              <span>طباعة / حفظ تقرير رسمي (PDF)</span>
            </button>
            <button id="embedCalcBtn"`;

if (indexHtml.includes('<button id="embedCalcBtn"') && !indexHtml.includes('id="printReportBtn"')) {
  indexHtml = indexHtml.replace('<button id="embedCalcBtn"', arPrintBtn);
  fs.writeFileSync(indexPath, indexHtml, 'utf8');
  console.log('✅ Added printReportBtn to index.html');
}

const enPrintBtn = `<button id="printReportBtn" type="button" class="col-span-2 flex items-center justify-center gap-2 py-2.5 px-3 rounded-xl text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200 hover:text-emerald-600 dark:hover:text-emerald-400 bg-slate-100 hover:bg-emerald-50 dark:bg-slate-800 dark:hover:bg-slate-800/80 border border-slate-200/80 dark:border-slate-700 hover:border-emerald-500/30 transition-all shadow-xs">
              <i data-lucide="printer" class="w-4 h-4 text-emerald-600 dark:text-emerald-400"></i>
              <span>Print / Save Official Report (PDF)</span>
            </button>
            <button id="embedCalcBtn"`;

if (indexEnHtml.includes('<button id="embedCalcBtn"') && !indexEnHtml.includes('id="printReportBtn"')) {
  indexEnHtml = indexEnHtml.replace('<button id="embedCalcBtn"', enPrintBtn);
  fs.writeFileSync(indexEnPath, indexEnHtml, 'utf8');
  console.log('✅ Added printReportBtn to index-en.html');
}
