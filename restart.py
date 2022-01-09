from __future__ import print_function
import paramiko
from scp import SCPClient
import time
import random
import socket
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from datetime import datetime, timedelta
from google.oauth2 import service_account



# Reading service account file
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1GuaqLoDwsyotEE5NJult8vJgiKjAIqfGRamyRvB5apc'

day = (datetime.now()).strftime('%a')
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

counter = 1
# initialing a while loop which runs every 10 seconds
while (True):
    print(datetime.now())
    try:
        # Reading data from Spreadsheet for Slot_id
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range="Restart!B:E").execute()
        values = result.get('values', [])

        # Assining x as number of entries
        x = len(values) - 1

        

        # If new entry is available then entring the updating the sheet
        if (counter<=x):
            mail = str(values[counter][0])
            
            ip_addr = str(values[counter][2])

            port_inp = int(values[counter][3])
        
            h = int(time.localtime(time.time())[3])
            m = int(time.localtime(time.time())[4])

            Time_slot = 0
            if(m<30):
                Time_slot = h*100
            else:
                Time_slot = h*100 + 30

            print(Time_slot)


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
            port = int(random.randint(49152,65535))

            if(port==port_inp):
                # declaring SSH VM credentials
                host = ip_addr
                username = ''
                password = ''

                # connect to server
                con = paramiko.SSHClient()
                con.load_system_host_keys()
                con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                con.connect(host, username=username, password=password)


                # execute the script
                stdin, stdout, stderr = con.exec_command('python E:\Remote_labs\\arduino.py')

                # printing the output of command
                print(stderr.read())
                print(str(stdout.read()))

                if stderr.read() == b'':
                    print('Success')
                else:
                    print('An error occurred')
        counter +=1;



        time.sleep(5)
    except Exception as e:
        print(e);
        print(datetime.now())
