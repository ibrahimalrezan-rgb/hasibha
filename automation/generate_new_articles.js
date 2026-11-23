const fs = require('fs');
const path = require('path');

const rootDir = 'C:/Users/ibrah/.gemini/antigravity/scratch/hasibha';
const articlesDir = path.join(rootDir, 'articles');

const articlesData = [
  {
    slug: 'gpa-guide-2026',
    calcUrl: '/gpa',
    calcUrlEn: '/gpa-en',
    date: '23 November 2026',
    readTimeAr: '8 دقائق قراءة',
    readTimeEn: '8 min read',
    titleAr: 'دليل حساب المعدل التراكمي (GPA) في السعودية 2026: الجامعات ونظام المسارات',
    descAr: 'دليل شامل ومفصل عن حساب المعدل الفصلي والتراكمي في الجامعات السعودية ونظام مسارات الثانوية 2026. أمثلة بالأرقام، شروط مرتبة الشرف، ووزن الساعات.',
    titleEn: 'Saudi GPA Calculation Guide 2026: Universities & High School Tracks',
    descEn: 'Comprehensive guide to calculating semester and cumulative GPA in Saudi universities and high school tracks (out of 4 and 5). Formulas, honors, and examples.',
    keywordsAr: 'حساب المعدل التراكمي, معدل الجامعة من 5, معدل من 4, نظام المسارات, مرتبة الشرف في الجامعات السعودية, حساب نقاط المواد',
    keywordsEn: 'gpa calculator saudi, cumulative gpa out of 5, university gpa ksa, high school tracks gpa, saudi grading scale',
    ctaTitleAr: 'جرب حاسبة المعدل التراكمي الذكية',
    ctaDescAr: 'احسب معدلك الفصلي والتراكمي من 4 أو من 5 ودرجات المواد بدقة فورية',
    ctaBtnAr: 'افتح حاسبة المعدل ←',
    ctaTitleEn: 'Try the Smart GPA Calculator',
    ctaDescEn: 'Calculate your semester and cumulative GPA out of 4 or 5 instantly',
    ctaBtnEn: 'Open GPA Calculator →',
    contentAr: `
<h2>مقدمة عن المعدل التراكمي (GPA) وأهميته الأكاديمية</h2>
<p>يُمثل <strong>المعدل التراكمي (Grade Point Average - GPA)</strong> المعيار الأكاديمي الأول لقياس تحصيل الطالب طوال مسيرته الدراسية، سواء في الجامعات السعودية أو في المرحلة الثانوية الحديثة وفق <strong>نظام المسارات</strong>. ولا تقتصر أهمية المعدل على التخرج فحسب، بل يحدد أهليتك لمرتبة الشرف، المنح والابتعاث الخارجي، والفرص الوظيفية المرموقة في سوق العمل السعودي المتسارع نحو رؤية 2030.</p>
<p>في هذا الدليل العملي لعام 2026، نشرح بالتفصيل معادلات حساب المعدل من 5 (المعمول به في جامعة الملك سعود، جامعة الملك عبد العزيز، وجامعة الإمام) والمعدل من 4 (المعمول به في جامعة البترول والمعادن والجامعات الأهلية)، مع إيضاح طريقة حساب معدل نظام المسارات ووزن الساعات المعتمدة.</p>

<h2>الفرق بين النظامين: مقياس 5.0 ومقياس 4.0</h2>
<p>تعتمد الجامعات السعودية أحد المقياسين التاليين لتحويل الدرجات المئوية إلى نقاط رقمية:</p>
<table class="article-table">
  <thead>
    <tr>
      <th>التقدير الحرفي</th>
      <th>الدرجة المئوية</th>
      <th>نقاط المقياس (5.0)</th>
      <th>نقاط المقياس (4.0)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>أ+ (A+)</td><td>95 - 100</td><td>5.00</td><td>4.00</td></tr>
    <tr><td>أ (A)</td><td>90 - أقل من 95</td><td>4.75</td><td>3.75</td></tr>
    <tr><td>ب+ (B+)</td><td>85 - أقل من 90</td><td>4.50</td><td>3.50</td></tr>
    <tr><td>ب (B)</td><td>80 - أقل من 85</td><td>4.00</td><td>3.00</td></tr>
    <tr><td>ج+ (C+)</td><td>75 - أقل من 80</td><td>3.50</td><td>2.50</td></tr>
    <tr><td>ج (C)</td><td>70 - أقل من 75</td><td>3.00</td><td>2.00</td></tr>
    <tr><td>د+ (D+)</td><td>65 - أقل من 70</td><td>2.50</td><td>1.50</td></tr>
    <tr><td>د (D)</td><td>60 - أقل من 65</td><td>2.00</td><td>1.00</td></tr>
    <tr><td>هـ (F)</td><td>أقل من 60 (راسب)</td><td>1.00 / 0.00</td><td>0.00</td></tr>
  </tbody>
</table>

<h2>المعادلة الرياضية لحساب المعدل الفصلي والتراكمي</h2>
<p>لحساب المعدل الفصلي بدقة، نطبق المعادلة الرياضية المعتمدة في اللائحة الموحدة للجامعات:</p>
<blockquote style="background:#f1f5f9;padding:16px;border-right:4px solid #059669;border-radius:8px;margin:20px 0;">
  <strong>المعدل الفصلي = مجموع (نقاط المادة × عدد ساعاتها المعتمدة) ÷ إجمالي عدد الساعات المعتمدة في الفصل</strong>
</blockquote>

<h3>مثال تطبيقي عملي:</h3>
<p>طالب درس 4 مواد في الفصل الدراسي الأول:</p>
<ul>
  <li><strong>مادة الرياضيات (3 ساعات):</strong> حصل على أ+ (5.0 نقاط) ➦ النقاط المكتسبة = 3 × 5.0 = 15 نقطة.</li>
  <li><strong>مادة الفيزياء (4 ساعات):</strong> حصل على ب+ (4.5 نقاط) ➦ النقاط المكتسبة = 4 × 4.5 = 18 نقطة.</li>
  <li><strong>مادة الإنجليزي (3 ساعات):</strong> حصل على أ (4.75 نقطة) ➦ النقاط المكتسبة = 3 × 4.75 = 14.25 نقطة.</li>
  <li><strong>مادة الثقافة الإسلامية (2 ساعة):</strong> حصل على أ+ (5.0 نقاط) ➦ النقاط المكتسبة = 2 × 5.0 = 10 نقاط.</li>
</ul>
<p>إجمالي النقاط = 15 + 18 + 14.25 + 10 = <strong>57.25 نقطة</strong>.<br>
إجمالي الساعات = 3 + 4 + 3 + 2 = <strong>12 ساعة معتمدة</strong>.<br>
<strong>المعدل الفصلي = 57.25 ÷ 12 = 4.77 من 5.00 (ممتاز مرتفع)</strong>.</p>

<h2>كيف يُحسب المعدل في نظام مسارات الثانوية العامة؟</h2>
<p>في نظام المسارات التابع لوزارة التعليم السعودية، يتم توزيع وزن الساعات لجميع المواد في كل فصل دراسي من الفصول الثلاثة. المواد ذات الحصص الأكبر (مثل الرياضيات والعلوم واللغة الإنجليزية) تمتلك تأثيراً مضاعفاً على المعدل مقارنة بالمواد ذات الحصة الواحدة. لذلك فإن التركيز على رفع درجات المواد ذات الساعات العالية هو المفتاح الأسرع لرفع المعدل التراكمي العام.</p>

<h2>شروط مرتبة الشرف في الجامعات السعودية</h2>
<p>وفق اللائحة الموحدة للدراسات الجامعية في المملكة:</p>
<ol>
  <li><strong>مرتبة الشرف الأولى:</strong> تُمنح للطالب الحاصل على معدل تراكمي من (4.75 إلى 5.00) أو من (3.75 إلى 4.00) عند التخرج.</li>
  <li><strong>مرتبة الشرف الثانية:</strong> تُمنح للطالب الحاصل على معدل تراكمي من (4.25 إلى أقل من 4.75) أو من (3.25 إلى أقل من 3.75).</li>
  <li><strong>الشرط الجوهري:</strong> ألا يكون الطالب قد رسب في أي مقرر درسه في جامعته أو في جامعة أخرى محولة.</li>
</ol>
`,
    contentEn: `
<h2>Introduction to GPA & Academic Standing</h2>
<p>The <strong>Grade Point Average (GPA)</strong> serves as the primary benchmark for academic evaluation across Saudi universities and the secondary education <strong>Pathways (Masarat) system</strong>. In 2026, academic performance directly impacts honors classification, scholarship programs, and high-demand corporate career opportunities throughout the Kingdom.</p>

<h2>Grading Scales: 5.0 vs 4.0 Systems</h2>
<p>Saudi academic institutions generally utilize either a 5.0 scale (standard at King Saud University, King Abdulaziz University, and Imam Mohammad Ibn Saud University) or a 4.0 scale (used at KFUPM and private universities):</p>
<table class="article-table">
  <thead>
    <tr>
      <th>Letter Grade</th>
      <th>Percentage Range</th>
      <th>5.0 Points</th>
      <th>4.0 Points</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>A+</td><td>95 - 100</td><td>5.00</td><td>4.00</td></tr>
    <tr><td>A</td><td>90 - 94</td><td>4.75</td><td>3.75</td></tr>
    <tr><td>B+</td><td>85 - 89</td><td>4.50</td><td>3.50</td></tr>
    <tr><td>B</td><td>80 - 84</td><td>4.00</td><td>3.00</td></tr>
    <tr><td>C+</td><td>75 - 79</td><td>3.50</td><td>2.50</td></tr>
    <tr><td>C</td><td>70 - 74</td><td>3.00</td><td>2.00</td></tr>
    <tr><td>D+</td><td>65 - 69</td><td>2.50</td><td>1.50</td></tr>
    <tr><td>D</td><td>60 - 64</td><td>2.00</td><td>1.00</td></tr>
    <tr><td>F</td><td>Below 60</td><td>0.00</td><td>0.00</td></tr>
  </tbody>
</table>

<h2>Calculation Formula</h2>
<blockquote style="background:#f1f5f9;padding:16px;border-left:4px solid #059669;border-radius:8px;margin:20px 0;">
  <strong>Semester GPA = Sum of (Course Points × Credit Hours) ÷ Total Credit Hours</strong>
</blockquote>
<p>Cumulative GPA reflects the aggregated points earned across all academic semesters divided by total completed credit hours.</p>
`
  },
  {
    slug: 'electricity-guide-2026',
    calcUrl: '/electricity',
    calcUrlEn: '/electricity-en',
    date: '23 November 2026',
    readTimeAr: '9 دقائق قراءة',
    readTimeEn: '9 min read',
    titleAr: 'دليل فاتورة الكهرباء والشرائح السكنية في السعودية 2026: الحساب وطرق التوفير',
    descAr: 'دليل شامل ومفصل عن تعريفة وشرائح استهلاك الكهرباء السكني في السعودية 2026. طريقة حساب الفاتورة، قراءة العداد الذكي، ونصائح تخفيض الاستهلاك صيفاً.',
    titleEn: 'Saudi Electricity Bill & Tariffs Guide 2026: Slices, Calculation & Tips',
    descEn: 'Comprehensive guide to Saudi Electricity Company (SEC) residential consumption tariffs, smart meter readings, VAT calculation, and summer power-saving strategies.',
    keywordsAr: 'فاتورة الكهرباء السعودية, شرائح الكهرباء السكنية 2026, حساب استهلاك الكهرباء, العداد الذكي, تخفيض فاتورة الكهرباء, استهلاك المكيفات',
    keywordsEn: 'saudi electricity bill, sec residential tariffs, kwh calculation ksa, smart electricity meter, summer electricity bill saudi',
    ctaTitleAr: 'جرب حاسبة فاتورة الكهرباء السعودية',
    ctaDescAr: 'احسب قيمة فاتورتك الدقيقة وفق شرائح الشركة السعودية للكهرباء مع الضريبة',
    ctaBtnAr: 'افتح حاسبة الكهرباء ←',
    ctaTitleEn: 'Try Saudi Electricity Bill Calculator',
    ctaDescEn: 'Calculate your exact residential SEC bill across consumption brackets with 15% VAT',
    ctaBtnEn: 'Open Electricity Calculator →',
    contentAr: `
<h2>مقدمة عن قطاع الكهرباء في السعودية</h2>
<p>تشهد المملكة العربية السعودية تحولاً تقنياً واسعاً في منظومة الطاقة وإدارة العدادات الذكية تحت إشراف <strong>هيئة تنظيم المياه والكهرباء</strong> والشركة السعودية للكهرباء (SEC). ومع ارتفاع درجات الحرارة خلال أشهر الصيف الطويلة، يصبح استهلاك الطاقة التحدي المالي الأكبر للأسر السعودية، حيث تمثل أجهزة التكييف أكثر من 65% إلى 70% من إجمالي استهلاك المبنى السكني.</p>
<p>في هذا الدليل لعام 2026، نكشف لك التركيبة الدقيقة لشرائح الاستهلاك، والحد الفاصل بين الشريحة الأولى والشريحة الثانية، وطريقة حساب ضريبة القيمة المضافة 15% ومقابل خدمة العداد.</p>

<h2>جدول شرائح الاستهلاك السكني المعتمدة 2026</h2>
<p>تُحسب تعرفة الكهرباء للقطاع السكني في المملكة بنظام الشرائح التصاعدية لحث المستهلكين على الترشيد:</p>
<table class="article-table">
  <thead>
    <tr>
      <th>الشريحة</th>
      <th>كمية الاستهلاك الشهري (كيلوواط.ساعة)</th>
      <th>سعر الكيلوواط الواحد</th>
      <th>الحد الأقصى لتكلفة الطاقة في الشريحة</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>الشريحة الأولى (المدعومة)</strong></td>
      <td>من 1 إلى 6,000 ك.و.س</td>
      <td><strong>18 هللة / ك.و.س</strong></td>
      <td>1,080 ريال سعودي</td>
    </tr>
    <tr>
      <td><strong>الشريحة الثانية</strong></td>
      <td>أكثر من 6,000 ك.و.س</td>
      <td><strong>30 هللة / ك.و.س</strong></td>
      <td>تُحسب كل وحدة إضافية بـ 30 هللة</td>
    </tr>
  </tbody>
</table>

<h2>مكونات الفاتورة الشهرية الرسمية</h2>
<p>لا تتكون فاتورة الكهرباء من استهلاك الطاقة فحسب، بل تشمل 3 بنود رئيسية:</p>
<ol>
  <li><strong>تكلفة استهلاك الطاقة (الطاقة المستهلكة):</strong> ناتج ضرب عدد الكيلوواط في سعر الشريحة (18 هللة أو 30 هللة).</li>
  <li><strong>مقابل خدمة العداد:</strong> رسوم شهرية ثابتة تعتمد على سعة القاطع الكهربائي للمنزل (تتراوح غالباً بين 10 إلى 30 ريالاً لمعظم المنازل).</li>
  <li><strong>ضريبة القيمة المضافة (15%):</strong> تُضاف على إجمالي استهلاك الطاقة ومقابل خدمة العداد معاً.</li>
</ol>

<h2>طريقة حساب الفاتورة عملياً (مثال توضيحي بالأرقام)</h2>
<p>افترض أن استهلاك منزلك في شهر يوليو بلغ <strong>7,500 كيلوواط.ساعة</strong> وقاطع العداد 60 أمبير (خدمة العداد 15 ريالاً):</p>
<ul>
  <li>الشريحة الأولى (6000 ك.و.س): 6,000 × 0.18 = <strong>1,080 ريال</strong>.</li>
  <li>الشريحة الثانية (1500 ك.و.س المتبقية): 1,500 × 0.30 = <strong>450 ريال</strong>.</li>
  <li>إجمالي استهلاك الطاقة = 1,080 + 450 = <strong>1,530 ريال</strong>.</li>
  <li>إضافة مقابل خدمة العداد = 1,530 + 15 = <strong>1,545 ريال</strong> (المبلغ الخاضع للضريبة).</li>
  <li>ضريبة القيمة المضافة 15% = 1,545 × 0.15 = <strong>231.75 ريال</strong>.</li>
  <li><strong>إجمالي الفاتورة المطلوب سدادها = 1,776.75 ريال سعودي</strong>.</li>
</ul>

<h2>أقوى 5 نصائح لتفادي الانتقال إلى الشريحة الثانية (30 هللة)</h2>
<ol>
  <li><strong>ضبط درجة حرارة المكيف على 24 درجة مئوية:</strong> كل درجة واحدة تخفضها عن 24 تزيد استهلاك الطاقة بنسبة 5% إلى 7%.</li>
  <li><strong>صيانة وتنظيف فلاتر المكيف دورياً كل أسبوعين:</strong> تراكم الغبار يجبر الضاغط (الكمبروسر) على العمل بطاقة قصوى مستمرة.</li>
  <li><strong>استخدام العزل الحراري والستائر العاكسة:</strong> عزل النوافذ والأسطح يقلل الحمل الحراري داخل الغرف بنسبة تصل إلى 40%.</li>
  <li><strong>استبدال الإنارة بـ تقنية LED:</strong> توفر حتى 80% من طاقة الإنارة ولا تصدر حرارة داخل المنزل.</li>
  <li><strong>متابعة العداد الذكي عبر تطبيق الكهرباء:</strong> مراقبة منحنى الاستهلاك الأسبوعي للتأكد من عدم تجاوز حاجز 6000 وحدة قبل نهاية دورة الفوترة.</li>
</ol>
`,
    contentEn: `
<h2>Understanding the Saudi Residential Electricity Tariff</h2>
<p>Residential electricity in Saudi Arabia operates on a tiered billing structure managed by the <strong>Saudi Electricity Company (SEC)</strong> under regulatory oversight by the Water and Electricity Regulatory Authority.</p>

<h2>Residential Consumption Brackets 2026</h2>
<table class="article-table">
  <thead>
    <tr>
      <th>Tier Bracket</th>
      <th>Monthly Consumption (kWh)</th>
      <th>Rate per kWh</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Tier 1 (Subsidized)</td><td>1 - 6,000 kWh</td><td>SAR 0.18 / kWh</td></tr>
    <tr><td>Tier 2</td><td>Above 6,000 kWh</td><td>SAR 0.30 / kWh</td></tr>
  </tbody>
</table>

<h2>Bill Breakdown & VAT</h2>
<p>The total monthly invoice includes:</p>
<ul>
  <li>Energy consumption cost across tiers.</li>
  <li>Meter service charge based on circuit breaker capacity (typically SAR 10 - SAR 30).</li>
  <li>15% Value Added Tax (VAT) applied to the subtotal.</li>
</ul>
`
  },
  {
    slug: 'sakani-guide-2026',
    calcUrl: '/sakani',
    calcUrlEn: '/sakani-en',
    date: '23 November 2026',
    readTimeAr: '10 دقائق قراءة',
    readTimeEn: '10 min read',
    titleAr: 'دليل الدعم السكني (سكني) 2026: شروط الاستحقاق ومصفوفة الدعم المالي',
    descAr: 'دليل شامل ومفصل عن برنامج الدعم السكني في السعودية 2026. مصفوفة الدعم المالي، شروط استحقاق الدعم المحدثة، باقات الدعم غير المسترد 100 ألف و150 ألف.',
    titleEn: 'Sakani Housing Support Guide 2026: Eligibility, Matrix & Grants',
    descEn: 'Complete guide to Saudi Sakani housing support programs, monthly mortgage subsidy matrix, 100k-150k non-refundable grants, and Ministry of Housing criteria.',
    keywordsAr: 'الدعم السكني 2026, شروط استحقاق سكني, مصفوفة الدعم المالي, باقة الدعم الفوري 150 الف, حاسبة التمويل العقاري المدعوم, الصندوق العقاري',
    keywordsEn: 'sakani housing support ksa, saudi mortgage subsidy, real estate development fund redf, non refundable housing grant, sakani eligibility',
    ctaTitleAr: 'جرب حاسبة الدعم السكني (سكني)',
    ctaDescAr: 'احسب نسبة وقيمة الدعم المالي الشهري والدعم الفوري المتاح لك وفق راتبك',
    ctaBtnAr: 'افتح حاسبة سكني ←',
    ctaTitleEn: 'Try Sakani Housing Support Calculator',
    ctaDescEn: 'Calculate your exact monthly subsidy and instant grant options based on your salary',
    ctaBtnEn: 'Open Sakani Calculator →',
    contentAr: `
<h2>مقدمة عن برنامج «سكني» وصندوق التنمية العقارية</h2>
<p>يُمثل برنامج <strong>الدعم السكني (سكني)</strong> بالشراكة مع <strong>صندوق التنمية العقارية (REDF)</strong> والبنوك السعودية ركيزة التحول الإسكاني ضمن رؤية 2030 لرفع نسبة تملك المواطنين للمساكن إلى أكثر من 70%. وقد شهد البرنامج تحديثات جوهرية في مصفوفة الدعم والحلول التمويلية لتناسب مختلف مستويات الدخل وتسهيل الحصول على المسكن الأول.</p>
<p>في هذا الدليل لعام 2026، نستعرض شروط الأهلية، أنواع الدعم السكني (الدعم العيني، الدعم المالي الشهري للأرباح، وباقة الدعم المالي المباشر غير المسترد بقيمة 100 ألف أو 150 ألف ريال)، مع توضيح الفئات المستهدفة وحاسبة الاستحقاق.</p>

<h2>شروط استحقاق الدعم السكني للمواطنين 2026</h2>
<p>حددت اللائحة التنفيذية لبرنامج الدعم السكني مجموعة من الشروط الأساسية التي يجب توفرها في المتقدم والأسرة:</p>
<ol>
  <li><strong>الجنسية والإقامة:</strong> أن يكون المتقدم سعودي الجنسية، ومقيماً إقامة دائمة داخل المملكة.</li>
  <li><strong>تكوين الأسرة:</strong> أن تتكون الأسرة من (زوج وزوجة، أو أب وأولاده، أو أم مطلقة أو أرملة تعول أولادها).</li>
  <li><strong>شرط السن:</strong> ألا يقل عمر المتقدم عن 25 سنة (ما لم يكن زوجاً أو عائلاً لأسرة).</li>
  <li><strong>عدم امتلاك مسكن مناسب:</strong> ألا يكون لدى الأسرة مسكن مناسب أو سبق لها امتلاك مسكن خلال الـ 5 سنوات السابقة لتاريخ تقديم الطلب.</li>
  <li><strong>عدم الاستفادة السابقة:</strong> ألا يكون أحد أفراد الأسرة قد استفاد مسبقاً من أي برنامج دعم سكني حكومي أو خاص.</li>
</ol>

<h2>خيارات وباقات الدعم السكني المتاحة</h2>
<p>يوفر برنامج سكني عدة مسارات تمويلية لتلبية احتياجات المستفيدين المتنوعة:</p>

<h3>1. باقة الدعم الفوري غير المسترد (100,000 - 150,000 ريال)</h3>
<p>تُعد من أكثر الخيارات إقبالاً، حيث يحصل المستفيد على مبلغ مالي مباشر غير مسترد يُودع في حسابه عند توقيع عقد التمويل العقاري مع البنك، ويُستخدم كدفعة أولى لتملك الوحدة السكنية (شراء جاهز، بناء ذاتي، أو شراء على الخارطة).</p>

<h3>2. دعم أرباح التمويل العقاري (المصفوفة الشهرية)</h3>
<p>يقوم الصندوق العقاري بسداد نسبة من أرباح القرض العقاري شهرياً نيابة عن المستفيد بناءً على مصفوفة الدخل:</p>
<ul>
  <li><strong>الراتب الأساسي حتى 14,000 ريال:</strong> يحصل المستفيد على <strong>دعم بنسبة 100%</strong> لأرباح مبلغ التمويل الذي يصل إلى 500,000 ريال.</li>
  <li><strong>الراتب أعلى من 14,000 ريال:</strong> تتدرج نسبة الدعم من 95% حتى 70% بحسب عدد أفراد الأسرة وإجمالي الدخل الشهري.</li>
</ul>

<h3>3. مبادرة تحمل ضريبة التصرفات العقارية عن المسكن الأول</h3>
<p>تتحمل الدولة ضريبة التصرفات العقارية بنسبة 5% نيابة عن المواطن المستفيد لتملك المسكن الأول حتى مبلغ مليون ريال من قيمة العقار.</p>
`,
    contentEn: `
<h2>About the Saudi Sakani Housing Program</h2>
<p>The <strong>Sakani Program</strong>, operated by the Ministry of Housing in coordination with the <strong>Real Estate Development Fund (REDF)</strong>, empowers Saudi citizens to acquire their first primary residence under Vision 2030 homeownership initiatives.</p>

<h2>Core Eligibility Criteria</h2>
<ul>
  <li>Saudi citizenship and permanent residency within KSA.</li>
  <li>Family composition (spouses, dependent children, or single mothers/widows).</li>
  <li>Minimum age of 25 years for standalone applicants.</li>
  <li>No primary home ownership during the preceding 5 years.</li>
  <li>No prior benefit from public housing subsidy programs.</li>
</ul>

<h2>Subsidized Support Options</h2>
<ol>
  <li><strong>Non-refundable Instant Grants:</strong> Direct financial grants ranging from SAR 100,000 to SAR 150,000.</li>
  <li><strong>Monthly Profit Subsidies:</strong> Matrix-based subsidy covering up to 100% of mortgage loan profits for salaries up to SAR 14,000 on financing amounts up to SAR 500,000.</li>
  <li><strong>Real Estate Transaction Tax (RETT) Relief:</strong> Exemption on up to SAR 1,000,000 for primary residential properties.</li>
</ol>
`
  },
  {
    slug: 'leave-allowance-guide-2026',
    calcUrl: '/leave-allowance',
    calcUrlEn: '/leave-allowance-en',
    date: '23 November 2026',
    readTimeAr: '9 دقائق قراءة',
    readTimeEn: '9 min read',
    titleAr: 'دليل رصيد وبدل الإجازة السنوية في نظام العمل السعودي 2026: الحساب والتسييل النقدي',
    descAr: 'دليل شامل ومفصل عن رصيد وبدل الإجازات السنوية في السعودية 2026 وفق المواد 109 و111 من نظام العمل. طريقة احتساب أجر الإجازة، التعويض النقدي، وشروط الترحيل.',
    titleEn: 'Saudi Annual Leave Allowance Guide 2026: Labor Law Articles 109 & 111',
    descEn: 'Comprehensive guide to annual leave entitlements, cash compensation for unused balances, encashment formulas, and labor law regulations in Saudi Arabia.',
    keywordsAr: 'بدل الإجازة السنوية, رصيد الإجازات في نظام العمل السعودي, المادة 109 نظام العمل, المادة 111, تسييل رصيد الإجازات, حساب أجر يوم الإجازة',
    keywordsEn: 'saudi annual leave allowance, unused leave encashment ksa, saudi labor law article 109, leave salary calculation, annual vacation compensation',
    ctaTitleAr: 'جرب حاسبة بدل الإجازة السنوية',
    ctaDescAr: 'احسب قيمة رصيد إجازاتك غير المستنفدة والبدل النقدي المستحق وفق نظام العمل',
    ctaBtnAr: 'افتح حاسبة بدل الإجازة ←',
    ctaTitleEn: 'Try Annual Leave Allowance Calculator',
    ctaDescEn: 'Calculate your exact cash compensation for unused annual leave days per Saudi Labor Law',
    ctaBtnEn: 'Open Leave Calculator →',
    contentAr: `
<h2>مفهوم الإجازة السنوية في نظام العمل السعودي</h2>
<p>تُعد <strong>الإجازة السنوية مدفوعة الأجر</strong> حقاً أساسياً كفله <strong>نظام العمل السعودي</strong> للعامل لحمايته من الإجهاد البدني والذهني. ونظراً لأهميتها في العلاقة التعاقدية، فقد حدد النظام ضوابط دقيقة لمدتها، وأجرها، وطريقة تعويض العامل نقدياً عن أي رصيد إجازات غير مستخدم في نهاية خدمته أو أثناء سريان العقد.</p>
<p>في هذا الدليل لعام 2026، نشرح نصوص المواد 109، 110، و111 من نظام العمل، مع أمثلة عملية توضح كيف يتم احتساب الأجر اليومي والبدل النقدي المستحق بالأرقام.</p>

<h2>مدة الإجازة السنوية المستحقة (المادة 109)</h2>
<p>تنص المادة 109 من نظام العمل السعودي على ما يلي:</p>
<ol>
  <li><strong>21 يوماً مدفوعة الأجر:</strong> كحد أدنى عن كل عام خدمة إذا كانت مدة خدمة العامل لدى صاحب العمل أقل من 5 سنوات متصلة.</li>
  <li><strong>30 يوماً مدفوعة الأجر:</strong> ترتفع تلقائياً إلى ثلاثين يوماً إذا أمضى العامل 5 سنوات متصلة أو أكثر في خدمة صاحب العمل نفسه.</li>
  <li><strong>أجر الإجازة:</strong> يُدفع للعامل أجره عن أيام الإجازة مقدماً قبل قيامه بها، ويُحسب على أساس <strong>الأجر الفعلي (الراتب الإجمالي شاملاً الأساسي والبدلات الثابتة)</strong> وليس الراتب الأساسي فقط.</li>
</ol>

<h2>التعويض النقدي عن رصيد الإجازات (المادة 111)</h2>
<p>توضح المادة 111 من النظام حق العامل في الحصول على تعويض مالي مباشر عن إجازاته:</p>
<blockquote style="background:#f1f5f9;padding:16px;border-right:4px solid #059669;border-radius:8px;margin:20px 0;">
  <strong>«للعامل الحق في الحصول على أجر عن أيام الإجازة المستحقة إذا ترك العمل قبل استعماله لها، وذلك بالنسبة إلى المدة التي لم يحصل على إجازته عنها، كما يستحق أجر الإجازة عن أجزاء السنة بنسبة ما قضاه منها في العمل.»</strong>
</blockquote>

<h2>المعادلة الحسابية للبدل النقدي لرصيد الإجازات</h2>
<p>يتم احتساب البدل المالي عبر الخطوات التالية:</p>
<ol>
  <li><strong>حساب أجر اليوم الواحد:</strong><br>
  <code>أجر اليوم = الراتب الفعلي الشهري (الإجمالي) ÷ 30 يوماً</code></li>
  <li><strong>حساب البدل النقدي الإجمالي:</strong><br>
  <code>البدل النقدي = عدد أيام الإجازة المستحقة غير المستنفدة × أجر اليوم الواحد</code></li>
</ol>

<h3>مثال تطبيقي عملي:</h3>
<p>موظف راتبه الإجمالي 9,000 ريال شهرياً، ولديه رصيد إجازات غير مستنفدة قدره 15 يوماً عند استقالته:</p>
<ul>
  <li>أجر اليوم الواحد = 9,000 ÷ 30 = <strong>300 ريال / يوم</strong>.</li>
  <li>البدل النقدي المستحق = 15 يوماً × 300 = <strong>4,500 ريال سعودي</strong>.</li>
</ul>
<p>يُصرف هذا المبلغ إلزامياً ضمن مستحقات التصفية النهائية مع مكافأة نهاية الخدمة فور انتهاء العلاقة العمالية.</p>
`,
    contentEn: `
<h2>Annual Leave Entitlements under Saudi Labor Law</h2>
<p>Annual leave is an inalienable statutory right established under the <strong>Saudi Labor Law</strong> to guarantee rest and work-life balance for all private sector employees.</p>

<h2>Statutory Durations (Article 109)</h2>
<ul>
  <li><strong>21 Days with Full Pay:</strong> Minimum entitlement for employees with less than 5 consecutive years of service.</li>
  <li><strong>30 Days with Full Pay:</strong> Applicable once the employee completes 5 consecutive years of continuous employment with the same employer.</li>
  <li><strong>Calculation Basis:</strong> Calculated on the employee's <em>actual full wage</em> (basic salary plus fixed allowances), payable prior to leave commencement.</li>
</ul>

<h2>Cash Encashment of Unused Leave (Article 111)</h2>
<p>Under Article 111, upon contract termination or resignation, employees are entitled to full cash compensation for any accrued, unused leave balance corresponding to their period of service.</p>
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
  const authorName = isEn ? 'Hasibha Editorial Team' : 'فريق حاسبها';
  const homeLabel = isEn ? 'Home' : 'الرئيسية';
  const articlesLabel = isEn ? 'Articles' : 'المقالات';

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
  "datePublished": "2026-11-23T00:00:00+03:00",
  "dateModified": "2026-11-23T00:00:00+03:00",
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

${content}

<div class="calc-box" style="margin-top:32px;background:#f8fafc;border:1px solid #e2e8f0;padding:24px;border-radius:16px;text-align:center;">
<h3>${ctaTitle}</h3>
<p style="color:#64748b;font-size:14px;margin-bottom:16px;">${ctaDesc}</p>
<a href="${ctaUrl}" class="cta-btn" style="display:inline-block;background:#059669;color:#fff;padding:10px 24px;border-radius:12px;font-weight:bold;text-decoration:none;">${ctaBtn}</a>
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
      <h4>${isEn ? 'Quick Calculators' : 'حاسبات سريعة'}</h4>
      <ul>
        <li><a href="${isEn ? '/vat-en' : '/vat'}">${isEn ? 'VAT Calculator' : 'ضريبة القيمة المضافة'}</a></li>
        <li><a href="${isEn ? '/salary-en' : '/salary'}">${isEn ? 'Salary & GOSI' : 'الراتب بعد التأمينات'}</a></li>
        <li><a href="${isEn ? '/mortgage-en' : '/mortgage'}">${isEn ? 'Mortgage' : 'التمويل العقاري'}</a></li>
        <li><a href="${isEn ? '/eos-en' : '/eos'}">${isEn ? 'End of Service' : 'نهاية الخدمة'}</a></li>
        <li><a href="${isEn ? '/gpa-en' : '/gpa'}">${isEn ? 'GPA Calculator' : 'حساب المعدل'}</a></li>
        <li><a href="${isEn ? '/electricity-en' : '/electricity'}">${isEn ? 'Electricity Bill' : 'فاتورة الكهرباء'}</a></li>
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

// Write the 8 article files
articlesData.forEach(art => {
  const arPath = path.join(articlesDir, `${art.slug}.html`);
  const enPath = path.join(articlesDir, `${art.slug}-en.html`);
  fs.writeFileSync(arPath, buildArticleHtml(art, false), 'utf8');
  fs.writeFileSync(enPath, buildArticleHtml(art, true), 'utf8');
  console.log(`✅ Generated ${art.slug}.html and ${art.slug}-en.html`);
});

// Update articles/index.html to include all 4 new articles
const arArticlesIndex = path.join(articlesDir, 'index.html');
let arIndexHtml = fs.readFileSync(arArticlesIndex, 'utf8');

const newArCards = articlesData.map(art => `
<a class="article-card" href="/articles/${art.slug}">
<span class="date">📅 </span>
<h3>${art.titleAr}</h3>
<p>${art.descAr}</p>
<span class="read-more">اقرأ المقال ←</span>
</a>`).join('');

if (!arIndexHtml.includes('gpa-guide-2026')) {
  arIndexHtml = arIndexHtml.replace('<div class="articles-grid">', '<div class="articles-grid">' + newArCards);
  fs.writeFileSync(arArticlesIndex, arIndexHtml, 'utf8');
  console.log('✅ Updated articles/index.html with new articles');
}

// Update articles/index-en.html to include all 4 new articles
const enArticlesIndex = path.join(articlesDir, 'index-en.html');
let enIndexHtml = fs.readFileSync(enArticlesIndex, 'utf8');

const newEnCards = articlesData.map(art => `
<a class="article-card" href="/articles/${art.slug}-en">
<span class="date">📅 </span>
<h3>${art.titleEn}</h3>
<p>${art.descEn}</p>
<span class="read-more">Read Article →</span>
</a>`).join('');

if (!enIndexHtml.includes('gpa-guide-2026')) {
  enIndexHtml = enIndexHtml.replace('<div class="articles-grid">', '<div class="articles-grid">' + newEnCards);
  fs.writeFileSync(enArticlesIndex, enIndexHtml, 'utf8');
  console.log('✅ Updated articles/index-en.html with new articles');
}

console.log('🚀 All 4 comprehensive guides generated and index files updated!');
