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
