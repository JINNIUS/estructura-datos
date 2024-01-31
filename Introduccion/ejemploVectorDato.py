#Declaramos dos vectores
#Estos vectores seran homojeneos
nombre=[]
identificadores=[]

#Definimos un tamaño para los vectores
#Lo puedes cambiar si quieres, antesd la copilacion
size=3# Leemos los datos y los arreglamos a los agregados a la lista

for i in range(size):
    print("Ingrese los datos de la persona", i +1)
    input_nombre = input("Nombre: ")
    identificadores = input("indentification: ")

    nombre.append(input_nombre)
    identificadores.append(input_identificadores)

print(nombre)
print(identificadores)