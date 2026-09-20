import json

p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\data.json"
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

ev = data["EV"]

# === EN ===
ev["ev24"]["en"][0][1] = "Marketing sales hit a record 3,188bn (+44%, 28% above target); Cikarang 33% / Kendal 67%"
ev["ev24"]["en"][2][1] = "Kendal JV (KIK) paid dividends of 322.9bn (KIJA holds 51%)"
ev["ev24"]["en"][3][1] = "FX loss of 205.7bn weighed on net profit"

ev["ev25"]["en"][0][1] = "Marketing sales 3,601bn, record again (+13%, 103% of target); Kendal ~70%"
ev["ev25"]["en"][4][1] = "FX loss down to 120.9bn; EBITDA/interest 4.4x, net debt/EBITDA 0.6x; consolidated cash surplus 1,570bn"

ev["ev26"]["en"][1][1] = "1Q26 marketing sales 518bn (Cikarang 139 / Kendal 379)"
ev["ev26"]["en"][2][1] = "AGM approved FY2025 dividend of IDR2.03/share (42.3bn total), paid 9 Jul"
ev["ev26"]["en"][4][1] = "1H26 results: net loss 6.4bn (one-off ~460bn); infrastructure share of revenue rose to 57%"
ev["ev26"]["en"][5][1] = "Kendal JV declared a dividend of 615bn (51% attributable to KIJA)"

# === ID ===
ev["ev24"]["id"][0][1] = "Penjualan pemasaran mencetak rekor 3.188 miliar (+44%, 28% di atas target); Cikarang 33% / Kendal 67%"
ev["ev24"]["id"][2][1] = "JV Kendal (KIK) membagikan dividen 322,9 miliar (KIJA memegang 51%)"
ev["ev24"]["id"][3][1] = "Rugi selisih kurs 205,7 miliar menekan laba bersih"

ev["ev25"]["id"][0][1] = "Penjualan pemasaran 3.601 miliar, rekor lagi (+13%, 103% target); Kendal sekitar 70%"
ev["ev25"]["id"][4][1] = "Rugi kurs turun ke 120,9 miliar; EBITDA/bunga 4,4x, utang bersih/EBITDA 0,6x; surplus kas konsolidasi 1.570 miliar"

ev["ev26"]["id"][1][1] = "Penjualan pemasaran 1Q26 518 miliar (Cikarang 139 / Kendal 379)"
ev["ev26"]["id"][2][1] = "RUPS menyetujui dividen FY2025 Rp2,03/saham (total 42,3 miliar), dibayar 9 Jul"
ev["ev26"]["id"][4][1] = "Hasil 1H26: rugi bersih 6,4 miliar (satu kali ~460 miliar); porsi infrastruktur pendapatan naik ke 57%"
ev["ev26"]["id"][5][1] = "JV Kendal mengumumkan dividen 615 miliar (51% diatribusikan ke KIJA)"

# ZH already has B/T suffixes - check they're consistent
# ev24 zh: 3,188B, 322.9B, 205.7B - OK
# ev25 zh: 3,601B, 120.9B, 1,570B - OK
# ev26 zh: 518B, 42.3B, 6.4B, 460B, 615B - OK

with open(p, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print("EV event units fixed in data.json")
