"""Generate egg curry image with Gemini Nano Banana."""
import base64
import json
import urllib.request

key = None
for line in open(r"C:\Projects\test\.env"):
    if line.startswith("GEMINI_API_KEY="):
        key = line.strip().split("=", 1)[1]

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent?key={key}"
body = {
    "contents": [{"parts": [{"text": (
        "Generate a photorealistic image: South Indian egg curry in a rustic "
        "bowl, halved hard-boiled eggs in a rich red masala gravy with curry "
        "leaves and steam rising, dark moody food photography, overhead shot."
    )}]}]
}
req = urllib.request.Request(
    url, data=json.dumps(body).encode(),
    headers={"Content-Type": "application/json"})
resp = json.load(urllib.request.urlopen(req, timeout=120))
for part in resp["candidates"][0]["content"]["parts"]:
    if "inlineData" in part:
        with open(r"C:\Projects\test\fable5\eggcurry_raw.png", "wb") as f:
            f.write(base64.b64decode(part["inlineData"]["data"]))
        print("saved eggcurry_raw.png")
        break
else:
    print("no image part:", json.dumps(resp)[:500])
