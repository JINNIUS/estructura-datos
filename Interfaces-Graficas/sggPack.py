# el metodo pack()
# organizar los widgets de forma relativa 


import tkinter as tk

root = tk.Tk()
root.title("Ejemplo con pack()")

label = tk.Label(root, text="¡Hola, Tkinter!")
label.pack(side="top", fill="x")

#side recibe como parametros "left, "right", "top", "bottom"

boton = tk.Button(root, text="Clic aqui")
boton.pack(side="left", fill="y")

entrada = tk.Entry(root)
entrada.pack(side="top", fill="x")

root.mainloop()

