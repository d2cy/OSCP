# module/createFolders.py

import os

def create_folders(path, machine):
    try:
        os.mkdir(path + '/' + machine)
        os.mkdir(path + '/' + machine + '/enumeration')
        os.mkdir(path + '/' + machine + '/exploits')
        os.mkdir(path + '/' + machine + '/notes')
        os.mkdir(path + '/' + machine + '/screenshots')
        os.mkdir(path + '/' + machine + '/others')
        print('[+] Folders Created Successfully')
    except:
        print('[-] Error Creating Folders')
