class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
   # def preorden(NodoArbol):
        #if NodoArbol is not None:
           # print(NodoArbol.valor)
            #preorden(NodoArbol.izquierda)
            #preorden(NodoArbol.derecha)

    # Recorrido en inorden
    def inorden (nodo):
        if nodo is not None:
            inorden(nodo.izquierda)
            print(nodo.valor)
            inorden(nodo.derecha)

    def postorden(nodo):
        if nodo is not None:
            postorden(nodo.izquierda)
            postorden(nodo.derecha)
            print(nodo.valor)

#Crear nodos
nodo1 = NodoArbol(1)
nodo2 = NodoArbol(2)
nodo3 = NodoArbol(3)

#Conectar nodos
nodo1.izquierda = nodo2
nodo1.derecha = nodo3

print(nodo1.valor)
print(nodo1.izquierda.valor)
print(nodo1.derecha.valor)
print(nodo2.valor) # None por que no tiene asignados nodos hijos



# pip install matplo