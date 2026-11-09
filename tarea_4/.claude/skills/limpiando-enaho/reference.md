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
