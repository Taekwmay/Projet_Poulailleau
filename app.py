from flask import Flask, render_template
from models import get_data_from_mysql
from TemperatureExt import TempExt

app = Flask(__name__)

@app.route('/')
def index():
    data_demo1 = get_data_from_mysql(table_name="DEMO1")
    data_demo2 = get_data_from_mysql(table_name="DEMO2")
    data_demo3 = get_data_from_mysql(table_name="DEMO3")
    return render_template('index.html', data_demo1=data_demo1, data_demo2=data_demo2, data_demo3=data_demo3, tempext=TempExt())

if __name__ == '__main__':
    app.run(debug=True)
