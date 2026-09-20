import json

p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\data.json"
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

# Fix ID TOP3: "316bn" -> "316 miliar"
for it in data["TOP3"]["id"]["items"]:
    if "316bn" in it[1]:
        it[1] = it[1].replace("316bn", "316 miliar")

# Fix ID OPP spacing: "3.750miliar" -> "3.750 miliar", "541miliar" -> "541 miliar"
for it in data["OPP"]["id"]["items"]:
    it[1] = it[1].replace("3.750miliar", "3.750 miliar").replace("541miliar", "541 miliar")

# Fix ZH TOP3: "bn" suffix -> "十亿盾"; fix "316 亿盾" which should be "316 十亿盾"
for it in data["TOP3"]["zh"]["items"]:
    it[1] = it[1].replace("751bn", "751 十亿盾")
    it[1] = it[1].replace("369bn", "369 十亿盾")
    it[1] = it[1].replace("56→316bn", "56→316 十亿盾")
    it[1] = it[1].replace("341→458bn", "341→458 十亿盾")
    it[1] = it[1].replace("30bn", "30 十亿盾")
    it[1] = it[1].replace("316 亿盾", "316 十亿盾")

with open(p, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print("TOP3/OPP units fixed")
