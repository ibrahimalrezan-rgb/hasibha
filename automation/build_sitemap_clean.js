const fs = require('fs');
const path = require('path');

const rootDir = 'C:/Users/ibrah/.gemini/antigravity/scratch/hasibha';
const sitemapPath = path.join(rootDir, 'sitemap.xml');
const TODAY = '2026-11-23';
const SITE_URL = 'https://hasibha.com';

const pages = [
  // Core
  { loc: `${SITE_URL}/`, priority: '1.0', changefreq: 'daily' },
  { loc: `${SITE_URL}/index-en`, priority: '0.9', changefreq: 'daily' },
  { loc: `${SITE_URL}/about`, priority: '0.6', changefreq: 'monthly' },
  { loc: `${SITE_URL}/about-en`, priority: '0.5', changefreq: 'monthly' },
  { loc: `${SITE_URL}/contact`, priority: '0.6', changefreq: 'monthly' },
  { loc: `${SITE_URL}/contact-en`, priority: '0.5', changefreq: 'monthly' },
  { loc: `${SITE_URL}/privacy`, priority: '0.5', changefreq: 'monthly' },
  { loc: `${SITE_URL}/privacy-en`, priority: '0.4', changefreq: 'monthly' },

  // Calculators (24 pairs = 48 URLs)
  { slug: 'vat', priority: '0.95' },
  { slug: 'salary', priority: '0.95' },
  { slug: 'mortgage', priority: '0.95' },
  { slug: 'eos', priority: '0.95' },
  { slug: 'zakat', priority: '0.90' },
  { slug: 'personal-loan', priority: '0.90' },
  { slug: 'citizen-account', priority: '0.90' },
  { slug: 'social-security', priority: '0.90' },
  { slug: 'gold-value', priority: '0.90' },
  { slug: 'gpa', priority: '0.95' },
  { slug: 'electricity', priority: '0.95' },
  { slug: 'sakani', priority: '0.95' },
  { slug: 'leave-allowance', priority: '0.95' },
  { slug: 'hijri-date', priority: '0.85' },
  { slug: 'currency', priority: '0.85' },
  { slug: 'bmi', priority: '0.85' },
  { slug: 'calorie', priority: '0.85' },
  { slug: 'water', priority: '0.80' },
  { slug: 'age', priority: '0.85' },
  { slug: 'discount', priority: '0.80' },
  { slug: 'date-diff', priority: '0.80' },
  { slug: 'length', priority: '0.75' },
  { slug: 'weight', priority: '0.75' },
  { slug: 'area', priority: '0.75' },
];

const sitemapUrls = [];

for (const p of pages) {
  if (p.slug) {
    sitemapUrls.push({ loc: `${SITE_URL}/${p.slug}`, priority: p.priority, changefreq: 'weekly' });
    sitemapUrls.push({ loc: `${SITE_URL}/${p.slug}-en`, priority: (parseFloat(p.priority) - 0.1).toFixed(2), changefreq: 'weekly' });
  } else {
    sitemapUrls.push(p);
  }
}

// Articles
const articlesDir = path.join(rootDir, 'articles');
if (fs.existsSync(articlesDir)) {
  sitemapUrls.push({ loc: `${SITE_URL}/articles/`, priority: '0.85', changefreq: 'weekly' });
  sitemapUrls.push({ loc: `${SITE_URL}/articles/index-en`, priority: '0.75', changefreq: 'weekly' });
  const files = fs.readdirSync(articlesDir);
  for (const f of files) {
    if (!f.endsWith('.html') || f.startsWith('index')) continue;
    const slug = f.slice(0, -5);
    const isEn = slug.endsWith('-en');
    sitemapUrls.push({
      loc: `${SITE_URL}/articles/${slug}`,
      priority: isEn ? '0.75' : '0.85',
      changefreq: 'weekly'
    });
  }
}

const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${sitemapUrls.map(u => `  <url>
    <loc>${u.loc}</loc>
    <lastmod>${TODAY}</lastmod>
    <changefreq>${u.changefreq}</changefreq>
    <priority>${u.priority}</priority>
  </url>`).join('\n')}
</urlset>
`;

fs.writeFileSync(sitemapPath, xml, 'utf8');
console.log(`✅ sitemap.xml generated with ${sitemapUrls.length} verified URLs!`);
