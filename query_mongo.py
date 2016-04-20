# 'query_mongo.py'
#
# TO DO
#   + loop through DB, get all hoods
#   + for each hood: get all data points from 2015-2010
#   + group by 6 month intervals or 1 year
#       - if 1 year, expand data points to 2015-2009
#   + calculate percent change data for each year
#       - % inc. = [(new-old)/(old)] * 100%
#   + order in list and get top 40%.
#   + get the neighborhood names [DONE]
#   + make visualisation [optional]

# libraries and tings
from pymongo import MongoClient
from datetime import datetime
import sys

# connect & config the mongo store
client = MongoClient()
db = client['housing']

# create an array of the neighborhood names
hoodList = db.collection_names()

# iterate through each neighborhood and get all data
for hood in hoodList:
    print ( db.get_collection( hood ).find_one() )
    break; # do this once

# DATA STRUCT
#data_point = collection.insert_one({
#    "neighborhood": neighborhood,
#    "date" : date,
#    "year" : date.year,
#    "month": date.month,
#    "price": price,
#})
