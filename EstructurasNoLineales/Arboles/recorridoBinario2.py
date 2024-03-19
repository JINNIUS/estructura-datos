import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def crear_arbol_binario(ax, nodo, x, y, nivel, espacio):
    if nodo is not None:
        texto = str(nodo.valor)
        
        ax.text(x, y, texto, horizontalalignment='center', fontsize=12)
        if nodo.izquierda is not None:
            ax.add_patch(FancyArrowPatch((x, y-0.05), (x-espacio/nivel, y-0.15), arrowstyle='->', mutation_scale=10))
        if nodo.derecha is not None:
            ax.add_patch(FancyArrowPatch((x, y-0.05), (x+espacio/nivel, y-0.15), arrowstyle='->', mutation_scale=10))
        crear_arbol_binario(ax, nodo.izquierda, x-espacio/nivel,y-0.2,nivel*2,espacio)
        crear_arbol_binario(ax, nodo.derecha, x+espacio/nivel, y-0.2, nivel*2, espacio)

def dibujar_arbol_binario(raiz):
    fig, ax = plt.subplots(3,1, figsize=(10,15))

    for i, recorrido in enumerate([inorden, preorden, postorden]):
        ax[i].set_xlim(0, 2)
        ax[i].set_ylim(0, 2)
        crear_arbol_binario(ax[i], raiz, 1, 1.9, 4, 1)
        ax[i].axis('off')
        ax[i].set_title("Recorrido "+recorrido.__name__.capitalize()) 

        recorrido_text = obtener_recorrido_texto(raiz,recorrido)
        ax[i].text(0.5, 0.5, recorrido_text, horizontalalignment="center", verticalalignment="center", fontsize=12)

    plt.tight_layout()
    plt.show()

def obtener_recorrido_texto(nodo, recorrido):
    recorrido_text = []
    recorrido(nodo, recorrido_text)
    return " ".join(map(str,recorrido_text))

def inorden(nodo, recorrido):
    if nodo is not None:
        inorden(nodo.izquierda, recorrido)
        recorrido.append(nodo.valor)
        inorden(nodo.derecha, recorrido)
    
def preorden(nodo, recorrido):
    if nodo is not None:
        recorrido.append(nodo.valor)
        preorden(nodo.izquierda, recorrido)
        preorden(nodo.derecha, recorrido)
    
def postorden(nodo, recorrido):
    if nodo is not None:
        postorden(nodo.izquierda, recorrido)
        postorden(nodo.derecha, recorrido)
        recorrido.append(nodo.valor)

raiz = NodoArbol("A")

nodoB = NodoArbol("B")
nodoD = NodoArbol("D")
nodoG = NodoArbol("G")
nodoE = NodoArbol("E")
nodoH = NodoArbol("H")
nodoI = NodoArbol("I")
nodoC = NodoArbol("C")
nodoF = NodoArbol("F")
nodoJ = NodoArbol("J")
nodoK = NodoArbol("K")

raiz.izquierda = nodoB
raiz.derecha = nodoC

nodoB.izquierda = nodoD
nodoB.derecha = nodoE
nodoE.izquierda = nodoH
nodoE.derecha = nodoI

nodoD.izquierda = nodoG

nodoC.derecha = nodoF
nodoF.izquierda = nodoJ
nodoJ.derecha = nodoK

dibujar_arbol_binario(raiz)
