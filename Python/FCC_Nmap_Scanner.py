# !/user/bin/python3
# To get this to work properly you must have Python-nmap module installed and namp installed on the computer.

import nmap

scanner = nmap.PortScanner()


print("Welcome to my simple Nmap automation tool.")
print(":-------------------------------------------")

ip_address = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_address)
type(ip_address)

resp = input("""\nPlease enter the type of scan you want to run
                1. SYN ACK Scan
                2. UDP Scan
                3. Comprehensive Scan\n
                ::""")
print("You selected option: ", resp)


if resp == '1':
    print("Nmap versionL ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())
elif resp == '2':
    print("Nmap versionL ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())
elif resp >= '4':
    print("Please enter a valid option")
