import tkinter as tk
from tkinter import messagebox
import time
import random

# Lista de oraciones para practicar
oraciones = [
    "La suave brisa, la risa de las flores. Es primavera.",
    "¡Cómo me gustaría lavar el polvo del mundo con esas gotas de rocío!",
    "Perdido en el bambú, pero cuando sale la luna, mi hogar.",
    "Mis ojos brillan de tanto contemplarte, flor de cerezo.",
    "Bellos copos de nieve, ninguno cae fuera de ninguna parte."
]

class EscrituraVelozApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Escritura Veloz")
        self.root.geometry("700x300")
        self.root.resizable(False, False)

        self.inicio_tiempo = None
        self.texto_objetivo = tk.StringVar()
        self.texto_usuario = tk.StringVar()

        # Etiqueta de instrucción
        tk.Label(root, text = "Escribe la siguiente oración exactamente como aparece:",
                    font = ("Arial", 14)).pack(pady = 10)

        # Oración a escribir
        self.label_oracion = tk.Label(root, text = "", wraplength = 650,
                                      font = ("Arial", 16), fg = "blue")
        self.label_oracion.pack(pady = 10)

        # Campo de entrada
        self.entry = tk.Entry(root, textvariable = self.texto_usuario,
                              font = ("Arial", 14), width = 60)
        self.entry.pack(pady = 10)
        self.entry.bind("<KeyPress>", self.iniciar_tiempo)

        # Botones
        tk.Button(root, text = "Iniciar nueva oración", command = self.nueva_oracion,
                  font = ("Arial", 12)).pack(pady = 5)
        tk.Button(root, text = "Evaluar", command = self.evaluar,
                  font = ("Arial", 12)).pack(pady = 5)
        
        self.nueva_oracion()

    def nueva_oracion(self):
        """Genera una nueva oración aleatoria y reinicia el test."""
        self.texto_objetivo.set(random.choice(oraciones))
        self.label_oracion.config(text = self.texto_objetivo.get())
        self.texto_usuario.set("")
        self.inicio_tiempo = None
        self.entry.config(state = "normal")
        self.entry.focus()
    
    def iniciar_tiempo(self, event=None):
        """Inicia el cronómetro al primer carácter escrito."""
        if self.inicio_tiempo is None:
            self.inicio_tiempo = time.time()

    def evaluar(self):
        """Calcula velocidad y precisión."""
        if self.inicio_tiempo is None:
            messagebox.showwarning("Aviso", "Debes escribir algo antes de evaluar.")
            return
        
        tiempo_total = time.time() - self.inicio_tiempo
        texto_usuario = self.texto_usuario.get()
        texto_objetivo = self.texto_objetivo.get()

        # Calcular precisión
        caracteres_correctos = sum(1 for i, c in enumerate(texto_usuario)
                                   if i < len(texto_objetivo) and c ==
texto_objetivo[i])
        precision = (caracteres_correctos / len(texto_objetivo)) * 100

        # Calcular velocidad (palabras por minuto)
        palabras = len(texto_usuario.split())
        minutos = tiempo_total / 60
        wpm = palabras / minutos if minutos > 0 else 0

        # Mostrar resultados
        messagebox.showinfo(
            "Resultados",
            f"Tiempo: {tiempo_total:.2f} segundos\n"
            f"Velocidad: {wpm:.2f} palabras/minuto\n"
            f"Precisión: {precision:.2f}%"
        )

        self.entry.config(state = "disabled")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = EscrituraVelozApp(root)
    root.mainloop()