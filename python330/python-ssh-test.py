from paramiko import SSHClient
from paramiko.client import AutoAddPolicy
import getpass #sudo pip3.6 install getpass

hostname = input("Enter hostname or IP: ")
user_name = input("Enter username: ")
passwd = getpass.getpass("Enter password: ")
cmd = input("Enter command to execute: ")

def connect():
    with SSHClient() as client:
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(hostname,username=user_name,password=passwd) #key_file=/root/.ssh/id_rsa
        stdin, stdout, stderr = client.exec_command(cmd)
        print(stdin)
        print(stdout.read())
        print(stderr.read())

connect()
