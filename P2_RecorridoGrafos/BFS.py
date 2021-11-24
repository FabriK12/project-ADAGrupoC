from collections import deque
from functions import generarMatriz, colorRange

def findComponentsBFS(matrix, rango):
	count = 0
	components = list()
	resultado = generarMatriz(matrix)
	width = int(len(matrix))
	height = int(len(matrix[0]))
	for i in range(width):
		for j in range(height):
			if resultado[i, j] == -1:
				count += 1
				bfs(i, j, matrix, resultado, rango)
	return resultado

def bfs(i, j, matriz, resultado, rango):
	reference = matriz[i][j]
	reference = int(reference)
	vertice = {
		"i": i,
		"j": j
	}
	queue = deque()
	queue.append(vertice)
	resultado[i][j] = reference

	while len(queue) > 0:
		vertice = queue.popleft()
		i = vertice["i"]
		j = vertice["j"]

		#if resultado[i][j] == -1:
		#	resultado[i][j] = reference

		#print("verticeCopia", ver)
		ver = vertice.copy()
		#arriba
		if i-1 >= 0 and j >= 0:
			pixel = matriz[i-1][j]
			if resultado[i-1][j] == -1 and colorRange(reference, rango, pixel):
				ver["i"] = i-1
				ver["j"] = j
				#https://github.com/JackMerma/proyectoAdaGrupoC/tree/main/P2_Recorrido_en_grafos
				resultado[i-1][j] = reference#MARCAR VISITA EN MATRIZ RESULTADO
				queue.append(ver)

		#izquierda		
		if i >= 0 and j - 1 >= 0:
			pixel = matriz[i][j-1]
			if resultado[i][j-1] == -1 and colorRange(reference, rango, pixel):
				ver["i"] = i
				ver["j"] = j-1
				resultado[i][j-1] = reference
				queue.append(ver)

		#abajo
		if i+1 < len(matriz) and j >= 0:
			pixel = matriz[i+1][j]
			if resultado[i+1][j] == -1 and colorRange(reference, rango, pixel):
				ver["i"] = i+1
				ver["j"] = j
				resultado[i+1][j] = reference
				queue.append(ver)

		#derecha		
		if i >= 0 and j + 1 < len(matriz[0]):
			pixel = matriz[i][j+1]
			if resultado[i][j+1] == -1 and colorRange(reference, rango, pixel):
				ver["i"] = i
				ver["j"] = j+1
				resultado[i][j+1] = reference
				queue.append(ver)