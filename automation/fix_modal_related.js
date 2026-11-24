const fs = require('fs');
const path = require('path');

const rootDir = 'C:/Users/ibrah/.gemini/antigravity/scratch/hasibha';
const indexPath = path.join(rootDir, 'index.html');
const indexEnPath = path.join(rootDir, 'index-en.html');

let indexHtml = fs.readFileSync(indexPath, 'utf8');
let indexEnHtml = fs.readFileSync(indexEnPath, 'utf8');

const arOfflineBadge = `<span>يعمل بالكامل حتى مع انقطاع الإنترنت (Offline Mode) وبخصوصية 100%</span>
            </div>`;

const arRelatedHtml = `<span>يعمل بالكامل حتى مع انقطاع الإنترنت (Offline Mode) وبخصوصية 100%</span>
            </div>

            <!-- Related Calculators (Dwell Time Engine) -->
            <div class="col-span-2 pt-3 border-t border-slate-200/80 dark:border-slate-800">
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                  <i data-lucide="sparkles" class="w-3.5 h-3.5 text-amber-500"></i>
                  <span>حاسبات مقترحة قد تهمك أيضاً</span>
                </span>
              </div>
              <div id="modalRelatedCalcs" class="grid grid-cols-2 gap-2"></div>
            </div>`;

if (indexHtml.includes(arOfflineBadge) && !indexHtml.includes('id="modalRelatedCalcs"')) {
  indexHtml = indexHtml.replace(arOfflineBadge, arRelatedHtml);
  fs.writeFileSync(indexPath, indexHtml, 'utf8');
  console.log('✅ Added modalRelatedCalcs to Arabic index.html');
}

const enOfflineBadge = `<span>Works completely offline without internet connection & 100% private</span>
            </div>`;

const enRelatedHtml = `<span>Works completely offline without internet connection & 100% private</span>
            </div>

            <!-- Related Calculators (Dwell Time Engine) -->
            <div class="col-span-2 pt-3 border-t border-slate-200/80 dark:border-slate-800">
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                  <i data-lucide="sparkles" class="w-3.5 h-3.5 text-amber-500"></i>
                  <span>Related Calculators You Might Need</span>
                </span>
              </div>
              <div id="modalRelatedCalcs" class="grid grid-cols-2 gap-2"></div>
            </div>`;

if (indexEnHtml.includes(enOfflineBadge) && !indexEnHtml.includes('id="modalRelatedCalcs"')) {
  indexEnHtml = indexEnHtml.replace(enOfflineBadge, enRelatedHtml);
  fs.writeFileSync(indexEnPath, indexEnHtml, 'utf8');
  console.log('✅ Added modalRelatedCalcs to English index-en.html');
}
