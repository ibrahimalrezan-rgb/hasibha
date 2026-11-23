const fs = require('fs');
const path = require('path');

const rootDir = 'C:/Users/ibrah/.gemini/antigravity/scratch/hasibha';
const indexPath = path.join(rootDir, 'index.html');
const indexEnPath = path.join(rootDir, 'index-en.html');

let indexHtml = fs.readFileSync(indexPath, 'utf8');
let indexEnHtml = fs.readFileSync(indexEnPath, 'utf8');

// 1. Update descriptions & counts in index.html
indexHtml = indexHtml.replace('20 حاسبة ذكية مجانية معتمدة', '24 حاسبة ذكية مجانية معتمدة');
indexHtml = indexHtml.replace('20 حاسبة ذكية معتمدة:', '24 حاسبة ذكية معتمدة:');
indexHtml = indexHtml.replace('20 حاسبة مالية وصحية وتجارية', '24 حاسبة مالية وصحية وتجارية');
indexHtml = indexHtml.replace('all: { label: \'الكل\', count: 20 },', 'all: { label: \'الكل\', count: 24 },');
indexHtml = indexHtml.replace(/financial:\s*\{\s*label:\s*'مالية',\s*count:\s*9,/g, "financial: {\n        label: 'مالية',\n        count: 12,");
indexHtml = indexHtml.replace(/general:\s*\{\s*label:\s*'عامة',\s*count:\s*3,/g, "general: {\n        label: 'عامة',\n        count: 4,");

// Add to CALCULATORS in index.html
const calcTargetAr = "{ id: 'gold', url: '/gold-value', title: 'حاسبة قيمة الذهب', desc: 'تقدير قيمة الذهب حسب الوزن والعيار (24، 22، 21، 18) بالريال السعودي.', category: 'financial', icon: 'gem', keywords: 'ذهب عيار 21 24 جرام سعر الذهب' },";

const calcAdditionAr = `{ id: 'gold', url: '/gold-value', title: 'حاسبة قيمة الذهب', desc: 'تقدير قيمة الذهب حسب الوزن والعيار (24، 22، 21، 18) بالريال السعودي.', category: 'financial', icon: 'gem', keywords: 'ذهب عيار 21 24 جرام سعر الذهب' },
      { id: 'electricity', url: '/electricity', title: 'حاسبة فاتورة الكهرباء', desc: 'احسب فاتورة الكهرباء وفق شرائح الاستهلاك (18 و 30 هللة) ورسوم العداد والضريبة.', category: 'financial', icon: 'zap', keywords: 'كهرباء فاتورة شرائح استهلاك عداد سداد الصيف kwh' },
      { id: 'sakani', url: '/sakani', title: 'حاسبة الدعم السكني', desc: 'تقدير دعم سكني الشهري، نسبة دعم الأرباح، وباقات الدعم غير المسترد (100k/150k).', category: 'financial', icon: 'home', keywords: 'دعم سكني باقة 100 الف مصفوفة الدعم صندوق التنمية العقارية قسط' },
      { id: 'leave_allowance', url: '/leave-allowance', title: 'بدل الإجازة السنوية', desc: 'حساب أجر الإجازة المقدم أو تعويض رصيد الإجازات المتبقية وفق نظام العمل.', category: 'financial', icon: 'calendar-check', keywords: 'بدل اجازة رصيد اجازات سنوية نظام العمل تعويض مادة 109 مادة 111' },`;

indexHtml = indexHtml.replace(calcTargetAr, calcAdditionAr);

const calcTargetGenAr = "{ id: 'date_diff', url: '/date-diff', title: 'الوقت بين تاريخين', desc: 'حساب عدد الأيام والأسابيع والأشهر الفاصلة بين أي تاريخين بدقة.', category: 'general', icon: 'clock', keywords: 'فرق وقت تاريخين ايام مدة عد تنازلي' }";
const calcAdditionGenAr = `{ id: 'date_diff', url: '/date-diff', title: 'الوقت بين تاريخين', desc: 'حساب عدد الأيام والأسابيع والأشهر الفاصلة بين أي تاريخين بدقة.', category: 'general', icon: 'clock', keywords: 'فرق وقت تاريخين ايام مدة عد تنازلي' },
      { id: 'gpa', url: '/gpa', title: 'حاسبة المعدل التراكمي', desc: 'حساب المعدل الفصلي والتراكمي للجامعات (نظام 5 و 4) ومسارات الثانوي والموزونة.', category: 'general', icon: 'graduation-cap', keywords: 'معدل تراكمي فصلي جامعة مسارات ثانوي موزونة درجات قدرات تحصيلي gpa' }`;

indexHtml = indexHtml.replace(calcTargetGenAr, calcAdditionGenAr);

// Builders for index.html
const buildersAdditionAr = `
      electricity(pane) {
        let tariff = 'residential';
        pane.innerHTML = \`
          <div>
            <label class="\${labelClass}">نوع النشاط والتعرفة</label>
            <div class="flex gap-2">
              <button type="button" data-val="residential" data-active="true" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-emerald-600 bg-emerald-600 text-white shadow-sm transition-all">سكني (18 / 30 هللة)</button>
              <button type="button" data-val="commercial" data-active="false" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all">تجاري (20 / 30 هللة)</button>
            </div>
          </div>
          <div>
            <div class="flex justify-between mb-1.5">
              <label for="elKwh" class="\${labelClass}">كمية الاستهلاك الشهري (ك.و.س - kWh)</label>
              <span id="elKwhVal" class="text-sm font-bold text-emerald-600 tabular-nums">4,500 ك.و.س</span>
            </div>
            <input id="elKwh" type="number" min="0" step="50" value="4500" class="\${inputClass}" />
          </div>
          <div>
            <label for="elBreaker" class="\${labelClass}">سعة قاطع العداد (خدمة العداد)</label>
            <select id="elBreaker" class="\${inputClass}">
              <option value="10">حتى 60 أمبير (10 ر.س)</option>
              <option value="15" selected>61 إلى 100 أمبير (15 ر.س — سكني شائع)</option>
              <option value="20">101 إلى 200 أمبير (20 ر.س)</option>
              <option value="30">أكثر من 300 أمبير (30 ر.س)</option>
            </select>
          </div>
        \`;
        const compute = () => {
          const kwh = Math.max(0, parseFloat(document.getElementById('elKwh').value) || 0);
          const meterFee = parseFloat(document.getElementById('elBreaker').value) || 15;
          document.getElementById('elKwhVal').textContent = \`\${fmtNum(kwh, 0)} ك.و.س\`;

          const rate1 = tariff === 'commercial' ? 0.20 : 0.18;
          const rate2 = 0.30;

          const t1Units = Math.min(kwh, 6000);
          const t2Units = Math.max(0, kwh - 6000);
          const t1Cost = t1Units * rate1;
          const t2Cost = t2Units * rate2;
          const consumption = t1Cost + t2Cost;
          const vat = (consumption + meterFee) * 0.15;
          const total = consumption + meterFee + vat;

          const t1Pct = total > 0 ? (t1Cost / total) * 100 : 0;
          const t2Pct = total > 0 ? (t2Cost / total) * 100 : 0;
          const vatPct = total > 0 ? (vat / total) * 100 : 0;

          updateResultPanel({
            primaryLabel: 'إجمالي الفاتورة شاملة الضريبة (15%)',
            primaryValue: fmtSAR(total),
            primaryHint: t2Units > 0 ? \`تجاوز الشريحة 1 بـ \${fmtNum(t2Units, 0)} ك.و.س (تعرفة 30 هللة)\` : 'كامل الاستهلاك ضمن الشريحة الأولى المدعومة',
            breakdown: [
              { label: 'استهلاك الشريحة 1 (1-6000 ك.و.س)', value: fmtSAR(t1Cost) },
              { label: 'استهلاك الشريحة 2 (>6000 ك.و.س)', value: fmtSAR(t2Cost) },
              { label: 'رسوم خدمة العداد الشهري', value: fmtSAR(meterFee) },
              { label: 'ضريبة القيمة المضافة (15%)', value: fmtSAR(vat) }
            ],
            bars: [
              { label: 'الشريحة 1', pct: t1Pct, color: 'bg-emerald-500' },
              { label: 'الشريحة 2', pct: t2Pct, color: 'bg-rose-500' },
              { label: 'الضريبة والعداد', pct: vatPct, color: 'bg-amber-500' }
            ],
            shareText: \`حاسبة فاتورة الكهرباء السعودية\\nالاستهلاك: \${fmtNum(kwh, 0)} ك.و.س\\nقيمة الاستهلاك: \${fmtSAR(consumption)}\\nخدمة العداد: \${fmtSAR(meterFee)}\\nالضريبة (15%): \${fmtSAR(vat)}\\nإجمالي الفاتورة: \${fmtSAR(total)}\\nعبر حاسبها — hasibha.com\`
          });
        };
        setupToggleGroup(pane, '.toggle-opt', (val) => { tariff = val; compute(); });
        bindInputs(pane, compute);
      },

      sakani(pane) {
        let scheme = 'matrix';
        pane.innerHTML = \`
          <div>
            <label class="\${labelClass}">خيار الدعم السكني</label>
            <div class="flex gap-2">
              <button type="button" data-val="matrix" data-active="true" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-emerald-600 bg-emerald-600 text-white shadow-sm transition-all">مصفوفة دعم الأرباح</button>
              <button type="button" data-val="package100" data-active="false" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all">باقة 100 ألف غير مستردة</button>
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="skSalary" class="\${labelClass}">الراتب الشهري (أساسي + سكن)</label>
              <input id="skSalary" type="number" min="3000" step="500" value="12000" class="\${inputClass}" />
            </div>
            <div>
              <label for="skFamily" class="\${labelClass}">أفراد الأسرة</label>
              <input id="skFamily" type="number" min="1" max="15" value="5" class="\${inputClass}" />
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="skLoan" class="\${labelClass}">مبلغ التمويل العقاري (ر.س)</label>
              <input id="skLoan" type="number" min="100000" step="10000" value="800000" class="\${inputClass}" />
            </div>
            <div>
              <label for="skYears" class="\${labelClass}">مدة التمويل (سنوات)</label>
              <select id="skYears" class="\${inputClass}">
                <option value="15">15 سنة</option>
                <option value="20" selected>20 سنة</option>
                <option value="25">25 سنة</option>
              </select>
            </div>
          </div>
        \`;
        const compute = () => {
          const salary = Math.max(0, parseFloat(document.getElementById('skSalary').value) || 0);
          const family = Math.max(1, parseInt(document.getElementById('skFamily').value, 10) || 1);
          const loan = Math.max(0, parseFloat(document.getElementById('skLoan').value) || 0);
          const years = parseInt(document.getElementById('skYears').value, 10) || 20;
          const months = years * 12;
          const r = (4.5 / 100) / 12;

          const pmt = (p, rate, n) => rate > 0 ? (p * rate * Math.pow(1 + rate, n)) / (Math.pow(1 + rate, n) - 1) : p / n;
          const grossPmt = pmt(loan, r, months);

          let subPct = 100;
          let netPmt = grossPmt;
          let monthlySub = 0;

          if (scheme === 'matrix') {
            if (salary <= 14000) subPct = 100;
            else if (salary <= 16000) subPct = 90;
            else if (salary <= 18000) subPct = 80;
            else if (salary <= 20000) subPct = 70;
            else subPct = 50;

            if (family > 5 && salary > 14000) subPct = Math.min(100, subPct + (family - 5) * 5);

            const subBase = Math.min(loan, 500000);
            const fullProfit = pmt(subBase, r, months) - (subBase / months);
            monthlySub = fullProfit * (subPct / 100);
            netPmt = Math.max(0, grossPmt - monthlySub);
          } else {
            const grant = 100000;
            const reducedLoan = Math.max(0, loan - grant);
            netPmt = pmt(reducedLoan, r, months);
            monthlySub = Math.max(0, grossPmt - netPmt);
            subPct = 100;
          }

          const netPct = grossPmt > 0 ? (netPmt / grossPmt) * 100 : 100;
          const subBarPct = grossPmt > 0 ? (monthlySub / grossPmt) * 100 : 0;

          updateResultPanel({
            primaryLabel: 'القسط الشهري الفعلي بعد الدعم',
            primaryValue: fmtSAR(netPmt),
            primaryHint: \`قيمة الدعم الشهري من سكني: \${fmtSAR(monthlySub)} (\${subPct}%)\`,
            breakdown: [
              { label: 'القسط الشهري قبل الدعم (للبنك)', value: fmtSAR(grossPmt) },
              { label: 'الدعم الشهري من سكني', value: fmtSAR(monthlySub) },
              { label: 'نسبة الدعم المستحقة', value: \`\${subPct}%\` },
              { label: 'إجمالي وفر الدعم التراكمي', value: fmtSAR(monthlySub * months) }
            ],
            bars: [
              { label: 'القسط الفعلي', pct: netPct, color: 'bg-emerald-500' },
              { label: 'دعم سكني', pct: subBarPct, color: 'bg-sky-500' }
            ],
            shareText: \`حاسبة الدعم السكني (برنامج سكني)\\nالقسط قبل الدعم: \${fmtSAR(grossPmt)}\\nدعم سكني الشهري: \${fmtSAR(monthlySub)} (\${subPct}%)\\nالقسط بعد الدعم: \${fmtSAR(netPmt)}\\nعبر حاسبها — hasibha.com\`
          });
        };
        setupToggleGroup(pane, '.toggle-opt', (val) => { scheme = val; compute(); });
        bindInputs(pane, compute);
      },

      leave_allowance(pane) {
        let purpose = 'advance';
        pane.innerHTML = \`
          <div>
            <label class="\${labelClass}">نوع الحساب</label>
            <div class="flex gap-2">
              <button type="button" data-val="advance" data-active="true" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-emerald-600 bg-emerald-600 text-white shadow-sm transition-all">بدل إجازة مقدم</button>
              <button type="button" data-val="unused" data-active="false" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all">تعويض رصيد الإجازات</button>
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="lvBasic" class="\${labelClass}">الراتب الأساسي (ر.س)</label>
              <input id="lvBasic" type="number" min="0" value="8000" class="\${inputClass}" />
            </div>
            <div>
              <label for="lvHousing" class="\${labelClass}">بدل السكن (ر.س)</label>
              <input id="lvHousing" type="number" min="0" value="2000" class="\${inputClass}" />
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="lvOther" class="\${labelClass}">بدلات ثابتة أخرى (نقل، إلخ)</label>
              <input id="lvOther" type="number" min="0" value="1000" class="\${inputClass}" />
            </div>
            <div>
              <label for="lvDays" class="\${labelClass}">عدد أيام الإجازة / الرصيد</label>
              <input id="lvDays" type="number" min="1" max="90" value="21" class="\${inputClass}" />
            </div>
          </div>
        \`;
        const compute = () => {
          const basic = Math.max(0, parseFloat(document.getElementById('lvBasic').value) || 0);
          const housing = Math.max(0, parseFloat(document.getElementById('lvHousing').value) || 0);
          const other = Math.max(0, parseFloat(document.getElementById('lvOther').value) || 0);
          const days = Math.max(0, parseFloat(document.getElementById('lvDays').value) || 0);

          const actualWage = basic + housing + other;
          const dailyWage = actualWage / 30;
          const totalAllowance = days * dailyWage;

          updateResultPanel({
            primaryLabel: purpose === 'advance' ? 'إجمالي بدل الإجازة المدفوع مقدماً' : 'التعويض المالي عن رصيد الإجازات',
            primaryValue: fmtSAR(totalAllowance),
            primaryHint: \`بناءً على أجر يومي قدره \${fmtSAR(dailyWage)} (\${days} يوماً)\`,
            breakdown: [
              { label: 'الأجر الفعلي الشهري الشامل', value: fmtSAR(actualWage) },
              { label: 'أجر اليوم الواحد (الأجر ÷ 30)', value: fmtSAR(dailyWage) },
              { label: 'عدد أيام الإجازة المحسوبة', value: \`\${days} يوماً\` }
            ],
            bars: [
              { label: 'الأساسي', pct: actualWage > 0 ? (basic / actualWage) * 100 : 0, color: 'bg-emerald-500' },
              { label: 'بدل السكن والبدلات', pct: actualWage > 0 ? ((housing + other) / actualWage) * 100 : 0, color: 'bg-sky-500' }
            ],
            shareText: \`حاسبة بدل الإجازة السنوية (نظام العمل السعودي)\\nالأجر الفعلي: \${fmtSAR(actualWage)}\\nأجر اليوم: \${fmtSAR(dailyWage)}\\nعدد الأيام: \${days}\\nإجمالي البدل: \${fmtSAR(totalAllowance)}\\nعبر حاسبها — hasibha.com\`
          });
        };
        setupToggleGroup(pane, '.toggle-opt', (val) => { purpose = val; compute(); });
        bindInputs(pane, compute);
      },

      gpa(pane) {
        let mode = '5';
        pane.innerHTML = \`
          <div>
            <label class="\${labelClass}">نظام التقييم</label>
            <div class="flex gap-2">
              <button type="button" data-val="5" data-active="true" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-emerald-600 bg-emerald-600 text-white shadow-sm transition-all">جامعي (من 5.0)</button>
              <button type="button" data-val="4" data-active="false" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all">جامعي (من 4.0)</button>
              <button type="button" data-val="tracks" data-active="false" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all">مسارات الثانوي</button>
            </div>
          </div>
          <div id="gpaUniInputs" class="space-y-3">
            <div class="grid grid-cols-2 gap-3">
              <div>
                <label for="gpaCourse1" class="\${labelClass}">مادة 1 (3 ساعات)</label>
                <select id="gpaCourse1" class="\${inputClass}">
                  <option value="5.0" selected>أ+ (5.00 / 4.00)</option>
                  <option value="4.75">أ (4.75 / 3.75)</option>
                  <option value="4.5">ب+ (4.50 / 3.50)</option>
                  <option value="4.0">ب (4.00 / 3.00)</option>
                  <option value="3.5">ج+ (3.50 / 2.50)</option>
                  <option value="3.0">ج (3.00 / 2.00)</option>
                  <option value="2.0">د (2.00 / 1.00)</option>
                </select>
              </div>
              <div>
                <label for="gpaCourse2" class="\${labelClass}">مادة 2 (3 ساعات)</label>
                <select id="gpaCourse2" class="\${inputClass}">
                  <option value="5.0">أ+ (5.00 / 4.00)</option>
                  <option value="4.75" selected>أ (4.75 / 3.75)</option>
                  <option value="4.5">ب+ (4.50 / 3.50)</option>
                  <option value="4.0">ب (4.00 / 3.00)</option>
                  <option value="3.5">ج+ (3.50 / 2.50)</option>
                  <option value="3.0">ج (3.00 / 2.00)</option>
                  <option value="2.0">د (2.00 / 1.00)</option>
                </select>
              </div>
            </div>
            <div class="grid grid-cols-2 gap-3">
              <div>
                <label for="gpaCourse3" class="\${labelClass}">مادة 3 (3 ساعات)</label>
                <select id="gpaCourse3" class="\${inputClass}">
                  <option value="5.0">أ+ (5.00 / 4.00)</option>
                  <option value="4.75">أ (4.75 / 3.75)</option>
                  <option value="4.5" selected>ب+ (4.50 / 3.50)</option>
                  <option value="4.0">ب (4.00 / 3.00)</option>
                  <option value="3.5">ج+ (3.50 / 2.50)</option>
                  <option value="3.0">ج (3.00 / 2.00)</option>
                  <option value="2.0">د (2.00 / 1.00)</option>
                </select>
              </div>
              <div>
                <label for="gpaCourse4" class="\${labelClass}">مادة 4 (3 ساعات)</label>
                <select id="gpaCourse4" class="\${inputClass}">
                  <option value="5.0">أ+ (5.00 / 4.00)</option>
                  <option value="4.75">أ (4.75 / 3.75)</option>
                  <option value="4.5">ب+ (4.50 / 3.50)</option>
                  <option value="4.0" selected>ب (4.00 / 3.00)</option>
                  <option value="3.5">ج+ (3.50 / 2.50)</option>
                  <option value="3.0">ج (3.00 / 2.00)</option>
                  <option value="2.0">د (2.00 / 1.00)</option>
                </select>
              </div>
            </div>
          </div>
          <div id="gpaTrackInputs" class="grid grid-cols-3 gap-2 hidden">
            <div>
              <label for="gpaY1" class="\${labelClass}">سنة 1 (20%)</label>
              <input id="gpaY1" type="number" min="0" max="100" value="95" class="\${inputClass}" />
            </div>
            <div>
              <label for="gpaY2" class="\${labelClass}">سنة 2 (40%)</label>
              <input id="gpaY2" type="number" min="0" max="100" value="97" class="\${inputClass}" />
            </div>
            <div>
              <label for="gpaY3" class="\${labelClass}">سنة 3 (40%)</label>
              <input id="gpaY3" type="number" min="0" max="100" value="98" class="\${inputClass}" />
            </div>
          </div>
        \`;
        const compute = () => {
          const uniDiv = document.getElementById('gpaUniInputs');
          const trackDiv = document.getElementById('gpaTrackInputs');

          if (mode === 'tracks') {
            uniDiv.classList.add('hidden');
            trackDiv.classList.remove('hidden');
            const y1 = parseFloat(document.getElementById('gpaY1').value) || 0;
            const y2 = parseFloat(document.getElementById('gpaY2').value) || 0;
            const y3 = parseFloat(document.getElementById('gpaY3').value) || 0;
            const cum = (y1 * 0.20) + (y2 * 0.40) + (y3 * 0.40);

            updateResultPanel({
              primaryLabel: 'المعدل التراكمي لمسارات الثانوي',
              primaryValue: \`\${fmtNum(cum, 2)}%\`,
              primaryHint: cum >= 90 ? 'ممتاز مرتفع 🎖️' : 'جيد جداً',
              breakdown: [
                { label: 'السنة الأولى (20%)', value: \`\${(y1 * 0.20).toFixed(2)}%\` },
                { label: 'السنة الثانية (40%)', value: \`\${(y2 * 0.40).toFixed(2)}%\` },
                { label: 'السنة الثالثة (40%)', value: \`\${(y3 * 0.40).toFixed(2)}%\` }
              ],
              bars: [
                { label: 'المعدل العام', pct: cum, color: 'bg-emerald-500' }
              ],
              shareText: \`حاسبة المعدل التراكمي (مسارات الثانوي)\\nالمعدل النهائي: \${fmtNum(cum, 2)}%\\nعبر حاسبها — hasibha.com\`
            });
          } else {
            uniDiv.classList.remove('hidden');
            trackDiv.classList.add('hidden');
            const g1 = parseFloat(document.getElementById('gpaCourse1').value) || 5.0;
            const g2 = parseFloat(document.getElementById('gpaCourse2').value) || 4.75;
            const g3 = parseFloat(document.getElementById('gpaCourse3').value) || 4.5;
            const g4 = parseFloat(document.getElementById('gpaCourse4').value) || 4.0;

            const scaleFactor = (mode === '4') ? (4.0 / 5.0) : 1.0;
            const gpa = ((g1 + g2 + g3 + g4) / 4) * scaleFactor;
            const max = mode === '4' ? 4.0 : 5.0;

            let standing = 'ممتاز (Excellent)';
            if (gpa < (mode === '4' ? 3.0 : 3.75)) standing = 'جيد جداً (Very Good)';

            updateResultPanel({
              primaryLabel: \`المعدل الفصلي (من \${max.toFixed(1)})\`,
              primaryValue: fmtNum(gpa, 2),
              primaryHint: standing,
              breakdown: [
                { label: 'إجمالي الساعات المسجلة', value: '12 ساعة معتمدة' },
                { label: 'التقدير الأكاديمي', value: standing },
                { label: 'مرتبة الشرف المتوقعة', value: gpa >= (mode === '4' ? 3.75 : 4.75) ? 'مرتبة الشرف الأولى 🥇' : (gpa >= (mode === '4' ? 3.25 : 4.25) ? 'مرتبة الشرف الثانية 🥈' : 'لا تنطبق') }
              ],
              bars: [
                { label: 'المعدل المحقق', pct: (gpa / max) * 100, color: 'bg-emerald-500' }
              ],
              shareText: \`حاسبة المعدل التراكمي الجامعي\\nالمعدل: \${fmtNum(gpa, 2)} من \${max.toFixed(1)}\\nالتقدير: \${standing}\\nعبر حاسبها — hasibha.com\`
            });
          }
        };
        setupToggleGroup(pane, '.toggle-opt', (val) => { mode = val; compute(); });
        bindInputs(pane, compute);
      },`;

const buildersEndMarker = `    };

    // 5. MODAL CONTROLLERS (CALCULATOR + ARTICLE)`;

indexHtml = indexHtml.replace(buildersEndMarker, buildersAdditionAr + '\n' + buildersEndMarker);

fs.writeFileSync(indexPath, indexHtml, 'utf8');
console.log('✅ index.html updated with 4 new calculators & builders!');
