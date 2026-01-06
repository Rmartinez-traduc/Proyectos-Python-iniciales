import tkinter as tk
from langdetect import detect

# Inicializar la ventana principal
ventana = tk.Tk()
ventana.title("Detector de idioma")
ventana.geometry("300x200")

# Crear una entrada de texto
entrada = tk.Entry(ventana)
entrada.pack(pady=10)

# Crear una etiqueta para mostrar el resultado
resultado_etiqueta = tk.Label(ventana, text = "")
resultado_etiqueta.pack(pady = 10)

# Crear la función para detectar el idioma
def detectar_idioma():
    texto = entrada.get()
    if not texto.strip():
        resultado_etiqueta.config(text = "Por favor ingresa algún texto")
        return
    try:
        idioma = detect(texto)
    except Exception:
        idioma = "No se pudo detectar el idioma"
    
    resultado_etiqueta.config(text = idioma)

# Añadir un botón para iniciar la detección
boton_detectar = tk.Button(ventana, text = "Detectar idioma", command = detectar_idioma)
boton_detectar.pack(pady = 10)

ventana.mainloop()