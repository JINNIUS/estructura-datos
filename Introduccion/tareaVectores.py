# Crear un programa que almacene nombres en un vector
# capturar datos hasta que el valor ingresado, se "STOP"
# mostrar el resultante 
# (Sugerencia usar el metodo while)

nombre = input("Ingrese el nombre de la persona o escriba STOP para terminar el programa: ")

nombres=[]

while nombre != "STOP":

    nombres.append(nombre)
    nombre = input("Ingrese el nombre de la persona o escriba STOP para terminar el programa: ")
    
print(f"Los nombres ingresados son: {nombres}")