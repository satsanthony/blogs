"""Resize blog images and fetch boot product thumbnails via og:image."""
import re
import urllib.request
from PIL import Image

BASE = r"C:\Projects\test\fable5"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"}


def shrink(src, dst, width, quality=72):
    im = Image.open(src).convert("RGB")
    if im.width > width:
        im = im.resize((width, int(im.height * width / im.width)), Image.LANCZOS)
    im.save(dst, "JPEG", quality=quality)
    print(dst, im.size)


shrink(rf"{BASE}\ralphs.png", rf"{BASE}\ralphs_web.jpg", 900)
shrink(rf"{BASE}\animal_man.png", rf"{BASE}\animal_man_web.jpg", 800)

PAGES = {
    "boot_tecovas": "https://www.tecovas.com/products/the-annie",
    "boot_ariat": "https://www.ariat.com/HRTG_WESTERN_R_TOE_W_FOO.html",
    "boot_corral": "https://www.6pm.com/p/corral-boots-z5138-brown/product/9959169",
}

for name, url in PAGES.items():
    try:
        req = urllib.request.Request(url, headers=UA)
        html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
        m = re.search(r'property="og:image"\s+content="([^"]+)"', html) or \
            re.search(r'content="([^"]+)"\s+property="og:image"', html)
        if not m:
            print(name, "NO OG IMAGE")
            continue
        img_url = m.group(1)
        req2 = urllib.request.Request(img_url, headers=UA)
        with open(rf"{BASE}\{name}_raw.img", "wb") as f:
            f.write(urllib.request.urlopen(req2, timeout=30).read())
        shrink(rf"{BASE}\{name}_raw.img", rf"{BASE}\{name}.jpg", 140, quality=75)
    except Exception as e:
        print(name, "FAILED:", e)
