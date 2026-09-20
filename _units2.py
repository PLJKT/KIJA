import json

p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\data.json"
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

# Fix RK risk indicators - add "bn" to numbers missing units
rk = data.get("RK", {})

# rk24 EN: "FX loss","205.7" -> "205.7bn"
for item in rk.get("rk24", {}).get("en", []):
    if item[0] == "FX loss":
        item[1] = "205.7bn"
        item[4] = "USD debt exposure weighed on profit"
# ID
for item in rk.get("rk24", {}).get("id", []):
    if item[0] == "Rugi selisih kurs":
        item[1] = "205,7 miliar"
# ZH
for item in rk.get("rk24", {}).get("zh", []):
    if item[0] == "汇兑损失":
        item[1] = "205.7B"

# rk25 EN: "FX loss","120.9 (-41%)" -> "120.9bn (-41%)"
for item in rk.get("rk25", {}).get("en", []):
    if item[0] == "FX loss":
        item[1] = "120.9bn (-41%)"
# ID
for item in rk.get("rk25", {}).get("id", []):
    if item[0] == "Rugi selisih kurs":
        item[1] = "120,9 miliar (-41%)"
# ZH
for item in rk.get("rk25", {}).get("zh", []):
    if item[0] == "汇兑损失":
        item[1] = "120.9B（-41%）"

# rk26 EN: "One-off refinancing cost","~460" -> "~460bn"
for item in rk.get("rk26", {}).get("en", []):
    if item[0] == "One-off refinancing cost":
        item[1] = "~460bn"
# ID
for item in rk.get("rk26", {}).get("id", []):
    if item[0] == "Biaya refinancing satu kali":
        item[1] = "~460 miliar"
# ZH
for item in rk.get("rk26", {}).get("zh", []):
    if item[0] == "一次性再融资成本":
        item[1] = "约 460B"

with open(p, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print("RK risk indicator units fixed in data.json")
