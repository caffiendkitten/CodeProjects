# A socket is an endpoint for sending and receiving data
# !/user/bin/python3

import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.2.41'
host = socket.gethostname() # Host is the server IP
port = 444 # Port to listen on 

# serversocket.bind((host, port)) # Host will be replaced/substitued with IP, if changed and not running on host
serversocket.bind(('192.168.2.41', port))

serversocket.listen(3)

while True:
    #Starting the connection 
    clientsocket, address = serversocket.accept()
    print("Received connection from: %s " % str(address) )
    
    #Banner Message sent to client after successful connection
    message = "thanks for connecting to the server\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()



