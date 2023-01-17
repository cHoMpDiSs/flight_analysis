from flask import Flask, render_template, request, jsonify, redirect
from .models import *
from app import db, app
from .functions import panda, db_query

@app.route("/")
def home():
    flight_delays_usa, flight_delays_ww, flight_cancellations_usa, flight_cancellations_ww = db_query()
    return render_template('index.html',data1=flight_delays_usa, data2=flight_delays_ww, data3=flight_cancellations_usa, data4=flight_cancellations_ww)

@app.route("/pandas")
def plot():
    return panda()

