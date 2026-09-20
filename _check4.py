import json

p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\data.json"
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

# Print full TOP3 and OPP items
for lang in ["en", "id", "zh"]:
    print(f"\n=== TOP3 {lang} ===")
    items = data["TOP3"].get(lang, {}).get("items", [])
    for it in items:
        print(f"  {it[0]}: {it[1][:200]}")
    print(f"\n=== OPP {lang} ===")
    items = data["OPP"].get(lang, {}).get("items", [])
    for it in items:
        print(f"  {it[0]}: {it[1][:200]}")
