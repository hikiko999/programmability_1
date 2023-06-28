#! https://blog.wimwauters.com/networkprogrammability/2020-03-24-paramiko_introduction_part2/
import paramiko
from connection import get_connection

def get_description(devices):
    host = 'ios-xe-mgmt-latest.cisco.com'
    username = 'developer'
    password = 'lastorangerestoreball8876'
    port = 22

    command = 'show interface description \n'

    for device in devices.keys(): 
        print(f"Executing on device: {devices[device]['ip']}\n\n")
        ssh = get_connection(host=devices[device]['ip'], username=devices[device]['username'], password=devices[device]['password'], port=devices[device]['port'])
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.readlines()
        newoutput = ' '.join(map(str, output))
        print(newoutput)