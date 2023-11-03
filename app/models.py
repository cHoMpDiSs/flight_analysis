from datetime import datetime
from app import db


class FlightDelaysUSA(db.Model):

    __tablename__='flight_delays_USA'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number_of_delays = db.Column(db.Integer, nullable=False)
    day_recorded = db.Column(db.DateTime, nullable=False)

    def __init__(self,number_of_delays, day_recorded):
        self.number_of_delays = number_of_delays
        self.day_recorded = day_recorded

    def __repr__(self):
        return f'FlightDelaysUSA("{self.number_of_delays}","{self.day_recorded}")'


class FlightDelaysWW(db.Model):

    __tablename__='flight_delays_WW'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number_of_delays_ww = db.Column(db.Integer, nullable=False)
    day_recorded = db.Column(db.DateTime, nullable=False)

    def __init__(self,number_of_delays_ww, day_recorded):
        self.number_of_delays_ww = number_of_delays_ww
        self.day_recorded = day_recorded

    def __repr__(self):
        return f'FlightDelaysWW("{self.number_of_delays_ww}","{self.day_recorded}")'

class FlightCancellationsUSA(db.Model):

    __tablename__='flight_cancellations_USA'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number_of_cancellations_usa = db.Column(db.Integer, nullable=False)
    day_recorded = db.Column(db.DateTime, nullable=False)

    def __init__(self,number_of_cancellations_usa, day_recorded):
        self.number_of_cancellations_usa = number_of_cancellations_usa
        self.day_recorded = day_recorded

    def __repr__(self):
        return f'FlightCancellationsUSA("{self.number_of_cancellations_usa}","{self.day_recorded}")'


class FlightCancellationsWW(db.Model):

    __tablename__='flight_cancellations_WW'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number_of_cancellations_ww = db.Column(db.Integer, nullable=False)
    day_recorded = db.Column(db.DateTime, nullable=False)

    def __init__(self,number_of_cancellations_ww, day_recorded):
        self.number_of_cancellations_ww = number_of_cancellations_ww
        self.day_recorded = day_recorded

    def __repr__(self):
        return f'FlightCancellationsWW("{self.number_of_cancellations_ww}","{self.day_recorded}")'
