from Tkinter import *
import socket 
import threading
from threading import Thread

def secondwindow():
	global name1
	name1 = str(name.get("1.0",END)).strip()
	
	
	window1.destroy()
	def receive():
		while True:
			message,address=s.recvfrom(1024)
			T.insert(END,message)
			


	def sendToServer():
		global name1
		a = T1.get("1.0",END)

		if a!="":
			T1.delete("1.0", END)
			
			
			         
			host = "localhost" 
			port = 12384
			s.connect((host, port))
			s.send(name1+":"+a)
			Thread(target = receive).start()	
		else:
			return

	
	
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	root = Tk()
	T = Text(root, height=12, width=80)
	T.pack()
	T1 = Text(root, height=1, width=80)
	T1.pack()
	B = Button(root,text="Send",borderwidth = 1,command=sendToServer)
	B.pack()
	mainloop()

name1=""
window1 = Tk()
window1.geometry('400x400')
name = Text(window1, height=2, width=50)
name.pack()
submit = Button(window1,text="Send",borderwidth = 1,command=secondwindow)
submit.pack()
mainloop()




    
