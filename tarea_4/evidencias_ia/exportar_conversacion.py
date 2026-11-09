"""Convierte el registro de una sesión de Claude Code (.jsonl) en un markdown legible para evidencias_ia/.

    python evidencias_ia/exportar_conversacion.py <sesion.jsonl> <salida.md> "<título>" [términos_a_ocultar.txt]

El cuarto argumento, opcional, es un archivo fuera del repositorio con un término por línea (por ejemplo, nombres de
otras personas que aparezcan en los comandos): cada uno se reemplaza por [oculto].

Claude Code guarda cada sesión en ~/.claude/projects/<carpeta-del-proyecto>/<id-de-sesion>.jsonl. El markdown conserva,
en orden, los mensajes de la usuaria (también los que escribió mientras Claude trabajaba), las respuestas de Claude y
cada herramienta que usó, con su entrada y su resultado (estos últimos plegados y recortados si son muy largos).

Qué se omite u oculta:
- El razonamiento interno del modelo y los avisos del sistema, que no son parte de la conversación.
- Correos electrónicos y el nombre de usuario de Windows en las rutas.
- Los resultados que contenían los comentarios del issue de la tarea (entregas de otros estudiantes).
"""
import json
import re
import sys
from pathlib import Path
USUARIO = Path.home().name

MAX_ENTRADA = 4000
MAX_RESULTADO = 2500
# resultados que no se publican: los comentarios del issue (entregas de otros estudiantes) y la inspección del propio
# registro de la sesión (repite datos internos de la cuenta y del sistema)
OMITIR_SI_LA_ENTRADA_TIENE = ("/comments", "comments.json", "issue.txt", "json.loads(l)")


TERMINOS = []


def ocultar(texto):
    for t in TERMINOS:
        texto = re.sub(re.escape(t), "[oculto]", texto, flags=re.I)
    texto = re.sub(r"[\w.+-]+@[\w-]+\.[\w.-]+", "[correo oculto]", texto)
    texto = re.sub(r'"(organizationUuid|accountUuid)": "[^"]+"', r'"": "[oculto]"', texto)
    texto = re.sub(r"noreply\[correo oculto\]", "noreply@anthropic.com", texto)  # la firma de los commits no es privada
    for ruta in (str(Path.home()), Path.home().as_posix(), f"/c/Users/{USUARIO}"):
        texto = texto.replace(ruta, "~")
    return texto.replace(USUARIO, "usuario")


def limpiar_mensaje(texto):
    texto = re.sub(r"<system-reminder>.*?</system-reminder>", "", texto, flags=re.S)
    texto = re.sub(r"</?pasted_content[^>]*>", "", texto)
    texto = re.sub(r"</?(command-name|command-message|command-args|local-command-stdout)>", " ", texto)
    return texto.strip()


def recortar(texto, n):
    return texto if len(texto) <= n else texto[:n] + f"\n… [recortado: {len(texto) - n:,} caracteres más]"


def texto_de(contenido):
    if isinstance(contenido, str):
        return contenido
    partes = []
    for b in contenido or []:
        if b.get("type") == "text":
            partes.append(b["text"])
        elif b.get("type") == "image":
            partes.append("[imagen]")
    return "\n".join(partes)


def entrada_legible(nombre, entrada):
    if nombre in ("Bash", "PowerShell"):
        return entrada.get("command", ""), "bash" if nombre == "Bash" else "powershell"
    if nombre == "Edit":
        return (f"archivo: {entrada.get('file_path')}\n--- antes ---\n{entrada.get('old_string', '')}\n"
                f"--- después ---\n{entrada.get('new_string', '')}"), "text"
    if nombre == "Write":
        return f"archivo: {entrada.get('file_path')}\n\n{entrada.get('content', '')}", "text"
    return json.dumps(entrada, ensure_ascii=False, indent=2), "json"


def bloque(md):
    return md.replace("```", "ˋˋˋ")  # que un ``` dentro del texto no cierre el bloque de código


def exportar(jsonl, salida, titulo):
    lineas = [json.loads(l) for l in Path(jsonl).read_text(encoding="utf-8").splitlines() if l.strip()]
    pendientes, pendientes_lenguaje, out = {}, {}, []
    inicio = next((d.get("timestamp") for d in lineas if d.get("timestamp")), "")
    fin = next((d.get("timestamp") for d in reversed(lineas) if d.get("timestamp")), "")
    out += [f"# {titulo}", "",
            f"- Sesión de Claude Code `{Path(jsonl).stem}`, del {inicio[:16].replace('T', ' ')} al "
            f"{fin[:16].replace('T', ' ')} (UTC).",
            "- Generado con `evidencias_ia/exportar_conversacion.py` a partir del registro `.jsonl` de la sesión.",
            "- Se ocultaron correos y rutas personales; se omitieron el razonamiento interno del modelo, los avisos del "
            "sistema y los resultados que contenían entregas de otros estudiantes.", "", "---", ""]
    for d in lineas:
        tipo = d.get("type")
        if tipo == "user" and not d.get("isMeta"):
            contenido = d["message"]["content"]
            if isinstance(contenido, list) and any(b.get("type") == "tool_result" for b in contenido):
                for b in contenido:
                    if b.get("type") != "tool_result":
                        continue
                    nombre, entrada, desc = pendientes.pop(b["tool_use_id"], ("herramienta", "", ""))
                    if any(s in entrada for s in OMITIR_SI_LA_ENTRADA_TIENE):
                        resultado = ("[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes "
                                     "o datos internos del registro de la sesión.]")
                    else:
                        resultado = recortar(texto_de(b.get("content")), MAX_RESULTADO)
                    out += [f"<details><summary>🔧 {nombre}{': ' + desc if desc else ''}"
                            f"{' ⚠️ error' if b.get('is_error') else ''}</summary>", "",
                            "```" + (pendientes_lenguaje.pop(b["tool_use_id"], "text")), bloque(entrada), "```", "",
                            "Resultado:", "", "```text", bloque(resultado), "```", "", "</details>", ""]
                continue
            texto = limpiar_mensaje(texto_de(contenido))
            if texto:
                out += ["## 👤 Usuaria", "", texto, ""]
        elif tipo == "attachment":
            a = d.get("attachment", {})
            if a.get("type") == "queued_command" and a.get("origin", {}).get("kind") == "human":
                out += ["## 👤 Usuaria (mensaje enviado mientras Claude trabajaba)", "", limpiar_mensaje(a["prompt"]), ""]
        elif tipo == "assistant":
            for b in d["message"]["content"]:
                if b.get("type") == "text" and b["text"].strip():
                    out += ["## 🤖 Claude", "", b["text"].strip(), ""]
                elif b.get("type") == "tool_use":
                    entrada, lenguaje = entrada_legible(b["name"], b.get("input", {}))
                    pendientes[b["id"]] = (b["name"], recortar(entrada, MAX_ENTRADA), b.get("input", {}).get("description", ""))
                    pendientes_lenguaje[b["id"]] = lenguaje
    Path(salida).parent.mkdir(parents=True, exist_ok=True)
    Path(salida).write_text(ocultar("\n".join(out)), encoding="utf-8")
    return len(out)


if __name__ == "__main__":
    jsonl, salida, titulo = sys.argv[1:4]
    if len(sys.argv) > 4:
        TERMINOS += [t.strip() for t in Path(sys.argv[4]).read_text(encoding="utf-8").splitlines() if t.strip()]
    print(f"{salida}: {exportar(jsonl, salida, titulo)} líneas")
