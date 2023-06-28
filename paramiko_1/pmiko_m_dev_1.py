#! https://blog.wimwauters.com/networkprogrammability/2020-03-23-paramiko_introduction_part1/
import paramiko
from connection import get_connection
import time

devices = {
   'iosxe1': {
      'ip': 'sandbox-iosxe-recomm-1.cisco.com',
      'username': 'developer',
      'password': 'lastorangerestoreball8876',
      'port': '22'
      },
   'iosxe2': {
      'ip': 'sandbox-iosxe-recomm-1.cisco.com',
      'username': 'developer',
      'password': 'lastorangerestoreball8876',
      'port': '22'
      }
   }

command = 'show ip interface brief \n'

for device in devices.keys(): 
   print(f"Executing on device: {devices[device]['ip']}\n\n")
   ssh = get_connection(host=devices[device]['ip'], username=devices[device]['username'], password=devices[device]['password'], port=devices[device]['port'])
   stdin, stdout, stderr = ssh.exec_command(command)
   output = stdout.readlines()

   print(' '.join(map(str, output)))