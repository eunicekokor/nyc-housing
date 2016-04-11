# 'get_data_from_quandl.py'
#
#   + parses csv of Zillow Neighborhoods
#   + fetches Zillow stats using Quandl API
#   + creates Flask app, and a REST API to poll

# libraries and tings
import config
import requests
import json
import csv
import Quandl

# get the api key from config
apiKey = config.apiKey

# parse the neighborhood codes csv
with open('hood_codes.csv', 'rb') as csvfile:
    hoodreader = csv.reader(csvfile, delimiter=',')
    for row in hoodreader:
        if row[1] == 'New York' and row[3] == 'New York':
            neighborhood = row[0]
            hood_code = row[-1].split("|")[1]
            print ( neighborhood + ': ' + hood_code)
