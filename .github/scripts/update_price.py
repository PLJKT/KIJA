#!/usr/bin/env python3
"""Fetch latest KIJA.JK closing price from Yahoo Finance and update data.json."""
import json
import sys
import urllib.request
from datetime import datetime, timezone

DATA_FILE = "data.json"
TICKER = "KIJA.JK"
SHARES_BN = 20.59  # weighted avg shares (bn)
EPS = 20.55        # FY25 audited EPS (IDR)
BVPS = 304.1       # parent BVPS (IDR)
DPS = 2.03         # FY25 dividend per share (IDR)

def fetch_price():
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{TICKER}?range=5d&interval=1d"
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

def main():
    price, prev_price, ts = fetch_price()
    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    date_str = dt.strftime("%Y-%m-%d")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        dj = json.load(f)

    # Update refPrice in FY section
    if "FY" in dj:
        dj["FY"]["refPrice"] = price
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
                    break

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(dj, f, ensure_ascii=False, indent=1)

    print(f"Updated price: {price} (prev: {prev_price}, date: {date_str})")

if __name__ == "__main__":
    main()
