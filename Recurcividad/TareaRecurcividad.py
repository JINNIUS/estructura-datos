#Suma de elementos de un Array
arr=[5,8,9,10]
def suma_recursiva(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + suma_recursiva(arr[1:])
        
suma = suma_recursiva(arr)

print(suma)


"""
lista=[1,7,0,8,6]

suma=sum(lista)

print(suma)
"""