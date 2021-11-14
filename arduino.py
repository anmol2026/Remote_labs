import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
import sys
import time
time.sleep(3)
arduino.write(bytes('0', 'utf-8'))

