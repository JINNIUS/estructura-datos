class Tarea:
    def __init__(self, nombre, fecha_inicial, fecha_limite):
        self.nombre = nombre
        self.fecha_inicial = fecha_inicial
        self.fecha_limite = fecha_limite

    def mostrar_tareas(self):
        print("\nTareas creadas:\n ")
        for tarea in tareas: 
            print(f"Nombre: {tarea.nombre}, Fecha inicial: {tarea.fecha_inicial}, Fecha limite: {tarea.fecha_limite}")

tareas = []

tarea1 = Tarea("Comprar leche", "01/01/2024", "05/01/2024")
tareas.append(tarea1)
tarea2 = Tarea("Ir al supermercado", "11/01/2024", "05/02/2024")
tareas.append(tarea2)
tarea3 = Tarea("Leer un libro", "08/01/2024", "10/01/2024")
tareas.append(tarea3)
tarea4 = Tarea("Ir al cine", "21/02/2024", "25/02/2024")
tareas.append(tarea4)
tarea5 = Tarea("Estudiar para el examen", "16/01/2024", "18/01/2024\n")
tareas.append(tarea5)

tarea1.mostrar_tareas()