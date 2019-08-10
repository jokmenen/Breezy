from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    timer_data = "Jan 5, 2021 15:37:25"
    timer_name = "TIMER 1"
    return render_template('index.html', timer_name = timer_name, timer_data = timer_data)

if __name__ == '__main__':
    app.run()