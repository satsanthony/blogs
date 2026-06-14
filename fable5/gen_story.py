import anthropic, base64, json

key = None
for line in open(r"C:\Projects\test\.env"):
    if line.startswith("ANTHROPIC_API_KEY="):
        key = line.strip().split("=", 1)[1]

img_b64 = base64.standard_b64encode(open(r"C:\Projects\test\fable5\animal_man_web.jpg", "rb").read()).decode()

client = anthropic.Anthropic(api_key=key)
msg = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=512,
    system=(
        "You are a comedy writer with sharp sarcasm and a nose for absurdity. "
        "Your wheelhouse: travel, food, hiking, beaches, city life, fashion, and American pop culture. "
        "You write short, punchy, and deceptively smart."
    ),
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {"type": "base64", "media_type": "image/jpeg", "data": img_b64}
            },
            {
                "type": "text",
                "text": (
                    "Look at the attached photo. Write a short, funny story inspired by what you see "
                    "— weave the visual details into a real narrative. Keep it under 150 words. "
                    "No bullet points, no headers. Just a single flowing story that hooks the reader "
                    "in the first sentence and lands a punchline at the end."
                )
            }
        ]
    }]
)

# Strip thinking blocks if any, get only text
text = ""
for block in msg.content:
    if hasattr(block, "text"):
        text = block.text.strip()
        break

print("STORY_START")
print(text)
print("STORY_END")
