import pyautogui, sys
import time
import win32clipboard
import win32con
import numpy as np
from Print_da_Tela import *

Tudo = ''
output = ''
curtidas = ''

def Coletar_Instagram():
	global curtidas, output, Tudo
	def facebooktoexcel(letra):
		global curtidas, output, Tudo

		if "biafariasm" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if "beamendon" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if "biancafelipe_" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if "TaynarafasgasgasgaasaswRamalho" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if "ernanematheus7" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if "giovannysdo" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if "joaovinicius5_" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if "pedroppmoura_" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if "juliacrcarvalho" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if ('luizfialhoo_') in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if "manupaiva_" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if "vi_izabele" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if "juliavx" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if "tuizagalganid" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		if "svictorduarte" in curtidas:
			output = output + letra + " \t \t \t"
		else:
			output = output + "\t \t \t" 

		output = output + '\n'

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

	# Abrir o Chrome

	alt_tab_to_chrome(220,76,64, 40, True)
	alt_tab_to_chrome(248,110,42, 0, False)

	# Recarregar  a página

	pyautogui.press('f5')

	time.sleep(4)

	# Selecionar comentários e copiar

	pyautogui.moveTo(1100,400, 0.5)

	double_key('ctrl','a')
	time.sleep(0.5)
	double_key('ctrl','c')
	time.sleep(1)

	win32clipboard.OpenClipboard()
	novo = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
	Tudo = Tudo + 'ComecouComentarios'  + novo
	win32clipboard.CloseClipboard()


	# Ir para o final da pagina (alinhamento)

	pyautogui.moveTo(1400,300, 0.5)
	pyautogui.click(clicks = 1)

	pyautogui.scroll(-10000)

	time.sleep(2)

	# Abrir e copiar caixa de likes

	pyautogui.click(1041,600, duration = 0.5)

	oldtext = 'teste'
	text = ''


	while (oldtext != text):
		# Selecionar e copiar a lista de pessoas

		pyautogui.moveTo(598,314,0.5)
		pyautogui.mouseDown(button='left')
		pyautogui.moveTo(966, 640, 0.5)
		pyautogui.mouseUp(button='left')
		double_key('ctrl','c')

		#Extraindo o ctrl+c e adicionando-o ao total

		win32clipboard.OpenClipboard()
		oldtext = text
		text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
		Tudo = Tudo + ' ComecouCurtidas: ' + text
		win32clipboard.CloseClipboard()

		# Arrasta para baixo, para selecionar novas pessoas

		pyautogui.click()
		pyautogui.scroll(-350)

	print (Tudo.encode("utf-8"))

	Tudo = Tudo.encode('utf-8')
	Tudo = str(Tudo)



	curtidas = Tudo[Tudo.index('ComecouCurtidas'):]

	print(curtidas)


	output = ''

	facebooktoexcel('A')

	curtidas = Tudo[:Tudo.index('ComecouCurtidas')]

	facebooktoexcel('B')


	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, output)
	win32clipboard.CloseClipboard()

	print(output)

	double_key('alt','tab')