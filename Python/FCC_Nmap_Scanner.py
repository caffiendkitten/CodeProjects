# !/user/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome to my simple Nmap automation tool.")
print(":-------------------------------------------")

ip_address = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_address)
type(ip_address)




