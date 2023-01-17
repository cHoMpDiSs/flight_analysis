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
db.init_app(app)
db.create_all()

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger

trigger = CronTrigger(hour='*/5')

from .functions import plotting
from .flight_data import update_flight_data, cut_off_delay

sched = BackgroundScheduler()
sched.add_job(update_flight_data, trigger)
sched.add_job(cut_off_delay, trigger)
sched.add_job(plotting, trigger)

sched.start()


    