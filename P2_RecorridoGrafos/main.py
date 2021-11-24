import cv2 as cv
import numpy as np

from DFS import findComponents, generarMatriz

nemo = cv.imread('images/dory.jpg')

nemoGray = cv.cvtColor(nemo, cv.COLOR_BGR2GRAY)

def rescaleFrame(frame, scale=0.75):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

remoRescale = rescaleFrame(nemoGray, 0.40)
cv.imshow('original', remoRescale)
matrixResult = findComponents(remoRescale, 30)

# Convertir matriz
matriz = np.array(matrixResult, dtype=np.uint8)

print(matriz)
cv.imshow('Paleta reducida', matriz)
cv.imwrite('images/rescala.jpg', matriz)
cv.waitKey(0)
'''

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