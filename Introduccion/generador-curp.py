# Hacer un programa que genere una curp hipotetica tomando los siguientes valores
# Inicial del Apellido Paterno y Materno, como la inicial de tu nombre(s)

nombre = input("Ingresa tu primer nombre: ")
nombre2 = input("Ingrese su segundo nombre: ")
apellido = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apllido: ")

nombre.upper()
nombre2.upper()
apellido.upper()
apellido2.upper()

var = nombre[0]
var2 = nombre2[0]
var3 = apellido[0]
var4 = apellido[0]

curp = (var4+var3+var2+var)
print(nombre)
print(nombre2)
print(apellido)
print(apellido2)
print("Tu curp es: ", curp.upper())