from configparser import ConfigParser, ExtendedInterpolation
import os
def update_config(ip, path, machine_name):
    for file in os.listdir('./config'):
        if file.endswith('.ini'):
            #print(f'[*] Updating {file}')
            config = ConfigParser(interpolation=ExtendedInterpolation())
            config.read(f"./config/{file}")
            config['General']['IP'] = ip
            config['General']['Path'] = path
            config['General']['machine'] = machine_name
            with open(f"./config/{file}", 'w') as configfile:
                config.write(configfile)
            #print(f'[+] Updated {file}')
