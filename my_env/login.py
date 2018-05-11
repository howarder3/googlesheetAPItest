import gspread

from oauth2client.service_account import ServiceAccountCredentials

def auth_gss_client(path, scopes):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(path,scopes)
    return gspread.authorize(credentials)

auth_json_path = 'auth.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']

gss_client = auth_gss_client(auth_json_path, gss_scopes)

# update.py
import time

def update_sheet(gss_client, key, today, item, price):
    wks = gss_client.open_by_key(key)
    sheet = wks.sheet1
    sheet.insert_row([today, item, price], 2)

spreadsheet_key = "19nQvlQIGRIoGELFxGfHWazG45DM7D2GccZg8wlD85_g"


today = time.strftime("%c")
update_sheet(gss_client, spreadsheet_key, today, "cheapest_item","cheapest_price")