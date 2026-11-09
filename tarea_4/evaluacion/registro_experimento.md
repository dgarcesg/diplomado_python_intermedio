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
