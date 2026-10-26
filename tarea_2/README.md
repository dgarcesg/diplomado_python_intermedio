# Tarea 2 – Voces y documentos peruanos: del archivo escaneado al texto buscable

> **Pregunta:** ¿Pueden convertir documentos escaneados y entrevistas en audio en un archivo de texto estructurado y buscable?

Pipeline abierto y local que extrae texto de documentos peruanos con **PaddleOCR**, transcribe entrevistas en español peruano con **faster-whisper** (VAD + diarización), seudonimiza los nombres de las personas entrevistadas y publica los resultados en un dashboard de **Streamlit**.

**Dashboard público:** _(pendiente: enlace de Streamlit Community Cloud)_

## Corpus, fuentes y licencias

Fecha de extracción de ambos corpus: **25/10/2026**. El detalle por archivo (URL, licencia y cómo recuperarlo) está en [`datos/fuentes.csv`](datos/fuentes.csv). Los originales no se versionan (`datos/raw/` está en `.gitignore`); `datos/ejemplos/` contiene una muestra liviana con licencia que permite publicarla.

### A. Documentos (25 imágenes: 8 impresos, 8 fotos, 9 manuscritos)

| Archivos | Fuente | Licencia |
|---|---|---|
| 8 impresos nítidos | Revista *Fénix* n.º 19 (1969), Biblioteca Nacional del Perú: Núñez, E. «Un manuscrito autógrafo y desconocido de Mariano Melgar» ([artículo](https://revistafenix.bnp.gob.pe/index.php/fenix/article/view/515)) | CC BY-NC-ND 4.0 |
| 6 fotos con sombra o inclinación | Fotografías propias de *THĒMIS-Revista de Derecho* n.º 88 y n.º 81 ([revistas.pucp.edu.pe](https://revistas.pucp.edu.pe/index.php/themis)) | CC BY 4.0 |
| 2 fotos con sombra o inclinación | Fotografías propias de *Estudio de anulación de laudos 2022*, Centro de Arbitraje de la Cámara de Comercio de Lima ([PDF](https://www.arbitrajeccl.com.pe/wp-content/uploads/2024/04/Estudio-de-anulacion-de-laudos-2022.pdf)) | Sin licencia declarada: solo texto y metadatos, la imagen no se publica |
| 9 manuscritos | Biblioteca Digital de la Biblioteca Nacional del Perú ([BNP Digital](https://bibliotecadigital.bnp.gob.pe)) | Dominio público |

### B. Audio (20 clips descargados de Wikimedia Commons; 13 en español conservados, 32,3 min)

| Clips | Contenido | Licencia |
|---|---|---|
| `clip_001` … `clip_007` | Entrevistas en la calle en Lima (Fiestas Patrias 2022) | CC BY-SA 4.0 |
| `clip_008` … `clip_011` | Lecturas en voz alta de artículos sobre huacas de Lima | CC BY-SA 4.0 |
| `clip_019`, `clip_020` | Entrevistas rurales sobre plantas medicinales, Shansha (Áncash) | CC BY-SA 4.0 |
| `clip_012` … `clip_018` | Entrevistas rurales **en quechua de Áncash**: descartadas del corpus en español | CC BY-SA 4.0 |

Autores en Commons: JorgeFlores-pe, Rosario MQ, Christopher Bellido, Mayhely Aida, QM Keen, Ariana zafra, Stefanya E. Trujillo Mendoza, Jhon Manayay, Lucía Pérez2 y Figuemijun.

## Metodología

| Paso | Herramienta y configuración |
|---|---|
| OCR | PaddleOCR 3.7 (`lang="es"` → PP-OCRv6 medium), CPU, sin preprocesamiento, mismos parámetros para los tres tipos |
| ASR | faster-whisper *large-v3-turbo* (int8, CPU, `beam_size=5`) con VAD Silero, idioma fijado en español, mediante `voz.py` (Sesión 13) |
| Diarización | Huellas de voz WeSpeaker ResNet34 + *clustering* aglomerativo (coseno, umbral 0,7) en todos los clips |
| Seudonimización | Nombres de personas entrevistadas → `[PERSONA_n]` (comparación difusa con rapidfuzz), más DNI, teléfonos y correos con expresiones regulares; revisión manual de las transcripciones |
| Limpieza | Duplicados por hash SHA-256, documentos ilegibles, audios sin voz y clips fuera de idioma |

## Hallazgos

1. **La calidad del OCR depende del tipo de documento.** La confianza media de PaddleOCR es de 0,99 en impresos y 0,97 en fotos, pero baja a 0,81 en manuscritos, donde aparecen errores como «don Preardo Palma» por «don Ricardo Palma». En las fotos de revistas a dos columnas también se cuelan fragmentos del margen de la página vecina.
2. **Whisper no sirve para el quechua y alucina en audio difícil.** 7 de los 9 clips rurales de Áncash tienen las respuestas en quechua: la detección de Whisper eligió idiomas al azar (suajili, inglés, islandés) y una transcripción de prueba alucinó repeticiones («y y y y…» o frases enteras), así que se descartaron. En la calle, el ruido produce transcripciones pobres: `clip_005` dura 1,7 min y solo da 76 palabras, con frases repetidas («de malos, de malos…»).

## Limitaciones

1. **Solo CPU.** Sin GPU, PaddleOCR tarda de 1 a 4 min por página (oneDNN falla en Windows y hay que desactivarlo) y Whisper turbo corre cerca de tiempo real; por eso los resultados se guardan como respaldo crudo y el dashboard no ejecuta modelos.
2. **Orden de lectura y diarización imperfectos.** PaddleOCR entrega las líneas de arriba hacia abajo, lo que intercala las columnas en páginas a dos columnas. La diarización sin número fijo de hablantes separa a veces una sola voz en dos (`clip_008`, una lectura de una sola persona, sale con 2 hablantes). Además, el corpus de audio en español quedó en 13 clips (32,3 min), por debajo del mínimo de 20 clips, tras descartar los clips en quechua.

## Estructura

```
tarea_2/
├── 01_extraccion.ipynb     # OCR, ASR, seudonimización, limpieza, EDA y exportación
├── 02_evaluacion.ipynb     # CER/WER, LLM y comparación de modelos
├── app.py                  # Dashboard de Streamlit (solo lee CSV)
├── voz.py                  # Módulo de audio de la Sesión 13
├── requirements.txt        # Dependencias de la app
├── evidencias_ia/          # Capturas de la conversación con el asistente de IA
└── datos/
    ├── documentos.csv      # OCR de los 25 documentos
    ├── transcripciones.csv # ASR de los clips en español (seudonimizado)
    ├── fuentes.csv         # Fuente, licencia y acceso de cada archivo
    └── ejemplos/           # Imágenes y audios publicables para el dashboard
```

## Cómo ejecutar

Dashboard en local (solo necesita los CSV de `datos/`):

```bash
cd tarea_2
pip install -r requirements.txt
streamlit run app.py
```

Notebooks: entorno del repositorio del curso (`uv sync --group docai --group audio`), más `easyocr` y `kaleido` (`uv pip install easyocr kaleido`). Descargar los originales según `datos/fuentes.csv` en `datos/raw/documentos/` y `datos/raw/audio/`, y ejecutar `01_extraccion.ipynb` con el kernel del entorno. El OCR y el ASR guardan un respaldo crudo por archivo en `datos/raw/`: si se vuelve a ejecutar, se reutiliza.
