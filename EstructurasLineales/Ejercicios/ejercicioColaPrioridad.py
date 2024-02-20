import heapq

class SistemaPlanificacionTareas:
    def __init__(self):
        # Iniciamos la cola
        self.tareas = []

    def agregar_tareas(self,tarea,prioridad):
        #Encolar tareas
        heapq.heappush(self.tareas, (prioridad, tarea))
    
    def procesar_tareas(self):
        #Mostrar Tareas encoladas
        while self.tareas:
            prioridad, tarea = heapq.heappop(self.tareas)
            print("Procesando tarea:",tarea, "(prioridad:",prioridad,")")

sistema = SistemaPlanificacionTareas()
sistema.agregar_tareas("Comer", 4)
sistema.agregar_tareas("Despertar", 2)
sistema.agregar_tareas("Desayunar", 1)
sistema.agregar_tareas("Salir de casa", 3)
sistema.procesar_tareas()