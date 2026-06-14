"""Patch Test 3 story and image in the HTML file."""
import base64, re

p = r"C:\Projects\test\fable5\putting-claude-fable-5-to-the-test.html"
html = open(p, encoding="utf-8").read()

# --- 1. Replace the Test 3 story paragraphs ---
old_story = (
    "    <p>\n"
    "      Raj had read the safari brochure carefully. \"Do not feed the animals,\" it said. \"Keep windows up,\" it said.\n"
    "      Nowhere, and he checked twice, did it say anything about what to do when a zebra leans into your rental car\n"
    "      like a coworker who has decided your cubicle is now a meeting room.\n"
    "    </p>\n"
    "    <p>\n"
    "      \"Can I help you?\" Raj asked, with the calm of a man whose insurance did not cover this.\n"
    "      The zebra inspected the dashboard, the cupholder, and Raj's emotional state, in that order.\n"
    "      It smelled faintly of grass and total entitlement.\n"
    "    </p>\n"
    "    <p>\n"
    "      Raj's wife took photos from the passenger seat. \"Smile!\" she said. Raj did not smile. The zebra, somehow, did.\n"
    "      After a long minute the zebra withdrew, having found neither snacks nor respect, and Raj rolled the window up\n"
    "      three days too late. The brochure now lives on his fridge, with one line added in pen:\n"
    "      \"The zebras have read this too, and they do not care.\"\n"
    "    </p>"
)

new_story = """    <p>Greg crossed his arms and held perfectly still, certain that any sudden movement would shatter the moment. Behind the glass, a two-ton hippopotamus floated mouth-agape like it had just heard the most devastating gossip of its life. The fish darted around its teeth like nervous dental hygienists.</p>
    <p>"Don't smile too big," his wife whispered, lining up the shot. "You'll upstage the hippo."</p>
    <p>Greg nodded solemnly. He'd worn his nicest gray henley and his chunkiest watch for this exact photo, the one he'd been promising his followers for weeks: <em>Me and my spirit animal.</em></p>
    <p>What he didn't realize was that the hippo wasn't yawning in majestic serenity. The hippo was, in fact, screaming. Silently. Eternally. At the man who had been standing motionless against its tank for forty-five minutes.</p>
    <p>The caption Greg posted that night read: "Found my zen."</p>
    <p>The hippo found no such thing.</p>"""

if old_story in html:
    html = html.replace(old_story, new_story)
    print("Story replaced")
else:
    print("ERROR: old story block not found; searching for partial match...")
    if "Raj had read the safari brochure" in html:
        print("partial found")
    else:
        print("no match at all")

# --- 2. Replace verdict for Test 3 ---
old_verdict = "Verdict: it caught the actual comedy of the photo, the man's heroic deadpan at point-blank zebra range. Satisfactory."
new_verdict = "Verdict: it nailed every visual detail, the crossed arms, the chunky watch, the fish orbiting the hippo's open jaws, and turned them into a punchline. Satisfactory."
html = html.replace(old_verdict, new_verdict)

# --- 3. Replace the Test 3 alt text ---
html = html.replace(
    'alt="A zebra leaning into a car next to a man"',
    'alt="Man posing next to a hippo tank at an aquarium"'
)

# --- 4. Swap the base64 image to the new animal_man_web.jpg ---
new_b64 = base64.b64encode(open(r"C:\Projects\test\fable5\animal_man_web.jpg", "rb").read()).decode()

# The current embedded image is between 'data:image/jpeg;base64,' and the closing '"'
# in the animal_man img tag. We can find it by the alt text context.
# Strategy: replace the old b64 block for this specific img tag.
pattern = r'(src="data:image/jpeg;base64,)([A-Za-z0-9+/=]+)(" alt="Man posing next to a hippo tank at an aquarium")'
replaced, count = re.subn(pattern, r'\g<1>' + new_b64 + r'\g<3>', html)
if count:
    html = replaced
    print(f"Image b64 replaced ({count} match)")
else:
    print("WARNING: image b64 pattern not found; alt text swap may have not applied yet")

open(p, "w", encoding="utf-8").write(html)
print(f"Done. File size {len(html)//1024} KB")
