import tkinter as tk
from tkinter import messagebox
class EditorTextoFrame(tk.Frame):
    def __init__(self, master= None):
        super().__init__(master)
        self.master = master
        self.historial = []

        self.text_label = tk.Label(self, text="Texto Actual")
        self.text_label.pack()

        self.texto_var = tk.StringVar()

        self.texto_actual = tk.Label(self, textvariable=self.texto_var)
        self.texto_actual.pack()
        
        self.entry_texto = tk.Entry(self)
        self.entry_texto.pack()
     
        self.boton_agregar = tk.Button(self, text="Agregar Texto", command=self.agregar_texto)
        self.boton_agregar.pack()

        self.boton_deshacer = tk.Button(self, text="Deshacer", command=self.deshacer)
        self.boton_agregar.pack()

        self.boton_deshacer.pack()

        self.pack()

    def agregar_texto(self):
        texto_nuevo = self.entry_texto.get()
        self.historial.append(texto_nuevo)
        self.entry_texto.delete(0, tk.END)
        self.actualizar_texto()
    
    def deshacer(self):
        if self.historial:
            self.historial.pop()
            self.actualizar_texto()
        else:
            messagebox.showwarning("Mensaje", "La pila esta vacia")

    def actualizar_texto(self):
        texto_actual = "".join(self.historial)
        self.texto_var.set(texto_actual)

root = tk.Tk()
editor_frame = EditorTextoFrame(master=root)
editor_frame.mainloop()