# !/usr/bin/python3
# A simple port scanner in Python that will ask the user what url and what port they want to check if open
# 

import socket


def portScanner(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((host, int(port))):
        print("The port is closed")
    else:
        print("The port is open")

def main():
    host = input("Please enter the IP you want to scan: ")
    port = input("Please enter the port you want to scan: ")
    portScanner(host, port)


main()