#! https://blog.wimwauters.com/networkprogrammability/2020-03-23-paramiko_introduction_part1/
import paramiko
import time

host = 'sandbox-iosxe-recomm-1.cisco.com'
username = 'developer'
password = 'lastorangerestoreball8876'
port = 22

command = 'show ip interface brief \n'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host,username=username,password=password,port=port,look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh.exec_command(command)
output = stdout.readlines()
print(' '.join(map(str, output)))
