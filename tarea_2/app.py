"""Dashboard de la Tarea 2: voces y documentos peruanos, del archivo escaneado al texto buscable.

Solo lee los CSV que generan los notebooks (no corre OCR, ASR ni LLM en vivo):

    datos/documentos.csv           OCR de los documentos            (01_extraccion.ipynb)
    datos/transcripciones.csv      ASR de los clips de audio        (01_extraccion.ipynb)
    datos/fuentes.csv              fuente, licencia y acceso        (01_extraccion.ipynb)
    datos/extraccion_llm.csv       campos extraídos por el LLM      (02_evaluacion.ipynb, opcional)
    datos/evaluacion_modelos.csv   CER/WER por modelo               (02_evaluacion.ipynb, opcional)
    datos/evaluacion_por_archivo.csv  error y texto por archivo y modelo (opcional)
    datos/auditoria_llm.csv        auditoría humana de 20 extracciones (opcional)
    datos/ejemplos/                imágenes (.jpg) y audios (.mp3) publicables

Ejecutar en local:  streamlit run app.py
"""

import json
import unicodedata
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATOS = Path(__file__).parent / "datos"
EJEMPLOS = DATOS / "ejemplos"
PREGUNTA = ("¿Pueden convertir documentos escaneados y entrevistas en audio "
            "en un archivo de texto estructurado y buscable?")
COLORES_TIPO = {"impreso": "#2a6f97", "foto": "#e09f3e", "manuscrito": "#9e2a2b"}
COLORES_CONDICION = {"calle": "#6a994e", "lectura": "#5e548e", "rural": "#bc6c25"}

st.set_page_config(page_title="Voces y documentos peruanos", page_icon="🎙️", layout="wide")


@st.cache_data
def leer(nombre):
    "Lee un CSV de datos/ o devuelve None si todavía no existe (resultados de la Parte 2)."
    ruta = DATOS / nombre
    return pd.read_csv(ruta, keep_default_na=False, na_values=[""]) if ruta.exists() else None


def sin_tildes(texto):
    "Minúsculas y sin tildes, para que la búsqueda encuentre 'peru' en 'Perú'."
    texto = unicodedata.normalize("NFD", str(texto).lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def coincide(serie, consulta):
    return serie.fillna("").map(sin_tildes).str.contains(sin_tildes(consulta), regex=False)


def campos_llm(id_registro):
    "Campos JSON que el LLM extrajo para un registro, o None."
    if llm is None:
        return None
    fila = llm[llm.id == id_registro]
    if fila.empty:
        return None
    try:
        return json.loads(fila.iloc[0].campos_json)
    except (TypeError, ValueError):
        return {"campos_json": fila.iloc[0].campos_json}


def error_por_archivo(id_registro):
    "Filas de evaluación (modelo, error, texto) de un archivo de la muestra, o un DataFrame vacío."
    if por_archivo is None:
        return pd.DataFrame()
    return por_archivo[por_archivo.id == id_registro]


def metrica_modelo(modalidad, metrica):
    "Valor de la métrica del modelo elegido (o del mejor) para una modalidad; None si no hay evaluación."
    if evaluacion is None:
        return None, None
    filas = evaluacion[(evaluacion.modalidad == modalidad) & (evaluacion.metrica == metrica)]
    if filas.empty:
        return None, None
    if "seleccionado" in filas and filas.seleccionado.astype(str).str.lower().eq("true").any():
        fila = filas[filas.seleccionado.astype(str).str.lower().eq("true")].iloc[0]
    else:
        fila = filas.loc[filas.valor.idxmin()]
    return fila.valor, fila.modelo


docs = leer("documentos.csv")
asr = leer("transcripciones.csv")
fuentes = leer("fuentes.csv")
llm = leer("extraccion_llm.csv")
evaluacion = leer("evaluacion_modelos.csv")
por_archivo = leer("evaluacion_por_archivo.csv")
auditoria = leer("auditoria_llm.csv")

if docs is None or asr is None:
    st.error("Faltan datos/documentos.csv o datos/transcripciones.csv: ejecute primero 01_extraccion.ipynb.")
    st.stop()

# ───────────────────────────────────────────────────────── encabezado
st.markdown(f"<h1 style='text-align:center'>{PREGUNTA}</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center'>Pipeline abierto y local: <b>PaddleOCR</b> para documentos peruanos "
    "(impresos, fotos y manuscritos), <b>faster-whisper</b> con VAD y diarización para entrevistas en "
    "español peruano, seudonimización de nombres y extracción estructurada con un LLM. "
    "Los resultados se calcularon en los notebooks; esta app solo los explora.</p>",
    unsafe_allow_html=True,
)

# ───────────────────────────────────────────────────────── filtros
with st.sidebar:
    st.header("Filtros")
    consulta = st.text_input("Buscar en los textos OCR y ASR", placeholder="p. ej. Melgar, arbitraje, huaca")
    tipos = st.multiselect("Tipo de documento", list(COLORES_TIPO), default=list(COLORES_TIPO))
    condiciones = st.multiselect("Condición del audio", sorted(asr.condicion.unique()),
                                 default=sorted(asr.condicion.unique()))
    dur_min, dur_max = float(asr.duracion_seg.min()), float(asr.duracion_seg.max())
    duracion = st.slider("Duración del clip (s)", dur_min, dur_max, (dur_min, dur_max))
    modelos_disponibles = sorted(set(docs.modelo_ocr) | set(asr.modelo_asr)
                                 | (set(evaluacion.modelo) if evaluacion is not None else set()))
    modelos = st.multiselect("Modelo", modelos_disponibles, default=modelos_disponibles)

docs_f = docs[docs.tipo.isin(tipos) & docs.modelo_ocr.isin(modelos)]
asr_f = asr[asr.condicion.isin(condiciones) & asr.duracion_seg.between(*duracion) & asr.modelo_asr.isin(modelos)]
if consulta:
    docs_f = docs_f[coincide(docs_f.texto_ocr, consulta)]
    asr_f = asr_f[coincide(asr_f.texto_asr, consulta)]
    st.sidebar.caption(f"«{consulta}» aparece en {len(docs_f)} documentos y {len(asr_f)} clips.")

# ───────────────────────────────────────────────────────── indicadores
cer, modelo_cer = metrica_modelo("documento", "CER")
wer, modelo_wer = metrica_modelo("audio", "WER")
revisada = auditoria is not None and auditoria.correcta.fillna("").astype(str).str.strip().ne("").all()
if revisada and len(auditoria):
    correctas = auditoria.correcta.astype(str).str.strip().str.lower().isin(["true", "1", "si", "sí"]).sum()
    concordancia, detalle_auditoria = f"{correctas / len(auditoria):.0%}", f"{correctas}/{len(auditoria)} correctas"
else:
    concordancia, detalle_auditoria = "pendiente", "auditoría de la Parte 2"

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Documentos procesados", len(docs_f), help=f"{len(docs)} en total")
c2.metric("Minutos de audio transcritos", f"{asr_f.duracion_seg.sum() / 60:.1f}",
          help=f"{asr.duracion_seg.sum() / 60:.1f} min en {len(asr)} clips en total")
c3.metric("CER (10 documentos)", "pendiente" if cer is None else f"{cer:.3f}", help=modelo_cer)
c4.metric("WER (9 clips)", "pendiente" if wer is None else f"{wer:.3f}", help=modelo_wer)
c5.metric("Concordancia LLM vs. humano", concordancia, help=detalle_auditoria)

tab_resultados, tab_docs, tab_audios, tab_fuentes = st.tabs(
    ["📊 Resultados", "📄 Explorador de documentos", "🎙️ Explorador de audios", "📚 Fuentes y licencias"])

# ───────────────────────────────────────────────────────── resultados
with tab_resultados:
    izquierda, derecha = st.columns(2)
    with izquierda:
        por_tipo = (docs_f.groupby("tipo").agg(documentos=("id", "size"), confianza=("confianza_media", "mean"))
                    .reindex([t for t in COLORES_TIPO if t in tipos]).dropna().reset_index())
        fig = px.bar(por_tipo, x="tipo", y="documentos", color="tipo", color_discrete_map=COLORES_TIPO,
                     text=por_tipo.confianza.map(lambda c: f"confianza {c:.2f}"),
                     labels={"tipo": "Tipo", "documentos": "Documentos"},
                     title="La confianza del OCR baja de los impresos a los manuscritos")
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, width="stretch")
    with derecha:
        clips = asr_f.assign(minutos=asr_f.duracion_seg / 60).sort_values("minutos", ascending=False)
        fig = px.bar(clips, x="id", y="minutos", color="condicion", color_discrete_map=COLORES_CONDICION,
                     hover_data=["n_hablantes", "n_palabras"],
                     labels={"id": "Clip", "minutos": "Minutos", "condicion": "Condición"},
                     title="Duración de cada clip transcrito, por condición de grabación")
        st.plotly_chart(fig, width="stretch")

    if evaluacion is not None:
        eval_f = evaluacion[evaluacion.modelo.isin(modelos)]
        fig = px.bar(eval_f, x="modelo", y="valor", color="modalidad", facet_col="metrica", text_auto=".3f",
                     labels={"valor": "Error (menor es mejor)", "modelo": "Modelo"},
                     title="Error de cada modelo sobre las mismas muestras de 10 documentos y 9 clips")
        fig.update_xaxes(matches=None)
        st.plotly_chart(fig, width="stretch")
    else:
        st.info("La comparación CER/WER entre modelos aparecerá cuando 02_evaluacion.ipynb genere "
                "datos/evaluacion_modelos.csv.")

    st.subheader("Registros filtrados")
    tabla = pd.concat([
        docs_f.assign(modalidad="documento", grupo=docs_f.tipo, modelo=docs_f.modelo_ocr, texto=docs_f.texto_ocr),
        asr_f.assign(modalidad="audio", grupo=asr_f.condicion, modelo=asr_f.modelo_asr, texto=asr_f.texto_asr),
    ])[["modalidad", "id", "grupo", "modelo", "fuente", "texto"]]
    st.dataframe(tabla, width="stretch", hide_index=True,
                 column_config={"texto": st.column_config.TextColumn("texto (revisado y seudonimizado)", width="large")})
    st.download_button("⬇️ Descargar CSV filtrado", tabla.to_csv(index=False).encode("utf-8"),
                       file_name="registros_filtrados.csv", mime="text/csv")

# ───────────────────────────────────────────────────────── explorador de documentos
with tab_docs:
    opciones = docs_f if len(docs_f) else docs
    if not len(docs_f):
        st.warning("Ningún documento cumple los filtros; se muestran todos.")
    elegido = st.selectbox("Documento", opciones.id,
                           format_func=lambda i: f"{i} · {docs.set_index('id').tipo[i]}")
    doc = docs.set_index("id").loc[elegido]
    imagen = EJEMPLOS / f"{elegido}.jpg"
    izquierda, derecha = st.columns([2, 3])
    with izquierda:
        if str(doc.publicar_imagen).lower() == "true" and imagen.exists():
            st.image(str(imagen), caption=doc.fuente, width="stretch")
        elif str(doc.publicar_imagen).lower() != "true":
            st.info("La licencia de este documento no permite publicar la imagen: se muestran solo el texto y los metadatos.")
        else:
            st.info("La imagen no está en la muestra publicada (datos/ejemplos/); se muestran el texto y los metadatos.")
        st.caption(f"**Fuente:** {doc.fuente}")
        st.caption(f"**Modelo:** {doc.modelo_ocr} · {doc.n_lineas} líneas · confianza media {doc.confianza_media:.2f}")
    with derecha:
        st.markdown("**Texto OCR**")
        st.text_area("Texto OCR", doc.texto_ocr, height=320, label_visibility="collapsed")
        if pd.notna(doc.texto_referencia) and str(doc.texto_referencia).strip():
            st.markdown("**Transcripción manual de referencia**")
            st.text_area("Referencia", doc.texto_referencia, height=160, label_visibility="collapsed")
        evaluado = error_por_archivo(elegido)
        if len(evaluado):
            st.markdown("**CER de cada modelo en este documento**")
            st.dataframe(evaluado[["modelo", "error"]], hide_index=True, width="stretch")
    st.markdown("**Campos extraídos por el LLM**")
    campos = campos_llm(elegido)
    if campos:
        st.json(campos)
    else:
        st.caption("Pendiente: datos/extraccion_llm.csv (Parte 2).")

# ───────────────────────────────────────────────────────── explorador de audios
with tab_audios:
    opciones = asr_f if len(asr_f) else asr
    if not len(asr_f):
        st.warning("Ningún clip cumple los filtros; se muestran todos.")
    elegido = st.selectbox("Clip", opciones.id,
                           format_func=lambda i: f"{i} · {asr.set_index('id').condicion[i]}")
    clip = asr.set_index("id").loc[elegido]
    audio = EJEMPLOS / f"{elegido}.mp3"
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Duración", f"{clip.duracion_seg / 60:.1f} min")
    c2.metric("Hablantes detectados", int(clip.n_hablantes))
    c3.metric("Palabras", int(clip.n_palabras))
    c4.metric("Factor de tiempo real", f"{clip.rtf:.2f}")
    if audio.exists():
        st.audio(str(audio))
    else:
        st.info("Este clip no está en la muestra de audio publicada: se muestran la transcripción y los metadatos.")
    st.caption(f"**Fuente:** {clip.fuente} · **Modelo:** {clip.modelo_asr}")

    st.markdown("**Transcripción por turnos de habla**")
    for turno in str(clip.texto_asr).split("\n"):
        marca, _, texto = turno.partition("] ")
        st.markdown(f"**{marca.strip('[')}**: {texto}" if texto else turno)

    evaluado = error_por_archivo(elegido)
    if len(evaluado):
        st.markdown("**Comparación de modelos en este clip**")
        columnas = st.columns(len(evaluado))
        for col, fila in zip(columnas, evaluado.itertuples()):
            col.metric(fila.modelo, f"WER {fila.error:.3f}")
            if "texto" in evaluado:
                col.text_area(fila.modelo, fila.texto, height=220, label_visibility="collapsed")
    st.markdown("**Campos extraídos por el LLM**")
    campos = campos_llm(elegido)
    if campos:
        st.json(campos)
    else:
        st.caption("Pendiente: datos/extraccion_llm.csv (Parte 2).")

# ───────────────────────────────────────────────────────── fuentes
with tab_fuentes:
    st.markdown("Cada archivo con su fuente, licencia e instrucciones de recuperación. Los originales no se "
                "publican en el repositorio; los descartados (duplicados, ilegibles o fuera de idioma) se listan "
                "igual para que el corpus sea reproducible.")
    if fuentes is not None:
        st.dataframe(fuentes, width="stretch", hide_index=True,
                     column_config={"fuente_url": st.column_config.LinkColumn("fuente_url")})
