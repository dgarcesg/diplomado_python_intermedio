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
