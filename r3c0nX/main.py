import os
import sys
import subprocess
import re
import argparse
import threading
import time
from modules import createFolders, nmapScan, runTools,filterResult, updateConfig

from configparser import ConfigParser, ExtendedInterpolation
config = ConfigParser(interpolation=ExtendedInterpolation())
wellknownservices = ConfigParser(interpolation=ExtendedInterpolation())

class Color:
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    

banner = """

=======================================================
=       ======   =============      ==========   ==   =
=  ====  ===   =   ==========   ==   ==========  ==  ==
=  ====  ==   ===   =========  ====  ==========  ==  ==
=  ===   =======   ====   ===  ====  ==  = =====    ===
=      =======    ====  =  ==  ====  ==     =====  ====
=  ====  =======   ===  =====  ====  ==  =  ====    ===
=  ====  ==   ===   ==  =====  ====  ==  =  ===  ==  ==
=  ====  ===   =   ===  =  ==   ==   ==  =  ===  ==  ==
=  ====  =====   ======   ====      ===  =  ==  ====  =
=======================================================
    -D2Cy 
"""

print(f"{Color.GREEN}{banner}{Color.CYAN}")

argparser = argparse.ArgumentParser()
argparser.add_argument('-p', '--path', help='Path to Create Folders')
argparser.add_argument('-m', '--machine', help='Machine Name/IP')
argparser.add_argument('-i', '--ip', help='Machine IP')

terminal_emulator = "xterm"

args = argparser.parse_args()

if len(sys.argv) < 4:
    print(f'{Color.RED}[-] Not Enough Arguments Passed')
    argparser.print_help()
    sys.exit(1)

config.read('./config/config.ini')
wellknownservices.read('./config/wellknownservices.ini')
threads = []
open_ports = []

def scriptScan():
    for line in open(args.path + '/' + args.machine + '/others/service.log', 'r'):
        service,port = line.split('\t')
        thread = threading.Thread(target=nmapScan.advanced_scan, args=(port, service, args.path, args.machine, args.ip,))
        threads.append(thread)
        thread.start()
        time.sleep(2)

def runToolHelper(service,port):
        config = ConfigParser(interpolation=ExtendedInterpolation())
        config.read(f"./config/{service}.ini")
        print(f'\n\n{Color.YELLOW}List of Available Tools for {service}{Color.RESET}\n')
        tools = config['Tools']
        for tool in tools:
            print(tool+". "+config.get('Tools', tool))
        print(f'\n\n{Color.MAGENTA}[+] Enter Tools to Run on Port  {port} {Color.GREEN} (Ex: 1,2 ) (Enter 0 to exit) :', end='')
        tools = input()
        if tools == '0':
            return
        for tool in tools.split(','):
            tool = tool.strip()
            cmd = config.get('Tools', tool)
            try:
                thread = threading.Thread(target=runTools.run_tools, args=(cmd,))
                threads.append(thread)
                thread.start()
                time.sleep(2)
            except:
                print(f'{Color.RED}[-] Invalid Tool{Color.RESET}')
        
def main():
    updateConfig.update_config(args.ip, args.path, args.machine) # Update Config Files
    createFolders.create_folders(path=args.path, machine=args.machine)  # Create Folders
    print(f'{Color.CYAN}[+] Running NMAP Scan\n\n{Color.RESET}') 
    nmapScan.nmap_scan(path=args.path, machine=args.machine, ip=args.ip) # Run NMAP Scan
    print(f'{Color.CYAN}[+] Filtering Well Known Ports\n\n ')
    filterResult.filter_well_known_ports(path=args.path, machine=args.machine) # Filter Well Known Ports and Run NMAP Scripts
    print(f'{Color.CYAN}[+] Running NMAP Scripts\n\n')
    scriptScan()
    print(f'{Color.CYAN}[+] Running Tools on Well Known Services\n\n') 
    file = open(args.path + '/' + args.machine + '/others/service.log', 'r')
    for line in file:
        service,ports = line.split('\t')
        # print(ports)
        if service == 'smb':
            ports = ports.strip()
            runToolHelper(service,ports)
        else:
            for port in ports.split(','):
                port = port.strip()
                config = ConfigParser(interpolation=ExtendedInterpolation())
                try:
                    config.read(f"./config/{service}.ini")
                    config['General']['port'] = port
                    with open(f"./config/{service}.ini", 'w') as configfile:
                        config.write(configfile)
                    runToolHelper(service,port)
                except:
                    print(f'{Color.RED}[-] Config File Not Found{Color.RESET}')
                # with open('config.ini', 'w') as configfile:
                #     config.write(configfile)
                

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()






