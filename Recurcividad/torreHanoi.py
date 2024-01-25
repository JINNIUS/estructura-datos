def torres_honoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
      # Caso Recursivo:
        #paso 1: Mueve la torre mas pequeña de origen auxiliar.
        torres_honoi(n-1, origen, auxiliar, destino)
        #paso 2: Mueve la torre 
        print((f"Mover disco {n} de origen a {destino}"))

        torres_honoi(n-1, origen, auxiliar, destino)
# Ejemplos de uso con 3 discos de A a C
torres_honoi(3,"A", "B", "C")