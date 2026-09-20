import json

p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\data.json"
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

print("Top-level keys:", list(data.keys()))
# Check if EV exists
if "EV" in data:
    for k in list(data["EV"].keys())[:3]:
        print(f"EV[{k}]:", data["EV"][k][:2] if isinstance(data["EV"][k], list) else data["EV"][k])
else:
    print("No EV key in data.json")

# Check I18N section
if "I18N" in data:
    for k in list(data["I18N"].keys())[:5]:
        print(f"I18N[{k}]:", str(data["I18N"][k])[:100])
