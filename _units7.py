# -*- coding: utf-8 -*-
import json, re

p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\index.html"
with open(p, "r", encoding="utf-8") as f:
    c = f.read()

# Fix DEBT kpi26 "excl. lease 4.7" -> "excl. lease 4.7bn"
c = c.replace('"d":"excl. lease 4.7"', '"d":"excl. lease 4.7bn"')

# Fix DEBT tableNote in data.json - check if it exists there
p2 = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\data.json"
with open(p2, "r", encoding="utf-8") as f:
    data = json.load(f)

# Fix DEBT in data.json
debt = data.get("DEBT", {})
# kpi26 desc
for kpi in debt.get("kpi26", []):
    if "excl. lease" in kpi.get("d", "") and "bn" not in kpi["d"]:
        kpi["d"] = kpi["d"].replace("4.7", "4.7bn")
# tableNote
if "tableNote" in debt:
    tn = debt["tableNote"]
    if "4,606.5" in tn and "bn" not in tn:
        debt["tableNote"] = tn.replace("4,606.5", "IDR 4,606.5bn").replace("31.8", "IDR 31.8bn").replace("4,863", "IDR 4,863bn").replace("4.8)", "IDR 4.8bn)")
# riskRows back-loaded
for rr in debt.get("riskRows", []):
    if "3,780" in rr.get("v", "") and "bn" not in rr["v"]:
        rr["v"] = rr["v"].replace("3,780", "~IDR 3,780bn")

# Fix VAL peers in data.json
val = data.get("VAL", {})
if "peers" in val and "rows" in val["peers"]:
    for row in val["peers"]["rows"]:
        if row[0] == "1H26 net profit" and "bn" not in row[1]:
            row[1] = "-6.4bn (one-off 460bn)"

# Fix DEBT refi in data.json
for row in debt.get("refi", []):
    if len(row) >= 2:
        t = row[1]
        if "460" in t and "bn" not in t and "460:" in t:
            row[1] = t.replace("460:", "IDR 460bn:").replace("280.7", "280.7bn").replace("154.6", "154.6bn").replace("24.9", "24.9bn")
        if "Total debt 4,863" in t:
            row[1] = t.replace("4,863", "IDR 4,863bn")

with open(p2, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

with open(p, "w", encoding="utf-8") as f:
    f.write(c)

print("Final sweep done")
