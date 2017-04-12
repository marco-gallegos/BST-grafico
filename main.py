import pygame, sys
from pygame.locals import *
from random import *


class Nodo(object) :
	def __init__(self, dato = None ) :
		self.dato = dato
		self.izq = None
		self.der = None

class BST(object) :
	def __init__(self, dato = None) :
		self.raiz = Nodo(dato)
	
	def push(self, a_insertar) :
		if self.raiz == None :
			self.raiz = Nodo(a_insertar)
			print("raiz"+str(a_insertar) )
			return
		
		iterador = self.raiz
		
		while True :
			if a_insertar < iterador.dato:
				if iterador.izq is None :
					iterador.izq = Nodo(a_insertar)
					break
					
				iterador = iterador.izq
				
			if a_insertar > iterador.dato :
				if iterador.der is None :
					iterador.der = Nodo(a_insertar)
					break
					
				iterador = iterador.der
				
			if iterador.dato == a_insertar :
				print("igual")
				return
		print("inserte "+str(a_insertar) )
		
		
	
	def iterar(self) :
		opc = 0;
		iterador = self.raiz
		while opc != 5 :
			print(str(iterador.dato))
			opc = int(input("1 izq 2 der 3 reset 5 salir: "))
			if opc is 1 and iterador.izq != None :
				iterador = iterador.izq
			if opc is 2 and iterador.der != None :
				iterador = iterador.der
			if opc is 3 :
				iterador = self.raiz
			if opc is 5 :
				break

abb = BST(randint(0,100))
#abb.push(7)
#abb.push(15)
#abb.push(8)
#abb.push(16)
#abb.push(9)
#abb.push(6)
for i in range(0,10) :
	var = randint(0,100)
	abb.push(var)

pygame.init()


FPS = 30
fpsClock = pygame.time.Clock()

ventana = pygame.display.set_mode((1000,700),0,32)

pygame.display.set_caption("Simulador inorden sobre unArbol Binario de Busqueda")

colorventana = (0,0,0)
colorlineas = (132, 132, 132)
colornodo = (131, 0, 127)
colornodobusqueda = (0, 60, 60)

colortexto = (255, 255, 255)

#ejemplo de crear texto para usar con blit
fuente = pygame.font.Font(None, 20)
texto = "hola pygame"
mensaje = fuente.render(texto,1,colortexto)
#mensaje es el parametro de blit

cambio_por_nivel = [250, 100, 80, 50, 30 , 20, 10, 10, 10, 10]



posx = 490
posy = 15

def pintarnodo(nodo, x, y, lev = -1, color = colornodo):
	
	texto = str(nodo.dato)
	mensaje = fuente.render(texto, 1, colortexto)
	pygame.draw.circle(ventana,color,(x,y),15)
	ventana.blit(mensaje,(x-7,y-5))
	
	lev += 1
	if nodo.izq != None :
		pygame.draw.line(ventana,colorlineas,(x-15,y+5),(x-cambio_por_nivel[lev],y+65),3)
		pintarnodo(nodo.izq,x-cambio_por_nivel[lev],y+65, lev)
	if nodo.der != None :
		pygame.draw.line(ventana,colorlineas,(x+15,y+5),(x+cambio_por_nivel[lev],y+65),3)
		pintarnodo(nodo.der,x+cambio_por_nivel[lev],y+65, lev)


def pintarnodosolo(nodo, x, y, lev = -1, color = colornodo):
	texto = str(nodo.dato)
	mensaje = fuente.render(texto, 1, colortexto)
	pygame.draw.circle(ventana,color,(x,y),15)
	ventana.blit(mensaje,(x-7,y-5))
	
	
def buscar(abb, num, x, y, lev = 0):
	nodo = abb.raiz
	oldx = x
	oldy = y
	newposx = x
	newposy = y
	while nodo.dato != num :
		if num < nodo.dato and nodo.izq != None :
			oldx = newposx
			oldy = newposy
			newposx -= cambio_por_nivel[lev]
			newposy += 65
			for pos in range(oldx,newposx,-1) :
				pygame.draw.circle(ventana,colornodobusqueda,(pos,oldy),10)
				pygame.display.update()
				
			for pos in range(oldy,newposy) :
				pygame.draw.circle(ventana,colornodobusqueda,(newposx,pos),10)
				pygame.display.update()
			nodo = nodo.izq
			lev+=1
			
		if num > nodo.dato and nodo.der != None :
			oldx = newposx
			oldy = newposy
			newposx += cambio_por_nivel[lev]
			newposy += 65
			for pos in range(oldx,newposx) :
				pygame.draw.circle(ventana,colornodobusqueda,(pos,oldy),10)
				pygame.display.update()
				
			for pos in range(oldy,newposy) :
				pygame.draw.circle(ventana,colornodobusqueda,(newposx,pos),10)
				pygame.display.update()
			nodo = nodo.der
			lev +=1
			
		if num == nodo.dato :
			print("encontrado")
			return
			
		if nodo.dato != num :
			if num < nodo.dato and nodo.izq is None :
				print("no encontrado ")
				return
			if num > nodo.dato and nodo.der is None :
				print("no encontrado ")
				return
				
	
		
		

while True :
	ventana.fill(colorventana)
	
	for event in pygame.event.get():
		if event.type is pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	#pintando mensaje en ventana
	#ventana.blit(mensaje,(posx,posy))
	
	pintarnodo(abb.raiz, posx, posy)
	pygame.display.update()
	
	opc = int(input("numero a buscar"))
	
	buscar(abb, opc, posx, posy )
	
	pygame.display.update()
	fpsClock.tick(FPS)
