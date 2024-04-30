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

@app.route('/change_name')
def form_name():
    return render_template('change_name.html')

@app.route('/change_name', methods=['POST'])
def submit():
    sensor1 = request.form['sensor1']
    sensor2 = request.form['sensor2']
    sensor3 = request.form['sensor3']

    # Faire ce que vous voulez avec les données ici, par exemple, les afficher
    print(f"Capteur 1: {sensor1}, MAC: {mac1}")
    print(f"Capteur 2: {sensor2}, MAC: {mac2}")
    print(f"Capteur 3: {sensor3}, MAC: {mac3}")

    # Vous pouvez également les enregistrer dans une base de données ou autre traitement nécessaire

    return "Données soumises avec succès!"
    
if __name__ == '__main__':
    app.run(host='192.168.233.153',debug=True)
