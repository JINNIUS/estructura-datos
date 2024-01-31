# Crear un programa que pida "x" cantidad de numeros 
# y separar los numeros pares en un vector y los nones en otro
# mostrar ambos vectores

x_numero=int(input("Ingrese la cantidad de numeros que desea ingresar: "))

numero1=[]
numero2=[]

size=2

for i in range(x_numero):

    numero3=int(input(f"Ingrese el numero {i + 1}: "))

    if numero3 % 2 == 0:
        numero1.append(numero3)
    else:
        numero2.append(numero3)

print("\nNúmeros pares:", numero1)
print("Números impares:", numero2)