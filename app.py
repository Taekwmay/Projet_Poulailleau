from flask import Flask, render_template
from models import get_data_from_mysql
from TemperatureExt import TempExt

app = Flask(__name__)

@app.route('/')
def index():
    data_demo1 = get_data_from_mysql(table_name="DEMO1")
    data_demo2 = get_data_from_mysql(table_name="DEMO2")
    data_demo3 = get_data_from_mysql(table_name="DEMO3")
    return render_template('index.html', data_demo1=data_demo1, data_demo2=data_demo2, data_demo3=data_demo3, tempext=round(TempExt(),2))

    name_sensor1 = SensorInit(device_addr, sensor_name)
    name_sensor2 = SensorInit(device_addr, sensor_name)
    name_sensor3 = SensorInit(device_addr, sensor_name)
    return render_template('index.html',

if __name__ == '__main__':
    app.run(debug=True)
