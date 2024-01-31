# El metodo place()
"""
El metodo posiciona los widgets de forma
absoluta en la ventana.

"""
import tkinter as tk

root = tk.Tk()
root.title("Ejemplo con place()")

label = tk.Label(root, text="¡Hola, Tkinter!")
label.place(x=10, y=10)

boton = tk.Button(root, text="Clic aqui")
boton.place(x=10, y=40)

entrada =tk.Entry(root)
entrada.place(x=10, y=70)

root.mainloop()