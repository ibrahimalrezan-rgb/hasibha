const fs = require('fs');
const path = require('path');

const rootDir = path.resolve(__dirname, '..');
const files = [];

function walk(dir) {
  for (const item of fs.readdirSync(dir)) {
    if (item === '.git' || item === 'node_modules') continue;
    const full = path.join(dir, item);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      walk(full);
    } else if (item.endsWith('.html') || item.endsWith('.js')) {
      files.push(full);
    }
  }
}

walk(rootDir);

let hasErrors = false;

for (const file of files) {
  const content = fs.readFileSync(file, 'utf8');
  const relPath = path.relative(rootDir, file);
  
  if (file.endsWith('.js')) {
    try {
      new Function(content);
    } catch (e) {
      console.error(`JS ERROR in ${relPath}: ${e.message}`);
      hasErrors = true;
    }
  } else if (file.endsWith('.html')) {
    const scriptRegex = /<script(?![^>]*type=["']application\/(ld\+json|json)["'])[^>]*>([\s\S]*?)<\/script>/gi;
    let match;
    while ((match = scriptRegex.exec(content)) !== null) {
      const code = match[2];
      if (!code.trim() || match[0].includes('src=')) continue;
      try {
        new Function(code);
      } catch (e) {
        console.error(`INLINE JS ERROR in ${relPath}: ${e.message}`);
        // print offending lines
        const lines = code.split('\n');
        console.error('Code preview:\n' + lines.slice(0, 15).join('\n'));
        hasErrors = true;
      }
    }
  }
}

if (!hasErrors) {
  console.log('ALL HTML and JS files passed syntax validation successfully! 0 errors.');
} else {
  process.exit(1);
}
