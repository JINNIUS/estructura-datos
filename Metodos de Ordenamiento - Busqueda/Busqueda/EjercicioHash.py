# Utilizar una tabla Hash para escribir un programa que cuente la frecuencia de aparicion 
# de cada palabra en un texto

def contar_frecuencias(texto):
    #Pasar el string a una lista de palabras
    palabras = texto.split()

    #Crear el diccionario que almacene las frecuencias
    frecuencias = {}

    #Recorrer las palabras en la lista
    for palabra in palabras:
        
        if palabra in frecuencias:
            frecuencias[palabra]+=1 #Incrementar el contador para las palabras existentes
        else:
            frecuencias[palabra]=1 #Inicio del contador con nuevas palabras
    return frecuencias

# Definir texto
texto_ejemplo = "hello world hello"
frecuencias = contar_frecuencias(texto_ejemplo)
print(frecuencias)