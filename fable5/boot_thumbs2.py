"""Fallback extraction of product images for Tecovas and Corral."""
import re
import urllib.request
from PIL import Image

BASE = r"C:\Projects\test\fable5"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"}


def shrink(src, dst, width=140):
    im = Image.open(src).convert("RGB")
    im.thumbnail((width, width * 2), Image.LANCZOS)
    im.save(dst, "JPEG", quality=75)
    print("saved", dst, im.size)


def grab(name, url):
    req = urllib.request.Request(url, headers=UA)
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
    pats = [
        r'(?:property|name)=[\'"](?:og|twitter):image[\'"][^>]*?content=[\'"]([^\'"]+)[\'"]',
        r'content=[\'"]([^\'"]+)[\'"][^>]*?(?:property|name)=[\'"](?:og|twitter):image[\'"]',
        r'"image"\s*:\s*\[?\s*"(https?://[^"]+\.(?:jpg|jpeg|png|webp)[^"]*)"',
        r'(https?://cdn\.shopify\.com/[^"\'\s]+\.(?:jpg|jpeg|png|webp)[^"\'\s]*)',
    ]
    for p in pats:
        m = re.search(p, html, re.I)
        if m:
            img_url = m.group(1).replace("\\/", "/")
            if img_url.startswith("//"):
                img_url = "https:" + img_url
            print(name, "->", img_url[:120])
            req2 = urllib.request.Request(img_url, headers=UA)
            raw = rf"{BASE}\{name}_raw.img"
            with open(raw, "wb") as f:
                f.write(urllib.request.urlopen(req2, timeout=30).read())
            shrink(raw, rf"{BASE}\{name}.jpg")
            return
    print(name, "STILL NO IMAGE; page len", len(html))


grab("boot_tecovas", "https://www.tecovas.com/products/the-annie")
grab("boot_corral", "https://www.6pm.com/p/corral-boots-z5138-brown/product/9959169")
