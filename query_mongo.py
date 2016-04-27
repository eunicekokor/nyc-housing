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

# connect & config the mongo store
client = MongoClient()
store = client['housing']

# create an array of the neighborhood names
hoodList = store.collection_names()

# iterate through each neighborhood and get all data for 2010->2015
for hood in hoodList:

    dataPoints = store.get_collection(hood).find({"year": {"$gt": 2009}})

    # create a dict of years for each neighborhood
    dictOfYears = {}

    # for each datapoint, group by year
    for datapoint in dataPoints:
        # add the year to dict. of years
        print ( datapoint )
        break # just do one data point in the neighborhood
    break # do this once

# DATA STRUCT
#data_point = {
#    "neighborhood": neighborhood,
#    "date" : date,
#    "year" : date.year,
#    "month": date.month,
#    "price": price,
#}

# NEW DATA STRUCT
#data_point = {
#   "neighborhood": neighborhood,
#    "data": [
#       {"2010":year, "avgPrice":price},
#       {"2011":year, "avgPrice":price},
#    ]
#}
