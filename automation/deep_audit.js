const fs = require('fs');
const path = require('path');

const baseDir = 'C:\\Users\\ibrah\\.gemini\\antigravity\\scratch\\hasibha';

function getFiles(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(file => {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat && stat.isDirectory()) {
            if (file !== 'node_modules' && file !== '.git' && file !== 'automation') {
                results = results.concat(getFiles(fullPath));
            }
        } else if (file.endsWith('.html')) {
            results.push(fullPath);
        }
    });
    return results;
}

const files = getFiles(baseDir);
console.log('Total HTML files to inspect:', files.length);

const errors = [];

files.forEach(fpath => {
    const rel = path.relative(baseDir, fpath).replace(/\\/g, '/');
    const content = fs.readFileSync(fpath, 'utf8');

    // 1. Check broken links (ignore template strings in scripts)
    const contentWithoutScripts = content.replace(/<script[\s\S]*?<\/script>/gi, '');
    const linkMatches = contentWithoutScripts.matchAll(/href=["']([^"'#?]+)["']/g);
    for (const match of linkMatches) {
        const target = match[1];
        if (target.startsWith('http://') || target.startsWith('https://') || target.startsWith('mailto:') || target.startsWith('tel:') || target.startsWith('#') || target.includes('${')) {
            continue;
        }

        let checkPath = target;
        if (checkPath.startsWith('/')) checkPath = checkPath.substring(1);
        if (checkPath === '') {
            checkPath = 'index.html';
        } else if (checkPath === 'articles' || checkPath === 'articles/') {
            checkPath = 'articles/index.html';
        } else if (!checkPath.endsWith('.html') && !checkPath.endsWith('.png') && !checkPath.endsWith('.xml') && !checkPath.endsWith('.txt') && !checkPath.endsWith('.css')) {
            checkPath = checkPath + '.html';
        }

        const resolved = path.join(baseDir, checkPath);
        if (!fs.existsSync(resolved)) {
            errors.push({ file: rel, type: 'Broken Link', detail: `href="${target}" -> resolved to ${checkPath} (FILE NOT FOUND)` });
        }
    }

    // 2. Check DOM ID references in JavaScript
    const scriptMatches = content.matchAll(/<script(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>/gi);
    for (const sm of scriptMatches) {
        const js = sm[1];
        if (js.includes('application/ld+json')) continue;

        // Check getElementById
        const idMatches = js.matchAll(/document\.getElementById\(["']([^"']+)["']\)/g);
        for (const im of idMatches) {
            const id = im[1];
            // Check if id exists in content
            const idPattern = new RegExp(`id=["']${id}["']`, 'i');
            if (!idPattern.test(content)) {
                errors.push({ file: rel, type: 'Missing DOM ID in JS', detail: `getElementById("${id}") called, but no element with id="${id}" exists in HTML!` });
            }
        }
    }

    // 3. Check for any leftover pregnancy reference
    if (content.toLowerCase().includes('pregnancy')) {
        errors.push({ file: rel, type: 'Dead Pregnancy Reference', detail: 'Found leftover pregnancy reference in file' });
    }

    // 4. Check for broken or empty hrefs
    if (content.includes('href=""') || content.includes("href=''")) {
        errors.push({ file: rel, type: 'Empty Link', detail: 'Found empty href=""' });
    }

    // 5. Check CSS / JS unclosed tags
    const openTags = (content.match(/<script(?![^>]*\/>)/gi) || []).length;
    const closeTags = (content.match(/<\/script>/gi) || []).length;
    if (openTags !== closeTags) {
        errors.push({ file: rel, type: 'Mismatched Script Tags', detail: `Open script tags: ${openTags}, Close tags: ${closeTags}` });
    }
});

console.log(`\nFound ${errors.length} issues:\n`);
errors.forEach(e => console.log(`[${e.file}] (${e.type}): ${e.detail}`));
