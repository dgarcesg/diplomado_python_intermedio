"""Reel vertical (1080 x 1920) de la Tarea 3: voz clonada, imágenes por escena, subtítulos, música y créditos.

Usa reel.py de la Sesión 15 (voz con Qwen3-TTS y subtítulos con Whisper) y añade una imagen por escena
con un acercamiento lento, la música de fondo y una placa final de créditos.

    # 1. Voz y subtítulos (lento: varios minutos en CPU). Escribe salidas/narracion.wav y narracion.json
    python reel/hacer_reel.py voz --voz audio-modelo-tarea-3.m4a
    # 2. Video (rápido; se puede repetir para ajustar el diseño o la música)
    python reel/hacer_reel.py video --musica reel/musica.mp3 --credito-musica "Título · Autor (Pixabay)"

Corre en el entorno de la Sesión 15 (qwen-tts, faster-whisper, pillow, imageio-ffmpeg).
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw

AQUI = Path(__file__).parent
CURSO = AQUI.parents[2] / "Data-Science-Python" / "sessions" / "15-texto-a-reel"
sys.path.insert(0, str(CURSO))
import reel  # noqa: E402

SALIDAS = AQUI / "salidas"
ANCHO, ALTO, FPS = 1080, 1920, 30
MARGEN = 70
NEGRO, TINTA, TINTA_2, TINTA_3, CAJA, RESALTE = "#000000", "#f0efec", "#c3c2b7", "#898781", "#1c1c1b", "#9ec5f4"
IMG_Y, IMG_ALTO = 360, 960          # franja de la imagen de cada escena
CIERRE = 4.0                         # segundos de la placa final de créditos
FUENTE_DATOS = "INDECI-SINPAD (ene 2016 – may 2024), IGP/ENFEN, IGN"
TTS = "Qwen/Qwen3-TTS-12Hz-0.6B-Base"


def voz(args, guion):
    """Recorta la grabación, narra cada escena, mide el WER y saca los subtítulos.

    El corte va en una pausa al final de una frase: si cae a mitad de palabra, el modelo arrastra ese
    pedazo de palabra al inicio de cada escena (se oía "prama" al empezar cada una).
    """
    SALIDAS.mkdir(exist_ok=True)
    ref = SALIDAS / "voz_referencia.wav"
    audio = reel.cargar_audio(args.voz)
    audio = audio[: int(args.corte * 16000)].copy()
    audio[-1600:] *= np.linspace(1, 0, 1600, dtype=np.float32)   # 0,1 s de salida suave
    sf.write(ref, audio, 16000)
    print(f"Referencia: {len(audio) / 16000:.1f} s", flush=True)

    v = reel.Voz(ref, modelo=args.tts)
    print("Transcripción de la referencia:", v.texto_ref, flush=True)
    n = reel.narrar(v, guion, max_wer=0.2, reintentos=args.reintentos, velocidad=args.velocidad)
    sf.write(SALIDAS / "narracion.wav", n.audio, n.sr)
    n.palabras = subtitulos_por_escena(n.audio, n.sr, n.escenas, guion)
    datos = {"sr": n.sr, "escenas": n.escenas, "palabras": n.palabras,
             "wer": [e.get("wer") for e in guion["escenas"]]}
    (SALIDAS / "narracion.json").write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")
    reel.a_srt(n, SALIDAS / "reel.srt")
    print(f"Narración: {n.duracion:.1f} s · WER por escena: {[round(w, 2) for w in datos['wer']]}")


def subtitulos_por_escena(audio, sr, escenas, guion):
    """Whisper escena por escena: con el audio completo inventaba palabras en los silencios entre escenas."""
    palabras = []
    for (ini, fin), e in zip(escenas, guion["escenas"]):
        a, b = max(0, int((ini - 0.1) * sr)), int((fin + 0.1) * sr)
        segs, _ = reel._whisper().transcribe(reel._a16k(audio[a:b], sr), language="es", word_timestamps=True,
                                             initial_prompt=e["frase"], condition_on_previous_text=False)
        desfase = a / sr
        for w in (w for s in segs for w in s.words if w.word.strip()):
            palabras.append((w.start + desfase, w.end + desfase, _como_en_guion(w.word.strip(), e["frase"])))
    return palabras


def _como_en_guion(palabra, frase):
    """Usa las mayúsculas del guion (Whisper a veces escribe "niño" en vez de "Niño")."""
    limpia = lambda x: x.strip(".,:;¿?¡!").lower()
    for g in frase.split():
        if limpia(g) == limpia(palabra) and g.strip(".,:;¿?¡!") != palabra.strip(".,:;¿?¡!"):
            nucleo = palabra.strip(".,:;¿?¡!")
            return palabra.replace(nucleo, g.strip(".,:;¿?¡!"))
    return palabra


def solo_subtitulos(args, guion):
    datos = json.loads((SALIDAS / "narracion.json").read_text(encoding="utf-8"))
    audio, sr = sf.read(SALIDAS / "narracion.wav", dtype="float32")
    datos["palabras"] = subtitulos_por_escena(audio, sr, datos["escenas"], guion)
    (SALIDAS / "narracion.json").write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")
    n = reel.Narracion(audio, sr, datos["escenas"], datos["palabras"])
    reel.a_srt(n, SALIDAS / "reel.srt")
    print(" ".join(p[2] for p in datos["palabras"]))


# --- Video -------------------------------------------------------------------

def _texto_envuelto(d, xy, texto, fuente, ancho, color, interlineado=1.2):
    x, y = xy
    for linea in reel._envolver(d, texto, fuente, ancho):
        d.text((x, y), linea, font=fuente, fill=color)
        y += int(fuente.size * interlineado)
    return y


def _base(titulo, autor):
    img = Image.new("RGB", (ANCHO, ALTO), NEGRO)
    d = ImageDraw.Draw(img)
    _texto_envuelto(d, (MARGEN, 80), titulo, reel._fuente("PublicSans", 46, 800), ANCHO - 2 * MARGEN, TINTA)
    aviso, f = "VOZ GENERADA CON IA", reel._fuente("PublicSans", 26, 700)
    x1 = MARGEN + d.textlength(aviso, font=f) + 36
    d.rounded_rectangle((MARGEN, 262, x1, 308), radius=23, outline=TINTA_2, width=2)
    d.text((MARGEN + 18, 285), aviso, font=f, fill=TINTA_2, anchor="lm")
    pie = reel._fuente("PublicSans", 27, 500)
    _texto_envuelto(d, (MARGEN, 1822), f"{autor} · Fuente: {FUENTE_DATOS}", pie, ANCHO - 2 * MARGEN, TINTA_3)
    return img


def _capa_escena(e):
    """Cifra grande y etiqueta, debajo de la imagen."""
    capa = Image.new("RGBA", (ANCHO, ALTO), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    y = IMG_Y + IMG_ALTO + 30
    if e.get("cifra"):
        f = reel._ajustar(d, e["cifra"], "Oswald", 700, ANCHO - 2 * MARGEN, 150)
        d.text((MARGEN, y), e["cifra"], font=f, fill=TINTA)
        y += int(f.size * 1.25)
        fe, color = reel._fuente("PublicSans", 42, 600), TINTA_2
    else:
        fe, color = reel._fuente("Oswald", 76, 600), TINTA
    _texto_envuelto(d, (MARGEN, y), e["etiqueta"], fe, ANCHO - 2 * MARGEN, color)
    return capa


def _cierre(titulo, credito_musica, autor):
    img = Image.new("RGB", (ANCHO, ALTO), NEGRO)
    d = ImageDraw.Draw(img)
    y = _texto_envuelto(d, (MARGEN, 420), "Fuentes y créditos", reel._fuente("Oswald", 84, 600), ANCHO, TINTA) + 40
    f = reel._fuente("PublicSans", 36, 500)
    for linea in [
        "Datos: INDECI, SINPAD (emergencias y daños, ene 2016 – may 2024).",
        "Índice Costero El Niño y fechas oficiales: IGP y ENFEN.",
        "Límites distritales: IGN, vía OCHA HDX (CC BY-IGO).",
        f"Música: {credito_musica}.",
        f"Voz generada con IA (Qwen3-TTS) a partir de la voz de {autor}.",
        "Gráficos, mapa y tablero: elaboración propia con Python.",
        "Código y datos: github.com/dgarcesg/diplomado_python_intermedio",
    ]:
        y = _texto_envuelto(d, (MARGEN, y), linea, f, ANCHO - 2 * MARGEN, TINTA_2, 1.3) + 22
    return img


def _imagen(ruta):
    return Image.open(AQUI / ruta).convert("RGB").resize((ANCHO * 2, IMG_ALTO * 2), Image.LANCZOS)


def _zoom(img, avance):
    """Acercamiento lento del 0 al 4 % a lo largo de la escena, anclado arriba para no cortar el título."""
    s = 1 + 0.04 * min(max(avance, 0), 1)
    w, h = img.width / s, img.height / s
    x0, y0 = (img.width - w) / 2, (img.height - h) * 0.2
    return img.resize((ANCHO, IMG_ALTO), Image.BILINEAR, box=(x0, y0, x0 + w, y0 + h))


def video(args, guion):
    datos = json.loads((SALIDAS / "narracion.json").read_text(encoding="utf-8"))
    narr, sr = sf.read(SALIDAS / "narracion.wav", dtype="float32")
    escenas = [tuple(x) for x in datos["escenas"]]
    palabras = [tuple(x) for x in datos["palabras"]]
    fin_voz = len(narr) / sr
    total = fin_voz + CIERRE
    # La voz se rellena con silencio hasta el final de los créditos
    voz_wav = SALIDAS / "voz_completa.wav"
    sf.write(voz_wav, np.concatenate([narr, np.zeros(int(CIERRE * sr), np.float32)]), sr)

    base = _base(guion["titulo"], args.autor)
    capas = [_capa_escena(e) for e in guion["escenas"]]
    imagenes = [_imagen(e["imagen"]) for e in guion["escenas"]]
    cierre = _cierre(guion["titulo"], args.credito_musica, args.autor)
    bloques = reel._bloques(palabras)
    fsub = reel._fuente("PublicSans", 54, 800)
    inicios = [0.0] + [ini - reel.PAUSA for ini, _ in escenas[1:]]
    finales = inicios[1:] + [fin_voz]

    salida = SALIDAS / "reel.mp4"
    filtro = (f"[1:a]aresample=48000,loudnorm=I=-15:TP=-2:LRA=11[v];"
              f"[2:a]aresample=48000,loudnorm=I=-31:TP=-9:LRA=11,volume={args.volumen_musica}dB,"
              f"afade=t=in:d=1.5,afade=t=out:st={total - 2.5:.2f}:d=2.5,atrim=0:{total:.2f}[m];"
              f"[v][m]amix=inputs=2:duration=first:normalize=0[a]")
    cmd = [reel.FFMPEG, "-y", "-v", "error",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{ANCHO}x{ALTO}", "-r", str(FPS), "-i", "-",
           "-i", str(voz_wav), "-stream_loop", "-1", "-i", str(args.musica),
           "-filter_complex", filtro, "-map", "0:v", "-map", "[a]",
           "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "160k", "-t", f"{total:.2f}", "-movflags", "+faststart", str(salida)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for k in range(int(total * FPS)):
        t = k / FPS
        if t >= fin_voz:   # placa final, con entrada suave
            a = min(1.0, (t - fin_voz) / 0.5)
            ultimo = proc_cuadro if a < 1 else None
            cuadro = Image.blend(ultimo, cierre, a) if ultimo is not None else cierre
            proc.stdin.write(cuadro.tobytes())
            continue
        i = max(j for j, ini in enumerate(inicios) if ini <= t)
        avance = (t - inicios[i]) / (finales[i] - inicios[i])
        img = base.copy()
        foto = _zoom(imagenes[i], avance)
        entrada = min(1.0, (t - inicios[i]) / 0.4)
        if i > 0 and entrada < 1:   # fundido con la escena anterior
            foto = Image.blend(_zoom(imagenes[i - 1], 1), foto, entrada)
        img.paste(foto, (0, IMG_Y))
        capa = capas[i]
        if entrada < 1:
            capa = capa.copy()
            capa.putalpha(capa.getchannel("A").point(lambda v: int(v * entrada)))
        img.paste(capa, (0, int(30 * (1 - entrada))), capa)

        d = ImageDraw.Draw(img)
        d.rounded_rectangle((MARGEN, 330, ANCHO - MARGEN, 336), radius=3, fill=CAJA)
        d.rounded_rectangle((MARGEN, 330, MARGEN + (ANCHO - 2 * MARGEN) * t / fin_voz, 336), radius=3, fill=TINTA_2)
        b = next((b for b in bloques if b[0][0] - 0.1 <= t <= b[-1][1] + 0.25), None)
        if b:
            texto = " ".join(p[2] for p in b)
            w = d.textlength(texto, font=fsub)
            x, y = (ANCHO - w) / 2, 1690
            d.rounded_rectangle((x - 30, y - 18, x + w + 30, y + fsub.size + 26), radius=24, fill=CAJA)
            for ini, fin, palabra in b:
                d.text((x, y), palabra, font=fsub, fill=RESALTE if ini <= t <= fin + 0.05 else TINTA)
                x += d.textlength(palabra + " ", font=fsub)
        proc_cuadro = img
        proc.stdin.write(img.tobytes())
    proc.stdin.close()
    proc.wait()
    # Portada: un cuadro de la primera escena
    portada_t = escenas[0][0] + 2.0
    print(f"Video: {salida} · {total:.1f} s (voz {fin_voz:.1f} s + créditos {CIERRE:.0f} s) · portada a los {portada_t:.0f} s")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("paso", choices=["voz", "subtitulos", "video"])
    p.add_argument("--guion", default=str(AQUI / "guion.json"))
    p.add_argument("--voz", help="tu grabación de referencia (paso voz)")
    p.add_argument("--corte", type=float, default=16.5, help="segundos de la grabación que se usan (en una pausa)")
    p.add_argument("--tts", default=TTS)
    p.add_argument("--velocidad", type=float, default=1.0)
    p.add_argument("--reintentos", type=int, default=1)
    p.add_argument("--musica", help="pista de fondo (paso video)")
    p.add_argument("--credito-musica", default="")
    p.add_argument("--volumen-musica", type=float, default=0.0, help="dB extra sobre -31 LUFS")
    p.add_argument("--autor", default="Adriana Garcés")
    args = p.parse_args()
    guion = json.loads(Path(args.guion).read_text(encoding="utf-8"))
    {"voz": voz, "subtitulos": solo_subtitulos, "video": video}[args.paso](args, guion)
