import pyautogui as piu
import time




def gravity():
	g=9.18
	m1=int(piu.prompt("Massa Benda 1"))
	m2=int(piu.prompt("Massa Benda 2"))
	d=int(piu.prompt("Jarak antar Benda ?"))
	time.sleep(3)
	# HUKUM GRAVITASI NEWTON 
	Fgrav=g*((m1*m2)/d**2)
	piu.alert("Gravitasi 2 Benda adalah= "+str(Fgrav))





gravity()
