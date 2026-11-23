const fs = require('fs');
const path = require('path');

const rootDir = 'C:/Users/ibrah/.gemini/antigravity/scratch/hasibha';
const indexPath = path.join(rootDir, 'index.html');
const indexEnPath = path.join(rootDir, 'index-en.html');

let indexHtml = fs.readFileSync(indexPath, 'utf8');
let indexEnHtml = fs.readFileSync(indexEnPath, 'utf8');

const newArArticles = `,
      {
        id: 'art-gpa',
        url: '/articles/gpa-guide-2026',
        tag: 'التعليم والجامعات',
        readTime: '3 دقائق قراءة',
        title: 'دليل حساب المعدل التراكمي (GPA) 2026: الجامعات ونظام المسارات',
        excerpt: 'شرح حساب المعدل الفصلي والتراكمي من 4 ومن 5، وزن الساعات المعتمدة، وشروط مرتبة الشرف.',
        calcId: 'gpa',
        paragraphs: [
          'يُحسب المعدل الفصلي بضرب نقاط كل مقرر في عدد ساعاته المعتمدة، ثم قسمة المجموع الكلي للنقاط على إجمالي الساعات.',
          'في نظام مسارات الثانوية العامة والجامعات، التركيز على رفع درجات المقررات ذات الساعات العالية هو المفتاح الأسرع لرفع المعدل التراكمي.'
        ]
      },
      {
        id: 'art-electricity',
        url: '/articles/electricity-guide-2026',
        tag: 'الفواتير والطاقة',
        readTime: '3 دقائق قراءة',
        title: 'فاتورة الكهرباء والشرائح السكنية 2026: كيف تتفادى الشريحة الثانية؟',
        excerpt: 'تعرف على الفرق بين تعرفة 18 هللة و30 هللة، وطريقة حساب ضريبة 15% ومقابل خدمة العداد.',
        calcId: 'electricity',
        paragraphs: [
          'تُحسب الشريحة الأولى المدعومة بـ 18 هللة لكل كيلوواط حتى 6000 وحدة، وما زاد عنها يُحسب بـ 30 هللة لكل وحدة إضافية.',
          'ضبط التكييف على 24 درجة مئوية وتنظيف الفلاتر دورياً يوفر حتى 35% من قيمة الفاتورة ويمنع قفز العداد للشريحة الأعلى.'
        ]
      },
      {
        id: 'art-sakani',
        url: '/articles/sakani-guide-2026',
        tag: 'العقار والدعم',
        readTime: '3 دقائق قراءة',
        title: 'الدعم السكني (سكني) 2026: مصفوفة الدعم المالي وباقة الـ 150 ألف',
        excerpt: 'تفاصيل الدعم الفوري غير المسترد لشراء المسكن الأول وشروط استحقاق دعم أرباح التمويل العقاري.',
        calcId: 'sakani',
        paragraphs: [
          'تتيح باقة الدعم الفوري مبلغاً غير مسترد يصل إلى 150 ألف ريال يُصرف كدفعة أولى لشراء المسكن الأول.',
          'يدعم الصندوق العقاري أرباح التمويل بنسبة 100% للرواتب حتى 14 ألف ريال لمبالغ التمويل حتى 500 ألف ريال.'
        ]
      },
      {
        id: 'art-leave',
        url: '/articles/leave-allowance-guide-2026',
        tag: 'نظام العمل',
        readTime: '3 دقائق قراءة',
        title: 'بدل الإجازة السنوية في نظام العمل 2026: متى تستحق التعويض النقدي؟',
        excerpt: 'شرح المادتين 109 و111 من نظام العمل، كيفية احتساب أجر اليوم، وتسييل رصيد الإجازات غير المستخدمة.',
        calcId: 'leave-allowance',
        paragraphs: [
          'يستحق الموظف إجازة سنوية 21 يوماً ترتفع إلى 30 يوماً بعد إتمام 5 سنوات خدمة متصلة لدى نفس صاحب العمل.',
          'عند الاستقالة أو انتهاء العقد، يُلزم النظام صاحب العمل بتعويض العامل نقدياً عن كامل رصيد إجازاته غير المستخدمة وفق راتبه الفعلي.'
        ]
      }`;

const newEnArticles = `,
      {
        id: 'art-gpa',
        url: '/articles/gpa-guide-2026-en',
        tag: 'Education & Academic',
        readTime: '3 min read',
        title: 'Saudi GPA Calculation Guide 2026: 4.0 & 5.0 Scales & Masarat',
        excerpt: 'How to calculate semester and cumulative GPA out of 4 and 5, credit hour weighting, and honors criteria.',
        calcId: 'gpa',
        paragraphs: [
          'Semester GPA is determined by multiplying course grade points by credit hours and dividing by total semester hours.',
          'Focusing on high-credit courses yields the most rapid improvement in cumulative academic standing.'
        ]
      },
      {
        id: 'art-electricity',
        url: '/articles/electricity-guide-2026-en',
        tag: 'Energy & Utilities',
        readTime: '3 min read',
        title: 'Saudi Residential Electricity Tariffs 2026: Tiers & Savings',
        excerpt: 'Understand Tier 1 (18 halalas) vs Tier 2 (30 halalas), 15% VAT calculation, and summer bill reduction.',
        calcId: 'electricity',
        paragraphs: [
          'Consumption up to 6,000 kWh is billed at 18 halalas per unit; consumption exceeding 6,000 kWh jumps to 30 halalas.',
          'Setting AC thermostats to 24°C prevents high-tier spikes and reduces monthly power bills by up to 35%.'
        ]
      },
      {
        id: 'art-sakani',
        url: '/articles/sakani-guide-2026-en',
        tag: 'Housing & Finance',
        readTime: '3 min read',
        title: 'Sakani Housing Support 2026: Subsidy Matrix & 150k Grants',
        excerpt: 'Direct non-refundable housing grants and profit subsidies for first-time Saudi home buyers.',
        calcId: 'sakani',
        paragraphs: [
          'Instant grant packages offer up to SAR 150,000 non-refundable assistance deposited directly towards down payments.',
          'Salaries up to SAR 14,000 receive 100% mortgage profit subsidy on financing up to SAR 500,000.'
        ]
      },
      {
        id: 'art-leave',
        url: '/articles/leave-allowance-guide-2026-en',
        tag: 'Labor Law',
        readTime: '3 min read',
        title: 'Saudi Annual Leave Allowance 2026: Cash Compensation & Rules',
        excerpt: 'Articles 109 & 111 of Saudi Labor Law: calculation formulas and encashing unused vacation balances.',
        calcId: 'leave-allowance',
        paragraphs: [
          'Employees receive 21 days annual leave, escalating to 30 days after 5 continuous years of service.',
          'Upon contract conclusion, employers must compensate employees for all unused accrued leave days based on actual wages.'
        ]
      }`;

if (!indexHtml.includes('art-gpa')) {
  const idx = indexHtml.indexOf('art-eosb');
  if (idx !== -1) {
    const endBracketIdx = indexHtml.indexOf('];', idx);
    if (endBracketIdx !== -1) {
      indexHtml = indexHtml.substring(0, endBracketIdx) + newArArticles + '\n    ' + indexHtml.substring(endBracketIdx);
      fs.writeFileSync(indexPath, indexHtml, 'utf8');
      console.log('✅ Added 4 new articles to index.html');
    }
  }
}

if (!indexEnHtml.includes('art-gpa')) {
  const idx = indexEnHtml.indexOf('art-eosb');
  if (idx !== -1) {
    const endBracketIdx = indexEnHtml.indexOf('];', idx);
    if (endBracketIdx !== -1) {
      indexEnHtml = indexEnHtml.substring(0, endBracketIdx) + newEnArticles + '\n    ' + indexEnHtml.substring(endBracketIdx);
      fs.writeFileSync(indexEnPath, indexEnHtml, 'utf8');
      console.log('✅ Added 4 new articles to index-en.html');
    }
  }
}
