from flask import Flask, render_template, request, jsonify, redirect
from scraper import plotting, panda
from run import *
from models import *

@app.route("/")
def home():
    flight_delays_usa = db.session.query(FlightDelaysUSA.number_of_delays, FlightDelaysUSA.day_recorded)
    flight_delays_ww = db.session.query(FlightDelaysWW.number_of_delays_ww, FlightDelaysWW.day_recorded)
    flight_cancellations_usa = db.session.query(FlightCancellationsUSA.number_of_cancellations_usa, FlightCancellationsUSA.day_recorded)
    flight_cancellations_ww = db.session.query(FlightCancellationsWW.number_of_cancellations_ww, FlightCancellationsWW.day_recorded)
    return render_template('index.html',data1=flight_delays_usa, data2=flight_delays_ww, data3=flight_cancellations_usa, data4=flight_cancellations_ww)

@app.route("/barplot")   
def scraper():   
    plotting()
    flight_delays_usa = db.session.query(FlightDelaysUSA.number_of_delays, FlightDelaysUSA.day_recorded)
    flight_delays_ww = db.session.query(FlightDelaysWW.number_of_delays_ww, FlightDelaysWW.day_recorded)
    flight_cancellations_usa = db.session.query(FlightCancellationsUSA.number_of_cancellations_usa, FlightCancellationsUSA.day_recorded)
    flight_cancellations_ww = db.session.query(FlightCancellationsWW.number_of_cancellations_ww, FlightCancellationsWW.day_recorded)
    return render_template('index.html',data1=flight_delays_usa, data2=flight_delays_ww, data3=flight_cancellations_usa, data4=flight_cancellations_ww)

@app.route("/pandas")
def plot():
    return panda()
    


