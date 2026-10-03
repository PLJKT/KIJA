# KIJA — Financial Research & Analysis

PT Kawasan Industri Jababeka Tbk（印尼证券交易所代码：**KIJA**）财务研究与分析项目。

本项目收录 KIJA 过去 10 年（2015–2025）的财务数据与深度分析报告，覆盖营收、利润、资产负债、利润率、杠杆、分部经营（房地产 / 基础设施 / 服务 / 高尔夫 / 旅游）、营销销售、EBITDA 与市场估值，并总结主要变化、风险与机会。**2026 年更新**：已加入 1H26（2026 年上半年）未经审计财务数据、2016–2026 结合财务数据的发展时间线，以及 2026 年下半年起 4 只同业股票的实时（live）行情联动。

## 目录

| 文件 | 说明 |
| --- | --- |
| [`index.html`](index.html) | **财务与经营 Dashboard**：三语（EN 默认 / ID / 中文）切换；12 个视图（见下「页面」节）；图表可下载 PNG，表格可导出 CSV |
| [`data.json`](data.json) | **Dashboard 的在线数据层（自助更新入口）**：全部展示数据（年度序列、各页 KPI、债务、土地、估值、清算价值、每股土地价值、关键参数、同业、股权/组织、时间线、术语词汇表等 27 个数据块）集中于此；在线打开 Dashboard 时页面自动拉取本文件并覆盖渲染 |
| [`MASTER_PLAYBOOK.md`](MASTER_PLAYBOOK.md) | **方法论复刻手册**：把本系统交付给任何 AI 后，仅凭一个上市公司代码即可生成高度相似的新系统（结构、三语、数字口径、图表、验证流程等硬约束） |
| [`CHANGELOG.md`](CHANGELOG.md) | 内部更新日志（页面不公开） |
| [`KIJA_财务分析报告_2015-2025.md`](KIJA_财务分析报告_2015-2025.md) | 十年财务与经营分析报告（含风险与机会） |
| [`KIJA_financial_data_2015-2025.csv`](KIJA_financial_data_2015-2025.csv) | 2015–2025 关键财务指标数据集 |
| [`analysis_en.md`](analysis_en.md) / [`analysis_id.md`](analysis_id.md) / [`analysis_zh.md`](analysis_zh.md) | 三语分析报告（独立成文，与 Dashboard 页面语言严格一致） |
| [`.github/scripts/update_price.py`](.github/scripts/update_price.py) | **实时股价抓取脚本**（Yahoo Finance v8 chart API；4 标的：KIJA / DMAS / BEST / LPCK），由 GitHub Action 每个工作日 ~09:30 UTC 运行，写回 `data.json` 后自动提交推送 |

**Dashboard 在线访问**：<https://PLJKT.github.io/KIJA/>（GitHub Pages，从 `index.html` 自动发布）。图表依赖 jsDelivr / cdnjs CDN，需联网加载。

### 自助更新数据（新年报/财报发布后）

1. 打开 <https://github.com/PLJKT/KIJA/blob/main/data.json>，点击右上角 ✏️（Edit this file）。
2. **只改要更新的数据**：如 `KP` 里各页 KPI 卡片、`AN` 年度序列（追加新年份时同步在 `years` 和各数组中补一位）、`EV`/`RK` 事件与风险、`DEBT`/`LAND`/`VAL`/`VALI`/`LIQ`/`KEYP` 各块数值、`FY` 期间页图表数据。**不要改动键名、数组顺序和结构**，页面渲染依赖这些结构。
3. 点击 Commit changes（直接提交到 main 分支即可）。
4. 约 1–2 分钟后 GitHub Pages 自动发布，Dashboard 打开时会拉取最新 `data.json` 并更新——**页面结构、三语、图表布局完全不变**。

> 说明：`index.html` 内嵌了一份构建时生成的离线副本（在无网络或本地打开时兜底）；在线访问（https://pljkt.github.io/KIJA/）时以线上 `data.json` 为准。本地打开 `index.html`（file://）不联网，显示内嵌副本，需联网访问在线地址才能读到最新数据。数据更新仍建议保留 1 位小数口径（如 `5149.4`，不要写 `5149.43`）。

**语言与数据口径**：页面右上角可切换 English（默认）/ Bahasa Indonesia / 中文，切换后全部内容（含图表标题、图例、tooltip、KPI 增量、脚注、叙述段落）严格使用所选语言，不混排；数字统一最多保留 1 位小数（四舍五入），带千位分隔符的整数不留小数位。股权结构与治理/组织页依据 FY2025 年报（AR2025）：38 家子公司/合资公司（持股、主营业务、2025 合并资产）、股东结构（Mu'min Ali Gunawan 21.1% / IsDB 11.5% / 库存股 0.1% / 公众 67.3%）、监事/董事/审计委员会与组织结构。

**实时股价（live price）**：Valuation 与 Valuation Illustration 两页的价格、市值、P/E、P/B、YTD、EV/EBITDA 等由 GitHub Action 每个工作日自动抓取 Yahoo Finance 最新收盘价并全站联动计算；4 标的为 KIJA、DMAS、BEST（Bekasi Fajar）、LPCK（Lippo Cikarang）。当前快照（2026-10-02）：KIJA 151 / DMAS 180 / BEST 120 / LPCK 510（IDR）。**同业对比中，BEST/LPCK 的 P&L 与每股数据均取各自最新 1H26 或 FY25 审计口径，与 KIJA 展示口径一致（apple-to-apple）。**

## 页面（12 个视图，导航从左到右）

1. **Overview 总览** — 6 张 KPI 卡片（1H26 营收 / 合并净利 / 归母净利 / EBITDA / 营销销售 / 现金）、营收趋势、合并 vs 归母净利（实线 vs 虚线）、利润率与杠杆、分部营收（房地产 vs 基建）、营销销售、EBITDA 趋势。
2. **Profitability 盈利能力** — 毛利率 / EBITDA 率 / 净利率趋势（2015–2025，含 2015 保守估算）、ROE vs ROA、EBITDA vs 净利、营收 vs 毛利率双轴、FCF 与 FCF 率、**五年分部盈利表（Segment P&L，按营收降序，含持股比例与 GPM/NPM）**。
3. **Debt & Solvency 债务与偿债** — 债务 KPI（总有息负债 / 平均成本 / 现金 / 净负债 / EBITDA 利息覆盖 / 净负债 EBITDA）、按债权人明细（高级票据 / Bank Mandiri / Bank INA Perdana / CCB / OCBC / 租赁）、期限结构、偿债趋势、现金 vs 债务、债务工具表、信用评级（Fitch B- / Moody's B3）、2026 再融资回顾（1.859 亿美元票据提前 18 个月清偿、一次性成本约 460 十亿盾）、**营运资金表（应收账款 / 长期应收 / 应付 / 客户定金 / DSO / DPO）**。
4. **Land Bank 土地储备** — 4 个项目（Cikarang / Kendal / Tanjung Lesung / Morotai）土地储备（2026-06-30 合计 5,089 ha）、AR2025 附注 7 账面价值与单价、与第三方市场挂牌要价对比（Cikarang 约 2,200–5,200 千盾/m²、Kendal 900–2,600、Tanjung Lesung 250–2,300；Morotai 无可靠公开市场价）。市场价为挂牌要价（非官方评估、非成交价——已在注释中强化此警示）。
5. **Valuation 估值分析** — 实时估值快照（市值 / 现价 / P/E / P/B / P/S / 股息率 / 52 周区间，全部随 live price 联动）、过去 12 个月股价与成交量双栏图（月收盘 / 区间 / 成交量 / 换手额 / 换手率）、同业对比（KIJA vs DMAS vs BEST vs LPCK：P/B、P/E、P/S、YTD 全 live）、分析师目标价（Sucor Sekuritas 250，买入）。
6. **Valuation Illustration 估值测算** — P/E、P/B、DCF（两阶段）、SOTP 四种方法低/基准/高区间，**每方法独立配色**的区间条形图（基准点 + 区间 + 现价红条，现价长度与实时价格精确一致）；方法对比表（输入 / 每股隐含值 / vs 现价 / 安全边际）；清算价值（五情景，从 2025-12-31 审计资产负债表起步）；**每股土地价值独立表**（总土地账面 5,783.5 十亿盾 × 100% / 75% / 50% / 25% ÷ 20.59B 股）；权重与 WACC 等参数注明。
7. **Risk & Direction 风险与方向** — 数据推导的风险指标行（绿/黄/红）、Top 3 改进行动（每条绑定可测量的数据缺口）、市场机会（结合当前宏观背景，有来源）。
8. **Holding Structure 股权结构** — 38 家子公司/合资公司表：实体、业务、持股路径（via）、持股比例、2025 合并资产、状态（AR2025）。
9. **Organization 治理与组织** — 公司事实、董事会/监事会/审计委员会、关键人物、组织结构。
10. **2026 Interim 2026 中报** — 1H26 深度页：分部收入饼图、P&L 快照、资产负债表快照、现金桥（期初现金 (end-2025) → 合并盈余 2026 → 期末现金 (end-2026)）、事件时间线、风险指标、增长驱动与亮点（仅 1H26 数据，与年报期严格隔离）。
11. **FY2025 2025 年报** — FY2025 深度页（同上模式，仅 FY2025 vs FY2024 口径）。
12. **FY2024 2024 年报** — FY2024 深度页（同上模式，仅 FY2024 vs FY2023 口径）。

> 期间页规则：每个年报页只显示该报告期对应的数据（FY2024 页绝不出现 2025 数据，现金桥标签按年份命名如 "Opening cash (end-2023)" / "Consolidated surplus 2024" / "Closing cash (end-2024)"）；图表轴与图例用完整词（"Infrastructure"），绝不出现原始变量名（"infraPie" / "revL"）。

## 更新历史

**第 14 轮（2026-10-03）——开发文档同步**：README / CHANGELOG / MASTER_PLAYBOOK 三份文档更新至当前状态。

**第 13 轮（2026-10-02）——外部 AI 反馈评估与交叉核验**：对第三方 9.5/10 评分反馈逐条评估——①采纳：分部盈利表 Real estate 行持股比例由空白改为 "51–100"（100% 全资 Cikarang + 51% Kendal JV）；②已满足：1H26 归母 vs 合并净利已在 KPI 卡片明确标注（归母 -177.9、合并 -6.4、NCI +171.4）；③部分采纳：三语土地注释强化为"挂牌价是 listing 价而非成交价、实际成交可远低于挂牌、隐含增值为理论上限非可变现值"（**刻意未采纳无来源的 "10–20% 折扣" 具体数字**）；④不采纳：FY 标签改为 "Year Ended" 全称（全站统一 FY2025 且有悬停解释，改动破坏一致性）。commit `ab1bddc`。

**第 12 轮（2026-09-30 → 10-02）——Valuation Illustration 估值图反复打磨 + 全站 live 化**：
- **vi-1 图表 redesign**（用户多轮验收-否决-修正循环，5 个 commit）：①浮动区间条（透明占位 + 绿色区间 + base 圆点 + 现价参考线）→ ②修复 SOTP 标签重叠（high 标签在区间右端、base 标签在圆点上方、区间为 0 时隐藏 high）→ ③SOTP 单一目标价改为灰色条（占位 0 + 独立灰条系列）→ ④新增 "Current Price" 行（红条从 0 画到现价、独立 stack `'p'` 精确长度、grid.left 加宽容纳长标签；删除垂直虚线）→ ⑤**每方法独立配色**（P/E 蓝、P/B 紫、DCF 橙、SOTP 灰蓝、Current Price 红），图例精简为 Price + Base 两项。
- **股价 live 化**：Yahoo Finance v8 chart API 抓取 KIJA 收盘价（quoteSummary v7/v10 已确认 401 死路），GitHub Action 每个工作日写回 `data.json → FY.refPrice`；Valuation 页 KPI、KEYP 派生行（延迟价 / 昨收 / 市值 / P/E / P/B / 股息 / YTD / EV-EBITDA）、LIQ/LBV 与同业对比全部自动重算。
- **同业扩展**：DMAS 单家 → KIJA / DMAS / BEST / LPCK 四家（P/B、P/E、P/S、YTD 全 live）；BEST/LPCK 取 1H26 口径（BEST：营收 427.1、EPS 3.12、BVPS 461.8、FY18 后无分红；LPCK：营收 4,519.2、EPS 48、BVPS 1,302.2、无 FY25 分红）；词汇表新增 BEST/LPCK 词条；图表与表格共用同一 live 数据源。
- 该轮所有数值自动随每日股价刷新（用户已确认 "all related numbers auto-update based on refresh of share price"）。

**第 11 轮（2026-09-19 前后）——数据勾稽核验 + 页面排版对齐**：
- 全量复算并交叉核对 59 项关键勾稽关系（年度收入/利润/EBITDA 增速、D/E、ROE、净利率、分部加总=收入、现金堆栈=总资产、净负债/EBITDA、债务本金与到期表、土地行项加总、市值/估值/清算/LBV 各估值数），全部通过；修正文字与数字不一致 4 处：毛利率 43→39 降幅 -3pct→**-4pct**（与显示数字一致）、毛利率峰值年份 2021→**2022**、租赁负债 4.7→**4.8**（与债务块一致）、相关风险卡片注释同步。
- 排版修复：Land Bank 页 lb-1 横向柱状图纵轴左边距 128→168px，长标签「Kota Jababeka Cikarang」不再被裁切、多余刻度线去除；4 卡 KPI 栅格新增显式规则，移动端不再出现 3+1 孤儿。

**第 10 轮——术语悬停解释 / 词汇表**：
- 全站关键专业名词与字母缩写（EBITDA、EPS、BVPS、P/E、P/B、P/S、EV、EV/EBITDA、DCF、WACC、SOTP、ROE、ROA、NCI、TTM、YoY、D/E、ICR、OCF、FCF、SEZ、JV、KEK、RUPS、SHGB、SBLC、PROPER、PLN、IDX、PP&E、LNG、FX、RSI、DPS、MOU、FDI、AGM、GMS、Beta、YTD、B3/B-、PT/Tbk、FY/AR/1H/Q/KPI 及净债务、毛利率、市值、土地储备、归母、少数股东、清算价值、安全边际、加权股本等约 117 条）添加「?」悬停提示：鼠标移到问号上即弹出解释（长词条自动换行；点击可固定/取消，移动端点击切换）。
- 解释内容以联网查证的英文专业定义为准（Fidelity / CFA Institute / Wall Street Prep / NYU Stern / Moody's / NISM / GuruFocus / CFI 等），**解释语言与被解释词完全一致**：英文缩写→英文释义、印尼文词（Margin kotor、Utang bersih、RUPS 等）→印尼文释义、中文词（毛利率、净利率等）→中文释义，三语界面互不混排。
- **同一页内同一词只标注第一个出现处**，后续相同词不再加「?」（用户要求）。
- 词表集中在 `data.json` 的 `GLOS` 数据块（第 27 个数据块），更新解释只改该块即可，无需动页面结构。

**第 9 轮——Land bank value per share**：在 Valuation Illustration 页新增独立表格「Land bank value per share」——土地总账面价值 5,783.5 十亿盾（AR2025 附注 7，成本法）× 100% / 75% / 50% / 25% ÷ 20.59B 加权股本，得到每股 280.9 / 210.7 / 140.4 / 70.2 盾，附与现价对比、安全边际及数据来源说明；独立成表，未与其他估值方法合并。

**第 8 轮（数据层迁移，自助更新）**：
- **`data.json` 成为单一在线数据层**：把原先分散在构建源码里的全部 27 个数据块（KP / EV / RK / DIR / TL / OWN / SUBS / BIZ / VIA / PILLAR / PILLAR_MAP / ORG / DEBT / LAND / VAL / DTXT / LTXT / VTXT / NXT / VALI / LIQ / LBV / KEYP / AN / CHT / FY / GLOS）集中到 `data.json`；`index.html` 的构建脚本改为从 `data.json` 生成内嵌离线副本。
- **运行时拉取**：在线打开 Dashboard 时，页面先拉取同目录 `data.json`（GitHub Pages 同源，HTTP(S) 下启用）覆盖内嵌数据后再渲染；本地 file:// 打开自动回退内嵌副本（无网络也可看，数据为最近一次构建时的版本）。
- **新增 `FY` 块**：各期间页图表专用数据（分部堆叠、营销销售、FY24 分部饼图、近三年净利、FY25 债务/现金/偿债/现金流、1H26 收入/目标/结构/一次性成本、5 年本金计划、债务页参考价与股价标注点、同业倍数等）全部数据化，用户改 `data.json` 即可联动图表。
- **自助更新流程**：见上方「自助更新数据」小节——只需编辑 `data.json` 中对应数值并提交，无需改动任何结构。

**第 7 轮——清算价值 + 关键参数（Bloomberg 标准字段）**：
- **清算价值（Liquidation value）**：以 2025-12-31 审计资产负债表为起点（总资产 15,056.2 / 总负债 6,911.9 / 少数股东权益 1,880.8 / 归母权益 6,263.6），开发土地（账面 5,783.5）按各项目市场挂牌要价重估（Cikarang 7.3–17.2x、Kendal 4.9–14.1x、Tanjung Lesung 2.4–22.4x，Morotai 维持账面），扣减全部负债与 NCI 后按 20.59B 加权股本折每股。五情景：账面 304.1 盾（+68.0%）、市场低位 1,612.7（+791.0%）、低位扣 20% 强制折价 1,351.0（+646.4%）、市场中位 3,344.6（+1,747.9%）、市场高位 5,076.5（+2,704.7%）。页面注明：挂牌价为第三方报价（2026-07–09）、非成交价；未对非土地资产打折；土地销售为持续经营核心业务，清算式速算方向性偏差已说明；非报价、非投资建议。
- **关键参数（Key parameters，Bloomberg 标准字段）**：自 Yahoo Finance quoteSummary（经 crumb 认证，为 Bloomberg 标准公开镜像；Bloomberg 官网 quote 页受机器人防护）取回 21 项参数，**现已被实时抓价替代**（见第 12 轮 live 化）。

**第 6 轮——数据核验**：以 AR2025 审计财务报表为准复核全部录入数据并多来源横向比对。关键修正：2023/2024/2025 年末现金与等价物 1,094.7 → 2,048.5 → 3,618.8（十亿盾）；FY2025 归母 EPS 20.55 盾（加权股本 20.59B 股）；2024 年末权益 7,538.9、2025 年末 8,144.4；2025 毛利率降幅 -3pct→-4pct；再融资规模 4.6 万亿盾。**估值测算（Valuation Illustration）**：按 P/E、P/B、DCF（两阶段）、SOTP 四种方法给出低/基准/高区间并对比现价（当时 181 盾，现已被 live price 替代）。基准值（当时快照）：P/E(8x) 164.4（-9.2%）、P/B(0.6x) 182.5（+0.8%）、DCF 452.4（+150.0%）、SOTP 250.0（+38.1%）；加权公允价值（35/25/30/10）263.9（+45.8%，安全边际 31.4%）。页面注明：说明性估算、非投资建议；WACC 10%、归母自由现金流占比 55%。

**第 5 轮——新增三页**：债务与偿债（Debt & Solvency）、土地储备（Land Bank）、估值分析（Valuation）。详见「页面」节。

## 核心结论速览

- **收入**：2019 年触底（2.25 万亿盾）后连续增长，2025 年达 5.15 万亿盾（+11.9%）
- **利润**：2023–2025 年盈利爆发，2025 年合并净利 8,571 亿盾、归母净利 4,232 亿盾
- **结构**：从"地产驱动"转向"地产＋基建"双轮，2026H1 基建（经常性收入）占比升至 57%
- **杠杆**：负债/权益从 2022 年峰值 96% 降至 2025 年 85%，2026 年中现金约 3.2 万亿盾
- **关注点**：毛利率下滑、少数股东分走约一半利润、土地收入确认节奏波动

## 数据来源

- **年报（官网 IR 页，全部已下载核对）**：AR2015 · AR2016（含 2015 审计比较数）· AR2017 · AR2018 · AR2019 · AR2020 · AR2021 · AR2022 · AR2023 · AR2024 · AR2025 · 1H2026 中期报告（IDX）
- **公司材料**：2024–2026 投资者演示（含 2026-08 投资者日）、IDX 公告与新闻稿
- **市场数据**：Yahoo Finance（live 收盘价，v8 chart API）、S&P Global MI via StockAnalysis、Digrin（月度收盘历史）、Pluang、IDX
- **行业/估值参考**：CBRE Q1-2026 大雅加达工业市场展望、第三方挂牌（Rumah123 / 99.co / Brighton / MM2100 BFIE）、Sucor Sekuritas 研报

> 本仓库内容为公开信息整理与财务分析，不构成投资建议。
