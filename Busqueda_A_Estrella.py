from Nodo import *
import math
def aEstrella(laberinto, inicio, fin, tipo = True):
    nodo_inicio = Nodo(None, inicio)
    nodo_inicio.g = nodo_inicio.h = nodo_inicio.f = 0
    nodo_fin = Nodo(None, fin)
    nodo_fin.g = nodo_fin.h = nodo_fin.f = 0
    visitar = []
    visitados = []
    visitar.append(nodo_inicio)
    while len(visitar) > 0:
        nodo_actual = visitar[0]
        indice_actual = 0
        for i, item in enumerate(visitar):
            if item.f < nodo_actual.f:
                nodo_actual = item
                indice_actual = i
        visitar.pop(indice_actual)
        visitados.append(nodo_actual)

        if nodo_actual == nodo_fin:
            ruta = []
            actual = nodo_actual
            while actual is not None:
                ruta.append(actual.posicion)
                actual = actual.padre
            return ruta[::-1]
        nodos_hijo = []
        for nueva_posicion in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            posicion_nodo = (nodo_actual.posicion[0] + nueva_posicion[0], nodo_actual.posicion[1] + nueva_posicion[1])         
            if posicion_nodo[0] > (len(laberinto) - 1) or posicion_nodo[0] < 0 or posicion_nodo[1] > (len(laberinto[len(laberinto)-1]) -1) or posicion_nodo[1] < 0:
                continue
            if laberinto[posicion_nodo[0]][posicion_nodo[1]] != ' ':
                continue
            nuevo_nodo = Nodo(nodo_actual, posicion_nodo)
            nodos_hijo.append(nuevo_nodo)
        for nodo_hijo in nodos_hijo:
            for nodo_hijo_visitado in visitados:
                if nodo_hijo == nodo_hijo_visitado:
                    continue
            nodo_hijo.g = nodo_actual.g + 1         
            if(tipo):
                #Distancia Manhattan
                nodo_hijo.h = (abs(nodo_hijo.posicion[0] - nodo_fin.posicion[0])) + (abs(nodo_hijo.posicion[1] - nodo_fin.posicion[1]))
            else:
                #Distancia Euclidea
                nodo_hijo.h = math.sqrt((nodo_hijo.posicion[0] - nodo_fin.posicion[0]) ** 2 + (nodo_hijo.posicion[1] - nodo_fin.posicion[1]) ** 2)            
            
            nodo_hijo.f = nodo_hijo.g + nodo_hijo.h
            print(nodo_hijo.f, nodo_hijo.g, nodo_hijo.h)
            
            for nodo_abierto in visitar:
                if nodo_hijo == nodo_abierto and nodo_hijo.g > nodo_abierto.g:
                    continue
            visitar.append(nodo_hijo)
