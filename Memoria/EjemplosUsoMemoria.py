# # Converciones nombres Variables
# nombre_paterno = "" #snake ase
# NOMBRE_PATERNO = "" #Screaming snake case
# NombrePaterno = "" #upper Camel case
# nombrePaterno = "" #lower Camel case

# #EJEMPLO MEMORIA ESTATICA

# edad = 25
# nombre = "Pedro"
# lista_estatica = [1,3,5,7,9]

# #EJEMPLO MEMORIA DINAMICA
# lista_dinamica = [2,4,6,8]
# print("Hola",nombre)
# print("selecciona un numero")
# print(lista_estatica)
# add_lista = int(input("Ingrese un numero"))
# lista_dinamica.append(add_lista)

class Persona:
    def __init__(self, nombre, edad) :
        self.nombre = nombre
        self.edad = edad
persona1 = Persona("Pedro",22)
persona2 = Persona("Irving",20)
persona3 = Persona("Will",18)

print(persona1.nombre)
print(persona2.nombre)
print(persona3.nombre)