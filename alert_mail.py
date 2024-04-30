import time
import mysql.connector
import smtplib
from email.mime.text import MIMEText

def send_alert_email(subject, body, sender_email, receiver_email):
    # Création du message
    message = MIMEText(body)
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Connexion au serveur SMTP
    with smtplib.SMTP("smtp.freesmtpservers.com",25) as server:
        server.sendmail(sender_email, receiver_email, message.as_string())

# Route pour vérifier les seuils et envoyer un e-mail d'alerte si nécessaire

def check_seuil():
    conn = mysql.connector.connect(
        host="localhost",
        user="mariadb",
        password="mariadb",
        database="mariadb"
    )
    cursor = conn.cursor()

    # Récupération des seuils d'alerte de température et d'humidité depuis la table Param
    cursor.execute("SELECT seuil_temp, seuil_hum FROM Param")
    temp_seuil, hum_seuil = cursor.fetchone()

    # Récupération de la température actuelle
    cursor.execute("""
        SELECT combined_tables.temperature 
        FROM (SELECT * FROM DEMO1 UNION ALL SELECT * FROM DEMO2 UNION ALL SELECT * FROM DEMO3) AS combined_tables 
        ORDER BY combined_tables.timestamp DESC 
        LIMIT 1
    """)
    temperature = cursor.fetchone()[0]

    # Récupération de l'humidité actuelle
    cursor.execute("""
        SELECT combined_tables.humidity 
        FROM (SELECT * FROM DEMO1 UNION ALL SELECT * FROM DEMO2 UNION ALL SELECT * FROM DEMO3) AS combined_tables 
        ORDER BY combined_tables.timestamp DESC 
        LIMIT 1
    """)
    humidity = cursor.fetchone()[0]

    # Vérification des seuils et envoi d'un e-mail d'alerte si nécessaire
    if temperature > temp_seuil:
        send_alert_email("température", "temperature superieur a 25", "stationmeteo@meteo.com", "client@meteo.com")
    if humidity > hum_seuil:
        send_alert_email("humidite", "humidite superieur a 30%", "stationmeteo@meteo.com", "client@meteo.com")

    # Fermeture de la connexion à la base de données
    cursor.close()
    conn.close()

    return "Vérification des seuils effectuée"


conn = mysql.connector.connect(
    host="localhost",
    user="mariadb",
    password="mariadb",
    database="mariadb"
)
cursor = conn.cursor()

# Récupération de la fréquence depuis la table Param
recup_freq = "SELECT freq FROM Param;"
cursor.execute(recup_freq)
freq = cursor.fetchone()[0]

while True:
    check_seuil()
    time.sleep(freq)