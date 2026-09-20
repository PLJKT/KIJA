# KIJA Dashboard — Master Playbook

> Purpose: hand this file to any AI, give it a listed company ticker (and optionally its official annual report PDFs), and it should produce a financial-operations dashboard that looks, feels, and behaves like the KIJA dashboard (https://pljkt.github.io/KIJA/).
>
> Read this top-to-bottom before writing any code. Treat every rule below as a hard constraint unless the user explicitly waives it.

---

## 1. Deliverable shape

- **One static site** hosted on **GitHub Pages** from the `main` branch, served at `https://<user>.github.io/<repo>/`.
- **Single-page app (SPA)** with in-page hash routing between "pages" (sections). No server, no build step beyond a Python concatenation script.
- **Offline-capable**: all data is embedded in `data.json` at build time; the page also tries to fetch `data.json` at runtime and falls back to the embedded copy.
- **Three languages, strict**: English (default), Bahasa Indonesia, 中文. Language switcher in the header (EN / ID / 中文). Once a language is chosen, **every visible string must be in that language** — no mixed paragraphs, no mixed numbers units, no leftover English in a ZH view. If a string is missing for the selected language, fall back to English rather than leaving blank, but flag it.
- Desktop-first, responsive down to mobile.

---

## 2. Repository layout

```
<repo>/
  index.html          # built artifact (committed, what GitHub Pages serves)
  data.json           # single source of truth for all data + i18n strings
  analysis_en.md      # long-form narrative report (linked from footer)
  analysis_id.md
  analysis_zh.md
  README.md
  CHANGELOG.md        # internal only, NOT shown on page
  _shots/             # self-screenshots from shot.py (gitignore optional)
  _kija_build/        # build sources (or rename to _build/)
    build.py
    head.html
    body.html
    js_a.html         # i18n dictionary (3 language blocks)
    js_b.html         # render logic, chart options, DOM wiring
```

Rename `_kija_build/` to `_build/` when starting a new project; the pipeline is identical.

---

## 3. Build pipeline (build.py)

`build.py` **concatenates, it does not bundle**. Order:

```
head.html  +  body.html  +  js_a.html  +  data_block()  +  js_b.html
```

- `data_block()` reads `data.json` and emits one `<script>` block:
  `var KP = {...}; var EV = {...}; ...` for every key listed in `DATA_KEYS`.
- **Critical pitfall**: there is no `js_c.html`. If you edit a file that is not in this list, the change never reaches `index.html`. All data must go through `data.json`; all render logic through `js_b.html`.
- Run full build: `python build.py` → writes `../<repo>/index.html`.
- Run single page test: `python build.py <page_name>` → writes `_build/_test_<page>.html` (page name must be in the hardcoded allowlist).
- `build.py` also runs an HTML tag-balance check; it exits non-zero on mismatch.
- On Windows, always run from PowerShell. Avoid `&&`, `$()`, heredocs; put multi-line logic in a `.py` file and run `python xxx.py`. The Edit tool on Windows frequently reports "File has not been read" even right after Read; batch edits are more reliable as a Python script that does string replacement and writes back.

---

## 4. data.json schema (canonical blocks)

Top-level keys (add or remove per company, but keep names stable once shipped):

| Key | Purpose |
|---|---|
| `KP` | KPI cards per page, per language: `KP.overview.en/id/zh`, `KP.debt`, `KP.prof`, `KP.val`, `KP.lb` etc. Each card: `{l, v, u, d, c}` where c ∈ up/dn/flat |
| `EV` | Headline EV/EBITDA comps |
| `RK` | Risk indicator rows `{n, v, lv}` where lv 0=green, 1=amber, 2=red |
| `DIR` | Direction / strategy blocks |
| `TL` | Timeline entries `[year, text]` per language |
| `OWN`, `SUBS`, `BIZ`, `VIA` | Holding structure, subsidiaries, business pillars |
| `PILLAR`, `PILLAR_MAP`, `ORG` | Pillar revenue split, org chart data |
| `DEBT` | Lenders, maturity ladder, cash/debt series, debt instruments table, ratings, refinancing history, risk rows |
| `WC` | Working capital: receivables, payables, DSO/DPO series |
| `LAND` | Land bank per project (ha, book value, market comparison) |
| `VAL`, `VALI`, `LIQ`, `LBV` | Valuation methods (P/E, P/B, DCF), valuation illustration table, liquidation value, landbank value per share at 100/75/50/25% |
| `DTXT`, `LTXT`, `VTXT`, `NXT` | Page narrative text per language |
| `KEYP` | Key people / boards |
| `AN` | Annual series 2015–latest: `AN.years[]` + parallel arrays (revenue, niCons, niParent, ebitda, cfo, capex, landAcq, fcfCons, grossMargin, etc.). **Every array must be same length as years**; build.py validates this. |
| `CHT` | Chart data series referenced by render code |
| `FY` | Per-year annual-report page blocks (k24/k25/k26 etc.) |
| `GLOS` | Hover glossary: maps term → `{en, id, zh}` short explanations. Used by the `?` superscript tooltip. |
| `TOP3`, `OPP` | Top-3 improvement actions and market opportunities (Risk & Direction page) |
| `meta` | Page title, subtitle, as-of date, units |

**Number rules**
- All numbers in IDR billion (or millions for share counts). State unit explicitly in every chart axis, table header, and KPI card (`u` field).
- Display rounding: **one decimal place, round half up**. No raw integers for financials.
- Negative numbers: prefix with `−` (U+2212), not hyphen.
- Percentages: store as number (e.g. `39`), format with `%` at render.

---

## 5. Design system

### Colors (CSS variables in head.html)

```
--green: #1F5E40      (primary brand, headers, up-trend)
--green2: #4A8B66
--teal:   #3E7D6B
--amber:  #C07A2D     (warning)
--clay:   #B04A2E
--soft:   #C7D0C8     (background panel)
--blue:   #2E6FB0     (secondary series, infrastructure)
--purple: #7A5BA6
--red:    #C0392B     (down / risk)
--gold:   #D9A53A
```

- Use **visually distinct hues** for different series on the same chart — never two green lines on one chart.
- Risk colors: green #2E7D32 (low), amber #C07A2D (elevated), red #C0392B (high).
- Background: off-white #F7F6F2; panels white; text near-black #1A1A1A.

### Typography

- Sans-serif system stack; **bold weight for top-nav tabs** (user requirement).
- Hierarchy: page H2 ~22px, block H3 ~15px bold, body 13–14px, table 12–13px, footnote 11px.
- Numbers right-aligned in tables; use tabular-nums where possible.
- No emojis. Use inline SVG for icons only.

### Layout

- Top dark-green hero bar: logo "K", company name, ticker, "Industrial Estate Developer · Financial & Operations Monitor", language switcher.
- Below hero: horizontal nav tabs (one per page), bold when active.
- Content: max-width ~1200px, centered, padding 24px.
- KPI cards: grid of equal-width white cards (responsive 4/2/1 columns). Each card: small label, big number, unit, delta chip (up/down/flat colored).
- Charts: white card with title + subtitle + ECharts canvas (~420px tall on desktop).
- Tables: `table-layout: fixed`, every `<col>` has explicit width summing to 100%. Row zebra or hairline borders only.
- Footer: small print, compact inline source links (one line, wrapped naturally), "This dashboard is for information only…" disclaimer. **Do not put version number or changelog on the public page.**

### Chart rules (ECharts)

- Default: `tooltip.trigger: 'axis'`, `axisPointer.type: 'shadow'` for bar, `'line'` for line.
- Toolbox: a small **9px download PNG icon in the bottom-right corner** of each chart (half the previous size per user feedback). Don't make it big.
- Dual-axis allowed only when absolutely necessary; label axes clearly.
- Bar charts must start at zero axis.
- Multi-series: use legend; colors from the palette above, distinct hues.
- No 3D charts, no rainbow palettes.
- No animation on load beyond a simple fade.

---

## 6. i18n (three-language) rules

- All UI strings live in `js_a.html` in three parallel blocks (EN / ID / ZH). Each key appears three times with same key name.
- Every user-visible string goes through `data-i18n="key"` in HTML or a render call `I18N.key`.
- **Strict separation**: when LANG = 'id', every word on the page (including chart subtitles, table headers, tooltips, footnotes) is Indonesian. No English sentences glued in. Same for ZH.
- Financial abbreviations (EBITDA, ROE, P/B, DSO, FCF, NCI, SEZ, JV) may stay as Latin letters in all three languages, but the surrounding explanation must be in the active language.
- Switching language re-renders the whole page (call `applyLang()` after setting LANG).

---

## 7. Hover glossary (the `?` superscript)

- For every professional term / acronym, append a small `<sup class="glos" data-term="XXX">?</sup>`.
- Hovering shows a tooltip with the definition. **Definition language matches the active page language.**
- **Only mark the FIRST occurrence of a term per page.** Subsequent identical terms on the same page must NOT get another `?`. (User requirement.)
- Definitions come from GLOS in data.json; write them in plain English first, then translate. Keep each to 1–2 sentences.

---

## 8. Pages (nav order, left to right)

Start with these; adapt names to the company:

1. **Overview** — 6–8 KPI cards, revenue bar chart, net profit trend, margins & leverage, segment revenue, marketing sales, EBITDA trend.
2. **Profitability** — gross / operating / net / EBITDA margin trend, ROE/ROA, FCF margin, FCF itself. Include annualized 1H figures where useful.
3. **Debt & Solvency** — total debt, avg cost, net debt, EBITDA/interest, net debt/EBITDA, lender breakdown, maturity ladder, cash vs debt series, debt instruments table, credit ratings, refinancing history, working capital (receivables/payables/DSO/DPO).
4. **Land Bank** (or the company's core asset class) — per-project table with ha, book value, market price comparison.
5. **Valuation** — market cap, price, 52-week range, P/E, P/B, dividend yield, peer comps, analyst views, 12-month share price chart with volume bars below, turnover & price range snapshot.
6. **Valuation Illustration** — methods table (P/E, P/B, DCF, liquidation value, landbank value per share at 100/75/50/25%), each with implied value vs current price, safety margin.
7. **Risk & Direction** — risk rows colored by level, top-3 improvement actions, market opportunities (write with current macro context).
8. **Holding Structure** — subsidiaries table: entity, activity, via, ownership, assets, status.
9. **Organization** — corporate facts, boards, committees, key people.
10. **FY2024 / FY2025 / 1H2026** annual deep-dive pages (most recent three, rightmost in nav).

---

## 9. Data integrity rules

- **Audit the numbers from official annual reports** (company IR website + IDX). For a 10-year history, use the most recent AR's 5-year summary and earlier ARs for the rest.
- When a metric can't be derived from disclosed line items (e.g. EBITDA pre-2019 when D&A not broken out), **compute conservatively** and note the assumption; do not leave the chart with a missing point if a reasonable estimate exists.
- Cross-check: revenue, net profit, EBITDA, operating cash flow, capex, total debt, cash — these must tie across the income statement, balance sheet, and cash flow statement.
- Mark unaudited / interim data clearly ("1H26, unaudited").
- **Sources**: footer lists every annual report by name (clickable to PDF), the latest interim report, investor presentation, IDX, and 1–2 third-party market references (CBRE/JLL/Moody's). Don't show raw URLs as text — show the name, link it.

---

## 10. Deployment & verification

- After every change:
  1. `python build.py`
  2. `python build.py <page>` to test the changed page
  3. Screenshot: `python "<skills>/html/scripts/shot.py" _test_<page>.html --only desktop`
  4. Read the screenshot, check layout, no overlap, no mixed languages, numbers one decimal.
  5. `git add -A && git commit -m "Rnn: short description" && git push origin main`
- GitHub Pages takes ~60–90s to deploy. Verify live with a cache-buster query (`?v=2`) if the user reports "still old".
- The shot.py script also reports `consoleErrors`; must be `[]` before shipping.

---

## 11. Recurring gotchas (learned the hard way)

1. **build.py does not include js_c.html or any ad-hoc file.** If you edit a file and nothing changes, check whether it's in the concatenation list.
2. **KP cards read from `data.json → KP.<page>`**, not from `DEBT.kpi26` or similar. If a KPI card isn't updating, grep both places.
3. **Regex `replace('a','b')` over an i18n block**: if you call it three times for three languages but the pattern matches the same first occurrence each time, you'll overwrite the EN string with the ID, then ZH. Better to replace by line number or anchor on the language block marker.
4. **GitHub Pages CDN cache**: if user says "no change", check `git rev-parse HEAD` matches `origin/main`, wait 90s, then re-fetch with cache-buster.
5. **PowerShell quoting**: use a `.py` file for anything with quotes, `$`, or loops.
6. **Don't show changelog or version on the public page.** Keep `CHANGELOG.md` in the repo only.
7. **Don't add a separate "Sources" page if the user wants it inline** — footer compact list is preferred.
8. **Don't use dual-axis charts by default**; only when two series are genuinely different units.
9. **Don't add hover glossary to repeated terms** on the same page; first occurrence only.
10. **Numbers must tie to their units**: every written statement like "revenue grew 12%" must correspond to a card/chart with the same unit (IDR bn) and same period.

---

## 12. How to bootstrap a new company

1. Create repo `<TICKER>-dashboard` on GitHub, enable Pages from `main`.
2. Copy this folder's `_build/` structure (head.html, body.html, js_a.html, js_b.html, build.py) as a template.
3. Collect 10 years of annual report PDFs from the company IR site + exchange.
4. Extract income statement / balance sheet / cash flow into `data.json → AN` arrays (years 2015–latest).
5. Fill KP, DEBT, LAND (or asset class), VAL blocks from the latest annual report and interim.
6. Translate all UI strings into EN/ID/ZH.
7. Run `python build.py`, screenshot each page, fix layout, push.
8. Ship the URL.

---

## 13. When the user asks for changes

- One request = one commit with a short message starting `Rnn:`.
- Always verify visually (shot.py) before saying done.
- If a request is ambiguous, ask one clarifying question before coding.
- Keep responses short; the dashboard is the deliverable, not the chat.

---

## 14. Annual-report extraction checklist

For each year (2015 through latest), pull these line items from the audited financial statements. Units: IDR billion (or local currency bn). Use the **5-year comparative summary table** in the latest annual report for years N-4..N, and earlier annual reports for older years. Cross-check every number across the three statements.

### Income statement
- Revenue / sales (`revenue`)
- Cost of revenue -> gross profit (`grossProfit`, derive gross margin)
- Operating profit / EBIT
- Interest expense (`interest`)
- Income tax expense (`tax`)
- Net profit (consolidated) (`niCons`)
- Net profit attributable to parent (`niParent`)
- Non-controlling interest (NCI)
- Depreciation & amortization (`da`) -- often in cash flow statement
- **EBITDA** = niCons + tax + interest + D&A (or operating profit + D&A). If D&A not disclosed for early years, estimate conservatively and note it.

### Balance sheet (year-end)
- Cash & equivalents (`cash`)
- Total debt (short-term + long-term borrowings, net of unamortized issuance cost) (`debt`)
- Accounts receivable, net (`ar`)
- Inventory / land held for development / land bank (`landBank`)
- Total assets (`assets`)
- Total equity (consolidated) and equity attributable to parent (`equity`, `equityParent`)
- Accounts payable (`ap`)
- Customer deposits / advances (`custDep`)

### Cash flow statement
- Cash flow from operations (`cfo`)
- Capital expenditures / purchase of PP&E (`capex`)
- Purchase of land / land acquisition (`landAcq`)
- Free cash flow (conservative) = `cfo - capex - landAcq` (`fcfCons`)

### Operating metrics (from MD&A / operating review)
- Segment revenue (real estate, infrastructure, hospitality etc.) -- split per pillar
- Marketing sales / pre-sales (for property developers)
- Land bank in ha by project
- Employees count (for per-capita metrics)

### Ratios to compute
- Gross margin = grossProfit / revenue
- EBITDA margin = EBITDA / revenue
- Net margin = niCons / revenue
- ROE = niCons / avg total equity
- ROA = niCons / avg total assets
- FCF margin = fcfCons / revenue
- DSO = AR / revenue x 365
- DPO = AP / COGS x 365
- Net debt / EBITDA = (debt - cash) / EBITDA
- EBITDA / interest coverage = EBITDA / interest expense
- Liabilities / equity

### Market data (latest)
- Share price, market cap, 52-week range
- P/E, P/B, dividend yield
- 12-month daily close price + volume (for price chart)
- Credit ratings (Fitch / Moody's / S&P)

### Debt details (latest balance sheet date)
- Each lender / bond: principal, rate, maturity, collateral, status (current / repaid)
- Maturity ladder by year
- Refinancing events (one-off costs, FX losses, derivative termination)
- Average cost of debt

### Holding structure & org (latest AR)
- List of subsidiaries: name, activity, ownership %, via (intermediate holding), assets, status
- Board of commissioners / directors / audit committee names
- Employees count, year founded, listed date

### Sources to cite (footer)
- Every annual report PDF (2015-latest) by name, linked
- Latest interim report (Q2 / 1H)
- Latest investor presentation
- Exchange announcements page
- 1-3 third-party references (rating agency, market research)

---

## 15. Template location

A stripped copy of the build pipeline lives in `_template/` next to this file. Copy it as `_build/` for a new project; see `_template/README.md` for bootstrap steps.
