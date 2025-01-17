from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

import db
#from db import Event
import os


app = Flask(__name__)

#DB STUFF
# db_name = "timer3.db"
# print('sqlite:////{}/{}'.format(os.getcwd(),db_name))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}/{}'.format(os.getcwd(), db.DB_NAME)
alchemy = SQLAlchemy(app)
Event = db.configure_database(alchemy)



#print("timerdata",timerdata, timerdata.date)
def create_new_timer(name,date):
    new_timer = Event(name = name, date = date)
    alchemy.session.add(new_timer)
    alchemy.session.commit()

@app.route('/')
def hello_world():
    timerdata = Event.query.all()
    timershead = timerdata[:5]
    timersbot = timerdata[5:]
    timer_data = "Jan 5, 2021 15:37:25"
    timer_name = "TIMER 1"
    return render_template('index.html', timershead = timershead, timersbot = timersbot)

timer_add_route = '/add'
@app.route(timer_add_route, methods = ['POST','GET'])
def new_timer():
    if request.method == 'POST':


        result = request.form.to_dict()
        try:
            date = datetime.strptime(result["date"], '%Y-%m-%d')
            time = datetime.strptime(result["time"], '%H:%M')
            print(time)
            dt = datetime.combine(date.date(),time.time())

            create_new_timer(str(result["name"]),datetime.strftime(dt, "%b %d, %Y %H:%M:00"))
        except Exception as e:
            print(e)
            return "Something went wrong"
        print("result:",result)
        return hello_world()
    return render_template('add_timer.html', route=timer_add_route)

@app.route('/fill')
def debug_fill():

    for x in range(11):
        x += 1
        name = "Timer {}".format(x)
        date =  'Feb {}, 2222 00:15:00'.format(x)
        print(name,date)
        create_new_timer(name,date)
    return hello_world()

if __name__ == '__main__':
    app.run()