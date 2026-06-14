"""Find an Annie product image URL on the Tecovas page."""
import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"}
req = urllib.request.Request("https://www.tecovas.com/products/the-annie", headers=UA)
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
urls = re.findall(r'https?://[^"\'\s\\]+\.(?:jpg|jpeg|png|webp)[^"\'\s\\]*', html)
urls = [u.replace("\\/", "/") for u in urls]
hits = [u for u in urls if "annie" in u.lower()]
for u in dict.fromkeys(hits[:10] or urls[:15]):
    print(u[:200])
