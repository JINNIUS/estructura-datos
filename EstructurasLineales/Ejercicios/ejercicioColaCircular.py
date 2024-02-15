#Ejercicio cola circular
from collections import deque

# Implementacion de un simulador de rotacion de empleados en turnos
def rotacion_empleados(empleados, turnos):

    cola_empleados = deque(empleados)

    for _ in range(turnos):
        empleado_actual = cola_empleados.popleft()
        cola_empleados.append(empleado_actual)
        print("Empleado en turno:", cola_empleados[0])

#Ejemplo de uso 
empleados = ["Francisco", "Rafa", "Irving", "Pedro"]
rotacion_empleados(empleados, 7)