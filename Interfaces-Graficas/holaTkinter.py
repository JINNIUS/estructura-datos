import tkinter as tk

def boton_clic():
    print("Boton clickeado")
def boton_texto():
    print("Boton clickeado")

# creando ventana principal
root = tk.Tk()
root.title("Mi Aplicacion Tkinter")

#Añadir widgets a la ventana

boton = tk.Button(root, text="Clic aqui", command=boton_clic)
boton.pack()

#texto = label
boton = tk.Button(root, text="Mostrar Texto", command=boton_texto)
boton.pack()

entrada = tk.Entry(root)
entrada.pack()

# Ejecutar el bucle principal
root.mainloop()