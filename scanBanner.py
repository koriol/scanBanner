


#!/usr/bin/python
# Input host IPv4 to scan if specified ports are open or closed

import socket
from termcolor import colored

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("[+] Enter a host to scan: ") #"192.168.1.7" format
port = int(input("[+] Enter a port to scan: ")) #445

def portScan(port):
    if socket.connect_ex((host, port)):
        print(colored(f"[!!] Port {port} on {host} is closed", 'red'))
    else:
        print(colored(f"[+] Port {port} on Host {host} is open", 'green'))

def retBanner(host, port):
    try:
        socket.setdefaulttimeout(2)
        sock = socket.socket()
        sock.connect((host, port))
        banner = sock.recv(1024)
        return banner
    except:
        return
    
def main():
    portScan(port)
    banner = retBanner(host, port)
    if banner:
            print(colored(f'[+] Port {str(port)} at host {host} returns: {str(banner)}', 'green')) # + str(port) + ' at host ' + ip + " returns: " + str(banner)))
        

main()