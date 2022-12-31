import requests
import pandas as pd
from pandas import *
from bs4 import BeautifulSoup


def flight_scraper():
    url = "https://flightaware.com/live/cancelled/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    data = soup.find_all("h3")
    raw_delays,  = data[1].text
    raw_usa = data[2].text
    raw_cancellations,  = data[3].text 
    raw_cancellations_usa = data[4].text
    total_delays,  = ''.join(ch for ch in raw_delays if ch.isdigit())
    total_usa = ''.join(ch for ch in raw_usa if ch.isdigit())
    total_cancellations,  = ''.join(ch for ch in raw_cancellations if ch.isdigit()) 
    total_cancellations_usa = ''.join(ch for ch in raw_cancellations_usa if ch.isdigit())

    data = ({
        "Total Delays" : total_delays,
        "Total USA" : total_usa,
        "Total Cancellations" : total_cancellations,
        "Total Cancellations USA" : total_cancellations_usa
    })
    data = [data] 
    df = pd.DataFrame(data)
    html = df.to_html()
    return html