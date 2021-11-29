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

# Assigning counter
counter = 1

# initialing a while loop which runs every 10 seconds
while(True):

    # Reading data from Spreadsheet for Slot_id
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range="Sheet9!F:F").execute()
    values = result.get('values', [])

    # Reading data from Spreadsheet for Email Id's
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range="Form!B:B").execute()
    mail_id = result.get('values', [])
    
    #Assining x as number of entries 
    x = len(mail_id)-1

    # Assiging s, s1, s2 as Slot id's for board 1 , 2 and 3 respectively
    s = str(values[counter][0])
    s1 = s.replace("C","D")
    s2 = s.replace("C","E")

    # Assinging s3 as the the address of row in which we need to write
    s3 = s + ':Z'+s[-1] 
    
    # If new entry is available then entring the updating the sheet
    if(s.find("!")==3):

        # Reading data from Spreadsheet for any existing entry
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=s3).execute()
        avail = result.get('values', [])
        
        # if an entry is not present for Board 1 the writing for Board 1
        if(avail[0][0] == ""):
            values = [
                [
                    mail_id[counter][0]
                ]
                
            ]
            body = ***REMOVED***
                'values': values
          ***REMOVED***
            result = service.spreadsheets().values().update(
                spreadsheetId=SPREADSHEET_ID, range=s,
                valueInputOption="USER_ENTERED", body=body).execute()
            print('***REMOVED***0} cells updated.'.format(result.get('updatedCells')))
            counter+=1
        
         # if an entry is present for Board 1 but not for Board2 then writing for Board 2
        elif(avail[0][1] == ""):
            values = [
                [
                    mail_id[counter][0]
                ]
                
            ]
            body = ***REMOVED***
                'values': values
          ***REMOVED***
            result = service.spreadsheets().values().update(
                spreadsheetId=SPREADSHEET_ID, range=s1,
                valueInputOption="USER_ENTERED", body=body).execute()
            print('***REMOVED***0} cells updated.'.format(result.get('updatedCells')))
            counter+=1

        # if an entry is present for Board 1 and 2 but not for Board 3 then writing for Board 3
        elif(avail[0][2] == ""):
            values = [
                [
                    mail_id[counter][0]
                ]
                
            ]
            body = ***REMOVED***
                'values': values
          ***REMOVED***
            result = service.spreadsheets().values().update(
                spreadsheetId=SPREADSHEET_ID, range=s2,
                valueInputOption="USER_ENTERED", body=body).execute()
            print('***REMOVED***0} cells updated.'.format(result.get('updatedCells')))
            counter+=1
        else:
            counter+=1
    
    # assinging 10 second delay to while loop
    time.sleep(10)
    