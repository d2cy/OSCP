import subprocess
import sys
terminal_emulator = "xterm"

def run_tools(command):
    try:
        command_parts = command.split(" ")
        command_parts.insert(0, terminal_emulator)
        command_parts.insert(1, '-hold')
        command_parts.insert(2, '-e')
        subprocess.Popen(command_parts)
    except:
        print('[-] Error Running Tool')
        sys.exit(1)
