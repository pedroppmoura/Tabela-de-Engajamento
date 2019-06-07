from win32api import GetSystemMetrics
import numpy as np
import cv2
from PIL import ImageGrab
import time

def printar_tela():
	img = ImageGrab.grab(bbox=(0, 0, GetSystemMetrics(0), GetSystemMetrics(1))) #x, y, w, h
	#img = ImageGrab.grab(bbox=(478, 469, 30, 30)) #x, y, w, h
	img_np = np.array(img)
	frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
	#cv2.imshow("frame", frame)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	return img

def dar_coordenadas_cor_print(a_,b_,c,limite):

	a = printar_tela()
	b = np.array(a)

	j = 0

	parar = False

	a1 = np.asarray([a_,b_,c])

	for eachRow in b:
		if parar == True:
			break
		j += 1
		i = 0
		for eachPix in eachRow:
			if parar == True:
				break
			i += 1

			if (a1 == eachPix).all() and j > GetSystemMetrics(1)*limite:
				print(eachPix)
				print(' : Row = ' +  str(j) + '; Column = ' +str(i))
				x_encontrado = i
				y_encontrado = j
				parar = True

	return x_encontrado, y_encontrado


