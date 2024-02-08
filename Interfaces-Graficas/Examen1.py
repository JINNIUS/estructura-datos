def funcionMisteriosa(n):
    #Caso base:
    if n <= 0:
        return 0
    #Caso recursivo:
    return n + funcionMisteriosa(n-1)

print(funcionMisteriosa(5))
#lo que hace dicha funcion es si n no menor o igual a 0 se llama a si mismo 
#resta uno y se suma a la variable que en este caso es 5 dando el valor de 15
# 1 + 2 + 3 + 4 + 5 = 15