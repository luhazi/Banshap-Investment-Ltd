"""
BANSHAP INVESTMENT COMPANY LIMITED — Local Assets Setup
========================================================
Run this once from the project folder:
  python setup_local_assets.py

What it does:
  1. Downloads Google Fonts (WOFF2) → assets/fonts/
  2. Generates assets/css/fonts.css  (self-hosted @font-face rules)
  3. Downloads any missing client logos → assets/img/clients/
"""

import os, ssl, re, time
import urllib.request

# ── SSL context (skip cert verify for corporate proxies) ──────────────────────
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

UA_BROWSER = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

UA_WOFF2 = (               # Makes Google Fonts return WOFF2 (not TTF)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

FONTS_DIR   = os.path.join("assets", "fonts")
FONTS_CSS   = os.path.join("assets", "css", "fonts.css")
CLIENTS_DIR = os.path.join("assets", "img", "clients")

os.makedirs(FONTS_DIR,   exist_ok=True)
os.makedirs(CLIENTS_DIR, exist_ok=True)

# ── Helpers ───────────────────────────────────────────────────────────────────

def fetch(url, headers=None, timeout=20):
    h = {"User-Agent": UA_BROWSER}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return r.read()

def download_file(url, path, referer=None, min_bytes=200):
    if os.path.exists(path) and os.path.getsize(path) > min_bytes:
        print(f"  [skip] {os.path.basename(path)}")
        return True
    headers = {}
    if referer:
        headers["Referer"] = referer
    try:
        data = fetch(url, headers=headers)
        if len(data) < min_bytes:
            print(f"  [fail] {os.path.basename(path)} — response too small ({len(data)} bytes)")
            return False
        with open(path, "wb") as f:
            f.write(data)
        print(f"  [ok]   {os.path.basename(path)} — {len(data)//1024} KB")
        return True
    except Exception as e:
        print(f"  [fail] {os.path.basename(path)} — {e}")
        return False


# ── 1. Download Google Fonts ──────────────────────────────────────────────────

FONT_REQUESTS = [
    # (label, Google Fonts API URL)
    ("Poppins",    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap"),
    ("Inter",      "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap"),
    ("Outfit",     "https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap"),
    ("Open Sans",  "https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;500;600;700&display=swap"),
    ("Jost",       "https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600;700&display=swap"),
]

print("=" * 60)
print("Step 1: Downloading Google Fonts")
print("=" * 60)

face_blocks = []          # collected @font-face CSS blocks
font_errors = []

for label, api_url in FONT_REQUESTS:
    print(f"\n  {label}:")
    try:
        css_bytes = fetch(api_url, headers={"User-Agent": UA_WOFF2})
        css = css_bytes.decode("utf-8")
    except Exception as e:
        print(f"    [fail] Could not fetch CSS: {e}")
        font_errors.append(label)
        continue

    blocks = re.findall(r"(@font-face\s*\{[^}]+\})", css, re.DOTALL)
    ok_count = 0

    for block in blocks:
        family_m = re.search(r"font-family:\s*'([^']+)'", block)
        style_m  = re.search(r"font-style:\s*(\w+)",      block)
        weight_m = re.search(r"font-weight:\s*([\d]+)",   block)
        src_m    = re.search(r"url\(([^)]+)\)\s*format\('woff2'\)", block)

        if not (family_m and weight_m and src_m):
            continue

        family   = family_m.group(1).replace(" ", "")
        style    = style_m.group(1) if style_m else "normal"
        weight   = weight_m.group(1)
        woff2_url = src_m.group(1).strip("'\"")

        filename   = f"{family.lower()}-{weight}-{style}.woff2"
        local_path = os.path.join(FONTS_DIR, filename)

        if download_file(woff2_url, local_path, min_bytes=1000):
            # Build a clean local @font-face block
            unicode_m = re.search(r"unicode-range:\s*([^;]+);", block)
            unicode_range = f"\n  unicode-range: {unicode_m.group(1)};" if unicode_m else ""
            local_block = (
                "@font-face {\n"
                f"  font-family: '{family_m.group(1)}';\n"
                f"  font-style: {style};\n"
                f"  font-weight: {weight};\n"
                f"  font-display: swap;\n"
                f"  src: url('../fonts/{filename}') format('woff2');"
                f"{unicode_range}\n"
                "}"
            )
            face_blocks.append(local_block)
            ok_count += 1

    print(f"    → {ok_count} weights saved")

# Write fonts.css
if face_blocks:
    with open(FONTS_CSS, "w", encoding="utf-8") as f:
        f.write("/* Self-hosted Google Fonts — auto-generated by setup_local_assets.py */\n\n")
        f.write("\n\n".join(face_blocks))
        f.write("\n")
    print(f"\n  ✓ {FONTS_CSS} written ({len(face_blocks)} @font-face rules)")
else:
    print("\n  ✗ No font faces collected — fonts.css not written")


# ── 2. Download Client Logos ──────────────────────────────────────────────────

print("\n" + "=" * 60)
print("Step 2: Downloading Client Logos")
print("=" * 60 + "\n")

LOGOS = [
    {
        "file":    "crdb.svg",
        "url":     "https://crdbbank.co.tz/storage/app/media/images/logo.svg",
        "referer": "https://crdbbank.co.tz/",
    },
    {
        "file":    "nmb.png",
        "url":     "https://www.nmbbank.co.tz/images/nmb-white-logo.png",
        "referer": "https://www.nmbbank.co.tz/",
    },
    {
        "file":    "vodacom.png",
        "url":     "https://images.seeklogo.com/logo-png/21/1/vodacom-logo-png_seeklogo-215102.png",
        "referer": "https://seeklogo.com/",
    },
    {
        "file":    "azam.png",
        "url":     "https://images.seeklogo.com/logo-png/63/1/azam-logo-png_seeklogo-631037.png",
        "referer": "https://seeklogo.com/",
    },
    {
        "file":    "tanesco.png",
        "url":     "https://images.seeklogo.com/logo-png/31/1/tanesco-tanzania-electric-supply-company-limited-logo-png_seeklogo-311615.png",
        "referer": "https://seeklogo.com/",
    },
    {
        "file":    "tpa.png",
        "url":     "https://images.seeklogo.com/logo-png/56/1/tanzania-ports-authority-tpa-logo-png_seeklogo-569241.png",
        "referer": "https://seeklogo.com/",
    },
]

logo_ok = 0
logo_fail = []

for logo in LOGOS:
    path = os.path.join(CLIENTS_DIR, logo["file"])
    ok = download_file(logo["url"], path, referer=logo["referer"], min_bytes=500)
    if ok:
        logo_ok += 1
    else:
        logo_fail.append(logo)
    time.sleep(0.4)

print(f"\n  Result: {logo_ok}/{len(LOGOS)} logos ready")


# ── Summary ───────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("Summary")
print("=" * 60)
print(f"  Fonts:  {len(face_blocks)} @font-face rules → {FONTS_CSS}")
print(f"  Logos:  {logo_ok}/{len(LOGOS)} downloaded")

if font_errors:
    print(f"\n  Font download errors: {', '.join(font_errors)}")

if logo_fail:
    print("\n  Logo download failures (manual fix needed):")
    print("  Save files into:  assets/img/clients/\n")
    for l in logo_fail:
        print(f"    {l['file']:15s}  {l['url']}")

if not font_errors and not logo_fail:
    print("\n  ✓ All assets local — site is ready for fast offline/GitHub loading!")
