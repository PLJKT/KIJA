import json

p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\data.json"
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

# Fix EN timeline - add "bn" to all financial figures
en_tl_fixes = {
    "Profit peak: net profit 427": "Profit peak: net profit 427bn",
    "Revenue 2,995; profit trend turned down": "Revenue 2,995bn; profit trend turned down",
    "Revenue 2,712; net profit 67": "Revenue 2,712bn; net profit 67bn",
    "Revenue 2,254 (decade low)": "Revenue 2,254bn (decade low)",
    "Revenue 2,396; net profit 45": "Revenue 2,396bn; net profit 45bn",
    "Revenue 2,490; parent -5": "Revenue 2,490bn; parent -5bn",
    "FX loss 404; parent -64": "FX loss 404bn; parent -64bn",
    "Revenue 3,300; parent 306": "Revenue 3,300bn; parent 306bn",
    "Revenue 4,602.6; parent 363.3": "Revenue 4,602.6bn; parent 363.3bn",
    "Revenue 5,149.4; cash 3,618.8": "Revenue 5,149.4bn; cash 3,618.8bn",
    "Net loss 6.4 (one-off); infra share 57%": "Net loss 6.4bn (one-off); infra share 57%",
}

for item in data["TL"]["en"]:
    if item[2] in en_tl_fixes:
        item[2] = en_tl_fixes[item[2]]

# Fix ID timeline
id_tl_fixes = {
    "Puncak laba: laba bersih 427": "Puncak laba: laba bersih 427 miliar",
    "Pendapatan 2,995; tren laba menurun": "Pendapatan 2.995 miliar; tren laba menurun",
    "Pendapatan 2,712; laba bersih 67": "Pendapatan 2.712 miliar; laba bersih 67 miliar",
    "Pendapatan 2,254 (terendah dekade)": "Pendapatan 2.254 miliar (terendah dekade)",
    "Pendapatan 2,396; laba bersih 45": "Pendapatan 2.396 miliar; laba bersih 45 miliar",
    "Pendapatan 2,490; entitas induk -5": "Pendapatan 2.490 miliar; entitas induk -5 miliar",
    "Rugi kurs 404; entitas induk -64": "Rugi kurs 404 miliar; entitas induk -64 miliar",
    "Pendapatan 3,300; entitas induk 306": "Pendapatan 3.300 miliar; entitas induk 306 miliar",
    "Pendapatan 4,602.6; entitas induk 363.3": "Pendapatan 4.602,6 miliar; entitas induk 363,3 miliar",
    "Pendapatan 5,149.4; kas 3,618.8": "Pendapatan 5.149,4 miliar; kas 3.618,8 miliar",
    "Rugi bersih 6.4 (satu kali); porsi infrastruktur 57%": "Rugi bersih 6,4 miliar (satu kali); porsi infrastruktur 57%",
}

for item in data["TL"]["id"]:
    if item[2] in id_tl_fixes:
        item[2] = id_tl_fixes[item[2]]

with open(p, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print("Timeline units fixed")
