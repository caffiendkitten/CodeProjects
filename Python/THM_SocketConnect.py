#!/usr/bin/env python
# This code will connect to a socket recursivly while taking the port and the math action in the response  and acting on them

import socket
import re

HOST="10.10.48.236"
PORT = 1337 #gives hint to start at port 1337
num = 0 #instructs us to begin at 0
count = 0
operation = ""
data = ""
while True: #while True, meaning until the port equals 9765, do these actions. infinite loop
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST, int(PORT)))
		print("connected to", HOST,"on port", PORT )

		request = "GET / HTTP/1.0\r\nHost:"+HOST+"\r\n\r\n"
		s.send(request.encode('utf8'))
		if ("STOP" in data) or (PORT == 9765):
			break
		print("Lets change somethin") 
		while True:
			response = s.recv(4096).decode()
			data = response

			if not data:
				break


			newData = data.splitlines()
			newData = newData[-1].split()
			operation = newData[0]
			number = newData[1]
			newPort = newData[2]
			# print("new Datas are: ",operation, number, newPort)

			PORT = newPort
			if(operation == 'add'):
				num += float(number)
			elif(operation == 'minus'):
				num -= float(number)
			elif(operation == 'multiply'):
				num *= float(number)
			elif(operation == 'divide'):
				num /= float(number)
		print("newNEW Datas are: ",operation, number, PORT)
		print("current Num is: ",num)
    				
		s.close()
	except socket.error as err:
		count += 1
		print("#",count) #, "Port 1337 not open:", err)
		s.close()
print("Final Num isssss: ",num)
