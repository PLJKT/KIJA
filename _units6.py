# -*- coding: utf-8 -*-
import json

# ============ Fix index.html inline strings ============
p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\index.html"
with open(p, "r", encoding="utf-8") as f:
    c = f.read()

# --- EN debt_refi_note ---
c = c.replace(
  "debt_refi_note:'The 15-yr IDR Mandiri loan (7.0–7.5%) cleared the USD185.9m notes 18 months early and unwound the USD100m call-spread hedges; one-off 1H26 costs ≈ 460 (FX 280.7 + derivative termination 154.6 + accelerated amortization 24.9).',",
  "debt_refi_note:'The 15-yr IDR Mandiri loan (7.0–7.5%) cleared the USD185.9m notes 18 months early and unwound the USD100m call-spread hedges; one-off 1H26 costs ≈ IDR 460bn (FX 280.7bn + derivative termination 154.6bn + accelerated amortization 24.9bn).',"
)
# --- ID debt_refi_note ---
c = c.replace(
  "debt_refi_note:'Pinjaman IDR Mandiri 15 tahun (7.0–7.5%) melunasi notes USD185.9 juta 18 bulan lebih cepat dan menghentikan hedging call-spread USD100 juta; biaya satu kali 1H26 sekitar 460 (kurs 280.7 + penghentian derivatif 154.6 + amortisasi dipercepat 24.9).',",
  "debt_refi_note:'Pinjaman IDR Mandiri 15 tahun (7,0–7,5%) melunasi notes USD185,9 juta 18 bulan lebih cepat dan menghentikan hedging call-spread USD100 juta; biaya satu kali 1H26 sekitar Rp460 miliar (kurs 280,7 miliar + penghentian derivatif 154,6 miliar + amortisasi dipercepat 24,9 miliar).',"
)
# --- ZH debt_refi_note ---
c = c.replace(
  "debt_refi_note:'15 年期印尼盾 Mandiri 贷款（7.0–7.5%）提前 18 个月清偿 1.859 亿美元票据，并终止 1 亿美元汇率看涨价差对冲；1H26 一次性成本约 460（汇兑 280.7 + 衍生品终止 154.6 + 加速摊销 24.9）。',",
  "debt_refi_note:'15 年期印尼盾 Mandiri 贷款（7.0–7.5%）提前 18 个月清偿 1.859 亿美元票据，并终止 1 亿美元汇率看涨价差对冲；1H26 一次性成本约 460 十亿盾（汇兑 280.7 十亿盾 + 衍生品终止 154.6 十亿盾 + 加速摊销 24.9 十亿盾）。',"
)

# --- EN val_peers_note ---
c = c.replace(
  "val_peers_note:'DMAS: Sinar Mas Land + Sojitz Cikarang industrial developer; 1H26 net profit +175% to 1.19T on data-center land sales; +56.6% YTD-2026. KIJA 1H26 net loss reflects ~460 one-off refinancing costs.',",
  "val_peers_note:'DMAS: Sinar Mas Land + Sojitz Cikarang industrial developer; 1H26 net profit +175% to IDR 1.19tn on data-center land sales; +56.6% YTD-2026. KIJA 1H26 net loss reflects ~IDR 460bn one-off refinancing costs.',"
)
# --- ID val_peers_note ---
c = c.replace(
  "val_peers_note:'DMAS: pengembang kawasan industri Cikarang milik Sinar Mas Land + Sojitz; laba bersih 1H26 +175% menjadi 1.19T dari penjualan lahan data center; +56.6% YTD-2026. Rugi bersih 1H26 KIJA mencerminkan biaya refinancing satu kali sekitar 460.',",
  "val_peers_note:'DMAS: pengembang kawasan industri Cikarang milik Sinar Mas Land + Sojitz; laba bersih 1H26 +175% menjadi Rp1,19 triliun dari penjualan lahan data center; +56,6% YTD-2026. Rugi bersih 1H26 KIJA mencerminkan biaya refinancing satu kali sekitar Rp460 miliar.',"
)
# --- ZH val_peers_note ---
c = c.replace(
  "val_peers_note:'DMAS：Sinar Mas Land + Sojitz 旗下 Cikarang 工业园开发商；1H26 净利 +175% 至 1.19T（数据中心售地）；2026 年 YTD +56.6%。KIJA 1H26 净亏主要反映约 460 的一次性再融资成本。',",
  "val_peers_note:'DMAS：Sinar Mas Land + Sojitz 旗下 Cikarang 工业园开发商；1H26 净利 +175% 至 1.19 万亿盾（数据中心售地）；2026 年 YTD +56.6%。KIJA 1H26 净亏主要反映约 460 十亿盾的一次性再融资成本。',"
)

# --- Fix inline RK (overwritten by data.json but fix anyway) ---
c = c.replace('["FX loss","205.7",1,60,', '["FX loss","205.7bn",1,60,')
c = c.replace('["Rugi selisih kurs","205.7",1,60,', '["Rugi selisih kurs","205,7 miliar",1,60,')
c = c.replace('["FX loss","120.9 (-41%)",1,45,', '["FX loss","120.9bn (-41%)",1,45,')
c = c.replace('["Rugi selisih kurs","120.9 (-41%)",1,45,', '["Rugi selisih kurs","120,9 miliar (-41%)",1,45,')
c = c.replace('["One-off refinancing cost","~460",1,60,', '["One-off refinancing cost","~460bn",1,60,')
c = c.replace('["Biaya refinancing satu kali","sekitar 460",1,60,', '["Biaya refinancing satu kali","~460 miliar",1,60,')
# rk-all bare numbers
c = c.replace('"205.7 (2024) → 120.9 (2025) → cleared 1H26"', '"205.7bn (2024) → 120.9bn (2025) → cleared 1H26"')
c = c.replace('"205.7 (2024) → 120.9 (2025) → bersih 1H26"', '"205,7 miliar (2024) → 120,9 miliar (2025) → bersih 1H26"')
c = c.replace('"2024 205.7B → 2025 120.9B → 2026H1 出清"', '"2024 205.7B → 2025 120.9B → 2026H1 出清"')  # ZH already has B

# --- Fix inline DEBT tableNote ---
c = c.replace(
  '"tableNote":"31 Dec 2025 balance-sheet total 4,606.5 (net of unamortized issuance cost 31.8); table shows principal. Total at 30 Jun 2026: 4,863 (excl. lease 4.8)."',
  '"tableNote":"31 Dec 2025 balance-sheet total IDR 4,606.5bn (net of unamortized issuance cost IDR 31.8bn); table shows principal. Total at 30 Jun 2026: IDR 4,863bn (excl. lease IDR 4.8bn)."'
)
# --- Fix inline DEBT refi rows ---
c = c.replace(
  '"One-off costs ≈ 460: FX loss 280.7 · derivative termination 154.6 · accelerated amortization 24.9"',
  '"One-off costs ≈ IDR 460bn: FX loss 280.7bn · derivative termination 154.6bn · accelerated amortization 24.9bn"'
)
c = c.replace(
  '"Total debt 4,863; average cost 7.16%"',
  '"Total debt IDR 4,863bn; average cost 7.16%"'
)
# --- Fix inline DEBT riskRows back-loaded ---
c = c.replace(
  '"~3,780 due 2031–2041"',
  '"~IDR 3,780bn due 2031–2041"'
)

# --- Fix inline VAL peers row ---
c = c.replace(
  '["1H26 net profit","-6.4 (one-off 460)","+175% → 1.19T"]',
  '["1H26 net profit","-6.4bn (one-off 460bn)","+175% → 1.19tn"]'
)

# --- Fix inline OPP ID spacing ---
c = c.replace("Rp3.750miliar", "Rp3.750 miliar")
c = c.replace("541miliar", "541 miliar")
c = c.replace("Rp1,65miliar", "Rp1,65 miliar")

with open(p, "w", encoding="utf-8") as f:
    f.write(c)
print("index.html inline fixes done")

# ============ Fix data.json ============
p2 = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\data.json"
with open(p2, "r", encoding="utf-8") as f:
    data = json.load(f)

# Fix DTXT (debt table) notes in each language
for lang in ["en", "id", "zh"]:
    d = data.get("DTXT", {}).get(lang, {})
    if "note" in d:
        n = d["note"]
        n = n.replace("4,606.5", "IDR 4,606.5bn").replace("31.8", "IDR 31.8bn")
        n = n.replace("4,863", "IDR 4,863bn").replace("4.8)", "IDR 4.8bn)")
        d["note"] = n

# Fix DEBT refi rows in data.json if present
debt = data.get("DEBT", {})
if "refi" in debt:
    for row in debt["refi"]:
        if len(row) >= 2:
            txt = row[1]
            if "460" in txt and "bn" not in txt:
                txt = txt.replace("460:", "IDR 460bn:").replace("280.7", "280.7bn").replace("154.6", "154.6bn").replace("24.9", "24.9bn")
                row[1] = txt
            if "Total debt 4,863" in txt:
                row[1] = txt.replace("4,863", "IDR 4,863bn")

# Fix VAL peers in data.json
val = data.get("VAL", {})
if "peers" in val and "rows" in val["peers"]:
    for row in val["peers"]["rows"]:
        if row[0] == "1H26 net profit":
            row[1] = "-6.4bn (one-off 460bn)"

# Fix RK in data.json (re-verify)
rk = data.get("RK", {})
for item in rk.get("rk24", {}).get("en", []):
    if item[0] == "FX loss":
        item[1] = "205.7bn"
for item in rk.get("rk25", {}).get("en", []):
    if item[0] == "FX loss":
        item[1] = "120.9bn (-41%)"
for item in rk.get("rk26", {}).get("en", []):
    if item[0] == "One-off refinancing cost":
        item[1] = "~460bn"

# Fix rk-all bare numbers
for item in rk.get("rk-all", {}).get("en", []):
    if "205.7" in str(item[4]):
        item[4] = item[4].replace("205.7 (2024)", "205.7bn (2024)").replace("120.9 (2025)", "120.9bn (2025)")
for item in rk.get("rk-all", {}).get("id", []):
    if "205.7" in str(item[4]):
        item[4] = item[4].replace("205.7 (2024)", "205,7 miliar (2024)").replace("120.9 (2025)", "120,9 miliar (2025)")

# Fix OPP ID spacing in data.json
for it in data.get("OPP", {}).get("id", {}).get("items", []):
    it[1] = it[1].replace("Rp3.750miliar", "Rp3.750 miliar").replace("541miliar", "541 miliar").replace("Rp1,65miliar", "Rp1,65 miliar")

with open(p2, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print("data.json fixes done")
