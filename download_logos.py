"""
Downloads the 6 remaining client logos into assets/img/clients/
Run from the BANSHAP INVESTMENT COMPANY LIMITED folder:
  python download_logos.py
"""
import os, ssl, time
import urllib.request

os.makedirs("assets/img/clients", exist_ok=True)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

logos = [
    {
        "file": "crdb.svg",
        "url":  "https://crdbbank.co.tz/storage/app/media/images/logo.svg",
        "referer": "https://crdbbank.co.tz/",
    },
    {
        "file": "nmb.png",
        "url":  "https://www.nmbbank.co.tz/images/nmb-white-logo.png",
        "referer": "https://www.nmbbank.co.tz/",
    },
    {
        "file": "vodacom.png",
        "url":  "https://images.seeklogo.com/logo-png/21/1/vodacom-logo-png_seeklogo-215102.png",
        "referer": "https://seeklogo.com/",
    },
    {
        "file": "azam.png",
        "url":  "https://images.seeklogo.com/logo-png/63/1/azam-logo-png_seeklogo-631037.png",
        "referer": "https://seeklogo.com/",
    },
    {
        "file": "tanesco.png",
        "url":  "https://images.seeklogo.com/logo-png/31/1/tanesco-tanzania-electric-supply-company-limited-logo-png_seeklogo-311615.png",
        "referer": "https://seeklogo.com/",
    },
    {
        "file": "tpa.png",
        "url":  "https://images.seeklogo.com/logo-png/56/1/tanzania-ports-authority-tpa-logo-png_seeklogo-569241.png",
        "referer": "https://seeklogo.com/",
    },
]

def download(logo):
    path = os.path.join("assets", "img", "clients", logo["file"])
    if os.path.exists(path) and os.path.getsize(path) > 500:
        print(f"  [skip] {logo['file']} already exists")
        return True

    headers = {
        "User-Agent":      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept":          "image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer":         logo["referer"],
        "Connection":      "keep-alive",
    }
    try:
        req = urllib.request.Request(logo["url"], headers=headers)
        with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
            data = r.read()
        if len(data) < 200:
            print(f"  [fail] {logo['file']} — response too small ({len(data)} bytes), likely blocked")
            return False
        with open(path, "wb") as f:
            f.write(data)
        print(f"  [ok]   {logo['file']} — {len(data)//1024} KB saved")
        return True
    except Exception as e:
        print(f"  [fail] {logo['file']} — {e}")
        return False

print("Downloading logos to assets/img/clients/\n")
ok = sum(download(l) for l in logos if not time.sleep(0.5))
print(f"\nResult: {ok}/{len(logos)} logos ready in assets/img/clients/")

if ok < len(logos):
    print("""
--- Some downloads failed ---
This usually means the site is blocking automated downloads.
Manual fix (takes 2 minutes):
  1. Open each URL in your browser
  2. Right-click the image → Save image as
  3. Save into:  assets/img/clients/
  4. Name the files exactly:
       crdb.svg
       nmb.png
       vodacom.png
       azam.png
       tanesco.png
       tpa.png

URLs to open:
  CRDB:     https://crdbbank.co.tz/storage/app/media/images/logo.svg
  NMB:      https://www.nmbbank.co.tz/images/nmb-white-logo.png
  Vodacom:  https://images.seeklogo.com/logo-png/21/1/vodacom-logo-png_seeklogo-215102.png
  Azam:     https://images.seeklogo.com/logo-png/63/1/azam-logo-png_seeklogo-631037.png
  TANESCO:  https://images.seeklogo.com/logo-png/31/1/tanesco-tanzania-electric-supply-company-limited-logo-png_seeklogo-311615.png
  TPA:      https://images.seeklogo.com/logo-png/56/1/tanzania-ports-authority-tpa-logo-png_seeklogo-569241.png
""")
