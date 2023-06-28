#! https://blog.wimwauters.com/networkprogrammability/2020-03-24-paramiko_introduction_part2/
import paramiko
from connection import get_connection

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

def main():
    print('Performing task')
    get_description(devices)

if __name__ == "__main__":
    # will trigger invoke
    # https://towardsdatascience.com/python-main-b729fab7a8c3#:~:text=What%20is%20the%20purpose%20of,__name__%20will%20vary.
    main()

