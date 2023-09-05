import subprocess
import re
import sys
import threading
import time
from configparser import ConfigParser, ExtendedInterpolation

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read('./config/config.ini')
terminal_emulator = config['General']['terminal']
config.read('./config/nmapscripts.ini')

def advanced_scan(port, service, path, machine, ip):
    try:
        port = port.strip()
        print(f'[+] Running NMAP Scan on port {port} with service {service}\n\n')
        script = config['SCRIPT'][service]
        subprocess.Popen([terminal_emulator, '-hold', '-e', 'nmap', '-Pn', '-vv', '-p' + port, '--script', script, '-oN', path + '/' + machine + '/enumeration/' + port + '.log', ip], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except:
        print('[-] Error Running NMAP Scan')
        sys.exit(1)

def nmap_scan(path, machine, ip):
    try:
        print('[+] Running NMAP Scan')
        nmap = subprocess.Popen(['nmap', '-vv', '-Pn', '-oX', path + '/' + machine + '/enumeration/nmap.xml', ip], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(nmap.stdout.readline, b''):
            print(line.rstrip().decode('utf-8'))
    except:
        print('[-] Error Running NMAP Scan')
        sys.exit(1)

    
