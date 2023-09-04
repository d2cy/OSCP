import os
import sys
import subprocess
import re
import argparse
import threading
import time
from modules import createFolders, nmapScan, runTools,filterResult

from configparser import ConfigParser, ExtendedInterpolation
config = ConfigParser(interpolation=ExtendedInterpolation())
wellknownservices = ConfigParser(interpolation=ExtendedInterpolation())


# Global Variables
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

print(banner)

argparser = argparse.ArgumentParser()
argparser.add_argument('-p', '--path', help='Path to Create Folders')
argparser.add_argument('-m', '--machine', help='Machine Name/IP')
argparser.add_argument('-i', '--ip', help='Machine IP')

terminal_emulator = "xterm"

args = argparser.parse_args()
# Count Number of Arguments Passed
if len(sys.argv) < 4:
    print('[-] Not Enough Arguments Passed')
    argparser.print_help()
    sys.exit(1)



# Read Config File
config = ConfigParser(interpolation=ExtendedInterpolation())

config.read('config.ini')
# Update Config File With IP Address and Path

config['DEFAULT']['ip'] = args.ip
config['DEFAULT']['path'] = args.path
config['DEFAULT']['machine'] = args.machine

with open('config.ini', 'w') as configfile:
    config.write(configfile)

config.read('config.ini')
wellknownservices.read('wellknownservices.ini')
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
    try:
        c = config.get('Tools', service)
        cmds = c.split(':~:')
        print(f'[+] Running Tools for {service} on port {port}\n\n')
        for cmd in cmds:
            thread = threading.Thread(target=runTools.run_tools, args=(cmd,))
            threads.append(thread)
            thread.start()
            time.sleep(1)
    except:
        print(f'[-] Tools for {service} Not Found in Config File')

    

def main():
    createFolders.create_folders(path=args.path, machine=args.machine)  # Create Folders 
    nmapScan.nmap_scan(path=args.path, machine=args.machine, ip=args.ip) # Run NMAP Scan
    print('[+] Filtering Well Known Ports and Running NMAP Scripts\n\n ')
    filterResult.filter_well_known_ports(path=args.path, machine=args.machine) # Filter Well Known Ports and Run NMAP Scripts
    scriptScan()
    print('[+] Running Tools on Well Known Services\n\n') 
    file = open(args.path + '/' + args.machine + '/others/service.log', 'r')
    for line in file:
        service,ports = line.split('\t')
        if service == 'smb':
            runToolHelper(service,ports)
        else:
            for port in ports.split(','):
                port = port.strip()
                config['DEFAULT']['port'] = port
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
                runToolHelper(service,port)

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()





