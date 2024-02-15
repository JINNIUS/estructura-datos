# Definicion :
# Es una estructura de datos que esta efocada en la busqueda de un solo elemento
# funciona como una coleccion de datos
# Tiene operaciones CRUD
#

lista = [10,20,30,40]
print(lista)

lista.insert(1,15)

# Insertar datos
print(lista)

# Buscar datos
posicion = lista.index(10) #Busca el dato almacenado y devulce la posicion del index
posicion = lista.index(30) #El dato almacenado debe existir
print(posicion)

#Actualizar datos, especificando el index
lista[1] = 17
print(lista)

#Eliminar, un elemento segun el index
del lista[1]
print(lista)