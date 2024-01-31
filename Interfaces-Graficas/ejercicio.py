# designar alias tk
import tkinter as tk 

def sumar_numeros():
    try:
       num1 = float(entrada_num1.get())
       num2 = float(entrada_num2.get())
       resultado.set(f"Resultado{num1+num2}")
    except ValueError:
       resultado.set("ERROR: Ingrese numeros validos ")
       
# Crear ventana principal
root = tk.Tk()
root.title("Calculadora Simple")

entrada_num1   = tk.Entry(root)
entrada_num1.place(x=10, y=40)
entrada_num2   = tk.Entry(root)
entrada_num2.place(x=10, y=100)
resultado   = tk.StringVar() 

etiqueta_num1 = tk.Label(root, text="Numero 1")
etiqueta_num1.place(x=10, y=10)
etiqueta_num2 = tk.Label(root, text="Numero 2")
etiqueta_num2.place(x=10, y=70)

resultado_f = tk.Label(root, textvariable=resultado)
resultado_f.place(x=70, y=134)

boton_sumar = tk.Button(root, text="SUMAR", command=sumar_numeros)
boton_sumar.place(x=10, y=130)

root.mainloop()

       
