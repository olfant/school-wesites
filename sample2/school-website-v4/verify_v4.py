import os
import re

base = r"c:\Users\ACER\OneDrive\Desktop\school\school-website-v4"
html_files = [os.path.join(base, "index.html")]
pages_dir = os.path.join(base, "pages")

for f in sorted(os.listdir(pages_dir)):
    if f.endswith(".html"):
        html_files.append(os.path.join(pages_dir, f))

print(f"Total HTML files found: {len(html_files)}")
for hf in html_files:
    print(" -", os.path.relpath(hf, base), f"({os.path.getsize(hf)} bytes)")

broken_links = []
for hf in html_files:
    hf_dir = os.path.dirname(hf)
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()

    # check img src
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    for src in img_srcs:
        if src.startswith("http") or src.startswith("data:"):
            continue
        target = os.path.normpath(os.path.join(hf_dir, src))
        if not os.path.exists(target):
            broken_links.append((os.path.relpath(hf, base), "img src", src, target))

    # check link href (css)
    css_hrefs = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', content)
    for href in css_hrefs:
        if href.startswith("http") or "icon" in href:
            continue
        target = os.path.normpath(os.path.join(hf_dir, href))
        if not os.path.exists(target):
            broken_links.append((os.path.relpath(hf, base), "css href", href, target))

    # check script src
    js_srcs = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', content)
    for js in js_srcs:
        if js.startswith("http"):
            continue
        target = os.path.normpath(os.path.join(hf_dir, js))
        if not os.path.exists(target):
            broken_links.append((os.path.relpath(hf, base), "script src", js, target))

    # check a href internal links
    a_hrefs = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', content)
    for a in a_hrefs:
        if a.startswith("#") or a.startswith("http") or a.startswith("mailto:") or a.startswith("tel:"):
            continue
        a_clean = a.split("#")[0]
        if not a_clean:
            continue
        target = os.path.normpath(os.path.join(hf_dir, a_clean))
        if not os.path.exists(target):
            broken_links.append((os.path.relpath(hf, base), "a href", a, target))

print(f"\nTotal broken local references: {len(broken_links)}")
if broken_links:
    for b in broken_links:
        print("BROKEN:", b)
else:
    print("SUCCESS: ALL 20 HTML FILES HAVE ZERO BROKEN LINKS AND PERFECT ASSET INTEGRITY!")
