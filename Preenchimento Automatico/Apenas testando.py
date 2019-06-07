import pyautogui, sys
from Print_da_Tela import *



def alt_tab_to_chrome(a,b,c):
	pyautogui.keyDown('alt')
	pyautogui.press('tab')

	c_x, c_y = dar_coordenadas_cor_print(220,76,64)

	pyautogui.click(c_x,c_y + 40, duration = 0.2)

	pyautogui.keyUp('alt')