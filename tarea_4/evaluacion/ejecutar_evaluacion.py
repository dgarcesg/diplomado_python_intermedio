"""Corre las 10 preguntas de evaluación en Claude Code, una sesión independiente por pregunta, en uno de dos modos.

    python evaluacion/ejecutar_evaluacion.py --modo A --preguntas <preguntas.csv> --vacia <carpeta_vacía>
    python evaluacion/ejecutar_evaluacion.py --modo B --preguntas <preguntas.csv>

Modo A (sin MCP ni Skills): corre en una carpeta vacía fuera del proyecto, sin servidores MCP (--strict-mcp-config sin
--mcp-config), sin Skills y sin shell ni web, así que no puede leer salidas ya calculadas ni bajar datos: responde con
lo que sabe el modelo.
Modo B (con MCP y Skills): corre en tarea_4/, con solo el MCP bcrp (evaluacion/mcp_bcrp.json), las Skills del proyecto
y la shell para ejecutarlas; sin web, para que la mejora se deba a las herramientas propias.

Los dos modos usan el mismo modelo y la misma instrucción. Cada corrida se guarda completa (stream-json) en
evaluacion/corridas/<modo>_<id>.jsonl, con el tiempo medido desde afuera.
"""
import argparse
import csv
import json
import subprocess
import sys
import time
from pathlib import Path

TAREA4 = Path(__file__).resolve().parents[1]
MODELO = "sonnet"
INSTRUCCION = ("\n\nResponde en español y en pocas líneas: da la cifra con su unidad, el periodo y la fuente. Si no "
               "puedes obtener o verificar el dato, dilo en vez de inventarlo.")
COMUNES = ["claude", "-p", "--model", MODELO, "--output-format", "stream-json", "--verbose"]
MODOS = {
    "A": COMUNES + ["--strict-mcp-config",
                    "--disallowedTools", "Skill", "Bash", "PowerShell", "WebSearch", "WebFetch", "Write", "Edit",
                    "NotebookEdit", "Agent"],
    "B": COMUNES + ["--mcp-config", str(TAREA4 / "evaluacion" / "mcp_bcrp.json"), "--strict-mcp-config",
                    "--allowedTools", "mcp__bcrp", "ListMcpResourcesTool", "ReadMcpResourceTool", "Skill", "Bash",
                    "Read", "Glob", "Grep",
                    "--disallowedTools", "WebSearch", "WebFetch", "Agent"],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modo", choices=list(MODOS), required=True)
    ap.add_argument("--preguntas", required=True)
    ap.add_argument("--vacia", help="carpeta vacía para el modo A")
    ap.add_argument("--solo", help="ids separados por coma, para repetir algunas")
    a = ap.parse_args()
    cwd = Path(a.vacia) if a.modo == "A" else TAREA4
    if a.modo == "A" and (not a.vacia or any(cwd.iterdir())):
        sys.exit("El modo A necesita --vacia con una carpeta vacía.")
    salida = TAREA4 / "evaluacion" / "corridas"
    salida.mkdir(parents=True, exist_ok=True)
    preguntas = list(csv.DictReader(open(a.preguntas, encoding="utf-8")))
    for p in preguntas:
        if a.solo and p["id"] not in a.solo.split(","):
            continue
        inicio = time.time()
        try:
            r = subprocess.run(MODOS[a.modo], input=p["pregunta"] + INSTRUCCION, cwd=cwd, capture_output=True,
                               text=True, encoding="utf-8", timeout=420)
            salida_txt, error = r.stdout, (r.stderr.strip() or None) if r.returncode else None
        except subprocess.TimeoutExpired as e:
            salida_txt, error = (e.stdout or b"").decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or ""), "timeout 420 s"
        segundos = round(time.time() - inicio, 1)
        (salida / f"{a.modo}_{p['id']}.jsonl").write_text(salida_txt, encoding="utf-8")
        meta = {"modo": a.modo, "id": p["id"], "segundos": segundos, "error": error, "modelo": MODELO,
                "cwd": "carpeta vacía" if a.modo == "A" else "tarea_4", "inicio": time.strftime("%Y-%m-%d %H:%M:%S")}
        (salida / f"{a.modo}_{p['id']}.meta.json").write_text(json.dumps(meta, ensure_ascii=False), encoding="utf-8")
        print(f"{a.modo} {p['id']}: {segundos} s{' · ' + error[:80] if error else ''}", flush=True)


if __name__ == "__main__":
    main()
