def invertir_palabra(palabra):
    if len(palabra) == 0:
        return palabra
    else:
        return invertir_palabra(palabra[1:]) + palabra[0]

palabra = input("Ingresa una pabra: ")
palabra_invertida = invertir_palabra(palabra)
print(f"La palabra invertida de {palabra} es {palabra_invertida}")
