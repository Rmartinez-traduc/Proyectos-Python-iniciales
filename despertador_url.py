from tkinter import messagebox, Label, Tk, ttk
from time import strftime
from pygame import mixer
import webbrowser
import random


ventana = Tk()
ventana.config(bg="pink")
ventana.geometry("500x250")
ventana.title("Alarma y Youtube")
ventana.minsize(width=500, height=250)
mixer.init()

try:
    with open("direcciones.txt", "r") as file:
        direcciones = [line.strip() for line in file.readlines() if line.strip()]
    url = random.choice(direcciones) if direcciones else "https://www.youtube.com/watch?v=pV-aYCjQBaM"
except FileNotFoundError:
    url = "https://www.youtube.com/watch?v=pV-aYCjQBaM"


lista_horas = []
lista_minutos = []
lista_segundos = []

for i in range(0, 24):
    lista_horas.append(i)
for i in range(0, 60):
    lista_minutos.append(i)
for i in range(0, 60):
    lista_segundos.append(i)

texto1 = Label(ventana, text="Hora", fg="magenta", font=("Arial", 12, "bold"))
texto1.grid(row=1, column=0, padx=5, pady=5)
texto2 = Label(ventana, text="Minutos", fg="magenta", font=("Arial", 12, "bold"))
texto2.grid(row=1, column=1, padx=5, pady=5)
texto3 = Label(ventana, text="Segundos", fg="magenta", font=("Arial", 12, "bold"))
texto3.grid(row=1, column=2, padx=5, pady=5)

combobox1 = ttk.Combobox(
    ventana,
    values=lista_horas,
    style="TCombobox",
    justify="center",
    width="12",
    font="Arial",
)
combobox1.grid(row=2, column=0, padx=15, pady=5)
combobox1.current(0)
combobox2 = ttk.Combobox(
    ventana,
    values=lista_minutos,
    style="TCombobox",
    justify="center",
    width="12",
    font="Arial",
)
combobox2.grid(row=2, column=1, padx=15, pady=5)
combobox2.current(0)
combobox3 = ttk.Combobox(
    ventana,
    values=lista_segundos,
    style="TCombobox",
    justify="center",
    width="12",
    font="Arial",
)
combobox3.grid(row=2, column=2, padx=15, pady=5)
combobox3.current(0)
style = ttk.Style()
style.theme_create(
    "combostyle",
    parent="alt",
    settings={
        "TCombobox": {
            "configure": {
                "selectbackground": "red",
                "fieldbackground": "white",
                "background": "grey",
            }
        }
    },
)
style.theme_use("combostyle")

ventana.option_add("*TCombobox*Listbox*Background", "white")
ventana.option_add("*TCombobox*Listbox*Foreground", "pink")
ventana.option_add("*TCombobox*Listbox*selectBackground", "green2")
ventana.option_add("*TCombobox*Listbox*selectForeground", "black")

alarma = Label(ventana, fg="violet", bg="pink", font=("Radioland", 20))
alarma.grid(column=0, row=3, sticky="nsew", ipadx=5, ipady=20)
repetir = Label(ventana, fg="white", bg="pink", text="Repetir", font="Arial")
repetir.grid(column=1, row=3, ipadx=5, ipady=20)
cantidad = ttk.Combobox(
    ventana, values=(1, 2, 3, 4, 5), justify="center", width="8", font="Arial"
)
cantidad.grid(row=3, column=2, padx=5, pady=5)
cantidad.current(0)


def obtener_tiempo():
    x_hora = combobox1.get()
    x_minutos = combobox2.get()
    x_segundos = combobox3.get()
    hora = strftime("%H")
    minutos = strftime("%M")
    segundos = strftime("%S")

    hora_total = hora + " : " + minutos + " : " + segundos
    texto_hora.config(text=hora_total, font=("Radioland", 25))
    hora_alarma = x_hora + " : " + x_minutos + " : " + x_segundos
    if int(segundos) == int(x_segundos):
        webbrowser.open(url)
        try:
            mixer.music.load("alarm_sound.mp3")
            mixer.music.play(loops=int(cantidad.get()))
        except:
            pass
            messagebox.showinfo(message=hora_alarma, title="Alarma")
            if int(segundos) == int(x_segundos):
                mixer.music.load(webbrowser.open(url))
                mixer.music.play(loops=int(cantidad.get()))
                messagebox.showinfo(message=hora_alarma, title="Alarma")
    texto_hora.after(100, obtener_tiempo)


texto_hora = Label(ventana, fg="black", bg="pink")
texto_hora.grid(columnspan=3, row=0, sticky="nsew", ipadx=5, ipady=20)
obtener_tiempo()
ventana.mainloop()
