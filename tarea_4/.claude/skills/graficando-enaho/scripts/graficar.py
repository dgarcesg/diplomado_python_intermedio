"""Gráficos de pobreza de la ENAHO 2024, siempre ponderados con facpob07.

    uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area
    uv run .claude/skills/graficando-enaho/scripts/graficar.py --por departamento --indicador pobreza_extrema
    uv run .claude/skills/graficando-enaho/scripts/graficar.py --por todos

--por: area, sexo, edad, departamento o todos. --indicador: pobreza (monetaria, por defecto) o pobreza_extrema.
Entra salidas/personas_2024.parquet (lo arma la skill limpiando-enaho) y sale figuras/<indicador>_por_<grupo>_2024.png.
El título se escribe con las cifras calculadas, así dice qué muestra el gráfico y no solo de qué trata.
"""
import argparse
import sys
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

RAIZ = Path(__file__).resolve().parents[4]
BASE = RAIZ / "salidas" / "personas_2024.parquet"
FIGURAS = RAIZ / "figuras"
AZUL, TINTA, TINTA_2, FONDO, REFERENCIA = "#2a78d6", "#0b0b0b", "#52514e", "#fcfcfb", "#8a8984"
INDICADORES = {"pobreza": ("pobre", "pobreza monetaria"), "pobreza_extrema": ("pobre_extremo", "pobreza extrema")}
GRUPOS = {"area": "area", "sexo": "sexo", "edad": "grupo_edad", "departamento": "nombre_departamento"}
NOMBRE_GRUPO = {"area": "área", "sexo": "sexo", "edad": "grupo de edad", "departamento": "departamento"}
CAJA = {"facecolor": FONDO, "edgecolor": "none", "pad": 1}  # el valor tapa la línea del promedio si se cruzan
FUENTE = ("Fuente: INEI, ENAHO 2024 (módulos 34 y 02), residentes habituales. Estimación ponderada con el factor "
          "de expansión facpob07. Elaboración propia.")


def tasas(p, grupo, columna):
    """% ponderado de personas en la condición, por grupo: suma de factores de quienes cumplen / suma de factores."""
    g = p.assign(_w=p[columna] * p.facpob07).groupby(grupo, observed=True)[["_w", "facpob07"]].sum()
    return 100 * g._w / g.facpob07


def titulo(por, s, etiqueta):
    if por == "area":
        r, u = s["Rural"], s["Urbana"]
        mayor, menor = ("rural", "urbana") if r >= u else ("urbana", "rural")
        return f"La {etiqueta} {mayor} ({max(r, u):.1f} %) supera a la {menor} ({min(r, u):.1f} %) en {abs(r - u):.1f} puntos"
    if por == "sexo":
        m, h = s["Mujer"], s["Hombre"]
        if abs(m - h) < 1:
            return f"La {etiqueta} es casi igual en mujeres ({m:.1f} %) y hombres ({h:.1f} %)"
        return f"La {etiqueta} es mayor en {'mujeres' if m > h else 'hombres'}: {max(m, h):.1f} % frente a {min(m, h):.1f} %"
    if por == "edad":
        return f"El grupo de {s.idxmax()} años tiene la {etiqueta} más alta ({s.max():.1f} %)"
    return (f"{s.idxmax()} tiene la {etiqueta} más alta ({s.max():.1f} %) y {s.idxmin()} la más baja "
            f"({s.min():.1f} %)")


def graficar(p, por, indicador):
    columna, etiqueta = INDICADORES[indicador]
    s = tasas(p, GRUPOS[por], columna)
    nacional = 100 * (p[columna] * p.facpob07).sum() / p.facpob07.sum()
    if por != "edad":  # la edad conserva su orden natural; lo demás se ordena de mayor a menor
        s = s.sort_values(ascending=por == "departamento")
    horizontal = por == "departamento"
    fig, ax = plt.subplots(figsize=(8, 9) if horizontal else (7.5, 4.8), facecolor=FONDO)
    ax.set_facecolor(FONDO)
    etiquetas = [str(i) for i in s.index]
    if horizontal:
        barras = ax.barh(etiquetas, s.values, color=AZUL, height=0.65)
        ax.axvline(nacional, color=REFERENCIA, lw=1, ls="--", zorder=0)
        ax.set_xlim(0, s.max() * 1.15)
        ax.set_xlabel(f"% de personas en {etiqueta}", color=TINTA_2)
        for b, v in zip(barras, s.values):
            ax.text(v + s.max() * 0.01, b.get_y() + b.get_height() / 2, f"{v:.1f}", va="center", fontsize=8, color=TINTA,
                    bbox=CAJA)
    else:
        barras = ax.bar(etiquetas, s.values, color=AZUL, width=0.6)
        ax.axhline(nacional, color=REFERENCIA, lw=1, ls="--", zorder=0)
        ax.set_ylim(0, s.max() * 1.18)
        ax.set_ylabel(f"% de personas en {etiqueta}", color=TINTA_2)
        for b, v in zip(barras, s.values):
            ax.text(b.get_x() + b.get_width() / 2, v + s.max() * 0.015, f"{v:.1f} %", ha="center", fontsize=9,
                    color=TINTA, bbox=CAJA)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    for lado in ("left", "bottom"):
        ax.spines[lado].set_color("#c3c2b7")
    ax.tick_params(colors=TINTA_2, labelsize=9)
    fig.suptitle(textwrap.fill(titulo(por, s, etiqueta), 70 if horizontal else 85), x=0.02, ha="left",
                 fontsize=12 if horizontal else 11, fontweight="bold", color=TINTA)
    ax.set_title(textwrap.fill(f"% de personas en {etiqueta} por {NOMBRE_GRUPO[por]}, Perú 2024 · línea punteada: "
                               f"promedio nacional ({nacional:.1f} %)", 75 if horizontal else 95),
                 loc="left", fontsize=9, color=TINTA_2)
    fig.text(0.02, 0.01, FUENTE, fontsize=7, color=TINTA_2, wrap=True)
    fig.tight_layout(rect=(0, 0.04, 1, 0.97))
    FIGURAS.mkdir(exist_ok=True)
    salida = FIGURAS / f"{indicador}_por_{por}_2024.png"
    fig.savefig(salida, dpi=200, facecolor=FONDO)
    plt.close(fig)
    print(f"{salida.relative_to(RAIZ)} · {titulo(por, s, etiqueta)}")
    print(s.round(2).to_string(header=False), f"\nPerú: {nacional:.2f}\n")


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # la consola de Windows (cp1252) no imprime ≠ ni →
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--por", choices=[*GRUPOS, "todos"], required=True)
    ap.add_argument("--indicador", choices=list(INDICADORES), default="pobreza")
    a = ap.parse_args()
    if not BASE.exists():
        sys.exit("ERROR: no existe salidas/personas_2024.parquet. Corran primero la skill limpiando-enaho.")
    p = pd.read_parquet(BASE)
    for por in (GRUPOS if a.por == "todos" else [a.por]):
        graficar(p, por, a.indicador)


if __name__ == "__main__":
    main()
