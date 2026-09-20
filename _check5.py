import json

p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\data.json"
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

for section in ["DTXT", "LTXT", "VTXT", "NXT", "DEC"]:
    for lang in ["en", "id", "zh"]:
        val = data.get(section, {}).get(lang, "")
        if isinstance(val, str) and any(c.isdigit() for c in val):
            print(f"\n=== {section} {lang} ===")
            print(val[:400])
