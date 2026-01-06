import tkinter as tk
from tkinter import messagebox
from urllib import request, error

def check_website():
    url = url_entry.get()
    if not url.startswith("http"):
        url = "https://" + url  # Asegurarse de que la URL tenga el esquema HTTP/HTTPS

    try:
        response = request.urlopen(url)
        if response.status == 200:
            messagebox.showinfo("Resultado", f"El sitio web '{url}' está disponible.")
        else:
            messagebox.showwarning("Resultado", f"El sitio web '{url}' devolvió el código {response.status}.")

    except error.URLError as e:
        messagebox.showerror("Error", f"No se pudo conectar a '{url}'. \nRazón: {e.reason}")

# Crear la ventana principal
root = tk.Tk()
root.title("Comprobador de conectividad de sitios web")

# Etiqueta y entrada para la URL
tk.Label(root, text = "Introduce la URL del sitio web:").pack(pady = 5)
url_entry = tk.Entry(root, width = 40)
url_entry.pack(pady = 5)

# Botón para comprobar la conectividad
tk.Button(root, text="Comprobar", command=check_website).pack(pady = 5)

# Iniciar el bucle de la interfaz gráfica
root.mainloop()
