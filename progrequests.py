import requests
import datetime
import csv
from io import StringIO

current_datetime = datetime.datetime.now()
formatted_date = current_datetime.strftime("%Y%m%d%H")
csv_date = datetime.datetime(year=current_datetime.year, month=current_datetime.month, day=current_datetime.day, hour=current_datetime.hour // 3 * 3, minute=0)

while True:
    formatted_csv_date = csv_date.strftime("%Y%m%d")
    formatted_csv_hour = csv_date.strftime("%H")
    url = f"https://donneespubliques.meteofrance.fr/?fond=donnee_libre&prefixe=Txt%2FSynop%2Fsynop&extension=csv&date={formatted_csv_date}&reseau={formatted_csv_hour}.csv"
    response = requests.get(url)
    if response.ok:
        data = response.content.decode('utf-8')  # Décode les octets en une chaîne de caractères
        csvfile = StringIO(data)  # Utilise StringIO pour traiter les données comme un fichier texte
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            if row[0] == "07510":
                temperature_kelvin = float(row[7])  # Température en Kelvin
                temperature_celsius = temperature_kelvin - 273.15  # Conversion en Celsius
                print(temperature_kelvin)
                print(temperature_celsius)
                #print(f"Temperature : {temperature_celsius:.2f} °C")
        break
    else:
        print("erreur")
        break
