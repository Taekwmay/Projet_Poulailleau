from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
from models import get_data_from_mysql
from TemperatureExt import TempExt
import mysql.connector
import smtplib
from email.mime.text import MIMEText
import time


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.example.com'  # Serveur SMTP
app.config['MAIL_PORT'] = 465  # Port du serveur SMTP (SSL)
app.config['MAIL_USERNAME'] = 'your-email@example.com'  # Adresse e-mail
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Mot de passe de l'adresse e-mail
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Fonction pour se connecter à la base de données et mettre à jour le nom du capteur
def update_sensor_name(sensor_mac, new_name):
    # Connexion à la base de données
    conn = mysql.connector.connect(
        host="localhost",
        user="mariadb",
        password="mariadb",
        database="mariadb"
    )
    cursor = conn.cursor()

    # Exécution de la requête de mise à jour
    sql = "UPDATE Sensors SET sensor_name = %s WHERE device_addr = %s"
    cursor.execute(sql, (new_name, sensor_mac))

    # Validation de la transaction et fermeture de la connexion
    conn.commit()
    conn.close()

def recup(mac):
    # Connexion à la base de données
    conn = mysql.connector.connect(
        host="localhost",
        user="mariadb",
        password="mariadb",
        database="mariadb"
    )
    cursor = conn.cursor()

    # Exécution de la requête de mise à jour
    recup1 = "select sensor_name from Sensors where device_addr like %s;"
    cursor.execute(recup1, (mac,))
    recup2 = cursor.fetchone()[0]

    conn.close()
    return recup2

@app.route('/')
def index():
    data_demo1 = get_data_from_mysql(table_name="DEMO1")
    data_demo2 = get_data_from_mysql(table_name="DEMO2")
    data_demo3 = get_data_from_mysql(table_name="DEMO3")
    return render_template('index.html', data_demo1=data_demo1, data_demo2=data_demo2, data_demo3=data_demo3, DEMO1 = recup('d6:1c:bf:b7:76:62'), DEMO2 = recup('d6:c6:c7:39:a2:e8'),DEMO3 = recup('d7:ef:13:27:15:29'), tempext=round(TempExt(),2))

@app.route('/change_name')
def form_name():
    return render_template('change_name.html')

@app.route('/change_name', methods=['POST'])
def submit():
    sensor1 = request.form['sensor1']
    sensor2 = request.form['sensor2']
    sensor3 = request.form['sensor3']

    # Mise à jour des noms des capteurs dans la base de données
    update_sensor_name("d6:1c:bf:b7:76:62", sensor1)
    update_sensor_name("d6:c6:c7:39:a2:e8", sensor2)
    update_sensor_name("d7:ef:13:27:15:29", sensor3)

    return redirect('/')

@app.route('/graph')
def graph():
    data_demo1 = get_data_from_mysql(table_name="DEMO1")
    data_demo2 = get_data_from_mysql(table_name="DEMO2")
    data_demo3 = get_data_from_mysql(table_name="DEMO3")
    return jsonify({
        'demo1': data_demo1,
        'demo2': data_demo2,
        'demo3': data_demo3})

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
        send_alert_email("température", "température supérieur à 25", "stationmeteo@meteo.com", "client@meteo.com")
    if humidity > hum_seuil:
        send_alert_email("humidité", "humidité supérieur à 30%", "stationmeteo@meteo.com", "client@meteo.com")

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

# Appeler la fonction check_seuil() à une fréquence constante
while True:
    check_seuil()
    time.sleep(freq)

if __name__ == '__main__':
    app.run(host='192.168.233.153', debug=True)