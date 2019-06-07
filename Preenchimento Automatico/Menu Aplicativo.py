from Coletar_dados_Facebook import Coletar_Facebook
from Coletar_dados_Instagram import Coletar_Instagram
from Coletar_dados_Linkedin import Coletar_Linkedin
from win32api import GetSystemMetrics
from tkinter import *
from math import *

def clickar(event):
	if event.x < 125 and event.x > 25 and event.y < 125 and event.y > 25:
		print('Executar função coletar facebook')
		Coletar_Facebook()
	if event.x < 325 and event.x > 225 and event.y < 125 and event.y > 25:
		print('Executar função coletar instagram')
		Coletar_Instagram()
	if event.x < 525 and event.x > 425 and event.y < 125 and event.y > 25:
		print('Executar função coletar linkedin')
		Coletar_Linkedin()
	#if event.x < 250 and event.x > 50 and event.y < 325 and event.y > 225:
	#	print('Executar função coletar facebook e depois instagram')
	#	data_fb = Coletar_Facebook()
	#	data_ig = Coletar_Instagram()
	#
	#	print(data_fb + "\n \t" + data_ig)

root=Tk()
frame=Frame(root,width=400,height=400)
frame.grid(row=0,column=0)
canvas=Canvas(frame,bg='#FFFFFF',width= GetSystemMetrics(0),height= GetSystemMetrics(1),scrollregion=(0,0,1200,1200))
hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width= GetSystemMetrics(0),height=  GetSystemMetrics(1))
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)



canvas.bind('<Button>', clickar)



Logo_fb = PhotoImage(file = "Facebook_logo.png")
canvas.create_image(75,75, image = Logo_fb)
canvas.create_text(75,150, text = "Coletar dados do Facebook")

Logo_ig = PhotoImage(file = "Instagram_logo.png")
canvas.create_image(275,75, image = Logo_ig)
canvas.create_text(275,150, text = "Coletar dados do Instagram")

Logo_li = PhotoImage(file = "Linkedin_logo.png")
canvas.create_image(475,75, image = Logo_li)
canvas.create_text(475,150, text = "Coletar dados do Linkedin")

#ig_fb = PhotoImage(file = "Fb_Ig.png")
#canvas.create_image(150,275, image = ig_fb)
#canvas.create_text(150,350, text = "Coletar dados do Instagram e do Facebook")


root.mainloop()
