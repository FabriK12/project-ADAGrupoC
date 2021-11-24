import numpy as np
from Stack import Stack

def generarMatriz(matrix):
	matriz = np.full((len(matrix), len(matrix[0])), -1, dtype=int)
	return matriz

def findComponents(matrix, rango):
	count = 0
	components = list()
	resultado = generarMatriz(matrix)
	width = int(len(matrix))
	height = int(len(matrix[0]))
	#print(resultado)
	print(width, height)
	for i in range(width):
		for j in range(height):
			if resultado[i, j] == -1:
				count += 1
				dfs(i, j, matrix, resultado, rango)
	return resultado

def colorRange(reference, range, pixelColor):
	return pixelColor >= (reference-range) and pixelColor <= (reference+range)

def verticeSig(matriz, resultado, reference, vertice, rango):
	ver = vertice
	i = ver["i"]
	j = ver["j"]
	#print("verticeCopia", ver)
	#arriba
	if i-1 >= 0 and j >= 0:
		i = i - 1
		pixel = matriz[i][j]
		if resultado[i][j] == -1 and colorRange(reference, rango, pixel):
			ver["i"] = i
			ver["j"] = j
			return ver

	i = ver["i"]
	j = ver["j"]

	#izquierda		
	if i >= 0 and j - 1 >= 0:
		j = j-1
		pixel = matriz[i][j]
		if resultado[i][j] == -1 and colorRange(reference, rango, pixel):
			ver["i"] = i
			ver["j"] = j
			return ver
	
	i = ver["i"]
	j = ver["j"]

	#abajo
	if i+1 < len(matriz) and j >= 0:
		i = i + 1
		pixel = matriz[i][j]
		if resultado[i][j] == -1 and colorRange(reference, rango, pixel):
			ver["i"] = i
			ver["j"] = j
			return ver
	
	i = ver["i"]
	j = ver["j"]

	#derecha		
	if i >= 0 and j + 1 < len(matriz[0]):
		#print("Entra aqui")
		j = j + 1
		#print(j)
		pixel = matriz[i][j]
		if resultado[i][j] == -1 and colorRange(reference, rango, pixel):
			ver["i"] = i
			ver["j"] = j
			return ver
		else:
			ver["i"] = -1
			ver["j"] = -1
	else:
		ver["i"] = -1
		ver["j"] = -1
	return ver


def dfs(i, j, matriz, resultado, rango):
	reference = matriz[i][j]
	reference = int(reference)
	#print("Reference: ", reference)
	vertice = {
		"i": i,
		"j": j
	}
	stack = Stack()
	stack.push(vertice)
	k = 0
	while stack.size > 0:
		#print("\n============================")
		#print(k+1)
		vertice = stack.peek()
		i = vertice["i"]
		j = vertice["j"]
		if resultado[i][j] == -1:
			resultado[i][j] = reference
		#print(resultado)
		#print("Vertice actual",vertice)
		

		verSig = verticeSig(matriz, resultado, reference, vertice.copy(), rango)
		#print(verSig)

		if verSig["i"] != -1 and verSig["j"] != -1:
			#print("Encontro hijo")
			stack.push(verSig)
			#print(stack)
		else:
			#print("No encontro hijo")
			stack.pop()
			#print(stack)

		k += 1

		

# Convertir matriz
#matriz = np.array(matriz, dtype=np.uint8)


##print(matriz)
#matriz[0,0] = 0
#cv.imshow('none', matriz)
#cv.waitKey(0)

##print(matriz)