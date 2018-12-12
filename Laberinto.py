rom Busqueda_A_Estrella import *
from Busqueda_Fuerza_Bruta import *
import pygame
import random

def generarObtaculos(n):
	obstaculos = []
	for i in range(n - 1):
		obstaculos.append((random.randint(0, n - 1), random.randint(0, n - 1)))
	return obstaculos
	
def generarLaberinto(n, obstaculos):
	laberinto = []
	for i in range(n):
		laberinto.append([' ' for j in range(n)])

	for i in range(len(obstaculos)):
		x, y = obstaculos[i]
		laberinto[x][y] = '0'
	return laberinto

def imprimir(laberinto):
	for i in range(len(laberinto)):
		print(laberinto[i])

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
BLANCO1 = (252, 252, 252)
VERDE = (127, 255, 126)
ROJO = (255, 124, 44)
AZUL = (128, 241, 255)
AMARILLO = (255, 255, 45)

pygame.init()

dimensiones = [600, 600]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Laberinto Pygame")

juego_terminado = False
x1 = y1 = 0
x2 = y2 = 0
k = 0
l = 0
px = 75
inicio = (0, 3)
final = (5, 5)
obstaculos = generarObtaculos(8)
print(obstaculos)
laberinto = generarLaberinto(8, obstaculos)
imprimir(laberinto)
ruta1 = aEstrella(laberinto, inicio, final)
busqueda(laberinto, inicio, final)
ruta2 = devolverRuta()
ruta2.append(final)

reloj = pygame.time.Clock()
ancho = int(dimensiones[0] / 8)
alto = int(dimensiones[1] / 8)
yi, xi = inicio
yf, xf = final
while juego_terminado is False:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			juego_terminado = True
		if evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_r:
				k = l = 0
				
	pantalla.fill(BLANCO)
	color = 0
	for i in range(0, dimensiones[0], ancho):
		for j in range(0, dimensiones[1], alto):
			pygame.draw.rect(pantalla, BLANCO, [i, j, ancho, alto], 0)

		color += 1
	for yo, xo in obstaculos:
		pygame.draw.rect(pantalla, NEGRO, [ xo * px, yo * px, ancho, alto], 0)
	pygame.draw.rect(pantalla, VERDE, [xi * px, yi * px, ancho, alto], 0)
	pygame.draw.rect(pantalla, ROJO, [xf * px, yf * px, ancho, alto], 0)
	pygame.draw.rect(pantalla, AZUL, [x1 * px, y1 * px, ancho, alto], 0)
	pygame.draw.rect(pantalla, AMARILLO, [x2 * px, y2 * px, ancho, alto], 0)
		
	if(k < len(ruta1)):
		y1, x1 = ruta1[k]
		k += 1
	if(l < len(ruta2)):
		y2, x2 = ruta2[l]
		l += 1
	pygame.display.flip()
	reloj.tick(1)
	
pygame.quit()
