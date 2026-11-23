const fs = require('fs');
const path = require('path');

const rootDir = 'C:/Users/ibrah/.gemini/antigravity/scratch/hasibha';
const indexPath = path.join(rootDir, 'index.html');
const indexEnPath = path.join(rootDir, 'index-en.html');

let indexHtml = fs.readFileSync(indexPath, 'utf8');
let indexEnHtml = fs.readFileSync(indexEnPath, 'utf8');

// 1. In index.html Modal buttons
const arTargetModalBtns = `<button id="whatsappShareBtn" type="button" class="flex items-center justify-center gap-2 px-3.5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-emerald-600 hover:bg-emerald-700 text-white transition-colors">
              <i data-lucide="message-circle" class="w-4 h-4"></i>
              <span>مشاركة واتساب</span>
            </button>
          </div>`;

const arReplacementModalBtns = `<button id="whatsappShareBtn" type="button" class="flex items-center justify-center gap-2 px-3.5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-emerald-600 hover:bg-emerald-700 text-white transition-colors">
              <i data-lucide="message-circle" class="w-4 h-4"></i>
              <span>مشاركة واتساب</span>
            </button>
            <button id="embedCalcBtn" type="button" class="col-span-2 flex items-center justify-center gap-2 py-2 px-3 rounded-xl text-xs font-semibold text-slate-600 dark:text-slate-300 hover:text-emerald-600 dark:hover:text-emerald-400 bg-slate-100 hover:bg-emerald-50 dark:bg-slate-800 dark:hover:bg-slate-800/80 border border-slate-200/80 dark:border-slate-700 hover:border-emerald-500/30 transition-all">
              <i data-lucide="code-2" class="w-4 h-4 text-emerald-600 dark:text-emerald-400"></i>
              <span>تضمين الحاسبة في موقعك أو مدونتك (Embed Code)</span>
            </button>
          </div>`;

if (indexHtml.includes(arTargetModalBtns)) {
  indexHtml = indexHtml.replace(arTargetModalBtns, arReplacementModalBtns);
  console.log('✅ Arabic modal buttons updated');
} else {
  console.error('❌ Could not find Arabic modal buttons marker');
}

// 2. In index.html JS listeners
const arTargetJs = `document.getElementById('whatsappShareBtn').addEventListener('click', () => {
        const url = \`https://wa.me/?text=\${encodeURIComponent(latestShareText)}\`;
        window.open(url, '_blank', 'noopener,noreferrer');
      });`;

const arReplacementJs = `document.getElementById('whatsappShareBtn').addEventListener('click', () => {
        const url = \`https://wa.me/?text=\${encodeURIComponent(latestShareText)}\`;
        window.open(url, '_blank', 'noopener,noreferrer');
      });

      // Embed Widget Action (Generates natural DoFollow backlinks)
      const embedCalcBtn = document.getElementById('embedCalcBtn');
      if (embedCalcBtn) {
        embedCalcBtn.addEventListener('click', () => {
          const calc = CALCULATORS.find(c => c.id === activeCalcId) || { title: 'حاسبة ذكية', url: '' };
          const embedUrl = \`https://hasibha.com/\${calc.url}\`;
          const embedSnippet = \`<iframe src="\${embedUrl}" width="100%" height="650" frameborder="0" style="border:1px solid #e2e8f0;border-radius:16px;box-shadow:0 4px 6px -1px rgba(0,0,0,0.1);" title="\${calc.title}"></iframe>\\n<p style="font-size:12px;text-align:center;color:#64748b;margin-top:8px;">تم الحساب بواسطة <a href="\${embedUrl}" target="_blank" rel="noopener" style="color:#059669;font-weight:bold;text-decoration:none;">\${calc.title} — منصة حاسبها</a></p>\`;
          copyTextSafe(embedSnippet);
          showToast('تم نسخ كود التضمين لموقعك مع الرابط بنجاح! 🚀');
        });
      }`;

if (indexHtml.includes(arTargetJs)) {
  indexHtml = indexHtml.replace(arTargetJs, arReplacementJs);
  console.log('✅ Arabic JS event listener updated');
} else {
  console.error('❌ Could not find Arabic JS target marker');
}

fs.writeFileSync(indexPath, indexHtml, 'utf8');

// 3. In index-en.html Modal buttons
const enTargetModalBtns = `<button id="whatsappShareBtn" type="button" class="flex items-center justify-center gap-2 px-3.5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-emerald-600 hover:bg-emerald-700 text-white transition-colors">
              <i data-lucide="message-circle" class="w-4 h-4"></i>
              <span>WhatsApp</span>
            </button>
          </div>`;

const enReplacementModalBtns = `<button id="whatsappShareBtn" type="button" class="flex items-center justify-center gap-2 px-3.5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-emerald-600 hover:bg-emerald-700 text-white transition-colors">
              <i data-lucide="message-circle" class="w-4 h-4"></i>
              <span>WhatsApp</span>
            </button>
            <button id="embedCalcBtn" type="button" class="col-span-2 flex items-center justify-center gap-2 py-2 px-3 rounded-xl text-xs font-semibold text-slate-600 dark:text-slate-300 hover:text-emerald-600 dark:hover:text-emerald-400 bg-slate-100 hover:bg-emerald-50 dark:bg-slate-800 dark:hover:bg-slate-800/80 border border-slate-200/80 dark:border-slate-700 hover:border-emerald-500/30 transition-all">
              <i data-lucide="code-2" class="w-4 h-4 text-emerald-600 dark:text-emerald-400"></i>
              <span>Embed Calculator on Your Website / Blog</span>
            </button>
          </div>`;

if (indexEnHtml.includes(enTargetModalBtns)) {
  indexEnHtml = indexEnHtml.replace(enTargetModalBtns, enReplacementModalBtns);
  console.log('✅ English modal buttons updated');
} else {
  console.error('❌ Could not find English modal buttons marker');
}

// 4. In index-en.html JS listeners
const enTargetJs = `document.getElementById('whatsappShareBtn').addEventListener('click', () => {
        const url = \`https://wa.me/?text=\${encodeURIComponent(latestShareText)}\`;
        window.open(url, '_blank', 'noopener,noreferrer');
      });`;

const enReplacementJs = `document.getElementById('whatsappShareBtn').addEventListener('click', () => {
        const url = \`https://wa.me/?text=\${encodeURIComponent(latestShareText)}\`;
        window.open(url, '_blank', 'noopener,noreferrer');
      });

      // Embed Widget Action (Generates natural DoFollow backlinks)
      const embedCalcBtn = document.getElementById('embedCalcBtn');
      if (embedCalcBtn) {
        embedCalcBtn.addEventListener('click', () => {
          const calc = CALCULATORS.find(c => c.id === activeCalcId) || { title: 'Smart Calculator', url: '' };
          const embedUrl = \`https://hasibha.com/\${calc.url}\`;
          const embedSnippet = \`<iframe src="\${embedUrl}" width="100%" height="650" frameborder="0" style="border:1px solid #e2e8f0;border-radius:16px;box-shadow:0 4px 6px -1px rgba(0,0,0,0.1);" title="\${calc.title}"></iframe>\\n<p style="font-size:12px;text-align:center;color:#64748b;margin-top:8px;">Calculated by <a href="\${embedUrl}" target="_blank" rel="noopener" style="color:#059669;font-weight:bold;text-decoration:none;">\${calc.title} — Hasibha</a></p>\`;
          copyTextSafe(embedSnippet);
          showToast('Embed code copied to clipboard! 🚀');
        });
      }`;

if (indexEnHtml.includes(enTargetJs)) {
  indexEnHtml = indexEnHtml.replace(enTargetJs, enReplacementJs);
  console.log('✅ English JS event listener updated');
} else {
  console.error('❌ Could not find English JS target marker');
}

fs.writeFileSync(indexEnPath, indexEnHtml, 'utf8');
console.log('🚀 Both files successfully updated with Backlink Embed Widget!');
