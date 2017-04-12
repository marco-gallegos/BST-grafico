class Nodo(object) :
	def __init__(self, dato = None ) :
		self.dato = dato
		self.izq = None
		self.der = None

class BST(object) :
	def __init__(self, dato = None) :
		self.raiz = Nodo(dato)

	def is_leaf(self, nodo) :
		if nodo.izq == None and nodo.izq == None :
			return True
		return False

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
		while a_eliminar != iterador.dato :
			if iterador.dato < a_eliminar and iterador.izq != None :
				iterador = iterador.izq
			if iterador.dato > a_eliminar and iterador.der != None :
				iterador = iterador.der
			if a_eliminar != iterador.dato and iterador.der == None and iterador.izq == None :
				print("no existe")
				return
