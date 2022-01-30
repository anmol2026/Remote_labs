from __future__ import print_function
import random
import socket
import sys
import time
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

brd_count = int(sys.argv[1])
limit = int(sys.argv[2])

# Assigning counter
counter = 1

def limitCheck(mail,limit):
    global counter
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range="Sheet9!L:M").execute()
    values = result.get('values', [])
    Dict_value = {}
    for i in range(1, 100):
        Dict_value[values[i][0]] = int(values[i][1])

    if (Dict_value[mail] < limit):
        print(str(counter) + " " +mail + " updated as no. of entries are " + str(Dict_value[mail]))
        return True
    else:
        print(str(counter) + " " +mail + " not updated as no. of entries are " + str(Dict_value[mail]))
        counter += 1
        return False


# initialing a while loop which runs every 10 seconds
while (True):
    print(datetime.now())
    try:
        # Reading data from Spreadsheet for Slot_id
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range="Sheet9!F:F").execute()
        values = result.get('values', [])

        # Reading data from Spreadsheet for Email Id's5
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range="Form!B:B").execute()
        mail_id = result.get('values', [])

        # Assining x as number of entries
        x = len(mail_id) - 1

        # Assiging s, s1, s2 as Slot id's for board 1 , 2 and 3 respectively
        s = str(values[counter][0])

        cells = {}

        for i in range(brd_count):
            cells[i] = s[0:4] + chr(ord('C') + i) + s[5:]
            print(cells[i])

        # Assinging s3 as the the address of row in which we need to write
        s3 = s + ':Z' + s[5:]

        # If new entry is available then entring the updating the sheet
        if (s.find("!") == 3 and limitCheck(mail_id[counter][0],limit)):

            # Reading data from Spreadsheet for any existing entry
            result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                        range=s3).execute()
            avail = result.get('values', [])

            # if an entry is not present for Board 1 then writing for Board 1
            updt = False 
            for i in range(brd_count):
                if (avail[0][i] == ""):
                    values = [
                        [
                            mail_id[counter][0]
                        ]

                    ]
                    body = {
                        'values': values
                    }
                    result = service.spreadsheets().values().update(
                        spreadsheetId=SPREADSHEET_ID, range=cells[i],
                        valueInputOption="USER_ENTERED", body=body).execute()
                    print('{0} cells updated.'.format(result.get('updatedCells')))
                    counter += 1
                    updt = True
                    break;
            
            if(updt==False):
                counter+=1


        # assinging 5 second delay to while loop
        time.sleep(5)
    except Exception as e:
        print(e);
        print(datetime.now())
