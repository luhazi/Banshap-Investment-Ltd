"""
Run this script from the BANSHAP INVESTMENT COMPANY LIMITED folder:
  python download_logos.py

It downloads all 10 client logos into assets/img/clients/
"""
import os
import urllib.request
import ssl

# Create the target directory
os.makedirs("assets/img/clients", exist_ok=True)

# SSL context - ignore cert errors for older servers
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
}

logos = [
    ("crdb.svg",     "https://crdbbank.co.tz/storage/app/media/images/logo.svg"),
    ("nmb.png",      "https://www.nmbbank.co.tz/images/nmb-white-logo.png"),
    ("vodacom.png",  "https://images.seeklogo.com/logo-png/21/1/vodacom-logo-png_seeklogo-215102.png"),
    ("azam.png",     "https://images.seeklogo.com/logo-png/63/1/azam-logo-png_seeklogo-631037.png"),
    ("tanesco.png",  "https://images.seeklogo.com/logo-png/31/1/tanesco-tanzania-electric-supply-company-limited-logo-png_seeklogo-311615.png"),
    ("tpa.png",      "https://images.seeklogo.com/logo-png/56/1/tanzania-ports-authority-tpa-logo-png_seeklogo-569241.png"),
    ("tra.png",      "https://www.tra.go.tz/public/dist/images/LOGO_WINGS.png"),
    ("watu.svg",     "https://watu.com/wp-content/uploads/Watu-Logo_White.svg"),
    ("stanbic.png",  "https://images.seeklogo.com/logo-png/57/1/stanbic-bank-logo-png_seeklogo-571354.png"),
    ("tbl.png",      "https://tanzaniabreweries.co.tz/sites/g/files/wnfebl10571/files/tanzania%20breweries/new%20new/Artboard%201%403x.png"),
]

ok = 0
fail = 0
for filename, url in logos:
    filepath = os.path.join("assets", "img", "clients", filename)
    print(f"Downloading {filename} ...", end=" ")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20, context=ctx) as resp:
            data = resp.read()
        with open(filepath, "wb") as f:
            f.write(data)
        size_kb = len(data) // 1024
        print(f"OK ({size_kb} KB)")
        ok += 1
    except Exception as e:
        print(f"FAILED — {e}")
        fail += 1

print(f"\n{'='*40}")
print(f"Done: {ok} downloaded, {fail} failed")
print("Logos saved to: assets/img/clients/")
