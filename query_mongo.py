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
import datetime

# connect & config the mongo store
client = MongoClient()
store = client['housing']

# create a mongo storee for each interval

# create an array of the neighborhood names
hoodList = store.collection_names()

# create a dict of years for each neighborhood
arrayOfHoods = []

# iterate through each neighborhood and get all data for 2010->2015
for hood in hoodList:

    dataPoints = store.get_collection(hood).find({"year": {"$gt": 2009}})

    # create a temp obj.
    temp = {}
    temp["data"] = []
    temp["neighborhood"] = hood

    # for each datapoint, add tuple to hood data
    for datapoint in dataPoints:

        date = datapoint["date"]
        price = datapoint["price"]

        temp["data"].append( (date, price) )

    # append the temp nhood obj to the glbl array
    arrayOfHoods.append( temp )

# calculations for 3-month period
for h in arrayOfHoods:
    data = h["data"]
    for d in range(0, len(data)-3, 3):
        data1 = data[d]  # start
        data2 = data[d+3] # end
        delta_price =  data2[1]-data1[1]
        print h["neighborhood"],data1[0],data2[0],delta_price
    break


# calculations for 6-month period
for h in arrayOfHoods:
    data = h["data"]
    for d in range(0, len(data)-6, 6):
        data1 = data[d]  # start
        data2 = data[d+6] # end
        delta_price =  data2[1]-data1[1]
        print h["neighborhood"],data1[0],data2[0],delta_price
    break


# calculations for 1 year period
for h in arrayOfHoods:
    data = h["data"]
    for d in range(0, len(data)-12, 12):
        data1 = data[d]  # start
        data2 = data[d+12] # end
        delta_price =  data2[1]-data1[1]
        print h["neighborhood"],data1[0],data2[0],delta_price
    break


# calculations for 2 year period
for h in arrayOfHoods:
    data = h["data"]
    for d in range(0, len(data)-24, 24):
        data1 = data[d]  # start
        data2 = data[d+24] # end
        delta_price =  data2[1]-data1[1]
        print h["neighborhood"],data1[0],data2[0],delta_price
    break

