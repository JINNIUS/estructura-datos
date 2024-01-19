#Ejemplo de la memoria dinamica usando clases

#Definicion de la clase
class ListaDinamica:
    def __init__(self):
        self.elementos = []

    def agregarElementos(self, elemento):
        self.elementos.append(elemento)

    def mostrarElementos(self):
        print("Elementos en la lista", self.elementos)

#Metodo memoria dinamica
def usoMemoriaDinamica():
    new_lista = ListaDinamica() #Objeto tipo lista dinamica

    new_lista.agregarElementos(10)
    new_lista.agregarElementos(10)
    new_lista.agregarElementos(10)

    #Mostrar la lista
    new_lista.mostrarElementos()

if __name__ == "__main__":
    usoMemoriaDinamica()
        