# KIJA Dashboard — Changelog (internal, not shown on page)

## v1.10.0 – 2026-10-02
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
- SOTP illustration illustration added
