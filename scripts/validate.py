#!/usr/bin/env python3
"""Validate local HTML references and required deployment assets."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import sys

ROOT = Path(__file__).resolve().parent.parent
HTML_FILES = sorted(ROOT.glob("*.html"))
REQUIRED = ["styles.css", "script.js", "favicon.svg", "robots.txt", "sitemap.xml", "vercel.json"]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.title = False
        self.description = False
        self.viewport = False
        self.og = set()

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "title":
            self.title = True
        if tag == "meta":
            if data.get("name") == "description": self.description = True
            if data.get("name") == "viewport": self.viewport = True
            if data.get("property", "").startswith("og:"): self.og.add(data["property"])
        for key in ("href", "src"):
            if key in data: self.references.append(data[key])


errors = []
for required in REQUIRED:
    if not (ROOT / required).exists(): errors.append(f"Missing required file: {required}")

for page in HTML_FILES:
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8"))
    if not parser.title: errors.append(f"{page.name}: missing title")
    if not parser.description: errors.append(f"{page.name}: missing meta description")
    if not parser.viewport: errors.append(f"{page.name}: missing viewport meta")
    for field in ("og:title", "og:description", "og:type"):
        if field not in parser.og: errors.append(f"{page.name}: missing {field}")
    for reference in parser.references:
        parsed = urlsplit(reference)
        if parsed.scheme or reference.startswith(("#", "mailto:", "tel:")): continue
        target = parsed.path
        if not target: continue
        local = ROOT / target.lstrip("/")
        if not local.exists(): errors.append(f"{page.name}: broken reference {reference}")

if errors:
    print("Validation failed:")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print(f"Validated {len(HTML_FILES)} HTML pages and all local references.")
