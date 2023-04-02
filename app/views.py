from flask import Flask, render_template, send_file
from .models import *
from app import db, app
from .functions import panda, db_query, plotting, flight_numbers

@app.route("/")
def home():
    flight_delays_usa, flight_delays_ww, flight_cancellations_usa, flight_cancellations_ww = db_query()
    usa_d = str(flight_delays_usa[0].day_recorded)[:11]
    usa_c = str(flight_cancellations_usa[0].day_recorded)[:11]
    ww_d = str(flight_delays_ww[0].day_recorded)[:11]
    ww_c = str(flight_cancellations_ww[0].day_recorded)[:11]





    return render_template('index.html',data1=flight_delays_usa, data2=flight_delays_ww, data3=flight_cancellations_usa,
     data4=flight_cancellations_ww, ud=usa_d, uc=usa_c, wd=ww_d, wc=ww_c)

@app.route("/pandas")
def pandas():
    return panda()

@app.route("/static/images/foo.png")
def plot():
    plotting()
    return send_file('static/images/foo.png',
    mimetype='image/png',
    attachment_filename='foo.png'), 200

@app.route("/test")
def test():
    flight_numbers()
