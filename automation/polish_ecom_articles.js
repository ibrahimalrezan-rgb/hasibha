const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'generate_ecom_articles.js');
let code = fs.readFileSync(filePath, 'utf8');

// 1. Replace hardcoded blockquote styles with CSS variables
code = code.replace(/background:#f1f5f9;padding:16px;border-right:4px solid #059669;border-radius:8px;margin:20px 0;/g, 'background:var(--surface);color:var(--text);padding:18px;border-inline-start:4px solid var(--accent);border-radius:12px;margin:20px 0;');
code = code.replace(/background:#f1f5f9;padding:16px;border-left:4px solid #059669;border-radius:8px;margin:20px 0;/g, 'background:var(--surface);color:var(--text);padding:18px;border-inline-start:4px solid var(--accent);border-radius:12px;margin:20px 0;');

// 2. Enhance buildArticleHtml to add TOC and use CSS variables
const oldBodyPattern = /<article class="article">\s*<h1>\$\{title\}<\/h1>\s*<div class="article-meta">[\s\S]*?<\/div>\s*\$\{content\}\s*<div class="calc-box" style="margin-top:32px;background:#f8fafc;border:1px solid #e2e8f0;padding:24px;border-radius:16px;text-align:center;">\s*<h3>\$\{ctaTitle\}<\/h3>\s*<p style="color:#64748b;font-size:14px;margin-bottom:16px;">\$\{ctaDesc\}<\/p>\s*<a href="\$\{ctaUrl\}" class="cta-btn" style="display:inline-block;background:#059669;color:#fff;padding:10px 24px;border-radius:12px;font-weight:bold;text-decoration:none;">\$\{ctaBtn\}<\/a>\s*<\/div>/;

const newBodyReplacement = `<article class="article">
<h1>\${title}</h1>
<div class="article-meta">
<span>📅 \${art.date}</span>
<span>✍️ \${authorName}</span>
<span>⏱️ \${isEn ? art.readTimeEn : art.readTimeAr}</span>
</div>

\${tocHtml}

\${processedContent}

<div class="calc-box" style="margin-top:32px;background:var(--surface);border:1px solid var(--border);padding:24px;border-radius:16px;text-align:center;">
<h3 style="color:var(--text);">\${ctaTitle}</h3>
<p style="color:var(--text-2);font-size:14px;margin-bottom:16px;">\${ctaDesc}</p>
<a href="\${ctaUrl}" class="cta-btn" style="display:inline-block;background:var(--accent);color:#fff;padding:10px 24px;border-radius:12px;font-weight:bold;text-decoration:none;">\${ctaBtn}</a>
</div>`;

// Insert the TOC extraction logic inside buildArticleHtml before return
const oldReturnPattern = /const authorName = isEn \? 'Hasibha Business Team' : 'فريق حاسبها للأعمال';\s*return `/;
const newReturnReplacement = `const authorName = isEn ? 'Hasibha Business Team' : 'فريق حاسبها للأعمال';

  let h2Count = 0;
  const tocList = [];
  const processedContent = content.replace(/<h2>(.*?)<\\/h2>/g, (match, headingText) => {
    h2Count++;
    const id = \`section-\${h2Count}\`;
    tocList.push({ id, text: headingText.replace(/<[^>]+>/g, '') });
    return \`<h2 id="\${id}">\${headingText}<\\/h2>\`;
  });

  const tocHtml = tocList.length > 0 ? \`
<div class="toc-box" style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:20px;margin:24px 0;">
  <div style="font-weight:700;font-size:15px;color:var(--text);margin-bottom:12px;display:flex;align-items:center;gap:8px;">
    <span>📌</span>
    <span>\${isEn ? 'Table of Contents' : 'جدول المحتويات'}</span>
  </div>
  <ul style="list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit, minmax(260px, 1fr));gap:8px;">
    \${tocList.map(item => \`<li><a href="#\${item.id}" style="color:var(--accent);text-decoration:none;font-size:14px;display:flex;align-items:center;gap:6px;padding:6px 10px;border-radius:8px;background:var(--card);border:1px solid var(--border);transition:all 0.2s;"><span style="opacity:0.6;">#</span> <span>\${item.text}</span></a></li>\`).join('\\n    ')}
  </ul>
</div>
\` : '';

  return \``;

code = code.replace(oldReturnPattern, newReturnReplacement);
code = code.replace(oldBodyPattern, newBodyReplacement);

fs.writeFileSync(filePath, code, 'utf8');
console.log('✅ Updated generate_ecom_articles.js with TOC and dark mode CSS variables!');
