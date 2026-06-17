"""
Downloads the 6 remaining client logos that aren't already saved locally.
Run from the BANSHAP INVESTMENT COMPANY LIMITED folder:
  python download_logos.py

The 8 logos you already placed in assets/img/clients/ are used directly.
This script downloads the remaining 6 into the same folder.
"""
import os
import urllib.request
import ssl

os.makedirs("assets/img/clients", exist_ok=True)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
}

logos = [
    ("crdb.svg",    "https://crdbbank.co.tz/storage/app/media/images/logo.svg"),
    ("nmb.png",     "https://www.nmbbank.co.tz/images/nmb-white-logo.png"),
    ("vodacom.png", "https://images.seeklogo.com/logo-png/21/1/vodacom-logo-png_seeklogo-215102.png"),
    ("azam.png",    "https://images.seeklogo.com/logo-png/63/1/azam-logo-png_seeklogo-631037.png"),
    ("tanesco.png", "https://images.seeklogo.com/logo-png/31/1/tanesco-tanzania-electric-supply-company-limited-logo-png_seeklogo-311615.png"),
    ("tpa.png",     "https://images.seeklogo.com/logo-png/56/1/tanzania-ports-authority-tpa-logo-png_seeklogo-569241.png"),
]

ok = 0
for filename, url in logos:
    path = os.path.join("assets", "img", "clients", filename)
    if os.path.exists(path):
        print(f"  already exists: {filename}")
        ok += 1
        continue
    print(f"Downloading {filename} ...", end=" ")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
            data = r.read()
        with open(path, "wb") as f:
            f.write(data)
        print(f"OK ({len(data)//1024} KB)")
        ok += 1
    except Exception as e:
        print(f"FAILED — {e}")

print(f"\nDone: {ok}/{len(logos)} logos in assets/img/clients/")
