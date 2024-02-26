from app import Flask, render_template
from models import get_data_from_mysql

app = Flask(__name__)

@app.route('/')
def index():
    data_demo1, data_demo2, data_demo3 = get_data_from_mysql()
    return render_template('index.html', data_demo1=data_demo1, data_demo2=data_demo2, data_demo3=data_demo3)

if __name__ == '__main__':
    app.run(debug=True)
