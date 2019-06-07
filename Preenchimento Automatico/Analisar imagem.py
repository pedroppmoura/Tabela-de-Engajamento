from win32api import GetSystemMetrics
import numpy as np
import cv2
from PIL import ImageGrab
import time
from PIL import Image

a = Image.open('Chrome.png')
b = np.array(a)

j = 0

for eachRow in b:
	j += 1
	i = 0
	for eachPix in eachRow:
		i += 1
		if [221 , 80 , 68] in eachPix:
			print(eachPix)
			print(' : Row = ' +  str(j) + '; Column = ' +str(i))
