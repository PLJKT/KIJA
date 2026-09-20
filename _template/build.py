# -*- coding: utf-8 -*-
"""Generic build script for a company financial dashboard.
Place this in <project>/_build/ alongside head.html, body.html, js_a.html, js_b.html.
Edit BASE/OUT/DJ below to match your new project.
"""
import io, os, json, sys
from html.parser import HTMLParser

# ---- EDIT THESE FOR A NEW PROJECT ----
BASE = r"C:\path\to\your\project"
BUILD = os.path.join(BASE, "_build")
OUT = os.path.join(BASE, "your-repo", "index.html")
DJ = os.path.join(BASE, "your-repo", "data.json")
# ---------------------------------------

DATA_KEYS = ["KP","EV","RK","DIR","TL","OWN","SUBS","BIZ","VIA","PILLAR","PILLAR_MAP","ORG",
             "DEBT","WC","LAND","VAL","DTXT","LTXT","VTXT","NXT","VALI","LIQ","KEYP","AN","CHT","FY","LBV","GLOS","TOP3","OPP"]

PAGES = ("overview","profit","debt","landbank","valuation","vali","risk","holding","org")

def read(p):
    with io.open(p, "r", encoding="utf-8") as f: return f.read()

def data_block():
    data = json.load(io.open(DJ, "r", encoding="utf-8"))
    lines = ["<script>", "/* data from data.json */"]
    for k in DATA_KEYS:
        lines.append("var %s = %s;" % (k, json.dumps(data[k], ensure_ascii=False, separators=(",", ":"))))
    lines.append("</script>")
    return "\n".join(lines)

def validate_data():
    if not os.path.exists(DJ):
        print("WARNING: data.json missing, skip validation"); return
    data = json.load(io.open(DJ, "r", encoding="utf-8"))
    missing = [k for k in DATA_KEYS if k not in data]
    if missing:
        print("data.json missing keys:", missing); sys.exit(1)
    y = data["AN"]["years"]
    for k, v in data["AN"].items():
        if k != "years" and len(v) != len(y):
            print("AN.%s length %d != years %d" % (k, len(v), len(y))); sys.exit(1)
    print("data.json OK,", len(DATA_KEYS), "blocks")

parts = [read(os.path.join(BUILD, "head.html")),
         read(os.path.join(BUILD, "body.html")),
         read(os.path.join(BUILD, "js_a.html")),
         data_block(),
         read(os.path.join(BUILD, "js_b.html"))]
html = "\n".join(parts)

if len(sys.argv) > 1 and sys.argv[1] in PAGES:
    p = sys.argv[1]
    html = html.replace("return 'overview';", "return '%s';" % p)
    out = os.path.join(BUILD, "_test_%s.html" % p)
    io.open(out, "w", encoding="utf-8", newline="\n").write(html)
    print("test page:", os.path.basename(out)); sys.exit(0)

validate_data()
io.open(OUT, "w", encoding="utf-8", newline="\n").write(html)
print("index.html written:", os.path.getsize(OUT), "bytes")

VOID = {"meta","link","br","img","hr","input","col","source","wbr"}
class Chk(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self, convert_charrefs=True); self.stack=[]; self.errors=[]
    def handle_starttag(self,t,a):
        if t not in VOID: self.stack.append((t,self.getpos()))
    def handle_endtag(self,t):
        if t in VOID: return
        if not self.stack: self.errors.append("stray </%s>"%t); return
        top,pos=self.stack.pop()
        if top!=t: self.errors.append("mismatch %s vs </%s>"%(top,t))
chk=Chk(); chk.feed(html)
if chk.stack: chk.errors.append("unclosed: %s"%[t for t,_ in chk.stack])
if chk.errors:
    print("HTML CHECK FAILED:"); [print(" -",e) for e in chk.errors]; sys.exit(1)
print("HTML tag balance OK")
