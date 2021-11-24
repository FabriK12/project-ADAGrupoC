import cv2 as cv
import numpy as np
from BFS import findComponentsBFS

from DFS import findComponentsDFS, generarMatriz

nemo = cv.imread('images/dory.jpg')
dory = cv.imread('images/dory.jpg')

nemoGray = cv.cvtColor(nemo, cv.COLOR_BGR2GRAY)
doryGray = cv.cvtColor(dory, cv.COLOR_BGR2GRAY)

def rescaleFrame(frame, scale=0.75):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

remoRescale = rescaleFrame(nemoGray, 0.40)
doryRescale = rescaleFrame(doryGray, 0.40)
#cv.imshow('original', remoRescale)
matrixResult = findComponentsDFS(remoRescale, 10)
matrixResult1 = findComponentsBFS(doryRescale, 10)

# Convertir matriz
matriz = np.array(matrixResult, dtype=np.uint8)
matriz1 = np.array(matrixResult1, dtype=np.uint8)


print(matriz)
cv.imshow('Dory DFS reducida', matriz)
cv.imshow('Dory reducida', matriz1)

#cv.imwrite('images/rescala.jpg', matriz)
cv.waitKey(0)
'''
probando = [
	[5, 9, 19, 3, 5],
	[11, 3, 16, 20, 10],
	[1, 6, 15, 2, 6],
	[5, 1, 8, 4, 30],
]
matrixResult = findComponentsDFS(probando, 10)
matrixResult1 = findComponentsBFS(probando, 10)
print(matrixResult)
print(matrixResult1)

probando = [
	[0, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 255, 255, 255, 255, 255, 255, 255, 255, 255],
	[0, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 255, 255, 255, 255, 255, 255, 255, 255, 255],
	[0, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 255, 255, 255, 255, 255, 255, 255, 255, 255],
	[0, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 255, 255, 255, 255, 255, 255, 255, 255, 255],
	[0, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 255, 255, 255, 255, 255, 255, 255, 255, 255],
	[0, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 255, 255, 255, 255, 255, 255, 255, 255, 255],
	[0, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 255, 255, 255, 255, 255, 255, 255, 255, 255],
	[0, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 255, 255, 255, 255, 255, 255, 255, 255, 255],
	[0, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 255, 255, 255, 255, 255, 255, 255, 255, 255],
	[0, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 255, 255, 255, 255, 255, 255, 255, 255, 255],
	[0, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 255, 255, 255, 255, 255, 255, 255, 255, 255],
	[0, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 255, 255, 255, 255, 255, 255, 255, 255, 255],
]

probando = [
	[5, 9, 19, 3],
	[11, 3, 16, 20],
	[1, 6, 15, 2],
	[5, 1, 8, 4],
]

print(len(probando[1]))



#print(matriz)
#matriz[0,0] = 0
#cv.imshow('none', matriz)
#cv.waitKey(0)

#print(nemoGray)
#print(len(nemoGray))

#x = np.array(probando, dtype=np.uint8)
#m = np.asmatrix(x)


#cv.imshow('none', m)

#cv.imshow('nemo', nemoGray)

#cv.waitKey(0)
'''