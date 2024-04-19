from collections import deque

class Laberinto:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])

    def es_valido(self, fila, columna):
        return 0 <= fila < self.filas and 0 <= columna < self.columnas and self.laberinto[fila][columna] !=1
    
    def encontrar_camino(self, inicio, fin):
        fila_inicio, columna = inicio
        fila_fin, columna_fin = fin
        