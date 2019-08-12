from flask_sqlalchemy import SQLAlchemy
import os

DB_NAME = "timer3.db"



def configure_database(db):

    class Event(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), unique=True, nullable=False)
        date = db.Column(db.String(120), unique=False, nullable=False)

        def __repr__(self):
            return '<Name %r>' % self.name


    print("DB Exists:", os.path.exists("/{}/{}".format(os.getcwd(), DB_NAME)))
    if not os.path.exists("/{}/{}".format(os.getcwd(), DB_NAME)):

            print("Creating new DB")
            db.create_all()# Create new DB if it doesn't exist yet
            return Event
    else:
            print("Configing DB")
            return Event # Else just config itumn(db.String(120), unique=True, nullable=False)