# Definicion :
# Es una estructura de datos que almancena elementos y que el primero en entrar es el ultimo en salir
# Usa el principio FIFO
#

from collections import deque

cola = deque()

# encolar
cola.append("Rafa")
cola.append("Irving")
cola.append("Pedro")
cola.append("Willmar")
print(cola)

# desencolar
elemento = cola.popleft()
print(elemento)


