"""Dashboard de la Tarea 3: puentes y carreteras que se llevaron los Niños Costeros.

Lee las tablas que escribe scripts/analizar_datos.py en web/data/. No recalcula
nada pesado: solo filtra y suma por temporada, departamento y distrito.

    streamlit run web/app.py
"""

import json
import math
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

DATA = Path(__file__).parent / "data"
REPO = "https://github.com/dgarcesg/diplomado_python_intermedio/tree/main/tarea_3"

# --- Colores sobre fondo negro. Las dos paletas categóricas (eventos y peligros)
# se validaron contra #000000: separación para daltonismo y contraste. ---
NEGRO = "#000000"
SUPERFICIE = "#141413"
TINTA = "#f0efec"
TINTA_2 = "#c3c2b7"
TINTA_3 = "#898781"
GRILLA = "#2c2c2a"
EJE = "#383835"
SIN_DANO = "#262624"

COLOR_2017 = "#d95926"
COLOR_2023 = "#199e70"
COLOR_AMBOS = "#9085e9"
COLOR_PELIGRO = {
    "Lluvias": "#3987e5",
    "Huaicos y deslizamientos": "#c98500",
    "Inundaciones": "#d55181",
}
RAMPA = ["#184f95", "#256abf", "#3987e5", "#6da7ec", "#b7d3f6"]  # azul: oscuro = poco daño
COSTA_NORTE_COLOR, RESTO_COLOR = "#c3c2b7", "#5f5e5a"

# Tipo de temporada: (etiqueta en la leyenda, color de la barra)
TIPOS = {
    "Niño Costero 2017": ("Niño Costero 2017", COLOR_2017),
    "Niño Costero 2023": ("Niño Costero 2023", COLOR_2023),
    "Otra con Niño costero": ("Otra temporada con meses de Niño costero", "#a3a29c"),
    "Normal": ("Temporada normal (línea base)", "#6b6a66"),
}

# Indicador: (etiqueta, unidad, decimales)
INDICADORES = {
    "puentes_destruidos": ("Puentes destruidos", "puentes", 0),
    "puentes_afectados": ("Puentes afectados", "puentes", 0),
    "km_via_destruidos": ("Km de vía destruidos (carretera + camino rural)", "km", 1),
    "carretera_destruida_km": ("Km de carretera destruidos", "km", 1),
    "camino_rural_destruido_km": ("Km de camino rural destruidos", "km", 1),
    "km_via_afectados": ("Km de vía afectados (carretera + camino rural)", "km", 1),
    "carretera_afectada_km": ("Km de carretera afectados", "km", 1),
    "camino_rural_afectado_km": ("Km de camino rural afectados", "km", 1),
}

FOCO = ["2016-17", "2022-23"]
AMBOS = "ambos"
COSTA_NORTE = ["TUMBES", "PIURA", "LAMBAYEQUE", "LA LIBERTAD"]
DEPTO_UBIGEO = {
    "01": "AMAZONAS", "02": "ANCASH", "03": "APURIMAC", "04": "AREQUIPA", "05": "AYACUCHO",
    "06": "CAJAMARCA", "07": "CALLAO", "08": "CUSCO", "09": "HUANCAVELICA", "10": "HUANUCO",
    "11": "ICA", "12": "JUNIN", "13": "LA LIBERTAD", "14": "LAMBAYEQUE", "15": "LIMA PROVINCIAS",
    "16": "LORETO", "17": "MADRE DE DIOS", "18": "MOQUEGUA", "19": "PASCO", "20": "PIURA",
    "21": "PUNO", "22": "SAN MARTIN", "23": "TACNA", "24": "TUMBES", "25": "UCAYALI",
}
NOMBRE_DEPTO = {
    "ANCASH": "Áncash", "APURIMAC": "Apurímac", "HUANUCO": "Huánuco", "JUNIN": "Junín",
    "SAN MARTIN": "San Martín", "MADRE DE DIOS": "Madre de Dios",
}
MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "set", "oct", "nov", "dic"]
MINUSCULAS = {"de", "del", "la", "las", "los", "el", "y", "e"}
FUENTE = "system-ui, -apple-system, 'Segoe UI', sans-serif"
CONFIG_GRAFICO = {"displaylogo": False, "modeBarButtonsToRemove": ["select2d", "lasso2d"]}
# Mapa base sin teselas: un rectángulo negro bajo los distritos, sobre el estilo "white-bg".
# (Un estilo propio en JSON falla con el plotly.js que trae Streamlit.)
FONDO_MAPA = dict(sourcetype="geojson", type="fill", color=NEGRO, below="traces", source={
    "type": "Feature", "properties": {},
    "geometry": {"type": "Polygon", "coordinates": [[[-180, -85], [180, -85], [180, 85], [-180, 85], [-180, -85]]]}})


# --- Formatos --------------------------------------------------------------

def num(x, dec=0):
    """Coma decimal y espacio de miles desde 10 000, como en el README. Redondea 24,5 a 25."""
    if x is None or pd.isna(x):
        return "—"
    x = float(Decimal(str(x)).quantize(Decimal(1).scaleb(-dec), rounding=ROUND_HALF_UP))
    entero, _, decimales = f"{x:,.{dec}f}".partition(".")
    entero = entero.replace(",", " " if abs(x) >= 10_000 else "")
    return entero + ("," + decimales if decimales else "")


def veces(x):
    return "—" if x is None or pd.isna(x) else f"{num(x, 1)}×"


def depto(nombre):
    return NOMBRE_DEPTO.get(nombre, nombre.title())


def titulo(texto):
    palabras = str(texto).lower().split()
    return " ".join(p if i and p in MINUSCULAS else p.capitalize() for i, p in enumerate(palabras))


def depto_de_ubigeo(ubigeo):
    return "LIMA METROPOLITANA" if ubigeo.startswith("1501") else DEPTO_UBIGEO[ubigeo[:2]]


def mes_texto(fecha):
    return f"{MESES[fecha.month - 1]} {fecha.year}"


def valor(x, indicador):
    _, unidad, dec = INDICADORES[indicador]
    return f"{num(x, dec)} {unidad}"


# --- Datos -----------------------------------------------------------------

@st.cache_data
def cargar_tablas():
    ub = {"ubigeo": str, "ubigeo_mapa": str}
    # Solo temporadas completas: a la 2015-16 le falta diciembre de 2015 porque el periodo empieza
    # en enero de 2016. Esos meses siguen en la serie mensual.
    temporadas = pd.read_csv(DATA / "por_temporada.csv")
    temporadas = temporadas[temporadas.completa].reset_index(drop=True)
    completas = set(temporadas.temporada)
    peligros = pd.read_csv(DATA / "por_temporada_peligro.csv")
    peligros = peligros[peligros.temporada.isin(completas)]
    mensual = pd.read_csv(DATA / "serie_mensual.csv")
    mensual["fecha"] = pd.to_datetime(mensual["mes"] + "-01")
    deptos = pd.read_csv(DATA / "por_departamento.csv")
    deptos = deptos[deptos.temporada.isin(completas)]
    distritos = pd.read_csv(DATA / "por_distrito.csv", dtype=ub)
    distritos = distritos[distritos.temporada.isin(completas)]
    reincidentes = pd.read_csv(DATA / "reincidentes.csv", dtype=ub)
    kpis = json.loads((DATA / "kpis.json").read_text(encoding="utf-8"))
    return temporadas, peligros, mensual, deptos, distritos, reincidentes, kpis


@st.cache_data
def cargar_mapa():
    """GeoJSON de distritos y una tabla con el departamento y la extensión de cada uno."""
    geo = json.loads((DATA / "distritos.geojson").read_text(encoding="utf-8"))
    filas = []
    for f in geo["features"]:
        p, g = f["properties"], f["geometry"]
        poligonos = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]
        puntos = [pt for pol in poligonos for anillo in pol for pt in anillo]
        lons, lats = [pt[0] for pt in puntos], [pt[1] for pt in puntos]
        departamento = depto_de_ubigeo(p["ubigeo"])
        filas.append({
            "ubigeo_mapa": p["ubigeo"],
            "departamento": departamento,
            "nombre": f"{p['distrito']} · {p['provincia']} ({depto(departamento)})",
            "lon_min": min(lons), "lon_max": max(lons),
            "lat_min": min(lats), "lat_max": max(lats),
        })
    return geo, pd.DataFrame(filas)


def solo(geo, ubigeos):
    ubigeos = set(ubigeos)
    return {"type": "FeatureCollection",
            "features": [f for f in geo["features"] if f["properties"]["ubigeo"] in ubigeos]}


def etiqueta_temporada(fila):
    if isinstance(fila.foco, str):
        return f"{fila.temporada} · {fila.foco}"
    if fila.tipo == "Normal":
        return f"{fila.temporada} · normal"
    if fila.temporada == "2023-24":
        return f"{fila.temporada} · final del Niño Costero 2023"
    return f"{fila.temporada} · Niño costero {fila.magnitud_nino.lower()}"


def totales_por_temporada(distritos, temporadas, departamento, indicador):
    d = distritos if departamento is None else distritos[distritos.departamento == departamento]
    serie = d.groupby("temporada")[indicador].sum()
    t = temporadas[["temporada", "tipo"]].copy()
    t["valor"] = t.temporada.map(serie).fillna(0)
    return t


# --- Estilo de los gráficos ------------------------------------------------

def estilo(fig, alto, leyenda=True):
    fig.update_layout(
        height=alto,
        paper_bgcolor=NEGRO, plot_bgcolor=NEGRO,
        font=dict(family=FUENTE, color=TINTA_2, size=13),
        margin=dict(l=8, r=16, t=64 if leyenda else 12, b=8),
        separators=", ",
        showlegend=leyenda,
        legend=dict(orientation="h", x=0, y=1.02, yanchor="bottom", bgcolor="rgba(0,0,0,0)", traceorder="normal",
                    font=dict(color=TINTA_2, size=12), title_text=""),
        hoverlabel=dict(bgcolor=SUPERFICIE, bordercolor=EJE, font=dict(color=TINTA, family=FUENTE)),
        bargap=0.3, barcornerradius=4,
    )
    ejes = dict(gridcolor=GRILLA, linecolor=EJE, zerolinecolor=EJE, automargin=True,
                tickfont=dict(color=TINTA_3), title_font=dict(color=TINTA_2))
    fig.update_xaxes(**ejes)
    fig.update_yaxes(**ejes)
    return fig


def mostrar(fig, clave):
    st.plotly_chart(fig, theme=None, config=CONFIG_GRAFICO, key=clave)


def leyenda_html(items, titulo_leyenda=""):
    partes = [f"<span class='ley-t'>{titulo_leyenda}</span>"] if titulo_leyenda else []
    for texto, color in items:
        partes.append(f"<span class='ley-i'><span class='ley-c' style='background:{color}'></span>{texto}</span>")
    st.markdown(f"<div class='ley'>{''.join(partes)}</div>", unsafe_allow_html=True)


def tarjeta(col, etiqueta, cifra, nota):
    col.markdown(
        f"<div class='kpi'><div class='kpi-t'>{etiqueta}</div>"
        f"<div class='kpi-v'>{cifra}</div><div class='kpi-n'>{nota}</div></div>",
        unsafe_allow_html=True,
    )


CSS = f"""
<style>
.stApp, [data-testid="stHeader"], [data-testid="stSidebar"] {{ background: {NEGRO}; }}
.block-container {{ padding-top: 2rem; }}
[data-testid="stSidebar"] {{ min-width: 330px; }}
.kpi {{ border: 1px solid {GRILLA}; border-radius: 8px; padding: 14px 16px; background: {NEGRO};
        min-height: 128px; }}
.kpi-t {{ color: {TINTA_2}; font-size: 0.85rem; }}
.kpi-v {{ color: {TINTA}; font-size: 2rem; font-weight: 600; line-height: 1.25; margin: 4px 0; }}
.kpi-n {{ color: {TINTA_3}; font-size: 0.8rem; line-height: 1.35; }}
.ley {{ display: flex; flex-wrap: wrap; gap: 6px 16px; align-items: center; font-size: 0.85rem;
        color: {TINTA_2}; margin: 2px 0 8px; }}
.ley-t {{ color: {TINTA_3}; }}
.ley-i {{ display: inline-flex; align-items: center; gap: 6px; }}
.ley-c {{ width: 12px; height: 12px; border-radius: 3px; border: 1px solid {EJE}; display: inline-block; }}
.pregunta {{ color: {TINTA}; font-size: 1.15rem; margin: 0 0 6px; }}
.sub {{ color: {TINTA_3}; font-size: 0.85rem; }}
</style>
"""


# --- Gráficos --------------------------------------------------------------

def figura_temporadas(t, indicador, mediana, alto=380):
    etiqueta, unidad, dec = INDICADORES[indicador]
    fig = go.Figure()
    for tipo, (nombre, color) in TIPOS.items():
        sub = t[t.tipo == tipo]
        if sub.empty:
            continue
        fig.add_bar(
            x=sub.temporada, y=sub.valor, name=nombre, marker_color=color,
            customdata=[valor(v, indicador) for v in sub.valor],
            hovertemplate="Temporada %{x}<br>%{customdata}<extra></extra>",
        )
    if mediana is not None and mediana > 0:
        fig.add_hline(y=mediana, line=dict(color=TINTA_2, width=1, dash="dash"),
                      annotation_text=f"Mediana de las temporadas normales: {num(mediana, dec)}",
                      annotation_position="top left", annotation_font=dict(color=TINTA_2, size=12))
    for fila in t[t.temporada.isin(FOCO)].itertuples():
        fig.add_annotation(x=fila.temporada, y=fila.valor, text=num(fila.valor, dec), showarrow=False,
                           yanchor="bottom", yshift=4, font=dict(color=TINTA, size=13))
    fig.update_layout(barmode="stack")
    fig.update_xaxes(categoryorder="array", categoryarray=list(t.temporada), title_text="Temporada de lluvias (diciembre a mayo)")
    fig.update_yaxes(title_text=etiqueta)
    return estilo(fig, alto)


def figura_peligros(peligros, indicador):
    etiqueta, _, _ = INDICADORES[indicador]
    total = peligros.groupby("temporada")[indicador].transform("sum")
    fig = go.Figure()
    for grupo, color in COLOR_PELIGRO.items():
        sub = peligros[peligros.grupo_peligro == grupo]
        porcentaje = (sub[indicador] / total[sub.index] * 100).fillna(0)
        fig.add_bar(
            x=sub.temporada, y=sub[indicador], name=grupo, marker_color=color,
            marker_line=dict(color=NEGRO, width=1.5),
            customdata=[f"{valor(v, indicador)} ({num(p)} % de la temporada)"
                        for v, p in zip(sub[indicador], porcentaje)],
            hovertemplate=f"{grupo} · %{{x}}<br>%{{customdata}}<extra></extra>",
        )
    fig.update_layout(barmode="stack")
    fig.update_xaxes(title_text="Temporada de lluvias (diciembre a mayo)")
    fig.update_yaxes(title_text=etiqueta)
    return estilo(fig, 380)


def tramos_nino(mensual):
    """Tramos continuos de meses dentro de un evento oficial de Niño costero."""
    meses = mensual.loc[mensual.nino_costero, "fecha"].sort_values().tolist()
    tramos = []
    for fecha in meses:
        if tramos and (fecha.year - tramos[-1][1].year) * 12 + fecha.month - tramos[-1][1].month == 1:
            tramos[-1][1] = fecha
        else:
            tramos.append([fecha, fecha])
    resultado = []
    for inicio, fin in tramos:
        if inicio <= pd.Timestamp("2017-04-01") and fin >= pd.Timestamp("2017-01-01"):
            nombre, color = "Niño 2017", COLOR_2017
        elif inicio <= pd.Timestamp("2024-02-01") and fin >= pd.Timestamp("2023-03-01"):
            nombre, color = "Niño 2023", COLOR_2023
        else:
            nombre, color = "Otro Niño", TINTA_3
        resultado.append((inicio, fin, nombre, color))
    return resultado


def figura_mensual(mensual, indicador):
    etiqueta, unidad, dec = INDICADORES[indicador]
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, row_heights=[0.64, 0.36], vertical_spacing=0.09,
                        subplot_titles=(f"{etiqueta} por mes",
                                        "ICEN: anomalía de la temperatura del mar en la región Niño 1+2 (°C)"))
    fig.add_bar(x=mensual.fecha, y=mensual[indicador], marker_color="#3987e5", name=etiqueta,
                customdata=[f"{mes_texto(f)}: {valor(v, indicador)}" for f, v in zip(mensual.fecha, mensual[indicador])],
                hovertemplate="%{customdata}<extra></extra>", row=1, col=1)
    fig.add_scatter(x=mensual.fecha, y=mensual.icen, mode="lines", line=dict(color=TINTA_2, width=2), name="ICEN",
                    customdata=[f"{mes_texto(f)}: ICEN {num(v, 2)} °C" for f, v in zip(mensual.fecha, mensual.icen)],
                    hovertemplate="%{customdata}<extra></extra>", row=2, col=1)
    fig.add_hline(y=0.4, line=dict(color=TINTA_3, width=1, dash="dot"), row=2, col=1)
    for inicio, fin, nombre, color in tramos_nino(mensual):
        x0, x1 = inicio - pd.Timedelta(days=15), fin + pd.Timedelta(days=16)
        fig.add_vrect(x0=x0, x1=x1, fillcolor=color, opacity=0.2, line_width=0, row="all", col=1)
        fig.add_annotation(x=x0, y=1, xref="x", yref="y domain", text=nombre, showarrow=False,
                           xanchor="left", yanchor="top", font=dict(color=TINTA_2, size=11))
    fig.update_xaxes(tickformat="%Y", dtick="M12", ticklabelmode="period")
    fig.update_yaxes(title_text=unidad, row=1, col=1)
    fig.update_yaxes(title_text="°C", row=2, col=1)
    fig.update_annotations(selector=dict(text=f"{etiqueta} por mes"), font=dict(color=TINTA, size=13), x=0, xanchor="left")
    fig.update_annotations(selector=dict(text="ICEN: anomalía de la temperatura del mar en la región Niño 1+2 (°C)"),
                           font=dict(color=TINTA, size=13), x=0, xanchor="left")
    estilo(fig, 520, leyenda=False)
    fig.update_layout(margin=dict(t=30), bargap=0.15)
    return fig


def figura_ranking(tabla, indicador, departamento_sel, alto=640):
    etiqueta, _, dec = INDICADORES[indicador]
    tabla = tabla.sort_values(indicador)
    marcas = ["▸ " if d == departamento_sel else "" for d in tabla.departamento]
    nombres = [f"{m}{depto(d)}" for m, d in zip(marcas, tabla.departamento)]
    colores = [COSTA_NORTE_COLOR if d in COSTA_NORTE else RESTO_COLOR for d in tabla.departamento]
    fig = go.Figure(go.Bar(
        x=tabla[indicador], y=nombres, orientation="h", marker_color=colores,
        customdata=[valor(v, indicador) for v in tabla[indicador]],
        hovertemplate="%{y}<br>%{customdata}<extra></extra>",
        text=[num(v, dec) for v in tabla[indicador]], textposition="outside",
        textfont=dict(color=TINTA_2, size=11), cliponaxis=False,
    ))
    fig.update_yaxes(tickfont=dict(color=TINTA_2))
    fig.update_xaxes(title_text=etiqueta, showgrid=True)
    estilo(fig, alto, leyenda=False)
    fig.update_layout(bargap=0.25, margin=dict(r=40))
    return fig


def figura_top_reincidentes(top, indicador):
    etiqueta, _, dec = INDICADORES[indicador]
    top = top.iloc[::-1]
    fig = go.Figure()
    for temporada, nombre, color in [("2016-17", "Niño Costero 2017", COLOR_2017),
                                     ("2022-23", "Niño Costero 2023", COLOR_2023)]:
        fig.add_bar(
            x=top[temporada], y=top.etiqueta, orientation="h", name=nombre, marker_color=color,
            marker_line=dict(color=NEGRO, width=1.5),
            customdata=[valor(v, indicador) for v in top[temporada]],
            hovertemplate=f"%{{y}}<br>{nombre}: %{{customdata}}<extra></extra>",
        )
    for fila in top.itertuples():
        fig.add_annotation(x=fila.total, y=fila.etiqueta, text=num(fila.total, dec), showarrow=False,
                           xanchor="left", xshift=6, font=dict(color=TINTA_2, size=11))
    fig.update_layout(barmode="stack")
    fig.update_yaxes(tickfont=dict(color=TINTA_2))
    fig.update_xaxes(title_text=f"{etiqueta}, sumando los dos eventos")
    estilo(fig, 34 * len(top) + 110)
    fig.update_layout(margin=dict(r=48))
    return fig


def clases(valores, dec):
    """Hasta 5 clases con cortes en cuantiles de los distritos con daño; 0 = sin daño."""
    positivos = valores[valores > 0]
    if positivos.empty:
        return pd.Series(0, index=valores.index), ["Sin daño registrado"]
    maximo = positivos.max()
    cortes = []
    for q in positivos.quantile([0.5, 0.75, 0.9, 0.97]):
        corte = round(q, dec)
        if corte > (cortes[-1] if cortes else 0) and corte < maximo:
            cortes.append(corte)
    limites = [0] + cortes + [maximo]
    clase = (pd.cut(valores, limites, labels=False) + 1).fillna(0).astype(int)
    etiquetas = ["Sin daño registrado"]
    for i, (a, b) in enumerate(zip(limites[:-1], limites[1:])):
        if dec == 0:
            bajo = int(a) + 1
            etiquetas.append(num(b) if bajo == b else f"{num(bajo)}–{num(b)}")
        else:
            etiquetas.append(f"hasta {num(b, dec)}" if i == 0 else f"{num(a, dec)}–{num(b, dec)}")
    return clase, etiquetas


def tonos(n):
    if n == 1:
        return [RAMPA[2]]
    return [RAMPA[round(i * (len(RAMPA) - 1) / (n - 1))] for i in range(n)]


def encuadre(extension, ancho=780, alto=600):
    lon_min, lon_max = extension.lon_min.min(), extension.lon_max.max()
    lat_min, lat_max = extension.lat_min.min(), extension.lat_max.max()
    lon_span, lat_span = max(lon_max - lon_min, 0.05), max(lat_max - lat_min, 0.05)
    zoom = math.log2(min(ancho / lon_span, alto / lat_span) * 360 / 512)
    return dict(lon=(lon_min + lon_max) / 2, lat=(lat_min + lat_max) / 2), min(zoom, 10)


def figura_mapa(geo, tabla, colores, centro, zoom, distrito_mapa=None):
    k = len(colores)
    escala = []
    for i, color in enumerate(colores):
        escala += [[i / k, color], [(i + 1) / k, color]]
    fig = go.Figure(go.Choroplethmap(
        geojson=geo, featureidkey="properties.ubigeo", locations=tabla.ubigeo_mapa, z=tabla.clase,
        zmin=-0.5, zmax=k - 0.5, colorscale=escala, showscale=False,
        marker_line=dict(width=0.3, color=NEGRO),
        customdata=tabla[["nombre", "detalle"]],
        hovertemplate="<b>%{customdata[0]}</b><br>%{customdata[1]}<extra></extra>",
    ))
    if distrito_mapa:
        fig.add_trace(go.Choroplethmap(
            geojson=solo(geo, [distrito_mapa]), featureidkey="properties.ubigeo", locations=[distrito_mapa],
            z=[0], colorscale=[[0, "rgba(0,0,0,0)"], [1, "rgba(0,0,0,0)"]], showscale=False,
            marker_line=dict(width=2.5, color=TINTA), hoverinfo="skip",
        ))
    fig.update_layout(
        map=dict(style="white-bg", layers=[FONDO_MAPA], center=centro, zoom=zoom),
        height=620, margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor=NEGRO,
        hoverlabel=dict(bgcolor=SUPERFICIE, bordercolor=EJE, font=dict(color=TINTA, family=FUENTE)),
    )
    return fig


# --- Página ----------------------------------------------------------------

st.set_page_config(page_title="Puentes y carreteras que se llevaron los Niños Costeros",
                   page_icon="🌉", layout="wide")
st.markdown(CSS, unsafe_allow_html=True)

temporadas, peligros, mensual, deptos, distritos, reincidentes, kpis = cargar_tablas()
geo, mapa = cargar_mapa()
NORMALES = kpis["temporadas_normales"]
temporadas["etiqueta"] = [etiqueta_temporada(f) for f in temporadas.itertuples()]

# Controles
st.sidebar.markdown("### Filtros")
opciones_temporada = {AMBOS: "Ambos Niños costeros"}
opciones_temporada |= dict(zip(temporadas.temporada, temporadas.etiqueta))
eleccion = st.sidebar.selectbox("Temporada de lluvias", list(opciones_temporada),
                                format_func=opciones_temporada.get,
                                help="Cada temporada va de diciembre a mayo.")
temps = FOCO if eleccion == AMBOS else [eleccion]
nombre_seleccion = "los dos Niños costeros" if eleccion == AMBOS else f"la temporada {eleccion}"

indicador = st.sidebar.selectbox("Indicador", list(INDICADORES), format_func=lambda k: INDICADORES[k][0],
                                 help="Colorea el mapa y ordena los rankings.")
etiqueta_ind, unidad_ind, dec_ind = INDICADORES[indicador]

lista_deptos = sorted(distritos.departamento.unique(), key=depto)
departamento = st.sidebar.selectbox("Departamento", [None] + lista_deptos,
                                    format_func=lambda d: "Todo el Perú" if d is None else depto(d))
zona = "el Perú" if departamento is None else depto(departamento)

catalogo = distritos.drop_duplicates("ubigeo")[["ubigeo", "ubigeo_mapa", "departamento", "provincia", "distrito", "region_natural"]]
if departamento:
    catalogo = catalogo[catalogo.departamento == departamento]
catalogo = catalogo.assign(nombre=[f"{titulo(f.distrito)} · {titulo(f.provincia)} ({depto(f.departamento)})"
                                   for f in catalogo.itertuples()]).sort_values("nombre")
nombres_distrito = dict(zip(catalogo.ubigeo, catalogo.nombre))
distrito = st.sidebar.selectbox("Buscar distrito", list(nombres_distrito), index=None,
                                format_func=nombres_distrito.get, placeholder="Escribe un nombre…",
                                help="Solo distritos con algún daño vial registrado entre 2016 y 2024.")

st.sidebar.markdown(
    f"<div class='sub'>Datos: INDECI-SINPAD, IGP/ENFEN e IGN. Periodo: enero de 2016 a mayo de 2024.<br>"
    f"<a href='{REPO}'>Código y datos en GitHub</a></div>", unsafe_allow_html=True)

# Encabezado
st.title("Puentes y carreteras que se llevaron los Niños Costeros")
st.markdown("<p class='pregunta'>¿Cuánta infraestructura vial destruyeron los Niños Costeros de 2017 y 2023, "
            "dónde se concentró el daño y qué distritos la perdieron en ambos eventos?</p>", unsafe_allow_html=True)
st.markdown(
    "Este tablero suma los puentes y kilómetros de vía que las autoridades locales reportaron como destruidos "
    "o afectados por lluvias, huaicos e inundaciones en el SINPAD. Compara las temporadas de lluvias de los dos "
    "Niños costeros con una temporada normal y marca los distritos que perdieron infraestructura en ambos.")
st.markdown("<p class='sub'>Cobertura: Perú, por distrito · enero de 2016 a mayo de 2024 · temporadas de "
            "diciembre a mayo · Fuentes: INDECI-SINPAD (emergencias y daños), IGP y ENFEN (ICEN y fechas "
            "oficiales de El Niño), IGN (límites distritales).</p>", unsafe_allow_html=True)

# Selección: distritos de la zona en las temporadas elegidas
zona_distritos = distritos if departamento is None else distritos[distritos.departamento == departamento]
sel = zona_distritos[zona_distritos.temporada.isin(temps)]
zona_reinc = reincidentes if departamento is None else reincidentes[reincidentes.departamento == departamento]
set_reinc = set(zona_reinc.ubigeo)

totales = totales_por_temporada(distritos, temporadas, departamento, indicador)
mediana = totales.loc[totales.temporada.isin(NORMALES), "valor"].median()
promedio = totales.loc[totales.temporada.isin(temps), "valor"].mean()
multiplicador = promedio / mediana if mediana > 0 else None

con_destruccion = set(sel.loc[sel.distritos_con_destruccion > 0, "ubigeo"])

c1, c2, c3, c4 = st.columns(4)
tarjeta(c1, "Puentes destruidos", num(sel.puentes_destruidos.sum()),
        f"En {nombre_seleccion}, en {zona}.")
nota_mult = (f"{etiqueta_ind} {'por temporada ' if eleccion == AMBOS else ''}frente a la mediana de las "
             f"4 temporadas normales ({num(mediana, dec_ind)}).")
if mediana == 0:
    nota_mult = "Sin daño en las temporadas normales de referencia: no se puede comparar."
tarjeta(c2, "Veces una temporada normal", veces(multiplicador), nota_mult)
tarjeta(c3, "Km de carretera destruidos", num(sel.carretera_destruida_km.sum()),
        f"Red nacional y departamental. Más {num(sel.camino_rural_destruido_km.sum())} km de camino rural.")
tarjeta(c4, "Distritos con destrucción vial", num(len(con_destruccion)),
        f"De ellos, {num(len(con_destruccion & set_reinc))} perdieron puentes o vías en los dos Niños.")
st.write("")

tab_mapa, tab_temp, tab_dep, tab_reinc, tab_hall, tab_met = st.tabs(
    ["Mapa", "Temporadas", "Departamentos", "Reincidentes", "Hallazgos", "Metodología y fuentes"])

# --- Mapa ---
with tab_mapa:
    modo = st.radio("Qué mostrar", ["Daño en la temporada elegida", "Reincidencia entre 2017 y 2023"],
                    horizontal=True, label_visibility="collapsed")
    zona_mapa = mapa if departamento is None else mapa[mapa.departamento == departamento]
    geo_zona = geo if departamento is None else solo(geo, zona_mapa.ubigeo_mapa)
    ubigeo_mapa_sel = None
    if distrito:
        ubigeo_mapa_sel = catalogo.set_index("ubigeo").at[distrito, "ubigeo_mapa"]
        ubigeo_mapa_sel = ubigeo_mapa_sel if isinstance(ubigeo_mapa_sel, str) else None
    encuadre_zona = zona_mapa[zona_mapa.ubigeo_mapa == ubigeo_mapa_sel] if ubigeo_mapa_sel else zona_mapa
    centro, zoom = encuadre(encuadre_zona)
    if ubigeo_mapa_sel:
        zoom = min(zoom - 1.2, 9)

    if modo.startswith("Daño"):
        por_temp = (sel.dropna(subset=["ubigeo_mapa"])
                    .pivot_table(index="ubigeo_mapa", columns="temporada", values=indicador, aggfunc="sum"))
        tabla = zona_mapa.set_index("ubigeo_mapa")[["nombre"]].join(por_temp)
        partes = tabla.reindex(columns=temps).fillna(0)
        tabla["valor"] = partes.sum(axis=1)
        tabla["clase"], etiquetas = clases(tabla.valor, dec_ind)
        if len(temps) > 1:
            tabla["detalle"] = [f"{etiqueta_ind}: {valor(v, indicador)}<br>2017: {num(a, dec_ind)} · 2023: {num(b, dec_ind)}"
                                for v, a, b in zip(tabla.valor, partes["2016-17"], partes["2022-23"])]
        else:
            tabla["detalle"] = [f"{etiqueta_ind}: {valor(v, indicador)}" for v in tabla.valor]
        colores = [SIN_DANO] + tonos(len(etiquetas) - 1)
        leyenda_html(list(zip(etiquetas, colores)), f"{etiqueta_ind} en {nombre_seleccion}:")
    else:
        foco = (zona_distritos[zona_distritos.temporada.isin(FOCO)].dropna(subset=["ubigeo_mapa"])
                .pivot_table(index=["ubigeo", "ubigeo_mapa"], columns="temporada",
                             values="distritos_con_destruccion", aggfunc="max", fill_value=0)
                .reindex(columns=FOCO, fill_value=0).reset_index())
        foco["d17"], foco["d23"] = foco["2016-17"] > 0, foco["2022-23"] > 0
        foco["ambos"] = foco.d17 & foco.d23
        por_poligono = foco.groupby("ubigeo_mapa")[["ambos", "d17", "d23"]].any()
        tabla = zona_mapa.set_index("ubigeo_mapa")[["nombre"]]
        tabla = tabla.join(por_poligono.reindex(tabla.index, fill_value=False))
        tabla["clase"] = 0
        tabla.loc[tabla.d23 & ~tabla.ambos, "clase"] = 2
        tabla.loc[tabla.d17 & ~tabla.ambos, "clase"] = 1
        tabla.loc[tabla.ambos, "clase"] = 3
        # Mazamari y Pangoa comparten polígono: uno tuvo destrucción en 2017 y el otro en 2023.
        mixto = tabla.d17 & tabla.d23 & ~tabla.ambos
        resumen = (zona_distritos[zona_distritos.temporada.isin(FOCO)].dropna(subset=["ubigeo_mapa"])
                   .pivot_table(index="ubigeo_mapa", columns="temporada",
                                values=["puentes_destruidos", "km_via_destruidos"], aggfunc="sum")
                   .reindex(columns=pd.MultiIndex.from_product([["puentes_destruidos", "km_via_destruidos"], FOCO]),
                            fill_value=0))
        resumen = resumen.reindex(tabla.index).fillna(0)
        textos = ["Sin destrucción vial en ninguno de los dos", "Destrucción solo en el Niño 2017",
                  "Destrucción solo en el Niño 2023", "Destrucción en los dos Niños (reincidente)"]
        tabla["detalle"] = [
            f"{'Polígono de dos distritos: destrucción en 2017 en uno y en 2023 en el otro' if m else textos[c]}"
            f"<br>Puentes destruidos · 2017: {num(r[('puentes_destruidos', '2016-17')])} · "
            f"2023: {num(r[('puentes_destruidos', '2022-23')])}<br>Km de vía destruidos · 2017: "
            f"{num(r[('km_via_destruidos', '2016-17')], 1)} · 2023: {num(r[('km_via_destruidos', '2022-23')], 1)}"
            for c, m, (_, r) in zip(tabla.clase, mixto, resumen.iterrows())]
        colores = [SIN_DANO, COLOR_2017, COLOR_2023, COLOR_AMBOS]
        conteo = tabla.clase.value_counts()
        nombres_clase = ["Ninguno", "Solo Niño 2017", "Solo Niño 2023", "Ambos Niños"]
        leyenda_html([(f"{nombres_clase[i]} ({num(conteo.get(i, 0))})", colores[i]) for i in (3, 1, 2, 0)],
                     "Distritos con puentes o vías destruidos:")

    mostrar(figura_mapa(geo_zona, tabla.reset_index(), colores, centro, zoom, ubigeo_mapa_sel), "mapa")
    st.caption(("Cortes de color en cuantiles de los distritos con daño. " if modo.startswith("Daño") else
                "Este modo siempre compara las temporadas 2016-17 y 2022-23, sin importar la temporada elegida. ")
               + "Mapa distrital del IGN (2020): 16 distritos creados después no tienen polígono y no aparecen.")

    if distrito:
        info = catalogo.set_index("ubigeo").loc[distrito]
        t_dist = totales_por_temporada(distritos[distritos.ubigeo == distrito], temporadas, None, indicador)
        estado = ("**reincidente**: perdió puentes o vías en los dos Niños" if distrito in set(reincidentes.ubigeo)
                  else "no es reincidente")
        st.markdown(f"#### {info.nombre}")
        st.markdown(f"Región {titulo(info.region_natural)} · {estado}.")
        if not isinstance(info.ubigeo_mapa, str):
            st.caption("Este distrito se creó después del mapa de 2020, así que no aparece en el mapa.")
        mostrar(figura_temporadas(t_dist, indicador, None, alto=300), "ficha")

# --- Temporadas ---
with tab_temp:
    st.markdown(f"#### {etiqueta_ind} por temporada de lluvias en {zona}")
    st.caption("Línea punteada: mediana de las 4 temporadas sin ningún mes de Niño costero (2017-18, 2019-20, "
               "2020-21 y 2021-22). Las cifras sobre las barras son las de los dos Niños costeros.")
    mostrar(figura_temporadas(totales, indicador, mediana), "temporadas")

    st.markdown(f"#### Mes a mes en {zona}, junto al calentamiento del mar")
    st.caption("Las franjas marcan los meses de cada evento El Niño costero según la lista oficial del IGP "
               "(criterio ENFEN). La línea punteada del ICEN es 0,4 °C, el umbral de condición cálida. "
               "El ICEN es nacional: no cambia con el departamento.")
    serie = mensual[mensual.departamento == (departamento or "PERÚ")]
    mostrar(figura_mensual(serie, indicador), "mensual")

    st.markdown(f"#### {etiqueta_ind} por tipo de peligro (todo el Perú)")
    st.caption("El tipo de peligro es la etiqueta con que la autoridad local registró la emergencia. Una lluvia "
               "intensa suele desencadenar huaicos, así que la división es aproximada."
               + (" Este gráfico es nacional: no cambia con el departamento." if departamento else ""))
    mostrar(figura_peligros(peligros, indicador), "peligros")

# --- Departamentos ---
with tab_dep:
    st.markdown(f"#### {etiqueta_ind} por departamento")
    leyenda_html([("Costa norte (Tumbes, Piura, Lambayeque y La Libertad)", COSTA_NORTE_COLOR),
                  ("Resto del país", RESTO_COLOR)])
    if departamento:
        st.caption(f"El ranking muestra todos los departamentos; {zona} aparece marcado con ▸.")
    columnas = st.columns(len(temps))
    for col, temporada in zip(columnas, temps):
        tabla_dep = deptos[deptos.temporada == temporada]
        total = tabla_dep[indicador].sum()
        costa = tabla_dep.loc[tabla_dep.departamento.isin(COSTA_NORTE), indicador].sum()
        with col:
            st.markdown(f"**{opciones_temporada[temporada]}**")
            st.markdown(f"<p class='sub'>La costa norte concentra el {num(costa / total * 100 if total else 0)} % "
                        f"del total nacional ({valor(total, indicador)}).</p>", unsafe_allow_html=True)
            mostrar(figura_ranking(tabla_dep, indicador, departamento), f"ranking_{temporada}")

# --- Reincidentes ---
with tab_reinc:
    k_reinc = kpis["reincidentes"]
    if departamento is None:
        st.markdown(
            f"**{num(k_reinc['distritos'])} distritos** perdieron puentes o vías en los dos Niños costeros. "
            f"Juntos suman **{num(k_reinc['puentes_destruidos_en_ambos'])} puentes destruidos**, el "
            f"{num(k_reinc['pct_de_los_puentes_destruidos_en_ambos_ninos'], 1)} % de los destruidos en los dos eventos.")
    else:
        st.markdown(f"En {zona}, **{num(len(zona_reinc))} distritos** perdieron puentes o vías en los dos Niños "
                    f"costeros. Juntos suman **{num(zona_reinc.puentes_destruidos_ambos.sum())} puentes destruidos**.")

    if zona_reinc.empty:
        st.info("No hay distritos reincidentes en esta zona.")
    else:
        valores = (distritos[distritos.ubigeo.isin(set_reinc) & distritos.temporada.isin(FOCO)]
                   .pivot_table(index="ubigeo", columns="temporada", values=indicador, aggfunc="sum")
                   .reindex(columns=FOCO, fill_value=0).fillna(0))
        valores["total"] = valores.sum(axis=1)
        top = (valores.join(zona_reinc.set_index("ubigeo")[["distrito", "departamento"]])
               .sort_values("total", ascending=False).head(15))
        top = top[top.total > 0]
        top["etiqueta"] = [f"{titulo(f.distrito)} ({depto(f.departamento)})" for f in top.itertuples()]
        st.markdown(f"#### Los {len(top)} reincidentes con más {etiqueta_ind.lower()}")
        if not top.empty:
            mostrar(figura_top_reincidentes(top, indicador), "top_reincidentes")

        st.markdown("#### Lista completa")
        busqueda = st.text_input("Filtrar por distrito o provincia", placeholder="Por ejemplo: Supe")
        lista = zona_reinc.copy()
        if busqueda:
            patron = busqueda.strip().upper()
            lista = lista[lista.distrito.str.contains(patron, regex=False) | lista.provincia.str.contains(patron, regex=False)]
        lista = pd.DataFrame({
            "Distrito": lista.distrito.map(titulo),
            "Provincia": lista.provincia.map(titulo),
            "Departamento": lista.departamento.map(depto),
            "Región": lista.region_natural.map(titulo),
            "Puentes 2017": lista["puentes_destruidos_2016-17"],
            "Puentes 2023": lista["puentes_destruidos_2022-23"],
            "Km de vía 2017": lista["km_via_destruidos_2016-17"],
            "Km de vía 2023": lista["km_via_destruidos_2022-23"],
            "Temporadas con destrucción": lista.temporadas_con_destruccion,
            "UBIGEO": lista.ubigeo,
        })
        st.dataframe(lista, hide_index=True, height=420, column_config={
            "Puentes 2017": st.column_config.NumberColumn(format="%d", help="Puentes destruidos en 2016-17"),
            "Puentes 2023": st.column_config.NumberColumn(format="%d", help="Puentes destruidos en 2022-23"),
            "Km de vía 2017": st.column_config.NumberColumn(format="%.1f", help="Km de vía destruidos en 2016-17"),
            "Km de vía 2023": st.column_config.NumberColumn(format="%.1f", help="Km de vía destruidos en 2022-23"),
            "Temporadas con destrucción": st.column_config.NumberColumn(
                format="%d de 8", help="Temporadas completas (2016-17 a 2023-24) con destrucción vial"),
        })
        st.download_button("Descargar esta lista (CSV)", lista.to_csv(index=False).encode("utf-8-sig"),
                           file_name="distritos_reincidentes.csv", mime="text/csv")
        st.caption("Reincidente: al menos un puente destruido o algún km de vía destruido tanto en la temporada "
                   "2016-17 como en la 2022-23. Las columnas 2017 y 2023 son puentes y km de vía destruidos en "
                   "cada Niño. «Temporadas con destrucción» cuenta las 8 temporadas completas del periodo "
                   "(2016-17 a 2023-24).")

# --- Hallazgos ---
with tab_hall:
    f17, f23 = kpis["temporadas_foco"]["2016-17"], kpis["temporadas_foco"]["2022-23"]
    med = kpis["mediana_normal"]

    def segundo(temporada, columna):
        fila = deptos[deptos.temporada == temporada].nlargest(2, columna).iloc[1]
        return f"{depto(fila.departamento)} ({num(fila[columna])})"

    lluvias = peligros[peligros.grupo_peligro == "Lluvias"].set_index("temporada").puentes_destruidos
    top4 = reincidentes.nlargest(4, "puentes_destruidos_ambos")

    with st.container(border=True):
        st.markdown("##### 1. Un Niño costero destruye entre 3 y 4 veces más puentes que una temporada de lluvias normal")
        st.dataframe(pd.DataFrame({
            "Temporada (diciembre a mayo)": ["Mediana de las 4 temporadas normales", "2016-17 · Niño Costero 2017",
                                             "2022-23 · Niño Costero 2023"],
            "Puentes destruidos": [num(med["puentes_destruidos"], 1)] + [
                f"{num(f['puentes_destruidos'])} ({veces(f['puentes_destruidos'] / med['puentes_destruidos'])})" for f in (f17, f23)],
            "Km de carretera destruidos": [num(med["carretera_destruida_km"])] + [
                f"{num(f['carretera_destruida_km'])} ({veces(f['carretera_destruida_km'] / med['carretera_destruida_km'])})" for f in (f17, f23)],
            "Distritos con destrucción vial": [num(med["distritos_con_destruccion"])] + [
                f"{num(f['distritos_con_destruccion'])} ({veces(f['distritos_con_destruccion'] / med['distritos_con_destruccion'])})" for f in (f17, f23)],
        }), hide_index=True)

    with st.container(border=True):
        st.markdown("##### 2. El daño en carreteras se concentra en la costa norte; el daño en puentes, no")
        st.markdown(
            f"- Tumbes, Piura, Lambayeque y La Libertad suman el **{num(f17['pct_costa_norte_km_via_destruidos'])} % (2017) "
            f"y el {num(f23['pct_costa_norte_km_via_destruidos'])} % (2023) de los km de vía destruidos**, pero solo el "
            f"**{num(f17['pct_costa_norte_puentes_destruidos'])} % y el {num(f23['pct_costa_norte_puentes_destruidos'])} % "
            f"de los puentes destruidos**.\n"
            f"- Más puentes destruidos: {depto(f17['top_departamento_puentes']['departamento'])} "
            f"({num(f17['top_departamento_puentes']['puentes_destruidos'])}) y {segundo('2016-17', 'puentes_destruidos')} "
            f"en 2017; {depto(f23['top_departamento_puentes']['departamento'])} "
            f"({num(f23['top_departamento_puentes']['puentes_destruidos'])}) y {segundo('2022-23', 'puentes_destruidos')} en 2023.\n"
            f"- El daño está disperso: los 10 distritos más golpeados reúnen apenas el "
            f"{num(f17['pct_top10_distritos_puentes_destruidos'])} % y el {num(f23['pct_top10_distritos_puentes_destruidos'])} % "
            f"de los puentes destruidos de cada temporada.")

    with st.container(border=True):
        total_puentes = f17["puentes_destruidos"] + f23["puentes_destruidos"]
        st.markdown(f"##### 3. {num(k_reinc['distritos'])} distritos perdieron infraestructura vial en los dos Niños")
        st.markdown(
            f"- Concentran el **{num(k_reinc['pct_de_los_puentes_destruidos_en_ambos_ninos'])} % de los puentes destruidos** "
            f"en los dos eventos ({num(k_reinc['puentes_destruidos_en_ambos'])} de {num(total_puentes)}).\n"
            f"- Más reincidentes: " + ", ".join(f"{depto(d)} ({num(n)})" for d, n in k_reinc["por_departamento"].items()) + ".\n"
            f"- Más puentes perdidos sumando los dos eventos: "
            + ", ".join(f"{titulo(f.distrito)} ({depto(f.departamento)}, {num(f.puentes_destruidos_ambos)})" for f in top4.itertuples())
            + ".")

    with st.container(border=True):
        st.markdown("##### 4. Cada Niño golpeó de forma distinta")
        st.markdown(
            f"- El de 2017 destruyó tres veces más km de vía que el de 2023: **{num(f17['km_via_destruidos'])} km** frente a "
            f"{num(f23['km_via_destruidos'])}.\n"
            f"- El de 2023 destruyó más puentes: **{num(f23['puentes_destruidos'])}** frente a {num(f17['puentes_destruidos'])}.\n"
            f"- En ambos, la mayor parte del daño se registró como «lluvia intensa»: {num(lluvias['2016-17'])} de "
            f"{num(f17['puentes_destruidos'])} puentes en 2017 ({num(lluvias['2016-17'] / f17['puentes_destruidos'] * 100)} %) y "
            f"{num(lluvias['2022-23'])} de {num(f23['puentes_destruidos'])} en 2023 "
            f"({num(lluvias['2022-23'] / f23['puentes_destruidos'] * 100)} %).")

# --- Metodología y fuentes ---
with tab_met:
    st.markdown(f"""
#### Fuentes

| Fuente | Qué aporta | Licencia |
|---|---|---|
| INDECI, SINPAD: [Emergencias y daños a nivel nacional](https://www.datosabiertos.gob.pe/dataset/emergencias-y-da%C3%B1os-nivel-nacional-por-departamento) | Puentes y km de vía destruidos y afectados por emergencia y distrito | ODC-By |
| IGP y ENFEN: [Índice Costero El Niño (ICEN)](http://met.igp.gob.pe/variabclim/indices.html) | Calentamiento del mar y fechas oficiales de cada Niño costero | Dato público |
| IGN, vía OCHA HDX: [límites administrativos (COD-AB)](https://data.humdata.org/dataset/cod-ab-per) | Polígonos de los distritos (vigentes al 14/07/2020) | CC BY-IGO |

Todos los archivos se descargaron el 01/11/2026. El registro con URL, licencia y SHA-256 de cada uno está en
[`datos/fuentes.csv`]({REPO}/datos/fuentes.csv).

#### Cómo se construyó

- **Periodo:** enero de 2016 a mayo de 2024 (10 817 registros de lluvias, huaicos e inundaciones con daño vial).
- **Temporada de lluvias:** de diciembre a mayo; 2016-17 va de diciembre de 2016 a mayo de 2017. El 98,2 % de los
  puentes destruidos del periodo cae en esos meses.
- **Fechas oficiales de los dos eventos** (IGP, criterio ENFEN 2024): Niño Costero 2017, de enero a abril de 2017
  (moderado); Niño Costero 2023, de marzo de 2023 a febrero de 2024 (fuerte).
- **Línea base:** mediana de las 4 temporadas sin ningún mes de Niño costero (2017-18, 2019-20, 2020-21 y 2021-22).
  «Veces una temporada normal» divide el valor de la temporada entre esa mediana, en la misma zona.
- **Km de vía** = km de carretera (red nacional y departamental) + km de camino rural (red vecinal).
- **Distrito con destrucción vial:** al menos un puente destruido o algún km de vía destruido en la temporada.
- **Reincidente:** distrito con destrucción vial tanto en 2016-17 como en 2022-23.
- **Peligros:** lluvias, huaicos y deslizamientos (con derrumbes y aluviones) e inundaciones.
- **Valores extremos:** se revisaron a mano los 22 valores sobre el percentil 99,9. Solo se anuló un registro
  inverosímil (Candarave, Tacna, 2024: 100 puentes destruidos y 1000 afectados).

#### Limitaciones

- **Subregistro:** el SINPAD recoge lo que reportan las autoridades locales; puede haber daños no reportados.
- **El SINPAD no marca qué daños se deben a El Niño:** se aproxima con la temporada de lluvias y las fechas
  oficiales. Parte del daño de una temporada con Niño puede deberse a otras lluvias.
- **Más reportes con los años:** el sistema pasó de 4492–5489 registros anuales en 2018-2020 a 7251–7799 en
  2021-2022 sin un Niño fuerte. Por eso la línea base usa la mediana y los titulares usan puentes.
- **Los puentes se cuentan sin distinguir tamaño:** un puente peatonal pesa lo mismo que uno vehicular.
- **Posible mezcla de unidades en caminos rurales** («km o metros» según el diccionario): los 2300 km de camino
  rural destruidos en 2017 deben leerse con cautela.
- **Sin valorización en soles:** el dataset solo trae el costo de la ayuda humanitaria.
- **Mapa de 2020:** 16 distritos creados después no tienen polígono (60 registros viales). Si un distrito se
  dividió después de 2017, su daño de 2023 queda en el distrito nuevo y la reincidencia puede subestimarse.
- **Línea base corta:** solo hay 4 temporadas normales en el periodo.
- **Enero a mayo de 2016 solo aparece en la serie mensual:** su temporada (2015-16) queda incompleta porque el
  periodo empieza en enero de 2016, así que no se muestra en los gráficos por temporada.
""")
    st.markdown("#### Descargar los datos filtrados")
    st.caption(f"Distritos con daño vial en {nombre_seleccion}, en {zona}: una fila por distrito y temporada.")
    st.download_button("Descargar CSV", sel.to_csv(index=False).encode("utf-8-sig"),
                       file_name="dano_vial_por_distrito.csv", mime="text/csv")
    st.markdown(f"Código, datos y documentación: [{REPO.removeprefix('https://')}]({REPO})")
