#!/usr/bin/env python3
"""Read-only content and SEO opportunity inventory for Hasibha."""
from collections import defaultdict
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://hasibha.com"
REPORT = ROOT / "automation/reports/content-opportunities.md"
SKIP = {".git", ".github", "automation", "node_modules", "reports"}

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_parts, self.h1_parts, self.words = [], [], []
        self.description, self.canonical, self.lang = "", "", ""
        self.meta, self.links, self.missing_alt = {}, 0, 0
        self.in_title = False
        self.h1_depth = 0
        self.skip_depth = 0
    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        tag = tag.lower()
        if tag == "html": self.lang = a.get("lang", "")
        if tag == "title": self.in_title = True
        if tag in ("script", "style", "noscript", "svg"): self.skip_depth += 1
        if tag == "meta":
            key = (a.get("name") or a.get("property") or "").lower()
            if key: self.meta[key] = a.get("content", "")
            if key == "description": self.description = a.get("content", "").strip()
        if tag == "link":
            if "canonical" in a.get("rel", "").lower().split(): self.canonical = a.get("href", "").strip()
        if tag == "h1": self.h1_depth += 1; self.h1_parts.append([])
        if tag == "a" and a.get("href") and not a["href"].startswith(("mailto:", "tel:", "javascript:", "#")): self.links += 1
        if tag == "img" and not a.get("alt", "").strip(): self.missing_alt += 1
    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "title": self.in_title = False
        if tag == "h1" and self.h1_depth: self.h1_depth -= 1
        if tag in ("script", "style", "noscript", "svg") and self.skip_depth: self.skip_depth -= 1
    def handle_data(self, data):
        if self.in_title: self.title_parts.append(data)
        if self.h1_depth and self.h1_parts: self.h1_parts[-1].append(data.strip())
        if not self.skip_depth:
            self.words.extend(re.findall(r"[\w\u0600-\u06FF]+", data, re.UNICODE))

def site_path(rel):
    value = "/" + str(rel).replace("\\", "/")
    if value == "/index.html": return "/"
    if value.endswith("/index.html"): return value[:-10] or "/"
    if value.endswith(".html"): return value[:-5]
    return value

def main():
    pages, issues, titles, descriptions = [], [], defaultdict(list), defaultdict(list)
    sitemap_paths = set()
    sitemap = ROOT / "sitemap.xml"
    if sitemap.exists():
        try:
            tree = ET.parse(sitemap)
            ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            for node in tree.findall(".//s:loc", ns):
                if node.text: sitemap_paths.add(node.text.strip().removeprefix(BASE).rstrip("/") or "/")
        except ET.ParseError as exc:
            issues.append(("P0", "Sitemap", "sitemap.xml XML غير صالح", str(exc)))
    for file in sorted(ROOT.rglob("*.html")):
        rel = file.relative_to(ROOT)
        if any(part in SKIP for part in rel.parts) or re.match(r"^(google[a-f0-9]+|bing[a-f0-9]+|yandex_[a-f0-9]+)\.html$", rel.name, re.I): continue
        parser = Parser()
        try: parser.feed(file.read_text(encoding="utf-8", errors="replace"))
        except Exception as exc:
            issues.append(("P1", "HTML", f"تعذر تحليل {rel}", str(exc))); continue
        title = "".join(parser.title_parts).strip()
        desc = parser.description
        h1 = [" ".join(parts).strip() for parts in parser.h1_parts]
        path = site_path(rel).rstrip("/") or "/"
        row = {"file": str(rel), "path": path, "lang": parser.lang or "غير محدد", "title": title, "description": desc,
               "words": len(parser.words), "links": parser.links, "missing_alt": parser.missing_alt}
        pages.append(row)
        if title: titles[title.casefold()].append(row)
        if desc: descriptions[desc.casefold()].append(row)
        if not title: issues.append(("P1", "Title", f"{rel}: عنوان الصفحة مفقود", "اقترح عنواناً فريداً يعكس نية البحث."))
        if not desc: issues.append(("P1", "Description", f"{rel}: الوصف التعريفي مفقود", "اكتب وصفاً دقيقاً وفريداً يوضح فائدة الصفحة."))
        if not h1: issues.append(("P1", "H1", f"{rel}: لا يوجد H1", "أضف عنواناً رئيسياً واضحاً ومطابقاً للمحتوى."))
        elif len(h1) > 1: issues.append(("P2", "H1", f"{rel}: يوجد {len(h1)} عناوين H1", "راجع التسلسل الدلالي للعناوين."))
        if not parser.canonical: issues.append(("P2", "Canonical", f"{rel}: canonical مفقود", "تحقق من URL الأساسي قبل إضافته."))
        if not parser.meta.get("og:title") or not parser.meta.get("og:description"):
            issues.append(("P2", "Social metadata", f"{rel}: بيانات Open Graph ناقصة", "أضف بيانات المشاركة الاجتماعية بعد مراجعة العنوان والوصف."))
        if parser.missing_alt:
            issues.append(("P2", "Accessibility", f"{rel}: {parser.missing_alt} صورة بلا alt", "أضف وصفاً للصور المعلوماتية، واترك alt فارغاً للزخرفية."))
        if len(parser.words) < 180:
            issues.append(("P2", "Content depth", f"{rel}: نص قصير نسبياً ({len(parser.words)} كلمة)", "راجع نية الصفحة؛ أضف أمثلة مفيدة فقط إن احتاج المستخدم، ولا تطل النص لمجرد عدد الكلمات."))
        if parser.links < 3:
            issues.append(("P3", "Internal linking", f"{rel}: روابط قليلة ({parser.links})", "اربط الصفحة بحاسبات وأدلة ذات صلة حقيقية إن وجدت."))
        if path not in sitemap_paths:
            issues.append(("P1", "Sitemap", f"{rel}: المسار غير موجود في sitemap.xml", "تحقق من قابلية الفهرسة قبل إضافته إلى sitemap."))
    for title, group in titles.items():
        if len(group) > 1: issues.append(("P1", "Duplicate title", f"عنوان مكرر في {len(group)} صفحات", ", ".join(x["file"] for x in group) + " — اجعل لكل صفحة عنواناً يميز نيتها."))
    for desc, group in descriptions.items():
        if len(group) > 1: issues.append(("P2", "Duplicate description", f"وصف مكرر في {len(group)} صفحات", ", ".join(x["file"] for x in group) + " — خصص الوصف لكل صفحة."))
    order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    issues.sort(key=lambda x: (order.get(x[0], 9), x[1], x[2]))
    counts = {p: sum(1 for x in issues if x[0] == p) for p in order}
    lines = [f"# Content & SEO Opportunity Audit — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}", "",
             f"- HTML pages scanned: **{len(pages)}**",
             f"- P0 critical: **{counts['P0']}** | P1 high: **{counts['P1']}** | P2 medium: **{counts['P2']}** | P3 low: **{counts['P3']}**", "",
             "> Read-only recommendations. No site files or production content are changed by this audit.", "", "## Prioritized opportunities", ""]
    for sev, kind, finding, recommendation in issues:
        lines += [f"### {sev} · {kind}", f"- Finding: {finding}", f"- Recommendation: {recommendation}", ""]
    lines += ["## Page inventory", "", "| File | Language | Words | Links | Missing alt | Title |", "|---|---|---:|---:|---:|---|"]
    for row in pages:
        safe_title = row["title"].replace("|", "\\|").replace("\n", " ")
        lines.append(f"| `{row['file']}` | {row['lang']} | {row['words']} | {row['links']} | {row['missing_alt']} | {safe_title} |")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Content audit complete: {len(pages)} pages; P1={counts['P1']}, P2={counts['P2']}, P3={counts['P3']}. Report: {REPORT}")

if __name__ == "__main__":
    main()
