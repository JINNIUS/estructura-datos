def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
#Ejemplo de uso:
lista_ordenada = [11,12,22,25,34,64,90]
elemento_a_buscar = 25
resultado = binary_search(lista_ordenada, elemento_a_buscar)
print(f"El elemento {elemento_a_buscar} esta en la posicion {resultado} (si es -1, el elemento no esta en la lista)")