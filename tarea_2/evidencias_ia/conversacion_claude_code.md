# Evidencia de uso de IA · Tarea 2

Conversación completa con **Claude Code** (modelo Claude Opus 5.5, Anthropic) usada para la Tarea 2 «Voces y documentos peruanos: del archivo escaneado al texto buscable» ([issue 190](https://github.com/d2cml-ai/Data-Science-Python/issues/190)).

- Se incluyen, en orden y sin editar, todos los mensajes del estudiante y todas las respuestas del asistente.
- Las herramientas que usó el asistente (comandos, lectura y edición de archivos) aparecen como una lista breve en cada turno, sin su salida completa.
- Las horas están en hora de Perú (UTC−5). Los nombres de personas entrevistadas en los audios se reemplazaron por los mismos seudónimos `[PERSONA_n]` del corpus.

---

## 1. Estudiante · 25/10/2026 19:42

> Claude, tengo esta tarea. Primero revisala y entiendela y luego te doy instrucciones: https://github.com/d2cml-ai/Data-Science-Python/issues/190

### Claude Code · 25/10/2026 19:43

<details><summary>Herramientas usadas (9)</summary>

- `Bash` View GitHub issue 190 with comments
- `Bash` Show recent commits and repo layout
- `ToolSearch` select:WebFetch
- `Bash` Fetch issue 190 and its comments from GitHub API
- `Bash` Print issue body and comments as UTF-8
- `Bash` Print issue body and comments as UTF-8
- `Bash` Check date and inspect the untracked tarea_2 notebook
- `Read` C:\Users\agarces\.claude\projects\C--Users-agarces-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio\memory\ds-python-up-kernel.md
- `Bash` Check course repo for session materials and env packages

</details>

`gh` no está instalado, así que traigo el issue por la web.

Ya revisé el issue y el estado actual del repo. Te resumo lo que pide y lo que encontré.

## Tarea 2: documentos escaneados y audio → texto estructurado y buscable

Es individual y se entrega en `tarea_2/`. Hay que armar un pipeline con OCR (PaddleOCR) y ASR (faster-whisper con VAD y diarización), seudonimizar los textos, evaluar con CER/WER y publicar un dashboard en Streamlit Cloud.

**Corpus obligatorios:**
- **Documentos:** 25 en total, de tres tipos: 8 impresos nítidos, 8 fotos con sombra o inclinación y 9 manuscritos. Todos con licencia que permita usarlos.
- **Audio:** al menos 30 minutos en 20 clips o más, en español peruano, y al menos un clip con 2 o más hablantes.

**Entregables y puntaje (20 pts):**

| Parte | Archivos | Pts |
|---|---|---|
| Flujo en GitHub | 3 issues como bitácora (cerrados), commits repartidos en el tiempo | 2 |
| 1 – Extracción | `01_extraccion.ipynb` (OCR, ASR, seudonimización, limpieza por hash, 3 gráficos Plotly con títulos analíticos), `documentos.csv`, `transcripciones.csv`, `fuentes.csv` | 6 |
| 2 – Evaluación | `02_evaluacion.ipynb`: 10 documentos y 10 clips con **transcripción manual**, línea base, un OCR y un ASR alternativos sobre las mismas muestras, extracción con LLM en `extraccion_llm.csv` y auditoría humana de 20 casos | 8 |
| 3 – Dashboard | `app.py`, `requirements.txt`, `README.md`, **desplegado en Streamlit Cloud** | 4 |

Además hay que guardar capturas de toda la conversación con la IA en `evidencias_ia/`. La entrega final es un comentario en el issue 190 con el formato que indican.

## Lo que encontré

- ⚠️ **El plazo vence hoy, domingo 25 a las 23:59 (hora de Perú).** En tu máquina son las 19:44, así que quedan unas **4 horas**.
- `tarea_2/01_extraccion.ipynb` está vacío (una sola celda sin contenido) y todavía no hay corpus descargado. Estás en la rama `P1-Corpus-y-extraccion`.
- El entorno `ds-python-up` ya tiene PaddleOCR 3.7, faster-whisper, jiwer, plotly y streamlit. El repo del curso tiene `voz.py` y `datos.py` de la Sesión 13, que se pueden reutilizar.
- `gh` no está instalado, así que no puedo crear ni cerrar issues desde aquí.

## Lo que tendrías que hacer tú

- La **transcripción manual** de los 10 documentos y los 10 clips. El enunciado prohíbe usar referencias automáticas como si fueran manuales.
- La **revisión humana** de la seudonimización y la auditoría de las 20 extracciones del LLM.
- Las capturas para `evidencias_ia/`.
- El despliegue en Streamlit Cloud, que necesita tu cuenta, y el comentario de entrega en el issue.

Con el tiempo que queda, lo realista es priorizar: primero la Parte 1 completa y la estructura de la Parte 2, y dejar listo el `app.py` para que lo despliegues. Dime cómo quieres avanzar.

---

## 2. Estudiante · 25/10/2026 19:56

> Entonces mi entorno ya está listo? tengo que descargar algo?

### Claude Code · 25/10/2026 19:56

<details><summary>Herramientas usadas (5)</summary>

- `Bash` Check imports, binaries, model caches and kernel
- `Bash` Check binaries, model caches, kernel and voz.py requirements
- `Bash` List Ollama models, model aliases in voz.py, free disk
- `Bash` Show ASR model registry in voz.py and check GPU
- `Read` C:\Users\agarces\AppData\Local\Temp\claude\C--Users-agarces-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio\babda432-59ec-4764-9da9-14b0848c6b99\tasks\b4wa86kzn.output

</details>

Lo verifico rápido: qué importa bien en el entorno y qué modelos ya están descargados.

Los imports de torch y paddle tardan. Mientras termina, reviso los binarios, las cachés y los requisitos de `voz.py`.

Casi listo. Las librerías principales ya están instaladas en `ds-python-up`, y el kernel está registrado. Lo que falta son sobre todo **modelos**, que se descargan solos la primera vez que se usan, y un par de herramientas para la Parte 2.

## Lo que ya está instalado
- **OCR:** PaddleOCR 3.7 con Paddle 3.3.
- **Audio (ASR):** faster-whisper 1.2.1, y en caché el modelo turbo que usa `voz.py`.
- **Diarización:** pyannote 4.0.
- **Utilidades:** jiwer (WER/CER), librosa, soundfile y ffmpeg.
- **Gráficos y app:** Plotly 7 y Streamlit 1.62.
- **LLM:** Ollama, con `qwen2.5:3b` y `qwen3:8b` ya descargados.

## Lo que se descarga solo al ejecutarse
| Qué | Tamaño aprox. | Cuándo |
|---|---|---|
| Modelos de PaddleOCR | ~200 MB a 2 GB (según el pipeline) | Primera llamada al OCR |
| faster-whisper `small` (la línea base que pide el enunciado) | ~500 MB | Parte 2 |
| Modelo de diarización (`pyannote/wespeaker...`) | ~30 MB | Primer clip con varios hablantes |
| ASR alternativo (Qwen3-ASR 0.6B o Parakeet) | ~1.2 GB | Parte 2 |

Espacio no falta: tienes 705 GB libres.

## Lo que falta instalar
1. **Un OCR alternativo para la Parte 2.** Tesseract no está instalado y necesita un instalador de Windows (`winget install UB-Mannheim.TesseractOCR` más el paquete de idioma español). Si prefieres no instalar nada en el sistema, **EasyOCR** se instala solo con pip y el enunciado lo acepta ("otro modelo... debidamente justificado").
2. **`kaleido`, para que los gráficos se vean en GitHub.** GitHub no muestra los gráficos interactivos de Plotly en un notebook, y el enunciado exige que sean visibles ahí. Con kaleido se guarda también una imagen estática de cada gráfico.

## Dos cosas a tener en cuenta
- **No tienes GPU NVIDIA**, así que todo corre en CPU. Transcribir 30 minutos con el modelo turbo puede tomar unos 20 a 30 minutos. Con `small` es más rápido. `qwen3:8b` en CPU será lento para 45 extracciones, así que `qwen2.5:3b` es la opción práctica.
- **Falta el corpus:** los 25 documentos y los 30 minutos de audio todavía no están descargados, y eso es lo que más tiempo va a tomar.

¿Quieres que instale `kaleido` y `easyocr` en el entorno? Prefiero preguntarte antes, porque el entorno vive en el repo del curso.

---

## 3. Estudiante · 25/10/2026 20:01

> instala easy ocr

### Claude Code · 25/10/2026 20:01

<details><summary>Herramientas usadas (4)</summary>

- `Bash` Check uv, OpenCV constraint note and key installed versions
- `Bash` Freeze env as constraints and dry-run EasyOCR install
- `Bash` Install EasyOCR and diff environment before/after
- `Bash` Smoke-test EasyOCR in Spanish and verify PaddleOCR import

</details>

La simulación muestra que solo se agregan 2 paquetes (`easyocr` y `ninja`) y no cambia nada de lo que ya está instalado. Lo instalo:

Quedó instalado. Ahora pruebo que EasyOCR funcione y que PaddleOCR siga importando bien. De paso se descargan los modelos de EasyOCR para español (~95 MB).

EasyOCR 1.7.2 quedó instalado en `ds-python-up` y funciona.

- **Prueba:** leí una imagen de prueba con el texto "Solicitud de licencia 2026" y lo reconoció bien (`['Solicitud', 'de licencia 2026']`).
- **Modelos:** ya están descargados en `~/.EasyOCR/model/` (detección y reconocimiento latino, ~95 MB). No necesita internet al usarlo en el notebook.
- **Resto del entorno:** solo se agregaron `easyocr` y `ninja`. OpenCV sigue en la versión 4.10.0.84 que exige PaddleX, y PaddleOCR importa sin problemas.

Un aviso: si algún día corres `uv sync` en el repo `Data-Science-Python`, va a desinstalar EasyOCR, porque no está en su `pyproject.toml`. Si eso pasa, se reinstala con el mismo comando.

Ya son las 20:02, así que quedan unas 4 horas para la entrega. ¿Seguimos con el corpus?

---

## 4. Estudiante · 25/10/2026 20:05

> por favor, primero crea el gitingore segun las indicaciones

### Claude Code · 25/10/2026 20:05

<details><summary>Herramientas usadas (2)</summary>

- `Write` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\.gitignore
- `Bash` Verify which paths the new gitignore excludes

</details>

Creé `tarea_2/.gitignore` con las cuatro líneas que pide el enunciado. Agregué tres cosas más:

- **Datos y modelos (del enunciado):** `datos/raw/`, `modelos/*.safetensors`, `modelos/*.bin` y `modelos/checkpoint-*/`.
- **Credenciales:** `.env` y `.streamlit/secrets.toml`, porque la lista de verificación exige no subir claves API. Este último aplica si después usas una clave de Gemini en Streamlit.
- **Temporales:** `.ipynb_checkpoints/` y `__pycache__/`.

Probé las reglas con `git check-ignore`:

| Ruta | Resultado |
|---|---|
| `datos/raw/audio/...`, `datos/raw/documentos/...`, pesos de modelos, `.env` | Se ignoran |
| `datos/documentos.csv`, `datos/ejemplos/...`, `modelos/config.json` | Se versionan |
| `tarea_1/` | Sin cambios, porque las reglas solo aplican dentro de `tarea_2/` |

Todavía no hice commit. ¿Quieres que lo haga ahora en la rama `P1-Corpus-y-extraccion`? Así empiezas a sumar historial de commits, que vale 1 punto.

---

## 5. Estudiante · 25/10/2026 20:37

> Ya están descargados los documentos. Haz la primera celda mardown de la parte 1. Te paso en breves las fuentes y licencias

### Claude Code · 25/10/2026 20:37

<details><summary>Herramientas usadas (6)</summary>

- `Bash` List tarea_2 contents and show notebook JSON
- `Read` C:\Users\agarces\.claude\projects\C--Users-agarces-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio\memory\no-rescrape-no-overwrite-notebook.md
- `Bash` List document images with dates, sizes and hashes
- `ToolSearch` select:NotebookEdit
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb

</details>

Antes de escribir la celda reviso dónde quedaron los documentos y el estado actual del notebook.

Agregué la celda markdown al inicio de `tarea_2/01_extraccion.ipynb`, encima de la celda de código vacía, sin tocar nada más. Incluye lo que pide el paso 1:

- **Título y pregunta guía**, con un resumen de lo que hace el notebook.
- **Fecha de extracción:** documentos, 25/10/2026, según la fecha de los archivos. La fecha del audio quedó pendiente.
- **Fuentes y licencias:** tablas para documentos y audio, marcadas como _(pendiente)_. Las lleno cuando me pases los datos. Si cada archivo tiene una fuente distinta, cambio la tabla a una fila por archivo.
- **Versiones:** Python 3.12.15, PaddleOCR 3.7.0 y, para el audio, faster-whisper 1.2.1 con el modelo turbo, VAD y diarización de pyannote, todo mediante `voz.py`.

Para el audio puse el modelo turbo porque es el que usa `voz.py` y ya está descargado. Si prefieres `small` para que transcriba más rápido en CPU, lo cambio.

⚠️ **Te falta un documento.** Hay 24 imágenes y el mínimo es 25, con 9 manuscritos. Tienes 8 impresos y 8 fotos, que están bien, pero solo 8 manuscritos: `Manuscrito-1`, `2`, `3.1` a `3.3` y `4.1` a `4.3`. Además, no hay archivos duplicados (lo revisé comparando el hash de cada archivo).

Un detalle sobre la calidad: los impresos y manuscritos tienen poca resolución (unos 500×770 píxeles), así que parecen capturas de pantalla. PaddleOCR puede fallar más con imágenes de ese tamaño. Si tienes los originales en mayor resolución, conviene usarlos.

Pásame las fuentes y licencias cuando las tengas.

---

## 6. Estudiante · 25/10/2026 20:41

> Actualiza. ya subi un manuscrito mas

### Claude Code · 25/10/2026 20:41

<details><summary>Herramientas usadas (3)</summary>

- `Bash` List manuscripts, count files and check duplicates
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb

</details>

Ya está `Manuscrito-5.png`: ahora son 25 documentos (8 + 8 + 9) y ninguno está duplicado. Actualizo la fila de manuscritos en la celda.

Actualicé la celda. El corpus de documentos ya cumple el mínimo: **25 imágenes**, con 8 impresos, 8 fotos y 9 manuscritos. Agregué `Manuscrito-5` a la tabla y una columna con la cantidad por tipo.

Revisé otra vez que no hubiera archivos repetidos (por hash) y no hay ninguno.

Las fuentes y licencias siguen como _(pendiente)_. Pásamelas y las completo en esta celda y en `datos/fuentes.csv`.

---

## 7. Estudiante · 25/10/2026 20:43

> Ahora si. La fuente de impreso-nitido es esta: https://revistafenix.bnp.gob.pe/index.php/fenix/article/view/515 y de manuscritos, son estos 4 links: https://bibliotecadigital.bnp.gob.pe/items/d2c6e978-52d4-4bb0-9f95-5104a308837c;origin=internal https://bibliotecadigital.bnp.gob.pe/items/00383e3a-518b-4397-9dcb-fe2710f3ab7b;origin=internal https://bibliotecadigital.bnp.gob.pe/items/661a505e-5dc5-411a-a174-2ef8499bd0f7;origin=internal  https://bibliotecadigital.bnp.gob.pe/items/5bd20bc1-c0b3-49c6-9beb-c2f5bc467bb6;origin=internal

### Claude Code · 25/10/2026 20:43

<details><summary>Herramientas usadas (7)</summary>

- `Bash` Fetch BNP item metadata and Fenix article page
- `Bash` Parse Fenix article metadata/license and probe BNP item page
- `Bash` Check Fenix license context and BNP site robots/status
- `Bash` Show Fenix license context and BNP robots.txt
- `WebFetch` https://bibliotecadigital.bnp.gob.pe/items/d2c6e978-52d4-4bb0-9f95-5104a308837c
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb

</details>

Primero verifico las licencias en cada fuente. La Biblioteca Digital de la BNP tiene una API pública, así que consulto los metadatos de cada ítem directamente.

Me bloquearon ese comando porque incluía una petición con User-Agent de navegador, y no voy a disfrazarme así. Repito solo las consultas legítimas, con un User-Agent que dice quién soy.

La Biblioteca Digital de la BNP responde 404 a cualquier petición por terminal, incluso para `robots.txt`. Pruebo una vez con WebFetch y, si tampoco funciona, no insisto.

No pude leer las páginas de la BNP Digital: el sitio carga su contenido con JavaScript y bloquea las peticiones automáticas. Mientras tanto, completo lo que sí verifiqué de *Fénix*.

Actualicé la celda con los datos que pude confirmar.

**Impresos (`Impreso-nitido-1` a `8`): verificado.** Revisé los metadatos de la página del artículo en *Fénix*:
- **Referencia:** Núñez, E. (1969), «Un manuscrito autógrafo y desconocido de Mariano Melgar», *Fénix* n.º 19, pp. 67-77, DOI `10.51433/fenix-bnp.1969.n19.p67-77`.
- **Licencia:** **CC BY-NC-ND 4.0**, según la política editorial de la BNP que aparece en la misma página. Permite el uso académico y no comercial, y mostrar las páginas citando la fuente. Lo que no permite es modificar la obra, y extraer el texto con OCR para analizarlo no cuenta como modificarla.

**Manuscritos: puse los 4 enlaces, pero no pude ver la licencia.** La Biblioteca Digital de la BNP carga su contenido con JavaScript y responde 404 a las peticiones automáticas, incluso a `robots.txt`. No voy a intentar saltarme ese bloqueo.

Para completar la tabla me faltan tres cosas:
1. **La licencia de cada ítem de la BNP.** Abre los 4 enlaces en tu navegador y copia el campo de derechos (algo como "Derechos", "Licencia" o "Dominio público"). Si puedes, copia también el título y la fecha de cada uno.
2. **Qué enlace corresponde a cada manuscrito.** Hay 5 manuscritos (`1`, `2`, `3.x`, `4.x` y `5`) y solo 4 enlaces, así que alguno debe compartir fuente. Por ejemplo: `d2c6e978` corresponde a `Manuscrito-1` y `Manuscrito-2`.
3. **La fuente de las fotos (`sombras-inclinacion-1` a `8`).** ¿Son fotos tuyas? En ese caso, ¿de qué documento son? Necesito saberlo para confirmar que no contienen datos personales.

---

## 8. Estudiante · 25/10/2026 20:46

> tranquilo, la licencia de la BNP es licencia creative commons dominio publico

### Claude Code · 25/10/2026 20:46

<details><summary>Herramientas usadas (1)</summary>

- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb

</details>

Listo. En la fila de manuscritos ahora dice **"Dominio público (Creative Commons), según la ficha de cada ítem en BNP Digital"**.

De los documentos solo falta la **fuente de las fotos** (`sombras-inclinacion-1` a `8`). ¿Son fotos tuyas o vienen de algún sitio?

Para `fuentes.csv` también me sirve saber qué enlace de la BNP corresponde a cada manuscrito. Si no tienes el dato a mano, pongo los 4 enlaces en cada fila y seguimos con el OCR.

---

## 9. Estudiante · 25/10/2026 20:48

> sombras-inclinacion son fotos de libros. Son los siguientes: https://themis.com.pe/producto/el-regimen-de-contrataciones-con-el-estado/ https://themis.com.pe/producto/revista-88-derecho-constitucional/ https://www.sancristoballibros.com/libro/vision-global-del-proceso_95544 . en todos los casos la licencia es Creative Commons Atribución 4.0 Internacional (CC BY 4.0)

### Claude Code · 25/10/2026 20:48

<details><summary>Herramientas usadas (5)</summary>

- `Bash` Fetch the three book pages and search for license info
- `Bash` Check THEMIS journal license on PUCP portal
- `Bash` Open THEMIS 88 issue page and look for license
- `Bash` Find THEMIS 88 issue link
- `Bash` Check license on THEMIS issue 88 page

</details>

Antes de anotarlo verifico la licencia en esas páginas. Las tres son tiendas de libros, y es poco común que una obra comercial tenga licencia CC BY.

Revisé las tres páginas y **no aparece ninguna mención a Creative Commons**:

| Fuente | Lo que dice la página |
|---|---|
| Themis: *El régimen de contrataciones con el Estado* | Libro a la venta (S/ 65.00), "Derechos Reservados" |
| Themis: *Revista 88: Derecho Constitucional* | Producto a la venta, "Derechos Reservados" |
| San Cristóbal: *Visión global del proceso* | Libro a la venta, "Todos los derechos reservados" |

Busqué también el n.º 88 de THEMIS en el portal de revistas de la PUCP. Existe, pero ahí tampoco encontré la licencia.

Prefiero no poner "CC BY 4.0" sin respaldo. Las licencias se califican, y la regla dice que solo se usen archivos con licencia que permita el uso.

Hay una salida que el enunciado acepta: **"capturas propias sin datos personales reales"**. Mi recomendación es registrar así las fotos:

- **Fuente:** foto propia de un libro impreso, con su ficha (título, editorial, ISBN y enlace).
- **Licencia:** "© [editorial], todos los derechos reservados; captura propia para uso académico".
- **En el dashboard:** mostrar solo el texto del OCR y los metadatos, sin publicar las imágenes.

¿Lo dejo así? Si tienes un respaldo de la licencia CC BY 4.0, como la página legal del libro donde lo diga, pásamelo y lo anoto tal cual.

---

## 10. Estudiante · 25/10/2026 20:51

> ponlo como sugieres. pero si tengo el respaldo, solo que esta por cada articulo de cada libro (e.g. https://revistas.pucp.edu.pe/index.php/themis/es/article/view/33548)

### Claude Code · 25/10/2026 20:51

<details><summary>Herramientas usadas (11)</summary>

- `Bash` Check license and metadata of THEMIS article 33548
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\datos\raw\documentos\sombras-inclinacion-1.jpg
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\datos\raw\documentos\sombras-inclinacion-2.jpg
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\datos\raw\documentos\sombras-inclinacion-3.jpg
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\datos\raw\documentos\sombras-inclinacion-4.jpg
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\datos\raw\documentos\sombras-inclinacion-5.jpg
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\datos\raw\documentos\sombras-inclinacion-6.jpg
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\datos\raw\documentos\sombras-inclinacion-7.jpg
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\datos\raw\documentos\sombras-inclinacion-8.jpg
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb

</details>

Reviso el artículo que me pasaste para confirmar su licencia.

Actualicé la celda con las fotos separadas por fuente:

- **Fotos 1 y 2, THĒMIS 88:** **CC BY 4.0**, que verifiqué en los metadatos del artículo 33548 que me pasaste.
- **Fotos 5, 6 y 8, *El régimen de contrataciones con el Estado*:** foto propia, "© Themis, derechos reservados".
- **Foto 7, *Visión global del proceso*:** foto propia, "© San Cristóbal Libros, derechos reservados".
- **Fotos 3 y 4, *Estudio de anulación de laudos 2022*:** quedaron como _(pendiente)_.

También agregué una nota en la celda: las fotos son capturas propias sin datos personales, y las que tienen derechos reservados no se van a mostrar en el dashboard (solo su texto OCR y metadatos).

Me faltan dos datos:
1. **¿De dónde salen las fotos 3 y 4?** Ese libro no está en los enlaces que me pasaste.
2. **¿La foto 8 es del libro de contrataciones con el Estado?** La asigné ahí por el tema; el título del libro no se ve en la página.

Si tienes los enlaces por artículo con CC BY para los otros libros, como el de THEMIS, pásamelos y cambio esas filas a CC BY 4.0.

Ya son casi las 21:00. ¿Paso a escribir las celdas de OCR con PaddleOCR mientras me respondes?

---

## 11. Estudiante · 25/10/2026 20:54

> 3 y 4 salen de aqui: https://www.arbitrajeccl.com.pe/wp-content/uploads/2024/04/Estudio-de-anulacion-de-laudos-2022.pdf

### Claude Code · 25/10/2026 20:54

<details><summary>Herramientas usadas (7)</summary>

- `Bash` Download CCL PDF and search its front matter for license
- `Bash` Inspect PDF text and search whole document for license
- `Bash` Render PDF cover, credits and last page to PNG
- `Read` C:\Users\agarces\AppData\Local\Temp\claude\C--Users-agarces-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio\babda432-59ec-4764-9da9-14b0848c6b99\scratchpad\descarga_ccl\p2.png
- `Read` C:\Users\agarces\AppData\Local\Temp\claude\C--Users-agarces-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio\babda432-59ec-4764-9da9-14b0848c6b99\scratchpad\descarga_ccl\p4.png
- `Bash` Confirm photo pages match the CCL PDF
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb

</details>

Reviso el PDF para buscar su licencia.

Las primeras páginas del PDF son imágenes, así que la búsqueda de texto no encuentra nada. Las convierto a PNG para revisar la portada y los créditos.

Las páginas de créditos están en blanco, así que el PDF **no declara ninguna licencia**. Antes de anotarlo, confirmo que las páginas 24 y 45 coinciden con tus fotos.

Coinciden: los textos de las fotos 3 y 4 aparecen en las páginas 24 y 45 del PDF. Actualizo la fila.

Actualicé la fila de las fotos 3 y 4 en la celda:

- **Fuente:** *Estudio de anulación de laudos 2022*, del Centro de Arbitraje de la Cámara de Comercio de Lima, pp. 24 y 45, con el enlace al PDF. Comprobé que el texto de tus fotos coincide con esas páginas del PDF.
- **Licencia:** el PDF es de acceso libre, pero no declara ninguna licencia; revisé el texto y las páginas de créditos, que están en blanco. Lo dejé como "Acceso libre, sin licencia declarada (derechos reservados); captura propia para uso académico", igual que los otros libros comerciales.

Con esto, la celda de configuración tiene completas las fuentes y licencias de los 25 documentos. Solo falta el audio.

Ya son pasadas las 21:00. Te propongo dos pasos:
1. **Hacer un commit ahora** con el `.gitignore` y esta primera celda, para que el historial muestre avance.
2. **Escribir y correr las celdas de OCR con PaddleOCR** para los 25 documentos. La primera vez descarga sus modelos y luego procesa todo en CPU, lo que puede tomar unos minutos.

¿Avanzo con ambos?

---

## 12. Estudiante · 25/10/2026 21:10

> he reemplazado las sombras-inclincacion 5-8. Todas vienen de: https://revistas.pucp.edu.pe/index.php/themis/es/issue/view/1850 con ccby4.0. Actualiza

### Claude Code · 25/10/2026 21:10

<details><summary>Herramientas usadas (7)</summary>

- `Bash` List replaced photos and fetch THEMIS issue 1850 contents
- `Bash` Verify license metadata of a THEMIS 81 article
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\datos\raw\documentos\sombras-inclinacion-5.jpg
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\datos\raw\documentos\sombras-inclinacion-6.jpg
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\datos\raw\documentos\sombras-inclinacion-7.jpg
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\datos\raw\documentos\sombras-inclinacion-8.jpg
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb

</details>

Reviso las fotos nuevas y la licencia de ese número de THEMIS.

Actualicé la celda. Las fotos 5 a 8 ahora figuran como THĒMIS n.º 81 (2022), con enlaces al número y a los dos artículos, y licencia **CC BY 4.0**. Verifiqué la licencia en los metadatos del artículo 26488, que es del mismo número.

Así queda la licencia de los 25 documentos:

| Documentos | Licencia |
|---|---|
| 8 impresos (*Fénix*) | CC BY-NC-ND 4.0 |
| Fotos 1, 2 y 5 a 8 (THĒMIS 88 y 81) | CC BY 4.0 |
| 9 manuscritos (BNP) | Dominio público |
| Fotos 3 y 4 (estudio de la CCL) | Sin licencia declarada; las anoté como captura propia para uso académico |

Las fotos 3 y 4 son las únicas que no se van a mostrar como imagen en el dashboard. Si quieres que todo el corpus tenga licencia abierta, podrías reemplazarlas por otras dos páginas de THĒMIS. No es obligatorio, porque el enunciado acepta capturas propias.

¿Sigo con el commit y las celdas de OCR?

---

## 13. Estudiante · 25/10/2026 21:13

> retira las columnas de tipo y N.o

### Claude Code · 25/10/2026 21:13

<details><summary>Herramientas usadas (2)</summary>

- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb

</details>

Listo. Quité las columnas **Tipo** y **N.º**, así que la tabla de documentos ahora tiene tres columnas: Archivos, Fuente y Licencia. El resto de la celda no cambió.

---

## 14. Estudiante · 25/10/2026 21:16

> empieza a extraer el texto de los documentos con Paddle OCR

### Claude Code · 25/10/2026 21:16

<details><summary>Herramientas usadas (24)</summary>

- `Bash` Find session 10 materials using PaddleOCR
- `Bash` Read course PaddleOCR runner and lecture code cells
- `Bash` Check PaddleOCR 3.7 language-to-model mapping
- `Bash` Read PaddleOCR model selection logic
- `Bash` Read the PP-OCRv6 language list
- `Bash` Find PP-OCRv6 supported languages definition
- `Bash` Test PaddleOCR on three sample documents and time it
- `Bash` Compare OCR speed with oneDNN on and PyTorch engine
- `Bash` Check whether PyTorch OCR weights were downloaded
- `Bash` Time PaddleOCR with the PyTorch engine
- `Bash` Check notebook execution tools, CPU cores and kernel spec
- `Bash` Inspect PaddleX save_to_img behavior
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `Bash` Execute the notebook copy in the background to run OCR
- `Read` C:\Users\agarces\AppData\Local\Temp\claude\C--Users-agarces-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio\babda432-59ec-4764-9da9-14b0848c6b99\tasks\bg0h2r9rj.output
- `Bash` Test which import order triggers the torch DLL error
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `Bash` Re-run the notebook copy in the background for OCR

</details>

Primero reviso cómo se usó PaddleOCR en la Sesión 10, para seguir el mismo patrón del curso.

oneDNN falla con el mismo error que documentó el laboratorio. El motor PyTorch no respondió en casi 5 minutos, quizá porque estaba descargando sus pesos. Reviso si llegó a descargarlos.

Ya se descargaron los pesos para PyTorch. Repito la prueba con ese motor.

Las celdas de OCR ya están en el notebook. Ahora lanzo la ejecución en segundo plano sobre una copia, que tomará unos 40 minutos.

La extracción con PaddleOCR ya está corriendo en segundo plano.

**Lo que agregué al notebook**, después de la celda de configuración:
- **Configuración del entorno:** imports y carpetas, y la celda imprime la fecha de ejecución y las versiones de PaddleOCR y Paddle.
- **2.1 Inventario:** le asigna a cada imagen un id de `doc_001` a `doc_025`, ordenados por tipo y número. También registra su tipo (impreso, foto o manuscrito), su resolución y su hash SHA-256, que sirve después para detectar duplicados.
- **2.2 Parámetros del OCR:** una tabla que documenta el idioma, el dispositivo, oneDNN y que no hay preprocesamiento, con el motivo de cada elección. El paso 2 del enunciado pide documentar esto.
- **OCR con respaldo:** por cada documento guarda en `datos/raw/documentos/` el JSON crudo, la página con las cajas dibujadas y el recorte de cada línea. Si el notebook se vuelve a ejecutar, reutiliza lo guardado en vez de procesar todo otra vez.
- **Resumen por tipo:** líneas promedio, confianza promedio y minutos de procesamiento, más un ejemplo de texto de cada tipo.

**La ejecución:** corre sobre una copia en el scratchpad, así no toco el notebook que tienes abierto. Empezó a las 21:44 y debería terminar alrededor de las 22:25. Cuando termine reviso los resultados.

Mientras tanto podemos avanzar con el **audio**. ¿Ya tienes los clips (al menos 30 minutos en 20 o más clips, con uno de dos o más hablantes)? Si todavía no, dime qué fuente prefieres. OpenSLR 73 trae español peruano con licencia CC BY-SA 4.0, pero son frases muy cortas y de un solo hablante. Para el clip de varios hablantes harían falta entrevistas de Wikimedia Commons.

Confirmado: si `paddle` se importa antes que `paddleocr`, torch ya no puede cargar sus DLL en Windows. Corrijo el orden de los imports en la celda de configuración y lo dejo comentado:

Relanzo la ejecución. Esta vez guardo el log completo para ver bien cualquier error.

Relancé la extracción con PaddleOCR a las 21:52, ya con el orden de imports corregido.

La primera vez falló porque en Windows importar `paddle` antes que `paddleocr` impide que torch cargue sus DLL. Lo confirmé probando los dos órdenes, y dejé un comentario en la celda que lo explica.

Debería terminar alrededor de las 22:30. Si falla antes, me entero de inmediato. Cuando termine reviso los resultados por tipo de documento.

Mientras tanto, sigue pendiente lo del **audio**. ¿Ya tienes los clips o te ayudo a buscar fuentes?

---

## 15. Estudiante · 25/10/2026 21:44

> ya tengo los clips. Estan en ""C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\datos\raw\audio" . La tabla informativa esta en "C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\DiplomadoPUCP2026_FundamentosPython\tarea_2\datos\raw\audio\manifiesto_descarga.csv". Revísalos e incorporalos al corpus

### Claude Code · 25/10/2026 21:44

<details><summary>Herramientas usadas (7)</summary>

- `Bash` List audio clips and show download manifest
- `Bash` Match manifest to WAV files: durations, format, licenses, duplicates
- `Bash` List functions and classes in voz.py
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\Data-Science-Python\sessions\13-audio-a-texto\voz.py
- `Bash` Detect spoken language of each clip with Whisper
- `Bash` Transcribe 35s samples of rural clips as Spanish
- `Bash` Count finished OCR documents and show time

</details>

Reviso los clips y el manifiesto.

Revisé los 20 clips y encontré un problema: **7 de los 9 clips rurales de Áncash (del 012 al 018) están principalmente en quechua.** Las preguntas de la entrevista son en español, pero las respuestas son en quechua. Whisper no soporta quechua e inventa texto, por ejemplo *"y y y y y y y"* o *"¿Qué ha hecho usted?"* repetido tres veces. Esos clips no sirven como español peruano, y transcribirlos así es justo la falla de alucinación que advierte el enunciado.

| Clips | Idioma | Clips | Minutos |
|---|---|---|---|
| 001–011 (calle y lectura) | Español | 11 | 27,9 |
| 019, 020 (rurales) | Español con palabras en quechua; se pueden usar | 2 | 4,3 |
| **Subtotal válido** | | **13** | **32,3** |
| 012–018 (rurales) | Quechua con preguntas en español | 7 | 16,0 |

Los minutos alcanzan (32,3 de 30), pero **faltan 7 clips en español para llegar a 20**.

Te recomiendo:
1. **Descargar 7 clips o más en español** de Commons. Lo más rápido es buscar más grabaciones `Es-Huaca …-article.ogg`, que son lecturas de estudiantes peruanos, o más entrevistas de Fiestas Patrias. Ya tienes el script que armó el manifiesto, así que basta con agregarlas ahí.
2. **Sacar del corpus en español los clips 012 a 018** y reportarlos como descartados, con el motivo: idioma quechua y alucinaciones de Whisper. Así lo pide el paso de limpieza.
3. **Opcional, para la bonificación:** esos mismos clips son quechua de Áncash, justo el caso de "quechua de Huaylas con MMS" que da puntos extra en la Parte 2.

Mientras tanto, el OCR va por 8 de 25 documentos, con los 8 impresos listos. Cuando confirmes el corpus de audio, preparo las celdas de transcripción para correrlas apenas termine el OCR.

---

## 16. Estudiante · 25/10/2026 22:04

> si, reportalos como descartados

### Claude Code · 25/10/2026 22:05

<details><summary>Herramientas usadas (34)</summary>

- `Bash` Copy voz.py and manifest; test diarization model access
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `Bash` Transcribe a sample of clip_020 to check language
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `Bash` Build a temporary notebook with only the ASR cells
- `Bash` Run the ASR-only notebook in the background
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `Bash` Test pandas multi-column assignment from tuples
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `Bash` Show OCR and ASR progress
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `Bash` Check progress, kaleido and Chrome availability

</details>

Entendido: los clips del 012 al 018 quedan como descartados por idioma. Así el corpus de audio queda en **13 clips y 32,3 minutos**. Los minutos alcanzan, pero sigue faltando para el mínimo de 20 clips. Si más tarde agregas clips en español al manifiesto, las celdas los van a tomar sin cambios.

Ahora copio `voz.py` y el manifiesto a `tarea_2`, y verifico que el modelo de diarización se pueda descargar sin token de Hugging Face.

La diarización funciona sin token, y rapidfuzz (para la seudonimización) ya está instalado. Actualizo la celda de configuración con el corpus de audio.

Ahora agrego la sección 3 de audio: inventario, revisión de idioma y transcripción con VAD y diarización.

Todavía no revisé una muestra del clip 020 y no quiero afirmar algo sin comprobarlo. Lo transcribo rápido:

El clip 020 está en español ("¿Qué planta? Es flor… Siempre viva"), así que la afirmación es correcta. Sigo con la celda de inventario:

Por error inserté una celda de relleno. La elimino:

Verifico rápido que la asignación de dos columnas con una lista de tuplas funcione en esta versión de pandas:

Funciona; el tipo de la columna queda como `object`, pero las sumas y comparaciones dan bien. Sigo con la **limpieza**:

Reviso rápido cómo van las dos ejecuciones antes de seguir con el EDA:

Las dos celdas quedaron en orden invertido porque las inserté en paralelo después de la misma celda. Lo corrijo: borro la de código y la vuelvo a insertar después del markdown.

Cambio los colores de las condiciones de audio para que no se repitan con los de los tipos de documento, porque el histograma muestra las dos leyendas juntas:

Ahora la **validación** de los extremos y la **exportación** de los tres CSV:

Corrijo un detalle: si algún documento se descartara, quedaría fuera de `fuentes.csv`. Calculo la fuente sobre todos los documentos y no solo sobre los conservados:

Ya está escrita toda la Parte 1 en el notebook, de la sección 1 a la 8. Las dos ejecuciones siguen corriendo.

**Lo que agregué:**

| Sección | Qué hace |
|---|---|
| 3. Audio | Inventario desde el manifiesto, detección de idioma con Whisper y los 7 clips en quechua marcados como descartados con su motivo. Transcripción con VAD, diarización en todos los clips, salida con marcas `[HABLANTE_n]` y exportación a JSON, CSV, SRT y TXT por clip. |
| 4. Seudonimización | Nombres de las personas entrevistadas → `[PERSONA_n]` con `voz.seudonimizar`, más búsqueda de DNI, teléfonos y correos con expresiones regulares. Reporta cuántas entidades reemplaza en cada corpus. |
| 5. Limpieza | Duplicados por hash, documentos ilegibles, audios sin voz y descartes por idioma, con su motivo. Termina con una lista de los mínimos de la tarea, marcando ✔ o ✘. |
| 6. EDA | Los 3 gráficos de Plotly Express; los títulos se arman con los datos para expresar la conclusión. |
| 7. Validación | Los 3 documentos y clips más largos y más cortos, y una verificación de que coinciden con los bordes de los histogramas. |
| 8. Exportación | `documentos.csv`, `transcripciones.csv` y `fuentes.csv`, que incluye también los descartados; muestra `shape` y `head(5)` de cada uno. |

**Progreso a las 22:15:** el OCR va en 13 de 25 documentos y el audio sigue en la detección de idioma. Van lento porque compiten por la CPU, así que calculo que ambos terminan entre 22:40 y 22:50.

**Dos decisiones que necesito de ti:**
1. **¿Instalo `kaleido`?** Sin él, GitHub no muestra los gráficos de Plotly y el notebook quedaría con los gráficos en blanco, aunque el enunciado exige que se vean. Tienes Chrome instalado, que es lo que usa kaleido. Lo instalaría igual que EasyOCR, sin cambiar ninguna otra versión del entorno.
2. **¿Hago commit ahora** del `.gitignore`, `voz.py` y el notebook en la rama `P1-Corpus-y-extraccion`? Así el historial muestra avance antes de la entrega.

Ten en cuenta que con 13 clips la lista de la limpieza va a marcar **✘ en "Clips de audio" (13 de 20)**. Si consigues 7 clips más en español antes de que termine el audio, solo hay que agregarlos al manifiesto y a la carpeta.

---

## 17. Estudiante · 25/10/2026 22:17

> 1. si, 2. no todavía

### Claude Code · 25/10/2026 22:17

<details><summary>Herramientas usadas (3)</summary>

- `Bash` Dry-run kaleido install with current versions pinned
- `Bash` Install kaleido and test PNG export of a Plotly chart
- `Bash` Verify Plotly renderers and check progress

</details>

Instalo kaleido con el mismo cuidado que EasyOCR: primero una simulación con las versiones actuales fijadas.

kaleido funciona: exportó un gráfico de prueba a PNG usando tu Chrome. El aviso "unclean kill browser" no afecta. Verifico que exista el renderizador combinado que usa el notebook:

Instalé `kaleido` 1.5.0 en `ds-python-up`. Solo se agregaron tres paquetes (`kaleido`, `choreographer` y `logistro`) y no cambió ninguna versión existente. Probé exportar un gráfico a PNG y funcionó, así que los 3 gráficos del EDA van a aparecer en GitHub. No hice commit.

**Progreso a las 22:19:**
- **OCR:** 15 de 25 documentos.
- **Audio:** terminó la detección de idioma y ya está transcribiendo los 13 clips.

Cuando terminen, ejecuto el notebook completo sobre los respaldos ya guardados, lo que tomará pocos minutos. Después reviso las transcripciones para completar la lista de nombres a seudonimizar con los que se escuchen en las grabaciones.

Queda poco más de hora y media para la entrega. Mientras esperamos, ¿empiezo a armar `app.py` para la Parte 3? Puede leer los CSV que va a generar este notebook, y desplegarla en Streamlit Cloud pide tiempo de tu parte.

---

## 18. Estudiante · 25/10/2026 22:25

> si porfa

### Claude Code · 25/10/2026 22:26

<details><summary>Herramientas usadas (15)</summary>

- `Write` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\app.py
- `Bash` Check Streamlit 1.62 width parameters and deprecations
- `Edit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\app.py
- `Edit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\app.py
- `Write` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\requirements.txt
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `Bash` Check OCR/ASR progress and language detection output
- `Bash` Preview transcripts and search for spoken names
- `Bash` Show time, tarea_2 contents and git status
- `Bash` Syntax-check app.py and remove pycache
- `Bash` Show OCR run outputs from executed notebook copy
- `Bash` Check ASR progress and search new transcripts for names
- `Bash` Show per-clip ASR processing times

</details>

Armo `app.py` para que lea solo los CSV y no cargue ningún modelo, así funciona dentro de los límites de Streamlit Community Cloud. Los resultados de la Parte 2 (métricas, extracción con LLM y auditoría) los toma si existen; si todavía no están, muestra "pendiente" en lugar de fallar.

`use_container_width` está obsoleto. Lo reemplazo por `width="stretch"` y cambio la expresión suelta por un `if`/`else` normal:

Creo `requirements.txt` solo con lo que la app necesita, en las mismas versiones que probé localmente:

Para asegurar el filtro por `publicar_imagen` convierto la columna a booleano explícitamente, porque viene de una lista de tuplas:

El OCR va en 23 de 25 y el audio en 6 de 13. Reviso las transcripciones que ya están listas para buscar nombres de personas que haya que seudonimizar:

El audio va en 6 de 13 clips. Ahora que terminó el OCR debería acelerar; calculo que termina cerca de las 22:45. Después:
1. Agrego los nombres que encontré a la seudonimización.
2. Ejecuto el notebook completo con los respaldos ya guardados, lo que toma pocos minutos.
3. Pruebo `app.py` con los CSV reales.

Un punto importante sobre el tiempo: **la Parte 2 depende de una transcripción manual que tienes que hacer tú.** Son 10 documentos y 10 clips de audio, y el enunciado prohíbe usar referencias automáticas como si fueran manuales. Con cerca de una hora y media disponible, eso es muy difícil de completar: solo una página de *Fénix* tiene unas 400 palabras, y 10 clips son unos 25 minutos de audio.

Te sugiero esta prioridad:
1. **Parte 1 completa y ejecutada** (6 puntos), que estará lista pronto.
2. **App desplegada en Streamlit Cloud** (4 puntos). Ese paso es tuyo, porque necesita tu cuenta, y conviene hacerlo cuanto antes.
3. **Parte 2:** puedo dejar el notebook armado (selección de la muestra, línea base, EasyOCR y el segundo modelo de audio) para que solo falte llenar `texto_referencia`. Si quieres empezar a transcribir ya, te recomiendo como muestra los documentos más cortos de cada tipo y los clips más cortos.

¿Te parece bien este orden?

---

## 19. Estudiante · 25/10/2026 22:32

> ya estoy avanzando con la transcripcion. cuales son los clips mas cortos?

### Claude Code · 25/10/2026 22:33

<details><summary>Herramientas usadas (8)</summary>

- `Bash` Rank documents by OCR word count per type
- `Bash` Check ASR run status and search all transcripts for names
- `Bash` See which name-like words matched in reading clips
- `NotebookEdit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\01_extraccion.ipynb
- `Bash` Check notebook mtime and back it up before in-place run
- `Bash` Execute the full notebook in place in the background
- `Bash` Summarize speakers, words and RTF per clip
- `Write` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\README.md

</details>

Estos son los **10 clips más cortos** de los 13 válidos. Suman unos **21 minutos** y cubren las tres condiciones de grabación (6 de calle, 2 de lectura y 2 rurales), así que cumplen lo de "distintas condiciones":

| Clip | Condición | Duración |
|---|---|---|
| `clip_020` | rural | 1:00 |
| `clip_004` | calle | 1:16 |
| `clip_003` | calle | 1:30 |
| `clip_005` | calle (ruido; Whisper alucina) | 1:40 |
| `clip_006` | calle | 1:44 |
| `clip_001` | calle | 2:16 |
| `clip_009` | lectura | 2:27 |
| `clip_008` | lectura | 2:36 |
| `clip_002` | calle | 3:09 |
| `clip_019` | rural | 3:20 |

Por si te sirve, estos son los **documentos más cortos** de cada tipo, según la cantidad de palabras que detectó el OCR:
- **Impresos:** `doc_005` (Impreso-nitido-5, ~205 palabras), `doc_006` (~213) y `doc_008` (~310).
- **Fotos:** `doc_012` (sombras-inclinacion-4, ~256), `doc_011` (sombras-inclinacion-3, ~326) y `doc_016` (sombras-inclinacion-8, ~526).
- **Manuscritos:** `doc_021` (Manuscrito-3.3, ~37), `doc_024` (4.3, ~73), `doc_022` (4.1, ~76) y `doc_023` (4.2, ~82).

Con 3 impresos, 3 fotos y 4 manuscritos completas los 10 y cubres los tres tipos.

Dos recomendaciones:
- **Transcribe mirando la imagen o escuchando el audio, no corrigiendo el texto del OCR o de Whisper.** Si partes del texto del modelo, la referencia hereda sus errores y el CER o el WER salen artificialmente bajos, que es justo una de las fallas que lista el enunciado.
- **Guarda cada transcripción como texto plano en UTF-8** en `tarea_2/datos/referencias/`, con el id como nombre (por ejemplo `doc_005.txt` o `clip_020.txt`). En los clips basta con lo que se dice; no hace falta marcar hablantes, porque el WER los excluye. Después el notebook de la Parte 2 lee esos archivos y llena `texto_referencia`.

Terminó la transcripción de los 13 clips. Reviso el resultado y busco nombres en los clips nuevos:

Mientras el notebook se ejecuta, empiezo el `README.md` con lo que ya sé. Los números finales del audio los completo cuando termine la ejecución.

---

> *25/10/2026 22:47 · La conversación superó el límite de contexto y Claude Code la resumió automáticamente; continúa en el mismo hilo.*

### Claude Code · 25/10/2026 22:47

<details><summary>Herramientas usadas (53)</summary>

- `Bash` Check background run log and current time
- `Bash` Summarize executed notebook outputs and check exported files
- `Bash` Check issue mentions of AI evidence folder and read EDA setup cell
- `ToolSearch` select:NotebookEdit
- `Bash` Back up notebook and silence kaleido logging in plotting helper
- `Bash` Re-execute the notebook in place with cached results
- `Bash` Smoke-test the Streamlit app with AppTest
- `Bash` Rerun AppTest with the absolute app path
- `Bash` Find how the search filter and word count are used
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\app.py
- `Bash` Verify README claims against detection and transcript files
- `Bash` Read the notebook's Quechua discard explanation
- `Bash` Check re-executed notebook for errors, stderr and PNGs
- `Bash` Show remaining stderr outputs
- `Bash` List logger names used by kaleido and choreographer
- `Bash` Silence kaleido logs for the rest of the notebook and re-execute
- `Edit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\README.md
- `Bash` Find the issue's Part 2 requirements in the transcript
- `ToolSearch` select:TaskStop
- `TaskStop` b0aop9boi
- `Bash` Fetch issue 190 and print the Part 2 section
- `Bash` List the issue's section headings
- `Bash` Print the issue's 02_evaluacion section and rubric
- `Bash` Check cached models and available ASR/LLM packages
- `Bash` Inspect voz.py transcriber API and package versions
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\voz.py
- `Bash` Write background scripts for alternative OCR and ASR runs
- `Bash` Check audio path column and fix document path in OCR script
- `Bash` Run baseline and alternative ASR on all clips in background
- `Bash` Run EasyOCR on all documents in background
- `Bash` Run Ollama structured extraction on all texts in background
- `Bash` Read voz metrics helpers, app expectations, and job progress
- `Bash` Show progress of the three background jobs
- `Bash` Read ASR and export cells from the extraction notebook
- `Bash` Patch export cell to keep manual references across reruns
- `Bash` Update export notes and check job progress
- `TaskStop` bvmedry3m
- `TaskStop` by7hl9h60
- `Bash` Check for orphaned Python processes and cached outputs
- `Bash` Reorder OCR and ASR jobs to process short items first
- `Bash` Relaunch ASR baseline and alternative in background
- `Bash` Relaunch EasyOCR in background, short documents first
- `Bash` Generate the 02_evaluacion notebook skeleton
- `Bash` Check what files exist in eval scratch and task folder
- `Write` C:\Users\agarces\AppData\Local\Temp\claude\C--Users-agarces-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio\babda432-59ec-4764-9da9-14b0848c6b99\scratchpad\eval\crear_02.py
- `Bash` Create 02_evaluacion notebook and check job progress
- `Bash` List shortest documents per type and cached outputs
- `Bash` Inspect ASR job log and running processes
- `Bash` Check LLM results and progress of OCR and ASR jobs
- `TaskStop` b09rghwu1
- `Bash` List EasyOCR outputs and remaining Python processes
- `Bash` Run LLM export and audit cells to create the audit sheet
- `Bash` Check ASR job progress

</details>

Volví a ejecutar el notebook. Ahora reviso que no tenga errores y que los registros de kaleido ya no aparezcan.

Ya volví a ejecutar el notebook y quedó limpio. Estoy revisando qué exige la Parte 2 en el issue para dejarla lista antes de que termines tus transcripciones.

Mientras corren, lanzo también la extracción con el LLM: Ollama `qwen2.5:3b` sobre los 38 textos, con salida en JSON. Es la tarea más larga y tampoco depende de tus referencias.

Mientras corren los modelos, armo `02_evaluacion.ipynb`. Primero reviso qué columnas espera `app.py` y las funciones de métricas que ya trae `voz.py`.

Los tres trabajos avanzan: EasyOCR va a unos 20 s por página y el LLM a unos 50 s por texto. Ahora escribo `02_evaluacion.ipynb`.

Ajusto primero la exportación de `01_extraccion.ipynb`: así tus referencias manuales no se borran si se vuelve a ejecutar, y las de audio pasan por la misma seudonimización antes de publicarse.

Mientras corren los modelos, escribo `02_evaluacion.ipynb`. Leerá tus referencias y calculará CER/WER en cuanto existan.

The command is too long for the shell. I'll write the generator script with the Write tool.

Tu notebook de la Parte 1 ya corre completo y sin errores, y la Parte 2 está armada. Lo que falta son tus referencias, la auditoría y el despliegue. Quedan unos 50 minutos.

**Parte 1, ya ejecutada**
- **Corpus:** 25 documentos (8 impresos, 8 fotos, 9 manuscritos) y 13 clips en español (32,3 min).
- **Mínimos:** cumple todos menos uno, «Clips de audio 13 (mínimo 20)», que queda marcado con ✘ en el notebook y en el README.
- **Seudonimización:** 14 nombres reemplazados en 4 clips; 0 en documentos.
- **Gráficos:** los 3 salen con imagen PNG, así que se ven en GitHub. Quité los mensajes de kaleido que llenaban la salida.
- **Exportación:** se generan `documentos.csv`, `transcripciones.csv` y `fuentes.csv` (45 filas, con los descartados), más 6 imágenes y 3 audios en `datos/ejemplos/`.
- **`app.py`:** lo probé con tus CSV y no da errores. Las métricas de la Parte 2 aparecen como «pendiente».
- **`README.md`:** escrito. Falta pegar el link de Streamlit.

**Parte 2, armada en `02_evaluacion.ipynb`**
- **Corriendo ahora:** EasyOCR (9 de 25 documentos), Whisper `small` como línea base y Parakeet v3 como ASR alternativo. El LLM `qwen2.5:3b` en Ollama va en 14 de 38 textos. Todo va del documento o clip más corto al más largo, y lo terminado queda guardado.
- **Va lento:** los tres trabajos se pelean la CPU. Whisper `small` todavía no termina el primer clip.
- **Dónde guardar tus referencias:** un archivo por caso en `tarea_2/datos/raw/referencias/<id>.txt`, por ejemplo `doc_021.txt` o `clip_020.txt`. Esa carpeta no se sube a Git. Al volver a ejecutar `01_extraccion.ipynb`, las copio a `texto_referencia` y les aplico la seudonimización antes de publicarlas.
- **Auditoría:** el notebook crea `datos/auditoria_llm.csv` con 20 casos. Tú llenas la columna `correcta` (sí/no); hay una columna de verificación automática para ayudarte.

**Los más cortos, por si te sirven**
- **Clips:** `clip_020` (60 s), `clip_004` (76 s), `clip_003` (90 s), `clip_005` (100 s), `clip_006` (104 s), `clip_001` (136 s), `clip_009` (147 s), `clip_008` (156 s), `clip_002` (189 s) y `clip_019` (200 s). Eso suma unos 21 minutos de audio para transcribir a mano.
- **Manuscritos:** `doc_021`, `doc_024`, `doc_022`.
- **Impresos:** `doc_005`, `doc_006`.
- **Fotos:** `doc_012`, `doc_011`.

**Necesito que me digas:**
1. **¿Qué 10 documentos y 10 clips estás transcribiendo?** Así le doy la CPU solo a esos y Whisper `small`, Parakeet y EasyOCR terminan a tiempo.
2. **¿Hago ya el commit y el push de la Parte 1, la app y el README?** El despliegue en Streamlit Cloud tarda unos minutos y depende del push, así que conviene hacerlo antes de la medianoche aunque la Parte 2 llegue después en otro commit.

Además, recuerda que la entrega pide las capturas de esta conversación en `tarea_2/evidencias_ia/` (01.png, 02.png…).

Mientras el ASR corre solo, genero `extraccion_llm.csv` y la plantilla de auditoría (no dependen de tus referencias), así puedes empezar a auditar ya.

El LLM ya extrajo los campos de los 38 textos y tengo lista la planilla de auditoría. El ASR alternativo es lo único que sigue corriendo y va lento.

- **`datos/extraccion_llm.csv`:** 38 filas, con unos 20 min de CPU en total.
- **`datos/auditoria_llm.csv`:** son 10 documentos y 10 audios elegidos al azar. Solo tienes que llenar las columnas `correcta` (sí/no) y `comentario`. La columna `chequeo_automatico` ayuda pero no decide; lo que ya marca:
  - `clip_001`: el LLM dice 3 hablantes, pero hay 2 marcas.
  - `clip_004`: ninguna de las 3 citas está copiada del texto; les inventó el prefijo «Habla 2:».
  - `doc_016`: puso una fecha («15 de mayo de 2022») que no aparece en el texto.
  - `clip_019`: usó `[PERSONA_2]` como si fuera un hablante. El chequeo no lo detecta porque quita las marcas, así que revísalo tú.
- **EasyOCR:** lo detuve en 22 de 25 documentos para liberar la CPU. Faltan `doc_003`, `doc_019` y `doc_020`; si alguno entra en tu muestra, el notebook lo calcula al ejecutarse.
- **ASR alternativo:** Parakeet v3 terminó de descargarse (casi 7 min) y está transcribiendo solo. Whisper `small` va en 1 de 13 clips. Ese primer clip tomó 588 s (RTF 9,7) porque competía con los otros procesos; borraré ese resultado y lo volveré a correr para que la latencia que reportes sea justa.

Sigo necesitando tus dos respuestas:
1. **¿Qué 10 documentos y 10 clips estás transcribiendo?**
2. **¿Hago ya el commit y el push de la Parte 1, `app.py` y el README?** Así puedes desplegar en Streamlit antes de las 23:59; la Parte 2 puede ir en otro commit.

---

## 20. Estudiante · 25/10/2026 23:24

> tengo las transcripciones de los documentos ya listas, pero en un excel, sirve? "C:\Users\agarces\Desktop\Documentos.xlsx"

### Claude Code · 25/10/2026 23:25

<details><summary>Herramientas usadas (28)</summary>

- `Bash` Inspect the user's Excel file of document transcriptions
- `Read` C:\Users\agarces\.claude\projects\C--Users-agarces-GITHUB-Diplomatura-PUCP-2026-diplomado-python-intermedio\memory\no-rescrape-no-overwrite-notebook.md
- `Bash` Save Excel references as text files and fill the documents CSV
- `Bash` Check whether the data folder and CSVs still exist
- `Bash` Inspect branches, stashes and reflog to see what changed
- `Bash` List Part 1 files present on main
- `Bash` List Part 1 files present on main
- `PowerShell` List Part 1 files present on main
- `Bash` Show working tree status
- `Bash` List Part 1 files on main and check fast-forward
- `Bash` Fast-forward the P2 branch to main
- `Bash` Save Excel references and fill the documents CSV column
- `Bash` Run EasyOCR on the three missing documents in background
- `Bash` Check ASR progress
- `Bash` Make the evaluation notebook tolerate missing audio references
- `Bash` Check EasyOCR progress on missing documents
- `Bash` Preview CER per document for both OCR models
- `Bash` Compare reference and OCR text for high-error documents
- `Bash` Locate large differences between reference and OCR in doc_002
- `Bash` Check EasyOCR completion
- `Bash` Execute the evaluation notebook in place
- `Bash` Fix empty-audio case and re-execute the evaluation notebook
- `Bash` Write the decision and reflection section into the notebook
- `Bash` Smoke-test the dashboard with evaluation CSVs
- `Read` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\app.py
- `Edit` C:\Users\agarces\GITHUB\Diplomatura PUCP 2026\diplomado_python_intermedio\tarea_2\app.py
- `Bash` Re-test dashboard metrics after the fix
- `Bash` Rerun clip_020 baseline alone for a fair latency

</details>

Sí, sirve. Las 10 filas del Excel corresponden a 3 impresos, 4 manuscritos y 3 fotos. Las guardo como referencias y actualizo `documentos.csv` directamente, sin volver a ejecutar el notebook.

Rama al día. Ahora cargo tus referencias del Excel y corro EasyOCR sobre los 3 documentos de tu muestra que le faltaban (`doc_003`, `doc_019`, `doc_020`).

Tus 10 referencias ya están cargadas: 3 impresos, 4 manuscritos y 3 fotos. Mientras EasyOCR termina los 3 documentos que faltan, reviso cómo va el audio.

Sí, el Excel sirve. Ya cargué tus 10 referencias en `documentos.csv` (3 impresos, 4 manuscritos y 3 fotos) y guardé una copia de cada una en `datos/raw/referencias/`, que no se sube a Git.

**Tu rama.** Habías cambiado a `P2-Evaluacion`, que salió de un `main` anterior al merge de la Parte 1, y por eso desaparecieron `app.py`, `README.md` y los CSV. No se perdió nada. Puse la rama al día con `main` mediante un avance rápido: no crea commits ni sube nada, y los archivos volvieron.

**CER preliminar de PaddleOCR (línea base):**

| Tipo | Documentos | CER |
|---|---|---|
| Impresos | `doc_001`, `doc_003` | 0,007 |
| Impresos | `doc_002` | 0,32 |
| Manuscritos | `doc_017` a `doc_020` | 0,20 a 0,25 |
| Fotos | `doc_011` | 0,18 |
| Fotos | `doc_009`, `doc_010` | 0,64 a 0,66 |

En las páginas a dos columnas (el poema de `doc_002` y las revistas de las fotos), PaddleOCR lee cada fila de lado a lado, mezclando las columnas, y tu referencia las lee una por una. Por eso el CER sube aunque las palabras estén bien leídas.

EasyOCR sale peor en los 7 documentos que ya terminó: CER entre 0,21 y 0,74. Faltan 2 manuscritos (`doc_019`, `doc_020`), que estarán en un minuto. El audio alternativo (Whisper `small` y Parakeet) va en 8 de 13 clips.

Quedan unos 30 minutos y necesito dos respuestas:
1. **¿Tienes referencias de audio?** Si las tienes, pásamelas igual, en Excel o como sea. Si no alcanzas, entrego el notebook con el WER como pendiente y el resto de la Parte 2 completo: CER, LLM y auditoría.
2. **¿Hago ya el commit en `P2-Evaluacion`** con `02_evaluacion.ipynb`, la columna de referencias en `documentos.csv`, `extraccion_llm.csv` y `auditoria_llm.csv`? La auditoría (columna `correcta` en `datos/auditoria_llm.csv`) la tienes que llenar tú.

Antes de pedirte el commit, pruebo que el dashboard funcione con los nuevos CSV de evaluación.

La Parte 2 de documentos ya está calculada: con tus referencias, el CER sale de 0,37 para PaddleOCR y 0,54 para EasyOCR. `02_evaluacion.ipynb` se ejecuta completo y sin errores, con el audio marcado como pendiente. Probé `app.py` con los archivos nuevos y no da errores. No he hecho ningún commit.

| Modelo | CER global | Impresos | Fotos | Manuscritos | Segundos por página |
|---|---|---|---|---|---|
| PaddleOCR (línea base, elegido) | **0,37** | **0,11** | **0,56** | **0,23** | 107 |
| EasyOCR | 0,54 | 0,32 | 0,62 | 0,72 | 58 |

- **Notebook:** la sección 8 ya tiene la decisión (PaddleOCR) y la reflexión por tipo de documento. Explica el problema de las dos columnas, la página vecina que se cuela en las fotos y los errores en nombres de los manuscritos. También incluye los errores del LLM que ya detectó la verificación automática.
- **Dashboard:** el CER aparece en las métricas de arriba. Corregí un error: mostraba «Concordancia 0%» mientras la auditoría estaba vacía. Ahora dice «pendiente» hasta que llenes las 20 filas.
- **Pendiente tuyo:**
  - En `datos/auditoria_llm.csv`, llenar `correcta` (sí/no) y `comentario` en las 20 filas.
  - Pasarme las referencias de audio, si llegas.
- **Archivos sin commit:** `02_evaluacion.ipynb`, `documentos.csv` (con la columna de referencias), `extraccion_llm.csv`, `auditoria_llm.csv`, `evaluacion_modelos.csv`, `evaluacion_por_archivo.csv` y el arreglo de `app.py`.

Quedan unos 25 minutos. **¿Hago ya el commit en `P2-Evaluacion` y el push**, para que puedas abrir el PR y desplegar en Streamlit? La auditoría puede ir en un segundo commit justo después.

Whisper `small` y Parakeet ya transcribieron los 13 clips. Volví a correr `clip_020` solo, porque su primera medición (588 s) estaba inflada por la competencia de CPU; ahora da RTF 0,81. En el resto de clips, Parakeet va entre 0,12 y 0,43 y `small` entre 0,09 y 1,41.

Si me pasas tus referencias de audio, el WER sale en un par de minutos; no hay que volver a correr ningún modelo.

Quedan unos 18 minutos. Sigo esperando tu respuesta sobre el commit y el push en `P2-Evaluacion`; no he hecho ninguno. Además, para entregar te falta:
- llenar la auditoría en `datos/auditoria_llm.csv`;
- poner las capturas en `evidencias_ia/`;
- desplegar en Streamlit y pegar el link en el README;
- dejar el comentario en el issue 190.

---

## 21. Estudiante · 25/10/2026 23:45

> ya tengo los audios "C:\Users\agarces\Desktop\Audios.xlsx"

### Claude Code · 25/10/2026 23:45

<details><summary>Herramientas usadas (4)</summary>

- `Bash` Inspect the user's Excel file of audio transcriptions
- `Bash` Load audio references, rerun evaluation, and show WER results
- `Bash` Write audio decision into the notebook's final section
- `Bash` Correct audio comparison claims to match per-clip results

</details>

Son 9 clips, no 10, y ninguno es rural. Los cargo ya con la misma seudonimización y vuelvo a ejecutar el notebook.

Ya está el WER con tus 9 clips. `02_evaluacion.ipynb` se ejecuta completo, sin errores, y la sección 8 tiene la decisión para documentos y audio. No he hecho ningún commit.

| Modelo | WER (9 clips) | RTF (CPU) |
|---|---|---|
| faster-whisper `small` (línea base) | 0,159 | 0,46 |
| faster-whisper `large-v3-turbo` (Parte 1, elegido) | **0,147** | 0,70 |
| Parakeet v3 | 0,202 | **0,22** |

- **Turbo vs. `small`:** turbo tiene el menor error global, pero `small` gana en 4 clips (`clip_002`, `clip_006`, `clip_007` y `clip_008`).
- **Parakeet:** es unas 3 veces más rápido, pero se equivoca más con el español coloquial.
- **Lecturas:** son el mejor caso, con WER entre 0,05 y 0,25.
- **Calle:** `clip_003` ronda 0,8 en los tres modelos porque el ruido tapa casi todo lo que dice el entrevistado.

**Muestra:** son 9 clips, uno menos de los 10 que pide la tarea, y no hay clips rurales. Lo dejé dicho en el notebook.

**Seudonimización:** en tus referencias de `clip_002` y `clip_007` había nombres. Los reemplacé por `[PERSONA_n]` antes de guardarlas en el CSV. Tus originales quedan en `datos/raw/referencias/`, que no se sube a Git.

Quedan unos 12 minutos. **¿Hago ahora el commit y el push en `P2-Evaluacion`?** Entrarían los cambios de `app.py`, `documentos.csv` y `transcripciones.csv`, y además `02_evaluacion.ipynb` y los 4 CSV de evaluación y LLM. Con eso abres el PR, despliegas en Streamlit y comentas en el issue. La auditoría la puedes llenar y subir después en otro commit.

---

## 22. Estudiante · 25/10/2026 23:48

> si hazlo

### Claude Code · 25/10/2026 23:48

<details><summary>Herramientas usadas (1)</summary>

- `Bash` Commit Part 2 files and push the P2-Evaluacion branch

</details>

Hice el commit `420af86` en `P2-Evaluacion` y lo subí a GitHub; la carpeta quedó sin cambios pendientes.

Quedan unos 10 minutos. Te propongo este orden:

1. **Abre el PR y haz el merge:** https://github.com/dgarcesg/diplomado_python_intermedio/compare/main...P2-Evaluacion
2. **Despliega en Streamlit:** entra a https://share.streamlit.io, elige «Create app» y usa estos datos:
   - Repository: `dgarcesg/diplomado_python_intermedio`
   - Branch: `main` (o `P2-Evaluacion` si aún no haces el merge)
   - Main file path: `tarea_2/app.py`
3. **Comenta en el issue 190** con el link de la app y el del repositorio.

Si te sobra tiempo:
- Llena `correcta` y `comentario` en las 20 filas de `datos/auditoria_llm.csv`.
- Pega el link de Streamlit en `README.md`, donde dice «pendiente».
- Sube las capturas a `tarea_2/evidencias_ia/`.

Cuando tengas el link de la app o la auditoría lista, dímelo y hago el commit.

---

## 23. Estudiante · 25/10/2026 23:50

> como hago lo del csv

### Claude Code · 25/10/2026 23:50

<details><summary>Herramientas usadas (1)</summary>

- `Bash` Create an Excel audit sheet on the Desktop

</details>

Lo más rápido es que lo llenes en Excel. Abrir el CSV directo en Excel suele estropear las tildes, así que te armo un Excel con el texto original al lado de cada extracción.

Te dejé el archivo en el Escritorio: **`C:\Users\agarces\Desktop\Auditoria.xlsx`**. Tiene 20 filas: 10 documentos y 10 audios.

**Qué hacer en cada fila:**
1. Lee lo que extrajo el LLM en `campos_json` y compáralo con `texto_original`, que está en la última columna.
2. En la columna **`correcta`** escribe **sí** solo si la extracción cumple los 4 criterios; si falla cualquiera, escribe **no**:
   - `tema` y `resumen` corresponden al texto.
   - `emisor`, `fecha` y `monto` están en el texto, o son `null` si no aparecen.
   - En los audios, el número de hablantes coincide y las citas están copiadas del texto.
   - No hay ningún dato inventado.
3. En **`comentario`**, cuando pongas «no», anota el error en pocas palabras, por ejemplo: «emisor es el destinatario» o «fecha inventada».

La columna `chequeo_automatico` te ayuda a ir rápido. Si dice «NO está» o «NO coincide», lo más probable es que sea «no».

**Los que ya se ven mal:**
- `clip_001`: dice 3 hablantes, pero hay 2.
- `clip_004`: las citas empiezan con «Habla 2:», un prefijo inventado.
- `doc_016`: la fecha no está en el texto.
- `doc_017`: el emisor que puso es el destinatario, y además con el error del OCR («don Preardo Palma»).
- `clip_019`: usa «[PERSONA_2]» como si fuera un hablante.

Guarda el Excel y avísame. Yo lo paso a `datos/auditoria_llm.csv`, vuelvo a ejecutar el conteo de correctas sobre 20 y hago el commit.

---

## 24. Estudiante · 26/10/2026 00:02

> ya actualicé el excel

### Claude Code · 26/10/2026 00:02

<details><summary>Herramientas usadas (4)</summary>

- `Bash` Copy the user's audit marks into the audit CSV
- `Bash` Update LLM conclusion, re-execute notebook and re-test app
- `Bash` Find hardcoded sample sizes in app labels
- `Bash` Fix clip count label, commit audit and push

</details>

Corrijo en el dashboard la etiqueta «WER (10 clips)», porque la muestra tiene 9, y hago el commit.

Tu auditoría ya está en el repositorio: hice el commit `71462d9` y lo subí a `P2-Evaluacion`. Volví a ejecutar el notebook completo sin errores y probé el dashboard, que tampoco da errores.

| Métrica | Valor |
|---|---|
| CER (PaddleOCR, 10 documentos) | 0,373 |
| WER (turbo, 9 clips) | 0,147 |
| Concordancia LLM vs. humano | 55 % (11/20) |
| En documentos | 3/10 correctas |
| En audios | 8/10 correctas |

- **Notebook:** la sección 8 ahora toma tu revisión como criterio final. Los errores del LLM que anotaste quedaron explicados ahí:
  - en las cartas confunde al destinatario con el emisor;
  - toma números de página («24», «57») como fechas;
  - inventa el tema en el clip con ruido;
  - repite el error de la diarización en `clip_008`.
- **Dashboard:** cambié la etiqueta a «WER (9 clips)», porque decía 10.

Ya son más de las 00:00, así que la entrega va con unos minutos de retraso. Lo que falta:
1. Abrir el PR y hacer el merge: https://github.com/dgarcesg/diplomado_python_intermedio/compare/main...P2-Evaluacion
2. Desplegar en https://share.streamlit.io. Usa el repositorio `dgarcesg/diplomado_python_intermedio`, la rama `main` y el archivo principal `tarea_2/app.py`.
3. Comentar en el issue 190 con el link de la app y el del repositorio.

Si me pasas el link de Streamlit, lo pongo en el README. Las capturas para `evidencias_ia/` también puedes subirlas después.

---

## 25. Estudiante · 26/10/2026 00:10

> puedes generar un word de toda markdown con toda nuestra conversación para incluir en evidencias_ia?

### Claude Code · 26/10/2026 00:10

<details><summary>Herramientas usadas (1)</summary>

- `Skill` anthropic-skills:docx

</details>

---

## 26. Estudiante · 26/10/2026 00:10

> puedes generar un markdown con toda nuestra conversación para incluir en evidencias_ia?

### Claude Code · 26/10/2026 00:10

<details><summary>Herramientas usadas (2)</summary>

- `Bash` Inspect the session transcript structure
- `Bash` List user messages in the transcript

</details>
