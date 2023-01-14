import requests
import pandas as pd
import matplotlib.pyplot as plt
from pandas import *
from bs4 import BeautifulSoup
import schedule
import time
from models import *
from datetime import datetime, date, timedelta
from sqlalchemy import desc

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
   
    flight_delays_usa = FlightDelaysUSA.query.order_by(desc(FlightDelaysUSA.day_recorded)).limit(1).all()
    flight_delays_ww = FlightDelaysWW.query.order_by(desc(FlightDelaysWW.day_recorded)).limit(1).all()
    flight_cancellations_usa = FlightCancellationsUSA.query.order_by(desc(FlightCancellationsUSA.day_recorded)).limit(1).all()
    flight_cancellations_ww = FlightCancellationsWW.query.order_by(desc(FlightCancellationsWW.day_recorded)).limit(1).all()
  
    data ={ 'USA Cancellations': str(flight_cancellations_usa[0].number_of_cancellations_usa), 'World Cancellations': str(flight_cancellations_ww[0].number_of_cancellations_ww),'USA Delays': str(flight_delays_usa[0].number_of_delays), 'World Delays': str(flight_delays_ww[0].number_of_delays_ww)}

    areas = list(data.keys())
    values = list(data.values())
    
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, int(y[i]), int(y[i]), ha = 'center')
                
    fig = plt.figure(figsize = (10, 10))
    plt.bar( areas, [int(x) for x in values], color ='maroon',
        width = 0.4)
    addlabels(areas, values)
    plt.xlabel("Flight Analysis")
    plt.ylabel("No. of flights affected")
    plt.title("Jordons Flight Analysis")
    plt.savefig('app/static/images/foo.png', dpi=150)
 
def panda():

    flight_delays_usa = FlightDelaysUSA.query.order_by(desc(FlightDelaysUSA.day_recorded)).limit(1).all()
    flight_delays_ww = FlightDelaysWW.query.order_by(desc(FlightDelaysWW.day_recorded)).limit(1).all()
    flight_cancellations_usa = FlightCancellationsUSA.query.order_by(desc(FlightCancellationsUSA.day_recorded)).limit(1).all()
    flight_cancellations_ww = FlightCancellationsWW.query.order_by(desc(FlightCancellationsWW.day_recorded)).limit(1).all()
    
    data = ({
        "Total Delays USA" : flight_delays_usa[0].number_of_delays,
        "Total Delays World Wide" : flight_delays_ww[0].number_of_delays_ww,
        "Total Cancellations USA" : flight_cancellations_usa[0].number_of_cancellations_usa,
        "Total Cancellations World Wide" : flight_cancellations_ww[0].number_of_cancellations_ww  
    })
    data = [data] 
    df = pd.DataFrame(data)
    html = df.to_html()
    return html

