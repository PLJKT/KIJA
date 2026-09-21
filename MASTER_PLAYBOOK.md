# Financial Dashboard — Master Playbook

> Purpose: hand this file to any AI, give it a listed company ticker (and optionally its official annual report PDFs), and it should produce a financial-operations dashboard that looks, feels, and behaves like the KIJA dashboard (https://pljkt.github.io/KIJA/).
>
> Read this top-to-bottom before writing any code. Treat every rule below as a hard constraint unless the user explicitly waives it.

---

## 1. Deliverable shape

- **One static site** hosted on **GitHub Pages** from the `main` branch, served at `https://<user>.github.io/<repo>/`.
- **Single-file SPA** (`index.html`) with in-page hash routing between "pages" (sections). No server, no build step, no framework.
- **Two files**: `index.html` (HTML + CSS + JS + inline data) and `data.json` (the single source of truth, loaded at runtime via XMLHttpRequest).
- **Runtime data override**: on load, the page fetches `data.json?v=<timestamp>` and overwrites the inline `AN`, `VAL`, `FY`, `GLOS`, `CHT`, `KP`, `EV`, `RK`, `DEBT`, `LAND`, `TL`, `TOP3`, `OPP` objects in `index.html`. **This means every data change must be made in BOTH files** — or just in `data.json` if it overrides inline. Always update `data.json`; update `index.html` inline too for consistency.
- **Three languages, strict**: English (default), Bahasa Indonesia, 中文. Language switcher in the header (EN / ID / 中文). Once a language is chosen, **every visible string must be in that language** — no mixed paragraphs, no mixed units, no leftover English in a ZH view.
- Desktop-first, responsive down to mobile.

---

## 2. Repository layout

```
<repo>/
  index.html          # the entire dashboard (HTML + CSS + JS + inline data fallback)
  data.json           # single source of truth (loaded at runtime, overrides inline)
  README.md
  CHANGELOG.md        # internal only, NOT shown on the public page
  .github/
    workflows/
      update-price.yml  # GitHub Action: weekday auto-fetch latest close price
    scripts/
      update_price.py   # fetches Yahoo Finance, patches data.json, commits
  _shots/             # self-screenshots from shot.py (gitignore optional)
```

No build step, no bundler. Edit `index.html` and `data.json` directly, commit, push.

---

## 3. Architecture (critical)

### How data flows

```
Browser loads index.html
  → renders with inline <script> objects (AN, KP, EV, ...)
  → fires XMLHttpRequest for data.json?v=Date.now()
  → on success: deep-merges/overwrites inline objects
  → calls applyLang() and renderAll()
```

**Implications:**
- If you change a number only in `index.html` inline but `data.json` has the old value, the user will see the old value. **Always update `data.json`.**
- If you add a new chart function but forget its data key in `data.json`, the chart renders blank or shows the raw key (e.g. `revL`, `infraPie`).
- The `?v=Date.now()` cache-buster means `data.json` never needs manual cache-clear. But `index.html` itself IS cached by GitHub Pages CDN — tell the user to **hard-refresh (Ctrl+F5)** when changes don't appear.

### Git commit discipline

- One logical change = one commit, message starts with `R<nn>:` short description.
- After committing, push immediately: `git push origin main`.
- GitHub Pages redeploys in ~60–90 seconds.

### Windows / PowerShell environment

- The agent runs on Windows. **Do not use Bash syntax** (`&&`, heredocs, `$()`, `ls -la`).
- For multi-line or quote-heavy edits, **write a `.py` file and run `python xxx.py`** rather than PowerShell here-strings.
- PowerShell `Set-Content` changes encoding silently; use Python `open(path, 'w', encoding='utf-8')` for all file writes.
- Use `assert`-based exact string matching in Python replace scripts (e.g. `assert old in c, "pattern not found"`) so a silent miss fails loudly.

---

## 4. data.json schema (canonical blocks)

Top-level keys (add or remove per company, but keep names stable once shipped):

| Key | Purpose |
|---|---|
| `meta` | Page title, subtitle, as-of date, units |
| `KP` | KPI cards per page, per language |
| `AN` | Annual series (parallel arrays): `years[]`, `revenue`, `niCons`, `niParent`, `ebitda`, `gpm`, `npm`, `roe`, `roa`, `de`, `assets`, `liab`, `equity`, `cfo`, `capex`, `landAcq`, `fcf`, `fcfCons`, `fcfMargin`, `fcfConsMargin`, `ebitdaMargin`, `msales`, `segRe`, `segInfra`. **Every array same length as `years`.** |
| `EV` | Event timeline per year page (ev24/ev25/ev26), each with `en/id/zh` arrays of `[date, text]` |
| `RK` | Risk indicator rows per page (rk24/rk25/rk26/rk-all), each `en/id/zh` arrays of `[name, value, level(0/1/2), maxScore, note]` |
| `TL` | Company history timeline, `[year, heading, key_metric]` per language |
| `DEBT` | Lenders, maturity ladder, cash/debt series, debt instruments table, ratings, refinancing history, risk rows, KPI cards |
| `WC` | Working capital: `years[]`, `ar`, `arLT`, `ap`, `deposits`, `revenue` arrays |
| `LAND` | Per-project land bank rows: `p`, `loc`, `st`, `ha`, `dev`, `book`, `m2`, `mLo`, `mHi`, `uplift`; plus KPI cards and `total` |
| `VAL` | Valuation: KPI cards, monthly price/close/events/stats, peer comparison, analyst targets, volume array, price range array |
| `VALI` | Valuation illustration: method comparison table (P/E, P/B, DCF, liquidation) |
| `LIQ` | Liquidation value calculation |
| `LBV` | Landbank value per share at 100/75/50/25% factor |
| `FY` | Per-year deep-dive page data: segment pies, P&L snapshot, balance sheet, cash bridge, revenue breakdown, one-off costs |
| `CHT` | Chart axis/label strings (overridden by data.json; must match keys used in render functions) |
| `GLOS` | Hover glossary: maps term → `{en, id, zh}` short explanations |
| `TOP3` | Top-3 improvement actions per language: `{h, sub, items: [[title, description]]}` |
| `OPP` | Market opportunities per language: same structure as TOP3 |
| `DIR` | Directors / boards |
| `OWN`, `SUBS`, `BIZ`, `VIA`, `PILLAR`, `PILLAR_MAP`, `ORG` | Holding structure, subsidiaries, business pillars, org chart |
| `DTXT`, `LTXT`, `VTXT`, `NXT`, `DEC` | Page narrative text and table headers per language |
| `SOURCES` | Footer source list: `[[name, url], ...]` |
| `SEG` | Segment profitability table (top-N business lines with margins) |

**Number rules (NON-NEGOTIABLE):**
- All financial figures in **IDR billion** (or local-currency bn). State the unit explicitly in every chart axis, table header, KPI card `u` field, **and every narrative note/subtitle**.
- **Every number in descriptive text must carry its unit.** Bare numbers like "≈ 460" or "FX loss 205.7" are bugs. Examples:
  - EN: `≈ IDR 460bn`, `FX 280.7bn`, `~3,780bn`
  - ID: `≈ Rp460 miliar`, `kurs 280,7 miliar`
  - ZH: `约 460 十亿盾`, `汇兑 280.7 十亿盾`
- Display rounding: **one decimal place, round half up**. Table values with thousands separators round to whole numbers (no decimal).
- Negative numbers: prefix with `−` (U+2212), not hyphen. No `+` sign on positive numbers.
- Percentages: store as number (e.g. `39`), format with `%` at render.
- The unit language must match the page language: EN uses "IDR bn", ID uses "Rp miliar", ZH uses "十亿盾". Do NOT mix "亿" with "十亿盾" within ZH text — be consistent.

---

## 5. Design system

### Colors (CSS variables)

```
--green: #1F5E40      (primary brand, headers, up-trend)
--green2: #4A8B66
--teal:   #3E7D6B
--amber:  #C07A2D     (warning)
--clay:   #B04A2E
--soft:   #C7D0C8     (background panel)
--blue:   #2E6FB0     (secondary series)
--purple: #7A5BA6
--red:    #C0392B     (down / risk)
--gold:   #D9A53A
```

- Use **visually distinct hues** for different series on the same chart — never two green lines or two similar blues on one chart. The user explicitly flagged "don't use the same color family for different indicators."
- Risk colors: green #2E7D32 (low), amber #C07A2D (elevated), red #C0392B (high).
- Background: off-white #F7F6F2; panels white; text near-black #1A1A1A.

### Typography

- Sans-serif system stack; **bold weight for top-nav tabs** (user requirement).
- Hierarchy: page H2 ~22px, block H3 ~15px bold, body 13–14px, table 12–13px, footnote 11px.
- Numbers right-aligned in tables; use tabular-nums.
- No emojis. Use inline SVG for icons only.

### Layout

- Top dark-green hero bar: logo "K", company name, ticker, tagline, language switcher (EN / ID / 中文).
- Below hero: horizontal nav tabs (one per page), **bold** when active.
- Content: max-width ~1200px, centered, padding 24px.
- KPI cards: grid of equal-width white cards (responsive 4/2/1 columns). Each: small label, big number, unit, delta chip (up/down/flat colored).
- Charts: white card with title + subtitle (`.sub`) + ECharts canvas (~420px tall).
- Tables: `table-layout: fixed`, every `<col>` has explicit width summing to 100%. Numbers right-aligned. Thousands separators where integers.
- Footer: compact inline source links (show source name, not URL), one-line disclaimer. **No version number, no changelog, no update date on the public page.** Keep `CHANGELOG.md` in the repo only.

### Chart rules (ECharts)

- Default: `tooltip.trigger: 'axis'`, `axisPointer.type: 'shadow'` for bar, `'line'` for line.
- Toolbox: a **tiny ~9px download PNG icon** in bottom-right of each chart. The user complained it was too large twice — keep it small.
- **Horizontal bars preferred** for P&L snapshots and balance sheet snapshots (year pages). Vertical bars for cash bridge.
- Dual-axis allowed only when two series are genuinely different units; label axes clearly.
- Bar charts must start at zero axis.
- Multi-series: use legend; colors from distinct hues.
- No 3D charts, no rainbow palettes.
- Chart subtitles (`.sub` div under each title) must carry units for every number mentioned.

---

## 6. i18n (three-language) rules

- All UI strings in an inline `I18N` object with three parallel blocks: `en: {...}, id: {...}, zh: {...}`.
- Every user-visible string goes through `data-i18n="key"` in HTML or `I18N.key` in JS.
- **Strict separation**: when LANG = 'id', every word on the page (chart subtitles, table headers, tooltips, footnotes, narrative paragraphs) is Indonesian. No English sentences glued in. Same for ZH.
- Financial abbreviations (EBITDA, ROE, P/B, DSO, FCF, NCI, SEZ, JV) may stay as Latin letters in all three languages.
- **Number units must follow the language**: EN uses "IDR bn" / "bn"; ID uses "Rp miliar" / "miliar"; ZH uses "十亿盾" (not "亿", not "万亿" unless truly trillion-scale).
- Switching language re-renders the whole page.

---

## 7. Hover glossary (the `?` superscript)

- For every professional term / acronym, append `<sup class="glos" data-term="XXX">?</sup>`.
- Hover shows tooltip with definition. **Definition language matches the active page language.**
- **Only mark the FIRST occurrence of a term per page.** Subsequent identical terms on the same page must NOT get another `?`. (User requirement.)
- Definitions from GLOS in data.json; 1–2 sentences each, based on professional finance/industry terminology.

---

## 8. Pages (nav order, left to right)

1. **Overview** — KPI cards, revenue trend bar chart, net profit consolidated vs parent (solid vs dashed), margins & leverage, segment revenue (Real Estate vs Infrastructure), marketing sales, EBITDA trend. Chart subtitle: time range and units.
2. **Profitability** — gross / EBITDA / net margin trend (2015–2025), ROE vs ROA, EBITDA vs net profit bars+line, revenue vs gross margin dual-axis, FCF and FCF margin. Add 1H26 annualized where useful.
3. **Debt & Solvency** — KPI cards (total debt, avg cost, cash, net debt, EBITDA/interest, net debt/EBITDA), debt-by-lender chart, maturity ladder, solvency trend, cash vs debt, debt instruments table, credit ratings, refinancing recap, **working capital table** (AR, AR long-term, AP, customer deposits, DSO/DPO by year).
4. **Land Bank** — KPI cards (total ha, dev ha, book value, implied uplift), per-project table with ha / dev ha / book value / book per sqm / market low / market high / uplift.
5. **Valuation** — KPI cards (price, 52wk range, market cap, P/B, P/E, dividend yield), 12-month share price chart with volume bars below, price range per month, trading snapshot (volume, turnover, RSI, DMA), peer comparison, analyst targets.
6. **Valuation Illustration** — method comparison table: P/E, P/B, DCF, liquidation value, landbank value per share at 100/75/50/25%. Each row: method, input, implied value per share, vs current price, safety margin. Landbank per-share in a **separate table**, not combined with other methods.
7. **Risk & Direction** — data-derived risk rows (colored green/amber/red), **Top 3 improvement actions** (each tied to a measurable data gap), **Market opportunities** (current macro context, sourced).
8. **Holding Structure** — subsidiaries table: entity, activity, via, ownership %, assets, status.
9. **Organization** — corporate facts, boards, committees, key people.
10. **FY20XX / FY20XX / 1H20XX** annual deep-dive pages (most recent three, rightmost in nav).

### Year-page pattern (CRITICAL)

Each annual deep-dive page uses a consistent 4-chart layout:
1. **Revenue mix pie** (segment breakdown for that year)
2. **P&L snapshot** (horizontal bars: Revenue, EBITDA, NP consolidated, NP parent — with unit in subtitle)
3. **Balance sheet snapshot** (horizontal bars: Assets, Liabilities, Equity)
4. **Cash bridge** (vertical bars: opening cash + net change = closing cash)

Below charts: event timeline panel + risk indicators panel + narrative paragraph.

- **Period-appropriate data only**: FY2024 page must NOT show 2025 data. FY2025 page must NOT show 2026 data. 1H2026 page shows 1H26 vs 1H25 comparison.
- Cash bridge labels are year-specific: "Opening cash (end-2023)" / "Consolidated surplus 2024" / "Closing cash (end-2024)" for FY2024; "Opening cash (end-2024)" / "Consolidated surplus 2025" / "Closing cash (end-2025)" for FY2025.
- Chart axis labels and legend keys must be clean words (e.g. "Infrastructure", "Real estate"), NOT raw variable names (e.g. "infraPie", "revL").

---

## 9. Data integrity rules

- **Audit numbers from official annual reports** (company IR website + IDX). For 10-year history, use the latest AR's 5-year summary + earlier ARs for older years. The 2016 AR contains full audited 2015 comparatives.
- When a metric can't be derived from disclosed line items (e.g. EBITDA early years when D&A not broken out), **compute conservatively** and note the assumption. Don't leave a chart point blank if a reasonable estimate exists.
- Cross-check: revenue, net profit, EBITDA, CFO, capex, total debt, cash must tie across income statement, balance sheet, and cash flow.
- Mark unaudited/interim data clearly.
- **Every number in narrative text, chart subtitle, event description, and risk note must carry its unit.** See section 4 number rules.
- **Sources**: footer lists every annual report by name (clickable to PDF), latest interim, investor presentation, IDX, and 1–2 third-party references. Show the name, link it — don't show raw URLs.

### Derived metrics — compute from source arrays, never copy from narrative

When writing narrative text (TOP3, OPP, RK, g24/g25/g26, DEC table), **do not hand-type derived numbers**. Pull them from the structured arrays:

| Metric | Formula | Source arrays |
|---|---|---|
| Net debt | `total interest-bearing debt − cash` | `DEBT.cashDebt.debt − DEBT.cashDebt.cash` |
| Net debt / EBITDA | `netDebt / AN.ebitda[yr]` | must match `DEBT.cov.nd` |
| DSO | `AR / revenue × 365` | `WC.ar / WC.revenue` |
| GPM peak year | `argmax(AN.gpm)` | `AN.gpm` vs `AN.years` |
| Marketing sales per quarter | sum of EV event entries | `EV.ev26` text |

**Critical distinction: total liabilities ≠ total debt.** Total liabilities (`AN.liab`) includes trade payables, customer deposits, tax, accrued expenses — NOT just interest-bearing borrowings. The g25 narrative once wrote "gross debt 6,904bn" when the actual interest-bearing debt was 4,607bn; 6,904 was total liabilities. Net debt uses interest-bearing debt only.

### Cross-page consistency audit (run before shipping)

Every number in the Risk & Direction page, annual-page narrative, and comparison table must reconcile to the structured data:
- TOP3/OPP claims → verify against `AN`, `WC`, `EV` arrays
- DEC table columns are `[1H26, FY<latest>, FY<previous>]` — do not shift values between years
- Risk rows (`RK`) → verify level scores and notes match the KPI cards on their respective pages
- Narrative text period references (e.g. "FY2025 cash 3.6tn") must match the correct year's data

---

## 10. Auto-updating stock price (GitHub Action)

- `.github/workflows/update-price.yml` runs weekdays ~09:30 UTC.
- `.github/scripts/update_price.py` fetches from Yahoo Finance `query1.finance.yahoo.com/v8/finance/chart/<TICKER>.<exchange>`, extracts latest close, updates `VAL.close[last]` and KPI cards in `data.json`, commits and pushes.
- Note: Yahoo Finance API does NOT send CORS headers, so this must run server-side (GitHub Action), not in the browser.

---

## 11. Verification before pushing

1. Run `python "<skills>/html/scripts/shot.py" index.html --only desktop` to screenshot.
2. Read the screenshot. Check:
   - No blank charts
   - No raw variable names in chart labels (e.g. `revL`, `infraPie`)
   - No mixed languages
   - Numbers have units
   - Layout is clean, no overlapping elements
3. Check `consoleErrors` in shot.py report is `[]`.
4. Commit and push.
5. Tell user to hard-refresh (Ctrl+F5).

---

## 12. Recurring gotchas (learned the hard way)

1. **data.json overrides inline JS at runtime.** If you edit index.html but not data.json, the user sees old data. Always update both.
2. **Missing CHT keys = blank charts or raw labels.** If a chart shows "infraPie" instead of "Infrastructure", the label key is missing from CHT in data.json.
3. **GitHub Pages CDN cache.** If user says "no change", verify `git log --oneline -1` matches what you pushed, wait 90s, tell them to Ctrl+F5.
4. **PowerShell here-strings fail silently** on multi-line JS replacement. Use Python scripts with `assert old in content` for exact matching.
5. **Don't show changelog/version/update-date on the public page.** Keep it in CHANGELOG.md locally.
6. **Don't add hover glossary to repeated terms** on the same page; first occurrence only.
7. **Don't use dual-axis charts by default.**
8. **Numbers must tie to units.** Every written number needs its unit. This is the most-violated rule across iterations.
9. **Don't mix unit languages.** ZH must not use "亿" when meaning "十亿盾". "万亿盾" is wrong for IDR bn figures (should be "十亿盾").
10. **Year pages must be period-appropriate.** FY2024 page must not show 2025 data.
11. **Chart download icons must be small.** ~9px. The user complained twice.
12. **Distinct colors for different series.** Never two green lines on one chart.
13. **Horizontal bars for P&L/BS snapshots**, vertical bars for cash bridge.
14. **Positive numbers get no "+" sign.**
15. **Tables: explicit column widths** summing to 100%, numbers right-aligned, thousands separators.
16. **Total liabilities ≠ total debt.** Interest-bearing debt excludes trade payables, customer deposits, tax, accruals. Net debt = interest-bearing debt − cash. Verify from `DEBT.cashDebt`, not from balance-sheet total liabilities.
17. **Narrative numbers must tie to structured arrays.** If you write "GPM peaked at 52%", check `AN.gpm` to find WHICH year — don't assume it was the land-sale era. If you write "1Q26 sales were X", check the EV timeline. A wrong year label is worse than no label.
18. **DEC comparison table columns are ordered** `[1H26, FY<latest>, FY<previous>]`. Don't mix FY2023 numbers into the FY2024 column.
19. **fmtN() already handles number formatting** — integers strip trailing `.0`, non-integers show 1 decimal, thousands separators auto-added. Don't hand-format numbers in narrative text; use the function for chart labels.

---

## 13. How to bootstrap a new company

1. Create repo on GitHub, enable Pages from `main`.
2. Copy this project's `index.html` and `data.json` as templates. Strip company-specific data but keep structure.
3. Collect 10 years of annual report PDFs from company IR site + exchange.
4. Extract income statement / balance sheet / cash flow into `data.json → AN` arrays.
5. Fill KP, DEBT, LAND (or core asset class), VAL, FY blocks from latest AR + interim.
6. Translate all UI strings into EN/ID/ZH.
7. Set up the GitHub Action for price auto-update (edit ticker in `update_price.py`).
8. Screenshot each page, fix layout, commit, push.
9. Ship the URL.

---

## 14. Annual-report extraction checklist

For each year (2015 through latest), pull these line items. Units: local currency bn. Use the 5-year comparative summary in the latest AR for N-4..N; earlier ARs for older years. Cross-check across three statements.

### Income statement
- Revenue, cost of revenue, gross profit (→ gross margin)
- Operating profit / EBIT, interest expense, tax
- Net profit consolidated / attributable to parent / NCI
- D&A (from cash flow statement) → EBITDA = niCons + tax + interest + D&A
- If D&A not disclosed early years: estimate conservatively, no note needed for very old years

### Balance sheet (year-end)
- Cash, total debt (net of unamortized issuance cost), AR, AR long-term, inventory/land bank
- Total assets, total equity (consolidated + parent), AP, customer deposits

### Cash flow statement
- CFO, capex, land acquisition, FCF conservative = CFO - capex - land acquisition

### Operating metrics (MD&A)
- Segment revenue split, marketing sales/pre-sales, land bank by project (ha), employee count

### Ratios to compute
- Gross margin, EBITDA margin, net margin, ROE, ROA, FCF margin
- DSO = AR / revenue × 365; DPO = AP / COGS × 365
- Net debt / EBITDA, EBITDA / interest, Liabilities / equity

### Market data (latest)
- Share price, market cap, 52-week range, P/E, P/B, dividend yield
- 12-month monthly close + volume + price range
- Credit ratings

### Debt details (latest balance sheet date)
- Each lender: principal, rate, maturity, collateral, status
- Maturity ladder by year, refinancing events (one-off costs broken down), average cost

### Holding structure & org (latest AR)
- Subsidiaries: name, activity, ownership %, via, assets, status
- Boards, committees, key people

### Sources (footer)
- Every AR PDF (by name, linked), latest interim, investor presentation, exchange, 1–3 third-party refs
