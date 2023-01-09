from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .secret import *

app = Flask(__name__)



# this is where we connect to the database


app.config['SQLALCHEMY_DATABASE_URI'] = SECRET_STRING
app.config["SQLALCHEMY_ECHO"] = True
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import views, models, flight_data
db.init_app(app)
db.create_all()
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()
sched.add_job(func=flight_data.update_flight_data, trigger='interval',days=1)
sched.add_job(func=flight_data.cut_off_delay_usa, trigger='interval',days=1)
sched.start()










