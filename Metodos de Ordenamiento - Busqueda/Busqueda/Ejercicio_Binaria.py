# Realizar una funcio de busqueda binaria que maneje listas 
# Ordenadas de manera decendente

def busqueda_binaria_decendente(lista, valor_objetivo):
    izquierda, derecha = 0, len(lista)-1

    while izquierda <= derecha:
        medio = (izquierda + derecha)//2

        if lista[medio] == valor_objetivo:
            return medio
        elif lista[medio]> valor_objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
# Ejemplo de uso

lista_decendente = [9, 8, 7, 6, 5, 4, 3, 2, 1]

valor_buscar = 6
indice_encontrado = busqueda_binaria_decendente(lista_decendente, valor_buscar)

if indice_encontrado != - 1:
    print("El elemento se encontro en el indice: ", indice_encontrado)
else:
    print("El elemento no se encontro en la lista")
