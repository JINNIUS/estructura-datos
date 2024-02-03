import tkinter as tk
from tkinter import messagebox

def CURP():
    Nombre = nombre.get().upper()
    Apellido_paterno = apellido_paterno.get().upper()
    Apellido_materno = apellido_materno.get().upper()
    Fecha = fecha.get()

    curp = Apellido_paterno[:2] + Apellido_materno[0] + Nombre[0] + Fecha[2:4] + Fecha[5:7] + Fecha[8:]

    resultado.config(text=f"SU CURP ES: {curp}")

ventana = tk.Tk()
ventana.title("CURP")

tk.Label(ventana, text="NOMBRE:").place(x=10, y=30)
nombre = tk.Entry(ventana)
nombre.place(x=150, y=30)

tk.Label(ventana, text="APELLIDO PATERNO:").place(x=10, y=60)
apellido_paterno = tk.Entry(ventana)
apellido_paterno.place(x=150, y=60)

tk.Label(ventana, text="APELLIDO MATERNO:").place(x=10, y=90)
apellido_materno = tk.Entry(ventana)
apellido_materno.place(x=150, y=90)

tk.Label(ventana, text="FECHA DE NACIMIENTO:").place(x=10, y=120)
fecha = tk.Entry(ventana)
fecha.place(x=150, y=120)

finaliza_curp = tk.Button(ventana, text="IMPRIMIR CURP", command=CURP)
finaliza_curp.place(x=164, y=150)

resultado = tk.Label(ventana, text="")
resultado.place(x=148, y=190)

ventana.minsize(300, 200)

ventana.mainloop()