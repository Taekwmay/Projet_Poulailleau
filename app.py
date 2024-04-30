from flask import Flask, render_template
from models import get_data_from_mysql
from TemperatureExt import TempExt
import requests

app = Flask(__name__)

@app.route('/')
def index():
    data_demo1 = get_data_from_mysql(table_name="DEMO1")
    data_demo2 = get_data_from_mysql(table_name="DEMO2")
    data_demo3 = get_data_from_mysql(table_name="DEMO3")
    return render_template('index.html', data_demo1=data_demo1, data_demo2=data_demo2, data_demo3=data_demo3, tempext=round(TempExt(),2))
    
@app.route('/update', methods=['POST'])
def update_sensor_names():
    global sensors
    new_sensor_names = request.form.getlist(SensorInit(device_addr, sensor_name))

    # Met à jour les noms des capteurs avec les nouveaux noms
    for i in range(len(sensors)):
        sensors[i]['sensor_name'] = new_sensor_names[i]

    # Redirige vers la page d'accueil après la mise à jour
    return render_template('index.html', data_demo1=data_demo1, data_demo2=data_demo2, data_demo3=data_demo3, tempext=round(TempExt(),2), sensors=sensors)
if __name__ == '__main__':
    app.run(debug=True)
