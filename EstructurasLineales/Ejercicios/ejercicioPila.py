#Ejemplo simple de Deshacer en un editor de texto

class EditorTexto:
    def __init__(self):
        #Aqui definimos la pila
        self.historial = []
    def agregar_texto(self, texto):
        #Utilizamos push para agregar texto a la pila
        self.historial.append(texto)
    def deshacer(self):
        #Utilizamos pop pero antes validando que la pila no este vacia
        if self.historial:
            self.historial.pop()
    def mostrar_texto(self):
        print(self.historial)
        return "".join(self.historial)
    
editor = EditorTexto()

editor.agregar_texto("Hola")
editor.agregar_texto(" Mundo")
print(editor.mostrar_texto())
editor.deshacer() # quita lo ultimo que agregaste
print(editor.mostrar_texto())