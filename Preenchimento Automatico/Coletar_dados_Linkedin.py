import pyautogui, sys
import time
import win32clipboard
import win32con
import numpy as np
from Print_da_Tela import *

Tudo = ''
output = ''
curtidas = ''

def Coletar_Linkedin():
	global curtidas, output, Tudo

	def alt_tab_to_chrome(a,b,c, extra, alttab):
		if alttab:
			pyautogui.keyDown('alt')
			pyautogui.press('tab')


		c_x, c_y = dar_coordenadas_cor_print(a,b,c,0)

		pyautogui.click(c_x,c_y + extra, duration = 0.2)

		pyautogui.keyUp('alt')

	def facebooktoexcel(letra):
		global curtidas, output

		prefix = "\\r\\n"


		if prefix + "Ana Beatriz Farias" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Beatriz Mendon\\xc3\\xa" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Bianca Souza" in curtidas:
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

		if prefix + "Giovanny Oliveira" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Jo\\xc3\\xa3o Vinicius Santiago" in curtidas:
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

		if prefix + "Izabele Vit\\xc3\\xb3ria Oliveira Leite" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if prefix + "Julia Vieira" in curtidas:
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

	alt_tab_to_chrome(220,76,64, 40, True)
	alt_tab_to_chrome(0,114,177, 0, False)

	# Clickar na caixa de likes

	c_x, c_y = dar_coordenadas_cor_print(27 , 132 , 187, 0)
	pyautogui.click(c_x,c_y, duration = 0.2)

	# Selecionar curtidas

	pyautogui.moveTo(536,205, 0.5)
	pyautogui.mouseDown(button='left')
	pyautogui.moveTo(1050, 750, 0.2)
	time.sleep(5)
	pyautogui.mouseUp(button='left')

	double_key('ctrl', 'c')

	time.sleep(0.2)

	win32clipboard.OpenClipboard()
	novo = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
	Tudo = Tudo + ' ComecouCurtidas: ' + novo 
	win32clipboard.CloseClipboard()

	# Fechar caixa de curtidas

	pyautogui.click(1240,600, duration = 0.2)


	# Abrir comentarios

	pyautogui.click(c_x + 90,c_y, duration = 0.2)
	time.sleep(0.5)
	pyautogui.click(c_x + 90,c_y, duration = 0.2)

	# Selecionar comentarios

	pyautogui.moveTo(c_x - 190,c_y, 0.2)
	pyautogui.mouseDown(button='left')
	pyautogui.moveTo(GetSystemMetrics(0) - 500,c_y, 0.2)

	novo = ''

	# Vai scrollando até o final dos comentários

	while not 'Exibir estat' in novo:
		pyautogui.scroll(-50)
		double_key('ctrl', 'c')

		win32clipboard.OpenClipboard()
		novo = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT) 
		win32clipboard.CloseClipboard()


	Tudo = Tudo + "ComecouComentarios" + novo

	pyautogui.mouseUp(button='left')


	### PARTE 2
	### EXTRAÇÃO DE INFORMAÇÕES DA STRING

	Tudo = str(Tudo.encode('utf-8'))

	curtidas = Tudo[:Tudo.index('ComecouComentarios')]

	output = ''

	facebooktoexcel('A')

	curtidas = Tudo[Tudo.index('ComecouComentarios'):]

	facebooktoexcel('B')

	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, output)
	win32clipboard.CloseClipboard()

	print(Tudo)
	print(output)

	double_key('alt','tab')

