#!/usr/bin/env python3
"""Read-only live HTTP/link audit for the deployed static Hasibha site."""

import os
import re
import html
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import urldefrag, urljoin, urlsplit, urlunsplit, unquote
from pathlib import Path

BASE = "https://hasibha.com"
HOST = urlsplit(BASE).netloc.lower()
ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "automation" / "reports"
CHECK_EXTERNAL = os.environ.get("CHECK_EXTERNAL", "false").lower() == "true"
MAX_EXTERNAL = 100
TIMEOUT = 12
USER_AGENT = "Hasibha-Link-Auditor/1.0 (+https://hasibha.com)"
issues = []
checked = {}
page_ids = {}
internal_targets = defaultdict(set)
external_targets = defaultdict(set)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag.lower() == "a" and attrs.get("href"):
            self.links.append(attrs["href"].strip())


def normalize(url):
    """Normalize a URL for deduplication while preserving meaningful query strings."""
    url, _fragment = urldefrag(url.strip())
    parts = urlsplit(url)
    if parts.scheme.lower() not in ("http", "https"):
        return None
    if not parts.netloc:
        return None
    scheme = parts.scheme.lower()
    netloc = parts.netloc.lower()
    path = re.sub(r"/{2,}", "/", parts.path or "/")
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")
    return urlunsplit((scheme, netloc, path, parts.query, ""))


def is_internal(url):
    parts = urlsplit(url)
    return parts.netloc.lower() == HOST or parts.netloc.lower() in (HOST + ":443", HOST + ":80")


def fetch(url, read_html=False):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            status = response.status
            final_url = response.geturl()
            content_type = response.headers.get("Content-Type", "")
            body = response.read(2_000_000) if read_html and "html" in content_type.lower() else b""
            return status, final_url, content_type, body, ""
    except urllib.error.HTTPError as exc:
        return exc.code, exc.geturl(), exc.headers.get("Content-Type", ""), b"", str(exc)
    except Exception as exc:
        return None, url, "", b"", f"{type(exc).__name__}: {exc}"


def add_issue(severity, kind, url, source, detail, suggestion):
    issues.append({
        "severity": severity, "kind": kind, "url": url,
        "source": source, "detail": detail, "suggestion": suggestion
    })


def load_sitemap():
    path = ROOT / "sitemap.xml"
    if not path.is_file():
        add_issue("ERROR", "sitemap", str(path), "repository", "sitemap.xml is missing", "Restore or generate sitemap.xml.")
        return []
    try:
        tree = ET.parse(path)
    except ET.ParseError as exc:
        add_issue("ERROR", "sitemap", str(path), "repository", f"Invalid XML: {exc}", "Fix sitemap.xml XML syntax.")
        return []
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = []
    for node in tree.findall(".//sm:loc", ns):
        if node.text:
            normalized = normalize(node.text.strip())
            if normalized:
                urls.append(normalized)
    return sorted(set(urls))


print("Loading sitemap URLs...")
sitemap_urls = load_sitemap()
if not sitemap_urls:
    print("No sitemap URLs could be read.")

# Fetch sitemap pages first; discover internal and external anchors from their HTML.
for index, url in enumerate(sitemap_urls, 1):
    status, final_url, content_type, body, error = fetch(url, read_html=True)
    checked[url] = (status, final_url, error)
    if status is None or status >= 400:
        sev = "ERROR" if status is None or status >= 500 or status == 404 else "WARN"
        add_issue(sev, "sitemap-page", url, "sitemap.xml",
                  f"HTTP {status}" if status is not None else error,
                  "Check deployment, redirects, or the URL in sitemap.xml.")
        continue
    if "html" not in content_type.lower() or not body:
        continue
    parser = PageParser()
    try:
        parser.feed(body.decode("utf-8", errors="replace"))
    except Exception as exc:
        add_issue("WARN", "parse", url, "crawler", f"Could not parse HTML: {exc}", "Inspect this page's HTML.")
        continue
    page_ids[url] = parser.ids
    for href in parser.links:
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
            continue
        target_with_fragment = urljoin(final_url, html.unescape(href))
        target, fragment = urldefrag(target_with_fragment)
        normalized = normalize(target)
        if not normalized:
            continue
        if is_internal(normalized):
            internal_targets[normalized].add(url)
            if fragment:
                internal_targets[normalized + "#" + unquote(fragment)].add(url)
        elif CHECK_EXTERNAL:
            external_targets[normalized].add(url)

# Check every distinct internal link discovered, including links not listed in sitemap.
for url, sources in sorted(internal_targets.items()):
    if "#" in url and url.split("#", 1)[0] in internal_targets:
        continue
    base_url, fragment = urldefrag(url)
    normalized = normalize(base_url)
    if not normalized or normalized in checked:
        continue
    status, final_url, content_type, body, error = fetch(normalized, read_html=True)
    checked[normalized] = (status, final_url, error)
    if status is None or status >= 400:
        sev = "ERROR" if status is None or status >= 500 or status == 404 else "WARN"
        add_issue(sev, "internal-link", normalized, ", ".join(sorted(sources)[:4]),
                  f"HTTP {status}" if status is not None else error,
                  "Correct the href, restore the destination, or configure a valid redirect.")
        continue
    if "html" in content_type.lower() and body:
        parser = PageParser()
        parser.feed(body.decode("utf-8", errors="replace"))
        page_ids[normalized] = parser.ids

# Check fragment links where the target page's HTML has been downloaded.
for item, sources in sorted(internal_targets.items()):
    if "#" not in item:
        continue
    target, fragment = item.split("#", 1)
    target = normalize(target)
    if target in page_ids and unquote(fragment) not in page_ids[target]:
        add_issue("WARN", "anchor", f"{target}#{fragment}", ", ".join(sorted(sources)[:4]),
                  "Target page loaded but the fragment ID was not found.",
                  "Correct the fragment or add the matching id to the target page.")

if CHECK_EXTERNAL:
    for url, sources in sorted(external_targets.items())[:MAX_EXTERNAL]:
        status, final_url, _ctype, _body, error = fetch(url, read_html=False)
        checked[url] = (status, final_url, error)
        if status is None or status >= 400:
            sev = "WARN" if status in (401, 403, 405, 429) else "ERROR"
            add_issue(sev, "external-link", url, ", ".join(sorted(sources)[:4]),
                      f"HTTP {status}" if status is not None else error,
                      "Recheck manually; some sites block automated requests. Update only if confirmed broken.")
    if len(external_targets) > MAX_EXTERNAL:
        add_issue("INFO", "external-limit", "—", "crawler",
                  f"Checked first {MAX_EXTERNAL} of {len(external_targets)} unique external URLs.",
                  "Run another focused external audit if more coverage is needed.")

order = {"ERROR": 0, "WARN": 1, "INFO": 2}
issues.sort(key=lambda x: (order.get(x["severity"], 9), x["kind"], x["url"], x["source"]))
counts = {key: sum(1 for issue in issues if issue["severity"] == key) for key in order}
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
lines = [
    f"# Live Link Audit — {now}", "",
    f"- Sitemap URLs: **{len(sitemap_urls)}**",
    f"- Unique URLs checked: **{len(checked)}**",
    f"- Internal link targets discovered: **{len(internal_targets)}**",
    f"- External link targets discovered: **{len(external_targets)}**",
    f"- Errors: **{counts['ERROR']}** | Warnings: **{counts['WARN']}** | Info: **{counts['INFO']}**", "",
    "> Read-only audit. No site files, links, or redirects are changed automatically.", "",
]
if not issues:
    lines.append("No HTTP or anchor issues were detected in this run.")
else:
    for issue in issues:
        lines += [
            f"## {issue['severity']} — {issue['kind']}",
            f"- URL: {issue['url']}",
            f"- Found from: {issue['source']}",
            f"- Result: {issue['detail']}",
            f"- Suggested action: {issue['suggestion']}", ""
        ]

REPORT_DIR.mkdir(parents=True, exist_ok=True)
report_path = REPORT_DIR / "live-link-audit.md"
report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
summary = os.environ.get("GITHUB_STEP_SUMMARY")
if summary:
    with open(summary, "a", encoding="utf-8") as stream:
        stream.write("\n".join(lines[:20]) + "\n")
print(f"Live link audit complete: {len(sitemap_urls)} sitemap URLs, {len(checked)} checked, "
      f"{counts['ERROR']} errors, {counts['WARN']} warnings. Report: {report_path}")
