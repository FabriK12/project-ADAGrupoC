import numpy as np
from collections import deque

def generarMatriz(matrix):
	matriz = np.full((len(matrix), len(matrix[0])), -1, dtype=int)
	return matriz

def colorRange(reference, range, pixelColor):
	return pixelColor >= (reference-range) and pixelColor <= (reference+range)

cola = deque()
cola.append(1)
cola.append(3)
cola.append(4)
print(cola.popleft())