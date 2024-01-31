# conociendo que hay diferentes SGG
# en una interfaz grafica pueden coexistir
# las opciones : pack(), place
# y grid por su naturaleza no

import tkinter as tk
root = tk.Tk()
root.title("Ejemplo combinando metodos")

root = tk.Tk()
root.title("Ejemplo con place()")

label = tk.Label(root, text="¡Hola, Tkinter!")
label.pack(side="top", fill="x")

boton = tk.Button(root, text="Clic aqui")
boton.grid(row=1, column=0, sticky="nsew")

boton = tk.Button(root, text="Clic aqui")
boton.grid(row=1, column=1, sticky="nsew")

entrada =tk.Entry(root)
entrada.place(x=10, y=70)

root.mainloop()