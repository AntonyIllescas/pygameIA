class Nodo():

    def __init__(self, padre = None, posicion = None):
        self.padre = padre
        self.posicion = posicion

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, otra):
        return self.posicion == otra.posicion
