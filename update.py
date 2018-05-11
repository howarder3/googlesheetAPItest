# update.py
import time

def update_sheet(gss_client, key, today, item, price):
    wks = gss_client.open_by_key(key)
    sheet = wks.sheet1
    sheet.insert_row([today, item, price], 2)

spreadsheet_key = 19nQvlQIGRIoGELFxGfHWazG45DM7D2GccZg8wlD85_g	
# spreadsheet_key_path = 'spreadsheet_key'


today = time.strftime("%c")
# with open(spreadsheet_key_path) as f:
#    spreadsheet_key = f.read().strip()
update_sheet(gss_client, spreadsheet_key, today, "cheapest_item","cheapest_price")