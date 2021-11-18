import paramiko
import socket
from scp import SCPClient

import sys
import random
import socket
import time


board_number = int(sys.argv[1])
Time_slot = int(sys.argv[2])
ip_addr = socket.gethostbyname(socket.gethostname());

slot_id = 2*(int(int(Time_slot)/100))

if(Time_slot%100 == 30):
    slot_id +=1

ip = int(ip_addr[ip_addr.rindex(".")+1:])


date = int(str(time.localtime(time.time())[2]) + str(time.localtime(time.time())[1]))

random.seed(slot_id + ip + date)

port = str(random.randint(49152,65535))

file1 = open(r"port.txt","w+")

file1.write(port)

# declare credentials
host = 'host ip'
username = 'username'
password = 'Enter pass'

# connect to server
con = paramiko.SSHClient()
con.load_system_host_keys()
con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
con.connect(host, username=username, password=password)


# execute the script
stdin, stdout, stderr = con.exec_command('cd "/home/iiitd/BTP_Scripts"; pwd; python3 spreadsheet.py ' + str(board_number) + ' ' + str(Time_slot) + ' '+ str(ip_addr) + '; '+ 'python3 gmail.py')

print(stderr.read())
print(454654)
print(str(stdout.read()))

if stderr.read() == b'':
    print('Success')
else:
    print('An error occurred')
stdin, stdout, stderr = con.exec_command('pwd')
print(stderr.read())
print(stdout.read())

