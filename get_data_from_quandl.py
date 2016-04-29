# 'get_data_from_quandl.py'
#
#   + parses csv of Zillow Neighborhoods
#   + fetches Zillow stats using Quandl API
#   + creates Flask app, and a REST API to poll

# libraries and tings
from Quandl.Quandl import DatasetNotFound
from pymongo import MongoClient
from datetime import datetime
import Quandl as Q
import numpy as np
import config
import csv
import sys

# connect & config the mongo store
client = MongoClient()
db = client['housing']

# create array for list of hoods
listOfHoods = []
errors = []
# get the api key from config
apiKey = config.apiKey

# parse the neighborhood codes csv
with open('hood_codes.csv', 'rb') as csvfile:

    hoodreader = csv.reader(csvfile, delimiter=',')

    # for each row in the csv, get the hood & code
    for row in hoodreader:

        # only get NYC neighborhoods
        if (row[1] == 'New York') and (row[3] == 'New York'):

            # add the neighborhood to listOfHoods
            neighborhood = row[0]
            hoodCode = row[-1].split("|")[1]
            listOfHoods.append( neighborhood )

            # create a mongo collection for the neighborhood
            collection = db[ str(neighborhood) ]

            # get data from Quandl (for one neighborhood)
            # https://www.quandl.com/data/ZILL/documentation/documentation
            quandlQuery = ('ZILL/N'+ hoodCode + '_A')
            try:
                data = Q.get(quandlQuery, authtoken = apiKey, returns='numpy')
            except DatasetNotFound:
                #print neighborhood, hoodCode
                continue

            for date, price in data:
                data_point = collection.insert_one({
                    "neighborhood": neighborhood,
                    "date" : date,
                    "year" : date.year,
                    "month": date.month,
                    "price": price,
                })
                #print ("neighborhood: " + neighborhood)
                #print ("date: " + str(date))
                #print ("Object Added.")
                #break  # do this for one obj.

            #break  # do this for one neighborhood
