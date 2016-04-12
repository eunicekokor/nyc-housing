# 'get_data_from_quandl.py'
#
#   + parses csv of Zillow Neighborhoods
#   + fetches Zillow stats using Quandl API
#   + creates Flask app, and a REST API to poll

# libraries and tings
from pymongo import MongoClient
import Quandl as Q
import numpy as np
import datetime
import config
import csv
import sys

# connect & config the mongo store
client = MongoClient()
db = client['housing']

# create array for list of hoods
listOfHoods = []

# get the api key from config
apiKey = config.apiKey

# parse the neighborhood codes csv
with open('hood_codes.csv', 'rb') as csvfile:
    hoodreader = csv.reader(csvfile, delimiter=',')
    # for each row in the csv, get the hood & code
    for row in hoodreader:
        # only get NYC ameighborhoods
        if row[1] == 'New York' and row[3] == 'New York':
            # add the neighborhood to listOfHoods
            neighborhood = row[0]
            hoodCode = row[-1].split("|")[1]
            listOfHoods.append( neighborhood )

            # ping the Quandl api
            # https://www.quandl.com/data/ZILL/documentation/documentation
            quandlQuery = ('ZILL/N'+ hoodCode + '_A')
            data = Q.get(quandlQuery, authtoken = apiKey, \
                returns='numpy')
            print (data)
            sys.stdout.flush()
            break  # do this for one neighborhood
