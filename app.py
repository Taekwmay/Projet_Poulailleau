from flask import Flask, render_template, request
from models import get_data_from_mysql
from TemperatureExt import TempExt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from my_models import Sensor, Base

app = Flask(__name__)

# Connexion à la base de données
engine = create_engine('mysql+pymysql://mariadb:mariadb@localhost/my_database')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

def update_sensor_name(sensor_table, new_name):
    session = DBSession()
    sensor = session.query(Sensor).filter_by(sensor_name=sensor_table).first()
    sensor.sensor_name = new_name
    session.commit()
    session.close()


@app.route('/')
def index():
    data_demo1 = get_data_from_mysql(table_name="DEMO1")
    data_demo2 = get_data_from_mysql(table_name="DEMO2")
    data_demo3 = get_data_from_mysql(table_name="DEMO3")
    return render_template('index.html', data_demo1=data_demo1, data_demo2=data_demo2, data_demo3=data_demo3, tempext=round(TempExt(),2))

@app.route('/change_name')
def form_name():
    return render_template('change_name.html')

@app.route('/change_name', methods=['POST'])
def submit():
    sensor1 = request.form['sensor1']
    sensor2 = request.form['sensor2']
    sensor3 = request.form['sensor3']
    
    update_sensor_name("DEMO1", sensor1)
    update_sensor_name("DEMO2", sensor2)
    update_sensor_name("DEMO3", sensor3)

    # Vous pouvez également les enregistrer dans une base de données ou autre traitement nécessaire

    return "Données soumises avec succès!"
    
if __name__ == '__main__':
    app.run(host='192.168.233.153',debug=True)
