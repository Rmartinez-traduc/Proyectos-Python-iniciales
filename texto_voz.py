import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import re
import os
import platform
import subprocess

def obtener_texto_desde_url(url):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Error al descargar la página: {e}")
    
    soup = BeautifulSoup(resp.text, "html.parser")

    for script in soup(["script", "style", "noscript"]):
        script.extract()
    
    texto = soup.get_text(separator = " ", strip = True)

    texto = re.sub(r"\s+", " ", texto)

    if not texto:
        raise ValueError("No se pudo extraer texto de la página")
    
    return texto

def texto_a_voz(texto, nombre_archivo = "articulo.mp3", idioma = "es"):
    """
    Convierte texto a voz y guarda en un archivo MP3
    """
    try:
        tts = gTTS(text = texto, lang = idioma)
        tts.save(nombre_archivo)
    except Exception as e:
        raise RuntimeError(f"Error al generar audio: {e}")
    print(f"Audio guardado como '{nombre_archivo}'")

if __name__ == "__main__":
    web_url = "https://www.biografiasyvidas.com/biografia/d/domingo.htm"
    archivo_audio = "audio.mp3"

    try:
        print("Descargando y procesando artículo...")
        texto = obtener_texto_desde_url(web_url)
        texto_a_voz(texto, nombre_archivo=archivo_audio)
    except Exception as e:
        print(f"Error: {e}")
    else:
        # Solo intentar abrir si el archivo fue creado
        if os.path.isfile(archivo_audio):
            sistema = platform.system()
            try:
                if sistema == "Windows":
                    os.startfile(archivo_audio)
                elif sistema == "Darwin":  # macOS
                    subprocess.run(["open", archivo_audio], check=False)
                else:  # Linux y otros
                    subprocess.run(["xdg-open", archivo_audio], check=False)
            except Exception as e:
                print(f"No se pudo abrir el archivo de audio: {e}")
        else:
            print(f"No se encontró el archivo de audio: {archivo_audio}")
