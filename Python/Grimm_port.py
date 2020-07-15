# !/user/bin/python3
# The program fetches the SSH banner, as shown below.


import socket
import re

s = socket.socket()
s2 = socket.socket()


def singlePort(ip, port):
    try:
        s.connect((ip, int(port)))
        s.settimeout(5)
        res = s.recv(1024).decode()
        if len(res) > 10:
            print(res)
            temp = re.findall(r'\d+', res) 
            resp = list(map(int, temp)) 
            print("response: ", resp)
            
            newport = ""
            for num in resp:
                if len(str(num)) >=5:
                    newport = num
                    print("numm", num)

            # numbers = []
            # for word in res.split():
            #     if word.isdigit():
            #         numbers.append(int(word))
            # print("all numbers in response are: ",numbers)
            # new = ""
            # # newport2 = [res[41], res[42], res[43], res[44], res[45]]
            # for y in num: #newport2:
            #     new += y  

            # print("new port is: ",new)
            s.close()
            # # print(ip)
            # # print(new)
            print(int(newport))

            s2.connect((ip, int(newport)))
            s2.settimeout(5)
            # print(resp1, resp2, resp3, resp4, resp5)
            newresp = s2.recv(1024).decode()
            print(newresp)
            s2.close()
        else:
            print(str(s.recv(1024)).strip('b'))
            s.close()
    except socket.error as err:
        print(err)
        


def portRange(ip, port1, port2):
    for x in range(int(port1), int(port2)+1): 
        print(x)
        try:
            s.connect((ip, x))
            s.settimeout(5)
            print(x, s.recv(1024).decode()) #.strip('b')
            s.close()
        except socket.error as err:
            print(err)
    # s = socket.socket()
    # s.connect((ip,int(port)))
    # s.settimeout(5)
    # print(str(s.recv(1024)).strip('b'))


        

def main():
    print("This will be a banner graber based on port or port range.")
    ip = input("Please enter the IP: ")
    option = input("Will this be a port or port range? Enter 'single' or 'range': ")
    if option == 'single':
        port = str(input("Please enter the port: "))
        singlePort(ip, port)
    elif option == 'range':
        port1 = str(input("Please enter the starting port: "))
        port2 = str(input("Please enter the ending port: "))
        portRange(ip, port1, port2)
    else:
        print("invalid input. Please restart and retry")

main()