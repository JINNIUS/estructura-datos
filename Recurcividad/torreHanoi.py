def torres_honoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
      # Caso Recursivo:
        torres_honoi(n-1, origen, auxiliar, destino)
        print((f"Mover disco {n} de origen a {destino}"))

        torres_honoi(n-1, origen, auxiliar, destino)
torres_honoi(3,"A", "B", "C")