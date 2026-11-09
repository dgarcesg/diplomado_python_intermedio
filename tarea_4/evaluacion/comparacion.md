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
  dos cifras, aunque las tenía disponibles.

## Criterio en las preguntas mixtas

Una respuesta mixta cuenta como correcta solo si cumple las dos condiciones:

1. **Exactitud de los datos:** cada cifra dentro de su tolerancia.
2. **Interpretación:** rechaza una conclusión causal a partir de dos cifras de un año.

Los dos modos interpretaron bien: ninguno afirmó causalidad. La diferencia está en los datos: A no pudo dar las cifras
de M2.

## Conclusión

Con MCP y Skills el agente pasó de 5/10 a 10/10. La mejora se concentra en lo que no está en la memoria del modelo:
valores exactos de series menos citadas (tipo de cambio, cobre regional), desagregaciones de la ENAHO y conteos de los
microdatos. El costo es tiempo: el modo B tardó en promedio unas 4 veces más (46,0 s frente a 11,7 s), y E4 llegó a
149 s porque leyó los microdatos.

El modo A se comportó de forma honesta: prefirió decir «no puedo verificar» a inventar. Sus aciertos no tienen fuente
comprobable, mientras que cada respuesta del modo B cita la serie del BCRP o el archivo del que salió. Para un informe
reproducible eso importa tanto como acertar.

**Límites:** son 10 preguntas y una corrida por modo, sin repeticiones, así que la diferencia es indicativa y no una
estimación con margen de error. Además, varias respuestas de A coinciden con el dato real por ser cifras muy
difundidas, y algunas de B se apoyaron en salidas ya calculadas.
