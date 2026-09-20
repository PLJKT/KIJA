import json

p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\data.json"
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

# Check TL timeline
for lang in ["en", "id", "zh"]:
    items = data.get("TL", {}).get(lang, [])
    for item in items:
        if len(item) >= 3:
            print(f"TL {lang} [{item[0]}]: {item[2][:80]}")

print("---")
# Check TOP3
for k in data.get("TOP3", {}):
    print(f"TOP3 {k}:", str(data["TOP3"][k])[:120])

print("---")
# Check OPP
for k in data.get("OPP", {}):
    print(f"OPP {k}:", str(data["OPP"][k])[:120])
