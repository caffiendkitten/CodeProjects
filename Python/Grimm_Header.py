# !/user/bin/python3

# Learn Python HTTP Methods.
# This will show an HTTP banner/headers


import socket
s = socket.socket()
s.settimeout(2)


def scan(ip, port):

    target = 'target1.bowneconsulting.com'
    s.connect((ip, int(port)))
    # s.connect((target, 80))
    req = 'HEAD / HTTP/1.1\r\nHost: ' + target + '\r\n\r\n'
    s.send(req.encode())
    print(s.recv(1024).decode())
    s.close()


def main():
    print("This will be a HTTP banner/header graber based on port")
    ip = input("Please enter the IP: ")
    port = str(input("Please enter the port: "))
    scan(ip, port)
        
    # option = input("Will this be a port or port range? Enter 'single' or 'range': ")
    # if option == 'single':
    #     port = str(input("Please enter the port: "))
    #     singlePort(ip, port)
    # elif option == 'range':
    #     port1 = str(input("Please enter the starting port: "))
    #     port2 = str(input("Please enter the ending port: "))
    #     portRange(ip, port1, port2)
    # else:
    #     print("invalid input. Please restart and retry")

main()