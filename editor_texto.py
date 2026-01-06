import tkinter as tk
from tkinter import filedialog, messagebox
import os

class EditorTexto:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de texto simple")
        self.root.geometry("800x600")

        self.archivo_actual = None

        # Área de texto con scroll
        self.texto = tk.Text(root, wrap = "word", undo = True)
        self.texto.pack(fill = "both", expand = True, side = "left")

        # Menú
        self.menu = tk.Menu(root)
        root.config(menu = self.menu)

        menu_archivo = tk.Menu(self.menu, tearoff = 0)
        menu_archivo.add_command(label = "Nuevo", command = self.nuevo_archivo)
        menu_archivo.add_command(label = "Abrir", command = self.abrir_archivo)
        menu_archivo.add_command(label = "Guardar",
command = self.guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label = "Salir", command = self.salir)

        self.menu.add_cascade(label = "Archivo", menu = menu_archivo)

        menu_editar = tk.Menu(self.menu, tearoff = 0)
        menu_editar.add_command(label = "Deshacer",
command = self.texto.edit_undo)
        menu_editar.add_command(label = "Rehacer",
command = self.texto.edit_redo)
        menu_editar.add_separator()
        menu_editar.add_command(label = "Cortar", command = lambda:
self.root.focus_get().event_generate("<<Cut>>"))
        menu_editar.add_command(label = "Copiar", command = lambda:
self.root.focus_get().event_generate("<<Copy>>"))
        menu_editar.add_command(label = "Pegar", command = lambda:
self.root.focus_get().event_generate("<<Paste>>"))
        
        self.menu.add_cascade(label = "Editar", menu = menu_editar)
    
    def nuevo_archivo(self):
        if self.confirmar_cambios():
            self.texto.delete(1.0, tk.END)
            self.archivo_actual = None
            self.root.title("Editor de texto - Nuevo")
    
    def abrir_archivo(self):
        if not self.confirmar_cambios():
            return
        ruta = filedialog.askopenfilename(filetypes = [("Archivos de texto", 
"*.txt"), ("Todos los archivos", "*.*")])
        if ruta:
            try:
                with open(ruta, "r", encoding = "utf-8") as f:
                    contenido = f.read()
                self.texto.delete(1.0, tk.END)
                self.texto.insert(tk.END, contenido)
                self.archivo_actual = ruta
                self.root.title(f"Editor de texto - {os.path.basename(ruta)}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo: \n{e}")

    def guardar_archivo(self):
        if self.archivo_actual:
            try:
                with open(self.archivo_actual, "w", encoding = "utf-8") as f:
                    f.write(self.texto.get(1.0, tk.END).rstrip())
                messagebox.showinfo("Guardado", "Archivo guardado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: \n{e}")
        else:
            self.guardar_como()
    
    def guardar_como(self):
        ruta = filedialog.asksaveasfilename(defaultextension = ".txt", filetypes = [("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if ruta:
            try:
                with open(ruta, "w", encoding = "utf-8") as f:
                    f.write(self.texto.get(1.0, tk.END).rstrip())
                self.archivo_actual = ruta
                self.root.title(f"Editor de texto - {os.path.basename(ruta)}")
                messagebox.showinfo("Guardado", "Archivo guardado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: \n{e}")

    def confirmar_cambios(self):
        if self.texto.edit_modified():
            respuesta = messagebox.askyesnocancel("Confirmar", "¿Desea guardar los cambios?")
            if respuesta: # Sí
                self.guardar_archivo()
                return True
            elif respuesta is None: # Cancelar
                return False
        return True
    
    def salir(self):
        if self.confirmar_cambios():
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = EditorTexto(root)
    root.mainloop()
    

