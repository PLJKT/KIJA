import json

p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\data.json"
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

for section in ["DTXT", "LTXT", "VTXT", "NXT", "DEC"]:
    val = data.get(section, {})
    print(f"=== {section} ===")
    if isinstance(val, dict):
        for k, v in val.items():
            print(f"  {k}: {str(v)[:200]}")
    else:
        print(f"  {str(val)[:200]}")
