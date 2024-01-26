#hacer una funcion recursiva para sumar numeros naturales

"""
numeros=[]

def ejemplo_recursivo(n):
    #Caso Base
    if n == 0:
        return 0
    #Llamada Recursiva
    else:
        return n + ejemplo_recursivo(n-1)
resultado = ejemplo_recursivo(5)
print("Resultado:",resultado)"""

def suma_dos_numeros_recursiva(a, b):
# Caso Base
  if b == 0:
    return a
# Llamada Recursiva
  else:
   print (a+1, b-1)

  return suma_dos_numeros_recursiva(a + 1, b - 1)

# Ejemplo de uso
num1 = 3
num2 = 4
resultado = suma_dos_numeros_recursiva(num1, num2)
print(f"La suma de {num1} y {num2} es: {resultado}")