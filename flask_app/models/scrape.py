from flask import render_template, request
import requests
from flask_app import app
from flask_app.models import scrape

from bs4 import BeautifulSoup



url = 'https://www.skysports.com/premier-league-table'


def get_league_table(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    league_table = soup.find('table', class_='standing-table__table callfn')

    # array to store teams within dict
    tablelist = []

    # initial formatting for the final print out
    #print("Team                         Pl  W  D  L  F  A GD Pts")

    for team in league_table.find_all('tbody'):
        rows = team.find_all('tr')

        for row in rows:
            rank = row.find_all('td', class_='standing-table__cell')[0].text
            # the .text.strip(), is removed from version1, in order to use white space in formatting via if statements
            # note: this errors if printed directly, regarding integers, because .text was used
            pl_team = row.find(
                'td', class_='standing-table__cell standing-table__cell--name').text.strip()
            # this focus on the data attribute used for table making, likely from JQuery DataTables plug-in
            #pl_team = pl_team['data-long-name']
            games_played = row.find_all(
                'td', class_='standing-table__cell')[2].text
            games_won = row.find_all(
                'td', class_='standing-table__cell')[3].text
            games_drawn = row.find_all(
                'td', class_='standing-table__cell')[4].text
            games_lost = row.find_all(
                'td', class_='standing-table__cell')[5].text
            goals_for = row.find_all(
                'td', class_='standing-table__cell')[6].text
            goals_against = row.find_all(
                'td', class_='standing-table__cell')[7].text
            goal_diff = row.find_all(
                'td', class_='standing-table__cell')[8].text
            total_points = row.find_all(
                'td', class_='standing-table__cell')[9].text

            # create a dict, I want to export to csv and practice scraping for database/excel use.
            teaminleague = {
                'rank': rank,
                'pl_team': pl_team,
                'games_played': games_played,
                'games_won': games_won,
                'games_drawn': games_drawn,
                'games_lost': games_lost,
                'goals_for': goals_for,
                'goals_against': goals_against,
                'goal_diff': goal_diff,
                'total_points': total_points
            }
            tablelist.append(teaminleague)
    return tablelist