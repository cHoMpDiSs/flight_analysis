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
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger

trigger = OrTrigger([CronTrigger(hour='5'),CronTrigger(hour='15'),CronTrigger(hour='20')])

sched = BackgroundScheduler()
sched.add_job(flight_data.update_flight_data, trigger)
sched.add_job(flight_data.cut_off_delay_usa, trigger)
sched.add_job(scraper.plotting, trigger)

sched.start()










