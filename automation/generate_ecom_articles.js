const fs = require('fs');
const path = require('path');

const rootDir = 'C:/Users/ibrah/.gemini/antigravity/scratch/hasibha';
const articlesDir = path.join(rootDir, 'articles');

const articlesData = [
  {
    slug: 'ecommerce-profit-guide-2026',
    calcUrl: '/ecommerce-profit',
    calcUrlEn: '/ecommerce-profit-en',
    date: '25 November 2026',
    readTimeAr: '9 دقائق قراءة',
    readTimeEn: '9 min read',
    titleAr: 'دليل أرباح وعمولات المتاجر الإلكترونية في السعودية 2026: سلة، زد، وبوابات الدفع',
    descAr: 'دليل شامل للتجار وأصحاب المتاجر في سلة وزد: كيف تحسب صافي الربح الحقيقي لكل طلب، عمولات مدى وفيزا وتابي، تكلفة الإعلانات (CAC و ROAS)، والضريبة.',
    titleEn: 'Saudi E-Commerce Profitability & Fees Guide 2026: Salla, Zid & Gateways',
    descEn: 'Comprehensive guide to calculating true e-commerce net profit in Saudi Arabia. Payment gateway fees (Mada, Visa, Tabby), ad spend (ROAS/CAC), and 15% VAT.',
    keywordsAr: 'أرباح المتاجر الإلكترونية, عمولة سلة, عمولة زد, بوابات الدفع مدى فيزا, عمولة تابي وتمارا, حساب صافي الربح, roas, cac, دروب شيبينغ السعودية',
    keywordsEn: 'saudi ecommerce profit, salla fees, zid commissions, mada payment gateway fee, tabby tamara rates, net margin ecommerce, ksa roas cac',
    ctaTitleAr: 'جرب حاسبة صافي ربح المتجر الإلكتروني',
    ctaDescAr: 'احسب صافي ربحك الفعلي وهامش الربح الصافي بعد خصم الشحن والعمولات والإعلانات والضريبة',
    ctaBtnAr: 'افتح حاسبة أرباح المتاجر ←',
    ctaTitleEn: 'Try E-Commerce Net Profit Calculator',
    ctaDescEn: 'Calculate your actual net margins after deducting product cost, shipping, payment fees, and ad CAC',
    ctaBtnEn: 'Open E-Commerce Calculator →',
    contentAr: `
<h2>مقدمة عن طفرة التجارة الإلكترونية في السعودية</h2>
<p>تشهد المملكة العربية السعودية نمواً قياسياً في قطاع التجارة الإلكترونية تماشياً مع مستهدفات رؤية 2030 لتشجيع ريادة الأعمال والتحول الرقمي. ومع انطلاق آلاف المتاجر على منصات رائدة مثل <strong>سلة (Salla)</strong> و<strong>زد (Zid)</strong> وأمازون ونون، يواجه العديد من التجار المبتدئين فخاً مالياً شائعاً: <em>الخلط بين إجمالي المبيعات (Revenue) وصافي الربح الفعلي (Net Profit)</em>.</p>
<p>في هذا الدليل العملي لعام 2026، نكشف لك المعادلة المالية الدقيقة لحساب ربح كل طلب، وتفكيك بنود التكاليف الخفية التي تلتهم أرباح المتاجر: من عمولات بوابات الدفع الإلكتروني إلى تكلفة اكتساب العميل الإعلانية (CAC).</p>

<h2>جدول عمولات بوابات الدفع الإلكتروني في السعودية 2026</h2>
<p>تختلف رسوم الدفع الإلكتروني باختلاف الوسيلة التي يختارها العميل عند إتمام الشراء:</p>
<table class="article-table">
  <thead>
    <tr>
      <th>وسيلة الدفع</th>
      <th>النسبة المئوية</th>
      <th>الرسم الثابت للعملية</th>
      <th>ملاحظات</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>بطاقات مدى (Mada)</strong></td><td>1.0%</td><td>1.00 ريال</td><td>الخيار الأكثر شعبية واستخداماً في السعودية</td></tr>
    <tr><td><strong>البطاقات الائتمانية (Visa / Master)</strong></td><td>2.2%</td><td>1.00 ريال</td><td>تشمل بطاقات الدفع والائتمان المحلية والدولية</td></tr>
    <tr><td><strong>اشتر الآن وادفع لاحقاً (تابي / تمارا)</strong></td><td>~ 7.0%</td><td>1.50 ريال</td><td>تزيد نسبة التحويل ولكنها تقتطع نسبة مرتفعة من الربح</td></tr>
    <tr><td><strong>الدفع عند الاستلام (COD)</strong></td><td>0% عمولة بنكية</td><td>رسوم تحصيل لشركة الشحن</td><td>ترتفع فيها نسبة الشحنات المرتجعة غير المستلمة</td></tr>
  </tbody>
</table>

<h2>المعادلة الرياضية لصافي ربح الطلب الواحد</h2>
<blockquote style="background:var(--surface);color:var(--text);padding:18px;border-inline-start:4px solid var(--accent);border-radius:12px;margin:20px 0;">
  <strong>صافي الربح = سعر البيع للعميل - (تكلفة المنتج + تكلفة الشحن + عمولة بوابة الدفع + تكلفة الإعلان لكل طلب CAC + ضريبة 15%)</strong>
</blockquote>

<h3>مثال تطبيقي عملي بالأرقام:</h3>
<p>افترض أنك تبيع ساعة يد بسعر <strong>200 ريال</strong> شاملة الشحن المجاني:</p>
<ul>
  <li>تكلفة شراء الساعة من المورد = <strong>60 ريال</strong>.</li>
  <li>تكلفة بوليصة الشحن = <strong>25 ريال</strong>.</li>
  <li>تكلفة الإعلانات لكل طلب مبيع (CAC) = <strong>35 ريال</strong>.</li>
  <li>دفع العميل ببطاقة مدى ➦ عمولة البوابة: (200 × 1%) + 1 = <strong>3 ريال</strong>.</li>
  <li>ضريبة القيمة المضافة 15% على هامش الربح والخدمات = <strong>12 ريال</strong> تقريباً.</li>
  <li><strong>إجمالي المصاريف = 60 + 25 + 35 + 3 + 12 = 135 ريال</strong>.</li>
  <li><strong>صافي الربح الفعلي = 200 - 135 = 65 ريال (هامش ربح صافٍ 32.5%)</strong>.</li>
</ul>

<h2>أهم مؤشرات الأداء المالي لمتجرك (ROAS و CAC)</h2>
<ol>
  <li><strong>العائد على الإنفاق الإعلاني (ROAS):</strong><br>
  يُحسب بقسمة (إجمالي المبيعات ÷ ميزانية الإعلانات). إذا كان هدفك تغطية التكاليف وتحقيق أرباح صحية، يجب ألا يقل ROAS عن 3.5x إلى 4.0x في معظم منتجات التجارة الإلكترونية.</li>
  <li><strong>تكلفة اكتساب العميل (CAC):</strong><br>
  إجمالي ما تنفقه على منصات إعلانات تيك توك وسناب شات وميتا مقسوماً على عدد الطلبات المحققة فعلياً.</li>
</ol>
`,
    contentEn: `
<h2>E-Commerce in Saudi Arabia: Revenue vs Net Profit</h2>
<p>With thousands of active merchants operating on <strong>Salla</strong>, <strong>Zid</strong>, Amazon, and Noon under Saudi Vision 2030 digital economy initiatives, mastering unit economics is the single most critical factor separating profitable brands from failed ventures.</p>

<h2>Payment Gateway Fee Breakdown 2026</h2>
<table class="article-table">
  <thead>
    <tr>
      <th>Payment Method</th>
      <th>Variable Fee</th>
      <th>Fixed Fee</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Mada Debit</td><td>1.0%</td><td>SAR 1.00</td></tr>
    <tr><td>Credit Cards (Visa / MC)</td><td>2.2%</td><td>SAR 1.00</td></tr>
    <tr><td>BNPL (Tabby / Tamara)</td><td>~ 7.0%</td><td>SAR 1.50</td></tr>
    <tr><td>Cash on Delivery (COD)</td><td>0% (Banking)</td><td>Carrier Collection Fee</td></tr>
  </tbody>
</table>

<h2>Order Unit Economics Formula</h2>
<blockquote style="background:var(--surface);color:var(--text);padding:18px;border-inline-start:4px solid var(--accent);border-radius:12px;margin:20px 0;">
  <strong>Net Profit = Retail Price - (Product Cost + Shipping + Gateway Fees + Ad CAC + 15% VAT)</strong>
</blockquote>
`
  },
  {
    slug: 'import-cost-guide-2026',
    calcUrl: '/import-cost',
    calcUrlEn: '/import-cost-en',
    date: '25 November 2026',
    readTimeAr: '10 دقائق قراءة',
    readTimeEn: '10 min read',
    titleAr: 'دليل الاستيراد من الصين إلى السعودية 2026: حساب الجمارك وسابر والتكلفة الشاملة',
    descAr: 'دليل شامل للتجار والمستوردين: حساب تكلفة القطعة الواصلة للمستودع (Landed Cost)، الرسوم الجمركية زاتكا، منصة سابر وفسح، والشحن الجوي والبحري.',
    titleEn: 'Importing to Saudi Arabia Guide 2026: Landed Cost, Customs & Saber',
    descEn: 'Complete guide for Saudi importers: Landed cost per unit, ZATCA customs duties, Saber platform compliance, international ocean/air freight, and 15% VAT.',
    keywordsAr: 'الاستيراد من الصين إلى السعودية, تكلفة الواصل للمستودع landed cost, منصة سابر, تعرفة الجمارك السعودية زاتكا, منصة فسح, تكلفة الشحن من الصين, ضريبة الاستيراد',
    keywordsEn: 'importing to saudi arabia, landed cost calculator ksa, saber platform compliance, zatca customs duty rate, air freight china to saudi, ocean freight import ksa',
    ctaTitleAr: 'جرب حاسبة تكلفة الاستيراد الشاملة',
    ctaDescAr: 'احسب التكلفة الدقيقة للقطعة الواحدة واصلة للمستودع شاملاً الشحن والجمارك وسابر والضريبة',
    ctaBtnAr: 'افتح حاسبة تكلفة الاستيراد ←',
    ctaTitleEn: 'Try Landed Import Cost Calculator',
    ctaDescEn: 'Calculate exact unit cost delivered to your warehouse including freight, customs, Saber, and VAT',
    ctaBtnEn: 'Open Import Calculator →',
    contentAr: `
<h2>مقدمة عن الاستيراد التجاري للمملكة العربية السعودية</h2>
<p>يُعد الاستيراد من الصين والأسواق العالمية عصب تجارة التجزئة والتوزيع في السعودية. إلا أن العديد من رواد الأعمال يقعون في خطأ الاكتفاء بحساب سعر الشراء من المصنع على منصات مثل <em>Alibaba</em>، ليفاجأوا عند وصول الشحنة بمصاريف إضافية ترفع تكلفة المنتج بنسبة 30% إلى 50% وتؤدي إلى تآكل هامش الربح بالكامل.</p>
<p>في هذا الدليل لعام 2026، نوضح المفهوم المالي لـ <strong>التكلفة الشاملة للواصل (Landed Cost)</strong> وكيفية حساب بنود الجمارك (ZATCA)، متطلبات منصة سابر (Saber)، ورسوم التخليص والنقل الداخلي.</p>

<h2>مكونات التكلفة الشاملة للقطعة (Landed Cost)</h2>
<p>تتألف التكلفة الحقيقية لأي بضاعة مستوردة من 5 بنود أساسية:</p>
<ol>
  <li><strong>قيمة البضاعة في المصنع (FOB / EXW):</strong> سعر الشراء المتفق عليه بالدولار الأمريكي.</li>
  <li><strong>تكلفة الشحن الدولي والتأمين (Freight & Insurance):</strong> تكلفة نقل الحاوية بحراً أو الطرد جواً حتى الميناء السعودي (CIF).</li>
  <li><strong>الرسوم الجمركية (Customs Duty):</strong> تُحسب وفق التعرفة الجمركية المتكاملة لهيئة الزكاة والضريبة والجمارك (غالباً 5% لمعظم المنتجات، وقد تصل إلى 12% أو 15% لبعض السلع المحمية).</li>
  <li><strong>ضريبة القيمة المضافة للاستيراد (15%):</strong> تُحسب على إجمالي (قيمة البضاعة + تكلفة الشحن والتأمين + الرسوم الجمركية).</li>
  <li><strong>مصاريف التخليص والمنصات التنظيمية:</strong> رسوم منصة سابر لإصدار شهادات المطابقة، إذن التسليم الملاحي، أتعاب المخلص الجمركي، والنقل بالشاحنة إلى مستودعك.</li>
</ol>

<h2>جدول مقارنة بين الشحن البحري والجوي</h2>
<table class="article-table">
  <thead>
    <tr>
      <th>نوع الشحن</th>
      <th>مدة الوصول التقديرية</th>
      <th>التكلفة النسبية</th>
      <th>الأنسب لـ</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>الشحن البحري (حاوية كاملة FCL أو مجمعة LCL)</strong></td><td>22 - 35 يوماً</td><td>منخفضة جداً لكل قطعة</td><td>الكميات الكبيرة، المنتجات الثقيلة، والسلع ذات الهوامش المحدودة</td></tr>
    <tr><td><strong>الشحن الجوي التجاري (Air Freight)</strong></td><td>5 - 9 أيام</td><td>متوسطة إلى مرتفعة</td><td>المنتجات الخفيفة، الإلكترونيات، والعينات السريعة</td></tr>
    <tr><td><strong>الشحن السريع (Express Courier)</strong></td><td>3 - 5 أيام</td><td>مرتفعة جداً</td><td>الطرود العاجلة والطلبات الخاصة</td></tr>
  </tbody>
</table>

<h2>نصائح ذهبية لتخفيض تكلفة الاستيراد</h2>
<ul>
  <li><strong>التأكد من رمز النظام المنسق (HS Code):</strong> معرفة الكود الدقيق للمنتج قبل الشراء لتحديد نسبة الجمارك ومتطلبات شهادة سابر بدقة وتفادي غرامات الميناء.</li>
  <li><strong>التفاوض على شروط الشحن الدولية (Incoterms):</strong> يُفضل الشراء بشروط FOB حيث تختار أنت شركة الشحن ووكيل التخليص بسعر منافس.</li>
  <li><strong>دمج الشحنات وتفادي الفراغات:</strong> تعبئة الكراتين بأقصى كفاءة لتقليل تكلفة الحاوية والشحن الحجمي.</li>
</ul>
`,
    contentEn: `
<h2>True Landed Cost Economics for Saudi Importers</h2>
<p>Successful importing into Saudi Arabia requires looking far beyond the supplier's initial FOB factory invoice. Total landed cost incorporates customs duties, Saber platform compliance, port handling, shipping insurance, and 15% import VAT.</p>

<h2>Landed Cost Structure</h2>
<ol>
  <li><strong>Ex-Factory Goods Value:</strong> Base purchase price from supplier.</li>
  <li><strong>International Ocean / Air Freight:</strong> Transport costs to Saudi entry ports (Jeddah Islamic Port, King Abdulaziz Port Dammam, Riyadh Dry Port, or King Khalid International Airport).</li>
  <li><strong>ZATCA Customs Duties:</strong> Applied on CIF value (typically 5% for standard consumer goods).</li>
  <li><strong>Import VAT (15%):</strong> Assessed on total (CIF Value + Customs Duty).</li>
  <li><strong>Regulatory & Clearance Fees:</strong> Saber conformity certificate, Fasah platform clearance, port handling, and inland transport to warehouse.</li>
</ol>
`
  },
  {
    slug: 'pricing-calculator-guide-2026',
    calcUrl: '/pricing-calculator',
    calcUrlEn: '/pricing-calculator-en',
    date: '25 November 2026',
    readTimeAr: '8 دقائق قراءة',
    readTimeEn: '8 min read',
    titleAr: 'دليل تسعير المنتجات ونقطة التعادل للتجار 2026: استراتيجيات التسعير وهامش الربح',
    descAr: 'دليل عملي لتسعير المنتجات في المتاجر والمشاريع السعودية: الفرق بين Markup و Margin، كيفية تحديد السعر شامل الضريبة، وحساب نقطة التعادل (Break-even).',
    titleEn: 'Product Pricing & Break-Even Guide 2026: Margins, Markups & Strategy',
    descEn: 'Practical guide to retail product pricing in Saudi Arabia: Margin vs Markup formulas, 15% VAT pricing, and calculating monthly break-even unit volume.',
    keywordsAr: 'تسعير المنتجات, هامش الربح margin, نسبة الاضافة markup, نقطة التعادل break even, تسعير المتاجر الالكترونية, استراتيجيات التسعير, حساب التكاليف الثابتة',
    keywordsEn: 'product pricing strategy, margin vs markup formula, break even point calculation, retail pricing ksa, fixed overhead break even',
    ctaTitleAr: 'جرب حاسبة تسعير المنتجات ونقطة التعادل',
    ctaDescAr: 'حدد السعر الأنسب لمنتجك قبل وبعد الضريبة واحسب عدد القطع المطلوب بيعها لتغطية تكاليفك',
    ctaBtnAr: 'افتح حاسبة التسعير ←',
    ctaTitleEn: 'Try Product Pricing & Break-Even Calculator',
    ctaDescEn: 'Determine optimal retail prices based on desired net margins and calculate monthly break-even sales volume',
    ctaBtnEn: 'Open Pricing Calculator →',
    contentAr: `
<h2>أهمية استراتيجية التسعير في السوق السعودي</h2>
<p>يُعتبر <strong>تسعير المنتجات</strong> القرار الاستراتيجي الأهم الذي يحدد مصير أي متجر أو علامة تجارية. فالتسعير المرتفع غير المدروس ينفر العملاء لصالح المنافسين، بينما التسعير المنخفض يؤدي إلى إفلاس المتجر بالرغم من تحقيقه مبيعات ضخمة! كما أن الفهم الخاطئ للفرق بين هامش الربح (Margin) ونسبة الإضافة فوق التكلفة (Markup) هو السبب وراء خسائر 40% من المتاجر الناشئة.</p>

<h2>الفرق الجوهري بين Margin و Markup</h2>
<table class="article-table">
  <thead>
    <tr>
      <th>المفهوم</th>
      <th>التعريف</th>
      <th>المعادلة الرياضية</th>
      <th>مثال (تكلفة 100 ر.س وبيعه بـ 150 ر.س)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>نسبة الإضافة (Markup %)</strong></td>
      <td>نسبة الربح المضاف فوق تكلفة الشراء</td>
      <td>(مبلغ الربح ÷ التكلفة) × 100</td>
      <td>(50 ÷ 100) × 100 = <strong>50% Markup</strong></td>
    </tr>
    <tr>
      <td><strong>هامش الربح (Margin %)</strong></td>
      <td>نسبة ما يمثله الربح من إجمالي سعر البيع</td>
      <td>(مبلغ الربح ÷ سعر البيع) × 100</td>
      <td>(50 ÷ 150) × 100 = <strong>33.3% Margin</strong></td>
    </tr>
  </tbody>
</table>

<h2>معادلة تسعير المنتج بناءً على هامش الربح المستهدف</h2>
<blockquote style="background:var(--surface);color:var(--text);padding:18px;border-inline-start:4px solid var(--accent);border-radius:12px;margin:20px 0;">
  <strong>سعر البيع المقترح قبل الضريبة = التكلفة الإجمالية للوحدة ÷ (1 - نسبة هامش الربح المطلوب)</strong>
</blockquote>
<p>فإذا كانت تكلفة القطعة 80 ريالاً، وتريد تحقيق هامش ربح صافٍ قدره 35%:<br>
سعر البيع قبل الضريبة = 80 ÷ (1 - 0.35) = 80 ÷ 0.65 = <strong>123.08 ريال</strong>.<br>
السعر النهائي للمستهلك شاملاً 15% ضريبة = 123.08 × 1.15 = <strong>141.54 ريال سعودي</strong>.</p>

<h2>كيف تحسب نقطة التعادل (Break-Even Point)؟</h2>
<p>نقطة التعادل هي حجم المبيعات الذي تتساوى عنده الإيرادات مع كافة التكاليف، بحيث لا يحقق المشروع ربحاً ولا خسارة. وكل قطعة تُباع بعد هذه النقطة تمثل ربحاً صافياً خالصاً:</p>
<blockquote style="background:var(--surface);color:var(--text);padding:18px;border-inline-start:4px solid var(--accent);border-radius:12px;margin:20px 0;">
  <strong>عدد قطع التعادل = المصاريف الشهرية الثابتة ÷ هامش ربح القطعة الواحدة</strong>
</blockquote>
`,
    contentEn: `
<h2>Retail Pricing Strategy in KSA: Margin vs Markup</h2>
<p>Product pricing represents the single most influential lever on retail business health. The mathematical difference between gross margin and cost markup causes significant confusion among new founders:</p>
<ul>
  <li><strong>Markup:</strong> Profit expressed as a percentage of unit cost.</li>
  <li><strong>Margin:</strong> Profit expressed as a percentage of selling price.</li>
</ul>

<h2>Break-Even Volume Formula</h2>
<blockquote style="background:var(--surface);color:var(--text);padding:18px;border-inline-start:4px solid var(--accent);border-radius:12px;margin:20px 0;">
  <strong>Break-Even Units = Total Monthly Fixed Overhead ÷ Unit Contribution Margin</strong>
</blockquote>
`
  },
  {
    slug: 'roi-guide-2026',
    calcUrl: '/roi',
    calcUrlEn: '/roi-en',
    date: '25 November 2026',
    readTimeAr: '8 دقائق قراءة',
    readTimeEn: '8 min read',
    titleAr: 'دليل العائد على الاستثمار (ROI) وفترة الاسترداد للمشاريع 2026: دراسة الجدوى السريعة',
    descAr: 'دليل شامل لحساب العائد على الاستثمار للمشاريع والمتاجر في السعودية: معادلة ROI السنوية، مدة استرداد رأس المال بالشهور والسنوات، وتقييم جدوى الفرص الاستثمارية.',
    titleEn: 'Return on Investment (ROI) & Payback Guide 2026: Financial Feasibility',
    descEn: 'Comprehensive guide to calculating ROI percentage, payback periods, and evaluating capital feasibility for small businesses and e-commerce ventures in Saudi Arabia.',
    keywordsAr: 'العائد على الاستثمار roi, فترة استرداد رأس المال payback period, دراسة جدوى المشاريع, تقييم الاستثمار, ارباح المشاريع الصغيرة السعودية',
    keywordsEn: 'return on investment ksa, roi calculator business, payback period formula, capital recovery time, investment feasibility saudi',
    ctaTitleAr: 'جرب حاسبة العائد على الاستثمار (ROI)',
    ctaDescAr: 'احسب نسبة العائد السنوي المتوقع وفترة استرداد رأس المال بالشهور والسنوات لمشروعك',
    ctaBtnAr: 'افتح حاسبة العائد على الاستثمار ←',
    ctaTitleEn: 'Try Return on Investment Calculator',
    ctaDescEn: 'Calculate your annual ROI percentage and capital payback period in months and years',
    ctaBtnEn: 'Open ROI Calculator →',
    contentAr: `
<h2>ما هو العائد على الاستثمار (ROI) ولماذا هو المعيار الأهم؟</h2>
<p>يُعد <strong>العائد على الاستثمار (Return on Investment - ROI)</strong> المقياس المالي العالمي الأول الذي يستخدمه المستثمرون ورواد الأعمال لتقييم كفاءة وجدوى أي مشروع تجاري أو حملة توسعية. فالربح كرقم مجرد (مثلاً 50,000 ريال) لا يعني شيئاً دون مقارنته بحجم رأس المال الذي تم توظيفه لتحقيق هذا الربح والمدة الزمنية المستغرقة.</p>

<h2>المعادلة الرياضية لاحتساب ROI السنوي</h2>
<blockquote style="background:var(--surface);color:var(--text);padding:18px;border-inline-start:4px solid var(--accent);border-radius:12px;margin:20px 0;">
  <strong>نسبة العائد السنوي (ROI %) = (صافي الأرباح السنوية ÷ إجمالي رأس المال المستثمر) × 100</strong>
</blockquote>

<h2>فترة استرداد رأس المال (Payback Period)</h2>
<p>توضح المدة الزمنية اللازمة للمشروع لتغطية رأس ماله الأولي والبدء في توليد أرباح حرة إضافية:</p>
<blockquote style="background:var(--surface);color:var(--text);padding:18px;border-inline-start:4px solid var(--accent);border-radius:12px;margin:20px 0;">
  <strong>فترة الاسترداد (بالأشهر) = رأس المال المستثمر ÷ صافي الربح الشهري</strong>
</blockquote>

<h3>جدول المعايير الاسترشادية لجودة العائد على الاستثمار في السعودية:</h3>
<table class="article-table">
  <thead>
    <tr>
      <th>نسبة ROI السنوية</th>
      <th>فترة الاسترداد المقابلة</th>
      <th>التقييم الاستثماري</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>أقل من 15%</td><td>أكثر من 6.5 سنوات</td><td>عائد متواضع (قد تكون البدائل الاستثمارية منخفضة المخاطر أفضل)</td></tr>
    <tr><td>15% - 30%</td><td>3.3 إلى 6.5 سنوات</td><td>عائد جيد ومستقر ومقبول في قطاعات التجزئة التقليدية</td></tr>
    <tr><td>30% - 60%</td><td>1.6 إلى 3.3 سنوات</td><td>عائد ممتاز ومجزي جداً في التجارة الإلكترونية والمشاريع الخدمية</td></tr>
    <tr><td>أكثر من 60%</td><td>أقل من 20 شهراً</td><td>عائد استثنائي وفائق النمو 🚀</td></tr>
  </tbody>
</table>
`,
    contentEn: `
<h2>Evaluating Investment Feasibility with ROI</h2>
<p>Return on Investment (ROI) measures the efficiency of capital deployed across entrepreneurial ventures, retail stores, or e-commerce brands in Saudi Arabia.</p>

<h2>Core Financial Formulas</h2>
<ul>
  <li><strong>Annual ROI (%) = (Annual Net Profit ÷ Invested Capital) × 100</strong></li>
  <li><strong>Payback Period (Months) = Invested Capital ÷ Monthly Net Profit</strong></li>
</ul>
`
  },
  {
    slug: 'shipping-weight-guide-2026',
    calcUrl: '/shipping-weight',
    calcUrlEn: '/shipping-weight-en',
    date: '25 November 2026',
    readTimeAr: '8 دقائق قراءة',
    readTimeEn: '8 min read',
    titleAr: 'دليل الوزن الحجمي وتكلفة الشحن الدولي 2026: معادلة IATA وتفادي زيادة التكاليف',
    descAr: 'دليل شامل للتجار وأصحاب الشحنات: ما هو الوزن الحجمي، معادلة IATA الدولية (الطول×العرض×الارتفاع ÷ 5000)، وكيف تمنع مفاجآت شركات الشحن أرامكس وDHL وسمسا.',
    titleEn: 'Volumetric vs Actual Weight Shipping Guide 2026: IATA Formula & Savings',
    descEn: 'Complete guide to volumetric dimensional weight in courier and air freight shipping. The IATA 5000 formula, chargeable weight rules, and packaging tips to lower freight costs.',
    keywordsAr: 'الوزن الحجمي volumetric weight, معادلة iata للشحن, الوزن الخاضع للفوترة chargeable weight, تكلفة الشحن ارامكس dhl سمسا, ابعاد الكرتون, تخفيض تكلفة الشحن',
    keywordsEn: 'volumetric weight shipping, dimensional weight calculation, iata 5000 formula, chargeable freight weight, air courier packaging tips ksa',
    ctaTitleAr: 'جرب حاسبة الوزن الحجمي وتكلفة الشحن',
    ctaDescAr: 'قارن الوزن الفعلي بالوزن الحجمي لكرتونك فورياً واعرف الوزن المعتمد للفوترة وتكلفة الشحن التقديرية',
    ctaBtnAr: 'افتح حاسبة الوزن الحجمي ←',
    ctaTitleEn: 'Try Volumetric Weight Calculator',
    ctaDescEn: 'Compare scale weight vs dimensional weight and identify the exact billable weight for your shipment',
    ctaBtnEn: 'Open Shipping Calculator →',
    contentAr: `
<h2>لماذا تحاسبك شركات الشحن على الحجم بدلاً من الوزن الحقيقي؟</h2>
<p>كثيراً ما يتفاجأ أصحاب المتاجر والمستوردون عند شحن بضائع خفيفة الوزن (مثل الملابس أو الإسفنج أو الألعاب البلاستيكية) بأن شركة الشحن تفرض عليهم تكلفة مضاعفة أضعافاً عما توقعوا بناءً على الميزان! السبب في ذلك هو <strong>الوزن الحجمي (Volumetric / Dimensional Weight)</strong>.</p>
<p>فطائرات الشحن وشاحنات النقل تمتلك مساحة شحن محدودة؛ وصندوق كبير مملوء بالقطن يزن 5 كيلوغرامات يشغل نفس الحيز الذي تشغله سبائك حديد تزن 50 كيلوغراماً. لذا وضعت المنظمات الدولية للشحن معايير موحدة للعدالة بين الحجم والوزن.</p>

<h2>معادلة IATA الدولية لحساب الوزن الحجمي</h2>
<blockquote style="background:var(--surface);color:var(--text);padding:18px;border-inline-start:4px solid var(--accent);border-radius:12px;margin:20px 0;">
  <strong>الوزن الحجمي (كجم) = (الطول × العرض × الارتفاع بالسنتيمتر) ÷ 5000</strong>
</blockquote>
<p><em>ملاحظة:</em> الرقم 5000 هو المعيار المعتمد لدى معظم شركات الشحن الجوي السريع في السعودية (أرامكس، DHL، فيديكس، سمسا، وسبل). وتستخدم بعض شركات الشحن البحري أو الاقتصادي مقسوماً قدره 6000.</p>

<h2>ما هو الوزن الخاضع للفوترة (Chargeable Weight)؟</h2>
<p>تطبق شركات الشحن قاعدة بسيطة ومباشرة:</p>
<blockquote style="background:#ecfdf5;padding:16px;border:1px solid #a7f3d0;border-radius:8px;margin:20px 0;color:#065f46;">
  <strong>الوزن المعتمد للشحن = أيهما أكبر: الوزن الفعلي على الميزان أم الوزن الحجمي بالأبعاد</strong>
</blockquote>

<h3>مثال تطبيقي:</h3>
<p>كرتون أبعاده: طول 60 سم، عرض 40 سم، ارتفاع 30 سم، ووزنه الفعلي على الميزان 8 كجم:</p>
<ul>
  <li>حساب الوزن الحجمي = (60 × 40 × 30) ÷ 5000 = 72,000 ÷ 5000 = <strong>14.4 كجم</strong>.</li>
  <li>الوزن الفعلي = <strong>8 كجم</strong>.</li>
  <li><strong>الوزن الخاضع للفوترة = 14.4 كجم</strong> (ستتم محاسبتك على 14.4 كجم وليس 8 كجم!).</li>
</ul>

<h2>أقوى 4 نصائح لتفادي دفع تكاليف الشحن الحجمي الزائدة</h2>
<ol>
  <li><strong>اختيار الكرتون المناسب لحجم المنتج تماماً:</strong> تجنب وضع منتج صغير في كرتون كبير مليء بالفراغات وأكياس الهواء.</li>
  <li><strong>استخدام أكياس الشحن البلاستيكية (Flyer Bags):</strong> للملابس والمنسوجات لأنها تأخذ حجم المنتج بالضبط دون أبعاد ثابتة.</li>
  <li><strong>التفريغ الهوائي (Vacuum Packing):</strong> يقلل حجم الوسائد والملابس الشتوية والدمى بنسبة تصل إلى 60%.</li>
  <li><strong>قص وتعديل حواف الكرتون:</strong> إذا كان هناك فراغ علوي في الكرتون، قم بقص الزوايا وثنيها لتقليل الارتفاع بضعة سنتيمترات توفر عليك مئات الريالات.</li>
</ol>
`,
    contentEn: `
<h2>Why Shipping Carriers Charge for Dimensional Volume</h2>
<p>International courier and express air freight carriers (Aramex, DHL, FedEx, SMSA, and SPL) utilize <strong>Volumetric (Dimensional) Weight</strong> alongside scale weight to account for the physical cargo volume occupied in aircraft and transport containers.</p>

<h2>The IATA International Formula</h2>
<blockquote style="background:var(--surface);color:var(--text);padding:18px;border-inline-start:4px solid var(--accent);border-radius:12px;margin:20px 0;">
  <strong>Volumetric Weight (kg) = (Length × Width × Height in cm) ÷ 5000</strong>
</blockquote>
<p><strong>Chargeable Weight:</strong> The billing basis is always the greater of scale weight or volumetric weight.</p>
`
  }
];

function buildArticleHtml(art, isEn = false) {
  const lang = isEn ? 'en' : 'ar';
  const dir = isEn ? 'ltr' : 'rtl';
  const title = isEn ? art.titleEn : art.titleAr;
  const desc = isEn ? art.descEn : art.descAr;
  const keywords = isEn ? art.keywordsEn : art.keywordsAr;
  const content = isEn ? art.contentEn : art.contentAr;
  const ctaTitle = isEn ? art.ctaTitleEn : art.ctaTitleAr;
  const ctaDesc = isEn ? art.ctaDescEn : art.ctaDescAr;
  const ctaBtn = isEn ? art.ctaBtnEn : art.ctaBtnAr;
  const ctaUrl = isEn ? art.calcUrlEn : art.calcUrl;
  const slug = art.slug;
  const canonicalUrl = isEn ? `https://hasibha.com/articles/${slug}-en` : `https://hasibha.com/articles/${slug}`;
  const alternateAr = `https://hasibha.com/articles/${slug}`;
  const alternateEn = `https://hasibha.com/articles/${slug}-en`;
  const toggleUrl = isEn ? `/articles/${slug}` : `/articles/${slug}-en`;
  const toggleLabel = isEn ? 'AR' : 'EN';
  const authorName = isEn ? 'Hasibha Business Team' : 'فريق حاسبها للأعمال';

  let h2Count = 0;
  const tocList = [];
  const processedContent = content.replace(/<h2>(.*?)<\/h2>/g, (match, headingText) => {
    h2Count++;
    const id = `section-${h2Count}`;
    tocList.push({ id, text: headingText.replace(/<[^>]+>/g, '') });
    return `<h2 id="${id}">${headingText}<\/h2>`;
  });

  const tocHtml = tocList.length > 0 ? `
<div class="toc-box" style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:20px;margin:24px 0;">
  <div style="font-weight:700;font-size:15px;color:var(--text);margin-bottom:12px;display:flex;align-items:center;gap:8px;">
    <span>📌</span>
    <span>${isEn ? 'Table of Contents' : 'جدول المحتويات'}</span>
  </div>
  <ul style="list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit, minmax(260px, 1fr));gap:8px;">
    ${tocList.map(item => `<li><a href="#${item.id}" style="color:var(--accent);text-decoration:none;font-size:14px;display:flex;align-items:center;gap:6px;padding:6px 10px;border-radius:8px;background:var(--card);border:1px solid var(--border);transition:all 0.2s;"><span style="opacity:0.6;">#</span> <span>${item.text}</span></a></li>`).join('\n    ')}
  </ul>
</div>
` : '';

  return `<!DOCTYPE html>
<html lang="${lang}" dir="${dir}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--hs:assets-->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/css/style.css?v=5">
<link rel="manifest" href="/manifest.json" />
<meta name="theme-color" content="#059669" />
<link rel="dns-prefetch" href="https://pagead2.googlesyndication.com">
<link rel="dns-prefetch" href="https://www.googletagmanager.com">
<script>try{var t=localStorage.getItem('hs-theme')||localStorage.getItem('hasibha_theme');if(t==='dark'||(!t&&window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)){document.documentElement.setAttribute('data-theme','dark');document.documentElement.classList.add('dark');}}catch(e){}</script>
<!--/hs:assets-->
<title>${title} | ${isEn ? 'Hasibha' : 'حاسبها'}</title>
<meta name="description" content="${desc}">
<meta name="keywords" content="${keywords}">
<link rel="canonical" href="${canonicalUrl}">
<link rel="alternate" hreflang="ar" href="${alternateAr}">
<link rel="alternate" hreflang="en" href="${alternateEn}">
<link rel="alternate" hreflang="x-default" href="${alternateAr}">
<link rel="icon" type="image/png" href="/images/logo.png">
<meta property="og:title" content="${title}">
<meta property="og:description" content="${desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="${canonicalUrl}">
<meta property="og:image" content="https://hasibha.com/images/logo.png">
<meta property="og:site_name" content="${isEn ? 'Hasibha' : 'حاسبها'}">
<meta property="og:locale" content="${isEn ? 'en_US' : 'ar_SA'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${title}">
<meta name="twitter:description" content="${desc}">
<meta name="twitter:image" content="https://hasibha.com/images/logo.png">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "${title}",
  "description": "${desc}",
  "datePublished": "2026-11-25T00:00:00+03:00",
  "dateModified": "2026-11-25T00:00:00+03:00",
  "author": {
    "@type": "Organization",
    "name": "${authorName}",
    "url": "https://hasibha.com"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Hasibha",
    "url": "https://hasibha.com",
    "logo": {
      "@type": "ImageObject",
      "url": "https://hasibha.com/images/logo.png"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "${canonicalUrl}"
  },
  "inLanguage": "${isEn ? 'en-US' : 'ar-SA'}"
}
</script>
</head>
<body>
<header class="site-header">
  <div class="wrap header-in">
    <a class="logo" href="${isEn ? '/index-en' : '/'}" aria-label="حاسبها">
      <div class="logo-mark">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">
          <rect x="3" y="3" width="8" height="8" rx="2" fill="white" fill-opacity="0.95"/>
          <rect x="13" y="3" width="8" height="8" rx="2" fill="white" fill-opacity="0.45"/>
          <rect x="3" y="13" width="8" height="8" rx="2" fill="white" fill-opacity="0.45"/>
          <path d="M14 17H20M17 14V20" stroke="white" stroke-width="2.4" stroke-linecap="round"/>
        </svg>
      </div>
      <span class="logo-text">حاسبها</span>
      <span class="logo-badge">2026</span>
    </a>
    <nav class="main-nav" aria-label="Navigation">
      <a href="${isEn ? '/index-en#calculators' : '/#calculators'}">${isEn ? 'Calculators' : 'الحاسبات'}</a>
      <a href="${isEn ? '/articles/index-en' : '/articles/'}">${isEn ? 'Articles' : 'المقالات'}</a>
      <a href="${isEn ? '/about-en' : '/about'}">${isEn ? 'About' : 'من نحن'}</a>
      <a href="${isEn ? '/contact-en' : '/contact'}">${isEn ? 'Contact' : 'تواصل معنا'}</a>
    </nav>
    <div class="header-actions">
      <button class="theme-btn" id="themeBtn" type="button" aria-label="Theme"><svg class="i-moon" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg><svg class="i-sun" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
      <a class="lang-btn" href="${toggleUrl}" hreflang="${isEn ? 'ar' : 'en'}">${toggleLabel}</a>
    </div>
  </div>
</header>

<main>
<div class="wrap">
<article class="article">
<h1>${title}</h1>
<div class="article-meta">
<span>📅 ${art.date}</span>
<span>✍️ ${authorName}</span>
<span>⏱️ ${isEn ? art.readTimeEn : art.readTimeAr}</span>
</div>

${tocHtml}

${processedContent}

<div class="calc-box" style="margin-top:32px;background:var(--surface);border:1px solid var(--border);padding:24px;border-radius:16px;text-align:center;">
<h3 style="color:var(--text);">${ctaTitle}</h3>
<p style="color:var(--text-2);font-size:14px;margin-bottom:16px;">${ctaDesc}</p>
<a href="${ctaUrl}" class="cta-btn" style="display:inline-block;background:var(--accent);color:#fff;padding:10px 24px;border-radius:12px;font-weight:bold;text-decoration:none;">${ctaBtn}</a>
</div>

</article>
</div>
</main>

<footer class="site-footer">
  <div class="wrap footer-in">
    <div class="footer-brand">
      <a class="logo" href="${isEn ? '/index-en' : '/'}">
        <div class="logo-mark">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <rect x="3" y="3" width="8" height="8" rx="2" fill="white" fill-opacity="0.95"/>
            <rect x="13" y="3" width="8" height="8" rx="2" fill="white" fill-opacity="0.45"/>
            <rect x="3" y="13" width="8" height="8" rx="2" fill="white" fill-opacity="0.45"/>
            <path d="M14 17H20M17 14V20" stroke="white" stroke-width="2.4" stroke-linecap="round"/>
          </svg>
        </div>
        <span class="logo-text">حاسبها</span>
      </a>
      <p>${isEn ? "Saudi Arabia's comprehensive smart calculators platform with immediate results and total privacy." : 'منصتك السعودية الشاملة للحاسبات المالية، التحويلات، والقياسات الصحية بدقة فورية وخصوصية تامة.'}</p>
    </div>
    <div class="footer-col">
      <h4>${isEn ? 'Business Calculators' : 'حاسبات التجارة والأعمال'}</h4>
      <ul>
        <li><a href="${isEn ? '/ecommerce-profit-en' : '/ecommerce-profit'}">${isEn ? 'E-Commerce Profit' : 'صافي ربح المتاجر'}</a></li>
        <li><a href="${isEn ? '/import-cost-en' : '/import-cost'}">${isEn ? 'Landed Import Cost' : 'تكلفة الاستيراد الشاملة'}</a></li>
        <li><a href="${isEn ? '/pricing-calculator-en' : '/pricing-calculator'}">${isEn ? 'Pricing & Break-Even' : 'تسعير المنتجات والتعادل'}</a></li>
        <li><a href="${isEn ? '/roi-en' : '/roi'}">${isEn ? 'ROI Feasibility' : 'العائد على الاستثمار'}</a></li>
        <li><a href="${isEn ? '/shipping-weight-en' : '/shipping-weight'}">${isEn ? 'Shipping Weight' : 'الوزن الحجمي للشحن'}</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>${isEn ? 'Information' : 'روابط ومعلومات'}</h4>
      <p>${isEn ? 'All calculators run client-side in your browser with zero data collection. Updated for 2026 regulations.' : 'جميع الحاسبات تعمل محلياً في جهازك بدون تخزين بياناتك. النتائج استرشادية ومحدثة لأنظمة 2026.'}</p>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <p>حاسبها © 2026 — ${isEn ? 'All rights reserved' : 'جميع الحقوق محفوظة'}</p>
  </div>
</footer>

<script>
function toggleTheme(){var r=document.documentElement,t=r.getAttribute('data-theme')==='dark'?'light':'dark';if(t==='dark')r.setAttribute('data-theme','dark');else r.removeAttribute('data-theme');try{localStorage.setItem('hs-theme',t);}catch(e){}}
(function(){var t=null;try{t=localStorage.getItem('hs-theme');}catch(e){}if(!t)t=(matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'light';if(t==='dark')document.documentElement.setAttribute('data-theme','dark');})();
</script>
</body>
</html>`;
}

// Write the 10 article files
articlesData.forEach(art => {
  const arPath = path.join(articlesDir, `${art.slug}.html`);
  const enPath = path.join(articlesDir, `${art.slug}-en.html`);
  fs.writeFileSync(arPath, buildArticleHtml(art, false), 'utf8');
  fs.writeFileSync(enPath, buildArticleHtml(art, true), 'utf8');
  console.log(`✅ Generated ${art.slug}.html and ${art.slug}-en.html`);
});

// Update articles/index.html
const arArticlesIndex = path.join(articlesDir, 'index.html');
let arIndexHtml = fs.readFileSync(arArticlesIndex, 'utf8');

const newArCards = articlesData.map(art => `
<a class="article-card" href="/articles/${art.slug}">
<span class="date">📅 </span>
<h3>${art.titleAr}</h3>
<p>${art.descAr}</p>
<span class="read-more">اقرأ المقال ←</span>
</a>`).join('');

if (!arIndexHtml.includes('ecommerce-profit-guide-2026')) {
  arIndexHtml = arIndexHtml.replace('<div class="articles-grid">', '<div class="articles-grid">' + newArCards);
  fs.writeFileSync(arArticlesIndex, arIndexHtml, 'utf8');
  console.log('✅ Updated articles/index.html with 5 e-commerce articles');
}

// Update articles/index-en.html
const enArticlesIndex = path.join(articlesDir, 'index-en.html');
let enIndexHtml = fs.readFileSync(enArticlesIndex, 'utf8');

const newEnCards = articlesData.map(art => `
<a class="article-card" href="/articles/${art.slug}-en">
<span class="date">📅 </span>
<h3>${art.titleEn}</h3>
<p>${art.descEn}</p>
<span class="read-more">Read Article →</span>
</a>`).join('');

if (!enIndexHtml.includes('ecommerce-profit-guide-2026')) {
  enIndexHtml = enIndexHtml.replace('<div class="articles-grid">', '<div class="articles-grid">' + newEnCards);
  fs.writeFileSync(enArticlesIndex, enIndexHtml, 'utf8');
  console.log('✅ Updated articles/index-en.html with 5 e-commerce articles');
}

console.log('🚀 All 5 e-commerce guides successfully created!');
