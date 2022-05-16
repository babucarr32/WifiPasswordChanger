import os
import subprocess

from subprocess import PIPE
def find_net_device():
    cmd ='netsh interface ipv4 show interfaces'.split()

    result = subprocess.run(cmd, universal_newlines = True,
                            stdout = subprocess.PIPE)                              
    result = result.stdout
    result = result.split('connected')[2]
    result = result.split('\n')[0]
    result = result.strip()
    return result

def change_ip(ip):
    adapter = find_net_device()
    change =f'netsh interface ip set address {adapter} static {ip} 255.255.255.0'
    change = change.split()

change_ip('192.168.1.30')


#again back to normal
def back2normal():
    adapter = find_net_device()
    normal = f'netsh interface ip set address {adapter} dhcp'
    subprocess.run(normal,stdout=PIPE, universal_newlines=True)

