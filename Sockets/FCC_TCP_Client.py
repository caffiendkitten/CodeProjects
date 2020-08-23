# !/user/bin/python3

import socket

#Creating the socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = 'x.x.x.x'
host = socket.gethostname()

port = 444 

# clientsocket.connect((host, port))
clientsocket.connect(('x.x.x.x', port)) # You can substitue the host with the server IP


# Receiving a maximum of 1024 bytes
message = clientsocket.recv(1024)

clientsocket.close()

print (message.decode('ascii'))