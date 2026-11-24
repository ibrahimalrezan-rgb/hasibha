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

// 1.1 Category update
const catRegexAr = /const CATEGORIES = \{[\r\n\s]*all:\s*\{[^}]*\},/;
const newCatAr = `const CATEGORIES = {
      all: { label: 'الكل', count: 29 },
      business: {
        label: 'تجارة وأعمال',
        count: 5,
        iconBox: 'bg-indigo-50 text-indigo-700 dark:bg-indigo-500/10 dark:text-indigo-400',
        badge: 'bg-indigo-50 text-indigo-700 dark:bg-indigo-500/10 dark:text-indigo-400'
      },`;

indexHtml = indexHtml.replace(catRegexAr, newCatAr);

// 1.2 Calculators array update
const calcRegexAr = /\{\s*id:\s*'gpa'[\s\S]*?\}\s*\];/;
const newCalcsAr = `{ id: 'gpa', url: '/gpa', title: 'حاسبة المعدل التراكمي', desc: 'حساب المعدل الفصلي والتراكمي للجامعات (نظام 5 و 4) ومسارات الثانوي والموزونة.', category: 'general', icon: 'graduation-cap', keywords: 'معدل تراكمي فصلي جامعة مسارات ثانوي موزونة درجات قدرات تحصيلي gpa' },

      // Business & E-commerce (5)
      { id: 'ecommerce_profit', url: '/ecommerce-profit', title: 'صافي ربح المتجر الإلكتروني', desc: 'حساب صافي الأرباح وهوامش الربح وخصم عمولات مدى وفيزا وتابي وتكاليف الإعلانات.', category: 'business', icon: 'shopping-cart', keywords: 'متجر الكتروني سلة زد امازون نون عمولة مدى تابي تمارا صافي الربح roas cac دروب شيبينغ تجارة' },
      { id: 'import_cost', url: '/import-cost', title: 'تكلفة الاستيراد الشاملة', desc: 'حساب التكلفة الحقيقية للقطعة الواصلة للمستودع شاملاً الجمارك، الشحن الدولي، والضريبة.', category: 'business', icon: 'package-check', keywords: 'استيراد تكلفة القطعة landed cost جمارك زاتكا سابر فسح شحن بحري جوي ضريبة بضائع' },
      { id: 'pricing', url: '/pricing-calculator', title: 'تسعير المنتجات ونقطة التعادل', desc: 'تحديد سعر البيع الأنسب للمنتج بناءً على هامش الربح المطلوب وتحليل نقطة التعادل.', category: 'business', icon: 'target', keywords: 'تسعير هامش الربح markup margin نقطة التعادل break even تكاليف ثابتة مبيعات تسعير' },
      { id: 'roi', url: '/roi', title: 'العائد على الاستثمار (ROI)', desc: 'دراسة جدوى سريعة: احتساب نسبة العائد السنوي والمدة الزمنية لاسترداد رأس المال المستثمر.', category: 'business', icon: 'trending-up', keywords: 'عائد على الاستثمار roi payback period فترة الاسترداد جدوى مشروع ارباح استثمار تمويل' },
      { id: 'shipping_weight', url: '/shipping-weight', title: 'الوزن الحجمي وتكلفة الشحن', desc: 'مقارنة الوزن الفعلي بالوزن الحجمي وفق معادلة IATA الدولية لتفادي فروقات أسعار الشحن.', category: 'business', icon: 'plane', keywords: 'وزن حجمي شحن دولي iata ابعاد الكرتون تكلفة الكيلو ارامكس dhl سمسا طرود' }
    ];`;

indexHtml = indexHtml.replace(calcRegexAr, newCalcsAr);

// 1.3 Builders update
const buildersRegexAr = /gpa\(pane\)\s*\{/;
const newBuildersAr = `ecommerce_profit(pane) {
        pane.innerHTML = \`
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="ecSalePrice" class="\${labelClass}">سعر بيع المنتج للعميل (ر.س)</label>
              <input id="ecSalePrice" type="number" min="0" value="199" class="\${inputClass}" />
            </div>
            <div>
              <label for="ecCostPrice" class="\${labelClass}">تكلفة شراء / تصنيع القطعة (ر.س)</label>
              <input id="ecCostPrice" type="number" min="0" value="70" class="\${inputClass}" />
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="ecShipping" class="\${labelClass}">تكلفة الشحن والتوصيل (ر.س)</label>
              <input id="ecShipping" type="number" min="0" value="25" class="\${inputClass}" />
            </div>
            <div>
              <label for="ecAdCost" class="\${labelClass}">تكلفة الإعلانات لكل طلب - CAC (ر.س)</label>
              <input id="ecAdCost" type="number" min="0" value="35" class="\${inputClass}" />
            </div>
          </div>
          <div>
            <label for="ecGateway" class="\${labelClass}">بوابة الدفع الإلكتروني</label>
            <select id="ecGateway" class="\${inputClass}">
              <option value="mada" selected>مدى (1.0% + 1 ر.س)</option>
              <option value="visa">فيزا / ماستركارد (2.2% + 1 ر.س)</option>
              <option value="tabby">تابي / تمارا (7.0% + 1.5 ر.س)</option>
              <option value="cod">الدفع عند الاستلام (0% عمولة)</option>
            </select>
          </div>
        \`;
        const compute = () => {
          const sale = Math.max(0, parseFloat(document.getElementById('ecSalePrice').value) || 0);
          const cost = Math.max(0, parseFloat(document.getElementById('ecCostPrice').value) || 0);
          const ship = Math.max(0, parseFloat(document.getElementById('ecShipping').value) || 0);
          const ad = Math.max(0, parseFloat(document.getElementById('ecAdCost').value) || 0);
          const gw = document.getElementById('ecGateway').value;

          let gwFee = 0;
          if (gw === 'mada') gwFee = (sale * 0.01) + 1.0;
          else if (gw === 'visa') gwFee = (sale * 0.022) + 1.0;
          else if (gw === 'tabby') gwFee = (sale * 0.07) + 1.5;

          const totalExpenses = cost + ship + ad + gwFee;
          const netProfit = sale - totalExpenses;
          const margin = sale > 0 ? (netProfit / sale) * 100 : 0;
          const roas = ad > 0 ? (sale / ad) : 0;

          updateResultPanel({
            primaryLabel: 'صافي الربح الفعلي للطلب الواحد',
            primaryValue: fmtSAR(netProfit),
            primaryHint: netProfit >= 0 ? 'مشروعك يحقق ربحاً إيجابياً مميزاً' : 'تنبيه: التكاليف تتجاوز سعر البيع (خسارة)',
            breakdown: [
              { label: 'سعر البيع للعميل', value: fmtSAR(sale) },
              { label: 'إجمالي التكاليف والمصاريف', value: fmtSAR(totalExpenses) },
              { label: 'هامش الربح الصافي (Net Margin)', value: \`\${margin.toFixed(1)}%\` },
              { label: 'عمولة بوابة الدفع', value: fmtSAR(gwFee) },
              { label: 'العائد على الإنفاق الإعلاني (ROAS)', value: \`\${roas.toFixed(2)}x\` }
            ]
          });
        };
        pane.querySelectorAll('input, select').forEach(el => el.addEventListener('input', compute));
        compute();
      },

      import_cost(pane) {
        pane.innerHTML = \`
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="impPrice" class="\${labelClass}">سعر الشراء للقطعة بالدولار ($)</label>
              <input id="impPrice" type="number" min="0" step="any" value="10" class="\${inputClass}" />
            </div>
            <div>
              <label for="impQty" class="\${labelClass}">كمية الشحنة (عدد القطع)</label>
              <input id="impQty" type="number" min="1" value="500" class="\${inputClass}" />
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="impShipUSD" class="\${labelClass}">تكلفة الشحن الدولي الإجمالية ($)</label>
              <input id="impShipUSD" type="number" min="0" value="800" class="\${inputClass}" />
            </div>
            <div>
              <label for="impCustomsRate" class="\${labelClass}">نسبة الرسوم الجمركية (%)</label>
              <input id="impCustomsRate" type="number" min="0" max="100" value="5" class="\${inputClass}" />
            </div>
          </div>
          <div>
            <label for="impClearanceSAR" class="\${labelClass}">رسوم التخليص والنقل الداخلي وسابر (ر.س)</label>
            <input id="impClearanceSAR" type="number" min="0" value="1200" class="\${inputClass}" />
          </div>
        \`;
        const compute = () => {
          const priceUSD = Math.max(0, parseFloat(document.getElementById('impPrice').value) || 0);
          const qty = Math.max(1, parseInt(document.getElementById('impQty').value) || 1);
          const shipUSD = Math.max(0, parseFloat(document.getElementById('impShipUSD').value) || 0);
          const customsPct = Math.max(0, parseFloat(document.getElementById('impCustomsRate').value) || 0) / 100;
          const clearanceSAR = Math.max(0, parseFloat(document.getElementById('impClearanceSAR').value) || 0);

          const USD_TO_SAR = 3.75;
          const goodsCostSAR = priceUSD * qty * USD_TO_SAR;
          const shipCostSAR = shipUSD * USD_TO_SAR;
          const cifSAR = goodsCostSAR + shipCostSAR;
          const customsDutySAR = cifSAR * customsPct;
          const vatSAR = (cifSAR + customsDutySAR) * 0.15;

          const totalImportCostSAR = goodsCostSAR + shipCostSAR + customsDutySAR + vatSAR + clearanceSAR;
          const costPerUnitSAR = totalImportCostSAR / qty;

          updateResultPanel({
            primaryLabel: 'التكلفة الشاملة للقطعة الواصلة (Landed Cost)',
            primaryValue: fmtSAR(costPerUnitSAR),
            primaryHint: \`إجمالي تكلفة الشحنة بالكامل: \${fmtSAR(totalImportCostSAR)}\`,
            breakdown: [
              { label: 'قيمة البضاعة في المصنع (ر.س)', value: fmtSAR(goodsCostSAR) },
              { label: 'تكلفة الشحن الدولي (ر.س)', value: fmtSAR(shipCostSAR) },
              { label: 'الرسوم الجمركية التقديرية', value: fmtSAR(customsDutySAR) },
              { label: 'ضريبة القيمة المضافة 15%', value: fmtSAR(vatSAR) },
              { label: 'التخليص والنقل ومنصة سابر', value: fmtSAR(clearanceSAR) }
            ]
          });
        };
        pane.querySelectorAll('input').forEach(el => el.addEventListener('input', compute));
        compute();
      },

      pricing(pane) {
        pane.innerHTML = \`
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="prCost" class="\${labelClass}">التكلفة الإجمالية للقطعة الواحدة (ر.س)</label>
              <input id="prCost" type="number" min="0" value="50" class="\${inputClass}" />
            </div>
            <div>
              <label for="prMargin" class="\${labelClass}">هامش الربح الصافي المستهدف (%)</label>
              <input id="prMargin" type="number" min="1" max="95" value="35" class="\${inputClass}" />
            </div>
          </div>
          <div>
            <label for="prFixedCosts" class="\${labelClass}">المصاريف الشهرية الثابتة (إيجار، رواتب، اشتراكات) (ر.س)</label>
            <input id="prFixedCosts" type="number" min="0" value="5000" class="\${inputClass}" />
          </div>
        \`;
        const compute = () => {
          const cost = Math.max(0, parseFloat(document.getElementById('prCost').value) || 0);
          const margin = Math.min(95, Math.max(1, parseFloat(document.getElementById('prMargin').value) || 35)) / 100;
          const fixedCosts = Math.max(0, parseFloat(document.getElementById('prFixedCosts').value) || 0);

          const priceBeforeVat = cost / (1 - margin);
          const profitPerUnit = priceBeforeVat - cost;
          const finalPriceWithVat = priceBeforeVat * 1.15;
          const markupPct = cost > 0 ? (profitPerUnit / cost) * 100 : 0;
          const breakEvenUnits = profitPerUnit > 0 ? Math.ceil(fixedCosts / profitPerUnit) : 0;

          updateResultPanel({
            primaryLabel: 'السعر النهائي المقترح للمستهلك (شامل 15%)',
            primaryValue: fmtSAR(finalPriceWithVat),
            primaryHint: \`السعر قبل الضريبة: \${fmtSAR(priceBeforeVat)} (ربحك: \${fmtSAR(profitPerUnit)} للقطعة)\`,
            breakdown: [
              { label: 'سعر البيع قبل الضريبة', value: fmtSAR(priceBeforeVat) },
              { label: 'مبلغ ضريبة القيمة المضافة 15%', value: fmtSAR(finalPriceWithVat - priceBeforeVat) },
              { label: 'نسبة الزيادة عن التكلفة (Markup)', value: \`\${markupPct.toFixed(1)}%\` },
              { label: 'نقطة التعادل الشهرية (Break-even)', value: \`\${breakEvenUnits} قطعة شهرياً\` },
              { label: 'مبيعات التعادل الشهرية', value: fmtSAR(breakEvenUnits * finalPriceWithVat) }
            ]
          });
        };
        pane.querySelectorAll('input').forEach(el => el.addEventListener('input', compute));
        compute();
      },

      roi(pane) {
        pane.innerHTML = \`
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="roiCapital" class="\${labelClass}">رأس المال المستثمر في المشروع (ر.س)</label>
              <input id="roiCapital" type="number" min="1" value="100000" class="\${inputClass}" />
            </div>
            <div>
              <label for="roiMonthly" class="\${labelClass}">صافي الأرباح الشهرية المتوقعة (ر.س)</label>
              <input id="roiMonthly" type="number" min="0" value="6500" class="\${inputClass}" />
            </div>
          </div>
        \`;
        const compute = () => {
          const capital = Math.max(1, parseFloat(document.getElementById('roiCapital').value) || 1);
          const monthly = Math.max(0, parseFloat(document.getElementById('roiMonthly').value) || 0);

          const annualProfit = monthly * 12;
          const annualRoi = (annualProfit / capital) * 100;
          const paybackMonths = monthly > 0 ? capital / monthly : 0;
          const paybackYears = paybackMonths / 12;

          let rating = 'عائد ممتاز جداً 🚀';
          if (annualRoi < 15) rating = 'عائد متواضع';
          else if (annualRoi < 30) rating = 'عائد جيد ومستقر';
          else if (annualRoi < 60) rating = 'عائد مرتفع ومجزي';

          updateResultPanel({
            primaryLabel: 'نسبة العائد السنوي على الاستثمار (ROI)',
            primaryValue: \`\${annualRoi.toFixed(1)}%\`,
            primaryHint: \`التقييم المالي: \${rating}\`,
            breakdown: [
              { label: 'إجمالي الأرباح السنوية', value: fmtSAR(annualProfit) },
              { label: 'فترة استرداد رأس المال', value: \`\${paybackMonths.toFixed(1)} شهر (\${paybackYears.toFixed(1)} سنة)\` },
              { label: 'إجمالي الأرباح بعد 3 سنوات', value: fmtSAR(annualProfit * 3) },
              { label: 'صافي الربح التراكمي (بعد خصم رأس المال)', value: fmtSAR((annualProfit * 3) - capital) }
            ]
          });
        };
        pane.querySelectorAll('input').forEach(el => el.addEventListener('input', compute));
        compute();
      },

      shipping_weight(pane) {
        pane.innerHTML = \`
          <div class="grid grid-cols-3 gap-3">
            <div>
              <label for="shpL" class="\${labelClass}">الطول (سم)</label>
              <input id="shpL" type="number" min="1" value="50" class="\${inputClass}" />
            </div>
            <div>
              <label for="shpW" class="\${labelClass}">العرض (سم)</label>
              <input id="shpW" type="number" min="1" value="40" class="\${inputClass}" />
            </div>
            <div>
              <label for="shpH" class="\${labelClass}">الارتفاع (سم)</label>
              <input id="shpH" type="number" min="1" value="30" class="\${inputClass}" />
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="shpActualWeight" class="\${labelClass}">الوزن الفعلي الحقيقي (كجم)</label>
              <input id="shpActualWeight" type="number" min="0.1" step="any" value="8" class="\${inputClass}" />
            </div>
            <div>
              <label for="shpRatePerKg" class="\${labelClass}">سعر الكيلو التقديري (ر.س)</label>
              <input id="shpRatePerKg" type="number" min="1" value="25" class="\${inputClass}" />
            </div>
          </div>
        \`;
        const compute = () => {
          const l = Math.max(1, parseFloat(document.getElementById('shpL').value) || 1);
          const w = Math.max(1, parseFloat(document.getElementById('shpW').value) || 1);
          const h = Math.max(1, parseFloat(document.getElementById('shpH').value) || 1);
          const actual = Math.max(0.1, parseFloat(document.getElementById('shpActualWeight').value) || 0.1);
          const rate = Math.max(1, parseFloat(document.getElementById('shpRatePerKg').value) || 25);

          const volWeight = (l * w * h) / 5000;
          const chargeableWeight = Math.max(actual, volWeight);
          const totalCost = chargeableWeight * rate;
          const isVolumetric = volWeight > actual;

          updateResultPanel({
            primaryLabel: 'الوزن الخاضع للفوترة (Chargeable Weight)',
            primaryValue: \`\${chargeableWeight.toFixed(2)} كجم\`,
            primaryHint: isVolumetric ? 'تنبيه: ستتم المحاسبة على الوزن الحجمي لأنه أكبر من الوزن الفعلي' : 'ستتم المحاسبة على الوزن الفعلي الحقيقي',
            breakdown: [
              { label: 'الوزن الفعلي الحقيقي', value: \`\${actual.toFixed(2)} كجم\` },
              { label: 'الوزن الحجمي (معادلة IATA الدولية)', value: \`\${volWeight.toFixed(2)} كجم\` },
              { label: 'نوع الوزن المعتمد للشحن', value: isVolumetric ? 'الوزن الحجمي 📦' : 'الوزن الفعلي ⚖️' },
              { label: 'تكلفة الشحن التقديرية', value: fmtSAR(totalCost) }
            ]
          });
        };
        pane.querySelectorAll('input').forEach(el => el.addEventListener('input', compute));
        compute();
      },

      gpa(pane) {`;

indexHtml = indexHtml.replace(buildersRegexAr, newBuildersAr);

if (!indexHtml.includes('تجارة وأعمال')) {
  console.error('❌ Failed to inject business category into Arabic index.html');
  process.exit(1);
}
fs.writeFileSync(indexPath, indexHtml, 'utf8');
console.log('✅ Arabic index.html successfully verified with business category and 29 calculators!');

// =========================================================================
// 2. ENGLISH: index-en.html
// =========================================================================

const catRegexEn = /const CATEGORIES = \{[\r\n\s]*all:\s*\{[^}]*\},/;
const newCatEn = `const CATEGORIES = {
      all: { label: 'All', count: 29 },
      business: {
        label: 'Business & E-com',
        count: 5,
        iconBox: 'bg-indigo-50 text-indigo-700 dark:bg-indigo-500/10 dark:text-indigo-400',
        badge: 'bg-indigo-50 text-indigo-700 dark:bg-indigo-500/10 dark:text-indigo-400'
      },`;

indexEnHtml = indexEnHtml.replace(catRegexEn, newCatEn);

const calcRegexEn = /\{\s*id:\s*'gpa'[\s\S]*?\}\s*\];/;
const newCalcsEn = `{ id: 'gpa', url: '/gpa-en', title: 'GPA Calculator', desc: 'Calculate semester and cumulative GPA out of 4 and 5 with honors rules.', category: 'general', icon: 'graduation-cap', keywords: 'gpa grade point average university tracks' },

      // Business & E-commerce (5)
      { id: 'ecommerce_profit', url: '/ecommerce-profit-en', title: 'E-commerce Net Profit', desc: 'Calculate net margins, payment gateway fees (Mada, Visa, Tabby), and ad spend (ROAS).', category: 'business', icon: 'shopping-cart', keywords: 'ecommerce profit margin salla zid amazon noon mada tabby roas cac' },
      { id: 'import_cost', url: '/import-cost-en', title: 'Landed Import Cost', desc: 'Calculate landed cost per unit including international shipping, customs, and 15% VAT.', category: 'business', icon: 'package-check', keywords: 'import landed cost customs zatca saber fasah freight cargo' },
      { id: 'pricing', url: '/pricing-calculator-en', title: 'Product Pricing & Break-even', desc: 'Determine optimal retail pricing based on desired net margins and break-even sales volume.', category: 'business', icon: 'target', keywords: 'pricing margin markup break even fixed costs retail' },
      { id: 'roi', url: '/roi-en', title: 'Return on Investment (ROI)', desc: 'Fast feasibility tool: compute annual ROI percentage and payback period in months and years.', category: 'business', icon: 'trending-up', keywords: 'roi return on investment payback period capital profit investment' },
      { id: 'shipping_weight', url: '/shipping-weight-en', title: 'Volumetric vs Actual Weight', desc: 'Compare actual vs volumetric weight using the international IATA standard formula.', category: 'business', icon: 'plane', keywords: 'volumetric weight dimensional actual weight iata shipping aramex dhl' }
    ];`;

indexEnHtml = indexEnHtml.replace(calcRegexEn, newCalcsEn);

const buildersRegexEn = /gpa\(pane\)\s*\{/;
const newBuildersEn = `ecommerce_profit(pane) {
        pane.innerHTML = \`
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="ecSalePrice" class="\${labelClass}">Product Retail Price (SAR)</label>
              <input id="ecSalePrice" type="number" min="0" value="199" class="\${inputClass}" />
            </div>
            <div>
              <label for="ecCostPrice" class="\${labelClass}">Unit Cost / Purchase Price (SAR)</label>
              <input id="ecCostPrice" type="number" min="0" value="70" class="\${inputClass}" />
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="ecShipping" class="\${labelClass}">Shipping & Delivery Cost (SAR)</label>
              <input id="ecShipping" type="number" min="0" value="25" class="\${inputClass}" />
            </div>
            <div>
              <label for="ecAdCost" class="\${labelClass}">Ad Cost Per Order - CAC (SAR)</label>
              <input id="ecAdCost" type="number" min="0" value="35" class="\${inputClass}" />
            </div>
          </div>
          <div>
            <label for="ecGateway" class="\${labelClass}">Payment Gateway</label>
            <select id="ecGateway" class="\${inputClass}">
              <option value="mada" selected>Mada (1.0% + SAR 1.0)</option>
              <option value="visa">Visa / Mastercard (2.2% + SAR 1.0)</option>
              <option value="tabby">Tabby / Tamara (7.0% + SAR 1.5)</option>
              <option value="cod">Cash on Delivery (0% gateway fee)</option>
            </select>
          </div>
        \`;
        const compute = () => {
          const sale = Math.max(0, parseFloat(document.getElementById('ecSalePrice').value) || 0);
          const cost = Math.max(0, parseFloat(document.getElementById('ecCostPrice').value) || 0);
          const ship = Math.max(0, parseFloat(document.getElementById('ecShipping').value) || 0);
          const ad = Math.max(0, parseFloat(document.getElementById('ecAdCost').value) || 0);
          const gw = document.getElementById('ecGateway').value;

          let gwFee = 0;
          if (gw === 'mada') gwFee = (sale * 0.01) + 1.0;
          else if (gw === 'visa') gwFee = (sale * 0.022) + 1.0;
          else if (gw === 'tabby') gwFee = (sale * 0.07) + 1.5;

          const totalExpenses = cost + ship + ad + gwFee;
          const netProfit = sale - totalExpenses;
          const margin = sale > 0 ? (netProfit / sale) * 100 : 0;
          const roas = ad > 0 ? (sale / ad) : 0;

          updateResultPanel({
            primaryLabel: 'Actual Net Profit Per Order',
            primaryValue: fmtSAR(netProfit),
            primaryHint: netProfit >= 0 ? 'Profitable order economics' : 'Warning: Total costs exceed selling price',
            breakdown: [
              { label: 'Customer Retail Price', value: fmtSAR(sale) },
              { label: 'Total Unit Expenses', value: fmtSAR(totalExpenses) },
              { label: 'Net Profit Margin', value: \`\${margin.toFixed(1)}%\` },
              { label: 'Payment Gateway Fee', value: fmtSAR(gwFee) },
              { label: 'Return on Ad Spend (ROAS)', value: \`\${roas.toFixed(2)}x\` }
            ]
          });
        };
        pane.querySelectorAll('input, select').forEach(el => el.addEventListener('input', compute));
        compute();
      },

      import_cost(pane) {
        pane.innerHTML = \`
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="impPrice" class="\${labelClass}">Unit Purchase Price (USD $)</label>
              <input id="impPrice" type="number" min="0" step="any" value="10" class="\${inputClass}" />
            </div>
            <div>
              <label for="impQty" class="\${labelClass}">Order Quantity (Units)</label>
              <input id="impQty" type="number" min="1" value="500" class="\${inputClass}" />
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="impShipUSD" class="\${labelClass}">Total International Freight (USD $)</label>
              <input id="impShipUSD" type="number" min="0" value="800" class="\${inputClass}" />
            </div>
            <div>
              <label for="impCustomsRate" class="\${labelClass}">Customs Tariff Rate (%)</label>
              <input id="impCustomsRate" type="number" min="0" max="100" value="5" class="\${inputClass}" />
            </div>
          </div>
          <div>
            <label for="impClearanceSAR" class="\${labelClass}">Clearance, Saber & Local Transport (SAR)</label>
            <input id="impClearanceSAR" type="number" min="0" value="1200" class="\${inputClass}" />
          </div>
        \`;
        const compute = () => {
          const priceUSD = Math.max(0, parseFloat(document.getElementById('impPrice').value) || 0);
          const qty = Math.max(1, parseInt(document.getElementById('impQty').value) || 1);
          const shipUSD = Math.max(0, parseFloat(document.getElementById('impShipUSD').value) || 0);
          const customsPct = Math.max(0, parseFloat(document.getElementById('impCustomsRate').value) || 0) / 100;
          const clearanceSAR = Math.max(0, parseFloat(document.getElementById('impClearanceSAR').value) || 0);

          const USD_TO_SAR = 3.75;
          const goodsCostSAR = priceUSD * qty * USD_TO_SAR;
          const shipCostSAR = shipUSD * USD_TO_SAR;
          const cifSAR = goodsCostSAR + shipCostSAR;
          const customsDutySAR = cifSAR * customsPct;
          const vatSAR = (cifSAR + customsDutySAR) * 0.15;

          const totalImportCostSAR = goodsCostSAR + shipCostSAR + customsDutySAR + vatSAR + clearanceSAR;
          const costPerUnitSAR = totalImportCostSAR / qty;

          updateResultPanel({
            primaryLabel: 'Total Landed Cost Per Unit',
            primaryValue: fmtSAR(costPerUnitSAR),
            primaryHint: \`Total Shipment Expense: \${fmtSAR(totalImportCostSAR)}\`,
            breakdown: [
              { label: 'Ex-Factory Goods Value (SAR)', value: fmtSAR(goodsCostSAR) },
              { label: 'International Freight (SAR)', value: fmtSAR(shipCostSAR) },
              { label: 'Estimated Customs Duty', value: fmtSAR(customsDutySAR) },
              { label: 'Import 15% VAT', value: fmtSAR(vatSAR) },
              { label: 'Clearance & Saber Platform Fees', value: fmtSAR(clearanceSAR) }
            ]
          });
        };
        pane.querySelectorAll('input').forEach(el => el.addEventListener('input', compute));
        compute();
      },

      pricing(pane) {
        pane.innerHTML = \`
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="prCost" class="\${labelClass}">Total Unit Cost (SAR)</label>
              <input id="prCost" type="number" min="0" value="50" class="\${inputClass}" />
            </div>
            <div>
              <label for="prMargin" class="\${labelClass}">Target Net Profit Margin (%)</label>
              <input id="prMargin" type="number" min="1" max="95" value="35" class="\${inputClass}" />
            </div>
          </div>
          <div>
            <label for="prFixedCosts" class="\${labelClass}">Monthly Fixed Overhead (Rent, Salaries, Software) (SAR)</label>
            <input id="prFixedCosts" type="number" min="0" value="5000" class="\${inputClass}" />
          </div>
        \`;
        const compute = () => {
          const cost = Math.max(0, parseFloat(document.getElementById('prCost').value) || 0);
          const margin = Math.min(95, Math.max(1, parseFloat(document.getElementById('prMargin').value) || 35)) / 100;
          const fixedCosts = Math.max(0, parseFloat(document.getElementById('prFixedCosts').value) || 0);

          const priceBeforeVat = cost / (1 - margin);
          const profitPerUnit = priceBeforeVat - cost;
          const finalPriceWithVat = priceBeforeVat * 1.15;
          const markupPct = cost > 0 ? (profitPerUnit / cost) * 100 : 0;
          const breakEvenUnits = profitPerUnit > 0 ? Math.ceil(fixedCosts / profitPerUnit) : 0;

          updateResultPanel({
            primaryLabel: 'Suggested Retail Price (with 15% VAT)',
            primaryValue: fmtSAR(finalPriceWithVat),
            primaryHint: \`Ex-VAT Price: \${fmtSAR(priceBeforeVat)} (Profit: \${fmtSAR(profitPerUnit)}/unit)\`,
            breakdown: [
              { label: 'Price Before VAT', value: fmtSAR(priceBeforeVat) },
              { label: '15% VAT Amount', value: fmtSAR(finalPriceWithVat - priceBeforeVat) },
              { label: 'Cost Markup Percentage', value: \`\${markupPct.toFixed(1)}%\` },
              { label: 'Monthly Break-even Volume', value: \`\${breakEvenUnits} units/month\` },
              { label: 'Break-even Gross Revenue', value: fmtSAR(breakEvenUnits * finalPriceWithVat) }
            ]
          });
        };
        pane.querySelectorAll('input').forEach(el => el.addEventListener('input', compute));
        compute();
      },

      roi(pane) {
        pane.innerHTML = \`
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="roiCapital" class="\${labelClass}">Total Invested Capital (SAR)</label>
              <input id="roiCapital" type="number" min="1" value="100000" class="\${inputClass}" />
            </div>
            <div>
              <label for="roiMonthly" class="\${labelClass}">Expected Monthly Net Profit (SAR)</label>
              <input id="roiMonthly" type="number" min="0" value="6500" class="\${inputClass}" />
            </div>
          </div>
        \`;
        const compute = () => {
          const capital = Math.max(1, parseFloat(document.getElementById('roiCapital').value) || 1);
          const monthly = Math.max(0, parseFloat(document.getElementById('roiMonthly').value) || 0);

          const annualProfit = monthly * 12;
          const annualRoi = (annualProfit / capital) * 100;
          const paybackMonths = monthly > 0 ? capital / monthly : 0;
          const paybackYears = paybackMonths / 12;

          let rating = 'Outstanding Return 🚀';
          if (annualRoi < 15) rating = 'Modest Yield';
          else if (annualRoi < 30) rating = 'Healthy & Stable';
          else if (annualRoi < 60) rating = 'High Yield';

          updateResultPanel({
            primaryLabel: 'Annual Return on Investment (ROI)',
            primaryValue: \`\${annualRoi.toFixed(1)}%\`,
            primaryHint: \`Feasibility Rating: \${rating}\`,
            breakdown: [
              { label: 'Projected Annual Profit', value: fmtSAR(annualProfit) },
              { label: 'Capital Payback Period', value: \`\${paybackMonths.toFixed(1)} months (\${paybackYears.toFixed(1)} years)\` },
              { label: 'Cumulative 3-Year Gross Profit', value: fmtSAR(annualProfit * 3) },
              { label: 'Net Profit Beyond Initial Capital', value: fmtSAR((annualProfit * 3) - capital) }
            ]
          });
        };
        pane.querySelectorAll('input').forEach(el => el.addEventListener('input', compute));
        compute();
      },

      shipping_weight(pane) {
        pane.innerHTML = \`
          <div class="grid grid-cols-3 gap-3">
            <div>
              <label for="shpL" class="\${labelClass}">Length (cm)</label>
              <input id="shpL" type="number" min="1" value="50" class="\${inputClass}" />
            </div>
            <div>
              <label for="shpW" class="\${labelClass}">Width (cm)</label>
              <input id="shpW" type="number" min="1" value="40" class="\${inputClass}" />
            </div>
            <div>
              <label for="shpH" class="\${labelClass}">Height (cm)</label>
              <input id="shpH" type="number" min="1" value="30" class="\${inputClass}" />
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="shpActualWeight" class="\${labelClass}">Actual Scale Weight (kg)</label>
              <input id="shpActualWeight" type="number" min="0.1" step="any" value="8" class="\${inputClass}" />
            </div>
            <div>
              <label for="shpRatePerKg" class="\${labelClass}">Freight Rate Per Kg (SAR)</label>
              <input id="shpRatePerKg" type="number" min="1" value="25" class="\${inputClass}" />
            </div>
          </div>
        \`;
        const compute = () => {
          const l = Math.max(1, parseFloat(document.getElementById('shpL').value) || 1);
          const w = Math.max(1, parseFloat(document.getElementById('shpW').value) || 1);
          const h = Math.max(1, parseFloat(document.getElementById('shpH').value) || 1);
          const actual = Math.max(0.1, parseFloat(document.getElementById('shpActualWeight').value) || 0.1);
          const rate = Math.max(1, parseFloat(document.getElementById('shpRatePerKg').value) || 25);

          const volWeight = (l * w * h) / 5000;
          const chargeableWeight = Math.max(actual, volWeight);
          const totalCost = chargeableWeight * rate;
          const isVolumetric = volWeight > actual;

          updateResultPanel({
            primaryLabel: 'Billable / Chargeable Weight',
            primaryValue: \`\${chargeableWeight.toFixed(2)} kg\`,
            primaryHint: isVolumetric ? 'Billed on volumetric weight (higher than actual scale weight)' : 'Billed on actual scale weight',
            breakdown: [
              { label: 'Actual Scale Weight', value: \`\${actual.toFixed(2)} kg\` },
              { label: 'IATA Volumetric Weight', value: \`\${volWeight.toFixed(2)} kg\` },
              { label: 'Applicable Billing Basis', value: isVolumetric ? 'Volumetric Dimension 📦' : 'Actual Weight ⚖️' },
              { label: 'Estimated Freight Charge', value: fmtSAR(totalCost) }
            ]
          });
        };
        pane.querySelectorAll('input').forEach(el => el.addEventListener('input', compute));
        compute();
      },

      gpa(pane) {`;

indexEnHtml = indexEnHtml.replace(buildersRegexEn, newBuildersEn);

if (!indexEnHtml.includes('Business & E-com')) {
  console.error('❌ Failed to inject business category into English index-en.html');
  process.exit(1);
}
fs.writeFileSync(indexEnPath, indexEnHtml, 'utf8');
console.log('✅ English index-en.html successfully verified with business category and 29 calculators!');
