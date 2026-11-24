const fs = require('fs');
const path = require('path');

const rootDir = 'C:/Users/ibrah/.gemini/antigravity/scratch/hasibha';
const indexPath = path.join(rootDir, 'index.html');
const indexEnPath = path.join(rootDir, 'index-en.html');

let indexHtml = fs.readFileSync(indexPath, 'utf8');
let indexEnHtml = fs.readFileSync(indexEnPath, 'utf8');

// =========================================================================
// 1. UPDATE META TAGS & OPEN GRAPH (Arabic & English)
// =========================================================================

// Arabic meta
indexHtml = indexHtml.replace(
  '24 حاسبة ذكية مجانية معتمدة في السعودية: حساب المواطن، الضمان المطور، التمويل العقاري، التأمينات والراتب، مكافأة نهاية الخدمة، الزكاة، الضريبة 15%، ومؤشر كتلة الجسم. نتائج فورية بدون تسجيل.',
  '29 حاسبة ذكية متخصصة لعام 2026: أرباح المتاجر الإلكترونية، تكلفة الاستيراد، مكافأة نهاية الخدمة، الضريبة 15%، التمويل العقاري، وحساب المواطن. تعمل بالكامل دون إنترنت وبخصوصية 100%.'
);

indexHtml = indexHtml.replace(
  '24 حاسبة ذكية معتمدة: حساب المواطن، الضمان المطور، التمويل، الراتب، نهاية الخدمة، الزكاة، والضريبة. دقة وخصوصية تامة.',
  '29 حاسبة ذكية لعام 2026: أرباح المتاجر، تكلفة الاستيراد، نهاية الخدمة، الضريبة، والتمويل. تعمل بدون إنترنت وبخصوصية تامة.'
);

// English meta
indexEnHtml = indexEnHtml.replace(
  '24 free smart calculators in Saudi Arabia: Citizen Account, Social Security, Real Estate Financing, GOSI & Salary, End of Service, Zakat, 15% VAT, and BMI. Instant results without registration.',
  '29 specialized smart calculators for 2026: E-commerce Net Profit, Landed Import Cost, End of Service, 15% VAT, Mortgage, and Salary. Works 100% offline with zero data collection.'
);

indexEnHtml = indexEnHtml.replace(
  '24 smart calculators: Citizen Account, Social Security, Mortgage, Salary, End of Service, Zakat, and VAT. Accurate and private.',
  '29 smart calculators for 2026: E-commerce, Import Cost, End of Service, VAT, and Mortgage. Offline ready & fully private.'
);

// =========================================================================
// 2. ADD RELATED CALCULATORS CONTAINER TO MODALS
// =========================================================================

const arModalRelatedHtml = `<!-- Related Calculators (Dwell Time Engine) -->
          <div class="pt-3 border-t border-slate-200/80 dark:border-slate-800">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-bold text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                <i data-lucide="sparkles" class="w-3.5 h-3.5 text-amber-500"></i>
                <span>حاسبات مقترحة قد تهمك أيضاً</span>
              </span>
            </div>
            <div id="modalRelatedCalcs" class="grid grid-cols-2 gap-2"></div>
          </div>
        </div>
      </div>
    </div>
  </div>`;

const enModalRelatedHtml = `<!-- Related Calculators (Dwell Time Engine) -->
          <div class="pt-3 border-t border-slate-200/80 dark:border-slate-800">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-bold text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                <i data-lucide="sparkles" class="w-3.5 h-3.5 text-amber-500"></i>
                <span>Related Calculators You Might Need</span>
              </span>
            </div>
            <div id="modalRelatedCalcs" class="grid grid-cols-2 gap-2"></div>
          </div>
        </div>
      </div>
    </div>
  </div>`;

const modalEndMarker = `        </div>\r\n      </div>\r\n    </div>\r\n  </div>`;
const modalEndMarkerLF = `        </div>\n      </div>\n    </div>\n  </div>`;

if (indexHtml.includes('<!-- Article Reader Modal -->')) {
  const modalEndIdx = indexHtml.indexOf('  <!-- ==================== ARTICLE READER MODAL');
  if (modalEndIdx !== -1) {
    const sliceBefore = indexHtml.substring(0, modalEndIdx);
    const lastClosingDiv = sliceBefore.lastIndexOf('        </div>');
    if (lastClosingDiv !== -1 && !indexHtml.includes('id="modalRelatedCalcs"')) {
      const targetBlock = indexHtml.substring(lastClosingDiv, modalEndIdx);
      indexHtml = indexHtml.substring(0, lastClosingDiv) + arModalRelatedHtml + '\n\n' + indexHtml.substring(modalEndIdx);
      console.log('✅ Added Related Calculators container to Arabic modal');
    }
  }
}

if (indexEnHtml.includes('<!-- Article Reader Modal -->')) {
  const modalEndIdx = indexEnHtml.indexOf('  <!-- ==================== ARTICLE READER MODAL');
  if (modalEndIdx !== -1) {
    const sliceBefore = indexEnHtml.substring(0, modalEndIdx);
    const lastClosingDiv = sliceBefore.lastIndexOf('        </div>');
    if (lastClosingDiv !== -1 && !indexEnHtml.includes('id="modalRelatedCalcs"')) {
      indexEnHtml = indexEnHtml.substring(0, lastClosingDiv) + enModalRelatedHtml + '\n\n' + indexEnHtml.substring(modalEndIdx);
      console.log('✅ Added Related Calculators container to English modal');
    }
  }
}

// =========================================================================
// 3. JAVASCRIPT: RELATED CALCULATORS & VIRAL WHATSAPP ENGINE
// =========================================================================

const arViralAndRelatedJs = `
    // Related Calculators Map (Contextual Dwell-Time Optimization)
    const RELATED_MAP = {
      ecommerce_profit: ['pricing', 'import_cost', 'shipping_weight'],
      import_cost: ['shipping_weight', 'ecommerce_profit', 'pricing'],
      pricing: ['ecommerce_profit', 'roi', 'discount'],
      roi: ['pricing', 'ecommerce_profit', 'mortgage'],
      shipping_weight: ['import_cost', 'ecommerce_profit', 'weight'],
      eosb: ['gosi', 'leave_allowance', 'citizen'],
      gosi: ['eosb', 'leave_allowance', 'citizen'],
      leave_allowance: ['eosb', 'gosi', 'date_diff'],
      vat: ['discount', 'ecommerce_profit', 'pricing'],
      mortgage: ['sakani', 'personal_loan', 'roi'],
      sakani: ['mortgage', 'personal_loan', 'citizen'],
      citizen: ['daman', 'gosi', 'sakani'],
      daman: ['citizen', 'gosi', 'sakani'],
      electricity: ['vat', 'gosi', 'discount'],
      gpa: ['age', 'date_diff', 'discount'],
      currency: ['vat', 'import_cost', 'gold'],
      zakat: ['gold', 'currency', 'roi'],
      gold: ['zakat', 'currency', 'weight'],
      bmi: ['calories', 'water', 'weight'],
      calories: ['bmi', 'water', 'weight'],
      water: ['calories', 'bmi', 'weight'],
      discount: ['vat', 'pricing', 'ecommerce_profit'],
      date_conv: ['age', 'date_diff', 'leave_allowance'],
      age: ['date_conv', 'date_diff', 'gpa'],
      date_diff: ['date_conv', 'age', 'leave_allowance']
    };

    function renderModalRelatedCalcs(currentId) {
      const container = document.getElementById('modalRelatedCalcs');
      if (!container) return;
      const relatedIds = RELATED_MAP[currentId] || ['vat', 'salary', 'eosb'];
      const calcs = relatedIds.map(id => CALCULATORS.find(c => c.id === id)).filter(Boolean).slice(0, 2);

      container.innerHTML = calcs.map(rel => {
        const cat = CATEGORIES[rel.category] || CATEGORIES.financial;
        return \`
          <button type="button" data-switch-calc="\${rel.id}" class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-800 hover:border-emerald-500/50 hover:bg-emerald-50/40 dark:hover:bg-slate-800 transition-all flex items-center gap-2.5 text-right group">
            <div class="w-8 h-8 rounded-lg \${cat.iconBox} flex items-center justify-center shrink-0 group-hover:scale-105 transition-transform">
              <i data-lucide="\${rel.icon}" class="w-4 h-4"></i>
            </div>
            <div class="min-w-0">
              <div class="text-xs font-bold text-slate-800 dark:text-slate-200 truncate group-hover:text-emerald-600 transition-colors">\${rel.title}</div>
              <div class="text-[10px] text-emerald-600 dark:text-emerald-400 font-medium flex items-center gap-1">
                <span>احسب الآن</span>
                <i data-lucide="arrow-left" class="w-3 h-3"></i>
              </div>
            </div>
          </button>
        \`;
      }).join('');

      container.querySelectorAll('[data-switch-calc]').forEach(btn => {
        btn.addEventListener('click', () => {
          openCalculator(btn.dataset.switchCalc);
        });
      });
      lucide.createIcons();
    }
`;

const enViralAndRelatedJs = `
    // Related Calculators Map (Contextual Dwell-Time Optimization)
    const RELATED_MAP = {
      ecommerce_profit: ['pricing', 'import_cost', 'shipping_weight'],
      import_cost: ['shipping_weight', 'ecommerce_profit', 'pricing'],
      pricing: ['ecommerce_profit', 'roi', 'discount'],
      roi: ['pricing', 'ecommerce_profit', 'mortgage'],
      shipping_weight: ['import_cost', 'ecommerce_profit', 'weight'],
      eosb: ['gosi', 'leave_allowance', 'citizen'],
      gosi: ['eosb', 'leave_allowance', 'citizen'],
      leave_allowance: ['eosb', 'gosi', 'date_diff'],
      vat: ['discount', 'ecommerce_profit', 'pricing'],
      mortgage: ['sakani', 'personal_loan', 'roi'],
      sakani: ['mortgage', 'personal_loan', 'citizen'],
      citizen: ['daman', 'gosi', 'sakani'],
      daman: ['citizen', 'gosi', 'sakani'],
      electricity: ['vat', 'gosi', 'discount'],
      gpa: ['age', 'date_diff', 'discount'],
      currency: ['vat', 'import_cost', 'gold'],
      zakat: ['gold', 'currency', 'roi'],
      gold: ['zakat', 'currency', 'weight'],
      bmi: ['calories', 'water', 'weight'],
      calories: ['bmi', 'water', 'weight'],
      water: ['calories', 'bmi', 'weight'],
      discount: ['vat', 'pricing', 'ecommerce_profit'],
      date_conv: ['age', 'date_diff', 'leave_allowance'],
      age: ['date_conv', 'date_diff', 'gpa'],
      date_diff: ['date_conv', 'age', 'leave_allowance']
    };

    function renderModalRelatedCalcs(currentId) {
      const container = document.getElementById('modalRelatedCalcs');
      if (!container) return;
      const relatedIds = RELATED_MAP[currentId] || ['vat', 'salary', 'eosb'];
      const calcs = relatedIds.map(id => CALCULATORS.find(c => c.id === id)).filter(Boolean).slice(0, 2);

      container.innerHTML = calcs.map(rel => {
        const cat = CATEGORIES[rel.category] || CATEGORIES.financial;
        return \`
          <button type="button" data-switch-calc="\${rel.id}" class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-800 hover:border-emerald-500/50 hover:bg-emerald-50/40 dark:hover:bg-slate-800 transition-all flex items-center gap-2.5 text-left group">
            <div class="w-8 h-8 rounded-lg \${cat.iconBox} flex items-center justify-center shrink-0 group-hover:scale-105 transition-transform">
              <i data-lucide="\${rel.icon}" class="w-4 h-4"></i>
            </div>
            <div class="min-w-0">
              <div class="text-xs font-bold text-slate-800 dark:text-slate-200 truncate group-hover:text-emerald-600 transition-colors">\${rel.title}</div>
              <div class="text-[10px] text-emerald-600 dark:text-emerald-400 font-medium flex items-center gap-1">
                <span>Calculate Now</span>
                <i data-lucide="arrow-right" class="w-3 h-3"></i>
              </div>
            </div>
          </button>
        \`;
      }).join('');

      container.querySelectorAll('[data-switch-calc]').forEach(btn => {
        btn.addEventListener('click', () => {
          openCalculator(btn.dataset.switchCalc);
        });
      });
      lucide.createIcons();
    }
`;

// Insert the JS functions and call renderModalRelatedCalcs in openCalculator
if (!indexHtml.includes('const RELATED_MAP =')) {
  indexHtml = indexHtml.replace('function openCalculator(id) {', arViralAndRelatedJs + '\n    function openCalculator(id) {');
  indexHtml = indexHtml.replace(
    'document.body.style.overflow = \'hidden\';',
    'document.body.style.overflow = \'hidden\';\n      renderModalRelatedCalcs(id);'
  );
  console.log('✅ Integrated Related Calculators JS into Arabic index.html');
}

if (!indexEnHtml.includes('const RELATED_MAP =')) {
  indexEnHtml = indexEnHtml.replace('function openCalculator(id) {', enViralAndRelatedJs + '\n    function openCalculator(id) {');
  indexEnHtml = indexEnHtml.replace(
    'document.body.style.overflow = \'hidden\';',
    'document.body.style.overflow = \'hidden\';\n      renderModalRelatedCalcs(id);'
  );
  console.log('✅ Integrated Related Calculators JS into English index-en.html');
}

// Upgrade updateResultPanel with viral formatting
const oldResultUpdateAr = `latestShareText = shareText || \`\${primaryLabel}: \${primaryValue}\\nعبر منصة حاسبها — hasibha.com\`;`;
const newResultUpdateAr = `const activeCalc = CALCULATORS.find(c => c.id === activeCalcId) || { title: 'حاسبة ذكية', url: '' };
      const viralLines = [
        \`📊 نتيجة حسابي عبر منصة حاسبها (hasibha.com):\`,
        \`🔹 \${primaryLabel}: \${primaryValue}\`
      ];
      if (breakdown && breakdown.length > 0) {
        breakdown.slice(0, 3).forEach(b => viralLines.push(\`▫️ \${b.label}: \${b.value}\`));
      }
      viralLines.push(\`\\n⚡ احسب نتيجتك فورياً ومجاناً: https://hasibha.com/\${activeCalc.url}\`);
      latestShareText = shareText || viralLines.join('\\n');`;

indexHtml = indexHtml.replace(oldResultUpdateAr, newResultUpdateAr);

const oldResultUpdateEn = `latestShareText = shareText || \`\${primaryLabel}: \${primaryValue}\\nvia Hasibha — hasibha.com\`;`;
const newResultUpdateEn = `const activeCalc = CALCULATORS.find(c => c.id === activeCalcId) || { title: 'Smart Calculator', url: '' };
      const viralLines = [
        \`📊 My calculation via Hasibha (hasibha.com):\`,
        \`🔹 \${primaryLabel}: \${primaryValue}\`
      ];
      if (breakdown && breakdown.length > 0) {
        breakdown.slice(0, 3).forEach(b => viralLines.push(\`▫️ \${b.label}: \${b.value}\`));
      }
      viralLines.push(\`\\n⚡ Calculate yours instantly & free: https://hasibha.com/\${activeCalc.url}\`);
      latestShareText = shareText || viralLines.join('\\n');`;

indexEnHtml = indexEnHtml.replace(oldResultUpdateEn, newResultUpdateEn);

fs.writeFileSync(indexPath, indexHtml, 'utf8');
fs.writeFileSync(indexEnPath, indexEnHtml, 'utf8');
console.log('🚀 Viral Loop & Dwell-Time engine successfully deployed into index.html and index-en.html!');
