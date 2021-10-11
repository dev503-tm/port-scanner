#Tool Coded By dev503-tm 
#pip3 install colorama
from colorama import Fore, Back
import os, re, sys
from threading import Thread
from socket import error, socket, gethostbyname
#def 
open_ports = []

def scan(ip, port):
    sock = socket()
    sock.settimeout(0.1)
    try:
        sock.connect((ip, port))
        print(f'{Fore.BLUE}[*] {Fore.WHITE}{host}:{port}\t\t\t\t{Fore.LIGHTGREEN_EX}OPEN')
        open_ports.append(port)
    except error:
        pass

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# banner
banner = f"""{Fore.GREEN}
 ____            _     ____
|  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __
| |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
|  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |
|_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|
                ***dev503-tm(2021)***
                
{Fore.BLUE}[*] {Fore.WHITE}Fast Port Scanner Tool Coded By devloper503
{Fore.BLUE}[*] {Fore.WHITE}Github https://github.com/dev503-tm"""
print(banner)
host = re.search('(https?\://)?([^/]*)/?.*', 
input(f'{Fore.BLUE}[+] {Fore.WHITE}EnterIP To Start Scan $ {Fore.LIGHTBLUE_EX}')
).group(2)
try:
    ip = gethostbyname(host)
    print(f'{Fore.BLUE}[*] {Fore.WHITE}IP Address : {Fore.LIGHTBLUE_EX}{ip}')
except:
    print(f'{Fore.BLUE}[!] {Fore.WHITE}Invalid Hostname Or IP\n')
    sys.exit()
print(f'{Fore.BLUE}[*] {Fore.WHITE}Scan Started...')
ports = range(65535)
for port in ports:
    try:
        thread = Thread(target=scan, args=(host, port))
        thread.start()
        thread.join()
    except KeyboardInterrupt:
        print(end='\n')
        sys.exit()
print(f'{Fore.BLUE}[*] {Fore.WHITE}Scan Finished')
print(f'{Fore.BLUE}[*] {Fore.WHITE}Open Ports : {Fore.YELLOW}{len(open_ports)}')
