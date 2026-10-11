#!/usr/bin/env python3
"""Read-only metadata and sitemap checks for the static Hasibha site."""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://hasibha.com"
REQUIRED = {
    "about.html": BASE + "/about",
    "about-en.html": BASE + "/about-en",
    "articles/index.html": BASE + "/articles/",
    "articles/index-en.html": BASE + "/articles/index-en",
    "articles/eos-guide-2026.html": BASE + "/articles/eos-guide-2026",
    "articles/eos-guide-2026-en.html": BASE + "/articles/eos-guide-2026-en",
    "articles/vat-guide-2026.html": BASE + "/articles/vat-guide-2026",
    "articles/zakat-guide-2026.html": BASE + "/articles/zakat-guide-2026",
    "articles/bmi-guide-2026.html": BASE + "/articles/bmi-guide-2026",
    "articles/mortgage-guide-2026.html": BASE + "/articles/mortgage-guide-2026",
    "articles/mortgage-guide-2026-en.html": BASE + "/articles/mortgage-guide-2026-en",
}

errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

def get_attr(html, pattern):
    m = re.search(pattern, html, re.I | re.S)
    return m.group(1).strip() if m else ""

for rel, expected_canonical in REQUIRED.items():
    path = ROOT / rel
    check(path.is_file(), f"Missing required page: {rel}")
    if not path.is_file():
        continue
    html = path.read_text(encoding="utf-8")
    title = get_attr(html, r"<title[^>]*>(.*?)</title>")
    description = get_attr(html, r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']')
    canonical = get_attr(html, r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']')
    check(bool(title), f"{rel}: missing title")
    check(bool(description), f"{rel}: missing meta description")
    check(canonical.rstrip("/") == expected_canonical.rstrip("/"),
          f"{rel}: canonical missing or incorrect (expected {expected_canonical})")
    if rel.startswith("articles/") and rel not in ("articles/index.html", "articles/index-en.html"):
        slug = Path(rel).stem
        if slug.endswith("-en"):
            ar_url = f"{BASE}/articles/{slug[:-3]}"
            en_url = f"{BASE}/articles/{slug}"
        else:
            ar_url = f"{BASE}/articles/{slug}"
            en_url = f"{BASE}/articles/{slug}-en"
        check(f'hreflang="ar" href="{ar_url}"' in html,
              f"{rel}: missing/corrupt Arabic hreflang")
        check(f'hreflang="en" href="{en_url}"' in html,
              f"{rel}: missing/corrupt English hreflang")
    if rel == "about.html":
        check(f'hreflang="ar" href="{BASE}/about"' in html and
              f'hreflang="en" href="{BASE}/about-en"' in html,
              "about.html: language alternates do not point to About pages")
        check(f'content="{BASE}/about"' in html,
              "about.html: social/canonical metadata does not identify the About page")
    if rel == "about-en.html":
        check(f'hreflang="ar" href="{BASE}/about"' in html and
              f'hreflang="en" href="{BASE}/about-en"' in html,
              "about-en.html: language alternates do not point to About pages")
    if rel in ("articles/index.html", "articles/index-en.html"):
        check('property="og:title"' in html and 'property="og:description"' in html,
              f"{rel}: missing Open Graph title/description")

sitemap_path = ROOT / "sitemap.xml"
check(sitemap_path.is_file(), "Missing sitemap.xml")
if sitemap_path.is_file():
    try:
        tree = ET.parse(sitemap_path)
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        urls = [node.text.strip() for node in tree.findall(".//sm:loc", ns) if node.text]
        check(len(urls) == len(set(urls)), "sitemap.xml contains duplicate URLs")
        check(BASE + "/articles/" in urls, "sitemap.xml is missing the Arabic articles index")
        for url in urls:
            check(url.startswith(BASE + "/"), f"sitemap.xml has a non-Hasibha URL: {url}")
    except ET.ParseError as exc:
        errors.append(f"sitemap.xml is not valid XML: {exc}")

if errors:
    print("SEO validation FAILED:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"SEO validation passed: {len(REQUIRED)} key pages and sitemap.xml checked.")
