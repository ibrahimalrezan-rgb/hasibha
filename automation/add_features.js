const fs = require('fs');
const path = require('path');

const rootDir = 'C:/Users/ibrah/.gemini/antigravity/scratch/hasibha';
const indexPath = path.join(rootDir, 'index.html');
const indexEnPath = path.join(rootDir, 'index-en.html');

let indexHtml = fs.readFileSync(indexPath, 'utf8');
let indexEnHtml = fs.readFileSync(indexEnPath, 'utf8');

// ========================================================
// 1. ARABIC (index.html)
// ========================================================

// Update trust badge 20+ to 24
indexHtml = indexHtml.replace('20+ حاسبة ذكية', '24 حاسبة ذكية');

const arSectionMarker = `<section id="calculators" class="py-12 sm:py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">`;

const arFeaturesHtml = `<section id="calculators" class="py-12 sm:py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

        <!-- ==================== INSTALL TO HOME SCREEN GUIDE (COLLAPSIBLE) ==================== -->
        <div id="installGuideContainer" class="mb-10 transition-all duration-300">
          <div id="installGuideCard" class="relative overflow-hidden rounded-3xl bg-gradient-to-r from-emerald-500/10 via-slate-100 to-sky-500/10 dark:from-emerald-950/40 dark:via-slate-900/60 dark:to-sky-950/40 border border-emerald-500/30 dark:border-emerald-500/20 p-5 sm:p-6 backdrop-blur-md shadow-sm">
            <div class="flex items-center justify-between gap-3 mb-4">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-2xl bg-gradient-to-br from-emerald-600 to-emerald-700 text-white flex items-center justify-center shrink-0 shadow-md shadow-emerald-600/20">
                  <i data-lucide="smartphone" class="w-5 h-5"></i>
                </div>
                <div>
                  <div class="flex items-center gap-2 flex-wrap">
                    <h3 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white">تثبيت حاسبها على شاشة هاتفك الرئيسية</h3>
                    <span class="inline-block text-[11px] font-semibold px-2.5 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-500/20 text-emerald-800 dark:text-emerald-300">تطبيق سريع بدون متجر 📲</span>
                  </div>
                  <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-0.5">احفظ حاسبها على هاتفك للوصول اللحظي بنقرة واحدة كأي تطبيق رسمي وبشاشة كاملة</p>
                </div>
              </div>
              <button id="dismissInstallGuide" type="button" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold text-slate-600 hover:text-slate-900 dark:text-slate-300 dark:hover:text-white bg-white/80 dark:bg-slate-800/80 hover:bg-white dark:hover:bg-slate-800 border border-slate-200/80 dark:border-slate-700 transition-colors shrink-0">
                <span>إخفاء الشرح</span>
                <i data-lucide="x" class="w-3.5 h-3.5"></i>
              </button>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- iPhone / Safari -->
              <div class="p-4 rounded-2xl bg-white/90 dark:bg-slate-900/85 border border-slate-200/80 dark:border-slate-800 flex flex-col justify-between shadow-xs">
                <div>
                  <div class="flex items-center justify-between mb-3 pb-2.5 border-b border-slate-100 dark:border-slate-800">
                    <div class="flex items-center gap-2 font-bold text-sm text-slate-900 dark:text-white">
                      <span class="text-base">🍏</span>
                      <span>طريقة التثبيت على الآيفون (Safari)</span>
                    </div>
                    <span class="text-[11px] font-semibold text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-500/10 px-2 py-0.5 rounded-full">iOS Safari</span>
                  </div>
                  <ol class="space-y-2.5 text-xs sm:text-sm text-slate-600 dark:text-slate-300">
                    <li class="flex items-start gap-2.5">
                      <span class="w-5 h-5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">1</span>
                      <span>اضغط على زر المشاركة <span class="inline-flex items-center gap-1 px-1.5 py-0.5 rounded bg-blue-50 dark:bg-blue-900/30 text-blue-600 dark:text-blue-300 font-semibold text-xs"><i data-lucide="share" class="w-3 h-3 inline"></i> مشاركة</span> في الشريط السفلي للمتصفح.</span>
                    </li>
                    <li class="flex items-start gap-2.5">
                      <span class="w-5 h-5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">2</span>
                      <span>مرر القائمة لأسفل واختر <strong class="text-slate-900 dark:text-white font-semibold">"إضافة إلى الصفحة الرئيسية"</strong> <span class="inline-flex items-center justify-center w-4 h-4 rounded bg-slate-200 dark:bg-slate-700 text-slate-800 dark:text-slate-200 text-xs">➕</span>.</span>
                    </li>
                    <li class="flex items-start gap-2.5">
                      <span class="w-5 h-5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">3</span>
                      <span>اضغط على كلمة <strong class="text-emerald-600 dark:text-emerald-400 font-bold">"إضافة" (Add)</strong> أعلى الزاوية، ومبروك تم التثبيت بنجاح!</span>
                    </li>
                  </ol>
                </div>
                <div class="mt-3 pt-2 text-[11px] text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                  <i data-lucide="check-circle" class="w-3.5 h-3.5 text-emerald-500"></i>
                  <span>يفتح بحجم شاشة كاملة وبدون استهلاك مساحة التخزين</span>
                </div>
              </div>

              <!-- Android / Chrome -->
              <div class="p-4 rounded-2xl bg-white/90 dark:bg-slate-900/85 border border-slate-200/80 dark:border-slate-800 flex flex-col justify-between shadow-xs">
                <div>
                  <div class="flex items-center justify-between mb-3 pb-2.5 border-b border-slate-100 dark:border-slate-800">
                    <div class="flex items-center gap-2 font-bold text-sm text-slate-900 dark:text-white">
                      <span class="text-base">🤖</span>
                      <span>طريقة التثبيت على الأندرويد (Chrome)</span>
                    </div>
                    <span class="text-[11px] font-semibold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-500/10 px-2 py-0.5 rounded-full">Google Chrome</span>
                  </div>
                  <ol class="space-y-2.5 text-xs sm:text-sm text-slate-600 dark:text-slate-300">
                    <li class="flex items-start gap-2.5">
                      <span class="w-5 h-5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">1</span>
                      <span>اضغط على قائمة الخيارات <span class="inline-flex items-center justify-center px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 font-bold text-xs"><i data-lucide="more-vertical" class="w-3 h-3 inline"></i></span> (الثلاث نقاط بأعلى المتصفح).</span>
                    </li>
                    <li class="flex items-start gap-2.5">
                      <span class="w-5 h-5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">2</span>
                      <span>اختر <strong class="text-slate-900 dark:text-white font-semibold">"تثبيت التطبيق"</strong> أو <strong class="text-slate-900 dark:text-white font-semibold">"الإضافة إلى الشاشة الرئيسية"</strong> 📲.</span>
                    </li>
                    <li class="flex items-start gap-2.5">
                      <span class="w-5 h-5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">3</span>
                      <span>اضغط <strong class="text-emerald-600 dark:text-emerald-400 font-bold">"تثبيت" (Install)</strong> وسيتم تثبيته فورياً في قائمة تطبيقاتك.</span>
                    </li>
                  </ol>
                </div>
                <div class="mt-3 pt-2 text-[11px] text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                  <i data-lucide="zap" class="w-3.5 h-3.5 text-amber-500"></i>
                  <span>يفتح فورياً دون الحاجة للبحث في المتصفح كل مرة</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Restore Pill Button (Visible when dismissed) -->
          <div id="installGuidePill" class="hidden text-center my-2">
            <button id="showInstallGuideBtn" type="button" class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full text-xs font-semibold text-emerald-700 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-500/10 hover:bg-emerald-100 dark:hover:bg-emerald-500/20 border border-emerald-500/30 transition-all shadow-xs">
              <i data-lucide="smartphone" class="w-3.5 h-3.5"></i>
              <span>كيف تثبت حاسبها على شاشتك الرئيسية كـ تطبيق؟ (شرح الآيفون والأندرويد)</span>
              <i data-lucide="chevron-down" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>

        <!-- ==================== FAVORITES & PINNED SECTION ==================== -->
        <div id="favoritesSection" class="mb-12 transition-all duration-300">
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center gap-2.5">
              <span class="flex items-center justify-center w-8 h-8 rounded-xl bg-amber-100 dark:bg-amber-500/20 text-amber-500 shadow-xs">
                <i data-lucide="star" class="w-4 h-4 fill-amber-400 text-amber-400"></i>
              </span>
              <div>
                <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
                  <span>حاسباتك المفضلة والمثبتة</span>
                  <span id="favCountBadge" class="text-xs px-2 py-0.5 rounded-full bg-amber-50 dark:bg-amber-500/10 text-amber-700 dark:text-amber-400 font-semibold tabular-nums"></span>
                </h3>
              </div>
            </div>
            <button id="clearFavsBtn" type="button" class="text-xs text-slate-400 hover:text-rose-500 dark:hover:text-rose-400 transition-colors hidden">
              إفراغ المفضلة
            </button>
          </div>

          <!-- Favorites Grid -->
          <div id="favoritesGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
            <!-- Dynamically populated -->
          </div>

          <!-- Empty Favorites Placeholder -->
          <div id="emptyFavsBanner" class="hidden p-4 rounded-2xl bg-amber-50/60 dark:bg-amber-950/15 border border-amber-200/60 dark:border-amber-800/40 text-xs sm:text-sm text-slate-600 dark:text-slate-400 flex items-center gap-3">
            <span class="text-xl shrink-0">⭐</span>
            <p>خصص صفحتك الرئيسية: اضغط على أيقونة النجمة بجانب أي حاسبة (مثل الزكاة، الضريبة، الراتب، الكهرباء) لتثبيتها هنا دائماً للوصول المباشر.</p>
          </div>
        </div>`;

indexHtml = indexHtml.replace(arSectionMarker, arFeaturesHtml);

// JavaScript logic in index.html
// Replace renderCalculatorsGrid and add favorites logic
const oldGridRegex = /function renderCalculatorsGrid\(\) \{[\s\S]*?lucide\.createIcons\(\);\s*\}/;

const newGridAndFavsJs = `    // ==================== FAVORITES & CARD RENDERER ====================
    let favorites = [];
    try {
      const saved = localStorage.getItem('hasibha_favorites');
      favorites = saved ? JSON.parse(saved) : ['vat', 'currency', 'salary'];
    } catch (e) {
      favorites = ['vat', 'currency', 'salary'];
    }

    function saveFavorites() {
      try {
        localStorage.setItem('hasibha_favorites', JSON.stringify(favorites));
      } catch (e) {}
    }

    function toggleFavorite(id) {
      const calc = CALCULATORS.find(c => c.id === id);
      const title = calc ? calc.title : '';
      const idx = favorites.indexOf(id);
      if (idx > -1) {
        favorites.splice(idx, 1);
        showToast(\`تمت إزالة \${title} من المفضلة\`);
      } else {
        favorites.push(id);
        showToast(\`تم تثبيت \${title} في مفضلتك ⭐\`);
      }
      saveFavorites();
      renderFavorites();
      renderCalculatorsGrid();
    }

    function buildCardHtml(calc, isPinned = false) {
      const cat = CATEGORIES[calc.category];
      const isFav = favorites.includes(calc.id);
      return \`
        <div class="calc-card group text-right w-full p-5 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200/90 dark:border-slate-800 hover:border-emerald-500/60 dark:hover:border-emerald-500/50 hover:shadow-lg hover:shadow-emerald-950/5 dark:hover:shadow-none transition-all duration-200 flex flex-col justify-between gap-4 relative">
          <div>
            <div class="flex items-start justify-between gap-3 mb-4">
              <div class="flex items-center gap-3">
                <div class="w-11 h-11 rounded-xl \${cat.iconBox} flex items-center justify-center shrink-0 group-hover:scale-105 transition-transform">
                  <i data-lucide="\${calc.icon}" class="w-5 h-5"></i>
                </div>
                <span class="text-[11px] font-semibold px-2.5 py-1 rounded-full \${cat.badge}">\${cat.label}</span>
              </div>
              <button type="button" data-fav-btn="\${calc.id}" aria-label="\${isFav ? 'إزالة من المفضلة' : 'تثبيت في المفضلة'}" title="\${isFav ? 'إزالة من المفضلة' : 'تثبيت في المفضلة'}" class="p-1.5 rounded-lg text-slate-300 dark:text-slate-600 hover:text-amber-400 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors z-20 focus:outline-none">
                <i data-lucide="star" class="w-5 h-5 \${isFav ? 'text-amber-400 fill-amber-400' : 'fill-none'}"></i>
              </button>
            </div>
            <a href="\${calc.url}" data-open-calc="\${calc.id}" class="block focus:outline-none">
              <h3 class="text-base font-bold text-slate-900 dark:text-white group-hover:text-emerald-700 dark:group-hover:text-emerald-400 transition-colors mb-1.5 flex items-center justify-between">
                <span>\${calc.title}</span>
                \${isPinned ? '<span class="text-[10px] text-amber-600 dark:text-amber-400 font-semibold px-2 py-0.5 rounded-md bg-amber-50 dark:bg-amber-500/10">مثبتة ⭐</span>' : ''}
              </h3>
              <p class="text-sm text-slate-600 dark:text-slate-400 line-clamp-2 leading-relaxed">\${calc.desc}</p>
            </a>
          </div>
          <a href="\${calc.url}" data-open-calc="\${calc.id}" class="pt-3 border-t border-slate-100 dark:border-slate-800/80 flex items-center justify-between text-xs font-semibold text-emerald-600 dark:text-emerald-400">
            <span>احسب الآن</span>
            <i data-lucide="arrow-left" class="w-4 h-4 transform group-hover:-translate-x-1 transition-transform"></i>
          </a>
        </div>
      \`;
    }

    function attachGridEvents(container) {
      container.querySelectorAll('[data-open-calc]').forEach(el => {
        el.addEventListener('click', (e) => {
          if (!e.ctrlKey && !e.metaKey && e.button === 0) {
            e.preventDefault();
            openCalculator(el.dataset.openCalc);
          }
        });
      });

      container.querySelectorAll('[data-fav-btn]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          toggleFavorite(btn.dataset.favBtn);
        });
      });
    }

    function renderFavorites() {
      const grid = document.getElementById('favoritesGrid');
      const banner = document.getElementById('emptyFavsBanner');
      const badge = document.getElementById('favCountBadge');
      const clearBtn = document.getElementById('clearFavsBtn');
      if (!grid) return;

      const favCalcs = favorites.map(id => CALCULATORS.find(c => c.id === id)).filter(Boolean);

      badge.textContent = \`\${favCalcs.length}\`;
      if (favCalcs.length > 0) {
        if (clearBtn) clearBtn.classList.remove('hidden');
        if (banner) banner.classList.add('hidden');
        grid.classList.remove('hidden');
        grid.innerHTML = favCalcs.map(c => buildCardHtml(c, true)).join('');
        attachGridEvents(grid);
      } else {
        if (clearBtn) clearBtn.classList.add('hidden');
        grid.classList.add('hidden');
        if (banner) banner.classList.remove('hidden');
      }
      lucide.createIcons();
    }

    function renderCalculatorsGrid() {
      const grid = document.getElementById('calculatorsGrid');
      const emptyState = document.getElementById('emptySearchState');
      const countBadge = document.getElementById('searchCountBadge');
      const clearBtn = document.getElementById('clearSearchBtn');

      const q = searchQuery.trim().toLowerCase();
      const filtered = CALCULATORS.filter(c => {
        const matchesCat = activeCategory === 'all' || c.category === activeCategory;
        const matchesSearch = !q ||
          c.title.toLowerCase().includes(q) ||
          c.desc.toLowerCase().includes(q) ||
          c.keywords.toLowerCase().includes(q) ||
          CATEGORIES[c.category].label.includes(q);
        return matchesCat && matchesSearch;
      });

      if (q) {
        countBadge.textContent = \`\${filtered.length} نتيجة\`;
        countBadge.classList.remove('hidden');
        clearBtn.classList.remove('hidden');
      } else {
        countBadge.classList.add('hidden');
        clearBtn.classList.add('hidden');
      }

      if (filtered.length === 0) {
        grid.innerHTML = '';
        emptyState.classList.remove('hidden');
        lucide.createIcons();
        return;
      }

      emptyState.classList.add('hidden');
      grid.innerHTML = filtered.map(calc => buildCardHtml(calc, false)).join('');
      attachGridEvents(grid);
      lucide.createIcons();
    }`;

indexHtml = indexHtml.replace(oldGridRegex, newGridAndFavsJs);

// In DOMContentLoaded, call renderFavorites() and bind install guide buttons & clearFavsBtn
const oldInitTarget = `// Initial Render
      renderCategoryPills();
      renderCalculatorsGrid();`;

const newInitCode = `// Install Guide Controller
      const guideCard = document.getElementById('installGuideCard');
      const guidePill = document.getElementById('installGuidePill');
      const dismissBtn = document.getElementById('dismissInstallGuide');
      const showBtn = document.getElementById('showInstallGuideBtn');

      if (localStorage.getItem('hasibha_hide_install_guide') === 'true') {
        if (guideCard) guideCard.classList.add('hidden');
        if (guidePill) guidePill.classList.remove('hidden');
      }

      if (dismissBtn) {
        dismissBtn.addEventListener('click', () => {
          if (guideCard) guideCard.classList.add('hidden');
          if (guidePill) guidePill.classList.remove('hidden');
          localStorage.setItem('hasibha_hide_install_guide', 'true');
          showToast('تم إخفاء الشرح. يمكنك إظهاره متى شئت من الزر الصغير');
          lucide.createIcons();
        });
      }

      if (showBtn) {
        showBtn.addEventListener('click', () => {
          if (guideCard) guideCard.classList.remove('hidden');
          if (guidePill) guidePill.classList.add('hidden');
          localStorage.removeItem('hasibha_hide_install_guide');
          lucide.createIcons();
        });
      }

      // Clear Favorites Button
      const clearFavsBtn = document.getElementById('clearFavsBtn');
      if (clearFavsBtn) {
        clearFavsBtn.addEventListener('click', () => {
          favorites = [];
          saveFavorites();
          renderFavorites();
          renderCalculatorsGrid();
          showToast('تم إفراغ قائمة المفضلة');
        });
      }

      // Initial Render
      renderFavorites();
      renderCategoryPills();
      renderCalculatorsGrid();`;

indexHtml = indexHtml.replace(oldInitTarget, newInitCode);

fs.writeFileSync(indexPath, indexHtml, 'utf8');
console.log('✅ index.html updated with Favorites and Install Guide!');
