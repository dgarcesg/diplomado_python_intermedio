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

```text
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
```

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

Pruebas: `mcp/test_server.py` tiene las **8 pruebas originales** de la Sesión 04, sin cambios, y **2 propias** para
`comparar_paises`.

## 4. Skills de la ENAHO (`.claude/skills/`)

| Skill | Entra | Sale | Reglas clave |
|---|---|---|---|
| `limpiando-enaho` | `datos/966-Modulo34.zip` y `966-Modulo02.zip` | `salidas/personas_2024.parquet`, `validacion.txt` e `indicadores.csv` | Llaves como texto; residentes `((p204==1)&(p205==2))\|((p204==2)&(p206==1))`; `merge(validate="m:1")`; pondera con `facpob07`; **15 verificaciones**; si falla una esencial, se detiene y no guarda la base |
| `graficando-enaho` | La base y un pedido en lenguaje natural | `figuras/<indicador>_por_<grupo>_2024.png` | Ponderado; por área, sexo, edad o departamento; título analítico calculado; unidad, período y fuente; barras desde 0 |
| `mapeando-enaho` | La base y el GeoJSON del curso | `mapas/pobreza_departamento_2024.png` y `salidas/comparacion_mapa_referencia.csv` | Une `ubigeo[:2]` = `FIRST_IDDP` como texto, nunca por nombre; exige 25 unidades; Lima y Callao separados; escala de un tono desde 0; compara con la referencia de la Sesión 16 |

Las Skills de gráficos y de mapa activan `limpiando-enaho` cuando no existe la base. Esto está demostrado en
`evidencias_ia/skills/`.

### Validación de la ENAHO 2024 (`salidas/validacion.txt`)

| Cifra | Referencia | Obtenido |
|---|---:|---:|
| Pobreza monetaria nacional | 27.6 % | **27.53 %** (personas × `facpob07`) · 27.58 % (sumaria × `factor07 × mieperho`) |
| Residentes habituales | 108,664 | **108,664** |
| Unidades territoriales | 25 | **25** |
| Pobreza urbana / rural | 24.8 % / 39.3 % | 24.74 / 39.44 (personas) · **24.81 / 39.30** (sumaria) |

Las referencias urbano/rural y por departamento de la Sesión 16 se calcularon por hogares (`factor07 × mieperho`). Con
ese método coinciden los **25 departamentos**. Con personas × `facpob07`, que es la ponderación de gráficos y mapa, hay
diferencias de hasta 0.5 pp por la unidad de ponderación, no por errores. La limpieza informa los dos métodos.

## 5. Fuentes de datos

| Fuente | Enlace | Uso |
|---|---|---|
| ENAHO 2024, módulo 34 (sumaria) | https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip | Pobreza y hogares |
| ENAHO 2024, módulo 02 (miembros) | https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo02.zip | Personas |
| Límites departamentales | https://raw.githubusercontent.com/d2cml-ai/Data-Science-Python/main/sessions/06-geoespacial/lab/Data/peru_departamental_simple.geojson | Mapa (se baja solo a `datos/`) |
| Series del BCRP | https://estadisticas.bcrp.gob.pe/estadisticas/series/ | MCP (API y catálogo, se baja solo a `mcp/datos/`) |
| Banco Mundial | https://api.worldbank.org/v2/ | `comparar_paises` |

Los microdatos y el catálogo **no se suben a git**: están en `.gitignore`, junto con la base derivada `salidas/*.parquet`.

## 6. Instalación (con `uv`)

```bash
git clone https://github.com/dgarcesg/diplomado_python_intermedio.git
cd diplomado_python_intermedio/tarea_4
uv sync                      # Python ≥ 3.11: fastmcp, pandas, pyarrow, geopandas, matplotlib, httpx, pytest
mkdir -p datos
curl -L -o datos/966-Modulo34.zip https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip
curl -L -o datos/966-Modulo02.zip https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo02.zip
```

## 7. Conectar el MCP a Claude Code

El servidor ya está en `.mcp.json`. **Hay que abrir Claude Code dentro de `tarea_4/`**, porque ahí están el
`.mcp.json` y `.claude/skills/`. Si se abre en la raíz del repositorio, no se cargan ni el MCP ni las Skills.

```bash
cd tarea_4
claude                       # aprobar el servidor "bcrp" cuando lo pida
/mcp                         # bcrp: connected, 5 herramientas, 2 recursos, 1 prompt
/skills                      # limpiando-enaho, graficando-enaho, mapeando-enaho
```

Para agregarlo a mano: `claude mcp add --scope project bcrp -- uv run mcp/server.py`.
Uso: `@bcrp:bcrp://departamento/04` adjunta un recurso, y `/mcp__bcrp__informe "tipo de cambio"` usa el prompt; los
temas de varias palabras van entre comillas.

## 8. Reproducir el procesamiento y las pruebas

```bash
uv run pytest -q                                                        # 10 passed
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024    # 15 de 15 verificaciones
uv run .claude/skills/graficando-enaho/scripts/graficar.py --por todos  # 4 figuras
uv run .claude/skills/mapeando-enaho/scripts/mapa.py                    # mapa + comparación con la referencia
```

Evaluación (Parte 4):

```bash
python evaluacion/ejecutar_evaluacion.py --modo A --preguntas evaluacion/preguntas.csv --vacia <carpeta_vacía_fuera_del_repo>
python evaluacion/ejecutar_evaluacion.py --modo B --preguntas evaluacion/preguntas.csv
python evaluacion/calificar.py                                          # escribe evaluacion/resultados.csv
```

## 9. Resultados de la evaluación

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

## 11. Ejemplo de una ejecución completa

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

## 12. Evidencias del uso de IA (`evidencias_ia/`)

| Carpeta | Contenido |
|---|---|
| `00_sesion_principal_claude_code.md` | La sesión principal de desarrollo: revisión de la tarea, MCP, Skills, integración y evaluación |
| `mcp/` | Demostración del MCP desde Claude Code (`/export` y registro completo) y verificación independiente de sus cifras |
| `skills/` | Demostración de las Skills: activación con lenguaje natural, invocación con `/`, coordinación mapa → limpieza y gráfico → limpieza |
| `integracion/` | La ejecución de la Parte 3: MCP y Skills en una misma sesión |
| `evaluacion/` | Registro de las corridas de los dos modos |
| `exportar_conversacion.py` | Convierte los `.jsonl` de Claude Code en markdown. Oculta correos, rutas personales e identificadores, y omite entregas de otros estudiantes |

Todo el desarrollo se hizo con Claude Code (Claude Opus 5.5).
