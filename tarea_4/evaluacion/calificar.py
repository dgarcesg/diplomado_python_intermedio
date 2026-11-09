"""Califica las corridas de evaluacion/corridas/ contra evaluacion/preguntas.csv y escribe evaluacion/resultados.csv.

    python evaluacion/calificar.py

Una respuesta es correcta si contiene cada cifra esperada dentro de su tolerancia y las etiquetas requeridas (mes,
departamento o, en las mixtas, el rechazo de una conclusión causal). Las cifras se leen en formato peruano o
anglosajón ("1,97", "1.97", "108,664", "37 819,7"). El resultado automático se revisa a mano: las correcciones van en
evaluacion/revision_manual.csv (id, modo, correcto, nota) y prevalecen sobre la calificación automática.
"""
import csv
import json
import re
import sys
from pathlib import Path

EVAL = Path(__file__).resolve().parent
CAUSAL = re.compile(r"causal|no (se )?(puede|pueden|permite|permiten|basta|alcanza)[^.]{0,60}(concluir|afirmar|"
                    r"atribuir|establecer|inferir|deducir)|no implica|correlaci|asociaci", re.I)
NO_SABE = re.compile(r"no (puedo|pude|tengo)[^.]{0,40}(verificar|acceso|obtener|confirmar)", re.I)


def candidatos(texto):
    """Todas las lecturas posibles de cada número del texto."""
    vals = set()
    for t in re.findall(r"\d[\d.,   ]*\d|\d", texto):
        t = re.sub(r"[   ]", "", t)
        for v in (t.replace(",", ""), t.replace(".", "").replace(",", "."), t.replace(",", ".")):
            try:
                vals.add(float(v))
            except ValueError:
                pass
    return vals


def leer_corrida(modo, id_):
    texto, herramientas, skills, ms, es_error = "", [], [], None, False
    ruta = EVAL / "corridas" / f"{modo}_{id_}.jsonl"
    for linea in ruta.read_text(encoding="utf-8").splitlines() if ruta.exists() else []:
        try:
            d = json.loads(linea)
        except json.JSONDecodeError:
            continue
        if d.get("type") == "assistant":
            for b in d["message"]["content"]:
                if b.get("type") == "tool_use":
                    if b["name"] == "Skill":
                        skills.append(b["input"].get("skill", "?"))
                    herramientas.append(b["name"])
        if d.get("type") == "result":
            texto, ms, es_error = d.get("result") or "", d.get("duration_ms"), d.get("is_error", False)
    meta_ruta = EVAL / "corridas" / f"{modo}_{id_}.meta.json"
    meta = json.loads(meta_ruta.read_text(encoding="utf-8")) if meta_ruta.exists() else {}
    return texto, herramientas, skills, meta.get("segundos"), meta.get("error") or ("error" if es_error else None)


def fuente(modo, herramientas, skills):
    if modo == "A":
        return "Conocimiento del modelo (sin herramientas de datos)"
    partes = []
    mcp = sorted({h.replace("mcp__bcrp__", "") for h in herramientas if h.startswith("mcp__bcrp__")})
    if mcp:
        partes.append("MCP bcrp: " + ", ".join(mcp))
    if any(h == "ReadMcpResourceTool" for h in herramientas):
        partes.append("recurso MCP")
    if skills:
        partes.append("Skills: " + ", ".join(dict.fromkeys(skills)))
    if any(h in herramientas for h in ("Read", "Bash", "Grep", "Glob")):
        partes.append("archivos/scripts del proyecto")
    return "; ".join(partes) or "Sin herramientas"


def calificar(p, texto):
    if not texto.strip():
        return 0, "sin respuesta"
    vals = candidatos(texto)
    esperados = [float(v) for v in p["valores_esperados"].split(";")]
    tolerancias = [float(t) for t in p["tolerancia"].split(";")]
    faltan = [str(e) for e, t in zip(esperados, tolerancias) if not any(abs(v - e) <= t + 1e-9 for v in vals)]
    etiquetas = [g for g in p["etiquetas_requeridas"].split(";") if g]
    sin_etiqueta = []
    for g in etiquetas:
        if g == "no causal":
            if not CAUSAL.search(texto):
                sin_etiqueta.append("rechazo de causalidad")
        elif not any(alt.lower() in texto.lower() for alt in g.split("|")):
            sin_etiqueta.append(g)
    if not faltan and not sin_etiqueta:
        return 1, "cifras dentro de la tolerancia" + (" y etiquetas presentes" if etiquetas else "")
    if faltan and NO_SABE.search(texto) and len(faltan) == len(esperados):
        return 0, "no contestada: dice no poder verificar"
    return 0, "; ".join(filter(None, [f"falta o fuera de tolerancia: {', '.join(faltan)}" if faltan else "",
                                      f"falta: {', '.join(sin_etiqueta)}" if sin_etiqueta else ""]))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    preguntas = list(csv.DictReader(open(EVAL / "preguntas.csv", encoding="utf-8")))
    revision = {}
    if (EVAL / "revision_manual.csv").exists():
        for r in csv.DictReader(open(EVAL / "revision_manual.csv", encoding="utf-8")):
            revision[(r["id"], r["modo"])] = r
    filas = []
    for modo in ("A", "B"):
        for p in preguntas:
            texto, herramientas, skills, seg, error = leer_corrida(modo, p["id"])
            ok, criterio = calificar(p, texto)
            if (p["id"], modo) in revision:
                r = revision[(p["id"], modo)]
                ok, criterio = int(r["correcto"]), f"revisión manual: {r['nota']}"
            filas.append({"id": p["id"], "tipo": p["tipo"], "modo": modo, "pregunta": p["pregunta"],
                          "respuesta_esperada": p["respuesta_esperada"], "respuesta_generada": " ".join(texto.split()),
                          "fuente_utilizada": fuente(modo, herramientas, skills),
                          "herramientas_usadas": ", ".join(dict.fromkeys(herramientas)) or "ninguna",
                          "correcto": ok, "criterio": criterio, "tiempo_s": seg, "error": error or ""})
    with open(EVAL / "resultados.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]))
        w.writeheader()
        w.writerows(filas)
    for modo in ("A", "B"):
        fs = [f for f in filas if f["modo"] == modo]
        tiempos = [f["tiempo_s"] for f in fs if f["tiempo_s"] is not None]
        print(f"Modo {modo}: {sum(f['correcto'] for f in fs)}/10 correctas · tiempo promedio "
              f"{sum(tiempos) / len(tiempos):.1f} s" if tiempos else f"Modo {modo}: sin corridas")
        for f in fs:
            print(f"  {f['id']} {'✔' if f['correcto'] else '✘'} {f['tiempo_s']} s · {f['criterio']} · {f['fuente_utilizada']}")


if __name__ == "__main__":
    main()
