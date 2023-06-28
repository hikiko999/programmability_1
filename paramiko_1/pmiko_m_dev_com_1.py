#! https://blog.wimwauters.com/networkprogrammability/2020-03-23-paramiko_introduction_part1/

import paramiko
from connection import get_connection
import time

commands = ['show version\n', 'show run\n']

max_buffer = 65535
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

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)

for device in devices.keys():
    
    connection = get_connection(host=devices[device]['ip'], username=devices[device]['username'], password=devices[device]['password'], port=devices[device]['port'])
    new_connection = connection.invoke_shell()
    # uses shell, for multi
    output = clear_buffer(new_connection)
    time.sleep(2)
    new_connection.send("terminal length 0\n")
    output = clear_buffer(new_connection)
        
    # writes to file
    for command in commands:
        outputFileName = device + '_' + command.replace('\n','_') + 'output.txt'
        # https://www.freecodecamp.org/news/how-to-remove-a-specific-character-from-a-string-in-python
        with open(outputFileName, 'wb') as f:
            print(f"Executing command {command}")
            new_connection.send(command)
            time.sleep(2)
            output = new_connection.recv(max_buffer)
            f.write(output)
            
    new_connection.close()