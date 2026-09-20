import json

p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\data.json"
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

# Check EV events for numbers missing units
ev = data.get("EV", {})
for lang in ["en", "id", "zh"]:
    items = ev.get(lang, [])
    for item in items:
        if len(item) >= 3:
            print(f"EV {lang}: {item[0]} | {item[1][:60]} | {item[2][:60]}")

# Check CHT labels
cht = data.get("CHT", {})
for k, v in cht.items():
    if isinstance(v, str) and any(c.isdigit() for c in v):
        print(f"CHT {k}: {v}")
