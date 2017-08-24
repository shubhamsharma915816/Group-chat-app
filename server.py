import socket               # Import socket module
from threading import Thread


def receive():
	while True:
		message,addr=s.recvfrom(1024)
		connections.add(addr)		
		l.append(addr)
		for i in connections:	
			
			s.sendto(message,i)
		



	
s = socket.socket(socket. AF_INET,socket.SOCK_DGRAM)         
host = "" 
port = 12384 
s.bind((host, port))        
connections = set()
l=[]
Thread(target=receive).start()
