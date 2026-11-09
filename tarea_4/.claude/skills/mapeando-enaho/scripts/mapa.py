"""Mapa coroplético de la pobreza monetaria por departamento (ENAHO 2024), ponderada con facpob07.

    uv run .claude/skills/mapeando-enaho/scripts/mapa.py

Une los indicadores con las geometrías por código, nunca por nombre: ubigeo[:2] de la ENAHO con FIRST_IDDP del
GeoJSON, ambos como texto de 2 dígitos. Exige las 25 unidades con dato (Lima 15 y Callao 07 por separado), compara
con la referencia de la Sesión 16 y guarda mapas/pobreza_departamento_2024.png y salidas/comparacion_mapa_referencia.csv.
"""
import math
import sys
from pathlib import Path

import geopandas as gpd
import httpx
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402

RAIZ = Path(__file__).resolve().parents[4]
BASE = RAIZ / "salidas" / "personas_2024.parquet"
GEOJSON = RAIZ / "datos" / "peru_departamental_simple.geojson"
URL_GEOJSON = ("https://raw.githubusercontent.com/d2cml-ai/Data-Science-Python/main/sessions/06-geoespacial/lab/"
               "Data/peru_departamental_simple.geojson")
REFERENCIA = Path(__file__).resolve().parents[1] / "referencia" / "pobreza_departamento_2024.csv"
TOLERANCIA_PP = 0.1
# rampa secuencial de un solo tono, de claro (cerca de 0) a oscuro
AZULES = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
TINTA, TINTA_2, FONDO = "#0b0b0b", "#52514e", "#fcfcfb"
FUENTE = ("Fuente: INEI, ENAHO 2024 (módulos 34 y 02), residentes habituales, ponderado con facpob07. Límites: "
          "GeoJSON departamental del curso. Elaboración propia.")


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # la consola de Windows (cp1252) no imprime ≠ ni →
    if not BASE.exists():
        sys.exit("ERROR: no existe salidas/personas_2024.parquet. Corran primero la skill limpiando-enaho.")
    if not GEOJSON.exists():
        GEOJSON.parent.mkdir(exist_ok=True)
        r = httpx.get(URL_GEOJSON, timeout=60, follow_redirects=True)
        r.raise_for_status()
        GEOJSON.write_bytes(r.content)

    p = pd.read_parquet(BASE)
    g = p.assign(_w=p.pobre * p.facpob07).groupby("departamento")[["_w", "facpob07"]].sum()
    pobreza = (100 * g._w / g.facpob07).rename("pobreza_pct").reset_index()
    nombres = p.drop_duplicates("departamento").set_index("departamento").nombre_departamento
    pobreza["nombre"] = pobreza.departamento.map(nombres)

    geo = gpd.read_file(GEOJSON)
    geo["FIRST_IDDP"] = geo.FIRST_IDDP.astype(str).str.zfill(2)
    m = geo.merge(pobreza, left_on="FIRST_IDDP", right_on="departamento", how="left", validate="1:1")
    fallas = []
    if len(m) != 25:
        fallas.append(f"el mapa tiene {len(m)} unidades, no 25")
    if m.pobreza_pct.isna().any():
        fallas.append(f"sin dato: {sorted(m.loc[m.pobreza_pct.isna(), 'FIRST_IDDP'])}")
    if not {"07", "15"} <= set(m.FIRST_IDDP):
        fallas.append("Lima (15) y Callao (07) no están separados")
    if fallas:
        sys.exit("ERROR en la unión territorial: " + "; ".join(fallas))

    # Comparación con la referencia de la Sesión 16 (una cifra decimal por departamento). Esa referencia se calculó
    # con la sumaria (hogares × factor07 × mieperho), así que se compara con los dos métodos: el del mapa (personas ×
    # facpob07) y el de la sumaria, que limpiando-enaho deja en salidas/indicadores.csv.
    ref = pd.read_csv(REFERENCIA, dtype={"ccdd": str})
    ind = pd.read_csv(RAIZ / "salidas" / "indicadores.csv", dtype={"codigo": str}).query("grupo == 'departamento'")
    comp = pobreza.merge(ref, left_on="departamento", right_on="ccdd", how="outer", validate="1:1",
                         suffixes=("", "_ref")).merge(ind[["codigo", "pobreza_pct_sumaria"]], left_on="departamento",
                                                      right_on="codigo", how="left", validate="1:1")
    comp["mapa_facpob07"] = comp.pobreza_pct.round(1)
    comp["sumaria_factor07"] = comp.pobreza_pct_sumaria.round(1)
    comp["dif_mapa_pp"] = (comp.mapa_facpob07 - comp.pobreza_pct_ref).round(2)
    comp["dif_sumaria_pp"] = (comp.sumaria_factor07 - comp.pobreza_pct_ref).round(2)
    comp["coincide"] = comp.dif_mapa_pp.abs() <= TOLERANCIA_PP
    comp["coincide_sumaria"] = comp.dif_sumaria_pp.abs() <= TOLERANCIA_PP
    comp[["departamento", "nombre", "pobreza_pct_ref", "mapa_facpob07", "dif_mapa_pp", "sumaria_factor07",
          "dif_sumaria_pp"]].rename(columns={"pobreza_pct_ref": "referencia_sesion16"}).to_csv(
        RAIZ / "salidas" / "comparacion_mapa_referencia.csv", index=False, encoding="utf-8")

    # el mapa
    vmax = math.ceil(m.pobreza_pct.max() / 10) * 10
    cmap = LinearSegmentedColormap.from_list("azules", AZULES)
    fig, ax = plt.subplots(figsize=(7.5, 9.5), facecolor=FONDO)
    ax.set_facecolor(FONDO)
    m.plot(column="pobreza_pct", cmap=cmap, vmin=0, vmax=vmax, edgecolor="white", linewidth=0.7, ax=ax,
           legend=True, legend_kwds={"label": "% de personas en pobreza monetaria", "shrink": 0.55, "pad": 0.01})
    for _, f in m.iterrows():
        x, y = f.geometry.representative_point().coords[0]
        color = "white" if f.pobreza_pct > 0.55 * vmax else TINTA
        if f.FIRST_IDDP == "07":  # Callao es muy pequeño: su etiqueta va en el mar, con una línea
            ax.annotate(f"Callao {f.pobreza_pct:.1f}", (x, y), xytext=(x - 2.2, y - 0.4), fontsize=6.5, color=TINTA,
                        arrowprops={"arrowstyle": "-", "color": TINTA_2, "lw": 0.6})
        else:
            ax.text(x, y, f"{f.pobreza_pct:.1f}", ha="center", va="center", fontsize=6.5, color=color)
    ax.set_axis_off()
    alta, baja = m.loc[m.pobreza_pct.idxmax()], m.loc[m.pobreza_pct.idxmin()]
    fig.suptitle(f"La pobreza monetaria va de {baja.pobreza_pct:.1f} % en {baja.nombre} a "
                 f"{alta.pobreza_pct:.1f} % en {alta.nombre}", x=0.03, ha="left", fontsize=12, fontweight="bold",
                 color=TINTA)
    ax.set_title("% de personas en pobreza monetaria por departamento, Perú 2024 · Lima (15) y Callao (07) por "
                 "separado", loc="left", fontsize=8.5, color=TINTA_2)
    fig.text(0.03, 0.015, FUENTE, fontsize=6.5, color=TINTA_2, wrap=True)
    fig.tight_layout(rect=(0, 0.03, 1, 0.97))
    (RAIZ / "mapas").mkdir(exist_ok=True)
    salida = RAIZ / "mapas" / "pobreza_departamento_2024.png"
    fig.savefig(salida, dpi=200, facecolor=FONDO)
    plt.close(fig)

    print(f"{salida.relative_to(RAIZ)}: 25 de 25 departamentos unidos por código (ubigeo[:2] = FIRST_IDDP).")
    print(f"Más alta: {alta.nombre} {alta.pobreza_pct:.2f} % · más baja: {baja.nombre} {baja.pobreza_pct:.2f} %")
    print(f"Referencia de la Sesión 16 (calculada con la sumaria): con el mismo método coinciden "
          f"{int(comp.coincide_sumaria.sum())} de 25 a ±{TOLERANCIA_PP} pp (máx. {comp.dif_sumaria_pp.abs().max():.2f}); "
          f"con personas × facpob07, la del mapa, {int(comp.coincide.sum())} de 25 (máx. "
          f"{comp.dif_mapa_pp.abs().max():.2f} pp, por la unidad de ponderación) → salidas/comparacion_mapa_referencia.csv")
    if not comp.coincide_sumaria.all():
        sys.exit("ERROR: con el mismo método que la referencia no coinciden todos los departamentos.")


if __name__ == "__main__":
    main()
