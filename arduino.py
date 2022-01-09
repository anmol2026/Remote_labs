import serial 
import sys
import socket
import time

ip_addr = socket.gethostbyname(socket.gethostname());
print("Board Restarting with IP " + ip_addr)

# serial writing '0' to restart board
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)
time.sleep(3)
arduino.write(bytes('0', 'utf-8'))


