"""Imágenes del reel (1080 x 960, fondo negro) a partir de las tablas de web/data/.

    python reel/imagenes.py

Usa el entorno de los scripts de datos (plotly + kaleido). La captura del dashboard (7_dashboard.png)
se toma aparte con el dashboard abierto.
"""
import json
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

AQUI = Path(__file__).parent
DATA = AQUI.parent / "web" / "data"
SALIDA = AQUI / "imagenes"
ANCHO, ALTO, ESCALA = 1080, 960, 2

NEGRO, TINTA, TINTA_2, TINTA_3, GRILLA, EJE = "#000000", "#f0efec", "#c3c2b7", "#898781", "#2c2c2a", "#383835"
COLOR_2017, COLOR_2023, COLOR_AMBOS, AZUL, SIN_DANO = "#d95926", "#199e70", "#9085e9", "#3987e5", "#262624"
COLOR_TIPO = {"Niño Costero 2017": COLOR_2017, "Niño Costero 2023": COLOR_2023,
              "Otra con Niño costero": "#a3a29c", "Normal": "#6b6a66"}
COSTA_NORTE = ["TUMBES", "PIURA", "LAMBAYEQUE", "LA LIBERTAD"]
NOMBRE_DEPTO = {"ANCASH": "Áncash", "APURIMAC": "Apurímac", "HUANUCO": "Huánuco", "JUNIN": "Junín",
                "SAN MARTIN": "San Martín", "MADRE DE DIOS": "Madre de Dios"}
FUENTE = "Segoe UI, Arial, sans-serif"


def depto(nombre):
    return NOMBRE_DEPTO.get(nombre, nombre.title())


def estilo(fig, titulo):
    fig.update_layout(
        width=ANCHO, height=ALTO, paper_bgcolor=NEGRO, plot_bgcolor=NEGRO, separators=", ",
        font=dict(family=FUENTE, color=TINTA_2, size=26), showlegend=False,
        title=dict(text=titulo, x=0.04, y=0.97, font=dict(color=TINTA, size=34)),
        margin=dict(l=40, r=40, t=110, b=40), bargap=0.25, barcornerradius=6,
    )
    ejes = dict(gridcolor=GRILLA, linecolor=EJE, zerolinecolor=EJE, automargin=True,
                tickfont=dict(color=TINTA_3, size=24), title_font=dict(color=TINTA_2, size=24))
    fig.update_xaxes(**ejes)
    fig.update_yaxes(**ejes)
    return fig


def guardar(fig, nombre):
    fig.write_image(SALIDA / nombre, width=ANCHO, height=ALTO, scale=ESCALA)
    print("listo:", nombre)


def serie_mensual(mensual):
    peru = mensual[mensual.departamento == "PERÚ"].copy()
    peru["fecha"] = pd.to_datetime(peru.mes + "-01")
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, row_heights=[0.68, 0.32], vertical_spacing=0.1,
                        subplot_titles=("Puentes destruidos por mes", "Calentamiento del mar (ICEN, °C)"))
    fig.add_bar(x=peru.fecha, y=peru.puentes_destruidos, marker_color=AZUL, row=1, col=1)
    fig.add_scatter(x=peru.fecha, y=peru.icen, mode="lines", line=dict(color=TINTA_2, width=3), row=2, col=1)
    for x0, x1, nombre, color in [("2017-01-01", "2017-04-01", "Niño 2017", COLOR_2017),
                                  ("2023-03-01", "2024-02-01", "Niño 2023", COLOR_2023)]:
        a, b = pd.Timestamp(x0) - pd.Timedelta(days=15), pd.Timestamp(x1) + pd.Timedelta(days=16)
        fig.add_vrect(x0=a, x1=b, fillcolor=color, opacity=0.28, line_width=0, row="all", col=1)
        fig.add_annotation(x=b, y=0.97, xref="x", yref="y domain", text=f"<b>{nombre}</b>", showarrow=False,
                           xanchor="left", yanchor="top", xshift=6, font=dict(color=color, size=26))
    fig.update_xaxes(tickformat="%Y", dtick="M24")
    estilo(fig, "")
    fig.update_annotations(selector=dict(text="Puentes destruidos por mes"), font=dict(color=TINTA, size=30), x=0, xanchor="left")
    fig.update_annotations(selector=dict(text="Calentamiento del mar (ICEN, °C)"), font=dict(color=TINTA, size=30), x=0, xanchor="left")
    fig.update_layout(margin=dict(t=70), bargap=0.1)
    guardar(fig, "1_serie_mensual.png")


def temporadas_barras(temporadas, columna, titulo, nombre, mediana, decimales=0):
    t = temporadas[temporadas.completa]
    fig = go.Figure(go.Bar(x=t.temporada, y=t[columna], marker_color=[COLOR_TIPO[x] for x in t.tipo]))
    fig.add_hline(y=mediana, line=dict(color=TINTA_2, width=2, dash="dash"),
                  annotation_text=f"Temporada normal: {mediana:,.0f}".replace(",", " "),
                  annotation_position="top left", annotation_font=dict(color=TINTA_2, size=24))
    for fila in t[t.foco.notna()].itertuples():
        valor = getattr(fila, columna)
        fig.add_annotation(x=fila.temporada, y=valor, text=f"<b>{valor:,.{decimales}f}</b>".replace(",", " "),
                           showarrow=False, yanchor="bottom", yshift=6, font=dict(color=TINTA, size=30))
    estilo(fig, titulo)
    fig.update_xaxes(tickangle=-45, title_text="Temporada de lluvias (diciembre a mayo)")
    guardar(fig, nombre)


def costa_norte(deptos):
    d = deptos[deptos.temporada == "2022-23"].nlargest(10, "km_via_destruidos").iloc[::-1]
    fig = go.Figure(go.Bar(
        x=d.km_via_destruidos, y=[depto(x) for x in d.departamento], orientation="h",
        marker_color=[COLOR_2023 if x in COSTA_NORTE else "#5f5e5a" for x in d.departamento],
        text=[f"{v:,.0f}".replace(",", " ") for v in d.km_via_destruidos], textposition="outside",
        textfont=dict(color=TINTA_2, size=24), cliponaxis=False))
    estilo(fig, "Km de vías destruidos en 2023, por departamento<br>"
                f"<span style='font-size:24px;color:{COLOR_2023}'>■ costa norte</span>")
    fig.update_yaxes(tickfont=dict(color=TINTA_2, size=26))
    fig.update_layout(margin=dict(r=90, t=140))
    guardar(fig, "4_costa_norte.png")


def mapa_reincidentes(distritos):
    geo = json.loads((DATA / "distritos.geojson").read_text(encoding="utf-8"))
    foco = distritos[distritos.temporada.isin(["2016-17", "2022-23"])].dropna(subset=["ubigeo_mapa"])
    flags = (foco.pivot_table(index=["ubigeo", "ubigeo_mapa"], columns="temporada",
                              values="distritos_con_destruccion", aggfunc="max", fill_value=0)
             .reindex(columns=["2016-17", "2022-23"], fill_value=0).reset_index())
    flags["ambos"] = (flags["2016-17"] > 0) & (flags["2022-23"] > 0)
    flags["d17"], flags["d23"] = flags["2016-17"] > 0, flags["2022-23"] > 0
    pol = flags.groupby("ubigeo_mapa")[["ambos", "d17", "d23"]].any()
    tabla = pd.DataFrame({"ubigeo_mapa": [f["properties"]["ubigeo"] for f in geo["features"]]}).set_index("ubigeo_mapa")
    tabla = tabla.join(pol.reindex(tabla.index, fill_value=False))
    tabla["clase"] = 0
    tabla.loc[tabla.d23 & ~tabla.ambos, "clase"] = 2
    tabla.loc[tabla.d17 & ~tabla.ambos, "clase"] = 1
    tabla.loc[tabla.ambos, "clase"] = 3
    colores = [SIN_DANO, COLOR_2017, COLOR_2023, COLOR_AMBOS]
    escala = [x for i, c in enumerate(colores) for x in ([i / 4, c], [(i + 1) / 4, c])]
    tabla = tabla.reset_index()
    fig = go.Figure(go.Choropleth(
        geojson=geo, featureidkey="properties.ubigeo", locations=tabla.ubigeo_mapa, z=tabla.clase,
        zmin=-0.5, zmax=3.5, colorscale=escala, showscale=False, marker_line=dict(width=0.2, color=NEGRO)))
    fig.update_geos(fitbounds="locations", visible=False, bgcolor=NEGRO, projection_type="mercator")
    estilo(fig, "")
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    for i, (texto, color) in enumerate([("Destrucción en los dos Niños", COLOR_AMBOS),
                                        ("Solo en 2017", COLOR_2017), ("Solo en 2023", COLOR_2023)]):
        fig.add_annotation(x=0.03, y=0.2 - i * 0.065, xref="paper", yref="paper", xanchor="left", showarrow=False,
                           text=f"<span style='color:{color}'>■</span> {texto}", font=dict(color=TINTA_2, size=26))
    guardar(fig, "5_mapa_reincidentes.png")


def top_reincidentes(reincidentes):
    top = reincidentes.nlargest(8, "puentes_destruidos_ambos").iloc[::-1]
    nombres = [f"{d.title()} ({depto(p)})" for d, p in zip(top.distrito, top.departamento)]
    fig = go.Figure()
    for col, nombre, color in [("puentes_destruidos_2016-17", "2017", COLOR_2017),
                               ("puentes_destruidos_2022-23", "2023", COLOR_2023)]:
        fig.add_bar(x=top[col], y=nombres, orientation="h", name=nombre, marker_color=color,
                    marker_line=dict(color=NEGRO, width=2))
    for n, total in zip(nombres, top.puentes_destruidos_ambos):
        fig.add_annotation(x=total, y=n, text=f"<b>{total:.0f}</b>", showarrow=False, xanchor="left", xshift=8,
                           font=dict(color=TINTA, size=26))
    estilo(fig, "Puentes destruidos en los distritos reincidentes<br>"
                f"<span style='font-size:24px'><span style='color:{COLOR_2017}'>■</span> Niño 2017   "
                f"<span style='color:{COLOR_2023}'>■</span> Niño 2023</span>")
    fig.update_layout(barmode="stack", margin=dict(r=70, t=140))
    fig.update_yaxes(tickfont=dict(color=TINTA_2, size=24))
    guardar(fig, "6_top_reincidentes.png")


if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    ub = {"ubigeo": str, "ubigeo_mapa": str}
    temporadas = pd.read_csv(DATA / "por_temporada.csv")
    kpis = json.loads((DATA / "kpis.json").read_text(encoding="utf-8"))
    med = kpis["mediana_normal"]
    serie_mensual(pd.read_csv(DATA / "serie_mensual.csv"))
    temporadas_barras(temporadas, "puentes_destruidos", "Puentes destruidos por temporada de lluvias",
                      "2_temporadas_puentes.png", med["puentes_destruidos"])
    temporadas_barras(temporadas, "carretera_destruida_km", "Km de carreteras destruidos por temporada",
                      "3_temporadas_carreteras.png", med["carretera_destruida_km"])
    costa_norte(pd.read_csv(DATA / "por_departamento.csv"))
    mapa_reincidentes(pd.read_csv(DATA / "por_distrito.csv", dtype=ub))
    top_reincidentes(pd.read_csv(DATA / "reincidentes.csv", dtype=ub))
