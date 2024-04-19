def busqueda_secuencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

#Uso de la funcion
lista = [5, 3, 9, 2, 8]
indice = busqueda_secuencial(lista, 9)
print("El elemento se encontró en el índice:", indice)