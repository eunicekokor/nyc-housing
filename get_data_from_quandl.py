# 'get_data_from_quandl.py'
#
#   + parses csv of Zillow Neighborhoods
#   + fetches Zillow stats using Quandl API
#   + creates Flask app, and a REST API to poll

# libraries and tings
import Quandl as Q
import config
import redis
import json
import time
import csv
import sys

# connect the redis store
store = redis.Redis(db=0)

# create array for list of hoods
listOfHoods = []

# get the api key from config
apiKey = config.apiKey

# parse the neighborhood codes csv
with open('hood_codes.csv', 'rb') as csvfile:
    hoodreader = csv.reader(csvfile, delimiter=',')
    # for each row in the csv, get the hood & code
    for row in hoodreader:
        # only get NYC neighborhoods
        if row[1] == 'New York' and row[3] == 'New York':
            # add the neighborhood to listOfHoods
            neighborhood = row[0]
            hoodCode = row[-1].split("|")[1]
            listOfHoods.append( neighborhood )

            # ping the Quandl api
            # https://www.quandl.com/data/ZILL/documentation/documentation
            #quandlQuery = ('ZILL/N'+ hoodCode + '_A')
            #data = Q.get(quandlQuery, authtoken=apiKey)
            #data.head()

            # add the pair to a redis store
            store.set(neighborhood, hoodCode)
