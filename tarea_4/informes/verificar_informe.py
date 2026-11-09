"""Verifica cifras del informe final con fuentes independientes del agente, sin pasar por el MCP ni por las Skills.

    uv run informes/verificar_informe.py

- BCRP: pide cada serie directo a la API de estadisticas.bcrp.gob.pe y recalcula.
- ENAHO: recalcula desde el zip del INEI con un código mínimo y separado de limpiar.py, usando solo la sumaria y su
  método oficial (hogares × factor07 × mieperho), y compara con la referencia de la Sesión 16.
"""
import statistics as st
import sys
import zipfile
from pathlib import Path

import httpx
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parents[1]
API = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api"


def bcrp(codigo, desde, hasta):
    p = httpx.get(f"{API}/{codigo}/json/{desde}/{hasta}", timeout=60).json()["periods"]
    return [(x["name"], float(x["values"][0])) for x in p if x["values"][0] != "n.d."]


inf = bcrp("PN01273PM", "2020-1", "2024-12")
valores = [v for _, v in inf]
print("PN01273PM 2020-2024:", "primero", inf[0], "último", inf[-1], "máximo", max(inf, key=lambda x: x[1]),
      "promedio", round(st.mean(valores), 2))
for codigo in ("RD15519DA", "RD15516DA"):
    s = bcrp(codigo, "2020", "2024")
    print(codigo, s, "variación % 2020-2024:", round(100 * (s[-1][1] - s[0][1]) / s[0][1], 2))

with zipfile.ZipFile(RAIZ / "datos" / "966-Modulo34.zip").open("966-Modulo34/sumaria-2024.dta") as f:
    h = pd.read_stata(f, convert_categoricals=False, columns=["ubigeo", "estrato", "pobreza", "factor07", "mieperho"])
h["w"] = h.factor07 * h.mieperho
h["pw"] = (h.pobreza <= 2) * h.w


def tasa(d):
    return round(100 * d.pw.sum() / d.w.sum(), 2)


print("ENAHO sumaria: Perú", tasa(h), "| urbana", tasa(h[h.estrato <= 5]), "| rural", tasa(h[h.estrato > 5]),
      "| Arequipa", tasa(h[h.ubigeo.str[:2] == "04"]), "| Cajamarca", tasa(h[h.ubigeo.str[:2] == "06"]),
      "| Ica", tasa(h[h.ubigeo.str[:2] == "11"]))
