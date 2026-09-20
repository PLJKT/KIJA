# -*- coding: utf-8 -*-
import json

p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\data.json"
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

# Fix VAL peers "1.19T" -> "1.19tn"
for row in data.get("VAL", {}).get("peers", {}).get("rows", []):
    if row[0] == "1H26 net profit":
        row[2] = "+175% → 1.19tn"

# Check NXT labels for bare numbers
nxt = data.get("NXT", {})
for lang in ["en", "id", "zh"]:
    for k, v in nxt.get(lang, {}).items():
        if isinstance(v, str) and any(c.isdigit() for c in v):
            print(f"NXT {lang}.{k}: {v}")

with open(p, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print("Done")
