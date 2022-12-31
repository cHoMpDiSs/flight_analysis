from flask import Flask
from scraper import flight_scraper
app = Flask(__name__)

@app.route("/")
def hello_world():
    return flight_scraper()