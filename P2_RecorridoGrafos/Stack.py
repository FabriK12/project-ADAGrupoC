class Node():
	def __init__(self, valor):
		self.valor = valor
		self.next = None

class Stack:

	def __init__(self):
		self.head = Node("head")
		self.size = 0 

	def __str__(self):
		actual = self.head.next
		str1 = "["
		while actual:
			str1 += str(actual.valor) + ", "
			actual = actual.next

		str1 = str1[:-2] + "]"	
		if(self.size == 0):
			return "[]"
		return str1

	def lenght(self):
		return self.size

	def isEmpty(self):
		return self.size == 0

	def push(self, valor):
		node = Node(valor)
		node.next = self.head.next
		self.head.next = node
		self.size += 1

	def peek(self):
		if self.isEmpty():
			raise Exception("Error la pila esta vacia...")
		return self.head.next.valor

	def pop(self):
		if self.isEmpty():
			raise Exception("Error la pila esta vacia...")
		remove = self.head.next
		self.head.next = self.head.next.next
		self.size -= 1
		return remove.valor