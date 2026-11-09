"""Limpia la ENAHO del INEI y arma una base de personas con pobreza, territorio y factor de expansión.

    uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024

Entra:  datos/966-Modulo34.zip (sumaria, una fila por hogar) y datos/966-Modulo02.zip (miembros, una por persona).
Sale:   salidas/personas_2024.parquet, salidas/indicadores.csv y salidas/validacion.txt.

El pipeline va siempre en el mismo orden: leer (llaves como texto), normalizar nombres, filtrar residentes habituales,
unir personas con hogares (validate="m:1"), construir indicadores, validar y guardar. Si una validación esencial falla,
el script escribe validacion.txt, borra la base vieja y termina con código 1: no se corrigen cifras a mano.
"""
import argparse
import sys
import zipfile
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[4]  # tarea_4/ (scripts → limpiando-enaho → skills → .claude → tarea_4)
DATOS, SALIDAS = RAIZ / "datos", RAIZ / "salidas"
CODIGO_INEI = {2024: "966"}  # el código de cada año en el portal de microdatos del INEI
LLAVES = ["conglome", "vivienda", "hogar"]
REFERENCIA = {"pobreza": 27.6, "urbano": 24.8, "rural": 39.3, "residentes": 108_664, "hogares": 33_691}
TOLERANCIA_PP = 0.1  # puntos porcentuales: la tarea acepta hasta 0.1 de diferencia en la pobreza nacional
DEPARTAMENTOS = {
    "01": "Amazonas", "02": "Áncash", "03": "Apurímac", "04": "Arequipa", "05": "Ayacucho", "06": "Cajamarca",
    "07": "Callao", "08": "Cusco", "09": "Huancavelica", "10": "Huánuco", "11": "Ica", "12": "Junín",
    "13": "La Libertad", "14": "Lambayeque", "15": "Lima", "16": "Loreto", "17": "Madre de Dios", "18": "Moquegua",
    "19": "Pasco", "20": "Piura", "21": "Puno", "22": "San Martín", "23": "Tacna", "24": "Tumbes", "25": "Ucayali",
}
GRUPOS_EDAD = [(0, 14, "0-14"), (15, 29, "15-29"), (30, 44, "30-44"), (45, 64, "45-64"), (65, 200, "65 y más")]


def leer(zip_path, archivo):
    """Lee el .dta del zip sin extraerlo. Las llaves llegan como texto: se verifica que conserven sus ceros."""
    if not zip_path.exists():
        sys.exit(f"ERROR: falta {zip_path.relative_to(RAIZ)}. Bájenlo del INEI: "
                 f"https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/{zip_path.name}")
    with zipfile.ZipFile(zip_path) as z:
        # el nombre exacto: el módulo 34 trae también sumaria-AAAA-12g.dta, que no es la que se usa
        nombre = next((n for n in z.namelist() if n.lower().endswith("/" + archivo)), None)
        if nombre is None:
            sys.exit(f"ERROR: {zip_path.name} no contiene {archivo}.")
        with z.open(nombre) as f:
            df = pd.read_stata(f, convert_categoricals=False)
    df.columns = df.columns.str.lower().str.replace("ñ", "n")  # "aÑo" llega como "año": queda "ano"
    return df.rename(columns={"ano": "anio"}), nombre


def tasa(df, columna, factor="facpob07"):
    """Porcentaje ponderado: suma de factores de quienes cumplen / suma de todos los factores."""
    return 100 * (df[columna] * df[factor]).sum() / df[factor].sum()


def indicadores(p, hog):
    """Pobreza por grupo con dos ponderaciones válidas: personas × facpob07 (la principal) y hogares de la sumaria ×
    factor07 × mieperho (la que reproduce las cifras publicadas por el INEI). La segunda solo existe para grupos que
    son del hogar (nacional, área, departamento); sexo y edad son de la persona."""
    filas = []

    def agregar(grupo, categoria, codigo, d, h=None):
        filas.append({"grupo": grupo, "categoria": categoria, "codigo": codigo,
                      "pobreza_pct": round(tasa(d, "pobre"), 2), "pobreza_extrema_pct": round(tasa(d, "pobre_extremo"), 2),
                      "pobreza_pct_sumaria": round(tasa(h, "pobre", "peso"), 2) if h is not None else None,
                      "poblacion_expandida": round(d.facpob07.sum()), "n_muestra": len(d)})

    agregar("nacional", "Perú", "00", p, hog)
    for area, d in p.groupby("area"):
        agregar("area", area, "", d, hog[hog.urbano == (area == "Urbana")])
    for sexo, d in p.groupby("sexo"):
        agregar("sexo", sexo, "", d)
    for edad, d in p.groupby("grupo_edad", observed=True):
        agregar("grupo_edad", edad, "", d)
    for cod, d in p.groupby("departamento"):
        agregar("departamento", DEPARTAMENTOS.get(cod, cod), cod, d, hog[hog.ubigeo.str[:2] == cod])
    return pd.DataFrame(filas)


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # la consola de Windows (cp1252) no imprime ≠ ni →
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--anio", type=int, default=2024)
    anio = ap.parse_args().anio
    if anio not in CODIGO_INEI:
        sys.exit(f"ERROR: solo está preparada la ENAHO {', '.join(map(str, CODIGO_INEI))}; no hay referencias "
                 f"oficiales cargadas para validar {anio}.")
    codigo = CODIGO_INEI[anio]
    checks = []  # (esencial, nombre, ok, detalle)

    def check(esencial, nombre, ok, detalle):
        checks.append((esencial, nombre, bool(ok), detalle))

    # 1-2. Leer y normalizar
    hogares, f_h = leer(DATOS / f"{codigo}-Modulo34.zip", f"sumaria-{anio}.dta")
    personas, f_p = leer(DATOS / f"{codigo}-Modulo02.zip", f"enaho01-{anio}-200.dta")
    hogares = hogares[[c for c in LLAVES + ["ubigeo", "dominio", "estrato", "pobreza", "factor07", "mieperho",
                                            "linea", "gashog2d", "inghog2d"] if c in hogares.columns]]
    for nombre, df, ancho in (("hogares", hogares, {"conglome": 6, "vivienda": 3, "hogar": 2, "ubigeo": 6}),
                              ("personas", personas, {"conglome": 6, "vivienda": 3, "hogar": 2, "codperso": 2})):
        ok = all(pd.api.types.is_string_dtype(df[c]) and df[c].str.len().eq(n).all() for c, n in ancho.items())
        check(True, f"Llaves de {nombre} como texto, con sus ceros iniciales", ok,
              ", ".join(f"{c}: {n} caracteres" for c, n in ancho.items()))
    check(True, "Una fila por hogar en la sumaria (llaves únicas)", not hogares.duplicated(LLAVES).any(),
          f"{len(hogares):,} hogares (referencia {REFERENCIA['hogares']:,})")
    check(True, "Una fila por persona en miembros (llaves + codperso únicas)",
          not personas.duplicated(LLAVES + ["codperso"]).any(), f"{len(personas):,} filas en el módulo 02")

    # 3. Residentes habituales: miembro del hogar presente, o ausente por menos de 30 días
    residente = (((personas.p204 == 1) & (personas.p205 == 2)) | ((personas.p204 == 2) & (personas.p206 == 1)))
    personas = personas[residente]
    check(True, "Residentes habituales", len(personas) == REFERENCIA["residentes"],
          f"{len(personas):,} (referencia {REFERENCIA['residentes']:,})")

    # 4. Unir personas (muchas) con su hogar (uno). ubigeo, estrato y dominio salen de la sumaria.
    personas = personas[LLAVES + ["codperso", "p207", "p208a", "facpob07"]]
    p = personas.merge(hogares, on=LLAVES, how="left", validate="m:1", indicator=True)
    check(True, "La unión no duplica personas", len(p) == len(personas), f"{len(p):,} filas tras unir")
    sin_hogar = int((p._merge != "both").sum())
    check(True, "Toda persona encuentra su hogar", sin_hogar == 0, f"{sin_hogar} personas sin hogar en la sumaria")
    p = p.drop(columns="_merge")

    # 5. Indicadores
    p["anio"] = anio
    p["departamento"] = p.ubigeo.str[:2]
    p["nombre_departamento"] = p.departamento.map(DEPARTAMENTOS)
    p["urbano"] = p.estrato <= 5
    p["area"] = p.urbano.map({True: "Urbana", False: "Rural"})
    p["pobre"] = (p.pobreza <= 2).astype(int)
    p["pobre_extremo"] = (p.pobreza == 1).astype(int)
    p["sexo"] = p.p207.map({1: "Hombre", 2: "Mujer"})
    p["edad"] = p.p208a
    p["grupo_edad"] = pd.cut(p.edad, [g[0] - 1 for g in GRUPOS_EDAD] + [GRUPOS_EDAD[-1][1]],
                             labels=[g[2] for g in GRUPOS_EDAD])

    # 6. Validar
    codigos = set(p.departamento)
    check(True, "Los 25 códigos territoriales (01-25), Lima y Callao separados", codigos == set(DEPARTAMENTOS),
          f"{len(codigos)} códigos; faltan {sorted(set(DEPARTAMENTOS) - codigos)}; sobran {sorted(codigos - set(DEPARTAMENTOS))}")
    check(True, "Factor de expansión facpob07 completo y positivo", p.facpob07.notna().all() and (p.facpob07 > 0).all(),
          f"{int(p.facpob07.isna().sum())} vacíos; población expandida {p.facpob07.sum():,.0f}")
    check(True, "Población expandida plausible para el Perú (30-37 millones)", 30e6 < p.facpob07.sum() < 37e6,
          f"{p.facpob07.sum() / 1e6:.2f} millones")
    nacional = tasa(p, "pobre")
    check(True, f"Pobreza monetaria nacional (personas × facpob07) a ±{TOLERANCIA_PP} pp de {REFERENCIA['pobreza']} %",
          abs(nacional - REFERENCIA["pobreza"]) <= TOLERANCIA_PP, f"{nacional:.2f} %")
    p["peso_hogar"] = p.factor07 * p.mieperho
    hog = hogares.assign(pobre=(hogares.pobreza <= 2).astype(int), peso=hogares.factor07 * hogares.mieperho)
    por_sumaria = tasa(hog, "pobre", "peso")
    check(False, f"Pobreza con la sumaria (factor07 × mieperho) a ±{TOLERANCIA_PP} pp de {REFERENCIA['pobreza']} %",
          abs(por_sumaria - REFERENCIA["pobreza"]) <= TOLERANCIA_PP, f"{por_sumaria:.2f} % (cálculo alternativo)")
    # La referencia urbano/rural del INEI se reproduce con la sumaria (hogares × miembros); con personas y facpob07
    # las cifras se mueven ~0.1 pp por la unidad de ponderación. Se informan las dos.
    hog["urbano"] = hog.estrato <= 5
    for area in ("urbano", "rural"):
        es = area == "urbano"
        en_personas, en_sumaria = tasa(p[p.urbano == es], "pobre"), tasa(hog[hog.urbano == es], "pobre", "peso")
        check(False, f"Pobreza {area} (sumaria) a ±{TOLERANCIA_PP} pp de {REFERENCIA[area]} %",
              abs(en_sumaria - REFERENCIA[area]) <= TOLERANCIA_PP,
              f"{en_sumaria:.2f} % con la sumaria; {en_personas:.2f} % con personas y facpob07")
    simple = 100 * p.pobre.mean()
    check(False, "La ponderación importa (promedio simple ≠ ponderado)", abs(simple - nacional) > 0.5,
          f"simple {simple:.2f} % vs ponderado {nacional:.2f} %: sin factor se sesga el resultado")

    # 7. Guardar
    SALIDAS.mkdir(exist_ok=True)
    base = SALIDAS / f"personas_{anio}.parquet"
    fallas = [c for c in checks if c[0] and not c[2]]
    lineas = [f"Validación ENAHO {anio} · limpiando-enaho", "=" * 60,
              f"Hogares: {f_h} | Personas: {f_p}", ""]
    for esencial, nombre, ok, detalle in checks:
        lineas.append(f"[{'PASA' if ok else 'FALLA'}] {'' if esencial else '(informativa) '}{nombre}: {detalle}")
    lineas += ["", f"Resultado: {len(checks) - len(fallas)} de {len(checks)} verificaciones aprobadas; "
                   f"{len(fallas)} esenciales fallidas."]
    if fallas:
        base.unlink(missing_ok=True)  # que nadie use una base vieja o mal construida
        lineas.append("PROCESO DETENIDO: no se guardó la base. Revisen las verificaciones marcadas FALLA.")
    else:
        p.to_parquet(base, index=False)
        indicadores(p, hog).to_csv(SALIDAS / "indicadores.csv", index=False, encoding="utf-8")
        lineas.append(f"Base guardada: salidas/{base.name} ({len(p):,} personas, {p.shape[1]} columnas) "
                      "y salidas/indicadores.csv.")
    (SALIDAS / "validacion.txt").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print("\n".join(lineas))
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    main()
