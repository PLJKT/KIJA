# KIJA Dashboard — Changelog (internal, not shown on page)

## v1.13.0 – 2026-10-02
- Cross-check fixes from third-party AI review (9.5/10): real estate ownership in segment table filled "51–100" (100% wholly-owned Cikarang + 51% Kendal JV)
- Land Bank note strengthened in en/id/zh: asking prices are listing prices, not transaction prices; negotiated deals can close well below advertised; implied uplift is a theoretical upper bound, not a realisable value (10–20% discount figure from review deliberately NOT adopted — no source)
- 1H26 parent vs consolidated loss already explicitly labelled (parent -177.9 / consolidated -6.4 / NCI +171.4); FY-label convention kept as-is (uniform FY2025 + hover glossary)

## v1.12.0 – 2026-10-01
- Live share price sync: GitHub Action (`update_price.py`, Yahoo v8 chart) fetches daily close and writes `FY.refPrice`; Valuation KPIs, KEYP derived rows, LIQ/LBV, peer comparison all recompute automatically
- vi-1 chart redesign (multiple iterations): floating range bars + base dot + Current Price red bar on independent stack with exact length; per-method distinct colors (P/E blue, P/B purple, DCF orange, SOTP grey-blue, Current Price red); slim legend Price + Base; SOTP single target as grey bar
- Peers comparison extended to 4 names: KIJA · DMAS · BEST (Bekasi Fajar) · LPCK (Lippo Cikarang); BEST/LPCK use latest 1H26 / FY25 audited basis (apple-to-apple with KIJA); all P/B, P/E, P/S, YTD live-derived
- update_price.py now fetches 4 tickers (KIJA/DMAS/BEST/LPCK), writes FY.best/FY.lpck + peer columns

## v1.11.0 – 2026-09-20
- Working capital data added to Debt & Solvency: AR, AR long-term, AP, customer deposits, DSO/DPO by year (only theme-relevant data, cross-checked vs history)
- Glossary extended; pre-elimination hover explanation added; segment table wording fixes (Segment total (pre-elimination), no "+" on positives, ownership column, thousand separators, GPM/NPM columns)
- 2015 EBITA/EBI margin series completed (conservative estimate from AR2016 audited comparatives, no note needed for old years)

## v1.10.0 – 2026-09-19
- Peers comparison extended from DMAS-only to 4 names: KIJA · DMAS · BEST (Bekasi Fajar) · LPCK (Lippo Cikarang)
- v-2 chart (P/B & P/S): 4 series with distinct colors; caption lists all 4 live prices
- Peers table: 5 columns × 6 rows; P/B, P/E, P/S, YTD live-derived for all four (FY25 audited constants)
- update_price.py now fetches 4 tickers (KIJA/DMAS/BEST/LPCK) and writes back FY.best/FY.lpck + peers cols 3–4
- BEST/LPCK FY25 audited constants added (BEST: rev 427.1, EPS 3.12, BVPS 461.8, no dividend since FY18; LPCK: rev 4519.2, EPS 48, BVPS 1302.2, no FY25 dividend)
- Glossary entries added for BEST / LPCK; heading, note and description reworded in en/id/zh

## v1.9.0 – 2026-09-19
- Footer: "Updated per 19 Sep 2026" (changelog removed from public page, kept here)
- ECharts saveAsImage (PNG) on every chart; floating CSV export of active-page tables
- aria-labels on nav / language toggle
- Growth-driver & highlights panel at end of FY2024 / FY2025 / 1H2026 (en/id/zh)
- YoY% added to revenue (o1) and net-profit (o2) tooltips

## v1.8.0 – 2026-09-19
- Price chart changed to dual-pane (price line + volume bars)
- Tooltip: monthly price range, volume, turnover (IDR bn), turnover rate
- Monthly volume recomputed by aggregating Yahoo daily bars

## v1.7.0 – 2026-09-18
- Corrected monthly traded volume (Yahoo 1mo interval mislabeled months)
- Market cap card placed before Price on Valuation page
- SOTP illustration added
