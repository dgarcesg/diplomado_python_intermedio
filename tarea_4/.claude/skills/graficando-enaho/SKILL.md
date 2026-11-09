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

   ```bash
   uv run ${CLAUDE_SKILL_DIR}/scripts/graficar.py --por <grupo> --indicador <indicador>
   ```

   El script pondera con `facpob07` y guarda `figuras/<indicador>_por_<grupo>_2024.png` a 200 dpi. Cumple las reglas:
   un solo color, barras desde cero y ordenadas (la edad conserva su orden), el valor en cada barra, una línea con el
   promedio nacional, un título que dice qué muestra con las cifras, el período, la unidad (% de personas) y la fuente.

4. Responde con la ruta de la figura y las cifras que imprime el script. No calcules nada a mano y no describas
   diferencias como causas.

5. Si piden otro tipo de gráfico o un grupo que el script no tiene, dilo y propón el más cercano. No improvises un
   gráfico sin ponderar.
