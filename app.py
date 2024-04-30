from flask import Flask, render_template, request
from models import get_data_from_mysql
from TemperatureExt import TempExt
import mysql.connector

app = Flask(__name__)

# Fonction pour se connecter à la base de données et mettre à jour le nom du capteur
def update_sensor_name(sensor_table, new_name):
    # Connexion à la base de données
    conn = mysql.connector.connect(
        host="localhost",
        user="mariadb",
        password="mariadb",
        database="mariadb"
    )
    cursor = conn.cursor()

    # Exécution de la requête de mise à jour
    sql = "UPDATE Sensors SET sensor_name = %s WHERE sensor_name = %s"
    cursor.execute(sql, (new_name, sensor_table))
    recup1 = "select sensor_name from Sensors where device_addr like 'd6:1c:bf:b7:76:62';"

    # Validation de la transaction et fermeture de la connexion
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = mysql.connector.connect(
        host="localhost",
        user="mariadb",
        password="mariadb",
        database="my_database"
    )
    cursor = conn.cursor()
    recup1="select sensor_name from Sensors where device_addr like 'd6:1c:bf:b7:76:62';"
    cursor.execute(sql)
    DEMO1 = cursor.fetchall()
    cursor.close()
    conn.close()
    data_demo1 = get_data_from_mysql(table_name="DEMO1")
    data_demo2 = get_data_from_mysql(table_name="DEMO2")
    data_demo3 = get_data_from_mysql(table_name="DEMO3")
    return render_template('index.html', data_demo1=data_demo1, data_demo2=data_demo2, data_demo3=data_demo3, DEMO1 = cursor.execute(recup1), tempext=round(TempExt(),2))

@app.route('/change_name')
def form_name():
    return render_template('change_name.html')

@app.route('/change_name', methods=['POST'])
def submit():
    sensor1 = request.form['sensor1']
    sensor2 = request.form['sensor2']
    sensor3 = request.form['sensor3']

    # Mise à jour des noms des capteurs dans la base de données
    update_sensor_name("DEMO1", sensor1)
    update_sensor_name("DEMO2", sensor2)
    update_sensor_name("DEMO3", sensor3)

    return "Noms des capteurs mis à jour avec succès!"

if __name__ == '__main__':
    app.run(host='192.168.233.153', debug=True)
