#Potencia de un Número
def potencia_recursiva(base, exponente):
    #caso base:
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

base = int(input("Ingrese un numero: "))
exponente = int(input("Ingresa el exponente: "))
resultado = potencia_recursiva(base, exponente)
print(f"El resultado de {base} elevado a la {exponente} es {resultado}")
