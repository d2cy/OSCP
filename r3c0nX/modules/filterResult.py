import xml.etree.ElementTree as ET
from configparser import ConfigParser, ExtendedInterpolation
import re
config = ConfigParser(interpolation=ExtendedInterpolation())
wellknownservices = ConfigParser(interpolation=ExtendedInterpolation())

# config.read('config.ini')
wellknownservices.read('./config/wellknownservices.ini')

def filter_well_known_ports(path, machine):
    xml_data = open(path + '/' + machine + '/enumeration/nmap.xml', 'r')
    root = ET.fromstring(xml_data.read())
    file = open(path + '/' + machine + '/others/service.log', 'w')
    for keys in wellknownservices['WellKnownServices']:
        pattern = re.compile(wellknownservices['WellKnownServices'][keys])
        ports = []
        for host in root.findall(".//host"):
            for port in host.findall(".//port"):
                service_name = port.find(".//service").get("name")
                if pattern.match(service_name):
                    ports.append(port.get("portid"))        
            if ports != []:
                file.write(keys + '\t' + ','.join(ports) + '\n')          
    file.close()
