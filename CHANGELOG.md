# KIJA Dashboard — Changelog (internal, not shown on page)

## v1.13.2 – 2026-10-03
- o3 chart (Margins & leverage trend): removed 1H26 data point, markPoint and x-axis category; title/subtitle now "(2015–2025)" in en/id/zh (half-year figure not comparable with annual margins/leverage series)
- o3 data re-verified vs audited financial statements (all 11 years): GPM [44.2,42,38,43,37,43,44,52,46,43,39] ✓ (2015 GP 1,388.5bn/2016 1,243.2bn/2017 1,136.9bn/2018 1,179.0bn/2019 843.5bn/2020 1,018.4bn/2021 1,092.6bn/2022 1,427.2bn(2023 AR restated)/2023 1,530.3bn/2024 1,967.2bn/2025 2,033.0bn); NPM/ROE/D-E recomputed from official revenue/niCons/equity/liab series — all consistent

## v1.13.1 – 2026-10-03
- Fix: "h26note" literal key leaked into o1 tooltip ("h26note; vs 1H25: -11%") — key was defined in I18N but CT() reads CHT; added h26note to CHT en/id/zh in both index.html and data.json
- Data re-verified for o1 Revenue chart vs official audited statements: 2015-18 from 2018 AR highlights (3,140/2,931/2,995/2,712), 2019-20 from 2020 AR text (2,254/2,396), 2021 from 2022 FS Note 27 (2,490.3), 2022 from 2023 FS Note 27 restated comparative (2,747.2; 2022 FS shows 2,720.3 under older line-item split — system uses 2023 AR comparative, consistent with prior restatement basis), 2023-25 audited (3,291.9/4,602.6/5,149.4), 1H26 2,436.5 (Q2 2026 interim). "vs 1H25: -11%" recomputed = 2,436.5/2,726.4-1 = -10.6% ≈ -11% ✓

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

## 2026-10-03 — Data verification: parent net profit
- Fixed AN.niParent 2016: 426.1 → 436.6 (audited FS 2016: parent 436,615,675,735; NCI -10,073,353,230)
- Fixed AN.niParent 2018: 112.5 → 41.0 (audited FS 2018/2019: parent 40,971,008,075; NCI +26,129,394,868; EPS 1.97)
- Cross-checked all years 2015-2025 vs official audited FS (2016, 2018, 2019, 2020 AR, 2022, 2023, 2024, 2025): only 2016 & 2018 were wrong
