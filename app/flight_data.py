from datetime import datetime, date, timedelta
from .functions import flight_scraper
from app import db
from .models import *


def update_flight_data():
    todays_date = datetime.now()
    total_ww, total_usa, total_cancellations_ww, total_cancellations_usa = flight_scraper()   
    
    flights_usa = FlightDelaysUSA(number_of_delays=total_usa,day_recorded=todays_date)
    db.session.add(flights_usa)
    
    flights_ww = FlightDelaysWW(number_of_delays_ww=total_ww,day_recorded=todays_date)
    db.session.add(flights_ww)    
    
    flight_cancel_usa = FlightCancellationsUSA(number_of_cancellations_usa=total_cancellations_usa,day_recorded=todays_date)
    db.session.add(flight_cancel_usa)
    
    flight_cancel_ww = FlightCancellationsWW(number_of_cancellations_ww=total_cancellations_ww,day_recorded=todays_date)
    db.session.add(flight_cancel_ww)
    db.session.commit()  
     

def cut_off_delay():   
    todays_date = datetime.now()
    cutoff = (datetime.now() - timedelta(days=2, hours=-1))
    FlightDelaysUSA.query.filter(FlightDelaysUSA.day_recorded<=cutoff).delete()  
    FlightDelaysWW.query.filter(FlightDelaysWW.day_recorded<=cutoff).delete()
    FlightCancellationsUSA.query.filter(FlightCancellationsUSA.day_recorded<=cutoff).delete()  
    FlightCancellationsWW.query.filter(FlightCancellationsWW.day_recorded<=cutoff).delete()
    db.session.commit()
   

