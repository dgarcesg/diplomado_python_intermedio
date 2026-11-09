---
name: mapeando-enaho
description: Hace el mapa coroplético de la pobreza monetaria por departamento del Perú con la ENAHO 2024 (INEI), uniendo indicadores y geometrías por código territorial (ubigeo y FIRST_IDDP), con los 25 departamentos y Lima y Callao por separado. Úsala cuando pidan un mapa, una distribución territorial o regional de la pobreza.
---

# Mapear la ENAHO

Todo se corre desde la raíz del proyecto (`tarea_4/`).

1. Si no existe `salidas/personas_2024.parquet`, usa primero la skill `limpiando-enaho` y verifica que su validación
   haya pasado.

2. Corre exactamente:

   ```bash
   uv run ${CLAUDE_SKILL_DIR}/scripts/mapa.py
   ```

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
