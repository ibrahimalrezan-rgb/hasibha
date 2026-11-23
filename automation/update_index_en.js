const fs = require('fs');
const path = require('path');

const rootDir = 'C:/Users/ibrah/.gemini/antigravity/scratch/hasibha';
const indexEnPath = path.join(rootDir, 'index-en.html');

let html = fs.readFileSync(indexEnPath, 'utf8');

// 1. Meta / Counts
html = html.replace('20 smart, free, and accurate calculators', '24 smart, free, and accurate calculators');
html = html.replace('20 smart calculators certified for Saudi Arabia', '24 smart calculators certified for Saudi Arabia');
html = html.replace('featuring 20 financial, health, and commercial calculators', 'featuring 24 financial, health, and commercial calculators');
html = html.replace(/all:\s*\{\s*label:\s*'All',\s*count:\s*20\s*\}/g, "all: { label: 'All', count: 24 }");
html = html.replace(/financial:\s*\{\s*label:\s*'Financial',\s*count:\s*9,/g, "financial: {\n        label: 'Financial',\n        count: 12,");
html = html.replace(/general:\s*\{\s*label:\s*'General',\s*count:\s*3,/g, "general: {\n        label: 'General',\n        count: 4,");

// 2. Add to CALCULATORS
const targetFin = "{ id: 'gold', url: '/gold-value-en', title: 'Gold Value Calculator', desc: 'Estimate gold worth by weight and karat (24K, 22K, 21K, 18K) in SAR.', category: 'financial', icon: 'gem', keywords: 'gold price gram karat 21k 24k sar' },";
const additionFin = `{ id: 'gold', url: '/gold-value-en', title: 'Gold Value Calculator', desc: 'Estimate gold worth by weight and karat (24K, 22K, 21K, 18K) in SAR.', category: 'financial', icon: 'gem', keywords: 'gold price gram karat 21k 24k sar' },
      { id: 'electricity', url: '/electricity-en', title: 'Electricity Bill Calculator', desc: 'Calculate electricity bills per SEC consumption tiers (0.18 & 0.30 SAR) and 15% VAT.', category: 'financial', icon: 'zap', keywords: 'electricity bill sec tariff kwh meter fee consumption vat' },
      { id: 'sakani', url: '/sakani-en', title: 'Sakani Housing Support', desc: 'Estimate monthly Sakani profit subsidy, support rate, and 100k/150k upfront grants.', category: 'financial', icon: 'home', keywords: 'sakani housing support redf subsidy matrix grant installment' },
      { id: 'leave_allowance', url: '/leave-allowance-en', title: 'Leave Allowance Calculator', desc: 'Calculate advance annual leave pay or unused vacation encashment under Saudi Labor Law.', category: 'financial', icon: 'calendar-check', keywords: 'leave allowance vacation pay labor law article 109 encashment' },`;

html = html.replace(targetFin, additionFin);

const targetGen = "{ id: 'date_diff', url: '/date-diff-en', title: 'Time Between Dates', desc: 'Compute exact difference in days, weeks, and months between two dates.', category: 'general', icon: 'clock', keywords: 'date difference duration days weeks countdown' }";
const additionGen = `{ id: 'date_diff', url: '/date-diff-en', title: 'Time Between Dates', desc: 'Compute exact difference in days, weeks, and months between two dates.', category: 'general', icon: 'clock', keywords: 'date difference duration days weeks countdown' },
      { id: 'gpa', url: '/gpa-en', title: 'GPA & Weighted Score', desc: 'Calculate university GPA on 5.0 and 4.0 scales, high school tracks, and admissions.', category: 'general', icon: 'graduation-cap', keywords: 'gpa calculator 5 scale 4 scale tracks high school weighted admission' }`;

html = html.replace(targetGen, additionGen);

// 3. Add to CALC_BUILDERS
const buildersAdditionEn = `      electricity(pane) {
        let tariff = 'residential';
        pane.innerHTML = \`
          <div>
            <label class="\${labelClass}">Tariff Category</label>
            <div class="flex gap-2">
              <button type="button" data-val="residential" data-active="true" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-emerald-600 bg-emerald-600 text-white shadow-sm transition-all">Residential (0.18 / 0.30)</button>
              <button type="button" data-val="commercial" data-active="false" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all">Commercial (0.20 / 0.30)</button>
            </div>
          </div>
          <div>
            <div class="flex justify-between mb-1.5">
              <label for="elKwh" class="\${labelClass}">Monthly Consumption (kWh)</label>
              <span id="elKwhVal" class="text-sm font-bold text-emerald-600 tabular-nums">4,500 kWh</span>
            </div>
            <input id="elKwh" type="number" min="0" step="50" value="4500" class="\${inputClass}" />
          </div>
          <div>
            <label for="elBreaker" class="\${labelClass}">Circuit Breaker Capacity</label>
            <select id="elBreaker" class="\${inputClass}">
              <option value="10">Up to 60 Amps (10 SAR)</option>
              <option value="15" selected>61 to 100 Amps (15 SAR — Residential)</option>
              <option value="20">101 to 200 Amps (20 SAR)</option>
              <option value="30">Over 300 Amps (30 SAR)</option>
            </select>
          </div>
        \`;
        const compute = () => {
          const kwh = Math.max(0, parseFloat(document.getElementById('elKwh').value) || 0);
          const meterFee = parseFloat(document.getElementById('elBreaker').value) || 15;
          document.getElementById('elKwhVal').textContent = \`\${fmtNum(kwh, 0)} kWh\`;

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
            primaryLabel: 'Total Bill (Including 15% VAT)',
            primaryValue: fmtSAR(total),
            primaryHint: t2Units > 0 ? \`Tier 1 exceeded by \${fmtNum(t2Units, 0)} kWh (charged at 0.30 SAR)\` : 'All consumption within subsidized Tier 1',
            breakdown: [
              { label: 'Tier 1 Consumption (1-6000 kWh)', value: fmtSAR(t1Cost) },
              { label: 'Tier 2 Consumption (>6000 kWh)', value: fmtSAR(t2Cost) },
              { label: 'Meter Service Fee', value: fmtSAR(meterFee) },
              { label: '15% VAT', value: fmtSAR(vat) }
            ],
            bars: [
              { label: 'Tier 1', pct: t1Pct, color: 'bg-emerald-500' },
              { label: 'Tier 2', pct: t2Pct, color: 'bg-rose-500' },
              { label: 'Meter & VAT', pct: vatPct, color: 'bg-amber-500' }
            ],
            shareText: \`Saudi Electricity Bill\\nConsumption: \${fmtNum(kwh, 0)} kWh\\nPower Cost: \${fmtSAR(consumption)}\\nMeter Fee: \${fmtSAR(meterFee)}\\nVAT (15%): \${fmtSAR(vat)}\\nTotal Bill: \${fmtSAR(total)}\\nVia Hasibha — hasibha.com\`
          });
        };
        setupToggleGroup(pane, '.toggle-opt', (val) => { tariff = val; compute(); });
        bindInputs(pane, compute);
      },

      sakani(pane) {
        let scheme = 'matrix';
        pane.innerHTML = \`
          <div>
            <label class="\${labelClass}">Sakani Support Scheme</label>
            <div class="flex gap-2">
              <button type="button" data-val="matrix" data-active="true" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-emerald-600 bg-emerald-600 text-white shadow-sm transition-all">Profit Subsidy Matrix</button>
              <button type="button" data-val="package100" data-active="false" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all">100k Direct Grant</button>
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="skSalary" class="\${labelClass}">Monthly Salary (Basic + Housing)</label>
              <input id="skSalary" type="number" min="3000" step="500" value="12000" class="\${inputClass}" />
            </div>
            <div>
              <label for="skFamily" class="\${labelClass}">Family Members</label>
              <input id="skFamily" type="number" min="1" max="15" value="5" class="\${inputClass}" />
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="skLoan" class="\${labelClass}">Mortgage Loan Amount (SAR)</label>
              <input id="skLoan" type="number" min="100000" step="10000" value="800000" class="\${inputClass}" />
            </div>
            <div>
              <label for="skYears" class="\${labelClass}">Loan Period (Years)</label>
              <select id="skYears" class="\${inputClass}">
                <option value="15">15 Years</option>
                <option value="20" selected>20 Years</option>
                <option value="25">25 Years</option>
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
            primaryLabel: 'Monthly Payment After Sakani Support',
            primaryValue: fmtSAR(netPmt),
            primaryHint: \`Monthly Sakani Subsidy: \${fmtSAR(monthlySub)} (\${subPct}%)\`,
            breakdown: [
              { label: 'Bank Installment Before Subsidy', value: fmtSAR(grossPmt) },
              { label: 'Monthly Sakani Support', value: fmtSAR(monthlySub) },
              { label: 'Subsidy Rate', value: \`\${subPct}%\` },
              { label: 'Total Cumulative Subsidy', value: fmtSAR(monthlySub * months) }
            ],
            bars: [
              { label: 'Net Payment', pct: netPct, color: 'bg-emerald-500' },
              { label: 'Sakani Support', pct: subBarPct, color: 'bg-sky-500' }
            ],
            shareText: \`Sakani Housing Support\\nInstallment Before Support: \${fmtSAR(grossPmt)}\\nMonthly Subsidy: \${fmtSAR(monthlySub)} (\${subPct}%)\\nPayment After Support: \${fmtSAR(netPmt)}\\nVia Hasibha — hasibha.com\`
          });
        };
        setupToggleGroup(pane, '.toggle-opt', (val) => { scheme = val; compute(); });
        bindInputs(pane, compute);
      },

      leave_allowance(pane) {
        let purpose = 'advance';
        pane.innerHTML = \`
          <div>
            <label class="\${labelClass}">Calculation Purpose</label>
            <div class="flex gap-2">
              <button type="button" data-val="advance" data-active="true" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-emerald-600 bg-emerald-600 text-white shadow-sm transition-all">Advance Leave Pay</button>
              <button type="button" data-val="unused" data-active="false" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all">Unused Encashment</button>
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="lvBasic" class="\${labelClass}">Basic Salary (SAR)</label>
              <input id="lvBasic" type="number" min="0" value="8000" class="\${inputClass}" />
            </div>
            <div>
              <label for="lvHousing" class="\${labelClass}">Housing Allowance (SAR)</label>
              <input id="lvHousing" type="number" min="0" value="2000" class="\${inputClass}" />
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="lvOther" class="\${labelClass}">Other Allowances (Transport, etc.)</label>
              <input id="lvOther" type="number" min="0" value="1000" class="\${inputClass}" />
            </div>
            <div>
              <label for="lvDays" class="\${labelClass}">Leave Days / Balance</label>
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
            primaryLabel: purpose === 'advance' ? 'Advance Leave Pay' : 'Unused Leave Encashment',
            primaryValue: fmtSAR(totalAllowance),
            primaryHint: \`Daily rate: \${fmtSAR(dailyWage)} (\${days} days)\`,
            breakdown: [
              { label: 'Actual Monthly Wage', value: fmtSAR(actualWage) },
              { label: 'Daily Wage Rate (Wage ÷ 30)', value: fmtSAR(dailyWage) },
              { label: 'Calculated Leave Days', value: \`\${days} days\` }
            ],
            bars: [
              { label: 'Basic Salary', pct: actualWage > 0 ? (basic / actualWage) * 100 : 0, color: 'bg-emerald-500' },
              { label: 'Allowances', pct: actualWage > 0 ? ((housing + other) / actualWage) * 100 : 0, color: 'bg-sky-500' }
            ],
            shareText: \`Annual Leave Calculator (Saudi Labor Law)\\nActual Wage: \${fmtSAR(actualWage)}\\nDaily Rate: \${fmtSAR(dailyWage)}\\nDays: \${days}\\nTotal Allowance: \${fmtSAR(totalAllowance)}\\nVia Hasibha — hasibha.com\`
          });
        };
        setupToggleGroup(pane, '.toggle-opt', (val) => { purpose = val; compute(); });
        bindInputs(pane, compute);
      },

      gpa(pane) {
        let mode = '5';
        pane.innerHTML = \`
          <div>
            <label class="\${labelClass}">Grading Scale</label>
            <div class="flex gap-2">
              <button type="button" data-val="5" data-active="true" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-emerald-600 bg-emerald-600 text-white shadow-sm transition-all">5.0 Scale</button>
              <button type="button" data-val="4" data-active="false" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all">4.0 Scale</button>
              <button type="button" data-val="tracks" data-active="false" class="toggle-opt flex-1 py-2.5 px-3 rounded-xl text-sm font-semibold border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all">High School Tracks</button>
            </div>
          </div>
          <div id="gpaUniInputs" class="space-y-3">
            <div class="grid grid-cols-2 gap-3">
              <div>
                <label for="gpaCourse1" class="\${labelClass}">Course 1 (3 cr)</label>
                <select id="gpaCourse1" class="\${inputClass}">
                  <option value="5.0" selected>A+ (5.00 / 4.00)</option>
                  <option value="4.75">A (4.75 / 3.75)</option>
                  <option value="4.5">B+ (4.50 / 3.50)</option>
                  <option value="4.0">B (4.00 / 3.00)</option>
                  <option value="3.5">C+ (3.50 / 2.50)</option>
                  <option value="3.0">C (3.00 / 2.00)</option>
                  <option value="2.0">D (2.00 / 1.00)</option>
                </select>
              </div>
              <div>
                <label for="gpaCourse2" class="\${labelClass}">Course 2 (3 cr)</label>
                <select id="gpaCourse2" class="\${inputClass}">
                  <option value="5.0">A+ (5.00 / 4.00)</option>
                  <option value="4.75" selected>A (4.75 / 3.75)</option>
                  <option value="4.5">B+ (4.50 / 3.50)</option>
                  <option value="4.0">B (4.00 / 3.00)</option>
                  <option value="3.5">C+ (3.50 / 2.50)</option>
                  <option value="3.0">C (3.00 / 2.00)</option>
                  <option value="2.0">D (2.00 / 1.00)</option>
                </select>
              </div>
            </div>
            <div class="grid grid-cols-2 gap-3">
              <div>
                <label for="gpaCourse3" class="\${labelClass}">Course 3 (3 cr)</label>
                <select id="gpaCourse3" class="\${inputClass}">
                  <option value="5.0">A+ (5.00 / 4.00)</option>
                  <option value="4.75">A (4.75 / 3.75)</option>
                  <option value="4.5" selected>B+ (4.50 / 3.50)</option>
                  <option value="4.0">B (4.00 / 3.00)</option>
                  <option value="3.5">C+ (3.50 / 2.50)</option>
                  <option value="3.0">C (3.00 / 2.00)</option>
                  <option value="2.0">D (2.00 / 1.00)</option>
                </select>
              </div>
              <div>
                <label for="gpaCourse4" class="\${labelClass}">Course 4 (3 cr)</label>
                <select id="gpaCourse4" class="\${inputClass}">
                  <option value="5.0">A+ (5.00 / 4.00)</option>
                  <option value="4.75">A (4.75 / 3.75)</option>
                  <option value="4.5">B+ (4.50 / 3.50)</option>
                  <option value="4.0" selected>B (4.00 / 3.00)</option>
                  <option value="3.5">C+ (3.50 / 2.50)</option>
                  <option value="3.0">C (3.00 / 2.00)</option>
                  <option value="2.0">D (2.00 / 1.00)</option>
                </select>
              </div>
            </div>
          </div>
          <div id="gpaTrackInputs" class="grid grid-cols-3 gap-2 hidden">
            <div>
              <label for="gpaY1" class="\${labelClass}">Year 1 (20%)</label>
              <input id="gpaY1" type="number" min="0" max="100" value="95" class="\${inputClass}" />
            </div>
            <div>
              <label for="gpaY2" class="\${labelClass}">Year 2 (40%)</label>
              <input id="gpaY2" type="number" min="0" max="100" value="97" class="\${inputClass}" />
            </div>
            <div>
              <label for="gpaY3" class="\${labelClass}">Year 3 (40%)</label>
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
              primaryLabel: 'High School Tracks Cumulative GPA',
              primaryValue: \`\${fmtNum(cum, 2)}%\`,
              primaryHint: cum >= 90 ? 'High Distinction 🎖️' : 'Very Good',
              breakdown: [
                { label: 'Year 1 (20%)', value: \`\${(y1 * 0.20).toFixed(2)}%\` },
                { label: 'Year 2 (40%)', value: \`\${(y2 * 0.40).toFixed(2)}%\` },
                { label: 'Year 3 (40%)', value: \`\${(y3 * 0.40).toFixed(2)}%\` }
              ],
              bars: [
                { label: 'Cumulative Average', pct: cum, color: 'bg-emerald-500' }
              ],
              shareText: \`High School Tracks GPA\\nFinal Score: \${fmtNum(cum, 2)}%\\nVia Hasibha — hasibha.com\`
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

            let standing = 'Excellent';
            if (gpa < (mode === '4' ? 3.0 : 3.75)) standing = 'Very Good';

            updateResultPanel({
              primaryLabel: \`Semester GPA (out of \${max.toFixed(1)})\`,
              primaryValue: fmtNum(gpa, 2),
              primaryHint: standing,
              breakdown: [
                { label: 'Total Enrolled Hours', value: '12 Credit Hours' },
                { label: 'Academic Rating', value: standing },
                { label: 'Expected Honor', value: gpa >= (mode === '4' ? 3.75 : 4.75) ? 'First Class Honors 🥇' : (gpa >= (mode === '4' ? 3.25 : 4.25) ? 'Second Class Honors 🥈' : 'None') }
              ],
              bars: [
                { label: 'Earned GPA', pct: (gpa / max) * 100, color: 'bg-emerald-500' }
              ],
              shareText: \`University GPA\\nScore: \${fmtNum(gpa, 2)} / \${max.toFixed(1)}\\nStanding: \${standing}\\nVia Hasibha — hasibha.com\`
            });
          }
        };
        setupToggleGroup(pane, '.toggle-opt', (val) => { mode = val; compute(); });
        bindInputs(pane, compute);
      }`;

const targetEndMarker = `    };

    function openCalculator(id) {`;

// Replace `date_diff(pane) {\n ... \n      }` with comma and addition
html = html.replace(`        bindInputs(pane, compute);
      }
    };`, `        bindInputs(pane, compute);
      },

${buildersAdditionEn}
    };`);

fs.writeFileSync(indexEnPath, html, 'utf8');
console.log('✅ index-en.html updated with 4 new calculators & builders!');
