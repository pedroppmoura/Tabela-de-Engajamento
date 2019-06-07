import pyautogui, sys
import time
import win32clipboard
import win32con
import numpy as np
from Print_da_Tela import *

def Coletar_Facebook():
	global curtidas, output

	def facebooktoexcel(letra):
		global curtidas, output

		if letra == "C":
			prefix = "\\r\\n\\r\\n"
		elif letra == "B":
			prefix = "\\r\\n"
		else:
			prefix = ''



		if prefix + "Ana Beatriz Farias" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Beatriz Mendon\\xc3\\xa" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Bianca Felipe" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Taynara Ramalho" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Ernane Matheus" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Giovanny Silva" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Jo\\xc3\\xa3o Vin\\xc3\\xadcius Pereira" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Pedro Paulo Pinheiro Moura" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "J\\xc3\\xbalia Caroline" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Luiz Andr\\xc3\\xa9 Fialho Oliveira" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Emanuelle Paiva" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Izabele Vitoria" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "J\\xc3\\xbalia Vieira" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Tuiza Galgani" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Victor Duarte" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		output = output + '\n'


	Tudo = ''

	def alt_tab_to_chrome(a,b,c, extra, alttab):
		if alttab:
			pyautogui.keyDown('alt')
			pyautogui.press('tab')

		c_x, c_y = dar_coordenadas_cor_print(a,b,c,0)

		pyautogui.click(c_x,c_y + extra, duration = 0.2)

		pyautogui.keyUp('alt')


	def double_key(a,b):
		pyautogui.keyDown(a)
		pyautogui.press(b)
		pyautogui.keyUp(a)

	def multiple_alttab(a):
		pyautogui.keyDown('alt')
		for i in range(a):
			pyautogui.press('tab')
			time.sleep(0.5)
		pyautogui.keyUp('alt')

	def check_cor_print_limite_y(a_,b_,c,limite):

		time.sleep(2)
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

				if (a1 == eachPix).all() and GetSystemMetrics(1)*limite > j:
					print(eachPix)
					print(' : Row = ' +  str(j) + '; Column = ' +str(i))
					x_encontrado = i
					y_encontrado = j
					parar = True

		return True

	# ABRIR CHROME

	alt_tab_to_chrome(220,76,64, 40, True)
	alt_tab_to_chrome(68,103,177, 0, False)

	# Arrastar página para o final

	pyautogui.moveTo(628, 400, 0.1)
	for aosjf in range(2):
		time.sleep(3)
		pyautogui.scroll(-10000)

	coord = {}

	if check_cor_print_limite_y(52,159,253,0.5):
		coord[0] = 731

	else:
		coord[0] = 527

	c_x, c_y = dar_coordenadas_cor_print(51 , 158 , 253,0.5)

	# Abrir Quadro de Reações

	pyautogui.moveTo(c_x+50,c_y, 0.5)
	pyautogui.click()

	# Selecionar tudo

	pyautogui.moveTo(575, 246, 2)
	pyautogui.mouseDown(button='left')
	pyautogui.moveTo(1000, 661, 0.5)
	time.sleep(2)
	pyautogui.mouseUp(button='left')

	# Dar ctl+c

	pyautogui.keyDown('ctrl')
	pyautogui.press('c')
	pyautogui.keyUp('ctrl')

	time.sleep(0.5)

	win32clipboard.OpenClipboard()
	novo = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
	Tudo = Tudo + ' ComecouCurtidas: ' + novo 
	win32clipboard.CloseClipboard()


	# Fechar janela de reações

	pyautogui.click(1136,600, duration = 0.5)

	# Abrir compartilhamentos e ir até o final

	pyautogui.moveTo(c_x+330,c_y, 0.5)
	pyautogui.click()

	time.sleep(1)

	pyautogui.scroll(-10000)
	time.sleep(1)
	pyautogui.scroll(-10000)
	time.sleep(1)
	pyautogui.scroll(-10000)

	# Selecionar compartilhamentos


	if coord[0] == 731:
		pyautogui.moveTo(1056,757, 0.5)
		pyautogui.mouseDown(button='left')
		pyautogui.moveTo(524, 77, 0.5)
		time.sleep(5)
		pyautogui.mouseUp(button='left')
	else:
		pyautogui.moveTo(1056,725, 0.5)
		pyautogui.mouseDown(button='left')
		pyautogui.moveTo(520, 725, 0.5)
		pyautogui.moveTo(520, 250, 0.5)
		time.sleep(5)
		pyautogui.mouseUp(button='left')


	# Copiar compartilhamentos

	pyautogui.keyDown('ctrl')
	pyautogui.press('c')
	pyautogui.keyUp('ctrl')

	time.sleep(0.5)

	win32clipboard.OpenClipboard()
	novo = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
	Tudo = Tudo + ' ComecouCompartilhamentos: ' + novo 
	win32clipboard.CloseClipboard()


	# Fechar compartilhamentos


	pyautogui.click(1160,700, duration = 0.5)

	time.sleep(1)

	pyautogui.scroll(-10000)

	time.sleep(1)

	# Abrir caixa de comentários

	c_x, c_y = dar_coordenadas_cor_print(51 , 158 , 253,0.5)


	pyautogui.click(c_x + 270,c_y, duration = 0.5)

	time.sleep(1)

	pyautogui.scroll(-10000)

	# Expandir caixa de comentários

	if coord[0] == 731:
		pyautogui.click(478,778, duration = 0.5)
	else:
		pyautogui.click(425,714, duration = 0.5)

	pyautogui.scroll(-10000)
	time.sleep(2)
	pyautogui.scroll(-10000)

	# Copiar comentários

	if coord[0] == 731:
		pyautogui.moveTo(841,790,0.5)
		time.sleep(2)
		pyautogui.mouseDown(button='left')
		pyautogui.moveTo(343, 790, 0.5)
		pyautogui.moveTo(343, 79, 0.5)
		time.sleep(5)
	else:
		pyautogui.moveTo(800,686,0.5)
		time.sleep(2)
		pyautogui.mouseDown(button='left')
		pyautogui.moveTo(317, 686, 0.5)
		pyautogui.moveTo(317, 86, 0.5)
		time.sleep(5)

	pyautogui.mouseUp(button='left')

	pyautogui.keyDown('ctrl')
	pyautogui.press('c')
	pyautogui.keyUp('ctrl')

	time.sleep(0.5)

	win32clipboard.OpenClipboard()
	novo = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
	Tudo = Tudo + 'ComecouComentarios' + novo
	win32clipboard.CloseClipboard()

	## Convertendo tudo para uma linguagem aceitavel pelo python (sem emojis).

	Tudo = Tudo.encode('utf-8')

	Tudo = str(Tudo)

	print(Tudo)


	### PARTE 2
	### EXTRAÇÃO DE INFORMAÇÕES DA STRING


	curtidas = Tudo[:Tudo.index('ComecouCompartilhamentos')]



	output = ''

	facebooktoexcel('A')

	curtidas = Tudo[Tudo.index('ComecouComentarios'):]



	facebooktoexcel('B')

	curtidas = Tudo[Tudo.index('ComecouCompartilhamentos'):Tudo.index('ComecouComentarios')]

	print('\n\n' + curtidas + '\n\n')

	facebooktoexcel('C')



	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, output)
	win32clipboard.CloseClipboard()

	print(output)

	double_key('alt','tab')


	return output
