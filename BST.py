class Nodo(object) :

	def __init__(self, dato = None ) :
		self.dato = dato
		self.izq = None
		self.der = None

class BST(object) :
	def __init__(self, dato = None) :
		if dato is None :
			self.raiz = None
		else:
			self.raiz = Nodo(dato)

	def is_leaf(self, nodo) :
		if nodo.izq == None and nodo.izq == None :
			return True
		return False

	def push(self, a_insertar) :
		if self.raiz == None :
			self.raiz = Nodo(a_insertar)
			print("raiz "+str(a_insertar) )
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
				print("Ya existe")
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

	def delete(self, a_eliminar) :
		iterador = self.raiz
		iterador_ant = None
		auxiliar = None
		if a_eliminar is self.raiz.dato and is_leaf(self.raiz) :
			del self.raiz
			self.raiz = None
			return

		while a_eliminar != iterador.dato :
			iterador_ant = iterador
			if iterador.dato < a_eliminar and iterador.izq != None :
				iterador = iterador.izq
			if iterador.dato > a_eliminar and iterador.der != None :
				iterador = iterador.der
			if a_eliminar != iterador.dato and iterador.der == None and iterador.izq == None :
				print("no existe")
				return
		if is_leaf(iterador) :
			if iterador_ant.der is iterador :
				del iterador
				iterador_ant.der = None
			elif iterador_ant.izq is iterador :
				del iterador
				iterador_ant.izq = None
		else :
			pass

if __name__ == '__main__':
	
	abb = BST();
	solicitud = "1) insertar 2) eliminar 3) iterar 4) recorridos 5) salir\t: "
	val_solicitud = 0
	val_insert = None
	val_del = None

	while val_solicitud != 5 :
		val_solicitud = int(input(solicitud))
		if val_solicitud is 1:
			val_insert = int(input("dame un numero\t: "))
			abb.push(val_insert)
		elif val_solicitud is 2 :
			val_del = int(input("dame un numero a eliminar"))
			abb.delete(val_del)
		elif val_solicitud is 3 :
			abb.iterar()
		elif val_solicitud is 4 :
			pass
		elif val_solicitud is 5 :
			print("bye")
		else :
			print("opcion invalida")
