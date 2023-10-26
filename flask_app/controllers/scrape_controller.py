from flask import render_template, request
import requests
from flask_app import app
from flask_app.models import scrape

from bs4 import BeautifulSoup

url = 'https://www.skysports.com/premier-league-table'


@app.route('/')
def index():

    data = scrape.get_league_table(url)




    return render_template('index.html', data = data)