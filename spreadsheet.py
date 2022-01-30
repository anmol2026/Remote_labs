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


# taking input from user
board_number = int(sys.argv[1])
Time_slot = int(sys.argv[2])
ip_addr = int(sys.argv[3])
<<<<<<< HEAD
=======
# board_number = 1
# Time_slot = 1030
>>>>>>> parent of 2b3065b (Add files via upload)


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


# Reading data from Spreadsheet
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range=day + "!C3:O50").execute()
values = result.get('values', [])


# Creating slot id from time slot
slot_id = 2*(int(int(Time_slot)/100))

if(Time_slot%100 == 30):
    slot_id +=1

# Reading email address according to slot id 
email = values[slot_id][int(board_number)-1]

# ip_addr = socket.gethostbyname(socket.gethostname())
ip = int(ip_addr[ip_addr.rindex(".")+1:])


# storing todays date in DDMM format
date = int(str(time.localtime(time.time())[2]) + str(time.localtime(time.time())[1]))

# generating random port number as a function of slot id, ip and date
random.seed(slot_id + ip + date)
port = str(random.randint(49152,65535))

# writing body of email
body = "Your IP Address is: " +   ip_addr + " and the port No is " + port

# writing port number to text file
file1 = open(r"port.txt","w+")
file1.write(port)

# writing email address to a text file
file2 = open(r"rec_email.txt","w+")
if(email == ""):
    # if a slot is not booked then writing the file with a default email
    file2.write("anmol19147@gmail.com")
<<<<<<< HEAD
    body = {
        'values': values
    }
    # update the sheet with the port number of slot if slot is not booked
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=day + "C3:O50",
        valueInputOption="USER_ENTERED", body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))

=======
>>>>>>> parent of 2b3065b (Add files via upload)
else:
    # if a slot is booked then writing the file with receivers email
    file2.write(email)

# writing emails body
file3 = open(r"email.txt","w+")
file3.write(body)

# Reseting the sheet for new Day at the end of previous day 
if(Time_slot==0):
<<<<<<< HEAD

    # assinging day and date for new day
    dateee = (datetime.now() + timedelta(6)).strftime('%A %d-%b-%Y')
    day = (datetime.now()+ timedelta(6)).strftime('%a')

=======
    dateee = (datetime.now() + timedelta(6)).strftime('%A %d-%b-%Y')
    day = (datetime.now()+ timedelta(6)).strftime('%a')
>>>>>>> parent of 2b3065b (Add files via upload)
    values = [
        [
        "Fill slots for : " + dateee 
        ],

    ]
    body = {
        'values': values
    }

    # updating the sheet with header of new day
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=day + "!A1",
        valueInputOption="USER_ENTERED", body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))

    # Assining new values as blank sheet
    values = [
        [
        "" 
        ]*12,
        
    ]*48
    body = {
        'values': values
    }
    # writing the sheet with blank values
    result = service.spreadsheets().values().update(
<<<<<<< HEAD
        spreadsheetId=SPREADSHEET_ID, range=day + "C3:O49",
=======
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=day + "C3:O49",
>>>>>>> parent of 2b3065b (Add files via upload)
        valueInputOption="USER_ENTERED", body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))


