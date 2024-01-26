def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))
resultado = potencia_recursiva(base, exponente)
print(f"El resultado de {base} elevado a la {exponente} es {resultado}")
