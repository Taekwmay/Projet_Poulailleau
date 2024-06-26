from flask import Flask, render_template, request, redirect
from models import get_data_from_mysql
from TemperatureExt import TempExt
import mysql.connector



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

if __name__ == '__main__':
    app.run(host='192.168.233.153', debug=True)