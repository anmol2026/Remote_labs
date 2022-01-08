import serial 
import time
import sys
import time

# serial writing '0' to restart board
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)
time.sleep(3)
arduino.write(bytes('0', 'utf-8'))
print("Board Restarting")

