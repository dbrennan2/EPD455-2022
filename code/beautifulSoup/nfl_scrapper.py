from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import cpickle
# set the year of data we want
year = '2021'

# set the website from which we want to get the data
url = 'https://www.pro-football-reference.com/years/' + year + '/rushing.htm#rushing_and_receiving::rush_yds'

# get the entire html code from the url
req = requests.get(url).text
# parse the text to make it meaningful - and something that soup can work with
soup = BeautifulSoup(req, 'lxml')

# create a dictionary where the key will be the player name and
# the elements will be their stats

player_dict = {}

# find the tag table
table = soup.find('table')


# find all the rows in the table using the tr tag
rows = table.find_all('tr')
for row in rows:
    # get the player, the players rush attempts and the rush yards
    player = row.find('td', {'data-stat':'player'})
    rush_attempts = row.find('td', {'data-stat':'rush_att'})
    rush_yards = row.find('td', {'data-stat':'rush_yds'})
    yards_per_attempt = row.find('td', {'data-stat':'rush_yds_per_att'})
    # Some rows are empty, so make sure that player is not none
    if player:
        player = player.text
        rush_attempts = float(rush_attempts.text)
        rush_yards = float(rush_yards.text)
        yards_per_attempt = float(yards_per_attempt.text)
        player_dict[player] = {'att' : rush_attempts, 'yds' : rush_yards, 'yds/att' : yards_per_attempt}




data = pd.DataFrame.from_dict(player_dict,orient = 'index')
print(data)

