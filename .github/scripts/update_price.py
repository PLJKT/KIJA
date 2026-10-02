#!/usr/bin/env python3
"""Fetch latest KIJA.JK closing price from Yahoo Finance and update data.json."""
import json
import sys
import urllib.request
from datetime import datetime, timezone

DATA_FILE = "data.json"
TICKER = "KIJA.JK"
DMAS_TICKER = "DMAS.JK"
SHARES_BN = 20.59  # weighted avg shares (bn)
EPS = 20.55        # FY25 audited EPS (IDR)
BVPS = 304.1       # parent BVPS (IDR)
DPS = 2.03         # FY25 dividend per share (IDR)
# DMAS (PT Puradelta Lestari) audited FY2025 (AR2025, IDX)
DMAS_SHARES_BN = 48.198   # issued & paid-up shares (bn)
DMAS_REV_BN = 1309.1      # FY25 audited revenue (bn)
DMAS_EPS = 16.60          # FY25 audited attributable EPS (800.3/48.198)
DMAS_BVPS = 137.14        # FY25 audited parent BVPS (6,609.8/48.198)
DMAS_DPS = 16.5           # FY25 dividend per share (paid Jul 2026)
DMAS_BASE = 129           # end-2025 close (YTD base)

def fetch_price(ticker):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=5d&interval=1d"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read())
    result = data["chart"]["result"][0]
    closes = result["indicators"]["quote"][0]["close"]
    timestamps = result["timestamp"]
    # Drop None closes
    valid = [(t, c) for t, c in zip(timestamps, closes) if c is not None]
    if not valid:
        raise ValueError("No valid closes found")
    last_ts, last_close = valid[-1]
    prev_close = valid[-2][1] if len(valid) >= 2 else last_close
    return round(last_close), round(prev_close), last_ts

def fetch_technicals(ticker):
    """Fetch ~1y daily closes + volumes; return (rows, rsi14, dma50, dma200, avgvol20, last_turnover_bn, last_date)."""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=1y&interval=1d"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read())
    result = data["chart"]["result"][0]
    q = result["indicators"]["quote"][0]
    closes, vols, ts = q["close"], q["volume"], result["timestamp"]
    rows = [(t, c, v) for t, c, v in zip(ts, closes, vols) if c is not None and v is not None]
    if len(rows) < 30:
        raise ValueError("Not enough daily data for technicals")
    cs = [r[1] for r in rows]
    vs = [r[2] for r in rows]
    n = len(cs)
    def avg(a, k):
        return sum(a[-k:]) / k
    dma50 = avg(cs, 50)
    dma200 = avg(cs, min(200, n))
    avgvol20 = avg(vs, 20) / 1e6
    last = rows[-1]
    last_turnover_bn = last[1] * last[2] / 1e9
    last_vol_m = last[2] / 1e6
    last_date = datetime.fromtimestamp(last[0], tz=timezone.utc).strftime("%Y-%m-%d")
    # Wilder RSI-14
    gains, losses = [], []
    for i in range(1, n):
        ch = cs[i] - cs[i - 1]
        gains.append(max(ch, 0)); losses.append(max(-ch, 0))
    ag = sum(gains[:14]) / 14; al = sum(losses[:14]) / 14
    for i in range(14, len(gains)):
        ag = (ag * 13 + gains[i]) / 14
        al = (al * 13 + losses[i]) / 14
    rsi = 100 - 100 / (1 + ag / al) if al > 0 else 100
    return rsi, dma50, dma200, avgvol20, last_turnover_bn, last_vol_m, last_date

def main():
    price, prev_price, ts = fetch_price(TICKER)
    dprice, _, dts = fetch_price(DMAS_TICKER)
    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    date_str = dt.strftime("%Y-%m-%d")
    ddt = datetime.fromtimestamp(dts, tz=timezone.utc)
    ddate_str = ddt.strftime("%Y-%m-%d")
    # time-sensitive technical rows (KIJA only)
    rsi, dma50, dma200, avgvol20, turn_bn, last_vol_m, tech_date = fetch_technicals(TICKER)

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        dj = json.load(f)

    # Update refPrice + price-derived peer-chart data in FY section
    if "FY" in dj:
        dj["FY"]["refPrice"] = price
        dj["FY"]["kijaPBPS"] = [round(price / BVPS, 2), round(price * SHARES_BN / 5149.4, 2)]
        dj["FY"]["dmasPBPS"] = [round(dprice / DMAS_BVPS, 2), round(dprice * DMAS_SHARES_BN / DMAS_REV_BN, 2)]
        dj["FY"]["dmas"] = {
            "price": dprice,
            "date": ddate_str,
            "base": DMAS_BASE,
            "bvps": DMAS_BVPS,
            "eps": DMAS_EPS,
            "rev": DMAS_REV_BN,
            "shares": DMAS_SHARES_BN,
            "dps": DMAS_DPS
        }
    else:
        dj["refPrice"] = price

    # Update valuation KPIs in KP.val[LANG] (this is what the page renders)
    if "KP" in dj and "val" in dj["KP"]:
        kpv = dj["KP"]["val"]
        chg = price - prev_price
        chg_pct = (chg / prev_price * 100) if prev_price else 0
        mcap = price * SHARES_BN / 1000
        pb = price / BVPS
        pe = price / EPS
        dy = DPS / price * 100
        labels = {
            "en": {"price": "Price", "mc": "at", "pb": "parent BVPS", "pe": "on FY25 EPS", "dy": "DPS"},
            "id": {"price": "Harga", "mc": "di", "pb": "BVPS induk", "pe": "EPS FY25", "dy": "DPS"},
            "zh": {"price": "股价", "mc": "@", "pb": "母公司 BVPS", "pe": "FY25 EPS", "dy": "每股"},
        }
        for lang in ["en", "id", "zh"]:
            if lang not in kpv or len(kpv[lang]) < 6:
                continue
            cards = kpv[lang]
            L = labels[lang]
            # [0] Market cap
            cards[0]["v"] = round(mcap, 1)
            cards[0]["d"] = f"{mcap:.2f}T {L['mc']} {price}"
            # [1] Price
            cards[1]["v"] = price
            cards[1]["l"] = f"{L['price']} ({date_str})"
            cards[1]["d"] = f"{chg:+.0f} ({chg_pct:+.1f}%)"
            cards[1]["c"] = "up" if chg >= 0 else "dn"
            # [3] P/B
            cards[3]["v"] = round(pb, 1)
            cards[3]["d"] = f"{pb:.2f}x {L['pb']} {BVPS}"
            # [4] P/E
            cards[4]["v"] = round(pe, 1)
            cards[4]["d"] = f"{pe:.1f}x {L['pe']} {EPS}"
            # [5] Dividend yield
            cards[5]["v"] = round(dy, 1)
            cards[5]["d"] = f"{L['dy']} {DPS} / {price}"

    # Update last monthly close and stats in VAL
    if "VAL" in dj:
        if "close" in dj["VAL"] and len(dj["VAL"]["close"]) > 0:
            dj["VAL"]["close"][-1] = price
        if "stats" in dj["VAL"]:
            for row in dj["VAL"]["stats"]:
                if row[0] == "Price / date":
                    row[1] = f"{price}.0 IDR · {date_str} (Yahoo Finance)"
                elif row[0].startswith("Beta"):
                    row[1] = f"0.25 / {rsi:.1f}"
                elif row[0].startswith("50-DMA"):
                    row[1] = f"{dma50:.1f} / {dma200:.1f}"
                elif row[0].startswith("Avg daily volume"):
                    row[1] = f"{avgvol20:.1f}M shares"
                elif row[0].startswith("Daily turnover"):
                    row[1] = f"≈ {turn_bn:.1f}B IDR · {last_vol_m:.1f}M shares ({tech_date}, Yahoo)"

    # Keep the rendered stats/peers tables (VTXT, all languages) in sync
    if "VTXT" in dj:
        stats_labels = {"en": "Price / date", "id": "Harga / tanggal", "zh": "股价 / 日期"}
        tech_row_keys = {  # match by row label prefix; update the time-sensitive rows
            "en": {"rsi": "Beta (5Y) / RSI", "dma": "50-DMA / 200-DMA", "vol": "Avg daily volume (20d)", "turn": "Daily turnover"},
            "id": {"rsi": "Beta (5Y) / RSI", "dma": "50-DMA / 200-DMA", "vol": "Volume harian rata-rata (20d)", "turn": "Nilai transaksi"},
            "zh": {"rsi": "Beta（5Y）/ RSI", "dma": "50 日均线 / 200 日均线", "vol": "20 日均成交量", "turn": "单日成交额"},
        }
        for lang in ["en", "id", "zh"]:
            v = dj["VTXT"].get(lang)
            if not v:
                continue
            if "stats" in v:
                for row in v["stats"]:
                    if row[0] == stats_labels[lang]:
                        dec = "," if lang == "id" else "."
                        unit = "盾" if lang == "zh" else "IDR"
                        row[1] = f"{price}{dec}0 {unit} · {date_str} (Yahoo Finance)"
                        break
                # technical rows
                keys = tech_row_keys.get(lang, {})
                dec = "," if lang == "id" else "."
                for row in v["stats"]:
                    if keys.get("rsi") and row[0] == keys["rsi"]:
                        row[1] = f"0.25 / {rsi:.1f}".replace(".", dec)
                    elif keys.get("dma") and row[0] == keys["dma"]:
                        row[1] = f"{dma50:.1f} / {dma200:.1f}".replace(".", dec)
                    elif keys.get("vol") and row[0] == keys["vol"]:
                        if lang == "zh":
                            row[1] = f"{avgvol20/100:.3f} 亿股"
                        elif lang == "id":
                            row[1] = f"{avgvol20:.1f}".replace(".", ",") + " juta saham"
                        else:
                            row[1] = f"{avgvol20:.1f}M shares"
                    elif keys.get("turn") and row[0].startswith(keys["turn"]):
                        td = tech_date[5:].replace("-", "/") if lang in ("en", "id") else tech_date[5:].replace("-", "-")
                        if lang == "zh":
                            row[0] = "单日成交额（" + tech_date[5:] + "）"
                            row[1] = f"约 {turn_bn:.1f}B 盾 · {last_vol_m/100:.2f} 亿股（{tech_date}，Yahoo）"
                        elif lang == "id":
                            row[0] = "Nilai transaksi (" + td + ")"
                            row[1] = f"≈ {turn_bn:.1f}".replace(".", ",") + f"B IDR · {last_vol_m:.1f}".replace(".", ",") + f" juta saham ({tech_date}, Yahoo)"
                        else:
                            row[0] = "Daily turnover (" + td + ")"
                            row[1] = f"≈ {turn_bn:.1f}B IDR · {last_vol_m:.1f}M shares ({tech_date}, Yahoo)"
            if "peers" in v and len(v["peers"]) >= 6:
                def _f(x, d, dec):
                    s = f"{x:.{d}f}".replace(".", dec)
                    return s
                peers = v["peers"]
                dec = "," if lang == "id" else "."
                # KIJA column (col 1)
                # P/B (parent BVPS, consistent with chart)
                peers[0][1] = _f(price / BVPS, 2, dec)
                # P/E (FY25 EPS)
                peers[1][1] = _f(price / EPS, 1, dec)
                # P/S (FY25 revenue)
                peers[2][1] = _f(price * SHARES_BN / 5149.4, 2, dec)
                # Dividend yield
                dy = _f(DPS / price * 100, 1, dec)
                peers[3][1] = ("约 " if lang == "zh" else "~") + dy + "%"
                # YTD 2026 (base 210, end-2025 close)
                ytd = round((price - 210) / 210 * 100)
                peers[5][1] = f"{ytd}% (210 → {price})" if lang != "zh" else f"{ytd}%（210 → {price}）"
                # DMAS column (col 2), live price-derived
                # P/B (parent BVPS)
                peers[0][2] = _f(dprice / DMAS_BVPS, 2, dec)
                # P/E (FY25 audited EPS)
                peers[1][2] = _f(dprice / DMAS_EPS, 1, dec)
                # P/S (FY25 audited revenue)
                peers[2][2] = _f(dprice * DMAS_SHARES_BN / DMAS_REV_BN, 2, dec)
                # Dividend yield (FY25 DPS 16.5)
                ddy = _f(DMAS_DPS / dprice * 100, 1, dec)
                peers[3][2] = ("约 " if lang == "zh" else "~") + ddy + "%"
                # YTD 2026 (base = end-2025 close)
                dytd = round((dprice - DMAS_BASE) / DMAS_BASE * 100)
                dytd_s = f"{dytd}% ({DMAS_BASE} → {dprice})" if lang != "zh" else f"{dytd}%（{DMAS_BASE} → {dprice}）"
                peers[5][2] = dytd_s

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(dj, f, ensure_ascii=False, indent=1)

    print(f"Updated price: {price} (prev: {prev_price}, date: {date_str})")

if __name__ == "__main__":
    main()
