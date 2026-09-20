# -*- coding: utf-8 -*-
import json

p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\data.json"
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

# Check I18N section
i18n = data.get("I18N", {})
for lang in ["en", "id", "zh"]:
    s = i18n.get(lang, {})
    for key in ["debt_refi_note", "val_peers_note"]:
        if key in s:
            val = s[key]
            if "460" in val and "bn" not in val and "miliar" not in val and "十亿盾" not in val and "triliun" not in val:
                print(f"NEEDS FIX: {lang}.{key}: {val[:120]}")
            else:
                print(f"OK: {lang}.{key}")

# Check DEBT tableNote/refi
debt = data.get("DEBT", {})
if "tableNote" in debt:
    print(f"\nDEBT.tableNote: {debt['tableNote'][:200]}")
for row in debt.get("refi", []):
    print(f"DEBT.refi: {row[1][:120]}")

# Check VAL peers
val = data.get("VAL", {})
for row in val.get("peers", {}).get("rows", []):
    if "net profit" in row[0]:
        print(f"\nVAL.peers: {row}")
