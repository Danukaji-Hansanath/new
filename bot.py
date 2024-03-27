import os
import requests
from datetime import datetime

def get_file_details(file_path):
    try:
        file_stat = os.stat(file_path)
        file_size = file_stat.st_size  # File size in bytes
        modified_date = file_stat.st_mtime  # Modified timestamp
        return file_size, modified_date
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None, None

def upload_file_to_telegram(token, chat_id, file_path, caption=None, thumbnail_path=None):
    url = f"https://api.telegram.org/bot{token}/sendDocument"
    files = {'document': open(file_path, 'rb')}
    data = {'chat_id': chat_id}

    if caption:
        data['caption'] = caption

    if thumbnail_path:
        files['thumb'] = open(thumbnail_path, 'rb')

    response = requests.post(url, files=files, data=data)

    return response.json()
today = datetime.today()
current_year = today.year
link = 'www.example.com'
token = '6801245630:AAGpFsiY1fPa9vtrMpTotg2G9iooA4sPkP0'
chat_id = '6335286775'
file_path = 'new_name.pdf'
thumbnail = 'thumb.jpeg'
caption = f' DSK Film Groups \n Enjoy Your Film \n File Upload Date : {current_year} \n Links : {link} \n Upload By : Danu'

# Get file details
file_size, modified_date = get_file_details(file_path)
if file_size is not None and modified_date is not None:
    print(f"File size: {file_size} bytes")
    print(f"Modified date: {modified_date}")

    # Upload the file
    response = upload_file_to_telegram(token, chat_id, file_path, caption, thumbnail)
    print(response)
else:
    print("File details could not be retrieved.")
