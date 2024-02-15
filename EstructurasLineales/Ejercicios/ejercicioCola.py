from collections import deque

# Implementacion de un sistema de gestion de tareas pendientes
class SistemasGestionTareas:
    def __init__(self):
        self.tareas_pendientes = deque()
    
    def agregar_tareas(self, tarea):
        self.tareas_pendientes.append(tarea)
        print(self.tareas_pendientes)

    def procesar_tareas(self):
        while self.tareas_pendientes:
            tarea = self.tareas_pendientes.popleft()
            print("Procesando tarea", tarea)

# Ejemplo de uso
sistema = SistemasGestionTareas()
sistema.agregar_tareas("Bañarse")
sistema.agregar_tareas("Deayunar")
sistema.agregar_tareas("Tender Cama")
sistema.procesar_tareas()
