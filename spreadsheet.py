from __future__ import print_function
import random
import socket
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from datetime import datetime, timedelta
  

from google.oauth2 import service_account

import sys


board_number = int(sys.argv[1])
Time_slot = int(sys.argv[2])
# board_number = 1
# Time_slot = 1030

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1GuaqLoDwsyotEE5NJult8vJgiKjAIqfGRamyRvB5apc'


day = (datetime.now()).strftime('%a')
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=day + "!C3:O50").execute()
values = result.get('values', [])


slot_id = 2*(int(int(Time_slot)/100))

if(Time_slot%100 == 30):
    slot_id +=1

email = values[slot_id][int(board_number)-1]

ip_addr = socket.gethostbyname(socket.gethostname())
ip = int(ip_addr[ip_addr.rindex(".")+1:])


date = int(str(time.localtime(time.time())[2]) + str(time.localtime(time.time())[1]))

random.seed(slot_id + ip + date)

port = str(random.randint(49152,65535))

body = "Your IP Address is: " +   ip_addr + " and the port No is " + port

file1 = open(r"port.txt","w+")

file1.write(port)

file2 = open(r"rec_email.txt","w+")
if(email == ""):
    file2.write("anmol19147@gmail.com")
else:
    file2.write(email)

file3 = open(r"email.txt","w+")

file3.write(body)

if(Time_slot==0):
    dateee = (datetime.now() + timedelta(6)).strftime('%A %d-%b-%Y')
    day = (datetime.now()+ timedelta(6)).strftime('%a')
    values = [
        [
        "Fill slots for : " + dateee 
        ],

    ]
    body = ***REMOVED***
        'values': values
  ***REMOVED***
    result = service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=day + "!A1",
        valueInputOption="USER_ENTERED", body=body).execute()
    print('***REMOVED***0} cells updated.'.format(result.get('updatedCells')))

    values = [
        [
        "" 
        ]*12,
        
    ]*48
    body = ***REMOVED***
        'values': values
  ***REMOVED***
    result = service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=day + "C3:O49",
        valueInputOption="USER_ENTERED", body=body).execute()
    print('***REMOVED***0} cells updated.'.format(result.get('updatedCells')))


