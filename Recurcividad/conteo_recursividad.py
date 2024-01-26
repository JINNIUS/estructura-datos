def contar_digitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)

numero = int(input("Ingresa un número: "))
cantidad_digitos = contar_digitos(numero)
print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
