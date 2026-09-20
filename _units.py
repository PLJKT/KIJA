p = r"C:\Users\HONOR\Doubao\chats\2026-09-18\new-chat\KIJA\index.html"
with open(p, "r", encoding="utf-8") as f:
    c = f.read()

# === EN fixes ===
# f26_2_s: add IDR bn to marketing sales numbers
c = c.replace(
  "c_f26_2_s:'1,187.6 / FY2026 target 3,750 (Cikarang 1,250 + Kendal 2,500); 32% achieved',",
  "c_f26_2_s:'1,187.6 / FY2026 target 3,750 (Cikarang 1,250 + Kendal 2,500), IDR bn; 32% achieved',"
)
# d1_s: lease 4.7 -> 4.7 bn
c = c.replace(
  "c_d1_s:'Total IDR4,863bn (excl. lease 4.7); average cost of debt 7.16%; Senior Notes USD185.9m fully repaid in 2Q26',",
  "c_d1_s:'Total IDR4,863bn (excl. lease 4.7bn); average cost of debt 7.16%; Senior Notes USD185.9m fully repaid in 2Q26',"
)
# d2_s: Mandiri ~3,780 -> 3,780 bn
c = c.replace(
  "c_d2_s:'Principal due 2H26–2030, IDR bn; Mandiri balance ~3,780 due 2031–2041 (15-yr facility)',",
  "c_d2_s:'Principal due 2H26–2030, IDR bn; Mandiri balance ~3,780bn due 2031–2041 (15-yr facility)',"
)
# d4_s: cash ~3,200 vs debt 4,863 -> add bn
c = c.replace(
  "c_d4_s:'Cash & equivalents vs total debt, IDR bn; 30 Jun 2026 cash ~3,200 vs debt 4,863',",
  "c_d4_s:'Cash & equivalents vs total debt, IDR bn; 30 Jun 2026 cash ~3,200bn vs debt 4,863bn',"
)

# === ID fixes ===
c = c.replace(
  "c_f26_2_s:'1,187.6 / target FY2026 3,750 (Cikarang 1,250 + Kendal 2,500); tercapai 32%',",
  "c_f26_2_s:'1,187.6 / target FY2026 3,750 (Cikarang 1,250 + Kendal 2,500), Rp miliar; tercapai 32%',"
)
c = c.replace(
  "c_d1_s:'Total Rp4,863 miliar (di luar sewa 4.7); biaya utang rata-rata 7.16%; Senior Notes USD185.9 juta lunas penuh pada 2Q26',",
  "c_d1_s:'Total Rp4,863 miliar (di luar sewa 4,7 miliar); biaya utang rata-rata 7,16%; Senior Notes USD185,9 juta lunas penuh pada 2Q26',"
)
c = c.replace(
  "c_d2_s:'Pokok jatuh tempo 2H26–2030, Rp miliar; sisa Mandiri sekitar 3,780 jatuh tempo 2031–2041 (fasilitas 15 tahun)',",
  "c_d2_s:'Pokok jatuh tempo 2H26–2030, Rp miliar; sisa Mandiri sekitar 3.780 miliar jatuh tempo 2031–2041 (fasilitas 15 tahun)',"
)
c = c.replace(
  "c_d4_s:'Kas & setara kas vs total utang, Rp miliar; 30 Jun 2026 kas sekitar 3,200 vs utang 4,863',",
  "c_d4_s:'Kas & setara kas vs total utang, Rp miliar; 30 Jun 2026 kas sekitar 3.200 miliar vs utang 4.863 miliar',"
)

# === ZH fixes ===
c = c.replace(
  "c_f26_2_s:'1,187.6 / 2026 全年目标 3,750（Cikarang 1,250 + Kendal 2,500），达标 32%',",
  "c_f26_2_s:'1,187.6 / 2026 全年目标 3,750（Cikarang 1,250 + Kendal 2,500），十亿盾；达标 32%',"
)
c = c.replace(
  "c_d2_s:'2026H2–2030 到期本金，十亿盾；Mandiri 剩余约 3,780B 集中在 2031–2041 偿还（15 年期贷款）',",
  "c_d2_s:'2026H2–2030 到期本金，十亿盾；Mandiri 剩余约 3,780 十亿盾集中在 2031–2041 偿还（15 年期贷款）',"
)
# Fix ZH g24: "万亿印尼盾" is wrong, should be "十亿盾"
c = c.replace(
  "g24:'营收增长 39% 至 4,602.6 万亿印尼盾，营销销售大增 44%（3,188 万亿），主要来自 Kendal 新地块；即便产生 205.7 亿汇兑损失，净利润仍达 770.1 亿。经常性基础设施（电力、水务、干港）成为更稳定的利润基础，土地销售仍是主要波动项。',",
  "g24:'营收增长 39% 至 4,602.6 十亿盾，营销销售大增 44%（3,188 十亿盾），主要来自 Kendal 新地块；即便产生 205.7 十亿盾汇兑损失，净利润仍达 770.1 十亿盾。经常性基础设施（电力、水务、干港）成为更稳定的利润基础，土地销售仍是主要波动项。',"
)
# Fix ZH g25: "亿" -> "十亿盾"
c = c.replace(
  "g25:'营收增 12% 至创纪录的 5,149.4 亿，净利润增 11% 至 857.1 亿；经常性基础设施占比升至约 57%。现金及等价物大增 77% 至 3,618.8 亿（含合资分红），净债务降至 3,285 亿。尽管土地结构承压，毛利率维持 39%。',",
  "g25:'营收增 12% 至创纪录的 5,149.4 十亿盾，净利润增 11% 至 857.1 十亿盾；经常性基础设施占比升至约 57%。现金及等价物大增 77% 至 3,618.8 十亿盾（含合资分红），净债务降至 3,285 十亿盾。尽管土地结构承压，毛利率维持 39%。',"
)
# Fix ZH g26: "亿" -> "十亿盾"
c = c.replace(
  "g26:'营收因 Kendal 土地确认放缓下降 11% 至 2,436.5 亿，但经营利润保持 524 亿，基础设施占比升至 57%。6.4 亿净亏损主要来自约 460 亿一次性再融资成本（汇兑 280.7、衍生品 154.6、摊销 24.9）。下半年关键指标：土地销售节奏与毛利率回升。',",
  "g26:'营收因 Kendal 土地确认放缓下降 11% 至 2,436.5 十亿盾，但经营利润保持 524 十亿盾，基础设施占比升至 57%。6.4 十亿盾净亏损主要来自约 460 十亿盾一次性再融资成本（汇兑 280.7、衍生品 154.6、摊销 24.9）。下半年关键指标：土地销售节奏与毛利率回升。',"
)
# Fix ZH c_p3_s: "IDR 亿" -> "十亿盾"
c = c.replace(
  "c_p3_s:'EBITDA 柱与合并净利润线，IDR 亿。',",
  "c_p3_s:'EBITDA 柱与合并净利润线，十亿盾。',"
)

with open(p, "w", encoding="utf-8") as f:
    f.write(c)
print("Number-unit fixes applied to index.html")
