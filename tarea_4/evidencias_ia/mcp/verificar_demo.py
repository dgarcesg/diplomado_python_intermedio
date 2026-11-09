"""Verificación independiente de la demo: pide los datos directo a las APIs (sin server.py) y recalcula."""
import httpx, statistics as st
def bcrp(c, d, h):
    p = httpx.get(f"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/{c}/json/{d}/{h}", timeout=60).json()["periods"]
    return [(x["name"], float(x["values"][0])) for x in p if x["values"][0] != "n.d."]
for c, d, h in [("PN01273PM", "2020-1", "2024-12"), ("RD12956DM", "2024-1", "2024-12")]:
    v = bcrp(c, d, h); vals = [x[1] for x in v]
    print(c, "n", len(v), "primero", v[0], "ultimo", v[-1], "max", max(v, key=lambda x: x[1]),
          "min", min(v, key=lambda x: x[1]), "prom", round(st.mean(vals), 4))
r = httpx.get("https://api.worldbank.org/v2/country/PER;CHL;COL/indicator/NY.GDP.MKTP.KD.ZG?format=json&date=2015:2024&per_page=1000", timeout=60).json()[1]
for pais in ("Peru", "Chile", "Colombia"):
    vals = [f["value"] for f in r if f["country"]["value"] == pais and f["value"] is not None]
    print(pais, len(vals), round(st.mean(vals), 2))
