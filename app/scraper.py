import requests
import pandas as pd
import matplotlib.pyplot as plt
from pandas import *
from bs4 import BeautifulSoup
from app import db, models
import schedule
import time
from .models import *
from datetime import datetime, date, timedelta


def flight_scraper():
    url = "https://flightaware.com/live/cancelled/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    data = soup.find_all("h3")
    raw_delays  = data[1].text
    raw_usa = data[2].text
    raw_cancellations  = data[3].text 
    raw_cancellations_usa = data[4].text
    total_delays  = ''.join(ch for ch in raw_delays if ch.isdigit())
    total_usa = ''.join(ch for ch in raw_usa if ch.isdigit())
    total_cancellations  = ''.join(ch for ch in raw_cancellations if ch.isdigit()) 
    total_cancellations_usa = ''.join(ch for ch in raw_cancellations_usa if ch.isdigit())

    
    
    return total_delays, total_usa, total_cancellations, total_cancellations_usa 

def plotting():
   
  
    flight_delays_usa = FlightDelaysUSA.query.order_by(FlightDelaysUSA.day_recorded).first()
    flight_delays_ww = FlightDelaysWW.query.order_by(FlightDelaysWW.day_recorded).first()
    flight_cancellations_usa = FlightCancellationsUSA.query.order_by(FlightCancellationsUSA.day_recorded).first()
    flight_cancellations_ww = FlightCancellationsWW.query.order_by(FlightCancellationsWW.day_recorded).first()


    data ={ 'USA Cancellations': str(flight_cancellations_usa.number_of_cancellations_usa), 'World Cancellations': str(flight_cancellations_ww.number_of_cancellations_ww),'USA Delays': str(flight_delays_usa.number_of_delays), 'World Delays': str(flight_delays_ww.number_of_delays_ww)}

    areas = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (10, 10))

    
    plt.bar( areas, [int(x) for x in values], color ='maroon',
        width = 0.4)
   
    plt.xlabel("Flight Analysis")
    plt.ylabel("No. of flights affected")
    plt.title("Jordons Flight Analysis")
    plt.savefig('app/static/images/foo.png', dpi=150)
 
def panda():


    flight_delays_usa = FlightDelaysUSA.query.order_by(FlightDelaysUSA.day_recorded).first()
    flight_delays_ww = FlightDelaysWW.query.order_by(FlightDelaysWW.day_recorded).first()
    flight_cancellations_usa = FlightCancellationsUSA.query.order_by(FlightCancellationsUSA.day_recorded).first()
    flight_cancellations_ww = FlightCancellationsWW.query.order_by(FlightCancellationsWW.day_recorded).first()
    data = ({
        "Total Cancellations USA" : flight_cancellations_usa.number_of_cancellations_usa,
        "Total Cancellations World Wide" : flight_cancellations_ww.number_of_cancellations_ww,
        "Total Delays USA" : flight_delays_usa.number_of_delays,
        "Total Delays World Wide" : flight_delays_ww.number_of_delays_ww
        
        
        
    })
    data = [data] 
    df = pd.DataFrame(data)
    html = df.to_html()
    return html
