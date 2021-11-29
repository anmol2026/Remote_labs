import paramiko
import socket
from scp import SCPClient
import sys
import random
import socket
import time


# taking inputs from user
board_number = int(sys.argv[1])
Time_slot = int(sys.argv[2])
ip_addr = socket.gethostbyname(socket.gethostname());

# Creating slot id from time slot
slot_id = 2*(int(int(Time_slot)/100))
if(Time_slot%100 == 30):
    slot_id +=1

# getting last byte of ip address of the machine 
ip = int(ip_addr[ip_addr.rindex(".")+1:])

# storing todays date in DDMM format
date = int(str(time.localtime(time.time())[2]) + str(time.localtime(time.time())[1]))

# generating random port number as a function of slot id, ip and date
random.seed(slot_id + ip + date)
port = str(random.randint(49152,65535))

# writing port number to text file
file1 = open(r"port.txt","w+")
file1.write(port)

# declaring SSH VM credentials
host = ''
username = ''
password = ''

# connect to server
con = paramiko.SSHClient()
con.load_system_host_keys()
con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
con.connect(host, username=username, password=password)


# execute the script
stdin, stdout, stderr = con.exec_command('cd "/home/iiitd/BTP_Scripts"; pwd; python3 spreadsheet.py ' + str(board_number) + ' ' + str(Time_slot) + ' '+ str(ip_addr) + '; '+ 'python3 gmail.py')

# printing the output of command
print(stderr.read())
print(str(stdout.read()))

if stderr.read() == b'':
    print('Success')
else:
    print('An error occurred')

