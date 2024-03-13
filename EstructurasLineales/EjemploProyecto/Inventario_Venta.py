import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class NodoArticulo():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.siguiente = None


class ListaEnlazada():
    def __init__(self):
        self.cabeza = None

    def agregar_al_principio(self, nombre, precio):
        nuevo_nodo = NodoArticulo(nombre, precio)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar(self, nombre):
        actual = self.cabeza
        previo = None
        while actual and actual.nombre != nombre:
            previo = actual
            actual = actual.siguiente
        if actual:
            if previo:
                previo.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.nombre, actual.precio)
            actual = actual.siguiente

    def obtener_lista(self):
        lista = []
        actual = self.cabeza
        while actual:
            lista.append((actual.nombre, actual.precio))
            actual = actual.siguiente
        return lista


class ColaPedidos():
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

#Hay que checar la clase
class PilaVentas():
    def __init__(self):
        self.items = []
        self.precio2 = []
        self.pres= []

    def esta_vacia(self):
        return len(self.precio2) == 0

    def apilar(self, items):
        self.items.append(items)
       # self.precio2.append(precio2)
        
    def apilar2(self, precio2, pres):
        self.precio2.append((precio2, pres))

    def desapilar(self):
        if not self.esta_vacia():
            return self.precio2.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]


class TiendaApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplicación de Inventario-Ventas")
        style = ttk.Style()
        style.configure("TFrame", background="#1BB2F6")
        style.configure("TNotebook", background="#79E1FA", tabposition='wn')

        self.tabControl = ttk.Notebook(self)
        style = ttk.Style()
        style.configure("TNotebook.Tab", background='blue', foreground='red')
        style.map("TNotebook.Tab", background=[('selected', 'blue')])
        self.tabControl = ttk.Notebook(self, style='TNotebook')

        self.tabArticulos = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabArticulos, text="Artículos")

        self.tabPedidos = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabPedidos, text="Pedidos")

        self.tabVentas = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabVentas, text="Ventas")

        self.tabControl.pack(expand=1, fill="both")

        self.lista_articulos = ListaEnlazada()
        self.cola_pedidos = ColaPedidos()
        self.pila_ventas = PilaVentas()

        self.create_articulos_widgets()
        self.create_pedidos_widgets()
        self.create_ventas_widgets()

    def create_articulos_widgets(self):
        frame_articulos = tk.LabelFrame(self.tabArticulos, text="Gestión de Artículos", background='#67D4FF')
        frame_articulos.pack(padx=10, pady=10, fill="both", expand=True)

        lbl_nombre = tk.Label(frame_articulos, text="Nombre:", bg="#63FFE2")
        lbl_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(frame_articulos)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        lbl_precio = tk.Label(frame_articulos, text="Precio:", bg="#63FFE2")
        lbl_precio.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_precio = tk.Entry(frame_articulos)
        self.entry_precio.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        btn_agregar = tk.Button(frame_articulos, text="Agregar Artículo", command=self.agregar_articulo, bg="#63FFE2")
        btn_agregar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        btn_eliminar = tk.Button(frame_articulos, text="Eliminar Artículo", command=self.eliminar_articulo, bg="#63FFE2")
        btn_eliminar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.listbox_articulos = tk.Listbox(frame_articulos)
        self.listbox_articulos.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def agregar_articulo(self):
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        if nombre and precio:
            self.lista_articulos.agregar_al_principio(nombre.upper(), precio)
            self.actualizar_lista_articulos()
            self.entry_nombre.delete(0, tk.END)
            self.entry_precio.delete(0, tk.END)
            messagebox.showinfo("Información", "Artículo agregado correctamente.")
        else:
            messagebox.showerror("Error", "Por favor ingresa el nombre y precio del artículo.")

    def eliminar_articulo(self):
        seleccionado = self.listbox_articulos.curselection()
        if seleccionado:
            indice = seleccionado[0]
            nombre = self.listbox_articulos.get(indice).split()[0]  # Obtener el nombre del artículo
            self.lista_articulos.eliminar(nombre)
            self.actualizar_lista_articulos()
            messagebox.showinfo("Información", "Artículo eliminado correctamente.")
        else:
            messagebox.showerror("Error", "Por favor selecciona un artículo.")

    def actualizar_lista_articulos(self):
        self.listbox_articulos.delete(0, tk.END)
        articulos = self.lista_articulos.obtener_lista()
        for articulo in articulos:
            self.listbox_articulos.insert(tk.END, f"{articulo[0]} - ${articulo[1]}")

    def create_pedidos_widgets(self):
        frame_pedidos = tk.LabelFrame(self.tabPedidos, text="Gestión de Pedidos", background='#67D4FF')
        frame_pedidos.pack(padx=10, pady=10, fill="both", expand=True)

        lbl_pedido = tk.Label(frame_pedidos, text="Pedido:", bg="#63FFE2")
        lbl_pedido.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_pedido = tk.Entry(frame_pedidos)
        self.entry_pedido.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        btn_hacer_pedido = tk.Button(frame_pedidos, text="Hacer Pedido", command=self.hacer_pedido, bg="#63FFE2")
        btn_hacer_pedido.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        btn_pedido_realizado = tk.Button(frame_pedidos, text="Pedido Realizado", command=self.pedido_realizado, bg="#63FFE2")
        btn_pedido_realizado.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.listbox_pedidos = tk.Listbox(frame_pedidos)
        self.listbox_pedidos.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def hacer_pedido(self):
        pedido = self.entry_pedido.get()
        if pedido:
            self.cola_pedidos.encolar(pedido.upper())
            self.actualizar_lista_pedidos()
            self.entry_pedido.delete(0, tk.END)
            messagebox.showinfo("Información", "Pedido realizado correctamente.")
        else:
            messagebox.showerror("Error", "Por favor ingresa el pedido.")

    def pedido_realizado(self):
        pedido = self.cola_pedidos.desencolar()
        if pedido:
            self.pila_ventas.apilar(pedido)
            messagebox.showinfo("Información", f"Pedido realizado: {pedido}")
            self.actualizar_lista_pedidos()
        else:
            messagebox.showinfo("Información", "No hay pedidos pendientes.")

    def actualizar_lista_pedidos(self):
        self.listbox_pedidos.delete(0, tk.END)
        pedidos = self.cola_pedidos.items
        for pedido in pedidos:
            self.listbox_pedidos.insert(tk.END, pedido)
    #Terminado
    def create_ventas_widgets(self):
        frame_ventas = tk.LabelFrame(self.tabVentas, text="Gestión de Ventas", background='#67D4FF')
        frame_ventas.pack(padx=10, pady=10, fill="both", expand=True)

        lbl_venta = tk.Label(frame_ventas, text="Venta:", bg="#63FFE2")
        lbl_venta.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_venta = tk.Entry(frame_ventas)
        self.entry_venta.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        lbl_precio2 = tk.Label(frame_ventas, text="Precio:",bg="#63FFE2")
        lbl_precio2.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_precio2 = tk.Entry(frame_ventas)
        self.entry_precio2.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        btn_realizar_venta = tk.Button(frame_ventas, text="Realizar Venta", command=self.realizar_venta, bg="#63FFE2")
        btn_realizar_venta.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        btn_devolucion = tk.Button(frame_ventas, text="Devolución", command=self.devolucion, bg="#63FFE2")
        btn_devolucion.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.listbox_ventas = tk.Listbox(frame_ventas)
        self.listbox_ventas.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    #Falta terminar:
    def realizar_venta(self):
        venta = self.entry_venta.get()
        precio2 = self.entry_venta.get()
        if venta and precio2:
            self.pila_ventas.apilar2(venta.upper(), precio2)#Error
            self.actualizar_lista_ventas()
            self.entry_venta.delete(0, tk.END)
            self.entry_precio2.delete(0, tk.END)
            messagebox.showinfo("Información", "Venta realizada correctamente.")
        else:
            messagebox.showerror("Error", "Por favor ingresa la venta.")
    #Falta terminar:
    def devolucion(self):
        venta = self.pila_ventas.desapilar()
        if venta:
            messagebox.showinfo("Información", f"Devolución realizada: {venta} ")
            self.actualizar_lista_ventas()
        else:
            messagebox.showinfo("Información", "No hay ventas realizadas para devolver.")
    #Parece estar terminado
    def actualizar_lista_ventas(self):
        self.listbox_ventas.delete(0, tk.END)
        ventas = self.pila_ventas.precio2
        for venta in ventas:
            self.listbox_ventas.insert(tk.END, f"{venta[0]} - $50")

if __name__ == "__main__":
    app = TiendaApp()
    app.minsize(380, 400)
    app.iconbitmap( "C:\\Users\\HOME\\Downloads\\compra_s3Z_icon.ico")
    app.mainloop()