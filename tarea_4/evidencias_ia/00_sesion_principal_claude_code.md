# Sesión principal de Claude Code: Tarea 4 completa (Partes 1 a 4)

- Sesión de Claude Code `57ecd584-3768-4852-a254-c84910c84d73`, del 2026-11-09 01:45 al 2026-11-09 04:18 (UTC).
- Generado con `evidencias_ia/exportar_conversacion.py` a partir del registro `.jsonl` de la sesión.
- Se ocultaron correos y rutas personales; se omitieron el razonamiento interno del modelo, los avisos del sistema y los resultados que contenían entregas de otros estudiantes.

---

## 👤 Usuaria

Hola Claude. Esta es mi tarea de esta semana. Revisala y luego te doy indicaciones: https://github.com/d2cml-ai/Data-Science-Python/issues/201

<details><summary>🔧 Bash: Read the assignment issue and its comments ⚠️ error</summary>

```bash
gh issue view 201 --repo d2cml-ai/Data-Science-Python --comments
```

Resultado:

```text
Exit code 127
/usr/bin/bash: line 1: gh: command not found
```

</details>

<details><summary>🔧 PowerShell: Read the assignment issue and its comments ⚠️ error</summary>

```powershell
gh issue view 201 --repo d2cml-ai/Data-Science-Python --comments
```

Resultado:

```text
Exit code 1
gh : El término 'gh' no se reconoce como nombre de un cmdlet, función, archivo de script o programa ejecutable. 
Compruebe si escribió correctamente el nombre o, si incluyó una ruta de acceso, compruebe que dicha ruta es correcta e 
inténtelo de nuevo.
En línea: 1 Carácter: 302
+ ... y { $PSStyle.OutputRendering = 'PlainText' } catch {} } }; gh issue v ...
+                                                                ~~
    + CategoryInfo          : ObjectNotFound: (gh:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```

</details>

<details><summary>🔧 Bash: Fetch the issue via the GitHub public API</summary>

```bash
ls "/c/Program Files/GitHub CLI/" 2>/dev/null; curl -s -H "Accept: application/vnd.github+json" https://api.github.com/repos/d2cml-ai/Data-Science-Python/issues/201 | python -c "import sys,json; d=json.load(sys.stdin); print(d.get('title')); print(d.get('state'), d.get('created_at'), d.get('comments')); print(); print(d.get('body'))"
```

Resultado:

```text
<persisted-output>
Output too large (39.7KB). Full output saved to: ~\.claude\projects\C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio\57ecd584-3768-4852-a254-c84910c84d73\tool-results\bwi1ns6w7.txt

Preview (first 2KB):
2026_Tarea_4
open 2026-11-01T17:36:05Z 29

<html>
<body>
<!--StartFragment--><html><head></head><body><h1><span>🤖 Tarea 4 – Agente de investigación socioeconómica: MCP, Skills y datos oficiales del Perú</span></h1><h2><span>Pregunta guía del trabajo</span></h2><blockquote><p><strong><span>¿Pueden construir un agente de inteligencia artificial capaz de investigar la realidad socioeconómica peruana utilizando datos oficiales del INEI y el BCRP, combinando servidores MCP, Skills de Claude Code y herramientas de análisis reproducible?</span></strong></p></blockquote><p><span>En este proyecto desarrollarán un </span><strong><span>agente de investigación socioeconómica</span></strong><span> que integre dos fuentes oficiales de información:</span></p><ol start="1"><li><p><strong><span>INEI – ENAHO 2024:</span></strong><span> microdatos para estudiar pobreza monetaria, desigualdades territoriales y características socioeconómicas de la población.</span></p></li><li><p><strong><span>BCRP – Series estadísticas:</span></strong><span> indicadores macroeconómicos para analizar inflación, actividad económica, tipo de cambio u otras variables relevantes.</span></p></li></ol><p><span>El agente deberá interpretar preguntas formuladas en lenguaje natural, consultar las fuentes correspondientes, procesar los datos, ejecutar cálculos verificables y producir gráficos, mapas e informes.</span></p><p><span>El objetivo principal no es construir un chatbot que responda utilizando únicamente su conocimiento previo, sino </span><strong><span>un sistema que utilice herramientas especializadas para producir respuestas verificables y reproducibles</span></strong><span>.</span></p><div><hr></div><h2><span>📌 Instrucciones generales</span></h2><p><span>El trabajo es </span><strong><span>individual</span></strong><span> y corresponde a la </span><strong><span>Tarea 4 del curso Python Intermedio</span></strong><span>.</span></p><h3><span>1. Materiales de referencia</span></h3><p><span>El proye
...
</persisted-output>
```

</details>

<details><summary>🔧 Bash: Download issue and comments, convert HTML to text</summary>

```bash
cd "~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad" && mkdir -p issue201 && curl -s https://api.github.com/repos/d2cml-ai/Data-Science-Python/issues/201 -o issue201/issue.json && curl -s "https://api.github.com/repos/d2cml-ai/Data-Science-Python/issues/201/comments?per_page=100" -o issue201/comments.json && cat > html2txt.py <<'EOF'
import sys, json, re, html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.pre=False
    def handle_starttag(s,t,a):
        if t in('p','div','br','tr','h1','h2','h3','h4','blockquote','pre'): s.out.append('\n')
        if t in('h1','h2','h3','h4'): s.out.append('#'*int(t[1])+' ')
        if t=='li': s.out.append('\n- ')
        if t in('td','th'): s.out.append(' | ')
        if t=='a':
            d=dict(a); s._href=d.get('href')
        if t=='hr': s.out.append('\n---\n')
    def handle_endtag(s,t):
        if t=='a' and getattr(s,'_href',None): s.out.append(f' <{s._href}>'); s._href=None
    def handle_data(s,d): s.out.append(d)
def conv(b):
    if not b: return ''
    if '<' in b and '>' in b:
        p=P(); p.feed(b); t=''.join(p.out)
    else: t=b
    return re.sub(r'\n\s*\n+','\n\n',t).strip()
d=json.load(open(sys.argv[1],encoding='utf-8'))
print(conv(d['body']))
print('\n\n========== COMMENTS ==========')
for c in json.load(open(sys.argv[2],encoding='utf-8')):
    print(f"\n--- {c['user']['login']} @ {c['created_at']} ---")
    print(conv(c['body']))
EOF
python html2txt.py issue201/issue.json issue201/comments.json > issue201/issue.txt; wc -c issue201/issue.txt; head -c 15000 issue201/issue.txt
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Bash: Convert issue HTML to text with UTF-8 output</summary>

```bash
cd "~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad" && PYTHONIOENCODING=utf-8 python html2txt.py issue201/issue.json issue201/comments.json > issue201/issue.txt; wc -c issue201/issue.txt
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

## 🤖 Claude

Estoy descargando el issue y sus 29 comentarios para leerlos. Sigo.

<details><summary>🔧 Read</summary>

```json
{
  "file_path": "C:\\Users\\usuario\\AppData\\Local\\Temp\\claude\\0e9f16fe359e3b06\\57ecd584-3768-4852-a254-c84910c84d73\\scratchpad\\issue201\\issue.txt"
}
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Bash: List comment authors to spot teacher clarifications</summary>

```bash
cd "~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad" && PYTHONIOENCODING=utf-8 python -c "
import json
for c in json.load(open('issue201/comments.json',encoding='utf-8')):
    b=c['body'] or ''
    print(c['user']['login'], c['author_association'], c['created_at'], len(b), 'TAREA' if 'Tarea 4' in b[:200] else '---', repr(b[:90]))
"; PYTHONIOENCODING=utf-8 python -c "
import json; d=json.load(open('issue201/issue.json',encoding='utf-8')); print(d['user']['login'], d['updated_at'])"
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Bash: Check current time and local repo state</summary>

```bash
date; date -u; echo; git -C "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio" log --oneline -8 --all --graph | head -20; echo; ls -la "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio"; git -C "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio" remote -v; git -C "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio" show --stat HEAD | head -20
```

Resultado:

```text
Sun, Nov  8, 2026  8:46:55 PM
Mon, Nov  9, 2026  1:46:55 AM

* 588da4a Create placeholder.md
*   43fce66 Merge pull request #15 from dgarcesg/P3-Reel
|\  
| * 0640326 README: enlace público del reel en Google Drive
| * 3fc4834 Tarea 3 · Parte 3: reel con voz clonada, imágenes por escena y subtítulos
* | ddd0036 Added Dev Container Folder
|/  
*   7d7cb06 Merge pull request #14 from dgarcesg/p2-dashboard
|\  
| * 028b1cc Dashboard: sin la temporada 2015-16 incompleta ni el contexto de OSITRÁN
| * 7f65ea3 Tarea 3: dashboard en Streamlit con fondo negro
|/  

total 28
drwxr-xr-x 1 usuario 1049089    0 Nov  8 20:37 .
drwxr-xr-x 1 usuario 1049089    0 Nov  4 19:46 ..
drwxr-xr-x 1 usuario 1049089    0 Nov  8 20:36 .devcontainer
drwxr-xr-x 1 usuario 1049089    0 Nov  8 20:44 .git
-rw-r--r-- 1 usuario 1049089 1101 Oct 18 20:04 LICENSE
drwxr-xr-x 1 usuario 1049089    0 Oct 25 19:34 tarea_1
drwxr-xr-x 1 usuario 1049089    0 Oct 26 00:19 tarea_2
drwxr-xr-x 1 usuario 1049089    0 Nov  1 23:48 tarea_3
drwxr-xr-x 1 usuario 1049089    0 Nov  8 20:37 tarea_4
origin	https://github.com/dgarcesg/diplomado_python_intermedio.git (fetch)
origin	https://github.com/dgarcesg/diplomado_python_intermedio.git (push)
commit 588da4a43c02839e0bc050d50830bd39717336ed
Author: Adriana Garcés García <[correo oculto]>
Date:   Sun Nov 8 20:35:55 2026 -0500

    Create placeholder.md

 tarea_4/placeholder.md | 1 +
 1 file changed, 1 insertion(+)
```

</details>

<details><summary>🔧 Bash: Inspect tarea_4 folder, memory notes and local tooling</summary>

```bash
ls -la "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4"; cat "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4/placeholder.md"; echo; cat "~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/memory/ds-python-up-kernel.md"; ls "~/GITHUB/"; ls "~/GITHUB/Diplomatura PUCP 2026/"; which uv; uv --version
```

Resultado:

```text
total 5
drwxr-xr-x 1 usuario 1049089 0 Nov  8 20:37 .
drwxr-xr-x 1 usuario 1049089 0 Nov  8 20:37 ..
-rw-r--r-- 1 usuario 1049089 2 Nov  8 20:37 placeholder.md


---
name: ds-python-up-kernel
description: "Where the user's ds-python-up environment lives and how it is registered as a Jupyter kernel"
metadata:
  node_type: memory
  type: reference
  originSessionId: e2663f81-fd11-426e-af9e-1aa5eee59f80
  modified: 2026-10-19T01:38:07.078Z
---

`ds-python-up` is a uv virtualenv (Python 3.12), not a conda env. It lives in the sibling repo at `~\GITHUB\Diplomatura PUCP 2026\Data-Science-Python\.venv`.

Registered on 2026-10-18 as a user-level Jupyter kernel named `ds-python-up` (display name "Python (ds-python-up)") in `%APPDATA%\jupyter\kernels\ds-python-up`. If `.venv` is moved or deleted, remove it with `jupyter kernelspec uninstall ds-python-up`.
Diplomatura PUCP 2026
Data-Science-Python
Diplomado_PUCP
diplomado_python_intermedio
DiplomadoPUCP2026_FundamentosPython
Group04_Assingment1
infraestructura-vial-afectada-ninos-costeros
MCP-BCRP
profile
Prueba1_DiplomadoPUCP2026
Python---Grupo-4
Tarea Raster
~/AppData/Local/anaconda3/Scripts/uv
uv 0.13.1 (62faed335 2026-10-13 x86_64-pc-windows-msvc)
```

</details>

<details><summary>🔧 Bash: Check local course repo and MCP-BCRP folder contents</summary>

```bash
B="~/GITHUB/Diplomatura PUCP 2026"; ls "$B/MCP-BCRP"; git -C "$B/MCP-BCRP" log --oneline -5 2>/dev/null; echo ---; ls "$B/Data-Science-Python/sessions" 2>/dev/null | head -40; git -C "$B/Data-Science-Python" log --oneline -3; echo ---; ls -R "$B/Data-Science-Python/sessions/04-mcp-claude-code/proyecto" 2>/dev/null | head -40; echo ---; ls -R "$B/Data-Science-Python/sessions/16-skills-enaho" 2>/dev/null | grep -v "^$" | head -60
```

Resultado:

```text
MCP-BCRP
---
01-datos-git-agentes
02-fundamentos-python
03-scraping-apis
04-mcp-claude-code
05-visualizacion-dashboards
06-geoespacial
07-raster
08-llms-rag
09-huggingface-finetuning
10-document-ai-voz
11-agentes
12-despliegue-evaluacion
13-audio-a-texto
15-texto-a-reel
16-skills-enaho
42960838 Sesión 16: skills de Claude Code para limpiar, graficar y mapear la ENAHO
d13359d8 Sesión 04: MCP en Claude Code, con el proyecto de un MCP del BCRP
bcec07e0 Sesión 15: notebook de la clase, del texto al reel con tu voz
---
~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/04-mcp-claude-code/proyecto:
evaluar.py
preguntas.csv
pyproject.toml
README.md
server.py
test_server.py
uv.lock
---
~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/16-skills-enaho:
README.md
referencias
~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/16-skills-enaho/referencias:
mapa_pobreza_2024.png
pobreza_departamento_2024.csv
```

</details>

<details><summary>🔧 Bash: Size up session 04 server, tests and session 16 guide</summary>

```bash
P="~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions"; wc -l "$P/04-mcp-claude-code/proyecto/"*.py "$P/04-mcp-claude-code/proyecto/README.md" "$P/16-skills-enaho/README.md"; grep -n "def \|@mcp\|TODO" "$P/04-mcp-claude-code/proyecto/server.py" | head -40; echo ---; grep -n "^def test" "$P/04-mcp-claude-code/proyecto/test_server.py"; echo ---; grep -n "^#" "$P/16-skills-enaho/README.md" | head -40; echo ---; find "~/GITHUB/Diplomatura PUCP 2026" -iname "*enaho*" -o -iname "*modulo34*" -o -iname "*sumaria*" 2>/dev/null | grep -v node_modules | head
```

Resultado:

```text
Command was moved to the background (ID: bki67n88d) so that a message that arrived while it was running can reach you; it was not interrupted. Output is being written to: ~\AppData\Local\Temp\claude\0e9f16fe359e3b06\57ecd584-3768-4852-a254-c84910c84d73\tasks\bki67n88d.output. You will be notified when it completes. It is running now: do not start a second copy while it runs. If it is no longer needed, stop it with TaskStop. To check interim output, use Read on that file path.
```

</details>

## 👤 Usuaria (mensaje enviado mientras Claude trabajaba)

no descargues los comentarios

## 🤖 Claude

Entendido: ya los había bajado a una carpeta temporal antes de tu mensaje. Los borro ahora y no los uso.

<details><summary>🔧 Bash: Delete the downloaded comments from the scratchpad</summary>

```bash
cd "~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad/issue201" && rm -f comments.json issue.txt && ls
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Read</summary>

```json
{
  "file_path": "C:\\Users\\usuario\\AppData\\Local\\Temp\\claude\\0e9f16fe359e3b06\\57ecd584-3768-4852-a254-c84910c84d73\\tasks\\bki67n88d.output"
}
```

Resultado:

```text
1	   75 ~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/04-mcp-claude-code/proyecto/evaluar.py
2	  107 ~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/04-mcp-claude-code/proyecto/server.py
3	   71 ~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/04-mcp-claude-code/proyecto/test_server.py
4	  146 ~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/04-mcp-claude-code/proyecto/README.md
5	  217 ~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/16-skills-enaho/README.md
6	  616 total
7	1:"""Servidor MCP del BCRP. Empiecen aquí: buscar_series ya funciona; completen los TODO hasta que pasen las pruebas.
8	31:def _sin_tildes(s):
9	36:def catalogo():
10	51:def _ficha(codigo):
11	60:@mcp.tool(annotations=SOLO_LECTURA)
12	61:def buscar_series(texto: str, frecuencia: str | None = None, limite: int = 10) -> list[dict]:
13	81:# TODO 1 · serie(codigo, desde, hasta) -> {"codigo", "nombre", "frecuencia", "datos": [{"periodo", "valor"}], "fuente"}
14	92:# TODO 2 · resumen(codigo, desde, hasta): primero, ultimo, cambio, variacion_pct, promedio, maximo y minimo
15	95:# TODO 3 · Una herramienta suya, bien descrita. Ideas:
16	101:# TODO 4 · Un recurso, por ejemplo la plantilla bcrp://serie/{codigo} con la ficha de la serie.
17	103:# TODO 5 · Un prompt, por ejemplo informe(tema) que pida citar el código y el periodo de cada cifra.
18	---
19	25:def test_buscar_encuentra_el_ipc():
20	31:def test_cuatro_herramientas_como_minimo():
21	37:def test_serie_mensual():
22	45:def test_serie_diaria():
23	51:def test_resumen_sin_cuentas_a_mano():
24	59:def test_codigo_inexistente_da_un_error_claro():
25	64:def test_un_recurso():
26	70:def test_un_prompt():
27	---
28	1:# Sesión 16 · Skills de Claude Code: limpiar, graficar y mapear la ENAHO
29	15:## Contenido
30	22:## Lo esencial de una skill
31	38:### Por qué crearla en Claude Code
32	48:## Los datos
33	59:## El proyecto
34	72:### 1. Preparar (0–8 min)
35	82:### 2. Limpiar (8–20 min)
36	107:# Limpiar la ENAHO
37	115:### 3. Graficar y mapear (20–32 min)
38	126:### 4. Evaluar y subir (32–45 min)
39	145:## Validación
40	160:## Entrega
41	182:## Para explorar
42	203:## Si se atascan
43	213:## Fuentes
44	---
45	~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/05-visualizacion-dashboards/lecture/enaho2019
46	~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/06-geoespacia
… [recortado: 146 caracteres más]
```

</details>

<details><summary>🔧 Write</summary>

```text
archivo: ~\.claude\projects\C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio\memory\no-descargar-comentarios-issue.md

---
name: no-descargar-comentarios-issue
description: Al revisar el issue de una tarea del curso, leer solo el enunciado; no bajar los comentarios (entregas de compañeros)
metadata:
  type: feedback
---

Al revisar el issue de una tarea en d2cml-ai/Data-Science-Python, leer solo el cuerpo del issue (el enunciado). No descargar ni leer los comentarios: son las entregas de otros estudiantes.

**Why:** La usuaria lo pidió expresamente el 8-nov-2026 (Tarea 4, issue #201). No dio el motivo; lo más probable es que no quiera ver ni tomar trabajo de sus compañeros.
**How to apply:** Pedir a la API solo `/issues/{n}` y nunca `/issues/{n}/comments`, y no usar `--comments` con `gh`.

```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Bash: Add the new memory to the memory index</summary>

```bash
echo "- [No descargar comentarios del issue](no-descargar-comentarios-issue.md) — leer solo el enunciado; los comentarios son entregas de compañeros" >> "~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/memory/MEMORY.md"
```

Resultado:

```text
(Bash completed with no output)
```

</details>

## 🤖 Claude

Revisé el enunciado de la Tarea 4. Sobre tu mensaje: los comentarios ya se habían bajado antes de que llegara. Solo vi los nombres de los autores y las primeras líneas de algunas entregas. Los borré, no los uso, y anoté no volver a bajarlos.

## ⚠️ Lo urgente: el plazo
- **La entrega cierra hoy, domingo 8 de noviembre, a las 11:59 p. m. (hora de Perú).** Son las 8:47 p. m., así que quedan unas **3 horas**.
- Para entregar hay que publicar un comentario en el issue con el formato que pide el enunciado.
- Una entrega tardía solo se acepta con justificación aprobada por los profesores, y cada día de retraso resta 2 puntos.
- `tarea_4/` solo tiene `placeholder.md` por ahora. Estás en la rama `parte-1-mcp-bcrp`.

## Qué pide (20 pts)
| Parte | Pts | Lo esencial |
|---|:-:|---|
| **1. MCP del BCRP** | 5 | `mcp/server.py` con `buscar_series`, `serie`, `resumen` y una herramienta propia. Además, un recurso, un prompt y el `.mcp.json`. Deben pasar las **10 pruebas**: las 8 originales sin cambios más 2 tuyas. |
| **2. Tres Skills ENAHO** | 6 | `limpiando-enaho` lee los módulos 34 y 02, filtra residentes habituales, une con `validate="m:1"`, pondera y escribe `salidas/validacion.txt`. Debe dar ~27.6 % ±0.1 pp, 108,664 residentes y 25 departamentos. `graficando-enaho` hace 3 gráficos y `mapeando-enaho` el mapa, unido por `ubigeo[:2]` ↔ `FIRST_IDDP`. Gráficos y mapa deben correr la limpieza primero si falta la base. |
| **3. Agente integrado** | 5 | Una pregunta propia con datos del BCRP y de ENAHO. Una sola ejecución que use **≥2 herramientas MCP y ≥2 Skills**. `informes/informe_final.md` con 3 hallazgos, un gráfico del BCRP, uno de ENAHO y el mapa. Hay que verificar a mano 3 cifras. |
| **4. Evaluación y documentación** | 4 | 10 preguntas (4 BCRP, 4 ENAHO, 2 mixtas), cada una respondida **en dos modos y en sesiones separadas**. Resultados en `resultados.csv` y `comparacion.md`, un README de 12 puntos y `evidencias_ia/` con las conversaciones completas. |

## Lo que ya tienes a mano
- **Sesión 04**, en tu copia local del repo del curso: `server.py` (107 líneas) ya trae `buscar_series` funcionando y 5 TODO marcados, que cubren casi toda la Parte 1. `test_server.py` tiene las 8 pruebas y también hay un `evaluar.py` que puede servir para la Parte 4.
- **Sesión 16**: el README con el método y `referencias/pobreza_departamento_2024.csv` y `mapa_pobreza_2024.png` para comparar.
- **Falta:** los módulos 34 y 02 de ENAHO 2024 no están en tu disco. Hay que bajarlos del INEI.

## Lo que más tiempo consume
1. **La Parte 4:** son 20 respuestas en sesiones independientes, cada una con su tiempo medido.
2. **`evidencias_ia/`:** pide las conversaciones completas. Claude Code ya las guarda como `.jsonl` en tu carpeta `.claude/projects/`, así que se pueden exportar y quitarles los datos sensibles. Esta sesión también cuenta.

Con el tiempo que queda, propongo avanzar en el orden de la tabla. Las Partes 1 y 2 valen 11 de los 20 puntos y son las que más se apoyan en material que ya existe. No haré commit ni push hasta que me lo pidas.

¿Qué quieres que hagamos?

## 👤 Usuaria

Vamos con la parte 1 en este branch. Yo ya contaba con un MCP para el BCRP (https://github.com/dgarcesg/MCP-BCRP). tambien hay una copia local. Puedes revisarla y decirme que recursos y prompts tenia?

<details><summary>🔧 Bash: List files in the local MCP-BCRP copy</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/MCP-BCRP" && find . -path ./MCP-BCRP/.git -prune -o -path '*/.venv' -prune -o -path '*/__pycache__' -prune -o -type f -print | head -60; git -C MCP-BCRP log --oneline -5 2>/dev/null; git -C MCP-BCRP remote -v 2>/dev/null
```

Resultado:

```text
./MCP-BCRP/.claude/settings.local.json
./MCP-BCRP/.gitattributes
./MCP-BCRP/.gitignore
./MCP-BCRP/.mcp.json
./MCP-BCRP/.pytest_cache/.gitignore
./MCP-BCRP/.pytest_cache/CACHEDIR.TAG
./MCP-BCRP/.pytest_cache/README.md
./MCP-BCRP/.pytest_cache/v/cache/lastfailed
./MCP-BCRP/.pytest_cache/v/cache/nodeids
./MCP-BCRP/datos/catalogo_bcrp.csv
./MCP-BCRP/evaluar.py
./MCP-BCRP/grafico.png
./MCP-BCRP/grafico.py
./MCP-BCRP/informe.md
./MCP-BCRP/preguntas.csv
./MCP-BCRP/pyproject.toml
./MCP-BCRP/README.md
./MCP-BCRP/resultados.csv
./MCP-BCRP/server.py
./MCP-BCRP/test_server.py
./MCP-BCRP/uv.lock
aa1a37e Paso 4: informe, gráfico y README del proyecto
d3f4df8 Paso 3: dos preguntas propias y evaluación (mcp 10 de 10, memoria 0 de 10)
802104e Paso 2: conectar bcrp y fetch en .mcp.json; recurso series destacadas
d8426e8 Paso 1 completo: resumen, comparar_paises, recurso y prompt (8 de 8)
fbf7a17 Paso 0 y TODO 1: plantilla del proyecto y herramienta serie
origin	https://github.com/dgarcesg/MCP-BCRP.git (fetch)
origin	https://github.com/dgarcesg/MCP-BCRP.git (push)
Shell cwd was reset to ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio
```

</details>

<details><summary>🔧 Read</summary>

```json
{
  "file_path": "C:\\Users\\usuario\\GITHUB\\Diplomatura PUCP 2026\\MCP-BCRP\\MCP-BCRP\\server.py"
}
```

Resultado:

```text
1	"""Servidor MCP del BCRP: busca entre las series oficiales del Banco Central de Reserva del Perú, descarga sus datos y
2	hace las cuentas (variaciones, promedios, extremos). También compara al Perú con otros países con el Banco Mundial.
3	
4	    uv run pytest                                           # el contrato: las 8 pruebas pasan
5	    uv run server.py                                        # el servidor, por stdio
6	    claude mcp add --scope project bcrp -- uv run server.py # conectarlo a Claude Code (ya está en .mcp.json)
7	
8	Las cuentas las hace Python, no el modelo: así cada cifra sale de una llamada que se puede repetir.
9	"""
10	import json
11	import re
12	import time
13	import unicodedata
14	from datetime import date
15	from functools import cache
16	from pathlib import Path
17	
18	import httpx
19	import pandas as pd
20	from fastmcp import FastMCP
21	from fastmcp.exceptions import ToolError
22	
23	AQUI = Path(__file__).parent
24	CATALOGO = AQUI / "datos" / "catalogo_bcrp.csv"
25	URL_CATALOGO = "https://estadisticas.bcrp.gob.pe/estadisticas/series/metadata"
26	API = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api"
27	SOLO_LECTURA = {"readOnlyHint": True, "openWorldHint": True}
28	
29	mcp = FastMCP("bcrp", instructions=(
30	    "Series oficiales del Banco Central de Reserva del Perú (BCRP). Primero busca el código con buscar_series; "
31	    "luego usa resumen para variaciones, promedios y extremos, y serie para los datos. No calcules a mano: "
32	    "cita siempre el código de la serie y el periodo."))
33	
34	
35	def _sin_tildes(s):
36	    return unicodedata.normalize("NFD", str(s).lower()).encode("ascii", "ignore").decode()
37	
38	
39	@cache
40	def catalogo():
41	    """El catálogo oficial: 17 mil series en unos 7 MB. Se baja una vez y queda en datos/."""
42	    if not CATALOGO.exists():
43	        CATALOGO.parent.mkdir(exist_ok=True)
44	        r = httpx.get(URL_CATALOGO, timeout=120)
45	        r.raise_for_status()
46	        CATALOGO.write_text(r.content.decode("latin-1"), encoding="utf-8")
47	    df = pd.read_csv(CATALOGO, sep=";", dtype=str).fillna("")
48	    df = df.rename(columns={"Código de serie": "codigo", "Categoría de serie": "categoria", "Grupo de serie": "grupo",
49	                            "Nombre de serie": "nombre", "Frecuencia": "frecuencia",
50	                            "Fecha de actualización": "actualizada", "Fecha de inicio": "inicio"})
51	    df["texto"] = (df.categoria + " " + df.grupo + " " + df.nombr
… [recortado: 12,166 caracteres más]
```

</details>

<details><summary>🔧 Bash: Check git sync, MCP config and test file vs course original</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/MCP-BCRP/MCP-BCRP" && git status --short; git fetch -q origin 2>&1; git status -sb | head -2; echo "--- .mcp.json"; cat .mcp.json; echo "--- pyproject"; cat pyproject.toml; echo "--- diff test_server vs curso"; diff test_server.py "~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/04-mcp-claude-code/proyecto/test_server.py" && echo "IDENTICOS"
```

Resultado:

```text
## main...origin/main
--- .mcp.json
{
  "mcpServers": {
    "bcrp": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "server.py"
      ],
      "env": {}
    },
    "fetch": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-server-fetch"
      ],
      "env": {}
    }
  }
}--- pyproject
[project]
name = "mcp-bcrp"
version = "0.1.0"
description = "Servidor MCP con las series oficiales del BCRP"
requires-python = ">=3.11"
dependencies = [
    "fastmcp>=4,<5",
    "httpx",
    "matplotlib>=3.11.2",
    "pandas",
]

[dependency-groups]
dev = ["pytest"]
--- diff test_server vs curso
IDENTICOS
Shell cwd was reset to ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio
```

</details>

## 🤖 Claude

Revisé la copia local (`MCP-BCRP/MCP-BCRP/`). Coincide con `origin/main` y no tiene cambios sin guardar.

## Recursos (2)
| URI | Función | Qué devuelve |
|---|---|---|
| `bcrp://serie/{codigo}` | `ficha_serie` | La ficha de una serie: código, nombre, categoría, frecuencia, fecha de inicio y última actualización. Es una plantilla y se adjunta así: `@bcrp:bcrp://serie/PN01273PM`. |
| `bcrp://series/destacadas` | `series_destacadas` | Las fichas de 7 series: inflación a 12 meses y mensual, tipo de cambio venta, tasa de referencia, reservas internacionales netas, precio del cobre y crecimiento del PBI. Es el recurso fijo que aparece en el menú `@` de Claude Code. |

## Prompts (1)
| Prompt | Uso | Qué pide |
|---|---|---|
| `informe(tema)` | `/mcp__bcrp__informe inflación` | Un informe breve con los últimos 12 meses. Indica buscar con `buscar_series`, calcular con `resumen` o `serie` sin hacer cuentas a mano, usar `comparar_paises` si ayuda, citar cada cifra con código y periodo, y cerrar con las URL de las fuentes y lo que no encontró. |

## Comparación con lo que pide la Parte 1
- ✅ **Herramientas:** tiene las 4 que pide la tarea: `buscar_series`, `serie`, `resumen` y la propia, `comparar_paises`, que compara al Perú con otros países usando la API del Banco Mundial.
- ✅ **Recurso y prompt:** cumple, con 2 recursos y 1 prompt.
- ✅ **Pruebas originales:** `test_server.py` es idéntico al de la Sesión 04, así que las 8 originales están intactas.
- ❌ **Faltan las 2 pruebas propias** de `comparar_paises`.
- ⚠️ **`.mcp.json`:** ejecuta `uv run server.py`. En `tarea_4/` el servidor queda en `mcp/server.py`, así que hay que cambiar la ruta.
- ⚠️ **Servidor `fetch`:** el `.mcp.json` también conecta este servidor de lectura web. Para la Parte 4, en el modo sin herramientas, conviene quitarlo o al menos documentarlo.

Lo siguiente sería copiar `server.py`, `test_server.py` y `pyproject.toml` a `tarea_4/`, ajustar las rutas, agregar las 2 pruebas y confirmar los **10 passed**. ¿Lo hago?

## 👤 Usuaria

si, pero quiero cambiar los recursos. copia todo menos eso y luego te digo cuales haremos

<details><summary>🔧 Bash: Read test file, ignore rules and catalog tracking status</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/MCP-BCRP/MCP-BCRP" && cat test_server.py; echo "--- gitignore"; cat .gitignore; echo "--- tracked?"; git ls-files datos/ uv.lock; ls -la datos/; echo "--- root gitignore"; cat "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/.gitignore" 2>/dev/null || echo "(no hay .gitignore en la raíz)"
```

Resultado:

```text
"""El contrato del servidor: si estas pruebas pasan, Claude Code y evaluar.py pueden usarlo.

    uv run pytest -q

Llaman al servidor en memoria, igual que lo haría Claude Code, y piden datos reales al BCRP.
"""
import asyncio

import pytest
from fastmcp import Client
from fastmcp.exceptions import ToolError

from server import mcp


async def _con_cliente(f):
    async with Client(mcp) as c:
        return await f(c)


def llamar(herramienta, **args):
    return asyncio.run(_con_cliente(lambda c: c.call_tool(herramienta, args))).data


def test_buscar_encuentra_el_ipc():
    r = llamar("buscar_series", texto="ipc 12 meses", limite=5)
    assert "PN01273PM" in [x["codigo"] for x in r]
    assert {"codigo", "nombre", "frecuencia"} <= r[0].keys()


def test_cuatro_herramientas_como_minimo():
    nombres = {t.name for t in asyncio.run(_con_cliente(lambda c: c.list_tools()))}
    assert {"buscar_series", "serie", "resumen"} <= nombres
    assert len(nombres) >= 4, "falta su herramienta propia"


def test_serie_mensual():
    r = llamar("serie", codigo="PN01271PM", desde="2025-01", hasta="2025-12")
    assert len(r["datos"]) == 12
    assert r["datos"][0]["periodo"] == "2025-01"
    assert r["datos"][2]["valor"] == pytest.approx(0.81, abs=0.01)   # IPC de Lima, marzo de 2025
    assert r["fuente"].startswith("https://estadisticas.bcrp.gob.pe")


def test_serie_diaria():
    r = llamar("serie", codigo="PD04638PD", desde="2026-10-01", hasta="2026-10-15")
    assert r["datos"][0]["periodo"] == "2026-10-01"
    assert r["datos"][-1] == {"periodo": "2026-10-15", "valor": pytest.approx(3.428, abs=0.001)}


def test_resumen_sin_cuentas_a_mano():
    r = llamar("resumen", codigo="PN01273PM", desde="2025-12", hasta="2026-09")
    assert r["primero"]["valor"] == pytest.approx(1.51, abs=0.01)
    assert r["ultimo"]["valor"] == pytest.approx(4.55, abs=0.01)
    assert r["maximo"]["periodo"] == "2026-09"
    assert {"cambio", "variacion_pct", "promedio", "minimo"} <= r.keys()


def test_codigo_inexistente_da_un_error_claro():
    with pytest.raises(ToolError, match="XX999"):
        llamar("serie", codigo="XX999", desde="2025-01", hasta="2025-02")


def test_un_recurso():
    async def contar(c):
        return len(await c.list_resources()) + len(await c.list_resource_templates())
    assert asyncio.run(_con_cliente(contar)) >= 1


def test_un_prompt():
    assert len(asyncio.run(_con_cliente(lambda c: c
… [recortado: 446 caracteres más]
```

</details>

<details><summary>🔧 Bash: Fetch World Bank values to set expected test results</summary>

```bash
curl -s "https://api.worldbank.org/v2/country/PER;CHL/indicator/NY.GDP.MKTP.KD.ZG?format=json&date=2019:2021&per_page=1000" | python -c "
import sys,json; r=json.load(sys.stdin); print(r[0]); [print(f['country']['value'], f['date'], f['value']) for f in r[1]]"; echo ---; curl -s "https://api.worldbank.org/v2/country/PER/indicator/XX.NO.EXISTE?format=json&date=2019:2021" | head -c 400
```

Resultado:

```text
{'page': 1, 'pages': 1, 'per_page': 1000, 'total': 6, 'sourceid': '2', 'lastupdated': '2026-10-08'}
Chile 2021 11.3374032409913
Chile 2020 -6.1396969411886
Chile 2019 0.644223402631923
Peru 2021 13.4166456126513
Peru 2020 -10.9333065010382
Peru 2019 2.24063176875049
---
[{"message":[{"id":"120","key":"Invalid value","value":"The provided parameter value is not valid"}]}]
```

</details>

## 🤖 Claude

Copio todo excepto los dos recursos. `test_un_recurso` va a fallar hasta que definamos los nuevos.

<details><summary>🔧 Bash: Copy server, tests, catalog cache and lockfile into tarea_4</summary>

```bash
SRC="~/GITHUB/Diplomatura PUCP 2026/MCP-BCRP/MCP-BCRP"; DST="~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4"; mkdir -p "$DST/mcp/datos" && cp "$SRC/server.py" "$SRC/test_server.py" "$DST/mcp/" && cp "$SRC/datos/catalogo_bcrp.csv" "$DST/mcp/datos/" && cp "$SRC/uv.lock" "$DST/" && ls -R "$DST"
```

Resultado:

```text
~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4:
mcp
placeholder.md
uv.lock

~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4/mcp:
datos
server.py
test_server.py

~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4/mcp/datos:
catalogo_bcrp.csv
```

</details>

## 🤖 Claude

Ahora quito los recursos de `server.py`, ajusto las rutas y agrego las 2 pruebas propias.

<details><summary>🔧 Edit</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py
--- antes ---
    uv run pytest                                           # el contrato: las 8 pruebas pasan
    uv run server.py                                        # el servidor, por stdio
    claude mcp add --scope project bcrp -- uv run server.py # conectarlo a Claude Code (ya está en .mcp.json)

Las cuentas las hace Python, no el modelo: así cada cifra sale de una llamada que se puede repetir.
"""
import json
import re
--- después ---
Desde tarea_4/:

    uv run pytest                                               # el contrato: 8 pruebas del curso + 2 propias
    uv run mcp/server.py                                        # el servidor, por stdio
    claude mcp add --scope project bcrp -- uv run mcp/server.py # conectarlo a Claude Code (ya está en .mcp.json)

Las cuentas las hace Python, no el modelo: así cada cifra sale de una llamada que se puede repetir.
"""
import re
```

Resultado:

```text
The file ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py has been updated successfully.
```

</details>

<details><summary>🔧 Edit</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py
--- antes ---
# TODO 4 · Recurso: la ficha de una serie. En Claude Code se adjunta con @bcrp:bcrp://serie/PN01273PM
@mcp.resource("bcrp://serie/{codigo}", mime_type="application/json")
def ficha_serie(codigo: str) -> str:
    """La ficha de una serie del BCRP: nombre, categoría, frecuencia, desde cuándo hay datos y última actualización."""
    return json.dumps(_ficha(codigo), ensure_ascii=False, indent=2)


# Un recurso fijo, sin {codigo}: es el que aparece en el menú de @ de Claude Code (las plantillas no aparecen).
DESTACADAS = {  # el indicador y el código de su serie, que Claude necesita para pedir los datos
    "Inflación a 12 meses (Lima)": "PN01273PM",
    "Inflación mensual (Lima)": "PN01271PM",
    "Tipo de cambio interbancario, venta (diario)": "PD04638PD",
    "Tasa de referencia del BCRP": "PD04722MM",
    "Reservas internacionales netas": "PN00027MM",
    "Precio del cobre": "PN38784BM",
    "Crecimiento del PBI (anual)": "PM04923AA",
}


@mcp.resource("bcrp://series/destacadas", mime_type="application/json")
def series_destacadas() -> str:
    """Las fichas de las series del BCRP más consultadas: inflación a 12 meses y mensual, tipo de cambio,
    tasa de referencia, reservas internacionales netas, precio del cobre y crecimiento del PBI."""
    fichas = {indicador: _ficha(codigo) for indicador, codigo in DESTACADAS.items()}
    return json.dumps(fichas, ensure_ascii=False, indent=2)


# TODO 5
--- después ---
# TODO 4 · Recursos: por definir.


# TODO 5
```

Resultado:

```text
The file ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py has been updated successfully.
```

</details>

<details><summary>🔧 Bash: Add own tests, config files, sync env and run tests</summary>

```bash
cat >> "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4/mcp/test_server.py" <<'EOF'


# ---------------------------------------------------------------------------------------------------------------------
# Pruebas propias: comparar_paises, la herramienta propia (Banco Mundial). Las 8 de arriba son las del curso, sin cambios.
# Valor de referencia consultado el 8-nov-2026 en api.worldbank.org: PBI real del Perú en 2020, -10.93 %.
# ---------------------------------------------------------------------------------------------------------------------

def test_comparar_paises_trae_cada_pais_y_su_promedio():
    r = llamar("comparar_paises", paises="PER;CHL", indicador="NY.GDP.MKTP.KD.ZG", desde=2019, hasta=2021)
    assert set(r["paises"]) == {"Peru", "Chile"}
    peru = r["paises"]["Peru"]
    assert [d["anio"] for d in peru["datos"]] == [2019, 2020, 2021]      # del año más antiguo al más reciente
    assert peru["datos"][1]["valor"] == pytest.approx(-10.93, abs=0.05)  # la caída del PBI del Perú en 2020
    assert peru["promedio"] == pytest.approx(sum(d["valor"] for d in peru["datos"]) / 3, abs=1e-3)
    assert r["fuente"].startswith("https://api.worldbank.org")


def test_comparar_paises_indicador_inexistente_da_un_error_claro():
    with pytest.raises(ToolError, match="XX.NO.EXISTE"):
        llamar("comparar_paises", paises="PER", indicador="XX.NO.EXISTE", desde=2019, hasta=2021)
EOF
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && cat > pyproject.toml <<'EOF'
[project]
name = "tarea-4-agente-socioeconomico"
version = "0.1.0"
description = "Tarea 4: agente de investigación socioeconómica con un MCP del BCRP y Skills de la ENAHO 2024"
requires-python = ">=3.11"
dependencies = [
    "fastmcp>=4,<5",
    "httpx",
    "matplotlib>=3.11.2",
    "pandas",
]

[dependency-groups]
dev = ["pytest"]

[tool.pytest.ini_options]
testpaths = ["mcp"]
EOF
cat > .mcp.json <<'EOF'
{
  "mcpServers": {
    "bcrp": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "mcp/server.py"
      ],
      "env": {}
    },
    "fetch": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-server-fetch"
      ],
      "env": {}
    }
  }
}
EOF
cat > .gitignore <<'EOF'
# Entorno
.venv/
__pycache__/
.pytest_cache/

# Datos que se descargan: microdatos de la ENAHO (datos/) y catálogo del BCRP (mcp/datos/)
datos/

# Configuración local de Claude Code
.claude/settings.local.json
EOF
uv sync 2>&1 | tail -3 && uv run pytest -q 2>&1 | tail -15
```

Resultado:

```text
 + uvicorn==0.54.0
 + watchfiles==1.3.0
 + websockets==17.3
_______________________________ test_un_recurso _______________________________

    def test_un_recurso():
        async def contar(c):
            return len(await c.list_resources()) + len(await c.list_resource_templates())
>       assert asyncio.run(_con_cliente(contar)) >= 1
E       assert 0 >= 1
E        +  where 0 = <function run at 0x0000018453BA75E0>(<coroutine object _con_cliente at 0x00000184750C2940>)
E        +    where <function run at 0x0000018453BA75E0> = asyncio.run
E        +    and   <coroutine object _con_cliente at 0x00000184750C2940> = _con_cliente(<function test_un_recurso.<locals>.contar at 0x0000018474C17950>)

mcp\test_server.py:67: AssertionError
=========================== short test summary info ===========================
FAILED mcp/test_server.py::test_un_recurso - assert 0 >= 1
1 failed, 9 passed in 34.59s
```

</details>

<details><summary>🔧 Bash: Confirm original tests unchanged and list new files</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && head -n 71 mcp/test_server.py | diff - "~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/04-mcp-claude-code/proyecto/test_server.py" && echo "Las 8 pruebas originales siguen idénticas"; git -C .. status --short
```

Resultado:

```text
Las 8 pruebas originales siguen idénticas
?? tarea_4/.gitignore
?? tarea_4/.mcp.json
?? tarea_4/mcp/
?? tarea_4/pyproject.toml
?? tarea_4/uv.lock
```

</details>

## 🤖 Claude

Ya está copiado todo menos los recursos. Las pruebas dan **9 passed, 1 failed**. La única que falla es `test_un_recurso`, que es lo esperado porque por ahora el servidor no tiene ningún recurso.

**Lo que hay en `tarea_4/`:**
- **`mcp/server.py`:** las 4 herramientas y el prompt `informe(tema)`, sin cambios. Quité los dos recursos y dejé `# TODO 4 · Recursos: por definir.` donde van los nuevos. También actualicé el docstring con las rutas nuevas.
- **`mcp/test_server.py`:** las 8 pruebas originales siguen idénticas a las del curso; lo comprobé con `diff`. Al final agregué 2 pruebas propias de `comparar_paises`, y las dos pasan:
  - Perú y Chile, 2019–2021: revisa que estén ambos países, los años en orden, el promedio, la fuente, y que el Perú cayera −10.93 % en 2020. Ese valor lo consulté hoy en la API del Banco Mundial.
  - Un indicador que no existe devuelve un error claro.
- **`.mcp.json`:** ahora ejecuta `uv run mcp/server.py`. Dejé el servidor `fetch` porque pediste copiar todo; para la Parte 4 habrá que quitarlo o documentarlo.
- **`pyproject.toml`:** son las mismas dependencias de antes con otro nombre de proyecto. También agregué `testpaths = ["mcp"]` y reutilicé el `uv.lock` para que las versiones no cambien.
- **`mcp/datos/catalogo_bcrp.csv`:** la copia local del catálogo, para no volver a bajarlo. Está en `.gitignore` junto con `datos/`, donde irán los microdatos de la ENAHO.

Para usar el MCP desde Claude Code, la sesión tiene que abrirse en `tarea_4/`, porque es ahí donde está el `.mcp.json`. Todavía no hice commit y `placeholder.md` sigue en la carpeta.

¿Qué recursos hacemos?

## 👤 Usuaria

cuales sugieres, en función de la tarea?

<details><summary>🔧 Bash: Inspect BCRP catalog columns and regional series coverage</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && date && PYTHONIOENCODING=utf-8 uv run python -c "
import pandas as pd
df=pd.read_csv('mcp/datos/catalogo_bcrp.csv',sep=';',dtype=str).fillna('')
print(df.columns.tolist()); print(len(df))
print(df.iloc[0].to_dict())
print(df['Categoría de serie'].value_counts().head(25).to_string())
t=(df['Categoría de serie']+' '+df['Grupo de serie']+' '+df['Nombre de serie']).str.lower()
for dep in ['cajamarca','huancavelica','puno','loreto']:
    m=t.str.contains(dep); print(dep, m.sum(), (m & (df['Fecha de actualización']>='2025')).sum())
print(df[t.str.contains('cajamarca') & (df['Fecha de actualización']>='2025')][['Código de serie','Categoría de serie','Grupo de serie','Nombre de serie','Frecuencia']].head(25).to_string())
"
```

Resultado:

```text
Sun, Nov  8, 2026  9:04:23 PM
['Código de serie', 'Categoría de serie', 'Grupo de serie', 'Nombre de serie', 'Descripción de la serie', 'Metodología de la serie', 'Unidad de medida', 'Escala', 'Geografía (País, Región de Perú)', 'Fuente', 'Frecuencia', 'Fecha de creación', 'Grupo de publicación', 'Área que publica', 'Fecha de actualización', 'Fecha de inicio', 'Fecha de fin', 'Memo', 'Unnamed: 18']
17167
{'Código de serie': 'PN00001MM', 'Categoría de serie': 'Sociedades creadoras de depósito', 'Grupo de serie': 'Cuentas monetarias de las sociedades creadoras de depósito', 'Nombre de serie': 'Activos Externos Netos de Corto Plazo (millones S/)', 'Descripción de la serie': 'https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf', 'Metodología de la serie': 'https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf', 'Unidad de medida': '', 'Escala': '', 'Geografía (País, Región de Perú)': '', 'Fuente': 'BCRP', 'Frecuencia': 'Mensual', 'Fecha de creación': '2022-03-24', 'Grupo de publicación': 'Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias', 'Área que publica': 'Departamento de Estadísticas Monetarias', 'Fecha de actualización': '2026-10-23', 'Fecha de inicio': 'Ene-1992', 'Fecha de fin': 'Dic-2025', 'Memo': '', 'Unnamed: 18': ''}
Categoría de serie
Sistemas de pagos                   2344
Empresas bancarias                  1813
Exportaciones e importaciones       1482
Producción                          1449
Entre 1930 a 1980                   1418
Sector público                      1195
Balanza comercial                    814
Sistema financiero                   642
Primera centuria independiente       596
PBI por sectores                     538
Sociedades creadoras de depósito     501
Resultado económico                  395
Otras cuentas monetarias             303
Banco Central de Reserva             302
Periodo colonial temprano            289
Ingresos                             283
Gastos                               274
Tasas de interés                     253
Periodo colonial tardío              244
Mercado de capitales                 226
Deuda pública                        206
Expectativas Empresariales           156
PBI gasto                            134
Cuenta financiera                    116
Moneda y crédito                     111
cajamarca 184 112
huancavelica 200 112
puno 193 115
loreto 168 97
     Código de serie  C
… [recortado: 4,967 caracteres más]
```

</details>

## 🤖 Claude

Sugiero tres recursos. Revisé el catálogo del BCRP y trae más información de la que usaba la ficha anterior, entre otras cosas la unidad de medida, la escala, la fuente, el área que publica y la fecha de fin. También tiene cerca de 100 series vigentes por cada departamento.

### 1. `bcrp://serie/{codigo}`: la ficha de una serie (es la que exige la tarea)
- La tarea pide un recurso con información descriptiva de una serie, y este lo cubre directamente.
- Sería más completa que la anterior: nombre, categoría, grupo, frecuencia, **unidad y escala**, **fuente y área que publica**, fechas de inicio, fin y actualización, y el enlace para citarla.
- Sirve en la Parte 3 para el requisito de presentar cada cifra con su código, período y fuente.
- Solo lee el catálogo local, así que no depende de que la API del BCRP responda.

### 2. `bcrp://departamento/{ubigeo}`: las series regionales de un departamento (la que más recomiendo)
- Usa como llave el **código INEI de 2 dígitos**, que es el mismo de `ubigeo[:2]` en la ENAHO y de `FIRST_IDDP` en el mapa. Por ejemplo, `06` es Cajamarca.
- Devolvería las series del BCRP de ese departamento:
  - crédito y depósitos del sistema financiero;
  - producción minera (cobre, oro, plata, plomo, zinc) y producción de electricidad;
  - recaudación de la SUNAT;
  - gasto de los gobiernos locales.
- Es el puente entre las dos fuentes: desde un departamento del mapa de pobreza llegas a sus indicadores del BCRP. Eso fortalece la orquestación de la Parte 3 (2 pts) y una pregunta de investigación territorial.
- **Hay que verificar** cómo trata el BCRP a Lima y Callao, porque la tarea exige mantenerlos separados.

### 3. `bcrp://guia`: una guía de uso fija (opcional, toma poco tiempo)
- Explica el formato de fechas según la frecuencia, qué herramienta usar para cada caso y la diferencia entre puntos porcentuales y variación %.
- Agrega una lista corta de series clave para el estudio: inflación a 12 meses, inflación de alimentos, PBI, tipo de cambio y tasa de referencia.
- A diferencia de las plantillas, este recurso **sí aparece en el menú `@`** de Claude Code.
- En la Parte 4 ayudaría a que el modo con MCP no falle por usar mal las fechas.

**Mi recomendación:** hacer el 1 y el 2. El 1 cubre el requisito y el 2 es el que distingue tu trabajo y ayuda en las Partes 2 y 3. El 3 tomaría unos 10 minutos más. Son las 9:04 p. m. y quedan unas 2 h 55 min.

¿Cuáles hacemos?

## 👤 Usuaria

estan bien 1 y 2. vamos

## 🤖 Claude

Hago el 1 y el 2. Antes reviso cómo nombra el catálogo a los departamentos y si separa Lima de Callao.

<details><summary>🔧 Bash: Check how regional series name departments, Lima and Callao</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && PYTHONIOENCODING=utf-8 uv run python -c "
import pandas as pd
df=pd.read_csv('mcp/datos/catalogo_bcrp.csv',sep=';',dtype=str).fillna('')
g='Geografía (País, Región de Perú)'
print(df[g].value_counts().head(15).to_string())
rd=df[df['Código de serie'].str.startswith('RD')]
print('RD total',len(rd),'vigentes',(rd['Fecha de actualización']>='2025').sum())
print(rd[g].value_counts().head(10).to_string())
print(rd['Fecha de fin'].value_counts().head(8).to_string())
for pat in ['Lima','Callao']:
    s=rd[rd['Nombre de serie'].str.contains(pat)|rd['Grupo de serie'].str.contains(pat)]
    print('==',pat,len(s)); print(s['Nombre de serie'].value_counts().head(12).to_string())
print(rd[['Unidad de medida','Escala','Fuente','Área que publica']].drop_duplicates().head(10).to_string())
"
```

Resultado:

```text
Geografía (País, Región de Perú)
      8668
RE    4764
PE    3735
RD total 4764 vigentes 2911
Geografía (País, Región de Perú)
RE    4764
Fecha de fin
2025        800
T4-2025     791
Dic-2025    765
2022        470
Dic-2022    469
T4-2022     469
2019        232
T4-2019     226
== Lima 235
Nombre de serie
Lima                                      25
Lima (var% anual)                         12
Lima (millones de soles)                  12
Lima - Nacionales                          9
Lima - Extranjeros                         9
Lima Metropolitana (millones de soles)     9
Lima provincias (millones de soles)        9
Lima Metropolitana (var% anual)            9
Lima provincias (var% anual)               9
Lima (gwh)                                 6
Lima (moneda nacional)                     6
Lima (moneda extranjera)                   6
== Callao 159
Nombre de serie
Callao                               21
Callao (millones de soles)           21
Callao (var% anual)                  15
Callao - Nacionales                   9
Callao - Extranjeros                  9
Callao (moneda nacional)              6
Callao (moneda extranjera)            6
Callao (total)                        6
Lima - Puerto de Callao               3
Lima y Callao (millones de soles)     3
Lima y Callao (var% anual)            3
Marítima Del Callao                   3
      Unidad de medida Escala                                     Fuente                                  Área que publica
8772                                         Ministerio de la Producción    Departamento de Bases de Datos Macroeconómicas
8806                                       Ministerio de Energía y Minas    Departamento de Bases de Datos Macroeconómicas
8948                                                          Osinergmin    Departamento de Bases de Datos Macroeconómicas
8998                           Ministerio de Comercio Exterior y Turismo    Departamento de Bases de Datos Macroeconómicas
9223                                                                 SBS    Departamento de Bases de Datos Macroeconómicas
9379                                                                BCRP    Departamento de Bases de Datos Macroeconómicas
9437                                                               Sunat    Departamento de Bases de Datos Macroeconómicas
9649                                   Ministerio de Economía y Finanzas    Departamento de Bases de Datos 
… [recortado: 263 caracteres más]
```

</details>

<details><summary>🔧 Bash: Check FastMCP version, error types and BCRP web link format</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && uv run python -c "import fastmcp, fastmcp.exceptions as e; print(fastmcp.__version__, [n for n in dir(e) if 'Error' in n])"; curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" -L "https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01273PM/html"
```

Resultado:

```text
4.1.4 ['AuthorizationError', 'ClientError', 'DisabledError', 'ErrorData', 'FastMCPError', 'InsufficientScopeError', 'MCPError', 'McpError', 'NotFoundError', 'PromptError', 'ResourceError', 'ResourceSecurityError', 'ToolError', 'ValidationError']
200 https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01273PM/html
```

</details>

<details><summary>🔧 Edit</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py
--- antes ---
    df = df.rename(columns={"Código de serie": "codigo", "Categoría de serie": "categoria", "Grupo de serie": "grupo",
                            "Nombre de serie": "nombre", "Frecuencia": "frecuencia",
                            "Fecha de actualización": "actualizada", "Fecha de inicio": "inicio"})
    df["texto"] = (df.categoria + " " + df.grupo + " " + df.nombre).map(_sin_tildes)
    return df


def _ficha(codigo):
    fila = catalogo().query("codigo == @codigo")
    if fila.empty:
        raise ToolError(f"No existe el código de serie {codigo!r}. Búsquenlo con buscar_series.")
    f = fila.iloc[0]
    return {
--- después ---
    df = df.rename(columns={"Código de serie": "codigo", "Categoría de serie": "categoria", "Grupo de serie": "grupo",
                            "Nombre de serie": "nombre", "Frecuencia": "frecuencia",
                            "Fecha de actualización": "actualizada", "Fecha de inicio": "inicio",
                            "Fecha de fin": "fin", "Unidad de medida": "unidad", "Escala": "escala",
                            "Fuente": "fuente", "Área que publica": "area", "Grupo de publicación": "publicacion",
                            "Geografía (País, Región de Perú)": "geografia"})
    df["texto"] = (df.categoria + " " + df.grupo + " " + df.nombre).map(_sin_tildes)
    return df


def _fila(codigo):
    fila = catalogo().query("codigo == @codigo")
    if fila.empty:
        raise ToolError(f"No existe el código de serie {codigo!r}. Búsquenlo con buscar_series.")
    return fila.iloc[0]


def _ficha(codigo):
    f = _fila(codigo)
    return {
```

Resultado:

```text
The file ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py has been updated successfully.
```

</details>

<details><summary>🔧 Edit</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py
--- antes ---
# TODO 4 · Recursos: por definir.

--- después ---
# TODO 4 · Recursos. En Claude Code se adjuntan con @, por ejemplo @bcrp:bcrp://serie/PN01273PM o
# @bcrp:bcrp://departamento/06; el agente también puede leerlos por su cuenta.
WEB = "https://estadisticas.bcrp.gob.pe/estadisticas/series"
FRECUENCIA_WEB = {"Diaria": "diarias", "Mensual": "mensuales", "Trimestral": "trimestrales", "Anual": "anuales"}
GEOGRAFIA = {"PE": "Perú", "RE": "Departamento"}


def _unidad(f):
    """La unidad de la serie: la del catálogo si la trae; si no, la que va entre paréntesis al final del nombre o del
    grupo, como "(var% 12 meses)" o "(millones S/)". None si no aparece en ninguno."""
    if f.unidad:
        return f"{f.unidad} ({f.escala})" if f.escala else f.unidad
    for texto in (f.nombre, f.grupo):
        m = re.search(r"\(([^()]+)\)\s*$", texto)
        if m:
            return m.group(1)
    return None


@mcp.resource("bcrp://serie/{codigo}", mime_type="application/json")
def ficha_serie(codigo: str) -> str:
    """La ficha completa de una serie del BCRP, sin bajar sus datos: nombre, categoría, frecuencia, unidad, fuente
    original, área del BCRP que la publica, cobertura (inicio y fin), última actualización y el enlace para citarla.
    Sirve para saber qué mide una serie y hasta cuándo hay datos antes de pedirlos con serie o resumen."""
    try:
        f = _fila(codigo)
    except ToolError as e:
        raise ResourceError(str(e)) from None
    return json.dumps({
        "codigo": f.codigo, "nombre": f"{f.grupo} - {f.nombre}", "categoria": f.categoria, "grupo": f.grupo,
        "frecuencia": f.frecuencia, "unidad": _unidad(f),
        "cobertura": GEOGRAFIA.get(f.geografia, "No indicada"),
        "fuente_original": f.fuente or "No indicada", "publica": f"BCRP, {f.area}" if f.area else "BCRP",
        "publicacion": f.publicacion or None,
        "inicio": f.inicio, "fin": f.fin, "actualizada": f.actualizada,
        "enlace": f"{WEB}/{FRECUENCIA_WEB[f.frecuencia]}/resultados/{f.codigo}/html"
        if f.frecuencia in FRECUENCIA_WEB else WEB,
    }, ensure_ascii=False, indent=2)


# Los 25 departamentos con su código INEI: el mismo de ubigeo[:2] en la ENAHO y de FIRST_IDDP en el mapa.
DEPARTAMENTOS = {
    "01": "Amazonas", "02": "Áncash", "03": "Apurímac", "04": "Arequipa", "05": "Ayacucho", "06": "Cajamarca",
    "07": "Callao", "08": "Cusco", "09": "Huancavelica", "10": "Huánuco", "11": "Ica", "12": "Junín",
    "13": "La Libertad", "14": "Lambayeque", "15": "Lima", "16": "Loreto", "17": "Madre de Dios", "18": "Moquegua",
    "19": "Pasco", "20": "Piura", "21": "Puno", "22": "San Martín", "23": "Tacna", "24": "Tumbes", "25": "Ucayali",
}


@mcp.resource("bcrp://departamento/{ubigeo}", mime_type="application/json")
def series_departamento(ubigeo: str) -> str:
    """Las series regionales del BCRP de un departamento, agrupadas por tema: producción minera y de electricidad,
    crédito y depósitos, recaudación de la SUNAT, gasto público y otras. Solo las que tienen datos hasta 2024 o
    después, para cruzarlas con la ENAHO 2024.

    ubigeo es el código INEI de 2 dígitos ("06" es Cajamarca, "15" Lima, "07" Callao), el mismo de ubigeo[:2] en la
    ENAHO y de FIRST_IDDP en el mapa. También acepta el nombre ("Cajamarca"). Lima y Callao van separados; las series
    que los suman se listan aparte, en combinadas_lima_callao. Para los datos, usen serie o resumen con el código."""
    clave = ubigeo.strip().zfill(2) if ubigeo.strip().isdigit() else next(
        (k for k, v in DEPARTAMENTOS.items() if _sin_tildes(v) == _sin_tildes(ubigeo.strip())), None)
    if clave not in DEPARTAMENTOS:
        raise ResourceError(f"{ubigeo!r} no es un departamento. Usen el código INEI de 2 dígitos, del 01 (Amazonas) "
                            "al 25 (Ucayali), o el nombre del departamento.")
    df = catalogo()
    reg = df[(d
… [recortado: 1,128 caracteres más]
```

Resultado:

```text
The file ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py has been updated successfully.
```

</details>

<details><summary>🔧 Edit</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py
--- antes ---
"""
import re
import time
--- después ---
"""
import json
import re
import time
```

Resultado:

```text
The file ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py has been updated successfully.
```

</details>

<details><summary>🔧 Edit</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py
--- antes ---
from fastmcp.exceptions import ToolError
--- después ---
from fastmcp.exceptions import ResourceError, ToolError
```

Resultado:

```text
The file ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py has been updated successfully.
```

</details>

<details><summary>🔧 Edit</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py
--- antes ---
    "luego usa resumen para variaciones, promedios y extremos, y serie para los datos. No calcules a mano: "
    "cita siempre el código de la serie y el periodo."))
--- después ---
    "luego usa resumen para variaciones, promedios y extremos, y serie para los datos. No calcules a mano: "
    "cita siempre el código de la serie y el periodo. La ficha de una serie (unidad, fuente, cobertura) está en el "
    "recurso bcrp://serie/{codigo}; las series de un departamento, en bcrp://departamento/{ubigeo}, con el código "
    "INEI de 2 dígitos que usa la ENAHO en ubigeo[:2]."))
```

Resultado:

```text
The file ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py has been updated successfully.
```

</details>

## 🤖 Claude

Ahora corro las pruebas y leo los recursos desde un cliente MCP, como lo haría Claude Code.

<details><summary>🔧 Bash: Read both resources through an MCP client for all 25 departments</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad" && cat > "$S/probar_recursos.py" <<'EOF'
import asyncio, json, sys
sys.path.insert(0, "mcp")
from fastmcp import Client
from server import mcp

async def main():
    async with Client(mcp) as c:
        print("plantillas:", [t.uriTemplate for t in await c.list_resource_templates()])
        leer = lambda uri: c.read_resource(uri)
        f = json.loads((await leer("bcrp://serie/PN01273PM"))[0].text); print(json.dumps(f, ensure_ascii=False, indent=1))
        f = json.loads((await leer("bcrp://serie/RD12956DM"))[0].text); print(f["nombre"], "|", f["unidad"], "|", f["fuente_original"], "|", f["cobertura"], "|", f["fin"])
        for cod in [f"{i:02d}" for i in range(1, 26)]:
            d = json.loads((await leer(f"bcrp://departamento/{cod}"))[0].text)
            print(cod, d["departamento"], d["n_series"], len(d["temas"]), "comb:", len(d["combinadas_lima_callao"]))
        for cod in ("15", "07"):
            d = json.loads((await leer(f"bcrp://departamento/{cod}"))[0].text)
            print("==", d["departamento"], [t["tema"][:60] for t in d["temas"]][:6])
            print("   combinadas:", [s["nombre"] for s in d["combinadas_lima_callao"]])
            print("   nombres raros:", sorted({s["nombre"] for t in d["temas"] for s in t["series"]})[:40])
        d = json.loads((await leer("bcrp://departamento/san martin"))[0].text); print("por nombre:", d["ubigeo"], d["departamento"])
        print("tamaño JSON Cajamarca:", len((await leer("bcrp://departamento/06"))[0].text))
        for malo in ("bcrp://departamento/26", "bcrp://departamento/Narnia", "bcrp://serie/XX999"):
            try: await leer(malo); print("SIN ERROR", malo)
            except Exception as e: print("error OK:", malo, "->", str(e)[:140])
asyncio.run(main())
EOF
PYTHONIOENCODING=utf-8 uv run python "$S/probar_recursos.py" 2>&1 | tail -80
```

Resultado:

```text
                    │ ~\GITHUB\Diplomatura PUCP                │
                    │ 2026\diplomado_python_intermedio\tarea_4\.venv\Lib\site │
                    │ -packages\fastmcp\resources\template.py:583 in _read    │
                    │                                                         │
                    │                 ... 6 frames hidden ...                 │
                    │                                                         │
                    │ ~\GITHUB\Diplomatura PUCP                │
                    │ 2026\diplomado_python_intermedio\tarea_4\.venv\Lib\site │
                    │ -packages\pydantic\_internal\_validate_call.py:137 in   │
                    │ __call__                                                │
                    │                                                         │
                    │ ~\GITHUB\Diplomatura PUCP                │
                    │ 2026\diplomado_python_intermedio\tarea_4\mcp\server.py: │
                    │ 256 in ficha_serie                                      │
                    │                                                         │
                    │   253 │   try:                                          │
                    │   254 │   │   f = _fila(codigo)                         │
                    │   255 │   except ToolError as e:                        │
                    │ > 256 │   │   raise ResourceError(str(e)) from None     │
                    │   257 │   return json.dumps({                           │
                    │   258 │   │   "codigo": f.codigo, "nombre": f"{f.grupo} │
                    │       f.categoria, "grupo": f.grupo,                    │
                    │   259 │   │   "frecuencia": f.frecuencia, "unidad": _un │
                    └─────────────────────────────────────────────────────────┘
                    ResourceError: No existe el código de serie 'XX999'.       
                    Búsquenlo con buscar_series.                               
plantillas: ['bcrp://serie/{codigo}', 'bcrp://departamento/{ubigeo}']
{
 "codigo": "PN01273PM",
 "nombre": "Índice de precios Lima Metropolitana (var% 12 meses) - IPC",
 "categoria": "Inflación",
 "grupo": "Índice de precios Lima Metropolitana (var% 12 meses)",
 "frecuencia": "Mensual",
 "unidad": "var% 12 meses",
 "cobertura": "No indicada",
 "fuente_original": "INEI",
 "publica":
… [recortado: 3,858 caracteres más]
```

</details>

<details><summary>🔧 Bash: Compare catalog end dates with update dates and live API</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && PYTHONIOENCODING=utf-8 uv run python -c "
import pandas as pd
df=pd.read_csv('mcp/datos/catalogo_bcrp.csv',sep=';',dtype=str).fillna('')
re_=df[df['Geografía (País, Región de Perú)']=='RE']
fin=re_['Fecha de fin'].str[-4:]; act=re_['Fecha de actualización']
print('fin<2024 y actualizada>=2025:', ((fin<'2024')&(act>='2025')).sum())
print(pd.crosstab(fin, act.str[:4]).tail(8))
"; curl -s "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD12956DM/json/2025-1/2026-12" | python -c "import sys,json; p=json.load(sys.stdin)['periods']; print('RD12956DM último:', p[-1])"
```

Resultado:

```text
fin<2024 y actualizada>=2025: 534
Fecha de actualización  2024  2026
Fecha de fin                      
2018                       0    43
2019                     225   458
2020                       0     1
2021                      48     3
2022                    1407     1
2023                     123     0
2024                       0    21
2025                       0  2356
RD12956DM �ltimo: {'name': 'Jun.2026', 'values': ['1454.9842']}
```

</details>

<details><summary>🔧 Bash: Check whether series marked as ending in 2019 really stopped</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && PYTHONIOENCODING=utf-8 uv run python -c "
import pandas as pd
df=pd.read_csv('mcp/datos/catalogo_bcrp.csv',sep=';',dtype=str).fillna('')
re_=df[(df['Geografía (País, Región de Perú)']=='RE')&(df['Fecha de fin'].str[-4:]=='2019')&(df['Fecha de actualización']>='2026')]
print(re_['Grupo de serie'].value_counts().head(6).to_string()); s=re_.iloc[0]; print(s['Código de serie'], s['Frecuencia'], s['Nombre de serie'])
" ; curl -s "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD38085BM/json/2018-1/2026-12" | head -c 300
```

Resultado:

```text
Grupo de serie
Arribos a los establecimientos de hospedaje según departamentos (número)               150
Pernoctaciones en los establecimientos de hospedaje (número)                           150
Permanencia promedio en los establecimientos de hospedaje (número de días)             150
Desembarque de anchoveta para harina y aceite por departamento y puerto (toneladas)      8
RD14253DQ Trimestral Arequipa - Puerto de Atico
{
"config":
{
"title":"Exportaciones por Departamento (Valores FOB en millones US$)",
"series":
[
{
"name":"Exportaciones por Departamento (Valores FOB en millones US$) - Amazonas",
"dec":"0"
}]
},
"periods":
[
{
"name":"Ene.2018",
"values":["2.40446246"]
},
{
"name":"Feb.2018",
"values":["1.7270469
```

</details>

<details><summary>🔧 Bash: Query live API for a tourism series marked as ending 2019</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && C=$(PYTHONIOENCODING=utf-8 uv run python -c "
import pandas as pd
df=pd.read_csv('mcp/datos/catalogo_bcrp.csv',sep=';',dtype=str).fillna('')
s=df[(df['Grupo de serie'].str.startswith('Arribos a los establecimientos'))&(df['Fecha de fin'].str[-4:]=='2019')].iloc[0]
print(s['Código de serie'])"); echo "$C"; curl -s "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/$C/json/2019-1/2026-12" | python -c "import sys,json; p=json.load(sys.stdin)['periods']; print(len(p), p[0], p[-1])"
```

Resultado:

```text
RD13335DM
12 {'name': 'Ene.2019', 'values': ['43554']} {'name': 'Dic.2019', 'values': ['37409']}
```

</details>

<details><summary>🔧 Bash: Relabel catalog end dates and rerun the test suite</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && python - <<'EOF'
from pathlib import Path
p = Path("mcp/server.py"); s = p.read_text(encoding="utf-8")
cambios = [
 ('        "inicio": f.inicio, "fin": f.fin, "actualizada": f.actualizada,\n',
  '        # la fecha de fin del catálogo puede ir atrasada: serie trae los datos más recientes que tenga la API\n'
  '        "inicio": f.inicio, "fin_segun_catalogo": f.fin, "actualizada": f.actualizada,\n'),
 ('"frecuencia": f.frecuencia, "hasta": f.fin}', '"frecuencia": f.frecuencia, "hasta_segun_catalogo": f.fin}'),
 ('    después, para cruzarlas con la ENAHO 2024.\n',
  '    después según el catálogo (que puede ir atrasado: la API suele tener datos más recientes), para cruzarlas con\n'
  '    la ENAHO 2024.\n'),
]
for a, b in cambios:
    assert s.count(a) == 1, a; s = s.replace(a, b)
p.write_text(s, encoding="utf-8")
EOF
uv run pytest -q 2>&1 | tail -3
```

Resultado:

```text
..........                                                               [100%]
10 passed in 9.89s
```

</details>

## 🤖 Claude

Los dos recursos quedaron listos y las pruebas dan **10 passed**.

**`bcrp://serie/{codigo}`, la ficha de una serie:**
- Devuelve el nombre, la categoría, la frecuencia, la **unidad**, la **fuente original** (INEI, MINEM, SUNAT…), el área del BCRP que la publica, la cobertura, las fechas y el **enlace web** para citarla. Comprobé que el enlace abre.
- Por ejemplo, `PN01273PM` sale como "var% 12 meses", con fuente INEI y publicada por el Departamento de Estadísticas de Precios.
- Si el código no existe, devuelve un error claro.

**`bcrp://departamento/{ubigeo}`, las series regionales:**
- Recibe el código INEI de 2 dígitos, el mismo de `ubigeo[:2]` en la ENAHO y de `FIRST_IDDP` en el mapa. También acepta el nombre, por ejemplo `san martin`.
- Funciona para los **25 departamentos**, con entre 63 y 128 series cada uno, agrupadas en 12 a 17 temas: minería, electricidad, crédito, depósitos, SUNAT, gasto regional y local, entre otros.
- Solo incluye series con datos hasta 2024 o después. Comprobé en la API que las que el catálogo da por terminadas en 2019 (por ejemplo, turismo) de verdad terminan ahí.
- **Lima (15) y Callao (07) quedan separados.** Las 9 series que los suman, como "Lima y Callao" o "Lima - Puerto de Callao", aparecen aparte en `combinadas_lima_callao`.
- Un código como `26` o un nombre que no existe devuelve un error claro.

También agregué los dos recursos a las instrucciones del servidor, para que el agente sepa que existen.

**Un detalle del catálogo:** la "fecha de fin" puede estar atrasada. Por ejemplo, el cobre de Cajamarca figura hasta dic-2025, pero la API ya tiene datos hasta jun-2026. Por eso ese campo se llama `fin_segun_catalogo`.

**Pendiente de la Parte 1:** demostrar el MCP desde Claude Code, que vale 1 punto. Para eso hay que abrir una sesión en `tarea_4/`, donde está el `.mcp.json`. Propongo hacerlo dentro de la ejecución de la Parte 3, así sirve de evidencia para las dos partes.

Son cerca de las 9:15 p. m. ¿Hago el commit de la Parte 1 en `parte-1-mcp-bcrp` y seguimos con la Parte 2?

## 👤 Usuaria

no. hagamos la demostración desde ahora. como la hacemos

## 🤖 Claude

Hay que abrir una sesión nueva de Claude Code dentro de `tarea_4/`. Esta sesión empezó en la raíz del repo y no cargó ese `.mcp.json`. Primero compruebo que Claude Code detecta el servidor desde esa carpeta.

<details><summary>🔧 PowerShell: Check Claude Code detects the bcrp server from tarea_4</summary>

```powershell
Set-Location "~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4"; (Get-Command claude -ErrorAction SilentlyContinue).Source; claude mcp list
```

Resultado:

```text
~\.local\bin\claude.exe
Checking MCP server health…

claude.ai Claude Docs: https://api.anthropic.com/v1/pages/mcp - ✔ Connected
claude.ai Microsoft 365: https://microsoft365.mcp.claude.com/mcp - ✔ Connected
bcrp: uv run mcp/server.py - ⏸ Pending approval (run `claude` to approve)
fetch: uvx mcp-server-fetch - ⏸ Pending approval (run `claude` to approve)
```

</details>

<details><summary>🔧 Bash: Create the folder for the MCP demo export</summary>

```bash
mkdir -p "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4/evidencias_ia/mcp" && echo ok
```

Resultado:

```text
ok
```

</details>

## 🤖 Claude

Claude Code ya detecta el servidor `bcrp` desde `tarea_4/`. Está pendiente de aprobación, igual que `fetch`, y eso se resuelve al abrir la sesión. También creé `evidencias_ia/mcp/` para guardar ahí la exportación.

## Cómo hacer la demostración (unos 10–15 min)

**1. Abre otra terminal y entra a la carpeta**
```
cd "~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4"
claude
```
- Cuando pregunte por los servidores del `.mcp.json`, **aprueba solo `bcrp`** y rechaza `fetch`. Así el agente no puede bajar datos de la web del BCRP sin pasar por tus herramientas.
- Cada vez que pida permiso para una herramienta `mcp__bcrp__…`, elige *"Yes, and don't ask again"*.

**2. Comprueba la conexión:** escribe `/mcp`. `bcrp` debe aparecer *connected*, con 4 herramientas, 2 recursos y 1 prompt. Te conviene una captura de esta pantalla.

**3. Pega estos pedidos de uno en uno.** Juntos cubren los 4 pasos que exige la tarea (identificar la serie, pedir los datos, calcular con las herramientas y presentar código, período y fuente), además de los recursos, el prompt y tu herramienta propia:

| # | Pedido | Qué demuestra |
|---|---|---|
| a | `Usando solo las herramientas del MCP bcrp: ¿cómo evolucionó la inflación a 12 meses de Lima Metropolitana entre enero de 2020 y diciembre de 2024? Dame el primer y último valor, el máximo y el promedio, con código de serie, periodo y fuente.` | `buscar_series` → `resumen` |
| b | `@bcrp:bcrp://serie/PN01273PM ¿Qué mide esta serie, en qué unidad está y cuál es su fuente original?` | Recurso de ficha |
| c | `@bcrp:bcrp://departamento/06 ¿Qué series del BCRP hay para Cajamarca? Con las herramientas del MCP, dime el mes de mayor producción de cobre de Cajamarca en 2024 y el promedio mensual de ese año.` | Recurso departamental → `resumen` |
| d | `Con comparar_paises: ¿creció más el Perú que Chile y Colombia entre 2015 y 2024? Dame el promedio de cada país y la fuente.` | Herramienta propia |
| e | `/mcp__bcrp__informe tipo de cambio` | Prompt MCP |

**4. Exporta la conversación** sin cerrar la sesión:
```
/export evidencias_ia/mcp/01_demo_mcp_claude_code.txt
```

Cuando termines, avísame. Después reviso la exportación y verifico las cifras directamente en la API del BCRP y del Banco Mundial; eso también sirve de práctica para la verificación de la Parte 3. También copio a `evidencias_ia/` el registro completo de esa sesión, que Claude Code guarda como `.jsonl` e incluye cada llamada a las herramientas.

Para la Parte 4 hay que documentar que en esa sesión también están conectados *Claude Docs* y *Microsoft 365*, que son conectores de tu cuenta de claude.ai.

## 👤 Usuaria

YA ESTA. ve documentando nuestras conversaciones en un markdown

## 🤖 Claude

Primero reviso la exportación de la demostración. Después armo el markdown con nuestra conversación.

<details><summary>🔧 Bash: Locate the demo export and session transcripts</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && ls -la evidencias_ia/mcp/ && wc -c evidencias_ia/mcp/*; echo; ls -la ~/.claude/projects/ | grep -i diplomado; ls -la ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/ 2>/dev/null; ls -la ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/*.jsonl | tail -3
```

Resultado:

```text
total 28
drwxr-xr-x 1 usuario 1049089     0 Nov  8 21:33 .
drwxr-xr-x 1 usuario 1049089     0 Nov  8 21:18 ..
-rw-r--r-- 1 usuario 1049089 28374 Nov  8 21:33 01_demo_mcp_claude_code.txt
28374 evidencias_ia/mcp/01_demo_mcp_claude_code.txt

drwxr-xr-x 1 usuario 1049089 0 Nov  6 17:08 C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-Diplomado-PUCP
drwxr-xr-x 1 usuario 1049089 0 Oct 11 19:04 C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-DiplomadoPUCP2026-FundamentosPython
drwxr-xr-x 1 usuario 1049089 0 Oct 25 19:32 C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-DiplomadoPUCP2026-FundamentosPython-Tarea-3
drwxr-xr-x 1 usuario 1049089 0 Nov  8 20:46 C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio
drwxr-xr-x 1 usuario 1049089 0 Nov  8 21:23 C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4
drwxr-xr-x 1 usuario 1049089 0 Nov  1 19:06 C--Users-usuario-OneDrive---HERNANDEZ---CIA-Documentos-GitHub-Diplomado-PUCP
total 876
drwxr-xr-x 1 usuario 1049089      0 Nov  8 21:23 .
drwxr-xr-x 1 usuario 1049089      0 Nov  8 21:23 ..
-rw-r--r-- 1 usuario 1049089 870021 Nov  8 21:33 7bfebfb8-d42f-472c-8fb2-7a5f78500694.jsonl
-rw-r--r-- 1 usuario 1049089 69681000 Nov  4 07:52 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/e13b3eef-d364-49f9-b8c5-a933a1e2bb0a.jsonl
-rw-r--r-- 1 usuario 1049089  5291274 Oct 18 23:09 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/e2663f81-fd11-426e-af9e-1aa5eee59f80.jsonl
-rw-r--r-- 1 usuario 1049089  1483609 Oct 19 09:38 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/fe611167-0042-4607-bef0-49ebeef88462.jsonl
```

</details>

<details><summary>🔧 Read</summary>

```json
{
  "file_path": "C:\\Users\\usuario\\GITHUB\\Diplomatura PUCP 2026\\diplomado_python_intermedio\\tarea_4\\evidencias_ia\\mcp\\01_demo_mcp_claude_code.txt"
}
```

Resultado:

```text
1	 ▐▛███▛█   Claude Code v2.1.319
2	▝▜██████▀  Opus 5.5 · Claude Pro
3	 ▝▝   ▝▝   ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea…
4	
5	
6	❯ /mcp.bcrp                                                                     
7	
8	  Read 2 files, ran 3 shell commands (ctrl+o to expand)
9	
10	● Voy a probar el servidor bcrp desde Claude Code: una llamada a cada
11	  herramienta y una al recurso.
12	
13	  Called bcrp 4 times (ctrl+o to expand)
14	
15	● readMcpResource(Read resource "bcrp://serie/PN01273PM" from server "bcrp")
16	  ⎿  {
17	       "contents": [
18	         {
19	     … +15 lines (ctrl+o to expand)
20	
21	● Las cinco llamadas respondieron. Ahora corro las pruebas del contrato.
22	
23	  Ran 1 shell command (ctrl+o to expand)
24	
25	● El servidor bcrp está conectado a Claude Code y funciona: todas las
26	  herramientas y el recurso respondieron con datos reales, y pasan las 10
27	  pruebas (uv run pytest: las 8 del curso y las 2 tuyas).
28	
29	  /mcp.bcrp no es un comando. Si querías ver el estado del servidor, es /mcp. El
30	  prompt del servidor se llama con /mcp__bcrp__informe <tema>, por ejemplo
31	  /mcp__bcrp__informe inflación.
32	
33	  ┌─────────────────────────────────┬───────────────────────────────────────┐
34	  │            Qué probé            │               Resultado               │
35	  ├─────────────────────────────────┼───────────────────────────────────────┤
36	  │ buscar_series("ipc 12 meses")   │ Primer resultado: PN01273PM (IPC      │
37	  │                                 │ Lima, var% 12 meses)                  │
38	  ├─────────────────────────────────┼───────────────────────────────────────┤
39	  │ resumen(PN01273PM, 2025-12 →    │ Pasó de 1.51 % a 4.55 %: subió 3.04   │
40	  │ 2026-09)                        │ puntos, con promedio de 3.42 % y el   │
41	  │                                 │ máximo en 2026-09                     │
42	  ├─────────────────────────────────┼───────────────────────────────────────┤
43	  │ serie(PD04638PD, 13–15 oct      │ Tipo de cambio interbancario de       │
44	  │ 2026)                           │ venta: 3.438, 3.439 y 3.428           │
45	  ├─────────────────────────────────┼───────────────────────────────────────┤
46	  │ comparar_paises(PER;CHL;COL,    │ Crecimiento promedio del PBI en esos  │
47	  │ 2023–2025)                      │ años: Perú 2.20 %, Chile 1.98 %,      │
48	  │                                 │ Colombia 1.66 %                       │
49	  ├─────────────────────
… [recortado: 18,938 caracteres más]
```

</details>

<details><summary>🔧 Bash: Verify demo figures against the APIs and inspect transcript structure</summary>

```bash
S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad"; cat > "$S/verificar_demo.py" <<'EOF'
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
EOF
python -I "$S/verificar_demo.py"; echo ---; J=~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/57ecd584-3768-4852-a254-c84910c84d73.jsonl; ls -la $J; python -I -c "
import json,sys,collections
c=collections.Counter()
for l in open(sys.argv[1],encoding='utf-8'):
    d=json.loads(l); t=d.get('type'); c[t]+=1
    if t in('user','assistant'):
        m=d['message']['content']
        kinds=[b.get('type') for b in m] if isinstance(m,list) else ['str']
        c[(t,)+tuple(sorted(set(kinds)))]+=1
for k,v in c.items(): print(v,k)
" $J
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Bash: Inspect attachment types and plain user messages in transcript</summary>

```bash
J=~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/57ecd584-3768-4852-a254-c84910c84d73.jsonl; python -I -c "
import json,sys,collections
for l in open(sys.argv[1],encoding='utf-8'):
    d=json.loads(l)
    if d.get('type')=='attachment':
        a=d.get('attachment',{}); print(a.get('type'), repr(json.dumps(a,ensure_ascii=False)[:160]))
    if d.get('type')=='user' and isinstance(d['message']['content'],str):
        print('USER', d.get('isMeta'), repr(d['message']['content'][:120]))
" $J | sort | uniq -c | sort -rn | head -30
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Bash: Find where mid-turn and typed user messages are stored ⚠️ error</summary>

```bash
J=~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/57ecd584-3768-4852-a254-c84910c84d73.jsonl; PYTHONIOENCODING=utf-8 python -I -c "
import json,sys
for l in open(sys.argv[1],encoding='utf-8'):
    d=json.loads(l)
    if d.get('type')=='attachment':
        a=d.get('attachment',{})
        if a.get('type') not in ('skill_listing','session_context','model','mcp_instructions_delta','instructions','environment','deferred_tools_delta','date','credential_org','auto_mode','agent_listing_delta'):
            print(a.get('type'), json.dumps(a,ensure_ascii=False)[:300])
    if d.get('type')=='user' and isinstance(d['message']['content'],str):
        print('USER', repr(d['message']['content'][:200]))
    if d.get('type')=='queue-operation': print('QUEUE', json.dumps(d,ensure_ascii=False)[:300])
" $J
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Bash: Find where mid-turn and typed user messages are stored</summary>

```bash
J=~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/57ecd584-3768-4852-a254-c84910c84d73.jsonl; python -I -c "
import json,sys; sys.stdout.reconfigure(encoding='utf-8')
skip={'skill_listing','session_context','model','mcp_instructions_delta','instructions','environment','deferred_tools_delta','date','credential_org','auto_mode','agent_listing_delta'}
for l in open(sys.argv[1],encoding='utf-8'):
    d=json.loads(l)
    if d.get('type')=='attachment':
        a=d.get('attachment',{})
        if a.get('type') not in skip: print('ATT', a.get('type'), json.dumps(a,ensure_ascii=False)[:250])
    if d.get('type')=='user' and isinstance(d['message']['content'],str):
        print('USER', repr(d['message']['content'][:150]))
    if d.get('type')=='queue-operation': print('QUEUE', json.dumps(d,ensure_ascii=False)[:250])
" $J
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Write</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evidencias_ia\exportar_conversacion.py

"""Convierte el registro de una sesión de Claude Code (.jsonl) en un markdown legible para evidencias_ia/.

    python evidencias_ia/exportar_conversacion.py <sesion.jsonl> <salida.md> "<título>"

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

MAX_ENTRADA = 4000
MAX_RESULTADO = 2500
# resultados que no se publican: incluían comentarios del issue con entregas de otros estudiantes
OMITIR_SI_LA_ENTRADA_TIENE = ("/comments", "comments.json", "issue.txt")


def ocultar(texto):
    texto = re.sub(r"[\w.+-]+@[\w-]+\.[\w.-]+", "[correo oculto]", texto)
    texto = re.sub(r"noreply\[correo oculto\]", "[correo oculto]", texto)  # la firma de los commits no es privada
    for ruta in (r"C:\\Users\\usuario", "~", "~"):
        texto = texto.replace(ruta.replace("\\\\", "\\"), "~")
    return texto.replace("usuario", "usuario")


def limpiar_mensaje(texto):
    texto = re.sub(r"<system-reminder>.*?</system-reminder>", "", texto, flags=re.S)
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
    return md.replace("ˋˋˋ", "ˋˋˋ")  # que un ˋˋˋ dentro del texto no cierre el bloque de código


def exportar(jsonl, salida, titulo):
    lineas = [json.loads(l) for l in Path(jsonl).read_text(encoding="utf-8").splitlines() if l.strip()]
    pendientes, out = {}, []
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
       
… [recortado: 2,475 caracteres más]
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

## 🤖 Claude

Antes de correrlo limpio dos restos del borrador.

<details><summary>🔧 Edit</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evidencias_ia\exportar_conversacion.py
--- antes ---
                        resultado = recortar(texto_de(b.get("content")), MAX_RESULTADO)
                    lenguaje = entrada_legible(nombre, {})[1] if False else None
                    out += [
--- después ---
                        resultado = recortar(texto_de(b.get("content")), MAX_RESULTADO)
                    out += [
```

Resultado:

```text
The file ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evidencias_ia\exportar_conversacion.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>🔧 Edit</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evidencias_ia\exportar_conversacion.py
--- antes ---
    pendientes, out = {}, []
--- después ---
    pendientes, pendientes_lenguaje, out = {}, {}, []
```

Resultado:

```text
The file ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evidencias_ia\exportar_conversacion.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>🔧 Edit</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evidencias_ia\exportar_conversacion.py
--- antes ---
    return len(out)


pendientes_lenguaje = {}

if __name__
--- después ---
    return len(out)


if __name__
```

Resultado:

```text
The file ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evidencias_ia\exportar_conversacion.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>🔧 Bash: Export both sessions to markdown and check redactions</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && P=~/.claude/projects && python -I evidencias_ia/exportar_conversacion.py "$P/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/57ecd584-3768-4852-a254-c84910c84d73.jsonl" evidencias_ia/00_sesion_principal_claude_code.md "Sesión principal de desarrollo con Claude Code (Tarea 4)" && python -I evidencias_ia/exportar_conversacion.py "$P/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/7bfebfb8-d42f-472c-8fb2-7a5f78500694.jsonl" evidencias_ia/mcp/02_demo_mcp_claude_code_completa.md "Demostración del MCP del BCRP desde Claude Code (registro completo)" && echo "--- chequeos de privacidad" && grep -c "Resultado omitido" evidencias_ia/00_sesion_principal_claude_code.md; grep -niE "gmail|pucp\.edu|usuario|[oculto]|[oculto]|[oculto]|[oculto]|[oculto]|[oculto]|organizationUuid" evidencias_ia/00_sesion_principal_claude_code.md evidencias_ia/mcp/02_demo_mcp_claude_code_completa.md | head; echo "--- mensajes de la usuaria"; grep -n -A2 "^## 👤" evidencias_ia/00_sesion_principal_claude_code.md | grep -v "^--$" | grep -v "^[0-9]*-$" | head -30
```

Resultado:

```text
evidencias_ia/00_sesion_principal_claude_code.md: 800 l�neas
evidencias_ia/mcp/02_demo_mcp_claude_code_completa.md: 434 l�neas
--- chequeos de privacidad
7
evidencias_ia/00_sesion_principal_claude_code.md:1955:      1 credential_org '{"type": "credential_org", "": "[oculto]"}'
--- mensajes de la usuaria
```

</details>

## 🤖 Claude

Encontré un dato interno de la cuenta en el resultado de uno de mis comandos de inspección. Lo oculto, omito esos resultados y vuelvo a exportar.

<details><summary>🔧 Bash: Redact account IDs, re-export, and audit both markdown files</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && python - <<'EOF'
from pathlib import Path
p = Path("evidencias_ia/exportar_conversacion.py"); s = p.read_text(encoding="utf-8")
a = '''# resultados que no se publican: incluían comentarios del issue con entregas de otros estudiantes
OMITIR_SI_LA_ENTRADA_TIENE = ("/comments", "comments.json", "issue.txt")'''
b = '''# resultados que no se publican: los comentarios del issue (entregas de otros estudiantes) y la inspección del propio
# registro de la sesión (repite datos internos de la cuenta y del sistema)
OMITIR_SI_LA_ENTRADA_TIENE = ("/comments", "comments.json", "issue.txt", "json.loads(l)")'''
assert s.count(a) == 1; s = s.replace(a, b)
a2 = '''                        resultado = "[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes.]"'''
b2 = '''                        resultado = ("[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes "
                                     "o datos internos del registro de la sesión.]")'''
assert s.count(a2) == 1; s = s.replace(a2, b2)
a3 = '''    texto = re.sub(r"noreply'''
b3 = '''    texto = re.sub(r'"(organizationUuid|accountUuid)": "[^"]+"', r'"\\1": "[oculto]"', texto)
    texto = re.sub(r"noreply'''
assert s.count(a3) == 1; s = s.replace(a3, b3)
p.write_text(s, encoding="utf-8")
EOF
P=~/.claude/projects && python -I evidencias_ia/exportar_conversacion.py "$P/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/57ecd584-3768-4852-a254-c84910c84d73.jsonl" evidencias_ia/00_sesion_principal_claude_code.md "Sesión principal de desarrollo con Claude Code (Tarea 4)" >/dev/null && python -I evidencias_ia/exportar_conversacion.py "$P/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/7bfebfb8-d42f-472c-8fb2-7a5f78500694.jsonl" evidencias_ia/mcp/02_demo_mcp_claude_code_completa.md "Demostración del MCP del BCRP desde Claude Code (registro completo)" >/dev/null && python -I -c "
import re,sys; sys.stdout.reconfigure(encoding='utf-8')
for f in ['evidencias_ia/00_sesion_principal_claude_code.md','evidencias_ia/mcp/02_demo_mcp_claude_code_completa.md']:
    t=open(f,encoding='utf-8').read()
    print('==',f,len(t),'chars | omitidos:',t.count('Resultado omitido'),'| herramientas:',t.count('<details>'))
    print('  sensibles:', re.findall(r'gmail|pucp\.edu|usuario|[oculto]|[oculto]|[oculto]|[oculto]|[oculto]|[oculto]|[oculto]|prompt_snapshot',t, re.I))
    for m in re.finditer(r'^## 👤[^\n]*\n\n([^\n]{0,110})',t,re.M): print('  >',m.group(1))
"
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Bash: Locate remaining sensitive strings in the main export</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && python -I -c "
import re,sys; sys.stdout.reconfigure(encoding='utf-8')
t=open('evidencias_ia/00_sesion_principal_claude_code.md',encoding='utf-8').read()
for m in re.finditer(r'gmail|[oculto]|[oculto]',t,re.I): print(m.start(), repr(t[max(0,m.start()-120):m.start()+60])); print()
"
```

Resultado:

```text
95110 '--- chequeos de privacidad" && grep -c "Resultado omitido" evidencias_ia/00_sesion_principal_claude_code.md; grep -niE "gmail|pucp\\.edu|usuario|[oculto]|[oculto]|[oculto]|'

95134 'ad" && grep -c "Resultado omitido" evidencias_ia/00_sesion_principal_claude_code.md; grep -niE "gmail|pucp\\.edu|usuario|[oculto]|[oculto]|[oculto]|[oculto]|[oculto]|nic'

95142 'rep -c "Resultado omitido" evidencias_ia/00_sesion_principal_claude_code.md; grep -niE "gmail|pucp\\.edu|usuario|[oculto]|[oculto]|[oculto]|[oculto]|[oculto]|[oculto]|org'
```

</details>

<details><summary>🔧 Bash: Add term-redaction list, re-export, and re-audit both files</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad" && printf '%s\n' [oculto] [oculto] [oculto] [oculto] [oculto] [oculto] [oculto] [oculto] > "$S/ocultar.txt" && python - <<'EOF'
from pathlib import Path
p = Path("evidencias_ia/exportar_conversacion.py"); s = p.read_text(encoding="utf-8")
reemplazos = [
 ('''    python evidencias_ia/exportar_conversacion.py <sesion.jsonl> <salida.md> "<título>"
''', '''    python evidencias_ia/exportar_conversacion.py <sesion.jsonl> <salida.md> "<título>" [términos_a_ocultar.txt]

El cuarto argumento, opcional, es un archivo fuera del repositorio con un término por línea (por ejemplo, nombres de
otras personas que aparezcan en los comandos): cada uno se reemplaza por [oculto].
'''),
 ('''def ocultar(texto):
''', '''TERMINOS = []


def ocultar(texto):
    for t in TERMINOS:
        texto = re.sub(re.escape(t), "[oculto]", texto, flags=re.I)
'''),
 ('''    texto = re.sub(r"</?(command-name''', '''    texto = re.sub(r"</?pasted_content[^>]*>", "", texto)
    texto = re.sub(r"</?(command-name'''),
 ('''    jsonl, salida, titulo = sys.argv[1:4]
''', '''    jsonl, salida, titulo = sys.argv[1:4]
    if len(sys.argv) > 4:
        TERMINOS += [t.strip() for t in Path(sys.argv[4]).read_text(encoding="utf-8").splitlines() if t.strip()]
'''),
]
for a, b in reemplazos:
    assert s.count(a) == 1, a; s = s.replace(a, b)
p.write_text(s, encoding="utf-8")
EOF
P=~/.claude/projects && python -I evidencias_ia/exportar_conversacion.py "$P/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/57ecd584-3768-4852-a254-c84910c84d73.jsonl" evidencias_ia/00_sesion_principal_claude_code.md "Sesión principal de desarrollo con Claude Code (Tarea 4)" "$S/ocultar.txt" >/dev/null && python -I evidencias_ia/exportar_conversacion.py "$P/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/7bfebfb8-d42f-472c-8fb2-7a5f78500694.jsonl" evidencias_ia/mcp/02_demo_mcp_claude_code_completa.md "Demostración del MCP del BCRP desde Claude Code (registro completo)" "$S/ocultar.txt" >/dev/null && python -I - "$S/ocultar.txt" <<'EOF'
import re, sys; sys.stdout.reconfigure(encoding="utf-8")
terminos = [t.strip() for t in open(sys.argv[1], encoding="utf-8") if t.strip()] + ["gmail", "pucp.edu", "usuario", "[oculto]", "prompt_snapshot", "pasted_content"]
for f in ["evidencias_ia/00_sesion_principal_claude_code.md", "evidencias_ia/mcp/02_demo_mcp_claude_code_completa.md"]:
    t = open(f, encoding="utf-8").read()
    print(f, len(t), "caracteres; términos sensibles encontrados:", [x for x in terminos if x.lower() in t.lower()])
EOF
date
```

Resultado:

```text
evidencias_ia/00_sesion_principal_claude_code.md 99906 caracteres; términos sensibles encontrados: ['gmail', '[oculto]', 'prompt_snapshot']
evidencias_ia/mcp/02_demo_mcp_claude_code_completa.md 39030 caracteres; términos sensibles encontrados: []
Sun, Nov  8, 2026  9:38:46 PM
```

</details>

<details><summary>🔧 Bash: Hide the account ID fragment, re-export and confirm no emails</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad" && echo [oculto] >> "$S/ocultar.txt" && P=~/.claude/projects && python -I evidencias_ia/exportar_conversacion.py "$P/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/57ecd584-3768-4852-a254-c84910c84d73.jsonl" evidencias_ia/00_sesion_principal_claude_code.md "Sesión principal de desarrollo con Claude Code (Tarea 4)" "$S/ocultar.txt" && python -I -c "
import re,sys; sys.stdout.reconfigure(encoding='utf-8')
t=open('evidencias_ia/00_sesion_principal_claude_code.md',encoding='utf-8').read()
print('correos reales:', re.findall(r'[\w.+-]+@(?!anthropic)[\w-]+\.[\w.-]+',t)); print('uuid org:', '[oculto]' in t)
for m in re.finditer(r'gmail',t): print(repr(t[m.start()-40:m.start()+30]))
" ; git -C .. status --short
```

Resultado:

```text
evidencias_ia/00_sesion_principal_claude_code.md: 860 l�neas
correos reales: []
uuid org: False
'on_principal_claude_code.md; grep -niE "gmail|pucp\\.edu|usuario|[ocult'
"\n    print('  sensibles:', re.findall(r'gmail|pucp\\.edu|usuario|[ocult"
"='utf-8').read()\nfor m in re.finditer(r'gmail|[oculto]|[oculto]',t,re."
'on_principal_claude_code.md; grep -niE "gmail|pucp\\\\.edu|usuario|[ocul'
'on_principal_claude_code.md; grep -niE "gmail|pucp\\\\.edu|usuario|[ocul'
'on_principal_claude_code.md; grep -niE "gmail|pucp\\\\.edu|usuario|[ocul'
'1], encoding="utf-8") if t.strip()] + ["gmail", "pucp.edu", "usuario",'
"eres; términos sensibles encontrados: ['gmail', '[oculto]', 'prompt_sn"
?? tarea_4/.gitignore
?? tarea_4/.mcp.json
?? tarea_4/evidencias_ia/
?? tarea_4/mcp/
?? tarea_4/pyproject.toml
?? tarea_4/uv.lock
```

</details>

<details><summary>🔧 Bash: Save the demo verification table and script as evidence</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad" && cp "$S/verificar_demo.py" evidencias_ia/mcp/verificar_demo.py && cat > evidencias_ia/mcp/03_verificacion_demo.md <<'EOF'
# Verificación independiente de la demostración del MCP

Las cifras que dio Claude Code con el MCP `bcrp` (ver `01_demo_mcp_claude_code.txt` y `02_demo_mcp_claude_code_completa.md`)
se recalcularon pidiendo los datos **directamente a las APIs**, sin pasar por `mcp/server.py`:

    python evidencias_ia/mcp/verificar_demo.py

Ejecutado el 8 de noviembre de 2026.

| Afirmación de la demo | Valor en la demo | Valor recalculado | Fuente | ¿Coincide? |
|---|---:|---:|---|:---:|
| Inflación 12 meses Lima, ene-2020 | 1.89 % | 1.888 % | BCRP API, PN01273PM | ✅ |
| Inflación 12 meses Lima, dic-2024 | 1.97 % | 1.966 % | BCRP API, PN01273PM | ✅ |
| Máximo 2020-2024 | 8.81 % (2022-06) | 8.813 % (Jun.2022) | BCRP API, PN01273PM | ✅ |
| Mínimo 2020-2024 | 1.60 % (2020-06) | 1.599 % (Jun.2020) | BCRP API, PN01273PM | ✅ |
| Promedio 2020-2024 (60 meses) | 4.47 % | 4.466 % | BCRP API, PN01273PM | ✅ |
| Cobre Cajamarca, mes máximo 2024 | 2,349.4 tm.f (2024-11) | 2,349.36 (Nov.2024) | BCRP API, RD12956DM | ✅ |
| Cobre Cajamarca, promedio mensual 2024 | 1,932.9 tm.f | 1,932.93 | BCRP API, RD12956DM | ✅ |
| Crecimiento promedio del PBI 2015-2024, Perú | 2.44 % | 2.44 % | Banco Mundial, NY.GDP.MKTP.KD.ZG | ✅ |
| Ídem, Chile | 2.06 % | 2.06 % | Banco Mundial | ✅ |
| Ídem, Colombia | 2.54 % | 2.54 % | Banco Mundial | ✅ |

Las diferencias son solo de redondeo: el MCP redondea a 2 decimales para presentar.

## Problemas encontrados en la demo

- **El prompt `/mcp__bcrp__informe` recibe solo la primera palabra del tema.** Con `tipo de cambio` llegó `tipo`.
  Claude Code separa los argumentos por espacios y el prompt tiene un solo argumento. El agente lo detectó y lo
  corrigió solo. Para temas de varias palabras hay que usar comillas (`/mcp__bcrp__informe "tipo de cambio"`).
- **`variacion_pct` no tiene sentido en series que ya son porcentajes**, como la inflación: en ese caso lo que
  sirve es `cambio`, en puntos porcentuales. La descripción de `resumen` lo advierte y el agente lo aplicó bien.
- **La fecha de fin del catálogo del BCRP va atrasada**, por ejemplo dic-2025, cuando la API ya tiene datos hasta
  sep-2026. Por eso el recurso la muestra como `fin_segun_catalogo`.
- **La primera orden de la demo fue `/mcp.bcrp`**, que no es un comando. Claude Code la interpretó como un pedido de
  probar el servidor y lo hizo, con una llamada a cada herramienta, al recurso y a las pruebas.
EOF
ls evidencias_ia evidencias_ia/mcp
```

Resultado:

```text
evidencias_ia:
00_sesion_principal_claude_code.md
exportar_conversacion.py
mcp

evidencias_ia/mcp:
01_demo_mcp_claude_code.txt
02_demo_mcp_claude_code_completa.md
03_verificacion_demo.md
verificar_demo.py
```

</details>

## 🤖 Claude

La demostración salió bien y la conversación ya está documentada en markdown.

**La demostración** cubre los 4 pasos que pide la tarea: identificó la serie, pidió los datos, hizo las cuentas con las herramientas y presentó cada cifra con su código, período y fuente. Usó las 4 herramientas, los 2 recursos y el prompt. Recalculé sus cifras pidiendo los datos directo a las APIs del BCRP y del Banco Mundial, sin pasar por el servidor, y **coinciden todas**. Hubo un solo problema: `/mcp__bcrp__informe tipo de cambio` le pasó al prompt solo "tipo". El agente lo detectó y lo corrigió; con comillas no ocurre.

**Lo que quedó en `evidencias_ia/`:**
- **`00_sesion_principal_claude_code.md`:** esta conversación completa, con tus mensajes textuales (incluido "no descargues los comentarios"), mis respuestas y cada herramienta con su entrada y su resultado, plegados.
- **`mcp/01_demo_mcp_claude_code.txt`:** tu `/export`.
- **`mcp/02_demo_mcp_claude_code_completa.md`:** la demostración con cada llamada a `bcrp` completa. El `/export` las muestra resumidas ("ctrl+o to expand").
- **`mcp/03_verificacion_demo.md`:** la tabla de verificación cifra por cifra y los problemas encontrados. Va con `verificar_demo.py` para repetirla.
- **`exportar_conversacion.py`:** convierte los registros `.jsonl` de Claude Code en estos markdown. Lo vuelvo a correr al cerrar cada parte para que el archivo siga al día.

**Lo que se oculta al exportar:**
- Los correos, tu usuario de Windows en las rutas y el identificador de tu cuenta.
- Los resultados donde aparecían los comentarios del issue, es decir, las entregas de tus compañeros.
- Los nombres de compañeros que habían quedado escritos en mis comandos. Se reemplazan por `[oculto]` usando una lista guardada fuera del repositorio, así que esos nombres no se publican.
- El razonamiento interno del modelo y los avisos del sistema, que no son parte de la conversación.

Revisé que ninguno de los dos markdown tenga correos ni ese identificador.

La Parte 1 está completa y todavía no hice commit. Son las 9:40 p. m. y quedan unas 2 h 20 min. ¿Hago el commit en `parte-1-mcp-bcrp` y empiezo a bajar los módulos 34 y 02 de la ENAHO para la Parte 2?

## 👤 Usuaria

ya esta todo. ya hice el commit push y cerré la branch parte-1 y la borre. ya todo está en el main. ahora he cambiado de branch. puedes ver si todo esta bien?

<details><summary>🔧 Bash: Check branches, main sync and committed tarea_4 files</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio" && git fetch --prune -q origin && echo "== rama actual"; git status -sb | head -5; echo "== ramas locales y remotas"; git branch -a; echo "== últimos commits (main)"; git log --oneline -6 origin/main; echo "== ¿rama actual vs origin/main?"; git rev-list --left-right --count origin/main...HEAD; echo "== archivos de tarea_4 en origin/main"; git ls-tree -r --name-only origin/main tarea_4/; echo "== ignorados presentes en disco"; git status --ignored --short tarea_4 | head
```

Resultado:

```text
== rama actual
## parte-2-skills-enaho...origin/parte-2-skills-enaho
?? tarea_4/mcp/
== ramas locales y remotas
  01_recoleccion
  02_llm_clasificador
  P1-Corpus-y-extraccion
  P2-Evaluacion
  P3-Reel
  main
  p1-obtencion-y-analisis-de-datos
  p2-dashboard
  parte-1-mcp-bcrp
* parte-2-skills-enaho
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
  remotes/origin/parte-2-skills-enaho
== últimos commits (main)
c3538a1 Merge pull request #17 from dgarcesg/parte-1-mcp-bcrp
a8cf028 #16 parte-1
588da4a Create placeholder.md
43fce66 Merge pull request #15 from dgarcesg/P3-Reel
0640326 README: enlace público del reel en Google Drive
3fc4834 Tarea 3 · Parte 3: reel con voz clonada, imágenes por escena y subtítulos
== ¿rama actual vs origin/main?
2	0
== archivos de tarea_4 en origin/main
tarea_4/.gitignore
tarea_4/.mcp.json
tarea_4/evidencias_ia/00_sesion_principal_claude_code.md
tarea_4/evidencias_ia/exportar_conversacion.py
tarea_4/evidencias_ia/mcp/01_demo_mcp_claude_code.txt
tarea_4/evidencias_ia/mcp/02_demo_mcp_claude_code_completa.md
tarea_4/evidencias_ia/mcp/03_verificacion_demo.md
tarea_4/evidencias_ia/mcp/verificar_demo.py
tarea_4/mcp/server.py
tarea_4/mcp/test_server.py
tarea_4/placeholder.md
tarea_4/pyproject.toml
tarea_4/uv.lock
== ignorados presentes en disco
?? tarea_4/mcp/
!! tarea_4/.claude/
!! tarea_4/.pytest_cache/
!! tarea_4/.venv/
```

</details>

<details><summary>🔧 Bash: Inspect the new branch base and ignore rules for .claude</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio" && echo "== HEAD"; git log --oneline -3 HEAD; echo "== tarea_4 en HEAD"; git ls-tree -r --name-only HEAD tarea_4/; echo "== main local vs origin/main"; git rev-list --left-right --count main...origin/main; echo "== untracked en detalle"; git status --short --untracked-files=all tarea_4 | head; echo "== .claude"; ls -la tarea_4/.claude; git check-ignore -v tarea_4/.claude/settings.local.json tarea_4/.claude/skills/limpiando-enaho/SKILL.md; echo "exit check-ignore skills: $?"; echo "== parte-1 fusionada en origin/main?"; git branch --merged origin/main | grep parte-1
```

Resultado:

```text
== HEAD
588da4a Create placeholder.md
43fce66 Merge pull request #15 from dgarcesg/P3-Reel
0640326 README: enlace público del reel en Google Drive
== tarea_4 en HEAD
tarea_4/placeholder.md
== main local vs origin/main
0	0
== untracked en detalle
?? tarea_4/mcp/__pycache__/server.cpython-314.pyc
?? tarea_4/mcp/__pycache__/test_server.cpython-314-pytest-9.2.0.pyc
?? tarea_4/mcp/datos/catalogo_bcrp.csv
== .claude
total 5
drwxr-xr-x 1 usuario 1049089  0 Nov  8 21:23 .
drwxr-xr-x 1 usuario 1049089  0 Nov  8 21:45 ..
-rw-r--r-- 1 usuario 1049089 95 Nov  8 21:23 settings.local.json
"C:\\Users\\usuario/.config/git/ignore":1:**/.claude/settings.local.json	tarea_4/.claude/settings.local.json
exit check-ignore skills: 0
== parte-1 fusionada en origin/main?
  parte-1-mcp-bcrp
```

</details>

<details><summary>🔧 Bash: Check which Part 1 files remain on disk in this branch</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio" && ls -la tarea_4 tarea_4/mcp; git log --oneline -2 origin/parte-2-skills-enaho; date
```

Resultado:

```text
tarea_4:
total 17
drwxr-xr-x 1 usuario 1049089 0 Nov  8 21:45 .
drwxr-xr-x 1 usuario 1049089 0 Nov  8 20:37 ..
drwxr-xr-x 1 usuario 1049089 0 Nov  8 21:23 .claude
drwxr-xr-x 1 usuario 1049089 0 Nov  8 20:58 .pytest_cache
drwxr-xr-x 1 usuario 1049089 0 Nov  8 20:57 .venv
drwxr-xr-x 1 usuario 1049089 0 Nov  8 21:45 mcp
-rw-r--r-- 1 usuario 1049089 2 Nov  8 20:37 placeholder.md

tarea_4/mcp:
total 12
drwxr-xr-x 1 usuario 1049089 0 Nov  8 21:45 .
drwxr-xr-x 1 usuario 1049089 0 Nov  8 21:45 ..
drwxr-xr-x 1 usuario 1049089 0 Nov  8 21:12 __pycache__
drwxr-xr-x 1 usuario 1049089 0 Nov  8 20:57 datos
588da4a Create placeholder.md
43fce66 Merge pull request #15 from dgarcesg/P3-Reel
Sun, Nov  8, 2026  9:48:05 PM
```

</details>

## 🤖 Claude

Lo de `main` está bien, pero **la rama nueva quedó desactualizada**.

**Lo que está bien:**
- `origin/main` tiene la Parte 1 completa con el merge del PR #17. Ahí están los 12 archivos de `tarea_4/`: servidor, pruebas, configuración y evidencias.
- Tu `main` local está igual a `origin/main`.
- No se subió nada que no debía: `.venv/`, `mcp/datos/` (el catálogo) y `.claude/settings.local.json` quedaron fuera.
- La futura carpeta `.claude/skills/` **no** queda ignorada. Lo comprobé porque tu `.gitignore` global ignora `settings.local.json`, pero no afecta a `skills/`.

**El problema:**
- `parte-2-skills-enaho` se creó desde `588da4a` ("Create placeholder.md"), es decir, **antes** del merge de la Parte 1. Está 2 commits atrás de `main`.
- Por eso, al cambiarte a esa rama, git quitó del disco `server.py`, `test_server.py`, `.mcp.json`, `pyproject.toml`, `evidencias_ia/` y los demás archivos de la Parte 1. **No se perdió nada**, todo está en `main`. Pero si empezamos la Parte 2 así, el PR va a chocar con lo que ya está en `main`.
- Lo que hoy figura como sin seguimiento (el catálogo y `__pycache__`) solo aparece porque el `.gitignore` tampoco está en esta rama.

**La solución** es adelantar la rama hasta `main`. Como la rama no tiene commits propios, no hay conflictos posibles:
```
git merge --ff-only origin/main
```

**Un detalle aparte:** borraste `parte-1-mcp-bcrp` en GitHub, pero la copia local sigue ahí. Como ya está fusionada, se puede borrar sin riesgo con `git branch -d parte-1-mcp-bcrp`.

¿Ejecuto los dos comandos? Solo cambian tu copia local, no hacen push. Son las 9:48 p. m.

## 👤 Usuaria

si porfa

<details><summary>🔧 Bash: Fast-forward branch to main, delete merged local branch, rerun tests</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio" && git merge --ff-only origin/main && git branch -d parte-1-mcp-bcrp && echo "== estado" && git status -sb | head -5 && git log --oneline -3 && ls -A tarea_4 tarea_4/mcp && cd tarea_4 && uv run pytest -q 2>&1 | tail -2
```

Resultado:

```text
Updating 588da4a..c3538a1
Fast-forward
 tarea_4/.gitignore                                 |   10 +
 tarea_4/.mcp.json                                  |   21 +
 .../00_sesion_principal_claude_code.md             | 2269 ++++++++++++++++++
 tarea_4/evidencias_ia/exportar_conversacion.py     |  135 ++
 .../evidencias_ia/mcp/01_demo_mcp_claude_code.txt  |  385 ++++
 .../mcp/02_demo_mcp_claude_code_completa.md        |  882 +++++++
 tarea_4/evidencias_ia/mcp/03_verificacion_demo.md  |   35 +
 tarea_4/evidencias_ia/mcp/verificar_demo.py        |   13 +
 tarea_4/mcp/server.py                              |  332 +++
 tarea_4/mcp/test_server.py                         |   91 +
 tarea_4/pyproject.toml                             |   17 +
 tarea_4/uv.lock                                    | 2397 ++++++++++++++++++++
 12 files changed, 6587 insertions(+)
 create mode 100644 tarea_4/.gitignore
 create mode 100644 tarea_4/.mcp.json
 create mode 100644 tarea_4/evidencias_ia/00_sesion_principal_claude_code.md
 create mode 100644 tarea_4/evidencias_ia/exportar_conversacion.py
 create mode 100644 tarea_4/evidencias_ia/mcp/01_demo_mcp_claude_code.txt
 create mode 100644 tarea_4/evidencias_ia/mcp/02_demo_mcp_claude_code_completa.md
 create mode 100644 tarea_4/evidencias_ia/mcp/03_verificacion_demo.md
 create mode 100644 tarea_4/evidencias_ia/mcp/verificar_demo.py
 create mode 100644 tarea_4/mcp/server.py
 create mode 100644 tarea_4/mcp/test_server.py
 create mode 100644 tarea_4/pyproject.toml
 create mode 100644 tarea_4/uv.lock
Deleted branch parte-1-mcp-bcrp (was a8cf028).
== estado
## parte-2-skills-enaho...origin/parte-2-skills-enaho [ahead 2]
c3538a1 Merge pull request #17 from dgarcesg/parte-1-mcp-bcrp
a8cf028 #16 parte-1
588da4a Create placeholder.md
tarea_4:
.claude
.gitignore
.mcp.json
.pytest_cache
.venv
evidencias_ia
mcp
placeholder.md
pyproject.toml
uv.lock

tarea_4/mcp:
__pycache__
datos
server.py
test_server.py
..........                                                               [100%]
10 passed in 11.56s
```

</details>

## 🤖 Claude

Ya está todo en orden:
- **`parte-2-skills-enaho` ahora está al día con `main`.** Volvieron a la carpeta los 12 archivos de la Parte 1 y las pruebas dan **10 passed**.
- **Borré la copia local de `parte-1-mcp-bcrp`.** Ya estaba fusionada.
- **No hice push.** Por eso git marca la rama `[ahead 2]` frente a su copia en GitHub, y se igualará con tu próximo push.

Son las 9:50 p. m. y quedan unas 2 h 10 min. Para la Parte 2, lo primero es bajar los módulos 34 y 02 de la ENAHO 2024 desde el INEI. Ocupan unos cuantos MB y van a `tarea_4/datos/`, que está en `.gitignore`. ¿Empiezo la descarga mientras armamos la Skill `limpiando-enaho`?

## 👤 Usuaria

si porfa

<details><summary>🔧 Bash: Download ENAHO 2024 modules 34 and 02 from INEI</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && mkdir -p datos && for m in 34 02; do curl -sSL --retry 3 -o "datos/966-Modulo$m.zip" "https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo$m.zip" & done; wait; ls -la datos; for f in datos/*.zip; do python -I -c "import zipfile,sys; z=zipfile.ZipFile(sys.argv[1]); [print(i.filename, i.file_size) for i in z.infolist()]" "$f"; done
```

Resultado:

```text
Command running in background with ID: bpllxm4iu. Output is being written to: ~\AppData\Local\Temp\claude\0e9f16fe359e3b06\57ecd584-3768-4852-a254-c84910c84d73\tasks\bpllxm4iu.output. You will be notified when it completes — do not poll that file or sleep while waiting. Read the file only if the user asks for progress, or if you need a line it prints before you can go on, such as a server's ready line or port.
Session cwd remains ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4; directory changes made by the backgrounded command do not apply to subsequent commands.
```

</details>

<details><summary>🔧 Read</summary>

```json
{
  "file_path": "C:\\Users\\usuario\\GITHUB\\Diplomatura PUCP 2026\\Data-Science-Python\\sessions\\16-skills-enaho\\README.md"
}
```

Resultado:

```text
1	# Sesión 16 · Skills de Claude Code: limpiar, graficar y mapear la ENAHO
2	
3	Qué es una skill de Claude Code, por qué conviene crearla dentro del repositorio y cómo se arma una que limpie la ENAHO
4	siempre de la misma forma. El proyecto son tres skills que trabajan juntas: una limpia los módulos del INEI, otra
5	hace gráficos y otra hace un mapa por departamento.
6	
7	**Slides de la clase:** https://claude.ai/artifact/X7H6PUvaWKde1epsYCJNze
8	
9	| Bloque | Duración | Qué se hace |
10	|---|---|---|
11	| Clase | 30 min | Qué es una skill, cómo se carga y se activa, por qué en Claude Code, el pipeline de la ENAHO y sus trampas |
12	| Proyecto | 45 min | Tres skills: `limpiando-enaho`, `graficando-enaho` y `mapeando-enaho`, validadas y probadas con y sin ellas |
13	| Presentaciones | 15 min | Cuatro repositorios al azar, tres minutos cada uno |
14	
15	## Contenido
16	
17	| Archivo | Qué hay |
18	|---|---|
19	| [`referencias/pobreza_departamento_2024.csv`](referencias/pobreza_departamento_2024.csv) | La pobreza 2024 de los 25 departamentos, para validar el mapa |
20	| [`referencias/mapa_pobreza_2024.png`](referencias/mapa_pobreza_2024.png) | Cómo debe verse el mapa |
21	
22	## Lo esencial de una skill
23	
24	- **Es una carpeta** con un `SKILL.md` obligatorio y, si hace falta, archivos de referencia y scripts. En un proyecto
25	  va en `.claude/skills/<nombre>/`. Así viaja con git y todo el equipo usa la misma.
26	- **`SKILL.md`** empieza con un bloque YAML con `name` (minúsculas, números y guiones; hasta 64 caracteres) y
27	  `description`. Debajo van las instrucciones, en menos de 500 líneas.
28	- **Carga progresiva.** Al inicio Claude solo ve `name` y `description` de cada skill, unos 100 tokens. El cuerpo se
29	  carga cuando la tarea lo pide, y los demás archivos solo si se usan. De un script solo entra al contexto lo que
30	  imprime.
31	- **Se activa sola** cuando un pedido coincide con la `description`, o a mano con `/nombre argumentos`. Dentro del
32	  archivo, `$ARGUMENTS` o `$0` toman los argumentos, y `${CLAUDE_SKILL_DIR}` es la carpeta de la skill.
33	- **La `description`** se escribe en tercera persona y dice qué hace y cuándo usarla, con las palabras que usaría
34	  quien la pide: ENAHO, INEI, pobreza, mapa.
35	- **Script o instrucción.** Lo que no se discute (llaves, filtros, uniones, validación) va en un script que la skill
36	  corre tal cual. Lo que requiere criterio va en el texto.
37	
38	### Por qué crearla en Claude Code
39	
40	1. Se ve
… [recortado: 9,754 caracteres más]
```

</details>

## 🤖 Claude

Los módulos se están bajando en segundo plano. Mientras tanto agrego las dependencias de la Parte 2 y reviso los archivos de referencia de la Sesión 16.

<details><summary>🔧 Bash: Add pyarrow and geopandas, inspect reference CSV and GeoJSON</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && uv add pyarrow geopandas 2>&1 | tail -2; R="~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions"; head -5 "$R/16-skills-enaho/referencias/pobreza_departamento_2024.csv"; wc -l "$R/16-skills-enaho/referencias/pobreza_departamento_2024.csv"; ls -la "$R/06-geoespacial/lab/Data/peru_departamental_simple.geojson"; python -I -c "
import json,sys; g=json.load(open(sys.argv[1],encoding='utf-8')); f=g['features']; print(len(f), list(f[0]['properties'].items())[:8]); print(sorted(x['properties']['FIRST_IDDP'] for x in f))" "$R/06-geoespacial/lab/Data/peru_departamental_simple.geojson"
```

Resultado:

```text
 + pyproj==3.8.0
 + shapely==2.2.0
ccdd,departamento,pobreza_pct
01,AMAZONAS,25.7
02,ANCASH,22.8
03,APURIMAC,24.0
04,AREQUIPA,15.8
26 ~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/16-skills-enaho/referencias/pobreza_departamento_2024.csv
-rw-r--r-- 1 usuario 1049089 139705 Oct 10 08:20 ~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/06-geoespacial/lab/Data/peru_departamental_simple.geojson
25 [('NOMBDEP', 'AMAZONAS'), ('COUNT', 84), ('FIRST_IDDP', '01'), ('HECTARES', 3930646.567)]
['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
```

</details>

<details><summary>🔧 Bash: Show download result and zip contents</summary>

```bash
cat "~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/tasks/bpllxm4iu.output"
```

Resultado:

```text
total 21228
drwxr-xr-x 1 usuario 1049089        0 Nov  8 21:50 .
drwxr-xr-x 1 usuario 1049089        0 Nov  8 21:50 ..
-rw-r--r-- 1 usuario 1049089  5793097 Nov  8 21:50 966-Modulo02.zip
-rw-r--r-- 1 usuario 1049089 15935617 Nov  8 21:50 966-Modulo34.zip
966-Modulo02/ 0
966-Modulo02/CED-01-200-2024.pdf 201079
966-Modulo02/Criterios para codificar Ocupaciones Peligrosas.pdf 395343
966-Modulo02/Diccionario2024.pdf 3940690
966-Modulo02/enaho01-2024-200.dta 10217755
966-Modulo02/enaho_tabla_ciuo_88.dta 349153
966-Modulo02/enaho_tabla_cno_2015.dta 56727
966-Modulo02/FichaTecnica.pdf 487444
966-Modulo34/ 0
966-Modulo34/ConstVarGasto-Metodologia actualizada.zip 24486
966-Modulo34/DefinicionValoresMonetariosBasedeDatos.pdf 254671
966-Modulo34/Diccionario2024.pdf 3940690
966-Modulo34/Estratificacion del Marco.pdf 207192
966-Modulo34/FichaTecnica.pdf 487444
966-Modulo34/sumaria-2024-12g.dta 29991565
966-Modulo34/Sumaria-2024-12g.pdf 2727028
966-Modulo34/sumaria-2024.dta 21219121
966-Modulo34/Sumaria-2024.pdf 2142849

[exited with code 0]
```

</details>

## 🤖 Claude

Los dos módulos ya se bajaron: 16 MB y 6 MB. Reviso las columnas y los tipos de las llaves antes de escribir la limpieza.

<details><summary>🔧 Bash: Inspect ENAHO columns, key types and sample rows</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && uv run python -c "
import zipfile, pandas as pd, sys
sys.stdout.reconfigure(encoding='utf-8')
for z, f, cols in [('datos/966-Modulo34.zip','966-Modulo34/sumaria-2024.dta',['conglome','vivienda','hogar','ubigeo','dominio','estrato','pobreza','factor07','mieperho']),
                   ('datos/966-Modulo02.zip','966-Modulo02/enaho01-2024-200.dta',['conglome','vivienda','hogar','codperso','ubigeo','p204','p205','p206','p207','p208a','facpob07','estrato','dominio'])]:
    with zipfile.ZipFile(z).open(f) as fh:
        df = pd.read_stata(fh, convert_categoricals=False)
    df.columns = df.columns.str.lower()
    print('==', f, df.shape); print([c for c in df.columns if not c.isascii() or c.startswith('a')][:5])
    print(df[[c for c in cols if c in df.columns]].dtypes.to_string())
    print(df[[c for c in cols if c in df.columns]].head(3).to_string())
    print('faltan:', [c for c in cols if c not in df.columns])
"
```

Resultado:

```text
== 966-Modulo34/sumaria-2024.dta (33691, 163)
['año']
conglome        str
vivienda        str
hogar           str
ubigeo          str
dominio        int8
estrato        int8
pobreza        int8
factor07    float32
mieperho       int8
  conglome vivienda hogar  ubigeo  dominio  estrato  pobreza   factor07  mieperho
0   015009      013    11  010101        4        4        3  79.816757         2
1   015009      047    11  010101        4        4        3  79.816757         3
2   015009      059    11  010101        4        4        3  79.816757         1
faltan: []
== 966-Modulo02/enaho01-2024-200.dta (117721, 40)
['año']
conglome        str
vivienda        str
hogar           str
codperso        str
ubigeo          str
p204        float64
p205        float64
p206        float64
p207        float64
p208a       float64
facpob07    float32
estrato        int8
dominio        int8
  conglome vivienda hogar codperso  ubigeo  p204  p205  p206  p207  p208a    facpob07  estrato  dominio
0   010651      013    11       01  150509   1.0   2.0   NaN   1.0   74.0  115.814941        4        2
1   010651      013    11       02  150509   1.0   2.0   NaN   2.0   70.0  115.814941        4        2
2   010651      013    11       03  150509   1.0   2.0   NaN   2.0   22.0  115.814941        4        2
faltan: []
```

</details>

## 🤖 Claude

Las llaves ya vienen como texto con sus ceros iniciales, y la columna del año llega como `año`. Escribo la Skill `limpiando-enaho`.

<details><summary>🔧 Write</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\.claude\skills\limpiando-enaho\scripts\limpiar.py

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


def leer(zip_path, contiene):
    """Lee el .dta del zip sin extraerlo. Las llaves llegan como texto: se verifica que conserven sus ceros."""
    if not zip_path.exists():
        sys.exit(f"ERROR: falta {zip_path.relative_to(RAIZ)}. Bájenlo del INEI: "
                 f"https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/{zip_path.name}")
    with zipfile.ZipFile(zip_path) as z:
        nombre = next(n for n in z.namelist() if n.lower().endswith(".dta") and contiene in n.lower())
        with z.open(nombre) as f:
            df = pd.read_stata(f, convert_categoricals=False)
    df.columns = df.columns.str.lower().str.replace("ñ", "n")  # "aÑo" llega como "año": queda "ano"
    return df.rename(columns={"ano": "anio"}), nombre


def tasa(df, columna, factor="facpob07"):
    """Porcentaje ponderado: suma de factores de quienes cumplen / suma de todos los factores."""
    return 100 * (df[columna] * df[factor]).sum() / df[factor].sum()


def indicadores(p):
    filas = []

    def agregar(grupo, categoria, codigo, d):
        filas.append({"grupo": grupo, "categoria": categoria, "codigo": codigo,
                      "pobreza_pct": round(tasa(d, "pobre"), 2), "pobreza_extrema_pct": round(tasa(d, "pobre_extremo"), 2),
                      "poblacion_expandida": round(d.facpob07.sum()), "n_muestra": len(d)})

    agregar("nacional", "Perú", "00", p)
    for area, d in p.groupby("area"):
        agregar("area", area, "", d)
    for sexo, d in p.groupby("sexo"):
        agregar("sexo", sexo, "", d)
    for edad, d in p.groupby("grupo_edad", observed=True):
        agregar("grupo_edad", edad, "", d)
    for cod, d in p.groupby("departamento"):
        agregar("departamento", DEPARTAMENTOS.get(cod, cod), cod, d)
    return pd.DataFrame(filas)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--anio", type=int, default=2024)
    anio = ap.parse_args().anio
    i
… [recortado: 6,363 caracteres más]
```

Resultado:

```text
File created successfully at: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\.claude\skills\limpiando-enaho\scripts\limpiar.py (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>🔧 Bash: Run the cleaning script and show validation and indicators ⚠️ error</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && sed -i '/hogares = hogares\[~hogares.columns.isin(\[\])\]/d' .claude/skills/limpiando-enaho/scripts/limpiar.py && PYTHONIOENCODING=utf-8 uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024; echo "exit: $?"; head -40 salidas/indicadores.csv 2>/dev/null
```

Resultado:

```text
Exit code 1
Validación ENAHO 2024 · limpiando-enaho
============================================================
Hogares: 966-Modulo34/sumaria-2024-12g.dta | Personas: 966-Modulo02/enaho01-2024-200.dta

[FALLA] Llaves de hogares como texto, con sus ceros iniciales: conglome: 6 caracteres, vivienda: 3 caracteres, hogar: 2 caracteres, ubigeo: 6 caracteres
[FALLA] Llaves de personas como texto, con sus ceros iniciales: conglome: 6 caracteres, vivienda: 3 caracteres, hogar: 2 caracteres, codperso: 2 caracteres
[PASA] Una fila por hogar en la sumaria (llaves únicas): 33,691 hogares (referencia 33,691)
[PASA] Una fila por persona en miembros (llaves + codperso únicas): 117,721 filas en el módulo 02
[PASA] Residentes habituales: 108,664 (referencia 108,664)
[PASA] La unión no duplica personas: 108,664 filas tras unir
[PASA] Toda persona encuentra su hogar: 0 personas sin hogar en la sumaria
[PASA] Los 25 códigos territoriales (01-25), Lima y Callao separados: 25 códigos; faltan []; sobran []
[PASA] Factor de expansión facpob07 completo y positivo: 0 vacíos; población expandida 34,147,768
[PASA] Población expandida plausible para el Perú (30-37 millones): 34.15 millones
[PASA] Pobreza monetaria nacional (personas × facpob07) a ±0.1 pp de 27.6 %: 27.53 %
[PASA] (informativa) Pobreza con la sumaria (factor07 × mieperho) a ±0.1 pp de 27.6 %: 27.58 % (cálculo alternativo)
[PASA] (informativa) Pobreza urbano a ±0.1 pp de 24.8 %: 24.74 %
[FALLA] (informativa) Pobreza rural a ±0.1 pp de 39.3 %: 39.44 %
[PASA] (informativa) La ponderación importa (promedio simple ≠ ponderado): simple 25.61 % vs ponderado 27.53 %: sin factor se sesga el resultado

Resultado: 13 de 15 verificaciones aprobadas; 2 esenciales fallidas.
PROCESO DETENIDO: no se guardó la base. Revisen las verificaciones marcadas FALLA.
exit: 1
```

</details>

<details><summary>🔧 Bash: Compute urban/rural poverty with household weights</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && uv run python -c "
import zipfile, pandas as pd
with zipfile.ZipFile('datos/966-Modulo34.zip').open('966-Modulo34/sumaria-2024.dta') as f: h=pd.read_stata(f, convert_categoricals=False)
h['pobre']=(h.pobreza<=2); h['w']=h.factor07*h.mieperho; h['urb']=h.estrato<=5
for u,d in h.groupby('urb'): print('sumaria urbano' if u else 'sumaria rural', round(100*(d.pobre*d.w).sum()/d.w.sum(),2))
print('dtype', h.conglome.dtype, pd.api.types.is_string_dtype(h.conglome))
"
```

Resultado:

```text
sumaria rural 39.3
sumaria urbano 24.81
dtype str True
```

</details>

<details><summary>🔧 Bash: Fix file selection and dtype check, rerun cleaning</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && python - <<'EOF'
from pathlib import Path
p = Path(".claude/skills/limpiando-enaho/scripts/limpiar.py"); s = p.read_text(encoding="utf-8")
cambios = [
 ('''def leer(zip_path, contiene):
    """Lee el .dta del zip sin extraerlo. Las llaves llegan como texto: se verifica que conserven sus ceros."""''',
  '''def leer(zip_path, archivo):
    """Lee el .dta del zip sin extraerlo. Las llaves llegan como texto: se verifica que conserven sus ceros."""'''),
 ('''        nombre = next(n for n in z.namelist() if n.lower().endswith(".dta") and contiene in n.lower())''',
  '''        # el nombre exacto: el módulo 34 trae también sumaria-AAAA-12g.dta, que no es la que se usa
        nombre = next((n for n in z.namelist() if n.lower().endswith("/" + archivo)), None)
        if nombre is None:
            sys.exit(f"ERROR: {zip_path.name} no contiene {archivo}.")'''),
 ('''    hogares, f_h = leer(DATOS / f"{codigo}-Modulo34.zip", "sumaria")''',
  '''    hogares, f_h = leer(DATOS / f"{codigo}-Modulo34.zip", f"sumaria-{anio}.dta")'''),
 ('''    personas, f_p = leer(DATOS / f"{codigo}-Modulo02.zip", "200")''',
  '''    personas, f_p = leer(DATOS / f"{codigo}-Modulo02.zip", f"enaho01-{anio}-200.dta")'''),
 ('''        ok = all(df[c].dtype == object and df[c].str.len().eq(n).all() for c, n in ancho.items())''',
  '''        ok = all(pd.api.types.is_string_dtype(df[c]) and df[c].str.len().eq(n).all() for c, n in ancho.items())'''),
 ('''    for area in ("urbano", "rural"):
        valor = tasa(p[p.urbano == (area == "urbano")], "pobre")
        check(False, f"Pobreza {area} a ±{TOLERANCIA_PP} pp de {REFERENCIA[area]} %",
              abs(valor - REFERENCIA[area]) <= TOLERANCIA_PP, f"{valor:.2f} %")''',
  '''    # La referencia urbano/rural del INEI se reproduce con la sumaria (hogares × miembros); con personas y facpob07
    # las cifras se mueven ~0.1 pp por la unidad de ponderación. Se informan las dos.
    hog["urbano"] = hog.estrato <= 5
    for area in ("urbano", "rural"):
        es = area == "urbano"
        en_personas, en_sumaria = tasa(p[p.urbano == es], "pobre"), tasa(hog[hog.urbano == es], "pobre", "peso")
        check(False, f"Pobreza {area} (sumaria) a ±{TOLERANCIA_PP} pp de {REFERENCIA[area]} %",
              abs(en_sumaria - REFERENCIA[area]) <= TOLERANCIA_PP,
              f"{en_sumaria:.2f} % con la sumaria; {en_personas:.2f} % con personas y facpob07")'''),
]
for a, b in cambios:
    assert s.count(a) == 1, a[:80]; s = s.replace(a, b)
p.write_text(s, encoding="utf-8")
EOF
PYTHONIOENCODING=utf-8 uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024; echo "exit: $?"; cat salidas/indicadores.csv
```

Resultado:

```text
Validación ENAHO 2024 · limpiando-enaho
============================================================
Hogares: 966-Modulo34/sumaria-2024.dta | Personas: 966-Modulo02/enaho01-2024-200.dta

[PASA] Llaves de hogares como texto, con sus ceros iniciales: conglome: 6 caracteres, vivienda: 3 caracteres, hogar: 2 caracteres, ubigeo: 6 caracteres
[PASA] Llaves de personas como texto, con sus ceros iniciales: conglome: 6 caracteres, vivienda: 3 caracteres, hogar: 2 caracteres, codperso: 2 caracteres
[PASA] Una fila por hogar en la sumaria (llaves únicas): 33,691 hogares (referencia 33,691)
[PASA] Una fila por persona en miembros (llaves + codperso únicas): 117,721 filas en el módulo 02
[PASA] Residentes habituales: 108,664 (referencia 108,664)
[PASA] La unión no duplica personas: 108,664 filas tras unir
[PASA] Toda persona encuentra su hogar: 0 personas sin hogar en la sumaria
[PASA] Los 25 códigos territoriales (01-25), Lima y Callao separados: 25 códigos; faltan []; sobran []
[PASA] Factor de expansión facpob07 completo y positivo: 0 vacíos; población expandida 34,147,768
[PASA] Población expandida plausible para el Perú (30-37 millones): 34.15 millones
[PASA] Pobreza monetaria nacional (personas × facpob07) a ±0.1 pp de 27.6 %: 27.53 %
[PASA] (informativa) Pobreza con la sumaria (factor07 × mieperho) a ±0.1 pp de 27.6 %: 27.58 % (cálculo alternativo)
[PASA] (informativa) Pobreza urbano (sumaria) a ±0.1 pp de 24.8 %: 24.81 % con la sumaria; 24.74 % con personas y facpob07
[PASA] (informativa) Pobreza rural (sumaria) a ±0.1 pp de 39.3 %: 39.30 % con la sumaria; 39.44 % con personas y facpob07
[PASA] (informativa) La ponderación importa (promedio simple ≠ ponderado): simple 25.61 % vs ponderado 27.53 %: sin factor se sesga el resultado

Resultado: 15 de 15 verificaciones aprobadas; 0 esenciales fallidas.
Base guardada: salidas/personas_2024.parquet (108,664 personas, 27 columnas) y salidas/indicadores.csv.
exit: 0
grupo,categoria,codigo,pobreza_pct,pobreza_extrema_pct,poblacion_expandida,n_muestra
nacional,Perú,00,27.53,5.5,34147768,108664
area,Rural,,39.44,15.6,6486385,36071
area,Urbana,,24.74,3.13,27661382,72593
sexo,Hombre,,27.37,5.37,16453003,52587
sexo,Mujer,,27.68,5.62,17694764,56077
grupo_edad,0-14,,37.52,8.59,7941994,26489
grupo_edad,15-29,,25.97,4.5,7512400,23122
grupo_edad,30-44,,27.87,5.59,6689119,20648
grupo_edad,45-64,,21.15,3.61,7803731,24735
grupo_edad,65 y más,,22.74,4.81,4200522,13670
departamento,Amazonas,01,26.08,6.
… [recortado: 1,184 caracteres más]
```

</details>

<details><summary>🔧 Skill</summary>

```json
{
  "skill": "dataviz"
}
```

Resultado:

```text
Launching skill: dataviz
```

</details>

<details><summary>🔧 Bash: Read sequential ramp and ink colors from the palette</summary>

```bash
D="~/AppData/Local/Temp/claude/bundled-skills/2.1.318/df3468254d83dc20a36d202c51969d1d/dataviz/references"; grep -n -i -A12 "sequential" "$D/palette.md" | head -50; grep -n -i -B1 -A3 "surface\|ink\|text token\|muted" "$D/palette.md" | head -40
```

Resultado:

```text
100:## Sequential hue
101-
102:Default single hue: **blue**, light->dark. When two sequential contexts appear at
103-once, the second takes the next categorical slot's hue (orange), each as its own
104-one-hue ramp.
105-
106-| step | hex | step | hex | step | hex | step | hex |
107-|---|---|---|---|---|---|---|---|
108-| 100 | `#cde2fb` | 250 | `#86b6ef` | 400 | `#3987e5` | 550 | `#1c5cab` |
109-| 150 | `#b7d3f6` | 300 | `#6da7ec` | 450 | `#2a78d6` | 600 | `#184f95` |
110-| 200 | `#9ec5f4` | 350 | `#5598e7` | 500 | `#256abf` | 650 | `#104281` |
111-| | | | | | | 700 | `#0d366b` |
112-
113:The full 100->700 range is for **sequential** encoding (continuous magnitude -
114-heatmaps, choropleths) where the lightest step means "near zero" and is allowed
115-to recede toward the surface. For an **ordinal** ramp (discrete ordered marks -
116-funnel stages, tiers - validated with `--ordinal`), the step nearest the surface
117-must still clear 2:1: on light, start no lighter than **step 250** (`#86b6ef`,
118-2.06:1); on dark, go no darker than **step 600** (`#184f95`, 2.15:1).
119-
120-## Diverging pair
121-
122-**blue <-> red** - warm/cool poles that read as opposite. Neutral midpoint is gray
123-(light `#f0efec`, dark `#383835`). Equal step count per arm. (blue<->aqua was
124-rejected - both cool, the midpoint doesn't read as "nothing".)
125-
17-  color-scheme: light;
18:  --surface-1:      #fcfcfb;   /* chart surface */
19-  --text-primary:   #0b0b0b;
20-  --text-secondary: #52514e;
21-  --series-1:       #2a78d6;   /* categorical slot 1 */
--
26-    color-scheme: dark;
27:    --surface-1:      #1a1a19;
28-    --text-primary:   #f0efec;
29-    --text-secondary: #c3c2b7;
30-    --series-1:       #3987e5;
--
34-  color-scheme: dark;
35:  --surface-1:      #1a1a19;
36-  --text-primary:   #f0efec;
37-  --text-secondary: #c3c2b7;
38-  --series-1:       #3987e5;
--
49-Both modes are selected. The dark column is the same eight hues stepped for the
50:dark surface, not a separate palette:
51-
52-| Slot | Hue | Light | Dark |
53-|------|-----|-------|------|
--
75-light; CVD 4.8 dark). Three light-mode slots (magenta, yellow, aqua)
76:sit below 3:1 contrast on the light surface: the **relief rule** applies (ship
77-visible direct labels or the table view). The dark steps were chosen for the
78:dark band (OKLCH L ~ 0.48-0.67, >= 3:1 on the dark surface) and validated as a
79-set. (Ordering history: adopted July 2026 for its more harmonious opening -
80-the same eight hues
… [recortado: 556 caracteres más]
```

</details>

<details><summary>🔧 Write</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\.claude\skills\graficando-enaho\scripts\graficar.py

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
            ax.text(v + s.max() * 0.01, b.get_y() + b.get_height() / 2, f"{v:.1f}", va="center", fontsize=8, color=TINTA)
        ax.text(nacional, len(s) - 0.3, f" Perú: {nacional:.1f} %", color=TINTA_2, fontsize=8, va="bottom")
    else:
        barras = ax.bar(etiquetas, s.values, color=AZUL, width=0.6)
        ax.axhline(nacional, color=REFERENCIA, lw=1, ls="--", zorder=0)
        ax.set
… [recortado: 1,915 caracteres más]
```

Resultado:

```text
File created successfully at: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\.claude\skills\graficando-enaho\scripts\graficar.py (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>🔧 Write</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\.claude\skills\mapeando-enaho\scripts\mapa.py

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

    # comparación con la referencia de la Sesión 16 (una cifra decimal por departamento)
    ref = pd.read_csv(REFERENCIA, dtype={"ccdd": str})
    comp = pobreza.merge(ref, left_on="departamento", right_on="ccdd", how="outer", validate="1:1",
                         suffixes=("", "_ref"))
    comp["calculado"] = comp.pobreza_pct.round(1)
    comp["diferencia_pp"] = (comp.calculado - comp.pobreza_pct_ref).round(2)
    comp["coincide"] = comp.diferencia_pp.abs() <= TOLERANCIA_PP
    comp[["departamento", "nombre", "calculado", "pobreza_pct_ref", "diferencia_pp", "coincide"]].rename(
        columns={"pobreza_pct_ref": "referencia_sesion16"}).to_csv(
        RAIZ / "salidas" / "comparacion_mapa_referencia.csv", index=False, encoding="utf-8")

    # el mapa
    vmax = math.ceil(m.pobreza_pct.max() / 10) * 10
    cmap = LinearSegmentedColormap.from_list("azules", AZULES)
    fig, ax = plt.subpl
… [recortado: 2,353 caracteres más]
```

Resultado:

```text
File created successfully at: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\.claude\skills\mapeando-enaho\scripts\mapa.py (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>🔧 Bash: Generate all charts and the map, then list outputs</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && mkdir -p .claude/skills/mapeando-enaho/referencia && cp "~/GITHUB/Diplomatura PUCP 2026/Data-Science-Python/sessions/16-skills-enaho/referencias/pobreza_departamento_2024.csv" .claude/skills/mapeando-enaho/referencia/ && PYTHONIOENCODING=utf-8 uv run .claude/skills/graficando-enaho/scripts/graficar.py --por todos 2>&1 | grep -v "^ " | head -40; PYTHONIOENCODING=utf-8 uv run .claude/skills/mapeando-enaho/scripts/mapa.py; ls figuras mapas; date
```

Resultado:

```text
figuras\pobreza_por_area_2024.png · La pobreza monetaria rural (39.4 %) supera a la urbana (24.7 %) en 14.7 puntos
Rural     39.44
Urbana    24.74 
Perú: 27.53

figuras\pobreza_por_sexo_2024.png · La pobreza monetaria es casi igual en mujeres (27.7 %) y hombres (27.4 %)
Mujer     27.68
Hombre    27.37 
Perú: 27.53

figuras\pobreza_por_edad_2024.png · El grupo de 0-14 años tiene la pobreza monetaria más alta (37.5 %)
0-14        37.52
15-29       25.97
30-44       27.87
45-64       21.15
65 y más    22.74 
Perú: 27.53

figuras\pobreza_por_departamento_2024.png · Cajamarca tiene la pobreza monetaria más alta (45.0 %) y Ica la más baja (5.9 %)
Ica               5.91
Moquegua         10.88
Madre de Dios    11.14
Lambayeque       14.05
Arequipa         15.77
Cusco            18.54
Junín            18.61
San Martín       21.99
Áncash           22.88
Tacna            23.88
Apurímac         24.09
Amazonas         26.08
Tumbes           26.60
Lima             26.89
Ucayali          27.12
La Libertad      30.07
Piura            31.81
Ayacucho         33.04
Huancavelica     33.61
Callao           33.77
Pasco            39.28
mapas\pobreza_departamento_2024.png: 25 de 25 departamentos unidos por código (ubigeo[:2] = FIRST_IDDP).
Más alta: Cajamarca 44.99 % · más baja: Ica 5.91 %
Comparación con la referencia de la Sesión 16: 16 de 25 coinciden a ±0.1 pp (máxima diferencia 0.50 pp) → salidas/comparacion_mapa_referencia.csv
AVISO: no coinciden:           nombre  calculado  pobreza_pct_ref
0       Amazonas       26.1             25.7
4       Ayacucho       33.0             32.8
8   Huancavelica       33.6             33.4
9        Huánuco       39.5             39.0
14          Lima       26.9             27.1
15        Loreto       42.6             43.0
18         Pasco       39.3             39.0
20          Puno       40.4             39.9
23        Tumbes       26.6             26.9
figuras:
pobreza_por_area_2024.png
pobreza_por_departamento_2024.png
pobreza_por_edad_2024.png
pobreza_por_sexo_2024.png

mapas:
pobreza_departamento_2024.png
Sun, Nov  8, 2026  9:56:04 PM
```

</details>

<details><summary>🔧 Bash: Compare reference with household-weighted department poverty</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && uv run python -c "
import zipfile, pandas as pd
with zipfile.ZipFile('datos/966-Modulo34.zip').open('966-Modulo34/sumaria-2024.dta') as f: h=pd.read_stata(f, convert_categoricals=False)
h['d']=h.ubigeo.str[:2]; h['w']=h.factor07*h.mieperho; h['x']=(h.pobreza<=2)*h.w
s=(100*h.groupby('d').x.sum()/h.groupby('d').w.sum()).round(1)
ref=pd.read_csv('.claude/skills/mapeando-enaho/referencia/pobreza_departamento_2024.csv',dtype={'ccdd':str}).set_index('ccdd').pobreza_pct
d=(s-ref).round(2); print('coinciden a 0.1:', (d.abs()<=0.1).sum(), 'de 25; max', d.abs().max())
"
```

Resultado:

```text
coinciden a 0.1: 25 de 25; max 0.0
```

</details>

<details><summary>🔧 Bash: Add household-weighted indicators and dual reference comparison</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && python - <<'EOF'
from pathlib import Path
p = Path(".claude/skills/limpiando-enaho/scripts/limpiar.py"); s = p.read_text(encoding="utf-8")
cambios = [
 ('''def indicadores(p):
    filas = []

    def agregar(grupo, categoria, codigo, d):
        filas.append({"grupo": grupo, "categoria": categoria, "codigo": codigo,
                      "pobreza_pct": round(tasa(d, "pobre"), 2), "pobreza_extrema_pct": round(tasa(d, "pobre_extremo"), 2),
                      "poblacion_expandida": round(d.facpob07.sum()), "n_muestra": len(d)})

    agregar("nacional", "Perú", "00", p)
    for area, d in p.groupby("area"):
        agregar("area", area, "", d)
    for sexo, d in p.groupby("sexo"):
        agregar("sexo", sexo, "", d)
    for edad, d in p.groupby("grupo_edad", observed=True):
        agregar("grupo_edad", edad, "", d)
    for cod, d in p.groupby("departamento"):
        agregar("departamento", DEPARTAMENTOS.get(cod, cod), cod, d)
    return pd.DataFrame(filas)''',
  '''def indicadores(p, hog):
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
    return pd.DataFrame(filas)'''),
 ('''        indicadores(p).to_csv(''', '''        indicadores(p, hog).to_csv('''),
]
for a, b in cambios:
    assert s.count(a) == 1, a[:60]; s = s.replace(a, b)
p.write_text(s, encoding="utf-8")

q = Path(".claude/skills/mapeando-enaho/scripts/mapa.py"); s = q.read_text(encoding="utf-8")
cambios = [
 ('''    # comparación con la referencia de la Sesión 16 (una cifra decimal por departamento)
    ref = pd.read_csv(REFERENCIA, dtype={"ccdd": str})
    comp = pobreza.merge(ref, left_on="departamento", right_on="ccdd", how="outer", validate="1:1",
                         suffixes=("", "_ref"))
    comp["calculado"] = comp.pobreza_pct.round(1)
    comp["diferencia_pp"] = (comp.calculado - comp.pobreza_pct_ref).round(2)
    comp["coincide"] = comp.diferencia_pp.abs() <= TOLERANCIA_PP
    comp[["departamento", "nombre", "calculado", "pobreza_pct_ref", "diferencia_pp", "coincide"]].rename(
        columns={"pobreza_pct_ref": "referencia_sesion16"}).to_csv(
        RAIZ / "salidas" / "comparacion_mapa_referencia.csv", index=False, encoding="utf-8")''',
  '''    # Comparación con la referencia de la Sesión 16 (una cifra decimal por departamento). Esa referencia se calculó
    # con la sumaria (hogares × factor07 × mieperho), así que se compara con los dos métodos: el del mapa (personas ×
    # facpob07) y el de la sumaria, que limpiando-enaho deja en salidas/indicadores.csv.
    ref = pd.read_csv(REFERENCIA, dtype={"ccdd": str})
    ind = pd.read_csv(RAIZ / "salidas" / "indicadores.csv", dtype={"codigo": str}).query("grupo == 'departamento'")
    comp = pobreza.merge(ref,
… [recortado: 2,359 caracteres más]
```

Resultado:

```text
Resultado: 15 de 15 verificaciones aprobadas; 0 esenciales fallidas.
Base guardada: salidas/personas_2024.parquet (108,664 personas, 27 columnas) y salidas/indicadores.csv.
grupo,categoria,codigo,pobreza_pct,pobreza_extrema_pct,pobreza_pct_sumaria,poblacion_expandida,n_muestra
nacional,Perú,00,27.53,5.5,27.58,34147768,108664
area,Rural,,39.44,15.6,39.3,6486385,36071
area,Urbana,,24.74,3.13,24.81,27661382,72593
mapas\pobreza_departamento_2024.png: 25 de 25 departamentos unidos por código (ubigeo[:2] = FIRST_IDDP).
Más alta: Cajamarca 44.99 % · más baja: Ica 5.91 %
Referencia de la Sesión 16 (calculada con la sumaria): con el mismo método coinciden 25 de 25 a ±0.1 pp (máx. 0.10); con personas × facpob07, la del mapa, 16 de 25 (máx. 0.50 pp, por la unidad de ponderación) → salidas/comparacion_mapa_referencia.csv
```

</details>

## 🤖 Claude

Ahora los gráficos y el mapa. Los abro para revisar que las etiquetas no se encimen.

<details><summary>🔧 Read</summary>

```json
{
  "file_path": "C:\\Users\\usuario\\GITHUB\\Diplomatura PUCP 2026\\diplomado_python_intermedio\\tarea_4\\mapas\\pobreza_departamento_2024.png"
}
```

Resultado:

```text
[imagen]
```

</details>

<details><summary>🔧 Read</summary>

```json
{
  "file_path": "C:\\Users\\usuario\\GITHUB\\Diplomatura PUCP 2026\\diplomado_python_intermedio\\tarea_4\\figuras\\pobreza_por_area_2024.png"
}
```

Resultado:

```text
[imagen]
```

</details>

<details><summary>🔧 Bash: Wrap titles, fix accent and national label, regenerate charts</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && python - <<'EOF'
from pathlib import Path
p = Path(".claude/skills/graficando-enaho/scripts/graficar.py"); s = p.read_text(encoding="utf-8")
cambios = [
 ('import argparse\nimport sys\n', 'import argparse\nimport sys\nimport textwrap\n'),
 ('GRUPOS = {"area": "area", "sexo": "sexo", "edad": "grupo_edad", "departamento": "nombre_departamento"}',
  'GRUPOS = {"area": "area", "sexo": "sexo", "edad": "grupo_edad", "departamento": "nombre_departamento"}\n'
  'NOMBRE_GRUPO = {"area": "área", "sexo": "sexo", "edad": "grupo de edad", "departamento": "departamento"}'),
 ('''        ax.text(nacional, len(s) - 0.3, f" Perú: {nacional:.1f} %", color=TINTA_2, fontsize=8, va="bottom")\n''', ''),
 ('''        ax.text(len(s) - 0.5, nacional, f"Perú: {nacional:.1f} %", color=TINTA_2, fontsize=8, ha="right",
                va="bottom")\n''', ''),
 ('''    fig.suptitle(titulo(por, s, etiqueta), x=0.02,''', '''    fig.suptitle(textwrap.fill(titulo(por, s, etiqueta), 70), x=0.02,'''),
 ('''    ax.set_title(f"% de personas en {etiqueta} por {por if por != 'edad' else 'grupo de edad'}, Perú 2024 · "
                 "línea punteada: promedio nacional", loc="left", fontsize=9, color=TINTA_2)''',
  '''    ax.set_title(f"% de personas en {etiqueta} por {NOMBRE_GRUPO[por]}, Perú 2024 · línea punteada: promedio "
                 f"nacional ({nacional:.1f} %)", loc="left", fontsize=9, color=TINTA_2)'''),
]
for a, b in cambios:
    assert s.count(a) == 1, a[:70]; s = s.replace(a, b)
p.write_text(s, encoding="utf-8")
EOF
PYTHONIOENCODING=utf-8 uv run .claude/skills/graficando-enaho/scripts/graficar.py --por todos 2>&1 | grep "png"
```

Resultado:

```text
figuras\pobreza_por_area_2024.png · La pobreza monetaria rural (39.4 %) supera a la urbana (24.7 %) en 14.7 puntos
figuras\pobreza_por_sexo_2024.png · La pobreza monetaria es casi igual en mujeres (27.7 %) y hombres (27.4 %)
figuras\pobreza_por_edad_2024.png · El grupo de 0-14 años tiene la pobreza monetaria más alta (37.5 %)
figuras\pobreza_por_departamento_2024.png · Cajamarca tiene la pobreza monetaria más alta (45.0 %) y Ica la más baja (5.9 %)
```

</details>

<details><summary>🔧 Read</summary>

```json
{
  "file_path": "C:\\Users\\usuario\\GITHUB\\Diplomatura PUCP 2026\\diplomado_python_intermedio\\tarea_4\\figuras\\pobreza_por_departamento_2024.png"
}
```

Resultado:

```text
[imagen]
```

</details>

## 🤖 Claude

Corto también el subtítulo para que no se salga del margen y escribo los `SKILL.md` y el `reference.md`.

<details><summary>🔧 Bash: Wrap chart subtitles and regenerate charts</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && python - <<'EOF'
from pathlib import Path
p = Path(".claude/skills/graficando-enaho/scripts/graficar.py"); s = p.read_text(encoding="utf-8")
a = '''    ax.set_title(f"% de personas en {etiqueta} por {NOMBRE_GRUPO[por]}, Perú 2024 · línea punteada: promedio "
                 f"nacional ({nacional:.1f} %)", loc="left", fontsize=9, color=TINTA_2)'''
b = '''    ax.set_title(textwrap.fill(f"% de personas en {etiqueta} por {NOMBRE_GRUPO[por]}, Perú 2024 · línea punteada: "
                               f"promedio nacional ({nacional:.1f} %)", 75 if horizontal else 95),
                 loc="left", fontsize=9, color=TINTA_2)'''
assert s.count(a) == 1; p.write_text(s.replace(a, b), encoding="utf-8")
EOF
PYTHONIOENCODING=utf-8 uv run .claude/skills/graficando-enaho/scripts/graficar.py --por todos 2>&1 | grep -c png
```

Resultado:

```text
4
```

</details>

<details><summary>🔧 Write</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\.claude\skills\limpiando-enaho\SKILL.md

---
name: limpiando-enaho
description: Limpia y valida los microdatos de la ENAHO 2024 del INEI (módulo 34 sumaria y módulo 02 miembros). Filtra residentes habituales, une personas y hogares, pondera con los factores de expansión y calcula la pobreza monetaria nacional, urbana/rural, por sexo, edad y departamento. Úsala cuando pidan limpiar, preparar o validar la ENAHO, cifras de pobreza del Perú en 2024, o cuando otra skill necesite salidas/personas_2024.parquet.
argument-hint: [año]
---

# Limpiar la ENAHO

Todo se corre desde la raíz del proyecto (`tarea_4/`).

1. Comprueba que existan `datos/966-Modulo34.zip` y `datos/966-Modulo02.zip` (966 = ENAHO 2024). Si faltan, bájalos:

   ˋˋˋbash
   curl -L -o datos/966-Modulo34.zip https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip
   curl -L -o datos/966-Modulo02.zip https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo02.zip
   ˋˋˋ

2. Corre exactamente, sin reescribir el pipeline:

   ˋˋˋbash
   uv run ${CLAUDE_SKILL_DIR}/scripts/limpiar.py --anio 2024
   ˋˋˋ

   Si piden otro año, el script lo rechaza: dilo, no inventes cifras.

3. Lee `salidas/validacion.txt`. Si el script termina con código 1 o alguna verificación esencial dice `FALLA`,
   **detente** y reporta cuál falló. Nunca ajustes resultados para que coincidan con la referencia.

4. Responde con las cifras de `salidas/indicadores.csv`, que ya están ponderadas:
   - `pobreza_pct`: personas × `facpob07` (la principal, 27.53 % nacional).
   - `pobreza_pct_sumaria`: hogares × `factor07 × mieperho`, la forma en que publica el INEI (27.58 %). Úsala si piden
     la cifra oficial o al comparar con referencias del INEI; existe solo para nacional, área y departamento.

   Para otros cortes usa `salidas/personas_2024.parquet` y pondera siempre con `facpob07`. Nunca un promedio simple.

5. Cita así: «INEI, ENAHO 2024 (módulos 34 y 02), cálculo propio con limpiar.py». Son asociaciones descriptivas: no
   afirmes causas.

6. Antes de usar una variable que no está en la base, o si dudas de un código, lee `reference.md`.

```

Resultado:

```text
File created successfully at: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\.claude\skills\limpiando-enaho\SKILL.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>🔧 Write</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\.claude\skills\limpiando-enaho\reference.md

# Referencia: ENAHO 2024 en `limpiando-enaho`

## Archivos de origen

| Módulo | Archivo dentro del zip | Una fila por | Filas | Factor |
|---|---|---|---:|---|
| 34, sumaria | `966-Modulo34/sumaria-2024.dta` (no `sumaria-2024-12g.dta`) | hogar | 33,691 | `factor07` |
| 02, miembros | `966-Modulo02/enaho01-2024-200.dta` | persona | 117,721 | `facpob07` |

Llaves del hogar: `conglome` (6), `vivienda` (3), `hogar` (2), como texto con sus ceros. La persona agrega `codperso` (2).
`ubigeo` tiene 6 dígitos: los dos primeros son el departamento (el mismo código que `FIRST_IDDP` en el mapa).

## Reglas del pipeline

- **Residente habitual:** `((p204 == 1) & (p205 == 2)) | ((p204 == 2) & (p206 == 1))`. Es miembro del hogar y no estuvo
  ausente 30 días o más, o no es miembro pero estuvo presente 30 días o más. Quedan 108,664 personas.
- **Unión:** personas (m) con sumaria (1) por las tres llaves, `validate="m:1"`. `ubigeo`, `estrato` y `dominio` salen
  de la sumaria.
- **Área:** `estrato <= 5` urbana; 6 a 8 rural.
- **Pobreza** (`pobreza` en la sumaria): 1 pobre extremo, 2 pobre no extremo, 3 no pobre. `pobre = pobreza <= 2`.

## Columnas de `salidas/personas_2024.parquet`

| Columna | Qué es |
|---|---|
| `conglome`, `vivienda`, `hogar`, `codperso` | Llaves |
| `ubigeo`, `departamento`, `nombre_departamento` | Ubicación; `departamento = ubigeo[:2]` |
| `estrato`, `urbano`, `area` | Estrato (1-8), urbano (bool), «Urbana»/«Rural» |
| `dominio` | 1-3 costa, 4-6 sierra, 7 selva, 8 Lima Metropolitana |
| `p207`, `sexo` | 1 hombre, 2 mujer |
| `p208a`, `edad`, `grupo_edad` | Edad en años y grupos 0-14, 15-29, 30-44, 45-64, 65 y más |
| `pobreza`, `pobre`, `pobre_extremo` | Código del INEI e indicadores 0/1 |
| `facpob07` | Factor de expansión de la persona: **úsenlo para toda cifra de personas** |
| `factor07`, `mieperho`, `peso_hogar` | Factor del hogar, miembros del hogar y su producto |
| `linea`, `gashog2d`, `inghog2d` | Línea de pobreza, gasto e ingreso anual del hogar (soles) |

## Valores de referencia (INEI, 2024)

| Cifra | Referencia | Este pipeline |
|---|---:|---:|
| Pobreza nacional | 27.6 % | 27.53 % personas · 27.58 % sumaria |
| Urbana / rural | 24.8 % / 39.3 % | 24.74 / 39.44 personas · 24.81 / 39.30 sumaria |
| Pobreza extrema | 5.5 % | 5.50 % |
| Residentes habituales | 108,664 | 108,664 |

La diferencia entre las dos ponderaciones (≤ 0.15 pp en el agregado, hasta 0.5 pp por departamento) viene de la unidad:
`facpob07` es de la persona y `factor07 × mieperho` reparte el factor del hogar entre sus miembros. Las dos son
estimaciones ponderadas válidas; el INEI publica con la segunda.

```

Resultado:

```text
File created successfully at: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\.claude\skills\limpiando-enaho\reference.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>🔧 Write</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\.claude\skills\graficando-enaho\SKILL.md

---
name: graficando-enaho
description: Hace gráficos de barras de la pobreza monetaria o extrema de la ENAHO 2024 (INEI) por área urbana/rural, sexo, grupo de edad o departamento, ponderados con el factor de expansión, con título analítico, unidades y fuente. Úsala cuando pidan graficar, visualizar o comparar la pobreza del Perú entre grupos o regiones con la ENAHO.
argument-hint: [area|sexo|edad|departamento|todos] [pobreza|pobreza_extrema]
---

# Graficar la ENAHO

Todo se corre desde la raíz del proyecto (`tarea_4/`).

1. Si no existe `salidas/personas_2024.parquet`, usa primero la skill `limpiando-enaho` y verifica que su validación
   haya pasado.

2. Traduce el pedido a las opciones del script:

   | El pedido habla de… | `--por` |
   |---|---|
   | urbano y rural, campo y ciudad, área | `area` |
   | hombres y mujeres, sexo, género | `sexo` |
   | niños, jóvenes, adultos mayores, edad | `edad` |
   | regiones, departamentos, territorios | `departamento` |
   | «los gráficos de pobreza», sin precisar | `todos` |

   `--indicador pobreza_extrema` si piden pobreza extrema; si no, `pobreza` (monetaria).

3. Corre exactamente:

   ˋˋˋbash
   uv run ${CLAUDE_SKILL_DIR}/scripts/graficar.py --por <grupo> --indicador <indicador>
   ˋˋˋ

   El script pondera con `facpob07` y guarda `figuras/<indicador>_por_<grupo>_2024.png` a 200 dpi. Cumple las reglas:
   un solo color, barras desde cero y ordenadas (la edad conserva su orden), el valor en cada barra, una línea con el
   promedio nacional, un título que dice qué muestra con las cifras, el período, la unidad (% de personas) y la fuente.

4. Responde con la ruta de la figura y las cifras que imprime el script. No calcules nada a mano y no describas
   diferencias como causas.

5. Si piden otro tipo de gráfico o un grupo que el script no tiene, dilo y propón el más cercano. No improvises un
   gráfico sin ponderar.

```

Resultado:

```text
File created successfully at: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\.claude\skills\graficando-enaho\SKILL.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>🔧 Write</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\.claude\skills\mapeando-enaho\SKILL.md

---
name: mapeando-enaho
description: Hace el mapa coroplético de la pobreza monetaria por departamento del Perú con la ENAHO 2024 (INEI), uniendo indicadores y geometrías por código territorial (ubigeo y FIRST_IDDP), con los 25 departamentos y Lima y Callao por separado. Úsala cuando pidan un mapa, una distribución territorial o regional de la pobreza.
---

# Mapear la ENAHO

Todo se corre desde la raíz del proyecto (`tarea_4/`).

1. Si no existe `salidas/personas_2024.parquet`, usa primero la skill `limpiando-enaho` y verifica que su validación
   haya pasado.

2. Corre exactamente:

   ˋˋˋbash
   uv run ${CLAUDE_SKILL_DIR}/scripts/mapa.py
   ˋˋˋ

   El script:
   - pondera la pobreza de cada departamento con `facpob07`;
   - une por código, nunca por nombre: `ubigeo[:2]` con `FIRST_IDDP`, como texto de 2 dígitos;
   - exige 25 unidades con dato, con Lima (15) y Callao (07) separados, y si no, se detiene con error;
   - pinta una escala de un solo tono, de claro a oscuro desde 0, con la unidad en la leyenda;
   - guarda `mapas/pobreza_departamento_2024.png`;
   - compara con la referencia de la Sesión 16 (`referencia/pobreza_departamento_2024.csv`) y guarda
     `salidas/comparacion_mapa_referencia.csv`.

   Si no está el GeoJSON, lo baja del repositorio del curso a `datos/`.

3. Al responder, informa la ruta del mapa, el departamento más alto y el más bajo y el resultado de la comparación.
   La referencia se calculó con la sumaria (hogares × `factor07 × mieperho`): con ese método coinciden los 25; con
   personas × `facpob07`, el del mapa, hay diferencias de hasta 0.5 pp por la unidad de ponderación. Explícalo así;
   no lo corrijas a mano.

4. Las diferencias territoriales son descriptivas: no afirmes causas.

```

Resultado:

```text
File created successfully at: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\.claude\skills\mapeando-enaho\SKILL.md (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Claude

Las tres Skills quedaron listas. Para la demostración borro la base limpia, así se ve que el mapa necesita correr antes la limpieza.

<details><summary>🔧 Bash: Remove clean base for the demo and list Part 2 files</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && rm -f salidas/personas_2024.parquet && mkdir -p evidencias_ia/skills && find .claude/skills -type f | sort && ls salidas figuras mapas && git -C .. status --short && date
```

Resultado:

```text
.claude/skills/graficando-enaho/scripts/graficar.py
.claude/skills/graficando-enaho/SKILL.md
.claude/skills/limpiando-enaho/reference.md
.claude/skills/limpiando-enaho/scripts/limpiar.py
.claude/skills/limpiando-enaho/SKILL.md
.claude/skills/mapeando-enaho/referencia/pobreza_departamento_2024.csv
.claude/skills/mapeando-enaho/scripts/mapa.py
.claude/skills/mapeando-enaho/SKILL.md
figuras:
pobreza_por_area_2024.png
pobreza_por_departamento_2024.png
pobreza_por_edad_2024.png
pobreza_por_sexo_2024.png

mapas:
pobreza_departamento_2024.png

salidas:
comparacion_mapa_referencia.csv
indicadores.csv
validacion.txt
 M tarea_4/pyproject.toml
 M tarea_4/uv.lock
?? tarea_4/.claude/
?? tarea_4/figuras/
?? tarea_4/mapas/
?? tarea_4/salidas/
Sun, Nov  8, 2026 10:00:00 PM
```

</details>

<details><summary>🔧 Bash: Ignore the derived ENAHO parquet in git</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && printf '\n# Base de personas que arma limpiando-enaho: son microdatos derivados y se regeneran con limpiar.py\nsalidas/*.parquet\n' >> .gitignore && tail -3 .gitignore
```

Resultado:

```text
# Base de personas que arma limpiando-enaho: son microdatos derivados y se regeneran con limpiar.py
salidas/*.parquet
```

</details>

## 🤖 Claude

La Parte 2 está construida y las tres Skills se probaron a mano: los gráficos y el mapa salen sin errores.

| Skill | Qué hace | Resultado |
|---|---|---|
| `limpiando-enaho` | Lee los dos zip, filtra residentes, une con `validate="m:1"`, pondera y valida | **15 de 15 verificaciones aprobadas**: 27.53 % (dentro de ±0.1 pp de 27.6), 108,664 residentes, 25 códigos, sin duplicados y 34.15 millones de población expandida. Si algo esencial falla, se detiene y no guarda la base; lo vimos funcionar en el primer intento. |
| `graficando-enaho` | Barras por área, sexo, edad o departamento | 4 figuras en `figuras/`. Cada título dice el resultado, por ejemplo "La pobreza monetaria rural (39.4 %) supera a la urbana (24.7 %) en 14.7 puntos". |
| `mapeando-enaho` | Mapa unido por `ubigeo[:2]` = `FIRST_IDDP` | 25 de 25 departamentos con Lima y Callao separados. Va de 5.9 % en Ica a 45.0 % en Cajamarca. |

**Un hallazgo para el informe:** las referencias de la Sesión 16 para urbano/rural y por departamento se calcularon por hogares (`factor07 × mieperho`). Con ese método coinciden los **25 departamentos** y el 24.8 / 39.3 urbano/rural. Con personas y `facpob07` hay diferencias de hasta 0.5 pp, que vienen de la unidad de ponderación. La limpieza calcula los dos métodos y el mapa compara ambos con la referencia.

Agregué `salidas/*.parquet` al `.gitignore`, porque son microdatos derivados que se regeneran con el script. Para la demostración ya borré la base limpia.

## Demostración de las Skills (unos 5 min)
Abre una sesión **nueva** en `tarea_4/` para que cargue las Skills:
```
cd "~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4"
claude
```
1. `Haz un mapa de la pobreza monetaria por departamento con ENAHO 2024.` Es el ejemplo del enunciado: como no hay base, debería correr `limpiando-enaho` y luego `mapeando-enaho`.
2. `Grafica la pobreza entre hombres y mujeres` muestra la activación con lenguaje natural.
3. `/graficando-enaho area` muestra la invocación individual.
4. `/export evidencias_ia/skills/01_demo_skills_claude_code.txt`

Cuando permita aprobar los comandos `uv run …`, elige *"Yes, and don't ask again"*. Mientras tanto, si quieres, preparo la Parte 3. ¿Cuál será tu pregunta de investigación? Una opción coherente con lo que ya tenemos: *¿Cómo evolucionaron la inflación y la producción minera entre 2020 y 2024, y qué brechas territoriales mostraba la pobreza en 2024, en particular en Cajamarca, el departamento más pobre y gran productor de cobre?*

## 👤 Usuaria

ya está

<details><summary>🔧 Bash: Check demo export, regenerated outputs and new transcript</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && ls -la evidencias_ia/skills/ salidas/ figuras/ mapas/; ls -lt ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/*.jsonl | head -3; date
```

Resultado:

```text
evidencias_ia/skills/:
total 12
drwxr-xr-x 1 usuario 1049089    0 Nov  8 22:16 .
drwxr-xr-x 1 usuario 1049089    0 Nov  8 21:59 ..
-rw-r--r-- 1 usuario 1049089 6474 Nov  8 22:16 01_demo_skills_claude_code.txt

figuras/:
total 420
drwxr-xr-x 1 usuario 1049089      0 Nov  8 21:55 .
drwxr-xr-x 1 usuario 1049089      0 Nov  8 21:56 ..
-rw-r--r-- 1 usuario 1049089  77855 Nov  8 22:13 pobreza_por_area_2024.png
-rw-r--r-- 1 usuario 1049089 162129 Nov  8 21:59 pobreza_por_departamento_2024.png
-rw-r--r-- 1 usuario 1049089  90993 Nov  8 21:59 pobreza_por_edad_2024.png
-rw-r--r-- 1 usuario 1049089  78635 Nov  8 22:12 pobreza_por_sexo_2024.png

mapas/:
total 268
drwxr-xr-x 1 usuario 1049089      0 Nov  8 21:56 .
drwxr-xr-x 1 usuario 1049089      0 Nov  8 21:56 ..
-rw-r--r-- 1 usuario 1049089 267018 Nov  8 22:09 pobreza_departamento_2024.png

salidas/:
total 1484
drwxr-xr-x 1 usuario 1049089       0 Nov  8 22:08 .
drwxr-xr-x 1 usuario 1049089       0 Nov  8 21:56 ..
-rw-r--r-- 1 usuario 1049089     989 Nov  8 22:09 comparacion_mapa_referencia.csv
-rw-r--r-- 1 usuario 1049089    1924 Nov  8 22:09 indicadores.csv
-rw-r--r-- 1 usuario 1049089 1497088 Nov  8 22:09 personas_2024.parquet
-rw-r--r-- 1 usuario 1049089    1974 Nov  8 22:09 validacion.txt
-rw-r--r-- 1 usuario 1049089 2081836 Nov  8 22:16 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/7e4804b7-5171-4706-a0a7-128ed2a04bb3.jsonl
-rw-r--r-- 1 usuario 1049089  872654 Nov  8 21:44 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/7bfebfb8-d42f-472c-8fb2-7a5f78500694.jsonl
Sun, Nov  8, 2026 10:19:26 PM
```

</details>

<details><summary>🔧 Read</summary>

```json
{
  "file_path": "C:\\Users\\usuario\\GITHUB\\Diplomatura PUCP 2026\\diplomado_python_intermedio\\tarea_4\\evidencias_ia\\skills\\01_demo_skills_claude_code.txt"
}
```

Resultado:

```text
1	 ▐▛███▛█   Claude Code v2.1.319
2	▝▜██████▀  Opus 5.5 · Claude Pro
3	 ▝▝   ▝▝   ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea…
4	
5	
6	❯ Haz un mapa de la pobreza monetaria por departamento con ENAHO 2024           
7	
8	● Skill(mapeando-enaho)
9	  ⎿  Successfully loaded skill
10	
11	  Ran 2 shell commands (ctrl+o to expand)
12	
13	● salidas/personas_2024.parquet no existe, aunque validacion.txt dice que se
14	  guardó. Así que antes corro la skill de limpieza.
15	
16	● Skill(limpiando-enaho)
17	  ⎿  Successfully loaded skill
18	
19	  Ran 1 shell command (ctrl+o to expand)
20	
21	● El script falló con código 1 por la consola de Windows (cp1252), que no puede
22	  imprimir «≠», no por una validación. Voy a revisar en qué punto ocurrió antes
23	  de seguir.
24	
25	  Ran 1 shell command (ctrl+o to expand)
26	
27	● El fallo fue en el print final, tras pasar las validaciones y escribir los
28	  archivos. Vuelvo a correr el script con la consola en UTF-8 para confirmar
29	  código 0, y después el mapa, que también imprime «→».
30	
31	  Read 1 file, ran 3 shell commands, wrote 1 memory (ctrl+o to expand)
32	
33	● Hice el mapa: mapas/pobreza_departamento_2024.png. Están los 25 departamentos,
34	  con Lima (15) y Callao (07) por separado. Los datos y las formas del mapa se
35	  unieron por el código del departamento (los dos primeros dígitos del ubigeo),
36	  no por el nombre.
37	
38	  Resultados (% de personas en pobreza monetaria, ponderado con facpob07):
39	  - Más alto: Cajamarca, 45,0 %. Le siguen Loreto (42,6 %) y Puno (40,4 %).
40	  - Más bajo: Ica, 5,9 %. Le siguen Moquegua (10,9 %) y Madre de Dios (11,1 %).
41	  - Nacional: 27,53 %.
42	
43	  Comparación con la referencia de la Sesión 16
44	  (salidas/comparacion_mapa_referencia.csv):
45	  - La referencia se calculó por hogares (factor07 × mieperho). Con ese mismo
46	    método coinciden los 25 departamentos (diferencia máxima de 0,1 puntos).
47	  - El mapa usa otro método, personas × facpob07. Con él coinciden 16 de 25, y
48	    la diferencia más grande es de 0,5 puntos (Huánuco y Puno).
49	  - Esas diferencias salen de usar personas en vez de hogares como unidad de
50	    ponderación, no de un error. No ajusté nada a mano.
51	
52	  Un problema al correrlo: la tabla de personas (salidas/personas_2024.parquet)
53	  no existía, así que primero corrí la limpieza: pasó las 15 verificaciones.
54	  - Esa primera corrida terminó con código 1, pero no por los datos. La consola
55	    de Window
… [recortado: 3,610 caracteres más]
```

</details>

<details><summary>🔧 Bash: List skills and tools invoked during the Skills demo</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && python -I -c "
import json,sys; sys.stdout.reconfigure(encoding='utf-8')
for l in open(sys.argv[1],encoding='utf-8'):
    d=json.loads(l)
    if d.get('type')=='assistant':
        for b in d['message']['content']:
            if b.get('type')=='tool_use':
                i=b['input']; print('TOOL', b['name'], (i.get('skill') or i.get('command') or i.get('file_path') or '')[:140])
    if d.get('type')=='user' and isinstance(d['message']['content'],str): print('USER', d['message']['content'][:100].replace(chr(10),' '))
" ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/7e4804b7-5171-4706-a0a7-128ed2a04bb3.jsonl
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Bash: Force UTF-8 output, fix title wrap and label overlap, rerun all</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && python - <<'EOF'
from pathlib import Path
base = Path(".claude/skills")
for ruta, ancla in [("limpiando-enaho/scripts/limpiar.py", "def main():\n"),
                    ("graficando-enaho/scripts/graficar.py", "def main():\n"),
                    ("mapeando-enaho/scripts/mapa.py", "def main():\n")]:
    p = base / ruta; s = p.read_text(encoding="utf-8")
    nuevo = ancla + "    sys.stdout.reconfigure(encoding=\"utf-8\")  # la consola de Windows (cp1252) no imprime ≠ ni →\n"
    assert s.count(ancla) == 1 and "reconfigure" not in s, ruta
    p.write_text(s.replace(ancla, nuevo), encoding="utf-8")
p = base / "graficando-enaho/scripts/graficar.py"; s = p.read_text(encoding="utf-8")
cambios = [
 ('''            ax.text(v + s.max() * 0.01, b.get_y() + b.get_height() / 2, f"{v:.1f}", va="center", fontsize=8, color=TINTA)''',
  '''            ax.text(v + s.max() * 0.01, b.get_y() + b.get_height() / 2, f"{v:.1f}", va="center", fontsize=8, color=TINTA,
                    bbox=CAJA)'''),
 ('''            ax.text(b.get_x() + b.get_width() / 2, v + s.max() * 0.015, f"{v:.1f} %", ha="center", fontsize=9,
                    color=TINTA)''',
  '''            ax.text(b.get_x() + b.get_width() / 2, v + s.max() * 0.015, f"{v:.1f} %", ha="center", fontsize=9,
                    color=TINTA, bbox=CAJA)'''),
 ('''    fig.suptitle(textwrap.fill(titulo(por, s, etiqueta), 70), x=0.02, ha="left", fontsize=12,''',
  '''    fig.suptitle(textwrap.fill(titulo(por, s, etiqueta), 70 if horizontal else 85), x=0.02, ha="left",
                 fontsize=12 if horizontal else 11,'''),
 ('''FUENTE = (''', '''CAJA = {"facecolor": FONDO, "edgecolor": "none", "pad": 1}  # el valor tapa la línea del promedio si se cruzan
FUENTE = ('''),
]
for a, b in cambios:
    assert s.count(a) == 1, a[:70]; s = s.replace(a, b)
p.write_text(s, encoding="utf-8")
EOF
grep -n "suptitle" -A1 .claude/skills/graficando-enaho/scripts/graficar.py; for s in "limpiando-enaho/scripts/limpiar.py --anio 2024" "graficando-enaho/scripts/graficar.py --por todos" "mapeando-enaho/scripts/mapa.py"; do uv run .claude/skills/$s > /dev/null; echo "$s -> exit $?"; done
```

Resultado:

```text
87:    fig.suptitle(textwrap.fill(titulo(por, s, etiqueta), 70 if horizontal else 85), x=0.02, ha="left",
88-                 fontsize=12 if horizontal else 11, fontweight="bold", color=TINTA)
limpiando-enaho/scripts/limpiar.py --anio 2024 -> exit 0
graficando-enaho/scripts/graficar.py --por todos -> exit 0
mapeando-enaho/scripts/mapa.py -> exit 0
```

</details>

## 🤖 Claude

Los tres scripts terminan con código 0 sin necesidad de `PYTHONIOENCODING`. Reviso el gráfico por sexo.

<details><summary>🔧 Read</summary>

```json
{
  "file_path": "C:\\Users\\usuario\\GITHUB\\Diplomatura PUCP 2026\\diplomado_python_intermedio\\tarea_4\\figuras\\pobreza_por_sexo_2024.png"
}
```

Resultado:

```text
[imagen]
```

</details>

<details><summary>🔧 Bash: Read the memory the demo session wrote about UTF-8</summary>

```bash
M="~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/memory"; ls "$M"; cat "$M"/enaho-skills-utf8-consola*.md; tail -2 "$M/MEMORY.md"
```

Resultado:

```text
avisar-profe-antes-de-actualizar-repo.md
ds-python-up-kernel.md
enaho-skills-utf8-consola.md
MEMORY.md
no-descargar-comentarios-issue.md
no-rescrape-no-overwrite-notebook.md
repo-nuevo-solo-dashboard.md
streamlit-cloud-falla-apps-recientes.md
tarea3-alcance-2016.md
---
name: enaho-skills-utf8-consola
description: "Scripts de las skills ENAHO (limpiar.py, mapa.py) caen al imprimir en la consola cp1252; correrlos con PYTHONIOENCODING=utf-8"
metadata:
  node_type: memory
  type: project
  originSessionId: 7e4804b7-5171-4706-a0a7-128ed2a04bb3
  modified: 2026-11-09T03:09:33.478Z
---

En tarea_4, `limpiar.py` y `mapa.py` (skills limpiando-enaho / mapeando-enaho) imprimen «≠» y «→». En la consola de Windows (cp1252) el `print` final lanza UnicodeEncodeError y el script termina con código 1, aunque las validaciones hayan pasado y los archivos ya se hayan escrito (8-nov-2026).

**Why:** el código 1 parece una validación fallida y la skill pide detenerse ante código 1; en realidad es solo la codificación de la consola.

**How to apply:** correr los scripts con `PYTHONIOENCODING=utf-8 uv run ...` (no reescribir el pipeline). Si aun así sale código 1, revisar `salidas/validacion.txt` para ver si alguna verificación dice FALLA.
- [No descargar comentarios del issue](no-descargar-comentarios-issue.md) — leer solo el enunciado; los comentarios son entregas de compañeros
- [Skills ENAHO: consola UTF-8](enaho-skills-utf8-consola.md) — limpiar.py/mapa.py caen al imprimir en cp1252; usar PYTHONIOENCODING=utf-8
```

</details>

<details><summary>🔧 Bash: Remove stale memory and export Skills demo transcript</summary>

```bash
M="~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/memory"; rm "$M/enaho-skills-utf8-consola.md" && sed -i '/enaho-skills-utf8-consola.md/d' "$M/MEMORY.md" && tail -1 "$M/MEMORY.md"; cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad" && python -I evidencias_ia/exportar_conversacion.py ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/7e4804b7-5171-4706-a0a7-128ed2a04bb3.jsonl evidencias_ia/skills/02_demo_skills_claude_code_completa.md "Demostración de las Skills de ENAHO desde Claude Code (registro completo)" "$S/ocultar.txt" && grep -c "Skill" evidencias_ia/skills/02_demo_skills_claude_code_completa.md; date
```

Resultado:

```text
- [No descargar comentarios del issue](no-descargar-comentarios-issue.md) — leer solo el enunciado; los comentarios son entregas de compañeros
evidencias_ia/skills/02_demo_skills_claude_code_completa.md: 268 l�neas
6
Sun, Nov  8, 2026 10:21:20 PM
[This command modified 1 file you've previously read: ..\..\..\..\.claude\projects\C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio\memory\MEMORY.md. Call Read before editing.]
```

</details>

<details><summary>🔧 Edit</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py
--- antes ---
# TODO 4 · Recursos.
--- después ---
FIGURAS = AQUI.parent / "figuras"
COLORES = ["#2a78d6", "#d95f02", "#1b9e77", "#7570b3"]  # orden fijo: la primera serie siempre en azul


@mcp.tool(annotations={"readOnlyHint": False, "openWorldHint": True})
def graficar_serie(codigos: str, desde: str, hasta: str, titulo: str | None = None) -> dict:
    """Grafica una o hasta cuatro series del BCRP en un mismo eje y guarda el PNG en figuras/. Úsenla cuando pidan
    un gráfico de una serie del BCRP (inflación, tipo de cambio, PBI, producción minera…) para un informe.

    codigos: uno o varios códigos separados por ";" (por ejemplo "PN01273PM" o "PN01273PM;PN01271PM"); todos deben
    tener la misma frecuencia y la misma unidad, porque nunca se usan dos ejes. Las fechas se escriben como en serie.
    titulo: lo que muestra el gráfico (un hallazgo, no solo el tema); si falta, se usa el nombre de la serie.
    Devuelve la ruta del PNG, el primer y último dato, el máximo y el mínimo de cada serie, y las fuentes.
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    lista = [c.strip() for c in codigos.replace(",", ";").split(";") if c.strip()]
    if not 1 <= len(lista) <= 4:
        raise ToolError("Pasen entre 1 y 4 códigos separados por ';'.")
    datos = [serie(c, desde, hasta) for c in lista]
    if len({d["frecuencia"] for d in datos}) > 1:
        raise ToolError("Las series tienen frecuencias distintas: grafíquenlas por separado.")
    unidades = {_unidad(_fila(c)) for c in lista}
    if len(unidades) > 1:
        raise ToolError(f"Las series tienen unidades distintas ({', '.join(map(str, unidades))}): un gráfico con dos "
                        "ejes engaña. Grafíquenlas por separado.")
    fig, ax = plt.subplots(figsize=(8, 4.5), facecolor="#fcfcfb")
    ax.set_facecolor("#fcfcfb")
    resumenes = []
    for d, color in zip(datos, COLORES):
        if not d["datos"]:
            raise ToolError(f"La serie {d['codigo']} no tiene datos entre {desde} y {hasta}.")
        x = pd.to_datetime([p["periodo"].replace("-T", "-Q") for p in d["datos"]])
        y = [p["valor"] for p in d["datos"]]
        ax.plot(x, y, color=color, lw=2, label=f"{d['nombre']} ({d['codigo']})")
        maximo, minimo = max(d["datos"], key=lambda p: p["valor"]), min(d["datos"], key=lambda p: p["valor"])
        resumenes.append({"codigo": d["codigo"], "nombre": d["nombre"], "primero": d["datos"][0],
                          "ultimo": d["datos"][-1], "maximo": maximo, "minimo": minimo, "fuente": d["fuente"]})
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    ax.tick_params(colors="#52514e", labelsize=9)
    ax.set_ylabel(next(iter(unidades)) or "", color="#52514e")
    ax.grid(axis="y", color="#e4e3df", lw=0.6)
    if len(datos) > 1:
        ax.legend(frameon=False, fontsize=8, loc="best")
    fig.suptitle(titulo or datos[0]["nombre"], x=0.02, ha="left", fontsize=11, fontweight="bold", color="#0b0b0b")
    ax.set_title(f"{desde} a {hasta} · {datos[0]['frecuencia'].lower()}", loc="left", fontsize=9, color="#52514e")
    fig.text(0.02, 0.01, "Fuente: BCRP, series estadísticas (" + ", ".join(lista) + "). Elaboración propia.",
             fontsize=7, color="#52514e")
    fig.tight_layout(rect=(0, 0.03, 1, 0.95))
    FIGURAS.mkdir(exist_ok=True)
    ruta = FIGURAS / f"bcrp_{'_'.join(lista)}_{desde}_{hasta}.png"
    fig.savefig(ruta, dpi=200, facecolor="#fcfcfb")
    plt.close(fig)
    return {"archivo": str(ruta.relative_to(AQUI.parent)).replace("\\", "/"), "series": resumenes}


# TODO 4 · Recursos.
```

Resultado:

```text
The file ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\mcp\server.py has been updated successfully.
```

</details>

<details><summary>🔧 Bash: Test the new chart tool and rerun the test suite</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad" && cat > "$S/probar_grafico.py" <<'EOF'
import asyncio, sys
sys.path.insert(0, "mcp")
from fastmcp import Client
from server import mcp
async def main():
    async with Client(mcp) as c:
        r = await c.call_tool("graficar_serie", {"codigos": "PN01273PM", "desde": "2020-01", "hasta": "2024-12",
                                                 "titulo": "Prueba"})
        print(r.data["archivo"], r.data["series"][0]["maximo"])
        try:
            await c.call_tool("graficar_serie", {"codigos": "PN01273PM;RD12956DM", "desde": "2020-01", "hasta": "2024-12"})
        except Exception as e:
            print("error esperado:", str(e)[:120])
asyncio.run(main())
EOF
uv run python "$S/probar_grafico.py" 2>&1 | grep -v "^ \|│\|╭\|╰" | tail -4; rm -f figuras/bcrp_PN01273PM_2020-01_2024-12.png; uv run pytest -q 2>&1 | tail -1
```

Resultado:

```text
[11/08/26 22:22:28] Error calling tool 'graficar_serie'                        
figuras/bcrp_PN01273PM_2020-01_2024-12.png {'periodo': '2022-06', 'valor': 8.81263294388897}
Binary file (standard input) matches
10 passed in 13.45s
```

</details>

<details><summary>🔧 Bash: Remove clean base and create Part 3 and 4 folders</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && rm -f salidas/personas_2024.parquet && mkdir -p informes evidencias_ia/integracion evaluacion && ls; date
```

Resultado:

```text
datos
evaluacion
evidencias_ia
figuras
informes
mapas
mcp
placeholder.md
pyproject.toml
salidas
uv.lock
Sun, Nov  8, 2026 10:23:25 PM
```

</details>

## 🤖 Claude

Todo listo para la Parte 3, que es la ejecución integrada. Son las 10:23 p. m.

## Ejecución integrada (unos 5–8 min)
Abre una **sesión nueva** en `tarea_4/`, para que cargue `graficar_serie`, y pega este pedido. Si prefieres otra pregunta, cambia solo la primera línea.

```
Pregunta de investigación: ¿Cómo evolucionaron la inflación y la producción de cobre del Perú entre 2020 y 2024, y qué brechas territoriales y entre áreas urbana y rural mostraba la pobreza monetaria en 2024, en particular en Cajamarca, el departamento con más pobreza y gran productor de cobre?

Actúa como agente de investigación:
1. Escribe primero un plan breve: qué series del BCRP y qué indicadores de la ENAHO necesitas, y con qué herramienta MCP o skill obtendrás cada uno.
2. BCRP, solo con el MCP bcrp: busca las series con buscar_series, saca las cifras con resumen (inflación a 12 meses de Lima, 2020-2024; producción de cobre de Cajamarca 2020-2024, cuya serie está en el recurso bcrp://departamento/06) y haz el gráfico de la inflación con graficar_serie.
3. ENAHO, con las skills: limpiando-enaho (la base no existe), graficando-enaho (por área) y mapeando-enaho.
4. Contrasta las cifras con las referencias: salidas/validacion.txt, salidas/comparacion_mapa_referencia.csv y las fuentes del BCRP.
5. Escribe informes/informe_final.md con estas secciones: (1) pregunta, objetivo y delimitación; (2) fuentes y metodología; (3) al menos 3 hallazgos con cada cifra citada (código de serie y periodo, o archivo de salida); (4) visualizaciones: el gráfico del BCRP, el gráfico de ENAHO por área y el mapa, enlazados con rutas relativas (../figuras/..., ../mapas/...); (5) interpretación; (6) limitaciones (niveles de agregación y periodos distintos, asociación no causal, tamaño de muestra por departamento); (7) reproducibilidad (comandos, scripts y códigos de series).

No calcules cifras a mano: todas deben salir de las herramientas o de los archivos de salida. Si una herramienta falla o no encuentra datos, dilo en el informe en vez de estimar.
```

Al terminar: `/export evidencias_ia/integracion/01_investigacion_agente.txt`

Mientras tanto armo la Parte 4: las 10 preguntas con respuestas esperadas verificadas de forma independiente, sin usar el MCP ni las Skills. Después verifico 3 cifras del informe.

## 👤 Usuaria

espera. ya hice commit y push de la parte 2 y fusione esa branch con el main. puedes ver si todo está ok antes de seguir con la parte 3?

<details><summary>🔧 Bash: Verify Part 2 merge, branch state and pending changes</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio" && git fetch --prune -q origin && echo "== rama"; git status -sb | head -12; echo "== ramas"; git branch -a; echo "== main"; git log --oneline -5 origin/main; echo "== HEAD vs origin/main"; git rev-list --left-right --count origin/main...HEAD; echo "== diff working tree vs origin/main (tarea_4)"; git diff --stat origin/main -- tarea_4 | tail -5; echo "== archivos de tarea_4 en origin/main"; git ls-tree -r --name-only origin/main tarea_4/ | grep -v evidencias_ia/00; echo "== ¿graficar_serie en main?"; git show origin/main:tarea_4/mcp/server.py | grep -c "def graficar_serie"; git show origin/main:tarea_4/.claude/skills/limpiando-enaho/scripts/limpiar.py | grep -c reconfigure; git show origin/main:tarea_4/.gitignore | tail -2
```

Resultado:

```text
== rama
## main...origin/main [behind 2]
== ramas
  01_recoleccion
  02_llm_clasificador
  P1-Corpus-y-extraccion
  P2-Evaluacion
  P3-Reel
* main
  p1-obtencion-y-analisis-de-datos
  p2-dashboard
  parte-2-skills-enaho
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
  remotes/origin/parte-2-skills-enaho
== main
eedf839 Merge pull request #19 from dgarcesg/parte-2-skills-enaho
cad86e4 #18 parte-2
c3538a1 Merge pull request #17 from dgarcesg/parte-1-mcp-bcrp
a8cf028 #16 parte-1
588da4a Create placeholder.md
== HEAD vs origin/main
2	0
== diff working tree vs origin/main (tarea_4)
 tarea_4/salidas/comparacion_mapa_referencia.csv    |  26 -
 tarea_4/salidas/indicadores.csv                    |  36 --
 tarea_4/salidas/validacion.txt                     |  22 -
 tarea_4/uv.lock                                    | 327 -------------
 22 files changed, 1770 deletions(-)
== archivos de tarea_4 en origin/main
tarea_4/.claude/skills/graficando-enaho/SKILL.md
tarea_4/.claude/skills/graficando-enaho/scripts/graficar.py
tarea_4/.claude/skills/limpiando-enaho/SKILL.md
tarea_4/.claude/skills/limpiando-enaho/reference.md
tarea_4/.claude/skills/limpiando-enaho/scripts/limpiar.py
tarea_4/.claude/skills/mapeando-enaho/SKILL.md
tarea_4/.claude/skills/mapeando-enaho/referencia/pobreza_departamento_2024.csv
tarea_4/.claude/skills/mapeando-enaho/scripts/mapa.py
tarea_4/.gitignore
tarea_4/.mcp.json
tarea_4/evidencias_ia/exportar_conversacion.py
tarea_4/evidencias_ia/mcp/01_demo_mcp_claude_code.txt
tarea_4/evidencias_ia/mcp/02_demo_mcp_claude_code_completa.md
tarea_4/evidencias_ia/mcp/03_verificacion_demo.md
tarea_4/evidencias_ia/mcp/verificar_demo.py
tarea_4/evidencias_ia/skills/01_demo_skills_claude_code.txt
tarea_4/evidencias_ia/skills/02_demo_skills_claude_code_completa.md
tarea_4/figuras/pobreza_por_area_2024.png
tarea_4/figuras/pobreza_por_departamento_2024.png
tarea_4/figuras/pobreza_por_edad_2024.png
tarea_4/figuras/pobreza_por_sexo_2024.png
tarea_4/mapas/pobreza_departamento_2024.png
tarea_4/mcp/server.py
tarea_4/mcp/test_server.py
tarea_4/placeholder.md
tarea_4/pyproject.toml
tarea_4/salidas/comparacion_mapa_referencia.csv
tarea_4/salidas/indicadores.csv
tarea_4/salidas/validacion.txt
tarea_4/uv.lock
== ¿graficar_serie en main?
1
1
# Base de personas que arma limpiando-enaho: son microdatos derivados y se regeneran con limpiar.py
salidas/*.parquet
```

</details>

## 🤖 Claude

Lo que está en GitHub está bien, pero tu copia local de `main` todavía no lo tiene.

**Lo que está bien en `origin/main`:**
- El PR #19 de la Parte 2 está fusionado con todo lo necesario: las 3 Skills (`SKILL.md`, scripts, `reference.md` y la referencia del mapa), las 4 figuras, el mapa, `validacion.txt`, `indicadores.csv`, la comparación con la referencia y las evidencias de la demostración de las Skills.
- También entraron los últimos cambios: `graficar_serie` en el servidor, la corrección de UTF-8 en los scripts y la regla `salidas/*.parquet` en `.gitignore`.
- No se subieron microdatos: ni los zip ni el `.parquet`.

**Lo que falta en tu copia local:**
- Estás en `main`, pero tu copia está **2 commits atrás** de GitHub, porque no hiciste `pull` después de fusionar.
- Por eso git quitó del disco las Skills, figuras, mapas y salidas al cambiarte de rama. Si abres ahora la sesión de la Parte 3, no va a encontrar las Skills ni `graficar_serie`.

**Cómo dejarlo listo:**
```
git pull --ff-only
git branch -d parte-2-skills-enaho
git switch -c parte-3-agente
```
1. El primer comando trae los 2 commits. No hay conflictos posibles, porque tu `main` no tiene commits propios.
2. El segundo borra la copia local de `parte-2-skills-enaho`, que ya está fusionada. Su copia en GitHub sigue existiendo; esta vez no la borraste.
3. El tercero crea la rama de la Parte 3 **desde el `main` actualizado**, para no repetir lo que pasó con la rama de la Parte 2.

¿Los ejecuto? Solo cambian tu copia local. Después vuelvo a correr las pruebas y la limpieza para confirmar que todo funciona antes de que abras la sesión de la Parte 3.

## 👤 Usuaria

si

<details><summary>🔧 Bash: Update main, delete merged branch, create Part 3 branch, verify</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio" && git pull --ff-only -q && git branch -d parte-2-skills-enaho && git switch -c parte-3-agente && git status -sb | head -3 && git rev-list --left-right --count origin/main...HEAD && cd tarea_4 && find .claude/skills -name SKILL.md && uv run pytest -q 2>&1 | tail -1 && uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 | tail -2 && rm -f salidas/personas_2024.parquet && git -C .. status --short && date
```

Resultado:

```text
Deleted branch parte-2-skills-enaho (was cad86e4).
Switched to a new branch 'parte-3-agente'
## parte-3-agente
0	0
.claude/skills/graficando-enaho/SKILL.md
.claude/skills/limpiando-enaho/SKILL.md
.claude/skills/mapeando-enaho/SKILL.md
10 passed in 12.36s
Resultado: 15 de 15 verificaciones aprobadas; 0 esenciales fallidas.
Base guardada: salidas/personas_2024.parquet (108,664 personas, 27 columnas) y salidas/indicadores.csv.
Sun, Nov  8, 2026 10:32:12 PM
```

</details>

<details><summary>🔧 Bash: Check claude CLI flags for headless evaluation runs</summary>

```bash
claude --help 2>&1 | grep -iE "tools|mcp-config|strict|model|output-format|permission|setting-sources|add-dir|no-session" | head -25
```

Resultado:

```text
  --add-dir <directories...>            Additional directories to allow tool
  --allow-dangerously-skip-permissions  Enable bypassing all permission checks
  --allowedTools, --allowed-tools <tools...>
                                        strictly ANTHROPIC_API_KEY or
                                        --append-system-prompt[-file], --add-dir
                                        (CLAUDE.md dirs), --mcp-config,
  --dangerously-skip-permissions        Bypass all permission checks.
  --disallowedTools, --disallowed-tools <tools...>
  --fallback-model <model>              Enable automatic fallback to specified
                                        model(s) when the default model is
                                        --print and --output-format=stream-json)
                                        --output-format=stream-json)
                                        --output-format=stream-json)
  --mcp-config <configs...>             Load MCP servers from JSON files or
  --model <model>                       Model for the current session. Provide
                                        an alias for the latest model (e.g.
                                        model's full name.
  --no-session-persistence              Disable session persistence - sessions
  --output-format <format>              Output format (only works with --print):
  --permission-mode <mode>              Permission mode to use for the session
                                        "bypassPermissions", "manual",
  --permission-prompts <target>         Who answers permission prompts with
                                        --permission-prompt-tool) or "none"
                                        denied automatically; the permission
                                        --output-format=stream-json)
```

</details>

<details><summary>🔧 Bash: Compute expected BCRP answers directly from the API</summary>

```bash
python -I - <<'EOF'
import httpx, statistics as st
def bcrp(c, d, h):
    p = httpx.get(f"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/{c}/json/{d}/{h}", timeout=60).json()
    return p["config"]["series"][0]["name"], [(x["name"], x["values"][0]) for x in p["periods"]]
for c, d, h in [("PN01273PM", "2024-12", "2024-12"), ("PN01206PM", "2024-12", "2024-12"), ("PD04722MM", "2024-12", "2024-12"),
                ("PN01273PM", "2020-1", "2024-12"), ("RD12956DM", "2024-1", "2024-12")]:
    n, v = bcrp(c, d, h)
    vals = [float(x[1]) for x in v if x[1] != "n.d."]
    print(c, n[:70], "| n", len(v), "| ult", v[-1], "| max", max(v, key=lambda x: float(x[1])), "| prom", round(st.mean(vals), 3))
EOF
```

Resultado:

```text
PN01273PM �ndice de precios Lima Metropolitana (var% 12 meses) - IPC | n 1 | ult ('Dic.2024', '1.96630270142824') | max ('Dic.2024', '1.96630270142824') | prom 1.966
PN01206PM Tipo de cambio - promedio del periodo (S/ por US$) - Interbancario - V | n 1 | ult ('Dic.2024', '3.73655789473684') | max ('Dic.2024', '3.73655789473684') | prom 3.737
PD04722MM Tasas de inter�s del Banco Central de Reserva - Tasa de Referencia de  | n 1 | ult ('Dic.2024', '5') | max ('Dic.2024', '5') | prom 5.0
PN01273PM �ndice de precios Lima Metropolitana (var% 12 meses) - IPC | n 60 | ult ('Dic.2024', '1.96630270142824') | max ('Jun.2022', '8.81263294388897') | prom 4.466
RD12956DM Producci�n de productos mineros seg�n departamentos - Cobre - Cajamarc | n 12 | ult ('Dic.2024', '2331.43155') | max ('Nov.2024', '2349.36473') | prom 1932.934
```

</details>

<details><summary>🔧 Bash: Check MCP isolation flags and approved project servers</summary>

```bash
claude --help 2>&1 | grep -iE -A2 "strict-mcp|--mcp-config|--tools |setting-sources|--bare" | head -30; echo ---; cat "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4/.claude/settings.local.json"
```

Resultado:

```text
  --bare                                Minimal mode: skip hooks (those defined
                                        in settings and by installed plugins;
                                        features built into Claude Code are
--
                                        (CLAUDE.md dirs), --mcp-config,
                                        --settings, --agents, --plugin-dir.
  --betas <betas...>                    Beta headers to include in API requests
--
  --mcp-config <configs...>             Load MCP servers from JSON files or
                                        strings (space-separated)
  --model <model>                       Model for the current session. Provide
--
                                        tools) and WebFetch unless --tools names
                                        them, and ignores user, project and
                                        local settings files (managed settings
--
                                        --strict-mcp-config to skip MCP servers
                                        too). Also confines the file tools to
                                        the working directories (--add-dir
--
  --setting-sources <sources>           Comma-separated list of setting sources
                                        to load (user, project, local).
  --settings <file-or-json>             Path to a settings JSON file or a JSON
--
  --strict-mcp-config                   Only use MCP servers from --mcp-config,
                                        ignoring all other MCP configurations
  --system-prompt <prompt>              System prompt to use for the session
--
                                        default, except under --bare outside
                                        cloud and background sessions): the
---
{
  "enabledMcpjsonServers": [
    "bcrp"
  ],
  "disabledMcpjsonServers": [
    "fetch"
  ]
}
```

</details>

## 👤 Usuaria

[Request interrupted by user]

## 👤 Usuaria

todo en la parte 2 esta funcional como pide la tarea?

## 🤖 Claude

Sí, la Parte 2 cumple los requisitos de la tarea. Hay dos detalles que conviene que conozcas.

| Requisito | Estado | Evidencia |
|---|:-:|---|
| **Limpieza:** lee los módulos 34 y 02, normaliza nombres, filtra residentes con la condición exacta y une por `conglome`, `vivienda` y `hogar` con `validate="m:1"` | ✅ | `limpiar.py` |
| Llaves como texto, sin perder los ceros iniciales | ✅ | Es una verificación de `validacion.txt` |
| Pobreza ~27.6 %, 108,664 residentes, 25 códigos, sin duplicados y factores aplicados | ✅ | 27.53 % (dentro de ±0.1 pp), 108,664, 25/25 y 15 de 15 verificaciones aprobadas |
| `validacion.txt` marca qué pasa y qué falla, y el proceso se detiene si algo esencial falla | ✅ | Se vio en el primer intento: código 1 y sin guardar la base |
| **Gráficos:** área, sexo y departamentos, ponderados, con título analítico, período, unidad y fuente, en `figuras/` | ✅ | 4 PNG; también hay uno por edad |
| **Mapa:** unido por `ubigeo[:2]` = `FIRST_IDDP`, 25 unidades, Lima y Callao separados, escala de un tono, unidad en la leyenda, en `mapas/` | ✅ | El script se detiene si falta alguna unidad |
| Comparación con la referencia de la Sesión 16 | ✅ | `comparacion_mapa_referencia.csv` |
| Invocación individual y activación con lenguaje natural | ✅ | Demostración: `/graficando-enaho area` y "Grafica la pobreza entre hombres y mujeres" |
| Gráficos y mapa corren antes la limpieza si falta la base | ⚠️ | **Demostrado solo con el mapa.** `graficando-enaho` tiene la misma instrucción, pero en la demostración la base ya existía. |

**Los dos detalles:**
1. **La coordinación del gráfico no está demostrada.** En la ejecución de la Parte 3 le pido al agente que corra `limpiando-enaho` de forma explícita, así que eso tampoco lo demuestra. Si quieres cubrirlo, basta un pedido de un minuto en una sesión sin la base: *"Grafica la pobreza por área con la ENAHO 2024"*.
2. **El mapa coincide con la referencia en 16 de 25 departamentos dentro de ±0.1 pp.** Usa personas × `facpob07` y la diferencia llega a 0.5 pp. La referencia se calculó por hogares; con ese método coinciden los 25, y así queda explicado en el CSV, en el `SKILL.md` y en `reference.md`. Si prefieres que el mapa pinte las cifras del método oficial del INEI y coincida 25 de 25, el cambio toma unos 5 minutos. Yo lo dejaría como está, porque la diferencia está explicada y mantiene la misma ponderación en gráficos y mapa.

En la evidencia de la demostración quedó el error de consola Windows de la primera corrida. No es un problema: muestra que se detectó y se corrigió, y los archivos que subiste ya tienen la corrección.

Son cerca de las 10:35 p. m. Detuve la preparación de la Parte 4 cuando me interrumpiste. ¿Ya lanzaste la sesión de la Parte 3? Si quieres, mientras corre sigo con las 10 preguntas.

## 👤 Usuaria

ya hice la coordinación del grafico

<details><summary>🔧 Bash: Find the new coordination session and any exports</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && ls -lt ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/*.jsonl | head -4; ls -la evidencias_ia/*/ informes/ salidas/ | head -40; git -C .. status --short; date
```

Resultado:

```text
-rw-r--r-- 1 usuario 1049089 2084482 Nov  8 22:29 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/7e4804b7-5171-4706-a0a7-128ed2a04bb3.jsonl
-rw-r--r-- 1 usuario 1049089  872654 Nov  8 21:44 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/7bfebfb8-d42f-472c-8fb2-7a5f78500694.jsonl
evidencias_ia/integracion/:
total 4
drwxr-xr-x 1 usuario 1049089 0 Nov  8 22:23 .
drwxr-xr-x 1 usuario 1049089 0 Nov  8 22:31 ..

evidencias_ia/mcp/:
total 88
drwxr-xr-x 1 usuario 1049089     0 Nov  8 21:49 .
drwxr-xr-x 1 usuario 1049089     0 Nov  8 22:31 ..
-rw-r--r-- 1 usuario 1049089 28758 Nov  8 21:49 01_demo_mcp_claude_code.txt
-rw-r--r-- 1 usuario 1049089 40307 Nov  8 21:49 02_demo_mcp_claude_code_completa.md
-rw-r--r-- 1 usuario 1049089  2473 Nov  8 21:49 03_verificacion_demo.md
-rw-r--r-- 1 usuario 1049089  1042 Nov  8 21:49 verificar_demo.py

evidencias_ia/skills/:
total 36
drwxr-xr-x 1 usuario 1049089     0 Nov  8 22:31 .
drwxr-xr-x 1 usuario 1049089     0 Nov  8 22:31 ..
-rw-r--r-- 1 usuario 1049089  6614 Nov  8 22:31 01_demo_skills_claude_code.txt
-rw-r--r-- 1 usuario 1049089 21239 Nov  8 22:31 02_demo_skills_claude_code_completa.md

informes/:
total 4
drwxr-xr-x 1 usuario 1049089 0 Nov  8 22:23 .
drwxr-xr-x 1 usuario 1049089 0 Nov  8 22:31 ..

salidas/:
total 1484
drwxr-xr-x 1 usuario 1049089       0 Nov  8 22:41 .
drwxr-xr-x 1 usuario 1049089       0 Nov  8 22:31 ..
-rw-r--r-- 1 usuario 1049089     989 Nov  8 22:31 comparacion_mapa_referencia.csv
-rw-r--r-- 1 usuario 1049089    1924 Nov  8 22:41 indicadores.csv
-rw-r--r-- 1 usuario 1049089 1497088 Nov  8 22:41 personas_2024.parquet
-rw-r--r-- 1 usuario 1049089    1974 Nov  8 22:41 validacion.txt
Sun, Nov  8, 2026 10:45:11 PM
```

</details>

<details><summary>🔧 Bash: Locate the session that ran the chart coordination</summary>

```bash
find ~/.claude/projects -name "*.jsonl" -newermt "2026-11-08 22:25" -printf "%TT %s %p\n" 2>/dev/null | sort; cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && ls -la --time-style=+%H:%M figuras/ && git -C .. diff --stat
```

Resultado:

```text
22:29:39.8271413000 2084482 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/7e4804b7-5171-4706-a0a7-128ed2a04bb3.jsonl
22:42:38.2780427000 713616 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/1949a996-0f82-493a-b15a-6820b5b0e6fb.jsonl
22:45:23.4682020000 4704346 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/57ecd584-3768-4852-a254-c84910c84d73.jsonl
total 412
drwxr-xr-x 1 usuario 1049089      0 22:31 .
drwxr-xr-x 1 usuario 1049089      0 22:31 ..
-rw-r--r-- 1 usuario 1049089  75255 22:42 pobreza_por_area_2024.png
-rw-r--r-- 1 usuario 1049089 161930 22:31 pobreza_por_departamento_2024.png
-rw-r--r-- 1 usuario 1049089  90575 22:31 pobreza_por_edad_2024.png
-rw-r--r-- 1 usuario 1049089  76596 22:31 pobreza_por_sexo_2024.png
```

</details>

<details><summary>🔧 Bash: List what the coordination session asked and invoked</summary>

```bash
python -I -c "
import json,sys; sys.stdout.reconfigure(encoding='utf-8')
for l in open(sys.argv[1],encoding='utf-8'):
    d=json.loads(l)
    if d.get('type')=='assistant':
        for b in d['message']['content']:
            if b.get('type')=='tool_use':
                i=b['input']; print('TOOL', b['name'], (i.get('skill') or i.get('command') or i.get('file_path') or '')[:150].replace(chr(10),' '))
            if b.get('type')=='text': print('TEXT', b['text'][:200].replace(chr(10),' '))
    if d.get('type')=='user' and isinstance(d['message']['content'],str): print('USER', d['message']['content'][:150].replace(chr(10),' '))
" ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/1949a996-0f82-493a-b15a-6820b5b0e6fb.jsonl
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Bash: Remove the clean base so Part 3 shows skill coordination</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && rm -f salidas/personas_2024.parquet && ls salidas && pwd -W
```

Resultado:

```text
comparacion_mapa_referencia.csv
indicadores.csv
validacion.txt
~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4
```

</details>

## 🤖 Claude

Listo, la base ya está borrada. Ahora abre la sesión de la Parte 3. **Asegúrate de estar en `tarea_4`:**
```
cd "~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4"
claude
```
Antes de pegar el pedido, confirma que `/mcp` muestra `bcrp` conectado.

Usa el mismo pedido que te pasé, pero **cambia el punto 3** por este:
```
3. ENAHO, con las skills graficando-enaho (por área) y mapeando-enaho. No corras la limpieza tú directamente: deja que las skills la pidan si falta la base.
```
Así, en una sola ejecución deberían aparecer `bcrp` con `buscar_series`, `resumen` y `graficar_serie`, y las Skills `graficando-enaho` → `limpiando-enaho` → `mapeando-enaho`. Eso cumple la condición de usar 2 herramientas MCP y 2 Skills, y además demuestra la coordinación del gráfico.

Al final: `/export evidencias_ia/integracion/01_investigacion_agente.txt`

La sesión que corriste desde la raíz no la voy a usar como evidencia de activación. Si quieres, la agrego como registro de desarrollo, aclarando que ahí las Skills no se cargaron.

Son las 10:48 p. m. Mientras corre la Parte 3, ¿lanzo las 10 preguntas del modo A (sin MCP ni Skills) con `claude -p` en segundo plano? Usan tu plan de Claude: son 10 sesiones independientes y cortas, desde una carpeta vacía fuera del repositorio. El modo B lo lanzo cuando termine la Parte 3, para que no compita por los mismos archivos.

## 👤 Usuaria

me sale: The skills in tarea_4/.claude/skills/ aren't registered in this session, so I'll follow each SKILL.md manually, starting with checking the scripts and whether the base for graficando-enaho exists

<details><summary>🔧 Bash: Find the new session and the folder it was opened in</summary>

```bash
find ~/.claude/projects -name "*.jsonl" -newermt "2026-11-08 22:44" -printf "%TT %s %p\n" 2>/dev/null | sort; for f in $(find ~/.claude/projects -name "*.jsonl" -newermt "2026-11-08 22:46" ! -name "57ecd584*"); do echo "== $f"; python -I -c "
import json,sys; sys.stdout.reconfigure(encoding='utf-8')
for l in open(sys.argv[1],encoding='utf-8'):
    d=json.loads(l)
    if d.get('cwd'): print('cwd:', d['cwd']); break
" "$f"; done
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Bash: Check whether the wrong session already wrote outputs</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && ls -la --time-style=+%H:%M:%S salidas informes figuras | grep -v "^total\|^d"; date +%H:%M:%S
```

Resultado:

```text
figuras:
-rw-r--r-- 1 usuario 1049089  75255 22:42:20 pobreza_por_area_2024.png
-rw-r--r-- 1 usuario 1049089 161930 22:31:30 pobreza_por_departamento_2024.png
-rw-r--r-- 1 usuario 1049089  90575 22:31:30 pobreza_por_edad_2024.png
-rw-r--r-- 1 usuario 1049089  76596 22:31:30 pobreza_por_sexo_2024.png

informes:

salidas:
-rw-r--r-- 1 usuario 1049089  989 22:31:30 comparacion_mapa_referencia.csv
-rw-r--r-- 1 usuario 1049089 1924 22:41:54 indicadores.csv
-rw-r--r-- 1 usuario 1049089 1974 22:41:54 validacion.txt
22:50:54
```

</details>

## 🤖 Claude

**Esa sesión también se abrió en la raíz del repositorio.** El registro dice `cwd: ...\diplomado_python_intermedio`, no `...\tarea_4`. Por eso no carga las Skills, y tampoco el MCP `bcrp`.

**1. Detén esa sesión ahora** con Esc o Ctrl+C. Todavía no ha escrito nada: no hay base ni informe nuevos.

**2. Ciérrala** con `/exit`.

**3. Ábrela desde `tarea_4`.** Si usas una terminal:
```
cd "~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4"
claude
```
- Si usas Claude Code dentro de VS Code u otro editor, esa sesión se abre en la carpeta del espacio de trabajo, que es la raíz del repositorio. En ese caso usa la terminal integrada con los comandos de arriba, o abre `tarea_4` como carpeta del editor.
- La sesión de la demostración del MCP y la de las Skills sí se abrieron en `tarea_4`, y ahí todo cargó bien.

**4. Comprueba antes de pegar el pedido** que todo cargó:
- `/mcp` muestra `bcrp` conectado.
- `/skills` lista `limpiando-enaho`, `graficando-enaho` y `mapeando-enaho`.

Ninguna de las dos sesiones abiertas desde la raíz (la del gráfico y esta) sirve como evidencia de las Skills. Cuando termines la Parte 3, decido contigo si las incluimos como registro de desarrollo, con esa aclaración.

## 👤 Usuaria

ya corrio, como lo exporto para el registor?

<details><summary>🔧 Bash: Find the Part 3 session and check its outputs</summary>

```bash
find ~/.claude/projects -name "*.jsonl" -newermt "2026-11-08 22:50" ! -name "57ecd584*" -printf "%TT %s %p\n" 2>/dev/null | sort; cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && ls -la --time-style=+%H:%M informes figuras salidas evidencias_ia/integracion | grep -v "^total\|^d"; date +%H:%M
```

Resultado:

```text
22:51:17.6405895000 487239 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/18d888ac-e439-4181-b8ea-fe0899357fc3.jsonl
22:55:05.2732510000 1871882 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/00a46994-d42b-48cd-bb38-e91a266e04b6.jsonl
evidencias_ia/integracion:

figuras:
-rw-r--r-- 1 usuario 1049089  75255 22:54 pobreza_por_area_2024.png
-rw-r--r-- 1 usuario 1049089 161930 22:31 pobreza_por_departamento_2024.png
-rw-r--r-- 1 usuario 1049089  90575 22:31 pobreza_por_edad_2024.png
-rw-r--r-- 1 usuario 1049089  76596 22:31 pobreza_por_sexo_2024.png

informes:

salidas:
-rw-r--r-- 1 usuario 1049089     989 22:54 comparacion_mapa_referencia.csv
-rw-r--r-- 1 usuario 1049089    1924 22:53 indicadores.csv
-rw-r--r-- 1 usuario 1049089 1497088 22:53 personas_2024.parquet
-rw-r--r-- 1 usuario 1049089    1974 22:53 validacion.txt
22:56
```

</details>

<details><summary>🔧 Bash: List what the tarea_4 session asked and invoked</summary>

```bash
python -I -c "
import json,sys; sys.stdout.reconfigure(encoding='utf-8')
for l in open(sys.argv[1],encoding='utf-8'):
    d=json.loads(l)
    if d.get('type')=='assistant':
        for b in d['message']['content']:
            if b.get('type')=='tool_use':
                i=b['input']; print('TOOL', b['name'], (i.get('skill') or i.get('command') or i.get('file_path') or json.dumps(i,ensure_ascii=False))[:130].replace(chr(10),' '))
            if b.get('type')=='text': print('TEXT', b['text'][:160].replace(chr(10),' '))
    if d.get('type')=='user' and isinstance(d['message']['content'],str): print('USER', d['message']['content'][:200].replace(chr(10),' '))
" ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/00a46994-d42b-48cd-bb38-e91a266e04b6.jsonl
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Bash: Export the skill coordination session to markdown</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad" && python -I evidencias_ia/exportar_conversacion.py ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/00a46994-d42b-48cd-bb38-e91a266e04b6.jsonl evidencias_ia/skills/04_coordinacion_grafico_completa.md "Coordinación de Skills: graficando-enaho activa limpiando-enaho cuando falta la base (registro completo)" "$S/ocultar.txt"
```

Resultado:

```text
evidencias_ia/skills/04_coordinacion_grafico_completa.md: 194 l�neas
```

</details>

## 🤖 Claude

Ya guardé el registro completo en `evidencias_ia/skills/04_coordinacion_grafico_completa.md`. Para tener también la vista de pantalla:

**1. En esa misma sesión**, exporta y limpia:
```
/export evidencias_ia/skills/03_coordinacion_grafico.txt
/clear
```
`/clear` empieza una conversación nueva en la misma terminal, que sigue en `tarea_4`. Revisa que `/mcp` muestre `bcrp` conectado.

**2. Pega el pedido completo de la Parte 3, todo junto:**
```
Pregunta de investigación: ¿Cómo evolucionaron la inflación y la producción de cobre del Perú entre 2020 y 2024, y qué brechas territoriales y entre áreas urbana y rural mostraba la pobreza monetaria en 2024, en particular en Cajamarca, el departamento con más pobreza y gran productor de cobre?

Actúa como agente de investigación:
1. Escribe primero un plan breve: qué series del BCRP y qué indicadores de la ENAHO necesitas, y con qué herramienta MCP o skill obtendrás cada uno.
2. BCRP, solo con el MCP bcrp: busca las series con buscar_series, saca las cifras con resumen (inflación a 12 meses de Lima, 2020-2024; producción de cobre de Cajamarca 2020-2024, cuya serie está en el recurso bcrp://departamento/06) y haz el gráfico de la inflación con graficar_serie.
3. ENAHO, con las skills graficando-enaho (por área) y mapeando-enaho. Si falta la base, deja que las skills pidan la limpieza.
4. Contrasta las cifras con las referencias: salidas/validacion.txt, salidas/comparacion_mapa_referencia.csv y las fuentes del BCRP.
5. Escribe informes/informe_final.md con estas secciones: (1) pregunta, objetivo y delimitación; (2) fuentes y metodología; (3) al menos 3 hallazgos con cada cifra citada (código de serie y periodo, o archivo de salida); (4) visualizaciones: el gráfico del BCRP, el gráfico de ENAHO por área y el mapa, enlazados con rutas relativas (../figuras/..., ../mapas/...); (5) interpretación; (6) limitaciones (niveles de agregación y periodos distintos, asociación no causal, tamaño de muestra por departamento); (7) reproducibilidad (comandos, scripts y códigos de series).

No calcules cifras a mano: todas deben salir de las herramientas o de los archivos de salida. Si una herramienta falla o no encuentra datos, dilo en el informe en vez de estimar.
```

**3. Al terminar:** `/export evidencias_ia/integracion/01_investigacion_agente.txt`

Son las 10:58 p. m. y queda 1 hora. Para llegar con la Parte 4, necesito lanzar **ahora** las 10 preguntas del modo A con `claude -p` en segundo plano. Usan tu plan de Claude: son 10 sesiones cortas desde una carpeta vacía, sin MCP, sin Skills y sin web. ¿Las lanzo?

## 👤 Usuaria

me sale  Failed to export conversation: ENOENT: no such file or directory, mkdir '~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evidencias_ia\skills\03_coordinacion_grafico.txt

<details><summary>🔧 Bash: Check the evidence folders exist ⚠️ error</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && ls -la evidencias_ia/ evidencias_ia/skills/; ls *.txt 2>/dev/null
```

Resultado:

```text
Exit code 2
evidencias_ia/:
total 132
drwxr-xr-x 1 usuario 1049089      0 Nov  8 22:31 .
drwxr-xr-x 1 usuario 1049089      0 Nov  8 22:31 ..
-rw-r--r-- 1 usuario 1049089 107432 Nov  8 21:49 00_sesion_principal_claude_code.md
-rw-r--r-- 1 usuario 1049089   7262 Nov  8 21:49 exportar_conversacion.py
drwxr-xr-x 1 usuario 1049089      0 Nov  8 22:23 integracion
drwxr-xr-x 1 usuario 1049089      0 Nov  8 21:49 mcp
drwxr-xr-x 1 usuario 1049089      0 Nov  8 22:56 skills

evidencias_ia/skills/:
total 56
drwxr-xr-x 1 usuario 1049089     0 Nov  8 22:56 .
drwxr-xr-x 1 usuario 1049089     0 Nov  8 22:31 ..
-rw-r--r-- 1 usuario 1049089  6614 Nov  8 22:31 01_demo_skills_claude_code.txt
-rw-r--r-- 1 usuario 1049089 21239 Nov  8 22:31 02_demo_skills_claude_code_completa.md
-rw-r--r-- 1 usuario 1049089 13831 Nov  8 22:56 04_coordinacion_grafico_completa.md
```

</details>

## 🤖 Claude

La carpeta `evidencias_ia/skills/` existe, así que el fallo es del comando `/export` de Claude Code y no de la ruta. **No te detengas por eso:** el registro completo de esa sesión ya está guardado en `evidencias_ia/skills/04_coordinacion_grafico_completa.md` y es más detallado que el `.txt`, porque incluye cada llamada a las Skills.

**Ahora:**
1. En esa sesión, escribe `/clear` y pega el pedido completo de la Parte 3.
2. Al terminar, exporta **sin subcarpeta**, porque así sí debería funcionar: `/export investigacion_agente.txt`. Lo muevo yo a `evidencias_ia/integracion/`, y además genero el registro completo desde el `.jsonl`.

Si el `.txt` de la coordinación también te interesa, puedes hacer lo mismo antes del `/clear`: `/export 03_coordinacion_grafico.txt`.

Son las 11:00 p. m. Sigo esperando tu respuesta sobre el **modo A** de la Parte 4. Sin lanzarlo ahora no alcanzamos a hacer el experimento antes de la medianoche. ¿Lo lanzo?

## 👤 Usuaria

quiero cambiar la pregunta de investigación para que el departamento sea arequipa

<details><summary>🔧 Bash: Confirm Arequipa copper series exists and its poverty rate</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && uv run python -c "
import pandas as pd, sys; sys.stdout.reconfigure(encoding='utf-8')
df=pd.read_csv('mcp/datos/catalogo_bcrp.csv',sep=';',dtype=str).fillna('')
s=df[df['Nombre de serie'].str.contains('Cobre - Arequipa')]
print(s[['Código de serie','Nombre de serie','Frecuencia','Fecha de fin']].to_string())
"; grep -i arequipa salidas/indicadores.csv
```

Resultado:

```text
      Código de serie          Nombre de serie  Frecuencia Fecha de fin
8809        RD12954DM  Cobre - Arequipa (tm.f)     Mensual     Dic-2025
9901        RD14265DQ  Cobre - Arequipa (tm.f)  Trimestral      T4-2025
10963       RD15519DA  Cobre - Arequipa (tm.f)       Anual         2025
departamento,Arequipa,04,15.77,1.62,15.78,1415224,4645
```

</details>

## 🤖 Claude

Arequipa funciona bien: tiene la serie mensual de cobre **RD12954DM** con datos hasta 2025, y su pobreza en 2024 es **15.8 %**, una de las más bajas. Hace buen contraste con Cajamarca (45.0 %). Este es el pedido completo con Arequipa:

```
Pregunta de investigación: ¿Cómo evolucionaron la inflación y la producción de cobre del Perú entre 2020 y 2024, y qué brechas territoriales y entre áreas urbana y rural mostraba la pobreza monetaria en 2024, en particular en Arequipa, uno de los principales productores de cobre del país?

Actúa como agente de investigación:
1. Escribe primero un plan breve: qué series del BCRP y qué indicadores de la ENAHO necesitas, y con qué herramienta MCP o skill obtendrás cada uno.
2. BCRP, solo con el MCP bcrp: busca las series con buscar_series, saca las cifras con resumen (inflación a 12 meses de Lima, 2020-2024; producción de cobre de Arequipa 2020-2024, cuya serie está en el recurso bcrp://departamento/04) y haz el gráfico de la inflación con graficar_serie.
3. ENAHO, con las skills graficando-enaho (por área) y mapeando-enaho. Si falta la base, deja que las skills pidan la limpieza.
4. Contrasta las cifras con las referencias: salidas/validacion.txt, salidas/comparacion_mapa_referencia.csv y las fuentes del BCRP.
5. Escribe informes/informe_final.md con estas secciones: (1) pregunta, objetivo y delimitación; (2) fuentes y metodología; (3) al menos 3 hallazgos con cada cifra citada (código de serie y periodo, o archivo de salida); (4) visualizaciones: el gráfico del BCRP, el gráfico de ENAHO por área y el mapa, enlazados con rutas relativas (../figuras/..., ../mapas/...); (5) interpretación; (6) limitaciones (niveles de agregación y periodos distintos, asociación no causal, tamaño de muestra por departamento); (7) reproducibilidad (comandos, scripts y códigos de series).

No calcules cifras a mano: todas deben salir de las herramientas o de los archivos de salida. Si una herramienta falla o no encuentra datos, dilo en el informe en vez de estimar.
```

Pégalo después de `/clear` en la sesión abierta en `tarea_4`. Al terminar: `/export investigacion_agente.txt`

Son las 11:01 p. m. ¿Lanzo el modo A de la Parte 4 mientras tanto? Necesito un sí para empezar.

## 👤 Usuaria

ya esta corriendo la parte 3 en otro terminal. avanza con la parte 4

## 🤖 Claude

Arranco la Parte 4. Primero calculo, directo de la API del BCRP, la respuesta esperada de la pregunta mixta sobre el cobre de Arequipa.

<details><summary>🔧 Bash: Compute Arequipa 2024 copper average from the BCRP API</summary>

```bash
python -I -c "
import httpx, statistics as st
p=httpx.get('https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD12954DM/json/2024-1/2024-12',timeout=60).json()['periods']
v=[float(x['values'][0]) for x in p]; print(len(v), round(st.mean(v),1), p[0], p[-1])"; claude --help 2>&1 | grep -iE "^\s+--model|sonnet|opus" | head -5; date +%H:%M
```

Resultado:

```text
12 37819.7 {'name': 'Ene.2024', 'values': ['33361.724939']} {'name': 'Dic.2024', 'values': ['39260.208007']}
  --model <model>                       Model for the current session. Provide
                                        'fable', 'opus', or 'sonnet') or a
23:01
```

</details>

<details><summary>🔧 Bash: Write pre-registered questions outside repo and MCP config</summary>

```bash
S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad"; mkdir -p "$S/eval" "$S/modo_a_vacio" && cat > "$S/eval/preguntas.csv" <<'EOF'
id,tipo,pregunta,respuesta_esperada,valores_esperados,tolerancia,etiquetas_requeridas,verificacion
B1,bcrp,¿Cuál fue la inflación a 12 meses de Lima Metropolitana en diciembre de 2024?,1.97 %,1.97,0.05,,API BCRP serie PN01273PM periodo Dic.2024 = 1.9663 (consulta directa a estadisticas.bcrp.gob.pe sin el MCP)
B2,bcrp,"¿Cuál fue el valor máximo de la inflación a 12 meses de Lima Metropolitana entre enero de 2020 y diciembre de 2024, y en qué mes ocurrió?",8.81 % en junio de 2022,8.81,0.05,junio|jun;2022,API BCRP serie PN01273PM 2020-01 a 2024-12: máximo Jun.2022 = 8.8126
B3,bcrp,"¿Cuál fue el tipo de cambio interbancario de venta promedio de diciembre de 2024, en soles por dólar?",S/ 3.737 por US$,3.737,0.005,,API BCRP serie PN01206PM periodo Dic.2024 = 3.7366
B4,bcrp,¿En qué nivel estaba la tasa de referencia de la política monetaria del BCRP en diciembre de 2024?,5.00 %,5.00,0.01,,API BCRP serie PD04722MM periodo Dic.2024 = 5
E1,enaho,¿Cuál fue la tasa de pobreza monetaria nacional del Perú en 2024 según la ENAHO del INEI?,27.6 %,27.6,0.1,,INEI (cifra oficial 2024) y tabla de validación de la Sesión 16: 27.6 %
E2,enaho,¿Cuál fue la tasa de pobreza monetaria en el área rural del Perú en 2024 según la ENAHO del INEI?,39.3 %,39.3,0.2,,INEI y Sesión 16: 39.3 %. Tolerancia 0.2 pp porque con personas × facpob07 se obtiene 39.44 % (ver salidas/validacion.txt)
E3,enaho,"¿Qué departamento tuvo la mayor tasa de pobreza monetaria en 2024 según la ENAHO del INEI, y cuál fue esa tasa?",Cajamarca con 45.0 %,45.0,0.2,Cajamarca,Referencia de la Sesión 16 (pobreza_departamento_2024.csv): Cajamarca 45.0 %
E4,enaho,¿Cuántas personas son residentes habituales en el módulo 02 (miembros del hogar) de la ENAHO 2024?,"108,664 personas",108664,0,,Enunciado de la Tarea 4 y tabla de validación de la Sesión 16: 108,664 de 117,721 filas
M1,mixta,"¿Cuál fue la inflación a 12 meses de Lima en diciembre de 2024 según el BCRP y la pobreza monetaria nacional de 2024 según la ENAHO? ¿Permiten esos dos datos concluir que la baja inflación redujo la pobreza?","1.97 % y 27.6 %; no permiten concluir causalidad",1.97;27.6,0.05;0.1,no causal,Las dos cifras de B1 y E1. Interpretación correcta: dos datos de un año no prueban causalidad (niveles y periodos distintos)
M2,mixta,"Según el BCRP, ¿cuál fue la producción promedio mensual de cobre de Arequipa en 2024 (en toneladas métricas finas), y según la ENAHO, cuál fue la pobreza monetaria de Arequipa en 2024? ¿Qué se puede decir de la relación entre ambas?","37,819.7 tm.f y 15.8 %; asociación descriptiva, no causal",37819.7;15.8,400;0.2,no causal,API BCRP serie RD12954DM 2024 (promedio de 12 meses = 37819.7); referencia Sesión 16 Arequipa 15.8 %. Interpretación: una sola observación no prueba relación causal
EOF
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && cat > evaluacion/mcp_bcrp.json <<'EOF'
{
  "mcpServers": {
    "bcrp": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "mcp/server.py"]
    }
  }
}
EOF
python -I -c "import csv,sys; r=list(csv.DictReader(open(sys.argv[1],encoding='utf-8'))); print(len(r), [x['id'] for x in r])" "$S/eval/preguntas.csv"; sha256sum "$S/eval/preguntas.csv"
```

Resultado:

```text
10 ['B1', 'B2', 'B3', 'B4', 'E1', 'E2', 'E3', 'E4', 'M1', 'M2']
ca410402cae8b57c2a2d7d8d887a06272678c6b7b45713b46d2a1443c60105c1 *~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad/eval/preguntas.csv
```

</details>

<details><summary>🔧 Write</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evaluacion\ejecutar_evaluacion.py

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


if _
… [recortado: 34 caracteres más]
```

Resultado:

```text
File created successfully at: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evaluacion\ejecutar_evaluacion.py (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>🔧 Bash: Smoke-test Mode A on one question and inspect isolation</summary>

```bash
S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad"; cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && python -I evaluacion/ejecutar_evaluacion.py --modo A --preguntas "$S/eval/preguntas.csv" --vacia "$S/modo_a_vacio" --solo B1 && python -I -c "
import json,sys; sys.stdout.reconfigure(encoding='utf-8')
for l in open('evaluacion/corridas/A_B1.jsonl',encoding='utf-8'):
    d=json.loads(l)
    if d.get('type')=='system' and d.get('subtype')=='init': print('tools:', d.get('tools')); print('mcp:', d.get('mcp_servers')); print('skills:', d.get('skills') or d.get('slash_commands','')[:5])
    if d.get('type')=='result': print('RESULT', d.get('duration_ms'), repr(d.get('result'))[:400])
"
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

## 🤖 Claude

El modo A queda bien aislado: sin MCP, sin shell, sin web y sin las Skills del proyecto. Respondió B1 de memoria en 10 s. Lanzo los dos modos completos en paralelo y en segundo plano.

<details><summary>🔧 Bash: Run Mode A on the remaining nine questions</summary>

```bash
S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad"; cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && python -I evaluacion/ejecutar_evaluacion.py --modo A --preguntas "$S/eval/preguntas.csv" --vacia "$S/modo_a_vacio" --solo B2,B3,B4,E1,E2,E3,E4,M1,M2
```

Resultado:

```text
Command running in background with ID: b2fgp4byb. Output is being written to: ~\AppData\Local\Temp\claude\0e9f16fe359e3b06\57ecd584-3768-4852-a254-c84910c84d73\tasks\b2fgp4byb.output. You will be notified when it completes — do not poll that file or sleep while waiting. Read the file only if the user asks for progress, or if you need a line it prints before you can go on, such as a server's ready line or port.
Session cwd remains ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4; directory changes made by the backgrounded command do not apply to subsequent commands.
```

</details>

<details><summary>🔧 Bash: Run Mode B on all ten questions</summary>

```bash
S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad"; cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && python -I evaluacion/ejecutar_evaluacion.py --modo B --preguntas "$S/eval/preguntas.csv"
```

Resultado:

```text
Command running in background with ID: bikdf1vev. Output is being written to: ~\AppData\Local\Temp\claude\0e9f16fe359e3b06\57ecd584-3768-4852-a254-c84910c84d73\tasks\bikdf1vev.output. You will be notified when it completes — do not poll that file or sleep while waiting. Read the file only if the user asks for progress, or if you need a line it prints before you can go on, such as a server's ready line or port.
Session cwd remains ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4; directory changes made by the backgrounded command do not apply to subsequent commands.
```

</details>

## 🤖 Claude

Mientras corren, registro el diseño antes de ver resultados (con la huella de las respuestas esperadas) y escribo el calificador.

<details><summary>🔧 Bash: Write the pre-registration record before results</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && cat > evaluacion/registro_experimento.md <<'EOF'
# Registro previo del experimento

Escrito **antes de ver los resultados**, el 8 de noviembre de 2026 a las 23:05 (hora de Perú).

## Preguntas y respuestas esperadas

Las 10 preguntas y sus respuestas esperadas (`preguntas.csv`) se fijaron antes de correr el experimento. Cada
respuesta se verificó con una fuente independiente del agente:
- **BCRP:** consulta directa a la API de estadisticas.bcrp.gob.pe, sin el MCP.
- **ENAHO:** cifras oficiales del INEI y referencias de la Sesión 16.

Durante las corridas, el archivo con las respuestas estuvo **fuera de `tarea_4/`**, para que ningún modo pudiera
leerlo. Después se copió a `evaluacion/preguntas.csv` sin cambios. Su huella permite comprobarlo:

    sha256(preguntas.csv) = ca410402cae8b57c2a2d7d8d887a06272678c6b7b45713b46d2a1443c60105c1

Para verificarla:

    sha256sum evaluacion/preguntas.csv

## Condiciones

| | Modo A: sin MCP ni Skills | Modo B: con MCP y Skills |
|---|---|---|
| Modelo | `sonnet` (Claude Sonnet 5.5) | El mismo |
| Instrucción | La pregunta + «Responde en español y en pocas líneas: da la cifra con su unidad, el periodo y la fuente. Si no puedes obtener o verificar el dato, dilo en vez de inventarlo.» | La misma |
| Sesiones | Una por pregunta (`claude -p`), independientes | La misma |
| Carpeta | Vacía, fuera del proyecto: no hay salidas ya calculadas que leer | `tarea_4/` |
| MCP | Ninguno (`--strict-mcp-config` sin `--mcp-config`) | Solo `bcrp` (`evaluacion/mcp_bcrp.json`) |
| Skills del proyecto | No (`Skill` deshabilitada; tampoco existen en esa carpeta) | Sí: `limpiando-enaho`, `graficando-enaho`, `mapeando-enaho` |
| Shell | No (`Bash` y `PowerShell` deshabilitadas) | Sí, para correr los scripts de las Skills |
| Web | No (`WebSearch` y `WebFetch` deshabilitadas) | No: así la mejora se atribuye a las herramientas propias |
| Otras herramientas habilitadas | `Read`, `Glob`, `Grep` (en la carpeta vacía) y las internas de Claude Code | `Read`, `Glob`, `Grep`, recursos MCP y las internas de Claude Code |

Se usó `sonnet` en los dos modos por tiempo y por el límite de uso del plan. Lo que exige el diseño es que el modelo
sea el mismo en ambos modos.

## Criterio de corrección

Se definió antes de ver los resultados y se aplica con `evaluacion/calificar.py`:
- **Cifras:** la respuesta es correcta si incluye cada cifra esperada dentro de la tolerancia de `preguntas.csv`.
- **Etiquetas:** debe incluir también las requeridas, como el mes y el año del máximo o el nombre del departamento.
- **Preguntas mixtas:** además de las dos cifras, la interpretación debe rechazar una conclusión causal.
- **Revisión manual:** se revisa cada respuesta a mano y se anota cualquier diferencia con la calificación automática.
- **Sin respuesta:** una respuesta que dice no poder obtener el dato, sin dar cifras, cuenta como no contestada.
EOF
echo ok
```

Resultado:

```text
ok
```

</details>

<details><summary>🔧 Write</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evaluacion\calificar.py

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
    if "Read" in herramientas or "Bash" in herramientas:
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
    if not faltan
… [recortado: 2,376 caracteres más]
```

Resultado:

```text
File created successfully at: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evaluacion\calificar.py (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Claude

Mientras corren las 20 preguntas, escribo el `README.md`. La sección de resultados de la evaluación la completo cuando terminen.

<details><summary>🔧 Write</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\README.md

# Tarea 4 · Agente de investigación socioeconómica: MCP del BCRP + Skills de la ENAHO 2024

## 1. Objetivo

Construir un agente en Claude Code que investigue la realidad socioeconómica peruana con **datos oficiales**:
- **BCRP:** consulta las series del BCRP mediante un **servidor MCP** propio.
- **ENAHO 2024 del INEI:** procesa los microdatos con tres **Skills** que limpian, grafican y mapean.

Cada cifra sale de una herramienta que se puede volver a ejecutar, no de la memoria del modelo. El proyecto incluye
pruebas automatizadas, un informe de investigación verificado y un experimento que compara al agente con y sin estas
herramientas.

**Pregunta de investigación:** ¿Cómo evolucionaron la inflación y la producción de cobre del Perú entre 2020 y 2024, y
qué brechas territoriales y entre áreas urbana y rural mostraba la pobreza monetaria en 2024, en particular en Arequipa,
uno de los principales productores de cobre del país?

## 2. Arquitectura

ˋˋˋtext
                        Pregunta en lenguaje natural
                                     │
                                     ▼
                ┌──────────────────────────────────────────┐
                │   Claude Code (agente que coordina)      │
                │   lee .mcp.json y .claude/skills/        │
                └──────┬────────────────────────────┬──────┘
                       │ MCP (stdio)                │ Skills (scripts con uv)
                       ▼                            ▼
       ┌──────────────────────────────┐   ┌───────────────────────────────────────┐
       │ mcp/server.py (FastMCP)      │   │ limpiando-enaho → personas_2024.parquet│
       │ buscar_series · serie        │   │   + validacion.txt + indicadores.csv  │
       │ resumen · comparar_paises    │   │ graficando-enaho → figuras/*.png      │
       │ graficar_serie               │   │ mapeando-enaho  → mapas/*.png         │
       │ recursos bcrp://serie/{cod}  │   │ (gráficos y mapa piden la limpieza    │
       │         bcrp://departamento/ │   │  si falta la base)                    │
       │ prompt informe(tema)         │   └──────────────────┬────────────────────┘
       └──────────────┬───────────────┘                      │
                      ▼                                      ▼
        API del BCRP · API del Banco Mundial      Microdatos INEI (datos/, fuera de git)
                      └───────────────┬──────────────────────┘
                                      ▼
                      informes/informe_final.md (cifras citadas)
ˋˋˋ

## 3. Servidor MCP del BCRP (`mcp/server.py`)

| Tipo | Nombre | Qué hace |
|---|---|---|
| Herramienta | `buscar_series` | Busca series en el catálogo oficial (17 mil series) por palabras clave y frecuencia |
| Herramienta | `serie` | Descarga los datos de una serie entre dos fechas, con reintentos, y devuelve la URL de la fuente |
| Herramienta | `resumen` | Calcula en Python el primer y último dato, el cambio, la variación %, el promedio, el máximo y el mínimo |
| Herramienta propia | `comparar_paises` | Compara al Perú con otros países usando indicadores anuales del Banco Mundial (crecimiento, inflación, desempleo) |
| Herramienta propia | `graficar_serie` | Grafica 1 a 4 series en un solo eje y guarda el PNG en `figuras/`; rechaza mezclar unidades (nunca usa dos ejes) |
| Recurso | `bcrp://serie/{codigo}` | La ficha de una serie: unidad, fuente original, área del BCRP que la publica, cobertura, fechas y enlace para citarla |
| Recurso | `bcrp://departamento/{ubigeo}` | Las series regionales del BCRP de un departamento, con el **mismo código INEI** que `ubigeo[:2]` de la ENAHO. Mantiene separados Lima (15) y Callao (07) |
| Prompt | `informe(tema)` | Un informe que cita el código y el periodo de cada cifra y dice qué no encontró |

Pruebas: `mcp/test_server.py` tiene las **8 pruebas originales** de la Sesión 04, sin cambios, y **2 pro
… [recortado: 7,152 caracteres más]
```

Resultado:

```text
File created successfully at: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\README.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>🔧 Bash: Check evaluation progress and Part 3 outputs</summary>

```bash
cat "~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/tasks/b2fgp4byb.output" "~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/tasks/bikdf1vev.output"; ls "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4/informes" "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4/figuras"; date +%H:%M
```

Resultado:

```text
A B2: 11.6 s
A B3: 10.8 s
A B4: 11.0 s
A E1: 11.3 s
A E2: 10.7 s
A E3: 12.1 s
A E4: 13.5 s
A M1: 11.6 s
B B1: 28.7 s
B B2: 29.1 s
B B3: 26.2 s
~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4/figuras:
bcrp_PN01273PM_2020-01_2024-12.png
pobreza_por_area_2024.png
pobreza_por_departamento_2024.png
pobreza_por_edad_2024.png
pobreza_por_sexo_2024.png

~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4/informes:
23:05
```

</details>

## 🤖 Claude

Progreso a las 23:05:
- **Modo A:** van 9 de 10, unos 11 s por pregunta.
- **Modo B:** van 3 de 10, unos 28 s por pregunta, porque consulta las herramientas.
- **Parte 3:** el agente ya generó el gráfico del BCRP con `graficar_serie` (`figuras/bcrp_PN01273PM_2020-01_2024-12.png`). Falta el informe.

**Mientras tanto dejé listos:**
- **`evaluacion/registro_experimento.md`:** el diseño y las condiciones de cada modo, con la huella SHA-256 de las respuestas esperadas. Lo escribí **antes** de ver resultados.
- **`evaluacion/ejecutar_evaluacion.py` y `evaluacion/calificar.py`:** las corridas y la calificación con tolerancias definidas de antemano.
- **`README.md`:** los 12 puntos que pide la tarea. Faltan dos secciones, los resultados de la evaluación y el ejemplo de ejecución, que completo cuando terminen las corridas y la Parte 3.

Cuando termine la Parte 3, avísame y exporta con `/export investigacion_agente.txt`. Yo sigo con la verificación de 3 cifras del informe y la comparación de los dos modos en cuanto terminen las corridas.

## 👤 Usuaria

<task-notification>
<task-id>b2fgp4byb</task-id>
<tool-use-id>toolu_01Mj3wxBwRRjPvbTAnLHdpB3</tool-use-id>
<output-file>~\AppData\Local\Temp\claude\0e9f16fe359e3b06\57ecd584-3768-4852-a254-c84910c84d73\tasks\b2fgp4byb.output</output-file>
<status>completed</status>
<summary>Background command "Run Mode A on the remaining nine questions" completed (exit code 0)</summary>
</task-notification>

<details><summary>🔧 Bash: Check Mode B progress and whether the report exists</summary>

```bash
cat "~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/tasks/bikdf1vev.output"; ls -la --time-style=+%H:%M "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4/informes"; date +%H:%M
```

Resultado:

```text
B B1: 28.7 s
B B2: 29.1 s
B B3: 26.2 s
B B4: 28.7 s
total 4
drwxr-xr-x 1 usuario 1049089 0 22:23 .
drwxr-xr-x 1 usuario 1049089 0 23:05 ..
23:05
```

</details>

## 🤖 Claude

El modo A ya terminó las 10 preguntas. El modo B lleva 4 de 10 y le quedan las de la ENAHO, que son más lentas porque usan las Skills. El informe de la Parte 3 todavía no aparece. Son las 23:06.

## 👤 Usuaria

ya salió el informe

<details><summary>🔧 Bash: Locate the report, Part 3 session and evaluation progress</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && ls -la --time-style=+%H:%M informes figuras mapas evidencias_ia/integracion *.txt 2>/dev/null; cat "~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/tasks/bikdf1vev.output"; find ~/.claude/projects -name "*.jsonl" -newermt "2026-11-08 22:58" ! -name "57ecd584*" -printf "%TT %s %p\n" | sort | tail -5; date +%H:%M
```

Resultado:

```text
evidencias_ia/integracion:
total 4
drwxr-xr-x 1 usuario 1049089 0 22:23 .
drwxr-xr-x 1 usuario 1049089 0 22:31 ..

figuras:
total 492
drwxr-xr-x 1 usuario 1049089      0 23:02 .
drwxr-xr-x 1 usuario 1049089      0 23:05 ..
-rw-r--r-- 1 usuario 1049089  80627 23:04 bcrp_PN01273PM_2020-01_2024-12.png
-rw-r--r-- 1 usuario 1049089  75255 23:02 pobreza_por_area_2024.png
-rw-r--r-- 1 usuario 1049089 161930 22:31 pobreza_por_departamento_2024.png
-rw-r--r-- 1 usuario 1049089  90575 22:31 pobreza_por_edad_2024.png
-rw-r--r-- 1 usuario 1049089  76596 22:31 pobreza_por_sexo_2024.png

informes:
total 28
drwxr-xr-x 1 usuario 1049089     0 23:07 .
drwxr-xr-x 1 usuario 1049089     0 23:05 ..
-rw-r--r-- 1 usuario 1049089 22188 23:07 informe_final.md

mapas:
total 268
drwxr-xr-x 1 usuario 1049089      0 22:31 .
drwxr-xr-x 1 usuario 1049089      0 23:05 ..
-rw-r--r-- 1 usuario 1049089 267018 23:02 pobreza_departamento_2024.png
B B1: 28.7 s
B B2: 29.1 s
B B3: 26.2 s
B B4: 28.7 s
B E1: 33.3 s
B E2: 27.0 s
B E3: 43.8 s
23:06:10.3669087000 204774 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/90327a95-c864-43b8-96ff-751e003849df.jsonl
23:06:37.5673942000 209677 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/7f34b5b1-82ca-44f6-b483-c4526576c066.jsonl
23:07:21.3408742000 215566 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/c25a9c26-7809-4608-bca0-5b5c5ab0fe2a.jsonl
23:08:22.8300971000 3151434 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/bb41b986-6df4-4690-b581-dbb7c2268b62.jsonl
23:09:10.1007605000 200004 ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/a6a245e9-f694-49dc-b5c3-ff9d60284eac.jsonl
23:09
```

</details>

<details><summary>🔧 Read</summary>

```json
{
  "file_path": "C:\\Users\\usuario\\GITHUB\\Diplomatura PUCP 2026\\diplomado_python_intermedio\\tarea_4\\informes\\informe_final.md"
}
```

Resultado:

```text
1	# Inflación, cobre y pobreza: Perú 2020-2024, con foco en Arequipa
2	
3	Informe del agente de investigación (Tarea 4). Cifras consultadas el 8 de noviembre de 2026 con el MCP `bcrp` y las
4	skills `graficando-enaho` y `mapeando-enaho`. Todas las cifras salen de una herramienta o de un archivo de salida; no
5	hay cálculos a mano.
6	
7	---
8	
9	## 1. Pregunta, objetivo y delimitación
10	
11	**Pregunta.** ¿Cómo evolucionaron la inflación y la producción de cobre del Perú entre 2020 y 2024, y qué brechas
12	territoriales y entre áreas urbana y rural mostraba la pobreza monetaria en 2024, en particular en Arequipa, uno de los
13	principales productores de cobre del país?
14	
15	**Objetivo.** Describir, con datos oficiales y citados, (a) la trayectoria de la inflación a 12 meses de Lima
16	Metropolitana y de la producción de cobre de Arequipa entre 2020 y 2024, y (b) la pobreza monetaria de 2024 por área
17	(urbana y rural) y por departamento, ubicando a Arequipa en ese mapa.
18	
19	**Delimitación.**
20	
21	| Dimensión | Alcance |
22	|---|---|
23	| Inflación | IPC de Lima Metropolitana, var. % 12 meses, mensual, ene-2020 a dic-2024 (`PN01273PM`) |
24	| Cobre | Producción de cobre de Arequipa, anual, 2020-2024 (`RD15519DA`); contexto: total nacional (`RD15516DA`) y otros cuatro departamentos productores en 2024 |
25	| Pobreza | ENAHO 2024 (INEI), pobreza monetaria de personas, residentes habituales: nacional, urbana/rural y 25 departamentos (Lima 15 y Callao 07 por separado) |
26	| Tipo de análisis | Descriptivo. No se estiman efectos causales |
27	
28	---
29	
30	## 2. Fuentes y metodología
31	
32	### 2.1 Fuentes
33	
34	| Fuente | Qué aporta | Fuente original | Acceso |
35	|---|---|---|---|
36	| BCRP, series estadísticas | Inflación (`PN01273PM`) y producción de cobre (`RD15519DA`, `RD15516DA`, `RD15517DA`, `RD15518DA`, `RD15522DA`, `RD15529DA`) | INEI (IPC); Ministerio de Energía y Minas (cobre) | API del BCRP vía el MCP `bcrp` (`mcp/server.py`) |
37	| INEI, ENAHO 2024 | Pobreza monetaria | INEI, módulos 34 (sumaria) y 02 (miembros del hogar) | `datos/966-Modulo34.zip`, `datos/966-Modulo02.zip` |
38	| GeoJSON departamental del curso | Límites para el mapa | Repositorio del curso | `datos/peru_departamental_simple.geojson` |
39	
40	Fichas del BCRP (recurso `bcrp://serie/{codigo}`):
41	
42	- `PN01273PM`: Índice de precios Lima Metropolitana (var% 12 meses) - IPC. Unidad: var% 12 meses. Fuente original:
43	  INEI. Publica: BCRP, Departamento de Estadísticas de Pr
… [recortado: 20,600 caracteres más]
```

</details>

<details><summary>🔧 Bash: List tools and skills used in the Part 3 session</summary>

```bash
python -I -c "
import json,sys; sys.stdout.reconfigure(encoding='utf-8')
for l in open(sys.argv[1],encoding='utf-8'):
    d=json.loads(l)
    if d.get('type')=='assistant':
        for b in d['message']['content']:
            if b.get('type')=='tool_use':
                i=b['input']; print('TOOL', b['name'], (i.get('skill') or i.get('command') or i.get('file_path') or json.dumps(i,ensure_ascii=False))[:120].replace(chr(10),' '))
    if d.get('type')=='user' and isinstance(d['message']['content'],str): print('USER', d['message']['content'][:90].replace(chr(10),' '))
" ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/bb41b986-6df4-4690-b581-dbb7c2268b62.jsonl | head -60
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Write</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\informes\verificar_informe.py

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

```

Resultado:

```text
File created successfully at: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\informes\verificar_informe.py (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>🔧 Bash: Independently verify report figures and check Mode B</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && uv run informes/verificar_informe.py; grep -E "^(04|06|11)," .claude/skills/mapeando-enaho/referencia/pobreza_departamento_2024.csv; cat "~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/tasks/bikdf1vev.output" | tail -3; date +%H:%M
```

Resultado:

```text
PN01273PM 2020-2024: primero ('Ene.2020', 1.88835605229068) último ('Dic.2024', 1.96630270142824) máximo ('Jun.2022', 8.81263294388897) promedio 4.47
RD15519DA [('2020', 556642.362777179), ('2021', 422079.19657724), ('2022', 463461.80659043), ('2023', 470380.220791986), ('2024', 453836.336219)] variación % 2020-2024: -18.47
RD15516DA [('2020', 2149115.61282999), ('2021', 2297741.5701674), ('2022', 2438964.16997026), ('2023', 2745744.80261672), ('2024', 2732642.16018559)] variación % 2020-2024: 27.15
ENAHO sumaria: Perú 27.58 | urbana 24.81 | rural 39.3 | Arequipa 15.78 | Cajamarca 45.01 | Ica 6.01
04,AREQUIPA,15.8
06,CAJAMARCA,45.0
11,ICA,6.0
B E2: 27.0 s
B E3: 43.8 s
B E4: 148.9 s
23:10
```

</details>

## 🤖 Claude

Todas las cifras del informe coinciden con las fuentes independientes. Las registro en el documento de verificación.

<details><summary>🔧 Bash: Write the manual verification document for the report</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && cat > informes/verificacion.md <<'EOF'
# Verificación de las cifras del informe final

Se comprobaron 8 afirmaciones numéricas de `informe_final.md`: 4 del BCRP y 4 de la ENAHO. La verificación usa fuentes
**independientes del agente**:
- **BCRP:** la API de estadisticas.bcrp.gob.pe consultada directamente, sin el MCP.
- **ENAHO:** un cálculo mínimo desde el zip del INEI, separado de `limpiar.py`, con el método oficial de la sumaria, y la
  referencia de la Sesión 16.

    uv run informes/verificar_informe.py

Ejecutado el 8 de noviembre de 2026.

| # | Afirmación del informe | Valor en el informe | Valor verificado | Fuente o procedimiento | ¿Coincide? | Diferencia |
|---|---|---:|---:|---|:-:|---|
| 1 | Inflación a 12 meses de Lima, ene-2020 → dic-2024 (Hallazgo 1) | 1.89 % → 1.97 % | 1.888 % → 1.966 % | API BCRP `PN01273PM` | ✅ | Redondeo |
| 2 | Máximo de la inflación 2020-2024 (Hallazgo 1) | 8.81 % en jun-2022 | 8.813 % en Jun.2022 | API BCRP `PN01273PM` | ✅ | — |
| 3 | Cobre de Arequipa 2020 → 2024: −18.47 % (Hallazgo 2) | 556,642 → 453,836 tm.f | 556,642.4 → 453,836.3 | API BCRP `RD15519DA` | ✅ | — |
| 4 | Cobre nacional 2020 → 2024: +27.15 % (Hallazgo 2) | 2,149,116 → 2,732,642 tm.f | 2,149,115.6 → 2,732,642.2 | API BCRP `RD15516DA` | ✅ | — |
| 5 | Pobreza nacional 2024 (§3.5) | 27.53 % (facpob07) · 27.58 % (sumaria) | 27.58 % (sumaria) · 27.6 % INEI | Cálculo independiente desde el zip + cifra oficial | ✅ | 0.07 pp con facpob07, dentro de ±0.1 |
| 6 | Pobreza rural 2024 (Hallazgo 3) | 39.44 % (facpob07) · 39.30 % (sumaria) | 39.30 % (sumaria) · 39.3 % INEI | Ídem | ✅ con la sumaria | 0.14 pp con facpob07, por la unidad de ponderación |
| 7 | Pobreza de Arequipa 2024 (Hallazgo 4) | 15.77 % (facpob07) · 15.78 % (sumaria) | 15.78 % · referencia 15.8 % | Ídem + `pobreza_departamento_2024.csv` (Sesión 16) | ✅ | — |
| 8 | Rango territorial: Cajamarca 44.99 % e Ica 5.91 % (Hallazgo 4) | 44.99 % / 5.91 % | 45.01 % / 6.01 % (sumaria) · ref. 45.0 / 6.0 | Ídem | ✅ | Ica difiere 0.1 pp por la ponderación (facpob07) |

**Conclusión:** las 8 cifras coinciden con su fuente. Las únicas diferencias, de 0.1 a 0.14 pp, vienen de ponderar por
persona (`facpob07`) en lugar de por hogar (`factor07 × mieperho`), y el informe ya las explica en §3.5 y §6.

**Fallas de herramientas:** durante la ejecución, una llamada a `resumen` (PN01273PM, 2021) recibió «El BCRP no
respondió con datos». El agente la repitió en vez de estimar el dato y lo registró en §2.2 del informe.
EOF
echo ok
```

Resultado:

```text
ok
```

</details>

## 🤖 Claude

Mientras el modo B termina sus dos últimas preguntas, exporto el registro completo de la ejecución de la Parte 3.

<details><summary>🔧 Bash: Export Part 3 session transcript and check Mode B</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad" && python -I evidencias_ia/exportar_conversacion.py ~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio-tarea-4/bb41b986-6df4-4690-b581-dbb7c2268b62.jsonl evidencias_ia/integracion/02_investigacion_agente_completa.md "Parte 3: ejecución integrada del agente (MCP bcrp + Skills ENAHO) que produjo informes/informe_final.md" "$S/ocultar.txt"; ls *.txt 2>/dev/null; cat "~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/tasks/bikdf1vev.output" | tail -2
```

Resultado:

```text
evidencias_ia/integracion/02_investigacion_agente_completa.md: 684 l�neas
B E4: 148.9 s
B M1: 34.9 s
```

</details>

<details><summary>🔧 Edit</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\README.md
--- antes ---
<!-- EJEMPLO -->
--- después ---
La Parte 3 se resolvió en **una sola sesión** de Claude Code abierta en `tarea_4/`. El registro completo está en
`evidencias_ia/integracion/02_investigacion_agente_completa.md`. Recibió la pregunta de investigación e hizo esto:

1. **Plan.** Qué series del BCRP y qué indicadores de la ENAHO necesitaba, y con qué herramienta obtendría cada uno.
2. **MCP `bcrp`:**
   - `buscar_series` → `PN01273PM` (inflación de Lima) y las series de cobre.
   - Recurso `bcrp://departamento/04` → las series de Arequipa, como `RD15519DA` (cobre anual).
   - Recursos `bcrp://serie/...` → unidad y fuente de cada serie.
   - `resumen` y `serie` → las cifras 2020-2024, sin cuentas a mano.
   - `graficar_serie` → `figuras/bcrp_PN01273PM_2020-01_2024-12.png`.
3. **Skills:** `graficando-enaho` hizo el gráfico por área y `mapeando-enaho` el mapa por departamento; las dos usan la
   base de `limpiando-enaho`.
4. **Contraste** con `salidas/validacion.txt` y con la referencia de la Sesión 16.
5. **Informe:** escribió [`informes/informe_final.md`](informes/informe_final.md), con 4 hallazgos, 3 figuras,
   interpretación, limitaciones y reproducibilidad.

Durante la ejecución, una llamada a la API del BCRP falló («El BCRP no respondió con datos»). El agente la repitió y lo
dejó escrito en el informe en vez de estimar el dato.

**Verificación manual:** [`informes/verificacion.md`](informes/verificacion.md) comprueba 8 cifras del informe, 4 del
BCRP y 4 de la ENAHO, con la API del BCRP consultada directamente y un cálculo independiente desde los microdatos.
Coinciden las 8.

Hallazgos principales:
- **Inflación de Lima:** pasó de 1.89 % (ene-2020) a un máximo de 8.81 % (jun-2022) y cerró 2024 en 1.97 %.
- **Cobre:** Arequipa produjo 18.47 % menos en 2024 que en 2020, mientras la producción nacional creció 27.15 %.
- **Pobreza por área:** la rural (39.4 %) supera a la urbana (24.7 %) en 14.7 pp.
- **Pobreza por departamento:** va de 5.9 % en Ica a 45.0 % en Cajamarca. Arequipa, con 15.8 %, es el quinto
  departamento con menos pobreza.

Son asociaciones descriptivas: el informe no afirma causalidad.
```

Resultado:

```text
The file ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\README.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>🔧 Bash: Check whether Mode B finished the last question</summary>

```bash
cat "~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/tasks/bikdf1vev.output" | tail -1; date +%H:%M:%S
```

Resultado:

```text
B M1: 34.9 s
23:11:16
```

</details>

## 🤖 Claude

La Parte 3 ya está documentada:
- `informes/informe_final.md`, escrito por el agente.
- `informes/verificacion.md` y `informes/verificar_informe.py`, con la verificación de las 8 cifras.
- `evidencias_ia/integracion/02_investigacion_agente_completa.md`, con el registro completo de la ejecución.
- La sección «Ejemplo de una ejecución completa» del README.

El modo B está en la última pregunta (M2). Cuando termine, califico y escribo la comparación. Son las 23:11.

## 👤 Usuaria

<task-notification>
<task-id>bikdf1vev</task-id>
<tool-use-id>toolu_01MYMobnWa2JUTugjTmFz2Ck</tool-use-id>
<output-file>~\AppData\Local\Temp\claude\0e9f16fe359e3b06\57ecd584-3768-4852-a254-c84910c84d73\tasks\bikdf1vev.output</output-file>
<status>completed</status>
<summary>Background command "Run Mode B on all ten questions" completed (exit code 0)</summary>
</task-notification>

<details><summary>🔧 Bash: Copy pre-registered answers, grade, and print all responses ⚠️ error</summary>

```bash
S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad"; cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && cp "$S/eval/preguntas.csv" evaluacion/preguntas.csv && sha256sum evaluacion/preguntas.csv && python -I evaluacion/calificar.py && python -I -c "
import csv,sys; sys.stdout.reconfigure(encoding='utf-8')
for r in csv.DictReader(open('evaluacion/resultados.csv',encoding='utf-8')):
    print(f\"--- {r['modo']} {r['id']} [{r['correcto']}] {r['herramientas_usadas'][:90]}\n{r['respuesta_generada'][:420]}\")
"
```

Resultado:

```text
Exit code 1
ca410402cae8b57c2a2d7d8d887a06272678c6b7b45713b46d2a1443c60105c1 *evaluacion/preguntas.csv
Modo A: 5/10 correctas � tiempo promedio 11.7 s
Traceback (most recent call last):
  File "~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evaluacion\calificar.py", line 127, in <module>
    main()
    ~~~~^^
  File "~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evaluacion\calificar.py", line 123, in main
    print(f"  {f['id']} {'\u2714' if f['correcto'] else '\u2718'} {f['tiempo_s']} s � {f['criterio']} � {f['fuente_utilizada']}")
    ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "~\AppData\Local\anaconda3\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode character '\u2714' in position 5: character maps to <undefined>
```

</details>

## 🤖 Claude

Las respuestas esperadas mantienen la misma huella SHA-256, así que no se modificaron. El calificador falló por el mismo problema de consola de Windows que vimos antes; lo corrijo.

<details><summary>🔧 Bash: Fix console encoding in grader, grade, print responses</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && sed -i 's/^def main():$/def main():\n    sys.stdout.reconfigure(encoding="utf-8")/; s/^import re$/import re\nimport sys/' evaluacion/calificar.py && python -I evaluacion/calificar.py && python -I -c "
import csv,sys; sys.stdout.reconfigure(encoding='utf-8')
for r in csv.DictReader(open('evaluacion/resultados.csv',encoding='utf-8')):
    print(f\"--- {r['modo']} {r['id']} [{r['correcto']}] {r['herramientas_usadas'][:90]}\n{r['respuesta_generada'][:420]}\")
"
```

Resultado:

```text
Modo A: 5/10 correctas · tiempo promedio 11.7 s
  B1 ✔ 10.3 s · cifras dentro de la tolerancia · Conocimiento del modelo (sin herramientas de datos)
  B2 ✔ 11.6 s · cifras dentro de la tolerancia y etiquetas presentes · Conocimiento del modelo (sin herramientas de datos)
  B3 ✘ 10.8 s · no contestada: dice no poder verificar · Conocimiento del modelo (sin herramientas de datos)
  B4 ✔ 11.0 s · cifras dentro de la tolerancia · Conocimiento del modelo (sin herramientas de datos)
  E1 ✔ 11.3 s · cifras dentro de la tolerancia · Conocimiento del modelo (sin herramientas de datos)
  E2 ✘ 10.7 s · no contestada: dice no poder verificar · Conocimiento del modelo (sin herramientas de datos)
  E3 ✘ 12.1 s · no contestada: dice no poder verificar · Conocimiento del modelo (sin herramientas de datos)
  E4 ✘ 13.5 s · falta o fuera de tolerancia: 108664.0 · Conocimiento del modelo (sin herramientas de datos)
  M1 ✔ 11.6 s · cifras dentro de la tolerancia y etiquetas presentes · Conocimiento del modelo (sin herramientas de datos)
  M2 ✘ 14.2 s · no contestada: dice no poder verificar · Conocimiento del modelo (sin herramientas de datos)
Modo B: 9/10 correctas · tiempo promedio 46.0 s
  B1 ✔ 28.7 s · cifras dentro de la tolerancia · MCP bcrp: buscar_series, serie
  B2 ✔ 29.1 s · cifras dentro de la tolerancia y etiquetas presentes · MCP bcrp: buscar_series, resumen
  B3 ✔ 26.2 s · cifras dentro de la tolerancia · MCP bcrp: buscar_series, serie
  B4 ✔ 28.7 s · cifras dentro de la tolerancia · MCP bcrp: buscar_series, serie
  E1 ✔ 33.3 s · cifras dentro de la tolerancia · Sin herramientas
  E2 ✔ 27.0 s · cifras dentro de la tolerancia · Sin herramientas
  E3 ✔ 43.8 s · cifras dentro de la tolerancia y etiquetas presentes · archivos/scripts del proyecto
  E4 ✔ 148.9 s · cifras dentro de la tolerancia · archivos/scripts del proyecto
  M1 ✘ 34.9 s · falta: rechazo de causalidad · MCP bcrp: serie
  M2 ✔ 59.0 s · cifras dentro de la tolerancia y etiquetas presentes · MCP bcrp: buscar_series, resumen; archivos/scripts del proyecto
--- A B1 [1] ninguna
**1,97 %** de inflación a 12 meses (variación del IPC de Lima Metropolitana, diciembre de 2024 frente a diciembre de 2023). Es también la inflación acumulada del año 2024. La fuente es el INEI (Instituto Nacional de Estadística e Informática del Perú), en su informe técnico de variación de precios de enero de 2025. Lo di de memoria. No tengo acceso a la web en esta sesión, así que no pude verificarlo en la pu
… [recortado: 8,776 caracteres más]
```

</details>

<details><summary>🔧 Bash: Print full mixed-question answers for manual review</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && python -I -c "
import csv,sys; sys.stdout.reconfigure(encoding='utf-8')
for r in csv.DictReader(open('evaluacion/resultados.csv',encoding='utf-8')):
    if (r['modo'],r['id']) in {('A','M1'),('B','M1'),('B','M2'),('A','M2'),('B','E1')}:
        print(f\"=== {r['modo']} {r['id']} [{r['correcto']}] {r['herramientas_usadas']}\n{r['respuesta_generada']}\n\")
"
```

Resultado:

```text
=== A M1 [1] ninguna
No pude consultar las fuentes en línea en esta sesión, así que estas cifras salen de mi memoria y no las verifiqué. Confírmalas antes de citarlas. - **Inflación a 12 meses, Lima Metropolitana, diciembre de 2024:** alrededor de 2,0 % (recuerdo 1,97 %). Fuente: BCRP, con datos del INEI. - **Pobreza monetaria nacional, 2024:** alrededor de 27,6 % de la población, frente a 29,0 % en 2023. Fuente: INEI, ENAHO. **¿Se concluye que la baja inflación redujo la pobreza?** No. Son dos datos descriptivos que coinciden en el tiempo, y eso no prueba causalidad. Además, la inflación de Lima no es la inflación que enfrentan los hogares de todo el país. La pobreza también depende de otros factores, como el empleo, los ingresos, el crecimiento y las transferencias, y el INEI mide la pobreza con una canasta de gasto, no con la inflación. Para sostener una relación causal haría falta un análisis específico, por ejemplo con la inflación de la canasta de alimentos y de otras regiones.

=== A M2 [0] ninguna
No pude obtener ni verificar ninguna de las dos cifras. En esta sesión no tengo acceso a internet, así que no puedo consultar el BCRP (series de producción minera) ni el INEI (ENAHO, pobreza monetaria departamental 2024). Prefiero no darle números de memoria que parezcan oficiales. **Qué se puede decir de la relación** - **Producción:** Arequipa es uno de los principales productores de cobre del país, sobre todo por Cerro Verde. Es una impresión general, no una cifra verificada. - **Pobreza:** en los últimos años Arequipa ha estado entre los departamentos con menor pobreza monetaria. Tampoco tengo el dato de 2024 confirmado. - **Relación:** no se puede afirmar causalidad con solo estos dos datos. Una alta producción de cobre puede coincidir con menor pobreza por los empleos, el canon y el dinamismo regional. Pero Arequipa también tiene otros sectores fuertes (servicios, comercio, agroindustria, manufactura). Además, las ENAHO departamentales tienen márgenes de error, y la minería está muy concentrada en pocas provincias. **Dónde obtener los datos** - BCRP: *Cuadros Anuales/Mensuales Regionales*, "Producción de cobre (TMF) – Arequipa". Para el promedio mensual de 2024, sume los 12 meses y divida entre 12. - INEI: informe técnico "Evolución de la pobreza monetaria 2015-2024", cuadro por departamentos. Si me comparte los datos o habilita una herramienta de búsqueda web, calculo el promedio y armo la comparación.

=== B E1 [1] Grep
La tasa de pobreza m
… [recortado: 2,997 caracteres más]
```

</details>

## 👤 Usuaria

This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summary:
1. Primary Request and Intent:
   - The user (Adriana Garcés García, GitHub @dgarcesg) is completing **Tarea 4** of the PUCP Python Intermedio course (issue https://github.com/d2cml-ai/Data-Science-Python/issues/201). The deadline is **Sunday 8 Nov 2026, 11:59 pm Peru time (UTC-5)**. Late work loses −2 pts/day and needs justified authorization.
   - Deliverable: `tarea_4/` folder in repo `dgarcesg/diplomado_python_intermedio`, containing four parts:
     - Part 1, BCRP MCP server (5 pts): ≥4 tools including an own tool, a resource, a prompt, `.mcp.json`, and 8 original + 2 own tests = "10 passed".
     - Part 2, three Skills (6 pts): `limpiando-enaho`, `graficando-enaho`, `mapeando-enaho`, validated against 27.6 % / 108,664 / 25 units, with coordination between them.
     - Part 3, integrated agent run (5 pts): ≥2 MCP tools + ≥2 Skills in one run; `informes/informe_final.md` with 7 sections, ≥3 findings, a BCRP chart, an ENAHO chart and a map; ≥3 numbers verified manually.
     - Part 4, evaluation (4 pts): 10 questions (4 BCRP, 4 ENAHO, 2 mixed); `evaluacion/preguntas.csv`, `resultados.csv`, `comparacion.md`; Mode A without MCP/Skills vs Mode B with them; a 12-point README; complete `evidencias_ia/`.
   - Delivery is a comment on the issue, in this format:
     ```
     ### Tarea 4 – Individual
     **Estudiante:** Nombre completo (@usuario_github)
     **Pregunta de investigación:** ...
     **Repositorio de GitHub:** ...
     **Informe final:** .../informes/informe_final.md
     **Pruebas MCP:** XX/10 aprobadas
     **Validación ENAHO:** Pobreza nacional 2024 XX.X % · Residentes habituales XX,XXX · Unidades territoriales XX/25
     **Evaluación del agente:** Sin MCP/Skills X/10 · Con MCP/Skills X/10 · Resultados completos: .../evaluacion/resultados.csv
     **Evidencia de integración MCP + Skills:** ...
     **Evidencias de uso de IA:** ...
     ```
   - User wants me to "ir documentando nuestras conversaciones en un markdown": the AI evidence must be kept up to date in `evidencias_ia/`.
   - The user handles commits, pushes and merges themselves. They asked me to check git state each time, and I ran local git commands only with explicit approval.
   - **SECURITY/PRIVACY CONSTRAINTS (verbatim intent):**
     - "no descargues los comentarios": never download or read issue comments, which are other students' submissions. Read only the issue body via `/issues/{n}`, never `/issues/{n}/comments`.
     - The task requires hiding API keys, passwords, tokens, personal data and confidential info before publishing conversations.
     - Do not upload raw microdata.
     - Commit or push only when the user asks; the user does git themselves.

2. Key Technical Concepts:
   - **FastMCP 4.1.4:**
     - Decorators `@mcp.tool`, `@mcp.resource` (templates `bcrp://serie/{codigo}`, `bcrp://departamento/{ubigeo}`) and `@mcp.prompt`.
     - `ToolError` and `ResourceError`.
     - In-memory `Client(mcp)` for tests.
     - Decorated functions remain directly callable (`resumen` calls `serie`).
   - **BCRP API:**
     - Endpoint `https://estadisticas.bcrp.gob.pe/estadisticas/series/api/{codigo}/json/{desde}/{hasta}`.
     - Catalog at `/metadata`, cached in `mcp/datos/catalogo_bcrp.csv`.
     - The catalog's "Fecha de fin" lags behind the API.
     - Regional series have codes starting with RD and Geografía "RE".
   - **World Bank API** for `comparar_paises`.
   - **Claude Code specifics:**
     - `.mcp.json` and `.claude/skills/` load only when Claude Code is opened **inside `tarea_4/`**.
     - `/export` failed when given a subfolder (ENOENT).
     - Sessions are stored as `.jsonl` in `~/.claude/projects/<dir>/<session>.jsonl`.
     - `claude -p` flags used: `--strict-mcp-config`, `--mcp-config`, `--allowedTools`, `--disallowedTools`, `--model sonnet`, `--output-format stream-json --verbose`; the prompt is passed via stdin.
   - **ENAHO 2024** (INEI code 966):
     - Module 34: `966-Modulo34/sumaria-2024.dta`, not `-12g`. Module 02: `966-Modulo02/enaho01-2024-200.dta`.
     - Keys `conglome`(6), `vivienda`(3), `hogar`(2), `codperso`(2), `ubigeo`(6), read as pandas `str` dtype.
     - Residents filter `((p204==1)&(p205==2))|((p204==2)&(p206==1))`.
     - Merge with `validate="m:1"`. Urban = `estrato <= 5`. Poor = `pobreza <= 2`.
     - Weights: `facpob07` (persons) vs `factor07×mieperho` (sumaria/INEI official). The Session 16 references are sumaria-based.
   - **Results:**
     - National poverty 27.53 % (facpob07) / 27.58 % (sumaria).
     - Urban/rural 24.74/39.44 (persons) vs 24.81/39.30 (sumaria).
     - 108,664 residents; 34.15 M expanded population; extreme poverty 5.5 %.
     - Departments: Cajamarca 44.99, Ica 5.91, Arequipa 15.77, Cusco 18.54.
   - **GeoPandas join:** `ubigeo[:2]` = `FIRST_IDDP` (text); 25 units; Lima 15 and Callao 07 kept separate.
   - **dataviz skill rules:** single blue `#2a78d6`; ink `#0b0b0b`/`#52514e`; surface `#fcfcfb`; sequential blue ramp for the choropleth from 0; no dual axis.
   - **Windows cp1252 console** crashes when printing Unicode. Fix: `sys.stdout.reconfigure(encoding="utf-8")`. Also, `python -I` ignores `PYTHONIOENCODING`.

3. Files and Code Sections (all under `~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\`):

   - **`mcp/server.py`**: the MCP server.
     - Base: copied from MCP-BCRP minus its old resources.
     - Imports: `json`, `ResourceError`.
     - `catalogo()` renames extra columns: `fin`, `unidad`, `escala`, `fuente`, `area`, `publicacion`, `geografia`.
     - `_fila(codigo)` raises `ToolError` if the code is missing; `_ficha` uses it.
     - Instructions mention both resources.
     - Tools: `buscar_series`, `serie`, `resumen`, `comparar_paises`, and the new `graficar_serie(codigos, desde, hasta, titulo=None)`.
       - `graficar_serie` takes 1–4 series; it rejects mixed frequencies or units (no dual axis).
       - It saves `figuras/bcrp_<codes>_<desde>_<hasta>.png` (200 dpi) and returns `{"archivo", "series":[primero, ultimo, maximo, minimo, fuente]}`.
     - Resource `ficha_serie` at `bcrp://serie/{codigo}`. Returns JSON with:
       - `codigo`, `nombre`, `categoria`, `grupo`, `frecuencia`;
       - `unidad`, from the catalog or from the parentheses in the name;
       - `cobertura`, `fuente_original`, `publica`, `publicacion`;
       - `inicio`, `fin_segun_catalogo`, `actualizada`;
       - `enlace`, as `{WEB}/{mensuales|...}/resultados/{codigo}/html`.
     - Resource `series_departamento` at `bcrp://departamento/{ubigeo}`:
       - Accepts the INEI 2-digit code or a department name; `DEPARTAMENTOS` dict 01–25.
       - Uses regional series with `geografia=="RE"` and `fin[-4:]>="2024"`.
       - Matches the department name by word in the series name.
       - Separates `combinadas_lima_callao` from `temas`, which are grouped by `grupo`.
     - Prompt `informe(tema)`.
   - **`mcp/test_server.py`**: the 8 original tests, unchanged (verified with diff), plus 2 own tests:
     - `test_comparar_paises_trae_cada_pais_y_su_promedio`: PER;CHL, 2019–2021; Peru 2020 ≈ −10.93 ± 0.05; checks the average and the source.
     - `test_comparar_paises_indicador_inexistente_da_un_error_claro`.
     - Result: 10 passed.
   - **`pyproject.toml`**:
     - Project `tarea-4-agente-socioeconomico`.
     - Dependencies: `fastmcp>=4,<5`, `httpx`, `matplotlib>=3.11.2`, `pandas`, plus `pyarrow` and `geopandas` added via `uv add`.
     - Dev dependency `pytest`; `[tool.pytest.ini_options] testpaths=["mcp"]`.
   - **`.mcp.json`**: `bcrp` (`uv run mcp/server.py`) and `fetch` (`uvx mcp-server-fetch`). The user approved only `bcrp`; `settings.local.json` lists `fetch` as disabled.
   - **`.gitignore`**: `.venv/`, `__pycache__/`, `.pytest_cache/`, `datos/`, `.claude/settings.local.json`, `salidas/*.parquet`.
   - **`.claude/skills/limpiando-enaho/`**: `SKILL.md`, `reference.md`, `scripts/limpiar.py`.
     - `RAIZ = Path(__file__).resolve().parents[4]`.
     - `leer(zip_path, archivo)` reads the exact `.dta` name from the zip without extracting; lowercases names; maps `año`→`anio`.
     - 15 checks (essential and informative): key dtypes and lengths, unique keys, residents == 108,664, merge preserves rows and every person finds a household, 25 codes, factor complete and positive, expanded population 30–37 M, national poverty ±0.1, sumaria ±0.1, urban/rural via sumaria ±0.1, weighted ≠ simple.
     - On an essential failure: deletes the parquet, writes `validacion.txt`, exits 1.
     - Otherwise writes `salidas/personas_2024.parquet`, `salidas/indicadores.csv` (with a `pobreza_pct_sumaria` column for nacional/área/departamento via `indicadores(p, hog)`) and `salidas/validacion.txt`.
     - `sys.stdout.reconfigure(encoding="utf-8")` in `main()`.
   - **`.claude/skills/graficando-enaho/`**: `SKILL.md`, `scripts/graficar.py`.
     - Options: `--por area|sexo|edad|departamento|todos` and `--indicador pobreza|pobreza_extrema`.
     - Weighted rates; analytic titles computed from the data (`textwrap.fill` at 70 horizontal / 85 vertical; fontsize 12 / 11); `NOMBRE_GRUPO` for accents.
     - National dashed line, noted in the subtitle; value labels with a `CAJA` bbox; source footnote; 200 dpi output to `figuras/`.
   - **`.claude/skills/mapeando-enaho/`**: `SKILL.md`, `scripts/mapa.py`, `referencia/pobreza_departamento_2024.csv` (copied from Session 16).
     - Downloads the GeoJSON to `datos/` if missing; merge `validate="1:1"`; requires 25 units with data and both 07 and 15.
     - Blue ramp, `vmin=0`; Callao label annotated offshore.
     - Writes `salidas/comparacion_mapa_referencia.csv` (both methods vs the reference; 25/25 with sumaria, 16/25 with facpob07, max 0.5 pp). Exits with an error only if the sumaria method mismatches.
   - **Outputs:**
     - `figuras/`: `pobreza_por_{area,sexo,edad,departamento}_2024.png` and `bcrp_PN01273PM_2020-01_2024-12.png` (from the Part 3 run).
     - `mapas/pobreza_departamento_2024.png`.
     - `salidas/`: `validacion.txt`, `indicadores.csv`, `comparacion_mapa_referencia.csv`.
   - **`informes/informe_final.md`**: written by the agent in Part 3 (session `bb41b986`).
     - Question about inflation and copper 2020–2024, focused on **Arequipa**.
     - Uses PN01273PM, RD15519DA (Arequipa annual copper) and RD15516DA (national), plus 2024 values for Moquegua, Áncash, Apurímac and Cusco.
     - 4 findings:
       - inflation 1.89→1.97 %, max 8.81 % in jun-2022, average 4.47 %;
       - Arequipa copper −18.47 % vs national +27.15 %;
       - rural 39.4 % vs urban 24.7 %;
       - range Ica 5.91 to Cajamarca 44.99; Arequipa 15.77 %, 5th lowest.
     - 3 figures, 7 sections; a documented API failure and retry.
   - **`informes/verificar_informe.py`** and **`informes/verificacion.md`**: 8 claims verified independently (direct BCRP API; minimal sumaria calculation from the zip). All match.
   - **`evaluacion/`**:
     - `preguntas.csv`: copied from scratchpad after the runs; sha256 `ca410402cae8b57c2a2d7d8d887a06272678c6b7b45713b46d2a1443c60105c1`, verified identical. Columns: `id`, `tipo`, `pregunta`, `respuesta_esperada`, `valores_esperados`, `tolerancia`, `etiquetas_requeridas`, `verificacion`. Questions:
       - B1: inflation Dec-2024 = 1.97 ±0.05.
       - B2: max 8.81 in junio 2022.
       - B3: exchange rate Dec-2024 = 3.737 ±0.005 (PN01206PM).
       - B4: reference rate 5.00 ±0.01 (PD04722MM).
       - E1: national poverty 27.6 ±0.1.
       - E2: rural poverty 39.3 ±0.2.
       - E3: Cajamarca 45.0 ±0.2.
       - E4: residents 108664 exact.
       - M1: 1.97 and 27.6, plus "no causal".
       - M2: Arequipa copper 37819.7 ±400 tm.f and 15.8 ±0.2, plus "no causal".
     - `mcp_bcrp.json`: only the `bcrp` server.
     - `registro_experimento.md`: written before results; records the hash, the conditions table and the grading criteria.
     - `ejecutar_evaluacion.py`: `MODELO="sonnet"`; `INSTRUCCION` appended to each question. Modes:
       ```python
       COMUNES = ["claude", "-p", "--model", MODELO, "--output-format", "stream-json", "--verbose"]
       MODOS = {
           "A": COMUNES + ["--strict-mcp-config", "--disallowedTools", "Skill", "Bash", "PowerShell", "WebSearch", "WebFetch", "Write", "Edit", "NotebookEdit", "Agent"],
           "B": COMUNES + ["--mcp-config", str(TAREA4 / "evaluacion" / "mcp_bcrp.json"), "--strict-mcp-config",
                           "--allowedTools", "mcp__bcrp", "ListMcpResourcesTool", "ReadMcpResourceTool", "Skill", "Bash", "Read", "Glob", "Grep",
                           "--disallowedTools", "WebSearch", "WebFetch", "Agent"],
       }
       ```
       - Mode A runs in the empty folder `scratchpad/modo_a_vacio`; Mode B runs in `tarea_4/`.
       - Each run is saved as `evaluacion/corridas/{A|B}_{id}.jsonl` plus `.meta.json` (seconds, error, model, cwd, start time). Option `--solo` reruns selected ids.
     - `calificar.py`:
       - Parses the corridas; `candidatos()` reads numbers in both decimal conventions.
       - Tolerance checks; label groups; a `CAUSAL` regex for "no causal"; a `NO_SABE` regex for "not answered".
       - `fuente()` summarizes the tools used.
       - Optional `revision_manual.csv` (id, modo, correcto, nota) overrides the automatic grade.
       - Writes `resultados.csv` with columns `id`, `tipo`, `modo`, `pregunta`, `respuesta_esperada`, `respuesta_generada`, `fuente_utilizada`, `herramientas_usadas`, `correcto`, `criterio`, `tiempo_s`, `error`.
       - `import sys` and `sys.stdout.reconfigure(encoding="utf-8")` in `main()` were just added via sed.
   - **`README.md`**: written with all 12 sections. It contains the placeholder `<!-- EVAL -->` in section 9, which is still to be filled. Section 11 (example run) is already filled.
   - **`evidencias_ia/`**:
     - `00_sesion_principal_claude_code.md` (needs regeneration at the end) and `exportar_conversacion.py`.
     - `exportar_conversacion.py` usage: `python -I evidencias_ia/exportar_conversacion.py <jsonl> <salida.md> "<título>" [ocultar.txt]`. It redacts emails, `~`→`~`, `usuario`→`usuario`, org/account UUIDs and the terms file. It omits results of tool inputs containing `/comments`, `comments.json`, `issue.txt` or `json.loads(l)`.
     - `mcp/`: `01_demo_mcp_claude_code.txt`, `02_demo_mcp_claude_code_completa.md`, `03_verificacion_demo.md`, `verificar_demo.py`.
     - `skills/`: `01_demo_skills_claude_code.txt`, `02_demo_skills_claude_code_completa.md`, `04_coordinacion_grafico_completa.md`.
     - `integracion/02_investigacion_agente_completa.md`.
   - **Scratchpad** (`~\AppData\Local\Temp\claude\0e9f16fe359e3b06\57ecd584-3768-4852-a254-c84910c84d73\scratchpad`):
     - `ocultar.txt`: classmate logins plus the org UUID fragment. Must never be committed.
     - `eval/preguntas.csv`, `modo_a_vacio/`, `verificar_demo.py`, `probar_recursos.py`, `probar_grafico.py`.
   - **Session transcripts:**
     - Main session: `~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/57ecd584-3768-4852-a254-c84910c84d73.jsonl`.
     - tarea_4 project dir sessions: `7bfebfb8` (MCP demo), `7e4804b7` (skills demo), `00a46994` (graph coordination), `bb41b986` (Part 3), plus the eval `-p` sessions.
     - Wrong-cwd sessions (repo root, not valid as skill evidence): `1949a996`, `18d888ac`.
   - **Memory dir:**
     - Added `no-descargar-comentarios-issue.md` and its index line.
     - Deleted the stale `enaho-skills-utf8-consola.md` (written by another session) and its index line.

4. Errors and fixes:
   - `gh` CLI not installed → used curl on the GitHub API.
   - cp1252 `UnicodeEncodeError` occurred several times:
     - PYTHONIOENCODING (ineffective with `python -I`) → `sys.stdout.reconfigure`.
     - The scripts' final prints made `limpiar.py` exit 1 in the skills demo → added `reconfigure` to all 3 skill scripts.
     - `calificar.py` → added `import sys` and `reconfigure` via sed.
   - **Downloaded issue comments before the user objected** ("no descargues los comentarios") → deleted the files, excluded them from exports, saved a memory, added a terms redaction list.
   - Wrong `.dta` picked (`sumaria-2024-12g`) → exact filename match.
   - Key dtype check used `object` → `pd.api.types.is_string_dtype`.
   - Rural poverty and department map mismatched the references → discovered the references are sumaria-based; both methods are reported, and the comparison uses both.
   - Chart titles truncated, missing accent, label overflow and overlap → `textwrap`, `NOMBRE_GRUPO`, national value moved to the subtitle, `CAJA` bbox.
   - The org UUID leaked in an exported tool result → redaction regex, omission of `json.loads(l)` inspection results, terms file.
   - Branch `parte-2-skills-enaho` was created before the Part 1 merge, and later local main was behind origin → with user approval: `git merge --ff-only origin/main`, then `git pull --ff-only`; deleted merged local branches; created `parte-3-agente` from updated main.
   - The user opened Claude Code at the repo root twice, so Skills and MCP did not load → instructed opening in `tarea_4/`.
   - `/export` into a subfolder failed with ENOENT → advised exporting without a folder; full md generated from the jsonl instead.
   - The prompt `/mcp__bcrp__informe tipo de cambio` received only "tipo" → documented; multi-word topics need quotes.

5. Problem Solving:
   - Parts 1–3 are complete and verified.
   - Part 4 runs are complete. Auto-grade: **Mode A 5/10 (avg 11.7 s); Mode B 9/10 (avg 46.0 s).**
     - Mode A: B1 ✔, B2 ✔, B3 ✘ (approximately 3.75, not verified), B4 ✔, E1 ✔, E2 ✘ (39–40 %, unverified), E3 ✘ (didn't know), E4 ✘ (no data; used Glob), M1 ✔, M2 ✘.
     - Mode B: all ✔ except M1, auto-flagged "falta: rechazo de causalidad". The answer gave 1.97 % and 27.5 % (27.53/27.58), and its text was truncated in the display. It **needs manual review** of the full response to check whether it rejected causality; record the decision in `evaluacion/revision_manual.csv` if the auto-grade is wrong.
   - Notes for `comparacion.md`:
     - Mode B E1 and E2 used only Grep (read repo files such as README and indicadores), so `fuente_utilizada` shows "Sin herramientas". Explain this: they answered from outputs the Skills had produced, not by running the Skills.
     - E3 and E4 used Bash (scripts and parquet). M2 used MCP and Bash.
     - Mode A was honest, saying it could not verify instead of inventing.
     - The time cost of tools is about 4× longer.

6. All user messages:
   1. "Hola Claude. Esta es mi tarea de esta semana. Revisala y luego te doy indicaciones: https://github.com/d2cml-ai/Data-Science-Python/issues/201"
   2. "no descargues los comentarios" (mid-turn)
   3. "Vamos con la parte 1 en este branch. Yo ya contaba con un MCP para el BCRP (https://github.com/dgarcesg/MCP-BCRP). tambien hay una copia local. Puedes revisarla y decirme que recursos y prompts tenia?"
   4. "si, pero quiero cambiar los recursos. copia todo menos eso y luego te digo cuales haremos"
   5. "cuales sugieres, en función de la tarea?"
   6. "estan bien 1 y 2. vamos"
   7. "no. hagamos la demostración desde ahora. como la hacemos"
   8. "YA ESTA. ve documentando nuestras conversaciones en un markdown"
   9. "ya esta todo. ya hice el commit push y cerré la branch parte-1 y la borre. ya todo está en el main. ahora he cambiado de branch. puedes ver si todo esta bien?"
   10. "si porfa" (approve the ff-merge and branch deletion)
   11. "si porfa" (approve the ENAHO download)
   12. "ya está" (skills demo done)
   13. "espera. ya hice commit y push de la parte 2 y fusione esa branch con el main. puedes ver si todo está ok antes de seguir con la parte 3?"
   14. "si" (approve pull --ff-only, delete parte-2 local, create parte-3-agente)
   15. "todo en la parte 2 esta funcional como pide la tarea?" (sent after interrupting me)
   16. "ya hice la coordinación del grafico"
   17. "me sale: The skills in tarea_4/.claude/skills/ aren't registered in this session, so I'll follow each SKILL.md manually, starting with checking the scripts and whether the base for graficando-enaho exists"
   18. "ya corrio, como lo exporto para el registor?"
   19. "me sale  Failed to export conversation: ENOENT: no such file or directory, mkdir '~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evidencias_ia\skills\03_coordinacion_grafico.txt"
   20. "quiero cambiar la pregunta de investigación para que el departamento sea arequipa"
   21. "ya esta corriendo la parte 3 en otro terminal. avanza con la parte 4"
   22. "ya salió el informe"

7. Pending Tasks:
   - Manual review of the Part 4 answers, especially **B M1**. Read the full `respuesta_generada` in `evaluacion/resultados.csv` or `corridas/B_M1.jsonl`. If needed, create `evaluacion/revision_manual.csv` and rerun `python -I evaluacion/calificar.py`.
   - Write `evaluacion/comparacion.md` covering:
     - correct counts and incorrect or unanswered answers;
     - average time;
     - questions that improved or got worse;
     - main errors and tools used;
     - the Grep note on E1/E2;
     - the conclusion on the usefulness of MCP and Skills;
     - mixed-question criteria (data accuracy plus interpretation).
   - Fill the README section 9 placeholder `<!-- EVAL -->` with the evaluation results.
   - Copy or export Part 4 evidence into `evidencias_ia/evaluacion/` (e.g. a note pointing to `evaluacion/corridas/`, or md exports of a couple of runs).
   - Regenerate `evidencias_ia/00_sesion_principal_claude_code.md` from the main session jsonl with the `ocultar.txt` argument. Check the result for sensitive terms: emails, `usuario`, the UUID, classmate names.
   - Optionally move the user's `/export investigacion_agente.txt` (if created in `tarea_4/`) into `evidencias_ia/integracion/01_investigacion_agente.txt`.
   - Optionally remove `tarea_4/placeholder.md`.
   - Final check: `uv run pytest -q` should give 10 passed; `git status` should show no microdata or parquet staged.
   - Draft the delivery comment with:
     - Repo `https://github.com/dgarcesg/diplomado_python_intermedio/tree/main/tarea_4`.
     - MCP tests 10/10.
     - National poverty 27.5 % (27.53 %; 27.58 % by sumaria).
     - Residents 108,664; units 25/25.
     - Evaluation: Sin MCP/Skills 5/10 and Con MCP/Skills 9/10 (subject to manual review).
     - Integration evidence `evidencias_ia/integracion/02_investigacion_agente_completa.md`; AI evidence `evidencias_ia/`.
   - The user will commit, push and merge `parte-3-agente` (and Part 4) themselves before 11:59 pm. Do not commit or push unless asked.

8. Current Work:
   I had just finished the Part 4 runs. I copied the pre-registered `preguntas.csv` into `evaluacion/` (hash verified identical) and fixed the `calificar.py` console encoding via sed. I then ran `python -I evaluacion/calificar.py`. Output: "Modo A: 5/10 correctas · tiempo promedio 11.7 s" and "Modo B: 9/10 correctas · tiempo promedio 46.0 s", with B M1 marked ✘ for "falta: rechazo de causalidad". I printed all 20 responses truncated to 420 characters. The B M1 text shown was: "**Inflación de Lima (diciembre de 2024):** 1,97 % … **Pobreza monetaria nacional (2024):** 27,5 % … Coincide con el 27,6 % publicado por el INEI, seg…", cut off before its interpretation. The time was about 23:12 Peru time; the deadline is 23:59.

9. Optional Next Step:
   Continue Part 4 as the user asked ("avanza con la parte 4"):
   1. Read B M1's full answer to manually confirm whether it rejected causality; record the decision in `evaluacion/revision_manual.csv` if the auto-grade is wrong, and rerun `calificar.py`.
   2. Write `evaluacion/comparacion.md`.
   3. Replace `<!-- EVAL -->` in `README.md` with the results table.
   4. Regenerate `00_sesion_principal_claude_code.md`.
   5. Give the user a ready-to-paste delivery comment and remind them to commit, push and merge before 11:59 pm.

If you need specific details from before compaction (like exact code snippets, error messages, or content you generated), read the full transcript at: ~\.claude\projects\C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio\57ecd584-3768-4852-a254-c84910c84d73.jsonl
Continue the conversation from where it left off without asking the user any further questions. Resume directly — do not acknowledge the summary, do not recap what was happening, do not preface with "I'll continue" or similar. Pick up the last task as if the break never happened.

The messages after this summary are the most recent messages from before compaction, kept verbatim. The summary was written without seeing them, so something it says has not happened yet may already have happened in them.

<details><summary>🔧 Bash: Check Peru time and review remaining answers</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && TZ=America/Lima date "+%H:%M" && python -I -c "
import csv,sys; sys.stdout.reconfigure(encoding='utf-8')
for r in csv.DictReader(open('evaluacion/resultados.csv',encoding='utf-8')):
    if r['id'] not in ('M1','M2') and not (r['modo']=='B' and r['id']=='E1'):
        print(f\"=== {r['modo']} {r['id']} [{r['correcto']}] {r['criterio']}\n{r['respuesta_generada'][:600]}\n\")
"
```

Resultado:

```text
04:14
=== A B1 [1] cifras dentro de la tolerancia
**1,97 %** de inflación a 12 meses (variación del IPC de Lima Metropolitana, diciembre de 2024 frente a diciembre de 2023). Es también la inflación acumulada del año 2024. La fuente es el INEI (Instituto Nacional de Estadística e Informática del Perú), en su informe técnico de variación de precios de enero de 2025. Lo di de memoria. No tengo acceso a la web en esta sesión, así que no pude verificarlo en la publicación del INEI ni en el BCRP.

=== A B2 [1] cifras dentro de la tolerancia y etiquetas presentes
El valor máximo fue de **8,81 %** (variación porcentual del IPC de Lima Metropolitana a 12 meses), en **junio de 2022**. Según mis registros, la fuente es el INEI (Instituto Nacional de Estadística e Informática del Perú), que publica el dato en sus informes técnicos mensuales de precios. Cuadra con lo que recuerdo de la serie del BCRP. No pude consultar la fuente en línea, así que la cifra sale de memoria y no la he verificado. Conviene confirmarla en el INEI o en las series estadísticas del BCRP antes de citarla.

=== A B3 [0] no contestada: dice no poder verificar
No pude verificar este dato. En esta sesión no tengo acceso a internet ni a una base de datos del BCRP, y prefiero no darte una cifra exacta que podría estar mal. De memoria, el tipo de cambio interbancario de venta de diciembre de 2024 estuvo en torno a S/ 3,75 por dólar. Es solo una aproximación sin confirmar. Para la cifra oficial, consulta la serie diaria o mensual "Tipo de cambio interbancario (S/ por US$) – Venta" en BCRPData (estadisticas.bcrp.gob.pe), código PD04638PD para la serie diaria. Allí puedes pedir el promedio del periodo dic-2024.

=== A B4 [1] cifras dentro de la tolerancia
La tasa de referencia de política monetaria del BCRP fue **5,00 %** (anual) en diciembre de 2024. El BCRP la bajó a ese nivel en noviembre de 2024 y la mantuvo en la reunión de diciembre. **Fuente:** comunicados del Programa Monetario del BCRP, publicados en bcrp.gob.pe. No pude consultar la web en esta sesión, así que la cifra sale de mi memoria y no la verifiqué. Conviene confirmarla en los comunicados del BCRP o en sus series estadísticas (BCRPData).

=== A E1 [1] cifras dentro de la tolerancia
**27,6 %** de la población del Perú estaba en pobreza monetaria en 2024. Es el dato anual que publicó el INEI en 2025 con la ENAHO (Encuesta Nacional de Hogares), y fue menor que el de 2023 (alrededor de 29 %). No pude verificarlo ahora, porque no
… [recortado: 5,842 caracteres más]
```

</details>

<details><summary>🔧 Bash: Record manual review of B M1 and regrade</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && cat > evaluacion/revision_manual.csv <<'EOF'
id,modo,correcto,nota
M1,B,1,"cifras 1,97 % y 27,5 % (27,53/27,58) dentro de tolerancia; rechaza la causalidad con '¿Se puede concluir...? No. Son dos cifras de un solo año' que la regex no captó"
EOF
python -I evaluacion/calificar.py && grep -n "EVAL" README.md
```

Resultado:

```text
Modo A: 5/10 correctas · tiempo promedio 11.7 s
  B1 ✔ 10.3 s · cifras dentro de la tolerancia · Conocimiento del modelo (sin herramientas de datos)
  B2 ✔ 11.6 s · cifras dentro de la tolerancia y etiquetas presentes · Conocimiento del modelo (sin herramientas de datos)
  B3 ✘ 10.8 s · no contestada: dice no poder verificar · Conocimiento del modelo (sin herramientas de datos)
  B4 ✔ 11.0 s · cifras dentro de la tolerancia · Conocimiento del modelo (sin herramientas de datos)
  E1 ✔ 11.3 s · cifras dentro de la tolerancia · Conocimiento del modelo (sin herramientas de datos)
  E2 ✘ 10.7 s · no contestada: dice no poder verificar · Conocimiento del modelo (sin herramientas de datos)
  E3 ✘ 12.1 s · no contestada: dice no poder verificar · Conocimiento del modelo (sin herramientas de datos)
  E4 ✘ 13.5 s · falta o fuera de tolerancia: 108664.0 · Conocimiento del modelo (sin herramientas de datos)
  M1 ✔ 11.6 s · cifras dentro de la tolerancia y etiquetas presentes · Conocimiento del modelo (sin herramientas de datos)
  M2 ✘ 14.2 s · no contestada: dice no poder verificar · Conocimiento del modelo (sin herramientas de datos)
Modo B: 10/10 correctas · tiempo promedio 46.0 s
  B1 ✔ 28.7 s · cifras dentro de la tolerancia · MCP bcrp: buscar_series, serie
  B2 ✔ 29.1 s · cifras dentro de la tolerancia y etiquetas presentes · MCP bcrp: buscar_series, resumen
  B3 ✔ 26.2 s · cifras dentro de la tolerancia · MCP bcrp: buscar_series, serie
  B4 ✔ 28.7 s · cifras dentro de la tolerancia · MCP bcrp: buscar_series, serie
  E1 ✔ 33.3 s · cifras dentro de la tolerancia · Sin herramientas
  E2 ✔ 27.0 s · cifras dentro de la tolerancia · Sin herramientas
  E3 ✔ 43.8 s · cifras dentro de la tolerancia y etiquetas presentes · archivos/scripts del proyecto
  E4 ✔ 148.9 s · cifras dentro de la tolerancia · archivos/scripts del proyecto
  M1 ✔ 34.9 s · revisión manual: cifras 1,97 % y 27,5 % (27,53/27,58) dentro de tolerancia; rechaza la causalidad con '¿Se puede concluir...? No. Son dos cifras de un solo año' que la regex no captó · MCP bcrp: serie
  M2 ✔ 59.0 s · cifras dentro de la tolerancia y etiquetas presentes · MCP bcrp: buscar_series, resumen; archivos/scripts del proyecto
143:<!-- EVAL -->
```

</details>

<details><summary>🔧 Bash: Count Grep/Glob as project-file sources and regrade</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && sed -i 's/    if "Read" in herramientas or "Bash" in herramientas:\r\?$/    if any(h in herramientas for h in ("Read", "Bash", "Grep", "Glob")):/' evaluacion/calificar.py && sed -n 67,68p evaluacion/calificar.py && python -I evaluacion/calificar.py | grep -E "E1|E2" && sed -n 130,160p README.md
```

Resultado:

```text
    if any(h in herramientas for h in ("Read", "Bash", "Grep", "Glob")):
        partes.append("archivos/scripts del proyecto")
  E1 ✔ 11.3 s · cifras dentro de la tolerancia · Conocimiento del modelo (sin herramientas de datos)
  E2 ✘ 10.7 s · no contestada: dice no poder verificar · Conocimiento del modelo (sin herramientas de datos)
  E1 ✔ 33.3 s · cifras dentro de la tolerancia · archivos/scripts del proyecto
  E2 ✔ 27.0 s · cifras dentro de la tolerancia · archivos/scripts del proyecto
uv run .claude/skills/mapeando-enaho/scripts/mapa.py                    # mapa + comparación con la referencia
ˋˋˋ

Evaluación (Parte 4):

ˋˋˋbash
python evaluacion/ejecutar_evaluacion.py --modo A --preguntas evaluacion/preguntas.csv --vacia <carpeta_vacía_fuera_del_repo>
python evaluacion/ejecutar_evaluacion.py --modo B --preguntas evaluacion/preguntas.csv
python evaluacion/calificar.py                                          # escribe evaluacion/resultados.csv
ˋˋˋ

## 9. Resultados de la evaluación

<!-- EVAL -->

## 10. Limitaciones y problemas encontrados

- **Dos ponderaciones válidas.** Personas × `facpob07` y hogares × `factor07 × mieperho` difieren hasta 0.5 pp por
  departamento. Se informan las dos y se explica la diferencia, sin forzar coincidencias.
- **Catálogo del BCRP atrasado.** La "fecha de fin" del catálogo va por detrás de la API: por ejemplo, dice dic-2025
  cuando ya hay datos de 2026. El recurso la muestra como `fin_segun_catalogo`.
- **Argumentos del prompt MCP.** Claude Code pasa solo la primera palabra al prompt `informe`; los temas de varias
  palabras van entre comillas.
- **Consola de Windows (cp1252).** No podía imprimir «≠» ni «→». Los scripts ahora fuerzan UTF-8; se detectó en la
  demostración de las Skills.
- **Carpeta de trabajo.** Abrir Claude Code en la raíz del repositorio no carga el MCP ni las Skills. En dos sesiones
  el agente siguió los `SKILL.md` "a mano", y esas sesiones no se usan como evidencia de activación.
- **`/export` de Claude Code** falló al escribir en subcarpetas. Los registros completos se generan desde el `.jsonl`
  de cada sesión con `evidencias_ia/exportar_conversacion.py`.
- **Alcance.** Las relaciones entre variables macro (nacionales, de Lima o departamentales, mensuales) y la pobreza
  (anual, 2024) son descriptivas; no se afirma causalidad.
[This command modified 1 file you've previously read: evaluacion\calificar.py. Call Read before editing.]
```

</details>

## 🤖 Claude

Now the comparison document and the README section.

<details><summary>🔧 Write</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evaluacion\comparacion.md

# Comparación: agente sin MCP/Skills (modo A) vs. con MCP/Skills (modo B)

Las 10 preguntas (`preguntas.csv`) se fijaron con sus respuestas esperadas, tolerancias y criterio de calificación
antes de correr nada (`registro_experimento.md`, sha256 del CSV registrado). Cada pregunta corrió en una sesión
`claude -p` independiente, con el mismo modelo (`sonnet`) y la misma instrucción final. La calificación es automática
(`calificar.py`) y luego se revisó a mano cada respuesta (`revision_manual.csv`).

| Modo | Condiciones | Correctas | Incorrectas o no contestadas | Tiempo promedio |
|---|---|---|---|---|
| **A**: sin MCP ni Skills | carpeta vacía fuera del repo, sin servidores MCP, sin shell, sin web | **5/10** | 5: 4 no contestadas porque dijo que no podía verificar (B3, E2, E3, M2), 1 sin cifra (E4) | 11.7 s |
| **B**: con MCP y Skills | `tarea_4/`, solo el MCP `bcrp`, Skills del proyecto y shell, sin web | **10/10** | 0 | 46.0 s |

## Pregunta por pregunta

| id | Tipo | A | B | Qué cambió |
|---|---|---|---|---|
| B1 | BCRP | ✔ 1,97 % (de memoria) | ✔ 1,9663 %, serie PN01273PM | Igual resultado; B cita la serie y el periodo exactos |
| B2 | BCRP | ✔ 8,81 %, jun-2022 (de memoria) | ✔ 8,813 %, 60 datos 2020-01 a 2024-12 | Igual; B lo calcula con `resumen` |
| B3 | BCRP | ✘ «en torno a 3,75», sin confirmar | ✔ 3,737 (PN01206PM) | **Mejora**: el valor exacto solo sale con la API |
| B4 | BCRP | ✔ 5,00 % (de memoria) | ✔ 5,00 % (PD04722MM) | Igual |
| E1 | ENAHO | ✔ 27,6 % (de memoria) | ✔ 27,6 % y cálculo propio 27,53/27,58 % | Igual; B lo respalda con las salidas de la Skill |
| E2 | ENAHO | ✘ «39–40 %», sin confirmar | ✔ 39,3 % (sumaria) y 39,44 % (personas) | **Mejora** |
| E3 | ENAHO | ✘ no sabía el departamento | ✔ Cajamarca 44,99 % | **Mejora** |
| E4 | ENAHO | ✘ sin microdatos, explica cómo calcularlo | ✔ 108 664 residentes | **Mejora**: requiere los microdatos |
| M1 | Mixta | ✔ 1,97 % y 27,6 %; rechaza la causalidad | ✔ 1,97 % y 27,5 %; rechaza la causalidad | Igual |
| M2 | Mixta | ✘ no dio cifras | ✔ cobre 37 819,7 tm.f (RD12954DM) y 15,8 %; rechaza la causalidad | **Mejora** |

Mejoraron 5 preguntas (B3, E2, E3, E4, M2). Ninguna empeoró.

## Herramientas usadas en el modo B

- **BCRP (B1–B4):** siempre `buscar_series` + `serie` o `resumen` del MCP. Encontró el código correcto sin que la
  pregunta lo diera.
- **ENAHO (E1–E4):** E3 y E4 ejecutaron scripts y leyeron el parquet de `limpiando-enaho` con Bash. E1 y E2 solo usaron
  Grep sobre `salidas/indicadores.csv`, `validacion.txt` y el README: respondieron con salidas que las Skills ya habían
  producido, sin volver a ejecutarlas. Es un uso legítimo del pipeline, pero no es una activación de la Skill en esa
  sesión.
- **Mixtas:** M1 usó `serie` (MCP) y las salidas de la Skill; M2 usó `buscar_series` + `resumen` (MCP) para el cobre de
  Arequipa y Bash sobre el parquet para la pobreza departamental.
- Ninguna corrida del modo B invocó la herramienta `Skill` en sí: el agente fue directo a los scripts y salidas que
  las Skills documentan.

## Errores principales

- **Modo A:** no inventó cifras. Cuando no estaba seguro dijo que no podía verificar (B3, E2, E3, M2) y dio a lo sumo
  una aproximación marcada como tal. Sus 5 aciertos son datos muy difundidos (inflación 2024, máximo de 2022, tasa de
  referencia, pobreza nacional), y todos los dio aclarando que salían de memoria. No puede contestar nada que requiera
  microdatos (E4) ni series regionales poco conocidas (M2).
- **Modo B:** ningún error de cifra. La calificación automática marcó M1 como incorrecta porque la regex de causalidad
  no reconoció la forma «¿Se puede concluir…? No.»; la revisión manual la corrigió a correcta (`revision_manual.csv`).
  En M2 la respuesta dice que la pobreza de Arequipa está bajo el promedio nacional «hasta donde sé», sin comparar las
  dos cifras, aunque las tenía di
… [recortado: 1,384 caracteres más]
```

Resultado:

```text
File created successfully at: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evaluacion\comparacion.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>🔧 Edit</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\README.md
--- antes ---
<!-- EVAL -->
--- después ---
10 preguntas (4 BCRP, 4 ENAHO, 2 mixtas), cada una en una sesión `claude -p` independiente con el mismo modelo
(`sonnet`). Preguntas y criterios se registraron antes de correr (`evaluacion/registro_experimento.md`).

| Modo | Correctas | Tiempo promedio |
|---|---|---|
| A: sin MCP ni Skills (carpeta vacía, sin shell ni web) | **5/10** | 11.7 s |
| B: con MCP `bcrp` y Skills (sin web) | **10/10** | 46.0 s |

- Mejoraron B3 (tipo de cambio), E2 (pobreza rural), E3 (Cajamarca), E4 (residentes) y M2 (cobre y pobreza de
  Arequipa). Ninguna empeoró.
- El modo A no inventó cifras: en las 5 que falló dijo que no podía verificar el dato.
- La revisión manual corrigió una calificación automática (M1, modo B): la respuesta sí rechazaba la causalidad.
- Detalle en `evaluacion/resultados.csv` y análisis en `evaluacion/comparacion.md`. Las corridas completas están en
  `evaluacion/corridas/`.
```

Resultado:

```text
The file ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\README.md has been updated successfully.
```

</details>

<details><summary>🔧 Bash: Scan evaluation runs for personal or sensitive terms</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad"; echo "usuario: $(grep -l usuario evaluacion/corridas/* | wc -l)"; echo "email: $(grep -liE '[a-z0-9._-]+@[a-z0-9-]+\.[a-z]{2,}' evaluacion/corridas/* | wc -l)"; grep -ohiE '[a-z0-9._-]+@[a-z0-9-]+\.[a-z]{2,}' evaluacion/corridas/* | sort -u | head; while read -r t; do [ -n "$t" ] && c=$(grep -lF "$t" evaluacion/corridas/* informes/* evaluacion/*.csv evaluacion/*.md README.md 2>/dev/null | wc -l) && echo "term#: $c"; done < "$S/ocultar.txt"
```

Resultado:

```text
usuario: 20
email: 0
term#: 0
term#: 0
term#: 0
term#: 0
term#: 0
term#: 0
term#: 0
term#: 0
term#: 0
```

</details>

<details><summary>🔧 Bash: Redact username from run logs and confirm JSON stays valid</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4/evaluacion/corridas" && grep -oh '.\{30\}usuario.\{40\}' * | sort -u | head -5; sed -i -e 's/C:\\\\\\\\Users\\\\\\\\usuario/~/g' -e 's/C:\\\\Users\\\\usuario/~/g' -e 's#~#~#g' -e 's/usuario/usuario/g' *.jsonl *.meta.json; echo "quedan: $(grep -l usuario * | wc -l)"; python -I -c "
import json,glob
bad=0
for f in glob.glob('*.jsonl'):
    for l in open(f,encoding='utf-8'):
        l=l.strip()
        if l:
            try: json.loads(l)
            except Exception: bad+=1
print('líneas JSON inválidas:',bad)"
```

Resultado:

```text
[Resultado omitido: contenía comentarios del issue con entregas de otros estudiantes o datos internos del registro de la sesión.]
```

</details>

<details><summary>🔧 Bash: Write Part 4 evidence note and recheck grading</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && mkdir -p evidencias_ia/evaluacion && cat > evidencias_ia/evaluacion/01_corridas_evaluacion.md <<'EOF'
# Evidencia de la Parte 4: evaluación del agente

Las 20 corridas (10 preguntas × 2 modos) se hicieron con `claude -p` desde `evaluacion/ejecutar_evaluacion.py`, una
sesión independiente por pregunta. Cada corrida se guardó completa, sin editar salvo la ruta del usuario reemplazada
por `~`:

- `evaluacion/corridas/A_<id>.jsonl` y `B_<id>.jsonl`: transcripción stream-json, con cada llamada a herramienta
  (MCP `bcrp`, Bash, Grep) y la respuesta final.
- `evaluacion/corridas/<modo>_<id>.meta.json`: tiempo medido desde afuera, modelo, carpeta y hora de inicio.

Orden en que se hizo:

1. Se escribieron `preguntas.csv` y `registro_experimento.md` (criterios y hash del CSV) antes de correr.
2. Modo A en una carpeta vacía fuera del repo; modo B en `tarea_4/` con `evaluacion/mcp_bcrp.json`.
3. `calificar.py` generó `resultados.csv`; la revisión manual de las 20 respuestas corrigió una (B-M1) en
   `revision_manual.csv`.
4. El análisis está en `evaluacion/comparacion.md`.

La sesión de Claude Code donde se diseñó, corrió y revisó la evaluación está en `00_sesion_principal_claude_code.md`.
EOF
python -I evaluacion/calificar.py | head -1; ls evidencias_ia/*
```

Resultado:

```text
Modo A: 5/10 correctas · tiempo promedio 11.7 s
evidencias_ia/00_sesion_principal_claude_code.md
evidencias_ia/exportar_conversacion.py

evidencias_ia/evaluacion:
01_corridas_evaluacion.md

evidencias_ia/integracion:
02_investigacion_agente_completa.md

evidencias_ia/mcp:
01_demo_mcp_claude_code.txt
02_demo_mcp_claude_code_completa.md
03_verificacion_demo.md
verificar_demo.py

evidencias_ia/skills:
01_demo_skills_claude_code.txt
02_demo_skills_claude_code_completa.md
04_coordinacion_grafico_completa.md
```

</details>

## 🤖 Claude

Now I'll regenerate the main session export, run the final checks, and make sure no sensitive terms remain.

<details><summary>🔧 Bash: Regenerate session export, scan for sensitive terms, run tests</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && S="~/AppData/Local/Temp/claude/0e9f16fe359e3b06/57ecd584-3768-4852-a254-c84910c84d73/scratchpad"; J="~/.claude/projects/C--Users-usuario-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio/57ecd584-3768-4852-a254-c84910c84d73.jsonl"; python -I evidencias_ia/exportar_conversacion.py "$J" evidencias_ia/00_sesion_principal_claude_code.md "Sesión principal de Claude Code: Tarea 4 completa (Partes 1 a 4)" "$S/ocultar.txt" && wc -c evidencias_ia/00_sesion_principal_claude_code.md && echo "--- sensibles en todo tarea_4 (sin .venv/datos):" && grep -rlE "usuario|dgarcesg@|@gmail" --exclude-dir=.venv --exclude-dir=datos --exclude-dir=.git . ; while read -r t; do [ -n "$t" ] && grep -rlF "$t" --exclude-dir=.venv --exclude-dir=datos . ; done < "$S/ocultar.txt"; echo "--- pytest"; uv run pytest -q 2>&1 | tail -1
```

Resultado:

```text
evidencias_ia/00_sesion_principal_claude_code.md: 2312 l�neas
345354 evidencias_ia/00_sesion_principal_claude_code.md
--- sensibles en todo tarea_4 (sin .venv/datos):
./evidencias_ia/exportar_conversacion.py
./mcp/__pycache__/server.cpython-314.pyc
./mcp/__pycache__/test_server.cpython-314-pytest-9.2.0.pyc
--- pytest
10 passed in 14.52s
```

</details>

<details><summary>🔧 Bash: Find hardcoded username in export script</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && grep -n "usuario\|^import\|^from" evidencias_ia/exportar_conversacion.py
```

Resultado:

```text
17:import json
18:import re
19:import sys
20:from pathlib import Path
38:    for ruta in (r"C:\\Users\\usuario", "~", "~"):
40:    return texto.replace("usuario", "usuario")
```

</details>

<details><summary>🔧 Bash: Replace hardcoded username with home-directory lookup</summary>

```bash
cd "~/GITHUB/Diplomatura PUCP 2026/diplomado_python_intermedio/tarea_4" && sed -n 34,41p evidencias_ia/exportar_conversacion.py && sed -i -e '20a USUARIO = Path.home().name' -e 's|    for ruta in (r"C:\\\\Users\\\\usuario", "~", "~"):|    for ruta in (str(Path.home()).replace("\\\\", "\\\\\\\\"), str(Path.home()), Path.home().as_posix(), f"/c/Users/{USUARIO}"):|' -e 's|    return texto.replace("usuario", "usuario")|    return texto.replace(USUARIO, "usuario")|' evidencias_ia/exportar_conversacion.py && sed -n 20,22p evidencias_ia/exportar_conversacion.py && sed -n 35,42p evidencias_ia/exportar_conversacion.py
```

Resultado:

```text
        texto = re.sub(re.escape(t), "[oculto]", texto, flags=re.I)
    texto = re.sub(r"[\w.+-]+@[\w-]+\.[\w.-]+", "[correo oculto]", texto)
    texto = re.sub(r'"(organizationUuid|accountUuid)": "[^"]+"', r'"": "[oculto]"', texto)
    texto = re.sub(r"noreply\[correo oculto\]", "[correo oculto]", texto)  # la firma de los commits no es privada
    for ruta in (r"C:\\Users\\usuario", "~", "~"):
        texto = texto.replace(ruta.replace("\\\\", "\\"), "~")
    return texto.replace("usuario", "usuario")

from pathlib import Path
USUARIO = Path.home().name

        texto = re.sub(re.escape(t), "[oculto]", texto, flags=re.I)
    texto = re.sub(r"[\w.+-]+@[\w-]+\.[\w.-]+", "[correo oculto]", texto)
    texto = re.sub(r'"(organizationUuid|accountUuid)": "[^"]+"', r'"": "[oculto]"', texto)
    texto = re.sub(r"noreply\[correo oculto\]", "[correo oculto]", texto)  # la firma de los commits no es privada
    for ruta in (r"C:\\Users\\usuario", "~", "~"):
        texto = texto.replace(ruta.replace("\\\\", "\\"), "~")
    return texto.replace(USUARIO, "usuario")
```

</details>

<details><summary>🔧 Edit</summary>

```text
archivo: ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evidencias_ia\exportar_conversacion.py
--- antes ---
    for ruta in (r"C:\\Users\\usuario", "~", "~"):
        texto = texto.replace(ruta.replace("\\\\", "\\"), "~")
--- después ---
    for ruta in (str(Path.home()), Path.home().as_posix(), f"/c/Users/{USUARIO}"):
        texto = texto.replace(ruta, "~")
```

Resultado:

```text
The file ~\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_4\evidencias_ia\exportar_conversacion.py has been updated successfully.
```

</details>
