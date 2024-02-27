import requests
import datetime
import csv
from io import BytesIO

current_datetime = datetime.datetime.now()
formatted_date = current_datetime.strftime("%Y%m%d%H")
csv_date = datetime.datetime(year = current_datetime.year, month = current_datetime.month, day = current_datetime.day, hour = current_datetime.hour//3*3, minute = 0)

while True :
    formated_csv_date = csv_date.strftime("%Y%m%d%H")
    url = f"https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/synop.{formated_csv_date}.csv"
    data = requests.get(url)
    if data :
        csvfile = BytesIO(data.content)
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            if row[0]== "07510" :
                print(row[7])
        break
    else :
        break
